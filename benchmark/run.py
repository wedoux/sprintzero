"""Benchmark runner: scores the ux-research-qa skill (and, later, the app)
against the seeded cases in benchmark/cases/.

  --target skill --skill-path <checkout>   Build the system prompt from the
                                            skill's SKILL.md + references/ +
                                            templates/, send each case as the
                                            user message.
  --target app                             Stub. R0 scope is the skill only.
  --dry-run                                Canned, deterministic readout, no
                                            network call - same convention as
                                            _probe_qa_gate.py / _probe_intake.py.
  (live, no --dry-run)                     Uses model_client.stream_text and
                                            credentials.resolve, the same call
                                            path app.py uses, so a result here
                                            means what an app result would mean.

Two independent scores, because label detection and actual judgement are
different failure modes:

  CK-ID score       Regex-extracts "<CODE> ... FIRES|CLEAR|NOT RUN" from the
                     readout for every CK-0x and P-0x code, and compares
                     against each case's front matter. Before R1 exists the
                     skill emits no CK codes at all, so every CK is recorded
                     "not detected" for v1.0 - that gap, not a score, is the
                     baseline's point. A check reporting CLEAR where the case
                     declared checks_expected_not_run is scored as a FALSE
                     PASS, not a miss: fail-closed is a correctness property
                     (spec principle 1), so a quiet pass on missing input is
                     worse than an honest NOT RUN.

  Strength score     Label-independent: parses the STRONG/UNCERTAIN/WEAK (or
                     N/A, for an explicitly-labelled hypothesis) verdict on
                     the claim under review, and checks it against that
                     case's own `expected_strength` gold label - not a
                     filename-inferred rule. R0.1 used "fire passes if not
                     STRONG, clear passes if not WEAK"; that rule scored a
                     correctly-caught flaw as a failure whenever a "clear"
                     case turned out to deserve WEAK for a real reason (see
                     benchmark/RESULTS.md, R0.2). NR cases aren't scored on
                     this axis at all (`expected_strength: []`) - they test
                     check applicability, not verdict quality.

                     Every case file must declare `expected_strength` and
                     `claim_honest` before run.py will score it at all
                     (checked by validate_gold_labels, enforced outside
                     --dry-run). From R1 onward, gold labels are written
                     before a case is run, not after reading what v1 said -
                     see the R0.2 note in RESULTS.md.

  Claim score        R1: parses "Claim matches its evidence: Yes|No" and checks
                     it against the case's `claim_honest` gold label. Scored on
                     every case, NR included - honesty of the claim doesn't
                     depend on whether a check could run. v1.0 never prints
                     the line, so its baseline here is "not detected" across
                     the board; the absolute R1 number is the one that means
                     something.

Parsing fails closed, the same way the checks must: a status word only counts
in capitals (prose like "it's not clear" isn't a CLEAR), a template line
copied back unfilled ("STRONG / UNCERTAIN / WEAK", "Yes / No") isn't read as
its first option, and when a readout reports one check more than once the
most severe result wins (FIRES, then NOT RUN, then CLEAR) - a later CLEAR
never overwrites an earlier FIRES.

Raw readouts are saved to benchmark/runs/<date>-<target>-<version>/<case-id>.md
(dry-run included) - without them a run can't be re-scored or audited later
against a scoring-logic change. If that directory already exists the run gets
a -2, -3... suffix instead, and a readout file is never overwritten: two runs
of the same commit on the same day used to share a directory, so the second
silently replaced the first's evidence. --rewritten/--source-run re-scores unchanged
cases from an earlier run's saved readouts (no new API calls) and only calls
the model live for the cases named in --rewritten; --source-run alone re-scores
every case and calls nothing.

Cost note: token counts here are an estimate (chars/4 vs words*1.35, the
larger of the two), not a measurement - there is no usage.* to read until a
live call actually returns one. Treat the printed figure as a ceiling to
decide whether to proceed, not a promise.
"""
import argparse
import datetime
import os
import re
import subprocess
import sys
from pathlib import Path

from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import credentials
import model_client

# Same convention as app.py: a .env at the repo root works in development.
# Without this, credentials.resolve() would fall through to the macOS
# Keychain, whose GUI authorization prompt a non-interactive run can never
# answer - that's a hang, not a failure, and it costs nothing to hit because
# no request has gone out yet. Load the obvious source first.
load_dotenv()

BENCH_DIR = Path(__file__).resolve().parent
CASES_DIR = BENCH_DIR / "cases"
RUNS_DIR = BENCH_DIR / "runs"
RESULTS_PATH = BENCH_DIR / "RESULTS.md"

# Confirmed 2026-10-26, Opus tier. Re-check before trusting this far into the
# future - pricing is not something this codebase has had reason to track.
INPUT_RATE_PER_MTOK = 5.0
OUTPUT_RATE_PER_MTOK = 25.0
LIVE_RUN_ASK_THRESHOLD_USD = 5.0  # approved to run unattended under this; ask above it
# v1.0 readouts ran ~750 tokens; v2 adds declared upstream, six CK rows, four
# question groups and a decision boundary. Over-estimating is the safe side.
ASSUMED_OUTPUT_TOKENS_PER_CASE = 1500


def _parse_front_matter(raw):
    """Hand-rolled, deliberately not a YAML library: every case's front matter
    is flat scalars plus one bracketed list syntax, and that is the entire
    format this needs to support."""
    front = {}
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        key, _, val = line.partition(":")
        key, val = key.strip(), val.strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            front[key] = [v.strip() for v in inner.split(",") if v.strip()]
        elif val.lower() in ("true", "false"):
            front[key] = val.lower() == "true"
        else:
            front[key] = val
    front.setdefault("checks_expected_to_fire", [])
    front.setdefault("checks_expected_clear", [])
    front.setdefault("checks_expected_not_run", [])
    return front


def load_case(path):
    text = path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError(f"{path}: missing '---' front matter block")
    return _parse_front_matter(m.group(1)), m.group(2).strip()


def load_all_cases():
    return [load_case(p) for p in sorted(CASES_DIR.glob("*.md"))]


def build_skill_system_prompt(skill_path):
    skill_path = Path(skill_path)
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        raise FileNotFoundError(f"{skill_md} not found - is --skill-path correct?")
    parts = [skill_md.read_text()]
    for d in ("references", "templates"):
        for p in sorted((skill_path / d).glob("*.md")):
            parts.append(p.read_text())
    return "\n\n---\n\n".join(parts)


def get_skill_version(skill_path):
    """The commit, not the path - a path says nothing about what was tested
    once the checkout moves on to its next commit."""
    try:
        out = subprocess.run(
            ["git", "-C", str(skill_path), "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, timeout=10, check=True,
        )
        return out.stdout.strip()
    except Exception:
        return f"{Path(skill_path).name}-not-a-git-checkout"


def estimate_tokens(text):
    return max(len(text) // 4, int(len(text.split()) * 1.35))


def estimate_cost(system_prompt, cases):
    sys_tokens = estimate_tokens(system_prompt)
    input_tokens = sum(sys_tokens + estimate_tokens(body) for _, body in cases)
    output_tokens = ASSUMED_OUTPUT_TOKENS_PER_CASE * len(cases)
    cost = (input_tokens / 1_000_000 * INPUT_RATE_PER_MTOK
            + output_tokens / 1_000_000 * OUTPUT_RATE_PER_MTOK)
    return input_tokens, output_tokens, cost


def print_cost_estimate(system_prompt, cases):
    input_tokens, output_tokens, cost = estimate_cost(system_prompt, cases)
    print(f"Cases: {len(cases)}")
    print(f"Estimated input tokens:  ~{input_tokens:,}")
    print(f"Estimated output tokens: ~{output_tokens:,} "
          f"(assumed {ASSUMED_OUTPUT_TOKENS_PER_CASE}/case)")
    print(f"Estimated cost @ ${INPUT_RATE_PER_MTOK:.0f}/MTok in, "
          f"${OUTPUT_RATE_PER_MTOK:.0f}/MTok out: ~${cost:.2f}")
    return cost


def dry_run_readout(front):
    """Deterministic stub - exercises the parse/score path with no network
    call. Picks a strength value from the case's own expected_strength (or
    N/A for a declared hypothesis) so a clean dry run stays clean regardless
    of which tiers a given case accepts. Uses .get, not [], so a draft case
    with no gold labels yet can still be dry-run while it's being written -
    only a live/rescore run enforces validate_gold_labels."""
    if front.get("is_hypothesis"):
        strength_line = "N/A"
    else:
        expected = front.get("expected_strength") or ["WEAK"]
        strength_line = expected[0]
    claim_line = "Yes" if front.get("claim_honest") == "yes" else "No"
    lines = ["## Finding: (dry-run stub)", "", f"**Evidence strength: {strength_line}**", "",
             f"**Claim matches its evidence:** {claim_line} — (stub)", ""]
    for ck in front["checks_expected_to_fire"]:
        lines.append(f"{ck}: FIRES (stub)")
    for ck in front["checks_expected_clear"]:
        lines.append(f"{ck}: CLEAR (stub)")
    for ck in front["checks_expected_not_run"]:
        lines.append(f"{ck}: NOT RUN (stub)")
    return "\n".join(lines)


def call_live_model(client, system_prompt, body, model):
    text, _final = model_client.stream_text(
        client,
        label="benchmark",
        model=model,
        max_tokens=4096,
        system=system_prompt,
        messages=[{"role": "user", "content": body}],
    )
    return text


def new_run_dir(base):
    """base itself if unused, else base-2, base-3... - never an existing one."""
    candidate, n = base, 1
    while candidate.exists():
        n += 1
        candidate = base.with_name(f"{base.name}-{n}")
    return candidate


def save_raw_readout(run_dir, case_id, readout):
    run_dir.mkdir(parents=True, exist_ok=True)
    # "x" mode: raises FileExistsError rather than replacing a saved readout.
    with (run_dir / f"{case_id}.md").open("x") as f:
        f.write(readout)


# A status next to a "/" on either side is a template line copied back
# unfilled ("FIRES / CLEAR / NOT RUN"), not a result - including its last option.
RESULT_RE = re.compile(r"\b(CK-0[1-6]|P-0[1-8])\b[^\n]*?(?<!/ )(?<!/)\b(FIRES|CLEAR|NOT RUN)\b(?!\s*/)")
STRENGTH_RE = re.compile(r"Evidence strength:\s*\**\s*(STRONG|UNCERTAIN|WEAK|N/A)\b(?!\s*/)", re.I)
CLAIM_RE = re.compile(r"Claim matches its evidence:\s*\**\s*(Yes|No)\b(?!\s*/)", re.I)
SEVERITY = {"FIRES": 3, "NOT RUN": 2, "CLEAR": 1}


def parse_readout(readout):
    found = {}
    for m in RESULT_RE.finditer(readout):
        code, status = m.group(1), m.group(2)
        if SEVERITY[status] > SEVERITY.get(found.get(code), 0):
            found[code] = status
    return found


def parse_strength(readout):
    m = STRENGTH_RE.search(readout)
    return m.group(1).upper() if m else None


def parse_claim_match(readout):
    m = CLAIM_RE.search(readout)
    return m.group(1).capitalize() if m else None


def score_case(front, found):
    violations = []
    for ck in front["checks_expected_to_fire"]:
        status = found.get(ck, "not detected")
        if status != "FIRES":
            violations.append(f"{ck}: expected FIRES, got {status}")
    for ck in front["checks_expected_clear"]:
        status = found.get(ck, "not detected")
        if status != "CLEAR":
            violations.append(f"{ck}: expected CLEAR, got {status}")
    for ck in front["checks_expected_not_run"]:
        status = found.get(ck, "not detected")
        if status == "CLEAR":
            violations.append(f"{ck}: FALSE PASS - expected NOT RUN, got CLEAR")
        elif status != "NOT RUN":
            violations.append(f"{ck}: expected NOT RUN, got {status}")
    p_codes = sorted(c for c in found if c.startswith("P-"))
    return violations, p_codes


def validate_gold_labels(cases):
    """Every case must declare its own gold labels before run.py will score
    it - not a rule inferred from its filename. Missing a key entirely (not
    just an empty list) is the failure: expected_strength: [] is a real,
    intentional label for an NR case; omitting the key is an unlabelled
    case. Raises rather than silently scoring against a guessed default."""
    missing = [front["id"] for front, _ in cases
               if "expected_strength" not in front or "claim_honest" not in front]
    if missing:
        raise ValueError(
            "Missing expected_strength/claim_honest gold labels - required "
            "before run.py will score a case, live or re-scored: "
            + ", ".join(missing)
        )


def score_strength(front, strength):
    """Returns (passed, label). passed is None when expected_strength is []
    - NR cases test check applicability, not verdict quality, and declare
    this explicitly rather than being inferred from the filename."""
    expected = front.get("expected_strength") or []
    if not expected:
        return None, strength
    if front.get("is_hypothesis") and strength == "N/A":
        return True, strength
    if strength is None:
        return False, strength
    return strength in expected, strength


def score_claim(front, claim_match):
    """Returns (passed, label). "Claim matches its evidence: Yes" should line
    up with claim_honest: yes, and No with no. A missing line fails - there's
    no pass without the readout saying it."""
    if claim_match is None:
        return False, None
    expected = "Yes" if front.get("claim_honest") == "yes" else "No"
    return claim_match == expected, claim_match


def score_lines(results, label=""):
    ck_failed = [r for r in results if r[1]]
    scored_on_strength = [r for r in results if r[3] is not None]
    strength_passed = [r for r in scored_on_strength if r[3]]
    claim_passed = [r for r in results if r[5]]
    return [
        f"- Cases run{label}: {len(results)}",
        f"- CK-ID score{label}: {len(results) - len(ck_failed)}/{len(results)} "
        "(regex-matched FIRES/CLEAR/NOT RUN against front matter)",
        f"- Strength score{label}: {len(strength_passed)}/{len(scored_on_strength)} "
        "(rated within each case's own expected_strength gold label; "
        f"{len(results) - len(scored_on_strength)} NR case(s) excluded, not applicable)",
        f"- Claim score{label}: {len(claim_passed)}/{len(results)} "
        "('Claim matches its evidence' against each case's claim_honest gold label)",
    ]


def report(results, *, target, version, model, run_dir, added_ids=frozenset()):
    """Cases with `added_in` in their front matter are totalled separately:
    the seeded 28 stay comparable with the v1 baseline, and the additions
    (gold labels written before any run) don't shift that comparison."""
    date = datetime.date.today().isoformat()
    seeded = [r for r in results if r[0] not in added_ids]
    added = [r for r in results if r[0] in added_ids]
    all_p_codes = sorted({c for _, _, p, *_ in results for c in p})
    lines = [f"\n## {date} — target={target} version={version} model={model}"]
    lines += score_lines(seeded, " (seeded cases)" if added else "")
    if added:
        lines += score_lines(added, " (added since R0)")
        lines[-4] += f" — {', '.join(r[0] for r in added)}"
    lines += [
        "- P-codes detected across all cases (v1.0 has no CK support; "
        f"partial credit only): {', '.join(all_p_codes) or 'none'}",
        f"- Raw readouts: {run_dir.relative_to(BENCH_DIR)}/",
        "",
    ]
    for result in results:
        lines.append(format_result_line(result, prefix="- **{id}**"))
        for v in result[1]:
            lines.append(f"  - {v}")
    block = "\n".join(lines) + "\n"
    print(block)
    with RESULTS_PATH.open("a") as f:
        f.write(block)


def format_result_line(result, prefix="  {id}"):
    case_id, violations, _p_codes, strength_ok, strength_label, claim_ok, claim_label = result
    strength_status = "N/A" if strength_ok is None else ("PASS" if strength_ok else "FAIL")
    return (prefix.format(id=case_id) + f": CK={'FAIL' if violations else 'PASS'} · "
            f"STRENGTH={strength_status} ({strength_label or 'not detected'}) · "
            f"CLAIM={'PASS' if claim_ok else 'FAIL'} ({claim_label or 'not detected'})")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--target", choices=["skill", "app"], required=True)
    ap.add_argument("--skill-path", help="Path to a ux-research-qa checkout")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--model", default=model_client.AGENT2_MODEL,
                     help="Defaults to the app's AGENT2_MODEL (the QA-role model).")
    ap.add_argument("--force", action="store_true",
                     help=f"Proceed with a live run estimated above "
                          f"${LIVE_RUN_ASK_THRESHOLD_USD:.2f}.")
    ap.add_argument("--rewritten", help="Comma-separated case IDs to actually call live. "
                     "All other cases are re-scored from --source-run instead of re-calling "
                     "the model - use this when only a few cases changed since an earlier run.")
    ap.add_argument("--source-run", help="Run directory (under benchmark/runs/) to pull saved "
                     "readouts from for cases not in --rewritten. Required with --rewritten; "
                     "on its own, re-scores every case from it and calls nothing.")
    args = ap.parse_args()

    if args.target == "app":
        print("ERROR: --target app is not implemented yet (R0 scope is --target skill).")
        sys.exit(2)
    if not args.skill_path:
        print("ERROR: --target skill requires --skill-path.")
        sys.exit(2)
    if args.rewritten and not args.source_run:
        print("ERROR: --rewritten requires --source-run.")
        sys.exit(2)

    cases = load_all_cases()
    added_ids = {front["id"] for front, _ in cases if front.get("added_in")}
    system_prompt = build_skill_system_prompt(args.skill_path)
    version = get_skill_version(args.skill_path)
    date = datetime.date.today().isoformat()
    suffix = "-dry-run" if args.dry_run else ""
    run_dir = new_run_dir(RUNS_DIR / f"{date}-{args.target}-{version}{suffix}")

    def score_and_save(front, readout):
        save_raw_readout(run_dir, front["id"], readout)
        found = parse_readout(readout)
        violations, p_codes = score_case(front, found)
        strength_ok, strength_label = score_strength(front, parse_strength(readout))
        claim_ok, claim_label = score_claim(front, parse_claim_match(readout))
        return (front["id"], violations, p_codes, strength_ok, strength_label, claim_ok, claim_label)

    if args.dry_run:
        results = [score_and_save(front, dry_run_readout(front)) for front, body in cases]
        report(results, target="skill", version=f"{version}-dry-run", model="stub", run_dir=run_dir, added_ids=added_ids)
        sys.exit(1 if any(v for _, v, *_ in results) else 0)

    validate_gold_labels(cases)

    rewritten_ids = set(args.rewritten.split(",")) if args.rewritten else None
    if rewritten_ids is None and args.source_run:
        cases_to_call_live = []
        cases_to_rescore = cases
    elif rewritten_ids is None:
        cases_to_call_live = cases
        cases_to_rescore = []
    else:
        cases_to_call_live = [c for c in cases if c[0]["id"] in rewritten_ids]
        cases_to_rescore = [c for c in cases if c[0]["id"] not in rewritten_ids]
        found_ids = {front["id"] for front, _ in cases_to_call_live}
        if found_ids != rewritten_ids:
            print(f"ERROR: --rewritten named case(s) not found: {rewritten_ids - found_ids}")
            sys.exit(2)

    results = []
    for front, _body in cases_to_rescore:
        saved = Path(args.source_run) / f"{front['id']}.md"
        if not saved.exists():
            print(f"ERROR: --source-run is missing {saved} - was this case renamed?")
            sys.exit(2)
        results.append(score_and_save(front, saved.read_text()))
        print(format_result_line(results[-1]) + f" [re-scored from {args.source_run}]")

    if not cases_to_call_live:
        report(results, target="skill", version=version, model="(rescored only)", run_dir=run_dir, added_ids=added_ids)
        return

    cost = print_cost_estimate(system_prompt, cases_to_call_live)
    if cost > LIVE_RUN_ASK_THRESHOLD_USD and not args.force:
        print(f"\nEstimated cost ~${cost:.2f} exceeds the ${LIVE_RUN_ASK_THRESHOLD_USD:.2f} "
              "pre-approved threshold. Confirm with Nikos, then re-run with --force.")
        sys.exit(1)

    api_key = credentials.resolve(allow_prompt=False)
    if not api_key:
        print("ERROR: no ANTHROPIC_API_KEY found (.env or keyring).")
        sys.exit(2)
    import anthropic
    client = anthropic.Anthropic(api_key=api_key)

    # A result is written for every case attempted, even if a later case
    # errors out - an uncaught exception here used to lose every prior
    # live call's result along with it, which is a worse outcome than the
    # error itself: it throws away money already spent along with the
    # evidence of what it bought.
    stop_early = False
    for front, body in cases_to_call_live:
        try:
            readout = call_live_model(client, system_prompt, body, args.model)
        except Exception as exc:
            results.append((front["id"], [f"ERROR: {exc}"], [], False, None, False, None))
            print(f"  {front['id']}: ERROR ({exc})")
            # A quota/rate-limit error will reject every subsequent call
            # identically - stop rather than spend the printed estimate
            # again for nothing.
            msg = str(exc).lower()
            if "usage limit" in msg or "rate_limit" in msg or "429" in msg:
                print("  Stopping: this looks account-level, not case-specific "
                      "- further calls would fail the same way.")
                stop_early = True
                break
            continue
        results.append(score_and_save(front, readout))
        print(format_result_line(results[-1]))

    report(results, target="skill",
           version=version + (" (STOPPED EARLY)" if stop_early else ""),
           model=args.model, run_dir=run_dir, added_ids=added_ids)
    if stop_early:
        sys.exit(1)


if __name__ == "__main__":
    main()

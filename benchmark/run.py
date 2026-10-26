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

  Strength score     Label-independent: parses the STRONG/UNCERTAIN/WEAK
                     verdict on the claim under review. A fire case (and the
                     Weather Underground baseline, which is fire-shaped even
                     though its filename doesn't say so) passes if the claim
                     is NOT rated STRONG; a clear case passes if it is NOT
                     rated WEAK. NR cases aren't scored on this axis - they
                     test check applicability, not verdict quality. This is
                     what makes v1 vs a future R1 a fair comparison: a skill
                     that emits no CK codes at all can still pass this axis
                     by reasoning its way to a calibrated verdict.

Raw readouts are saved to benchmark/runs/<date>-<target>-<version>/<case-id>.md
(dry-run included) - without them a run can't be re-scored or audited later
against a scoring-logic change.

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
ASSUMED_OUTPUT_TOKENS_PER_CASE = 750  # v1.0 baseline: provenance + falsification + pitfalls table + verdict, no CK section


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
          f"(assumed {ASSUMED_OUTPUT_TOKENS_PER_CASE}/case, v1.0 has no CK section)")
    print(f"Estimated cost @ ${INPUT_RATE_PER_MTOK:.0f}/MTok in, "
          f"${OUTPUT_RATE_PER_MTOK:.0f}/MTok out: ~${cost:.2f}")
    return cost


def dry_run_readout(front):
    """Deterministic stub - exercises the parse/score path with no network
    call. UNCERTAIN passes the strength score either way (fire wants
    not-STRONG, clear wants not-WEAK), so a clean dry run stays clean under
    both scores."""
    lines = ["## Finding: (dry-run stub)", "", "**Evidence strength: UNCERTAIN**", ""]
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


def save_raw_readout(run_dir, case_id, readout):
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / f"{case_id}.md").write_text(readout)


RESULT_RE = re.compile(r"\b(CK-0[1-6]|P-0[1-8])\b[^\n]*?\b(FIRES|CLEAR|NOT RUN)\b", re.I)
STRENGTH_RE = re.compile(r"Evidence strength:\s*\**\s*(STRONG|UNCERTAIN|WEAK)\b", re.I)


def parse_readout(readout):
    found = {}
    for m in RESULT_RE.finditer(readout):
        found[m.group(1).upper()] = m.group(2).upper()
    return found


def parse_strength(readout):
    m = STRENGTH_RE.search(readout)
    return m.group(1).upper() if m else None


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


def score_strength(front, strength):
    """Returns (passed, label). passed is None when the case isn't scored on
    this axis at all (NR cases test check applicability, not verdict
    quality)."""
    case_id = front["id"]
    if case_id.startswith("NR-"):
        return None, strength
    is_fire_type = "-fire-" in case_id or case_id.startswith("WU-baseline")
    if strength is None:
        return False, strength
    if is_fire_type:
        return strength != "STRONG", strength
    return strength != "WEAK", strength


def report(results, *, target, version, model, run_dir):
    date = datetime.date.today().isoformat()
    ck_failed = [r for r in results if r[1]]
    scored_on_strength = [r for r in results if r[3] is not None]
    strength_passed = [r for r in scored_on_strength if r[3]]
    all_p_codes = sorted({c for _, _, p, *_ in results for c in p})
    lines = [
        f"\n## {date} — target={target} version={version} model={model}",
        f"- Cases run: {len(results)}",
        f"- CK-ID score: {len(results) - len(ck_failed)}/{len(results)} "
        "(regex-matched FIRES/CLEAR/NOT RUN against front matter)",
        f"- Strength score: {len(strength_passed)}/{len(scored_on_strength)} "
        "(fire cases not rated STRONG, clear cases not rated WEAK; "
        f"{len(results) - len(scored_on_strength)} NR case(s) excluded, not applicable)",
        "- P-codes detected across all cases (v1.0 has no CK support; "
        f"partial credit only): {', '.join(all_p_codes) or 'none'}",
        f"- Raw readouts: {run_dir.relative_to(BENCH_DIR)}/",
        "",
    ]
    for case_id, violations, _p_codes, strength_ok, strength_label in results:
        ck_status = "FAIL" if violations else "PASS"
        if strength_ok is None:
            strength_status = "N/A"
        else:
            strength_status = "PASS" if strength_ok else "FAIL"
        lines.append(f"- **{case_id}**: CK={ck_status} · "
                     f"STRENGTH={strength_status} ({strength_label or 'not detected'})")
        for v in violations:
            lines.append(f"  - {v}")
    block = "\n".join(lines) + "\n"
    print(block)
    with RESULTS_PATH.open("a") as f:
        f.write(block)


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
    args = ap.parse_args()

    if args.target == "app":
        print("ERROR: --target app is not implemented yet (R0 scope is --target skill).")
        sys.exit(2)
    if not args.skill_path:
        print("ERROR: --target skill requires --skill-path.")
        sys.exit(2)

    cases = load_all_cases()
    system_prompt = build_skill_system_prompt(args.skill_path)
    version = get_skill_version(args.skill_path)
    date = datetime.date.today().isoformat()
    run_dir = RUNS_DIR / f"{date}-{args.target}-{version}"

    def score_and_save(front, body_or_none, readout):
        save_raw_readout(run_dir, front["id"], readout)
        found = parse_readout(readout)
        violations, p_codes = score_case(front, found)
        strength_ok, strength_label = score_strength(front, parse_strength(readout))
        return (front["id"], violations, p_codes, strength_ok, strength_label)

    if args.dry_run:
        results = [score_and_save(front, body, dry_run_readout(front)) for front, body in cases]
        report(results, target="skill", version=f"{version}-dry-run", model="stub", run_dir=run_dir)
        sys.exit(1 if any(v for _, v, *_ in results) else 0)

    cost = print_cost_estimate(system_prompt, cases)
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
    results = []
    stop_early = False
    for front, body in cases:
        try:
            readout = call_live_model(client, system_prompt, body, args.model)
        except Exception as exc:
            results.append((front["id"], [f"ERROR: {exc}"], [], False, None))
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
        result = score_and_save(front, body, readout)
        results.append(result)
        _id, violations, p_codes, strength_ok, strength_label = result
        print(f"  {_id}: CK={'FAIL' if violations else 'PASS'} · "
              f"STRENGTH={'N/A' if strength_ok is None else ('PASS' if strength_ok else 'FAIL')} "
              f"({strength_label or 'not detected'})")

    report(results, target="skill",
           version=version + (" (STOPPED EARLY)" if stop_early else ""),
           model=args.model, run_dir=run_dir)
    if stop_early:
        sys.exit(1)


if __name__ == "__main__":
    main()

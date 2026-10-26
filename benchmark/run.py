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

Scoring: regex-extracts "<CODE> ... FIRES|CLEAR|NOT RUN" from the readout for
every CK-0x and P-0x code, and compares against each case's front matter.
Before R1 exists the skill emits no CK codes at all, so every CK is recorded
"not detected" for v1.0 - that gap, not a score, is the baseline's point. A
check reporting CLEAR where the case declared checks_expected_not_run is
scored as a FALSE PASS, not a miss: fail-closed is a correctness property
(spec principle 1), so a quiet pass on missing input is worse than an honest
NOT RUN.

Cost note: token counts here are an estimate (chars/4 vs words*1.35, the
larger of the two), not a measurement - there is no usage.* to read until a
live call actually returns one. Treat the printed figure as a ceiling to
decide whether to proceed, not a promise.
"""
import argparse
import datetime
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import credentials
import model_client

BENCH_DIR = Path(__file__).resolve().parent
CASES_DIR = BENCH_DIR / "cases"
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
    """Deterministic stub - exercises the parse/score path with no network call."""
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


RESULT_RE = re.compile(r"\b(CK-0[1-6]|P-0[1-8])\b[^\n]*?\b(FIRES|CLEAR|NOT RUN)\b", re.I)


def parse_readout(readout):
    found = {}
    for m in RESULT_RE.finditer(readout):
        found[m.group(1).upper()] = m.group(2).upper()
    return found


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


def report(results, *, target, version, model):
    date = datetime.date.today().isoformat()
    failed = [r for r in results if r[1]]
    all_p_codes = sorted({c for _, _, p in results for c in p})
    lines = [
        f"\n## {date} — target={target} version={version} model={model}",
        f"- Cases run: {len(results)}",
        f"- Cases with violations: {len(failed)}",
        "- P-codes detected across all cases (v1.0 has no CK support; "
        f"partial credit only): {', '.join(all_p_codes) or 'none'}",
        "",
    ]
    for case_id, violations, _ in results:
        lines.append(f"- **{case_id}**: {'FAIL' if violations else 'PASS'}")
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

    if args.dry_run:
        results = []
        for front, _body in cases:
            found = parse_readout(dry_run_readout(front))
            violations, p_codes = score_case(front, found)
            results.append((front["id"], violations, p_codes))
        report(results, target="skill", version=f"{args.skill_path} (dry-run)", model="stub")
        sys.exit(1 if any(v for _, v, _ in results) else 0)

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

    results = []
    for front, body in cases:
        readout = call_live_model(client, system_prompt, body, args.model)
        found = parse_readout(readout)
        violations, p_codes = score_case(front, found)
        results.append((front["id"], violations, p_codes))
        print(f"  {front['id']}: {'FAIL' if violations else 'PASS'}")

    report(results, target="skill", version=args.skill_path, model=args.model)


if __name__ == "__main__":
    main()

"""Benchmark probe: the dry-run path scores correctly against a stub, and the
false-pass rule actually catches a quiet pass on missing input.

Boundaries asserted (no API calls - the model is never invoked; dry_run_readout
is a deterministic stub):

  1. The skill-path system prompt builder concatenates SKILL.md + references/
     + templates/ from an arbitrary directory, in that order.
  2. Every real case in benchmark/cases/ round-trips through the dry-run path
     with zero violations - the stub is built directly from each case's own
     front matter, so a mismatch here means the parser or scorer is broken,
     not that a case is "hard".
  3. CLEAR reported where checks_expected_not_run was declared scores as a
     FALSE PASS specifically (not just "any violation") - this is the one
     path spec principle 1 (fail closed) depends on this benchmark catching.
  4. A case missing its front matter block raises, rather than silently
     scoring as if it declared nothing.

Free and deterministic.
"""
import sys
import tempfile
from pathlib import Path

from benchmark import run as bench_run

violations = []

# --- 1. System prompt builder reads SKILL.md + references/ + templates/ ----
with tempfile.TemporaryDirectory() as tmp:
    skill_dir = Path(tmp)
    (skill_dir / "references").mkdir()
    (skill_dir / "templates").mkdir()
    (skill_dir / "SKILL.md").write_text("SKILL BODY")
    (skill_dir / "references" / "a.md").write_text("REF A")
    (skill_dir / "templates" / "t.md").write_text("TEMPLATE T")
    prompt = bench_run.build_skill_system_prompt(skill_dir)
    for expected in ("SKILL BODY", "REF A", "TEMPLATE T"):
        if expected not in prompt:
            violations.append(f"SYSTEM PROMPT: missing {expected!r} from the built prompt.")
    if prompt.index("SKILL BODY") > prompt.index("REF A"):
        violations.append("SYSTEM PROMPT: SKILL.md did not come first.")

# --- 2. Every real case scores clean against its own stub -------------------
cases = bench_run.load_all_cases()
if len(cases) != 28:
    violations.append(f"CASE COUNT: expected 28 seeded cases, found {len(cases)}.")

for front, _body in cases:
    found = bench_run.parse_readout(bench_run.dry_run_readout(front))
    case_violations, _p_codes = bench_run.score_case(front, found)
    if case_violations:
        violations.append(
            f"CASE {front.get('id')}: dry-run stub did not score clean against "
            f"its own front matter: {case_violations}"
        )

# Coverage check: at least 2 fire + 2 clear per CK-01..CK-06, per spec.
for i in range(1, 7):
    ck = f"CK-{i:02d}"
    fires = sum(1 for front, _ in cases if ck in front["checks_expected_to_fire"])
    clears = sum(1 for front, _ in cases if ck in front["checks_expected_clear"])
    if fires < 2:
        violations.append(f"COVERAGE: {ck} has {fires} fire case(s), need >= 2.")
    if clears < 2:
        violations.append(f"COVERAGE: {ck} has {clears} clear case(s), need >= 2.")

if not any(front["id"] == "WU-baseline-01" and not front["synthetic"] for front, _ in cases):
    violations.append("COVERAGE: WU-baseline-01 missing or not marked synthetic: false.")

nr_ids = {front["id"] for front, _ in cases if front["id"].startswith("NR-")}
if nr_ids != {"NR-01", "NR-02", "NR-03"}:
    violations.append(f"COVERAGE: expected NR-01..03, found {sorted(nr_ids)}.")

# --- 3. CLEAR where NOT RUN was expected is a FALSE PASS, specifically -------
front_nr = {"id": "synthetic-not-run-test", "checks_expected_to_fire": [],
            "checks_expected_clear": [], "checks_expected_not_run": ["CK-02"]}
quiet_pass = bench_run.score_case(front_nr, {"CK-02": "CLEAR"})[0]
if not quiet_pass or not any("FALSE PASS" in v for v in quiet_pass):
    violations.append(
        "FALSE PASS: a check reporting CLEAR where NOT RUN was expected must "
        "be flagged as FALSE PASS specifically, not a generic mismatch."
    )
honest_not_run = bench_run.score_case(front_nr, {"CK-02": "NOT RUN"})[0]
if honest_not_run:
    violations.append("FALSE PASS: an honestly-reported NOT RUN was flagged as a violation.")
missing_entirely = bench_run.score_case(front_nr, {})[0]
if not missing_entirely:
    violations.append(
        "FALSE PASS: a v1.0 readout with no CK codes at all ('not detected') "
        "must still be flagged against a NOT RUN expectation, not treated as a pass."
    )

# --- 4. Malformed case file raises, not silently scored as empty -----------
with tempfile.TemporaryDirectory() as tmp:
    bad = Path(tmp) / "BAD-01.md"
    bad.write_text("no front matter here, just a claim under review")
    try:
        bench_run.load_case(bad)
        violations.append("MALFORMED CASE: missing front matter did not raise.")
    except ValueError:
        pass

print("===== BENCHMARK ASSERTIONS =====")
if violations:
    for v in violations:
        sys.stdout.write(f"FAIL: {v}\n")
    sys.exit(1)
print(f"PASS: {len(cases)} cases parse and score clean against their own stub; "
      "coverage holds; a quiet CLEAR on missing input scores as FALSE PASS.")

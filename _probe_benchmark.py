"""Benchmark probe: the dry-run path scores correctly against a stub, the
false-pass rule catches a quiet pass on missing input, raw readouts land on
disk where a later audit can find them, the strength score applies to the
right cases, and the version string is a commit hash, not a path.

Boundaries asserted (no API calls - the model is never invoked; dry_run_readout
is a deterministic stub):

  1. The skill-path system prompt builder concatenates SKILL.md + references/
     + templates/ from an arbitrary directory, in that order.
  2. Every real case in benchmark/cases/ round-trips through the dry-run path
     with zero violations on both scores - the stub is built directly from
     each case's own front matter, so a mismatch here means the parser or
     scorer is broken, not that a case is "hard".
  3. CLEAR reported where checks_expected_not_run was declared scores as a
     FALSE PASS specifically (not just "any violation").
  4. A case missing its front matter block raises, rather than silently
     scoring as if it declared nothing.
  5. The strength score: a fire-type case (including WU-baseline, which is
     fire-shaped despite its filename) fails on STRONG and passes on
     UNCERTAIN/WEAK; a clear-type case fails on WEAK and passes on
     STRONG/UNCERTAIN; an NR case is not scored on this axis at all
     (passed is None); a readout with no parseable strength label fails,
     not "not applicable".
  6. A dry run writes one raw-readout file per case under
     benchmark/runs/<date>-<target>-<version>/ - without these, a run can't
     be re-scored later against a scoring-logic change.
  7. get_skill_version returns a short commit hash for a real git checkout,
     and falls back (rather than raising) for a directory that isn't one.

Free and deterministic.
"""
import subprocess
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

# --- 2. Every real case scores clean against its own stub, both axes -------
cases = bench_run.load_all_cases()
if len(cases) != 28:
    violations.append(f"CASE COUNT: expected 28 seeded cases, found {len(cases)}.")

for front, _body in cases:
    stub = bench_run.dry_run_readout(front)
    found = bench_run.parse_readout(stub)
    case_violations, _p_codes = bench_run.score_case(front, found)
    if case_violations:
        violations.append(
            f"CASE {front.get('id')}: dry-run stub did not score clean on the "
            f"CK axis: {case_violations}"
        )
    strength_ok, _label = bench_run.score_strength(front, bench_run.parse_strength(stub))
    if strength_ok is False:
        violations.append(
            f"CASE {front.get('id')}: dry-run stub (UNCERTAIN) failed the "
            "strength score - it should pass fire and clear cases alike."
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

# --- 5. Strength score applies to the right cases, with the right polarity -
fire_front = {"id": "CK-05-fire-03"}
clear_front = {"id": "CK-05-clear-03"}
wu_front = {"id": "WU-baseline-01"}
nr_front = {"id": "NR-04"}

checks = [
    (fire_front, "STRONG", False), (fire_front, "UNCERTAIN", True), (fire_front, "WEAK", True),
    (clear_front, "WEAK", False), (clear_front, "UNCERTAIN", True), (clear_front, "STRONG", True),
    (wu_front, "STRONG", False), (wu_front, "UNCERTAIN", True),
]
for front, label, expect_pass in checks:
    ok, _ = bench_run.score_strength(front, label)
    if ok is not expect_pass:
        violations.append(
            f"STRENGTH SCORE: {front['id']} with label {label} expected "
            f"passed={expect_pass}, got {ok}."
        )

nr_ok, _ = bench_run.score_strength(nr_front, "STRONG")
if nr_ok is not None:
    violations.append(f"STRENGTH SCORE: an NR case must not be scored on this axis, got {nr_ok!r}.")

no_label_ok, no_label_val = bench_run.score_strength(fire_front, None)
if no_label_ok is not False or no_label_val is not None:
    violations.append(
        "STRENGTH SCORE: a readout with no parseable strength label must fail "
        "(not pass, not N/A) - we can't confirm it without a label."
    )

# --- 6. A dry run saves one raw readout per case ----------------------------
with tempfile.TemporaryDirectory() as tmp:
    run_dir = Path(tmp) / "a-run"
    for front, _body in cases[:3]:
        bench_run.save_raw_readout(run_dir, front["id"], bench_run.dry_run_readout(front))
    saved = sorted(p.name for p in run_dir.glob("*.md"))
    expected = sorted(f"{front['id']}.md" for front, _ in cases[:3])
    if saved != expected:
        violations.append(f"RAW READOUTS: expected {expected}, found {saved}.")

# --- 7. Version is a commit hash for a real checkout, a fallback otherwise -
with tempfile.TemporaryDirectory() as tmp:
    repo = Path(tmp)
    subprocess.run(["git", "init", "-q", "-b", "main", str(repo)], check=True)
    (repo / "f.txt").write_text("x")
    subprocess.run(["git", "-C", str(repo), "add", "f.txt"], check=True)
    subprocess.run(
        ["git", "-C", str(repo), "-c", "user.email=a@b.c", "-c", "user.name=t",
         "commit", "-q", "-m", "x"],
        check=True,
    )
    expected_hash = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "--short", "HEAD"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    got = bench_run.get_skill_version(repo)
    if got != expected_hash:
        violations.append(f"VERSION: expected commit hash {expected_hash!r}, got {got!r}.")

with tempfile.TemporaryDirectory() as tmp:
    not_a_repo = Path(tmp)
    got = bench_run.get_skill_version(not_a_repo)
    if got == "" or "/" in got:
        violations.append(
            f"VERSION: a non-git directory must fall back to something readable, got {got!r}."
        )

print("===== BENCHMARK ASSERTIONS =====")
if violations:
    for v in violations:
        sys.stdout.write(f"FAIL: {v}\n")
    sys.exit(1)
print(f"PASS: {len(cases)} cases parse and score clean on both axes against their "
      "own stub; coverage holds; a quiet CLEAR on missing input scores as FALSE "
      "PASS; strength scoring applies to the right cases with the right polarity; "
      "raw readouts save per case; version resolves to a commit hash.")

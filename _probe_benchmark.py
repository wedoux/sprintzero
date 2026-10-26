"""Benchmark probe: the dry-run path scores correctly against a stub, the
false-pass rule catches a quiet pass on missing input, raw readouts land on
disk where a later audit can find them, the strength score is driven by each
case's own gold labels (not an inferred filename rule), a case missing its
gold labels blocks scoring, the version string is a commit hash, and the
rescore-from-saved-readouts path works without a network call.

Boundaries asserted (no API calls - the model is never invoked; dry_run_readout
is a deterministic stub):

  1. The skill-path system prompt builder concatenates SKILL.md + references/
     + templates/ from an arbitrary directory, in that order.
  2. Every real case in benchmark/cases/ round-trips through the dry-run path
     with zero violations on both scores - the stub is built from each case's
     own expected_strength/is_hypothesis, so a mismatch here means the parser
     or scorer is broken, not that a case is "hard".
  3. CLEAR reported where checks_expected_not_run was declared scores as a
     FALSE PASS specifically (not just "any violation").
  4. A case missing its front matter block raises, rather than silently
     scoring as if it declared nothing.
  5. The strength score reads expected_strength from the case itself: a tier
     inside that list passes, a tier outside it fails, an NR-style empty list
     isn't scored at all (passed is None), a readout with no parseable label
     fails (can't confirm a pass without one), and N/A only passes when the
     case also declares is_hypothesis - otherwise it's just another label
     outside the expected set.
  6. A dry run writes one raw-readout file per case under
     benchmark/runs/<date>-<target>-<version>/ - without these, a run can't
     be re-scored later against a scoring-logic change.
  7. get_skill_version returns a short commit hash for a real git checkout,
     and falls back (rather than raising) for a directory that isn't one.
  8. validate_gold_labels raises when expected_strength or claim_honest is
     missing entirely (not just empty), and passes when every case has both
     keys declared - this is the gate that keeps a label-less case from ever
     being scored live.
  9. Re-scoring from a saved readout (the --rewritten/--source-run path)
     produces the same result as scoring that same text fresh - no API call,
     same scoring function either way.

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
            f"CASE {front.get('id')}: dry-run stub did not score clean on the "
            "strength axis against its own expected_strength."
        )

# All 28 cases must carry real gold labels post-R0.2 - the point of this
# probe run is partly to prove that's actually true, not assumed.
for front, _ in cases:
    if "expected_strength" not in front or "claim_honest" not in front:
        violations.append(f"GOLD LABELS: {front['id']} is missing expected_strength or claim_honest.")

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

# --- 5. Strength score reads expected_strength from the case, not the id ---
weak_only = {"id": "any-id-01", "expected_strength": ["WEAK"]}
wide_open = {"id": "any-id-02", "expected_strength": ["UNCERTAIN", "STRONG"]}
not_scored = {"id": "any-id-03", "expected_strength": []}
hypothesis = {"id": "any-id-04", "expected_strength": ["UNCERTAIN"], "is_hypothesis": True}
non_hypothesis_same_tiers = {"id": "any-id-05", "expected_strength": ["UNCERTAIN"]}

checks = [
    (weak_only, "WEAK", True), (weak_only, "UNCERTAIN", False), (weak_only, "STRONG", False),
    (wide_open, "UNCERTAIN", True), (wide_open, "STRONG", True), (wide_open, "WEAK", False),
]
for front, label, expect_pass in checks:
    ok, _ = bench_run.score_strength(front, label)
    if ok is not expect_pass:
        violations.append(
            f"STRENGTH SCORE: {front['id']} with label {label} expected "
            f"passed={expect_pass}, got {ok}."
        )

not_scored_ok, _ = bench_run.score_strength(not_scored, "STRONG")
if not_scored_ok is not None:
    violations.append(
        f"STRENGTH SCORE: expected_strength: [] must not be scored on this axis, got {not_scored_ok!r}."
    )

hyp_ok, hyp_label = bench_run.score_strength(hypothesis, "N/A")
if hyp_ok is not True:
    violations.append("STRENGTH SCORE: is_hypothesis case with N/A must pass.")

non_hyp_na_ok, _ = bench_run.score_strength(non_hypothesis_same_tiers, "N/A")
if non_hyp_na_ok is not False:
    violations.append(
        "STRENGTH SCORE: N/A must NOT auto-pass a case that doesn't declare "
        "is_hypothesis, even if the readout says it - the escape hatch is "
        "per-case, not per-label."
    )

no_label_ok, no_label_val = bench_run.score_strength(weak_only, None)
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

# --- 8. validate_gold_labels is the actual enforcement gate ----------------
labelled = [({"id": "ok-01", "expected_strength": ["WEAK"], "claim_honest": "no"}, "")]
try:
    bench_run.validate_gold_labels(labelled)
except ValueError:
    violations.append("GOLD LABELS: a fully-labelled case set was rejected.")

missing_strength = [({"id": "bad-01", "claim_honest": "no"}, "")]
missing_honest = [({"id": "bad-02", "expected_strength": []}, "")]
for bad_set, which in [(missing_strength, "expected_strength"), (missing_honest, "claim_honest")]:
    try:
        bench_run.validate_gold_labels(bad_set)
        violations.append(f"GOLD LABELS: a case missing {which} entirely was not rejected.")
    except ValueError:
        pass

# --- 9. Re-scoring a saved readout matches scoring it fresh -----------------
sample_front, _ = cases[0]
sample_readout = bench_run.dry_run_readout(sample_front)
with tempfile.TemporaryDirectory() as tmp:
    source_run = Path(tmp) / "source-run"
    bench_run.save_raw_readout(source_run, sample_front["id"], sample_readout)
    reloaded = (source_run / f"{sample_front['id']}.md").read_text()
    if reloaded != sample_readout:
        violations.append("RESCORE: saved-then-reloaded readout text does not round-trip exactly.")
    fresh_found = bench_run.parse_readout(sample_readout)
    reloaded_found = bench_run.parse_readout(reloaded)
    if fresh_found != reloaded_found:
        violations.append("RESCORE: re-parsing a reloaded readout gave a different result than the original.")

print("===== BENCHMARK ASSERTIONS =====")
if violations:
    for v in violations:
        sys.stdout.write(f"FAIL: {v}\n")
    sys.exit(1)
print(f"PASS: {len(cases)} cases carry gold labels and score clean on both axes against "
      "their own stub; coverage holds; a quiet CLEAR on missing input scores as FALSE "
      "PASS; strength scoring reads expected_strength/is_hypothesis per case, not an "
      "inferred filename rule; validate_gold_labels blocks a case missing either field; "
      "raw readouts save and re-score identically; version resolves to a commit hash.")

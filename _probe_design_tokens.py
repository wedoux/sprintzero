"""Design-token probe: the two-axis status grammar must stay separated.

SprintZero renders two INDEPENDENT axes:
  Axis 1 - evidence strength (STRONG/UNCERTAIN/WEAK): neutral, never semantic.
  Axis 2 - QA status (QA_PASSED/QA_FAILED): the only axis allowed red/green.

Conflating them is the defect this probe exists to prevent: it made a WEAK
verdict read as a failure, when surfacing weak evidence is the QA layer
succeeding. This probe fails loudly if the axes are ever remerged.
"""
import re
import sys
from pathlib import Path

INDEX = Path(__file__).parent / "templates" / "index.html"
css = INDEX.read_text(encoding="utf-8")

# Semantic colour that must never touch the evidence-strength axis.
SEMANTIC_TOKENS = ("--green-", "--red-", "--amber-")
SEMANTIC_HEX = re.compile(
    r"#(?:F0F7F2|E5F2EA|FEF2F2|FCDFDF|FFFAEB|FFEFC9|1E7A47|276B47|A01F1F|B04040|8B5A00|B07800)",
    re.IGNORECASE,
)
STRENGTH_SELECTORS = (".verdict-banner.", ".classification.", ".confidence-fill.")
STRENGTH_CLASSES = ("STRONG", "UNCERTAIN", "WEAK")

violations = []

# --- Assertion 1: no strength rule may carry semantic colour -------------
for line in css.splitlines():
    stripped = line.strip()
    if not stripped.startswith(STRENGTH_SELECTORS):
        continue
    if not any(f".{c} " in stripped or f".{c}{{" in stripped for c in STRENGTH_CLASSES):
        continue
    for tok in SEMANTIC_TOKENS:
        if tok in stripped:
            violations.append(
                f"AXIS VIOLATION: evidence-strength rule uses semantic token {tok!r}.\n"
                f"    {stripped}\n"
                "    Strength is a measurement, not a judgement - use --strength-* tokens."
            )
    hit = SEMANTIC_HEX.search(stripped)
    if hit:
        violations.append(
            f"AXIS VIOLATION: evidence-strength rule hardcodes semantic hex {hit.group(0)!r}.\n"
            f"    {stripped}\n"
            "    Use the neutral --strength-* ramp."
        )

# --- Assertion 2: both axes' token sets must exist ------------------------
REQUIRED_TOKENS = [
    "--strength-strong-ink", "--strength-moderate-ink", "--strength-weak-ink",
    "--strength-strong-fill", "--strength-moderate-fill", "--strength-weak-fill",
    "--qa-pass-ink", "--qa-fail-ink", "--qa-degraded-ink",
]
for tok in REQUIRED_TOKENS:
    if f"{tok}:" not in css:
        violations.append(f"MISSING TOKEN: {tok} is not defined in :root.")

# --- Assertion 3: the QA axis must keep its semantic colour ---------------
# Decoupling must not accidentally neutralise the gate itself.
for sel, tok in ((".qa-stamp-value.QA_PASSED", "--qa-pass-ink"),
                 (".qa-stamp-value.QA_FAILED", "--qa-fail-ink")):
    if f"{sel} {{ color: var({tok})" not in css:
        violations.append(
            f"GATE VIOLATION: {sel} no longer resolves to {tok}. "
            "QA status must keep semantic colour - it is the axis that earns it."
        )

# --- Assertion 4: the strength ramp must actually differ across levels ----
fills = {}
for c in STRENGTH_CLASSES:
    m = re.search(rf"\.confidence-fill\.{c} \{{ background: var\((--[a-z-]+)\); \}}", css)
    if m:
        fills[c] = m.group(1)
if len(set(fills.values())) != len(STRENGTH_CLASSES):
    violations.append(
        f"RAMP VIOLATION: strength levels must be visually distinct, got {fills}."
    )

print("===== DESIGN TOKEN AXIS ASSERTIONS =====")
if violations:
    for v in violations:
        sys.stdout.write(f"FAIL: {v}\n")
    sys.exit(1)
print("PASS: evidence-strength axis is neutral; QA axis retains semantic colour.")

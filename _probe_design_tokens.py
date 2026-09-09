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

# The design system lives in its own partial, shared by every screen - but
# landing.html carries a second <style> block of its own, and that is where a
# QA-green "READY" pill sat unnoticed. Reading one file was how the probe
# missed it, so it reads every template now.
TEMPLATES = Path(__file__).parent / "templates"
STYLE_SOURCES = sorted(TEMPLATES.rglob("*.html"))
css = "\n".join(f.read_text(encoding="utf-8") for f in STYLE_SOURCES)

# Semantic colour that must never touch the evidence-strength axis.
# --qa-pass-/--qa-fail- are here too: borrowing the gate's own tokens for
# something that is not the gate is the same leak as borrowing raw green,
# and it is how a "READY" project pill on the landing screen went unnoticed.
SEMANTIC_TOKENS = ("--green-", "--red-", "--amber-", "--qa-pass-", "--qa-fail-")
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

# --- Assertion 5: semantic colour only where it is earned ----------------
# Assertion 1 guards three selectors. The other ~1000 lines were unguarded,
# and green had leaked into four of them: the knowledge-base panel, its
# bullets, the activity trail's done marker and the options message. Ambient
# "this is fine" green is precisely what stops a QA pass badge meaning
# anything, so the rule needs to hold across the whole stylesheet, not just
# where someone remembered to look.
#
# Allowed, and why:
#   .qa-, .check-pill-   AXIS 2. The gate. This is the axis that earns colour.
#   .sys-msg-challenge   AXIS 3 advisory chrome, on the --attention-* ramp.
#   .sys-msg-required    AXIS 3 advisory chrome.
#   .error, .parse-fail  Errors. Not an axis - "this broke" reads as red to
#   .sys-msg-error       everyone, and no grammar should relabel it.
SEMANTIC_OK_PREFIXES = (
    ".qa-", ".check-pill-",                 # AXIS 2. The gate itself.
    ".verdict-gate",                        # AXIS 2. The gate, on the banner.
    ".verdict-banner.qa-invalidated",       # AXIS 2. QA overruled the verdict.
                                            # Bare .verdict-banner.STRONG is
                                            # still caught by Assertion 1.
    ".hist-qa",                             # AXIS 2. QA status in history.
    ".sys-msg-challenge", ".sys-msg-required",   # AXIS 3 advisory chrome.
    ".sys-msg-error", ".parse-fail", ".error",   # Errors. Not an axis.
    ".create-error", ".ref-error",               # Errors, on the two forms.
    ".ref-remove:hover",                    # Destructive action turning red
                                            # on hover is an affordance, not
                                            # a verdict about anything.
)
ADVISORY_HEX = re.compile(r"#(?:FCE7E7)", re.IGNORECASE)

selector = "(unknown)"
in_root = False
in_style = False
for line in css.splitlines():
    if "<style" in line:
        in_style = True
    elif "</style>" in line:
        in_style = False
    if not in_style:
        continue
    stripped = line.strip()
    if stripped.startswith(":root"):
        in_root = True
    if in_root:
        if stripped.startswith("}"):
            in_root = False
        continue                      # :root is where these tokens live
    if stripped.endswith("{"):
        selector = stripped[:-1].strip()
    elif "{" in stripped and "}" in stripped:
        selector = stripped.split("{")[0].strip()
    if not (any(t in stripped for t in SEMANTIC_TOKENS)
            or SEMANTIC_HEX.search(stripped) or ADVISORY_HEX.search(stripped)):
        continue
    if selector.startswith(SEMANTIC_OK_PREFIXES):
        continue
    violations.append(
        f"AXIS VIOLATION: {selector!r} uses semantic colour outside the QA gate.\n"
        f"    {stripped}\n"
        "    Green and red belong to AXIS 2. Reference material, completed\n"
        "    steps and offered options are context chrome - use --context-*."
    )

print("===== DESIGN TOKEN AXIS ASSERTIONS =====")
if violations:
    for v in violations:
        sys.stdout.write(f"FAIL: {v}\n")
    sys.exit(1)
print("PASS: evidence-strength axis is neutral; QA axis retains semantic colour.")

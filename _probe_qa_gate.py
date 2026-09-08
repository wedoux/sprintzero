"""QA-gate probe: the QA result must visibly act on Agent 1's verdict.

Boundaries asserted (no API calls - synthetic Agent 2 output):

  1. QA_PASSED  -> the verdict renders exactly as before. No invalidation,
                   no strikethrough class, nothing added. A pass is not an event.
  2. QA_FAILED  -> the verdict is visibly invalidated AND carries the reason.
                   A struck-through verdict with no stated reason is the same
                   misread this work exists to remove.
  3. QA_FAILED with no reason (degraded) -> must NOT be dressed as a substantive
                   failure. merge_qa_review maps an unknown/absent qa_verdict to
                   QA_FAILED, so a malformed Agent 2 response lands here and
                   would otherwise invalidate a sound verdict while asserting a
                   finding that was never made.
"""
import sys
import xml.etree.ElementTree as ET

import app

AGENT1 = """<SprintZero_response>
  <attributes>
    <response_type>EVALUATION</response_type>
    <qa_status>QA_PENDING</qa_status>
  </attributes>
  <verdict>
    <classification>UNCERTAIN</classification>
    <confidence_score>0.61</confidence_score>
    <stability_status>EMERGING</stability_status>
    <one_line_verdict>Stale cache, not forecast modelling, drives the trust complaints.</one_line_verdict>
  </verdict>
</SprintZero_response>"""

def qa_review(verdict, required_action=None, blocking=None):
    ra = f"<required_action>{required_action}</required_action>" if required_action else ""
    bf = f"<blocking_findings>{blocking}</blocking_findings>" if blocking else ""
    return ET.fromstring(
        f"<qa_review><overall_qa_stamp><qa_verdict>{verdict}</qa_verdict>"
        f"{ra}{bf}</overall_qa_stamp></qa_review>"
    )

def render(qr):
    """Mirror the /qa handler's render path exactly."""
    from agents import agent2_qa
    root = ET.fromstring(AGENT1)
    agent2_qa.merge_qa_review(root, qr)
    status = root.findtext("attributes/qa_status")
    ra, bf, degraded = app.qa_gate_reason(qr, status)
    with app.app.app_context():
        from flask import render_template
        inval = None
        if status == "QA_FAILED":
            inval = render_template(
                "partials/verdict_invalidation.html",
                required_action=ra, blocking=bf, degraded=degraded,
            )
        surface = render_template(
            "partials/qa_surface.html", root=root,
            qa_checks=[], qa_degraded=degraded,
        )
    return status, degraded, inval, surface

violations = []

# --- 1. PASS: nothing happens to the verdict --------------------------------
status, degraded, inval, surface = render(qa_review("QA_PASSED"))
if status != "QA_PASSED":
    violations.append(f"PASS PATH: qa_status is {status!r}, expected QA_PASSED.")
if degraded:
    violations.append("PASS PATH: a passing review must never be marked degraded.")
if inval is not None:
    violations.append(
        "PASS PATH VIOLATION: invalidation fragment produced on QA_PASSED. "
        "A passing verdict must render exactly as it did before this feature."
    )
if "QA-FAILED" in surface or "QA INCOMPLETE" in surface:
    violations.append("PASS PATH: failure language leaked into a passing QA surface.")

# QA_PASSED_WITH_NOTES is also a pass per the schema.
status_n, _, inval_n, _ = render(qa_review("QA_PASSED_WITH_NOTES"))
if status_n != "QA_PASSED" or inval_n is not None:
    violations.append(
        f"PASS PATH: QA_PASSED_WITH_NOTES resolved to {status_n!r} with "
        f"invalidation={inval_n is not None}; it is a pass and must not invalidate."
    )

# --- 2. FAIL with a reason: invalidated AND explained -----------------------
ACTION = "Counter-signal R03 must be explicitly argued before commit."
BLOCKING = "Counter-Signal Engagement: R03 listed but not argued."
status, degraded, inval, surface = render(qa_review("QA_FAILED", ACTION, BLOCKING))
if status != "QA_FAILED":
    violations.append(f"FAIL PATH: qa_status is {status!r}, expected QA_FAILED.")
if degraded:
    violations.append("FAIL PATH: a review carrying required_action must not be degraded.")
if inval is None:
    violations.append("FAIL PATH VIOLATION: no invalidation fragment on QA_FAILED.")
else:
    if "QA-FAILED" not in inval:
        violations.append("FAIL PATH VIOLATION: no QA-FAILED stamp beside the verdict.")
    if ACTION not in inval:
        violations.append(
            "FAIL PATH VIOLATION: required_action absent from the invalidation surface. "
            "An invalidated verdict must say why and what to do."
        )
    if BLOCKING not in inval:
        violations.append("FAIL PATH: blocking_findings not reachable from the verdict.")

# --- 3. FAIL with no reason: degraded, not a fabricated finding -------------
status, degraded, inval, surface = render(qa_review("QA_FAILED"))
if not degraded:
    violations.append(
        "DEGRADED VIOLATION: QA_FAILED with no required_action and no "
        "blocking_findings was not flagged degraded."
    )
if inval is None:
    violations.append("DEGRADED: verdict left unmarked despite being blocked.")
else:
    if "QA-FAILED" in inval:
        violations.append(
            "DEGRADED VIOLATION: reasonless block rendered as a substantive "
            "QA-FAILED. Nothing was checked - it must not assert a finding."
        )
    if "QA INCOMPLETE" not in inval:
        violations.append("DEGRADED VIOLATION: missing 'QA INCOMPLETE' framing.")
if "QA INCOMPLETE" not in surface:
    violations.append("DEGRADED VIOLATION: QA surface still reports a plain failure.")

# --- 4. The malformed-Agent-2 path lands in degraded, not in failure --------
malformed = ET.fromstring("<qa_review><garbage/></qa_review>")
status, degraded, inval, _ = render(malformed)
if status != "QA_FAILED":
    violations.append(f"MALFORMED: expected QA_FAILED gate, got {status!r}.")
if not degraded:
    violations.append(
        "MALFORMED VIOLATION: qa_review with no overall_qa_stamp was treated as "
        "a real failure. This is the exact path that would strike through a "
        "sound verdict with no explanation."
    )

print("===== QA GATE BOUNDARY ASSERTIONS =====")
if violations:
    for v in violations:
        sys.stdout.write(f"FAIL: {v}\n")
    sys.exit(1)
print("PASS: pass renders unchanged; failure invalidates and explains;")
print("      reasonless failure degrades instead of fabricating a finding.")

"""History probe: a verdict must survive the tab that produced it.

A theme costs ~80s of synthesis and ~50s of adversarial review. Before this it
existed only in the browser tab that produced it. Three things must hold:

  recorded    Every synthesis turn writes exactly one record, against the right
              project. A missing record is 130 seconds of work thrown away.
  replayable  A stored verdict re-renders through the same right_pane.html the
              live flow uses — including a QA failure, which must still show as
              struck through. A history view that flatters a blocked verdict
              would be worse than having none.
  isolated    One project's history must never appear under another's.

Also asserts what is NOT recorded: intake and challenge turns are conversation,
not verdicts, and would only clutter the record.

Free and deterministic — no model calls.
"""
import re
import sys
import xml.etree.ElementTree as ET

import app
import history
import resources
import state

violations = []
CREATED = []


def document(response_type="EVALUATION", classification="UNCERTAIN",
             qa_verdict="QA_PASSED", qa_status="QA_PASSED", with_stamp=True):
    stamp = ""
    if with_stamp:
        stamp = (f"<overall_qa_stamp><qa_verdict>{qa_verdict}</qa_verdict>"
                 "<required_action>Argue counter-signal R03 before committing."
                 "</required_action>"
                 "<blocking_findings>Counter-Signal Engagement: R03 unargued."
                 "</blocking_findings></overall_qa_stamp>")
    return ET.fromstring(f"""<SprintZero_response>
  <attributes>
    <response_type>{response_type}</response_type>
    <qa_status>{qa_status}</qa_status>
  </attributes>
  <verdict>
    <classification>{classification}</classification>
    <confidence_score>0.61</confidence_score>
    <stability_status>EMERGING</stability_status>
    <one_line_verdict>Stale cache, not forecast modelling, drives the complaints.</one_line_verdict>
  </verdict>
  <evidence_chain><corroborating_evidence>
    <unit><id>R01</id><signal>MARKER_EVIDENCE</signal></unit>
  </corroborating_evidence></evidence_chain>
  <qa_review>{stamp}</qa_review>
</SprintZero_response>""")


alpha = state.create_project("Hist Alpha", "NEW_PRODUCT", "Whether X.")
beta = state.create_project("Hist Beta", "UNKNOWN", "Whether Y.")
CREATED += [alpha["project_id"], beta["project_id"]]
A, B = alpha["project_id"], beta["project_id"]

# --- 1. Recording ------------------------------------------------------------
history.record(A, "SZ-20260909-001", "Users cross-check a second app.", document())
history.record(A, "SZ-20260909-002", "Latency drives churn.",
               document(classification="WEAK", qa_verdict="QA_FAILED", qa_status="QA_FAILED"))

if history.count(A) != 2:
    violations.append(f"RECORDING: expected 2 records, got {history.count(A)}.")

rows = history.list_records(A)
if [r["query_id"] for r in rows] != ["SZ-20260909-002", "SZ-20260909-001"]:
    violations.append(f"ORDER: records are not newest-first; got {[r['query_id'] for r in rows]}.")
if any("document_xml" in r for r in rows):
    violations.append("LIST: the full document is being returned for the list view.")
first = next(r for r in rows if r["query_id"] == "SZ-20260909-001")
for field, expected in (("classification", "UNCERTAIN"), ("qa_status", "QA_PASSED"),
                        ("theme", "Users cross-check a second app.")):
    if first.get(field) != expected:
        violations.append(f"SUMMARY: {field} was {first.get(field)!r}, expected {expected!r}.")
print(f"1. recording : {history.count(A)} records, newest first")

# --- 2. What must NOT be recorded -------------------------------------------
for response_type in ("INTAKE", "CHALLENGE", "PARSE_ERROR", "REFUSAL"):
    history.record(A, "SZ-20260909-009", "not a verdict", document(response_type=response_type))
if history.count(A) != 2:
    violations.append(
        f"NOISE: a non-synthesis turn was recorded; count rose to {history.count(A)}. "
        "Intake and challenge turns are conversation, not verdicts."
    )
# A forged query id must not become a filename.
for bad in ("../escape", "SZ-bad", "", "SZ-20260909-001/../x"):
    if history.record(A, bad, "t", document()) is not None:
        violations.append(f"QUERY ID: {bad!r} was accepted as a record name.")
if history.count(A) != 2:
    violations.append("QUERY ID: a rejected id still wrote a file.")
print("2. filtering : non-synthesis turns and forged ids refused")

# --- 3. Isolation ------------------------------------------------------------
history.record(B, "SZ-20260909-001", "Beta's own theme.", document())
if history.count(B) != 1:
    violations.append(f"ISOLATION: beta has {history.count(B)} records, expected 1.")
if len(history.list_records(A)) != 2:
    violations.append("ISOLATION: writing to one project changed another's history.")
beta_row = history.list_records(B)[0]
if beta_row["theme"] != "Beta's own theme.":
    violations.append(
        "CROSS-PROJECT LEAK: a record written to one project was read from another "
        "under the same query id."
    )
print(f"3. isolation : alpha={history.count(A)} beta={history.count(B)} "
      "with colliding query ids")

# --- 4. Replay ----------------------------------------------------------------
root, entry = history.document(A, "SZ-20260909-001")
if root is None:
    violations.append("REPLAY: the stored document did not re-parse.")
elif root.findtext("verdict/classification") != "UNCERTAIN":
    violations.append("REPLAY: the stored document lost its verdict.")

http = app.app.test_client()


def element_classes(body, marker):
    """Class list of the first element matching `marker`.

    Matching against the whole page is useless here: every page inlines the
    stylesheet, so 'qa-invalidated' and 'qa-band-passed' appear as CSS
    selectors whether or not any element carries them.
    """
    m = re.search(rf'<div[^>]*class="([^"]*{marker}[^"]*)"', body)
    return m.group(1).split() if m else []

listing = http.get(f"/projects/{A}/history")
if listing.status_code != 200:
    violations.append(f"REPLAY: history list returned {listing.status_code}.")
elif b"SZ-20260909-002" not in listing.data:
    violations.append("REPLAY: the history list does not show its records.")

passed = http.get(f"/projects/{A}/history/SZ-20260909-001")
if passed.status_code != 200:
    violations.append(f"REPLAY: detail view returned {passed.status_code}.")
else:
    body = passed.data.decode()
    banner = element_classes(body, "verdict-banner")
    band = element_classes(body, "qa-band")
    if "MARKER_EVIDENCE" not in body:
        violations.append("REPLAY: the evidence chain did not re-render.")
    if "qa-band-passed" not in band:
        violations.append(f"REPLAY: a passed verdict's band is {band}, not passed.")
    if "Running…" in body:
        violations.append(
            "REPLAY: the QA band still says 'Running…' for a query that finished. "
            "There is no client to resolve it on a stored record."
        )
    if "qa-invalidated" in banner:
        violations.append(f"REPLAY: a passing verdict was rendered invalidated ({banner}).")

failed = http.get(f"/projects/{A}/history/SZ-20260909-002")
if failed.status_code != 200:
    violations.append(f"REPLAY: failed-verdict detail returned {failed.status_code}.")
else:
    body = failed.data.decode()
    banner = element_classes(body, "verdict-banner")
    band = element_classes(body, "qa-band")
    if "qa-invalidated" not in banner:
        violations.append(
            f"REPLAY FLATTERS A FAILURE: a blocked verdict re-rendered as valid "
            f"({banner}). The strikethrough is the whole point of the gate."
        )
    if "QA-FAILED" not in body:
        violations.append("REPLAY: the QA-FAILED stamp is missing from a stored failure.")
    if "Argue counter-signal R03" not in body:
        violations.append("REPLAY: required_action did not re-render with the failure.")
    if "qa-band-failed" not in band:
        violations.append(f"REPLAY: the Tier 1 band is {band}, not failed.")
print("4. replay    : passed renders clean, failed renders struck through")

# --- 5. Missing and corrupt records -------------------------------------------
if http.get(f"/projects/{A}/history/SZ-20260909-404").status_code != 404:
    violations.append("REPLAY: a missing record did not 404.")
if http.get(f"/projects/{A}/history/not-a-query-id").status_code != 404:
    violations.append("REPLAY: a malformed query id did not 404.")

corrupt = resources.history_dir(A, create=True) / "SZ-20260909-777.json"
corrupt.write_text("{ this is not json", encoding="utf-8")
rows = history.list_records(A)
if len(rows) != 2:
    violations.append(
        f"ROBUSTNESS: one corrupt record changed the list to {len(rows)} rows. "
        "A single bad file must not hide the rest of the history."
    )
corrupt.unlink()
print("5. robustness: missing 404s, corrupt record does not hide the others")

for pid in CREATED:
    state.delete_project(pid)

print("\n===== HISTORY ASSERTIONS =====")
if violations:
    for v in violations:
        sys.stdout.write(f"FAIL: {v}\n")
    sys.exit(1)
print("PASS: verdicts are recorded per project, replay through the live")
print("      renderer, and a blocked verdict stays blocked on replay.")

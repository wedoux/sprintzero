"""Phase 4 probe: end-to-end Agent 1 -> Agent 2 -> merge.

Mirrors the production flow in app.py's POST handler. Asserts:
  - Final document parses cleanly.
  - <qa_review> IS a direct child of <SprintZero_response> (Agent 2 appended it).
  - <qa_status> in attributes is QA_PASSED or QA_FAILED (not QA_PENDING).
  - Agent 1's spine survives the merge (verdict, evidence_chain, etc. still present).

This is the inverse of _probe_phase1_eval.py — there qa_review absence was correct;
here qa_review presence is correct. Both probes are run as Phase 4 regression.
"""
import sys
import xml.etree.ElementTree as ET

import state
from agents import agent2_qa
from app import (AGENT1_MODEL, AGENT2_MODEL, build_system_blocks, client,
                 load_corpora, parse_response)

THEME = (
    "Weather Underground iOS users experience a data-freshness failure mode in "
    "which the displayed temperature lags physical conditions, triggering "
    "cross-checks with a secondary weather app before users commit to outdoor plans."
)

project_state = state.load_state()
query_id = state.generate_query_id(project_state)
corpora = load_corpora()

sys.stdout.write(f"===== AGENT 1 (query_id={query_id}) =====\n")
import model_client

agent1_text, _final = model_client.stream_text(
    client,
    label="probe_agent1",
    model=AGENT1_MODEL,
    max_tokens=16000,
    system=build_system_blocks(corpora, project_state, query_id),
    messages=[{"role": "user", "content": THEME}],
)
root, parse_error = parse_response(agent1_text)
if root is None:
    sys.stdout.write(f"AGENT 1 PARSE FAILED: {parse_error}\n")
    sys.stdout.write(agent1_text + "\n")
    sys.exit(1)

response_type = root.findtext("attributes/response_type")
qa_status_after_agent1 = root.findtext("attributes/qa_status")
sys.stdout.write(f"Agent 1 response_type: {response_type}\n")
sys.stdout.write(f"Agent 1 qa_status    : {qa_status_after_agent1}\n")

if response_type not in ("EVALUATION", "GAP_FLAG"):
    sys.stdout.write(
        f"FAIL: expected synthesis response_type (EVALUATION/GAP_FLAG), got {response_type!r}. "
        "Phase 4 cannot exercise Agent 2 without synthesis output.\n"
    )
    sys.exit(1)

sys.stdout.write("\n===== AGENT 2 =====\n")
agent1_xml = ET.tostring(root, encoding="unicode")
qa_review, qa_error = agent2_qa.run_qa_review(client, AGENT2_MODEL, agent1_xml)
if qa_review is None:
    sys.stdout.write(f"AGENT 2 FAILED: {qa_error}\n")
    sys.exit(1)

sys.stdout.write(f"Agent 2 returned <qa_review> with {len(list(qa_review))} sub-elements.\n")

agent2_qa.merge_qa_review(root, qa_review)
final_xml = ET.tostring(root, encoding="unicode")

sys.stdout.write("\n===== POST-MERGE PARSE CHECK =====\n")
try:
    merged_root = ET.fromstring(final_xml)
except ET.ParseError as e:
    sys.stdout.write(f"MERGE PRODUCED INVALID XML: {e}\n")
    sys.exit(1)
sys.stdout.write("Final document parses cleanly.\n")

# === FULL-FLOW BOUNDARY ASSERTIONS =================================
# Phase 4 inverts the Phase 1 boundary: qa_review presence is now expected,
# and qa_status must have flipped out of QA_PENDING.
violations = []

if merged_root.find("qa_review") is None:
    violations.append(
        "FULL-FLOW VIOLATION: <qa_review> absent after merge. "
        "Agent 2 should have appended it as a direct child."
    )

# Spine survival — Agent 1's content must still be there.
spine = ["verdict", "evidence_chain", "reasoning_step", "falsification_attempt"]
for tag in spine:
    if merged_root.find(tag) is None:
        violations.append(
            f"FULL-FLOW VIOLATION: <{tag}> missing after merge. "
            "Agent 1's spine was damaged by the merge."
        )

final_qa_status = merged_root.findtext("attributes/qa_status")
if final_qa_status not in ("QA_PASSED", "QA_FAILED"):
    violations.append(
        f"FULL-FLOW VIOLATION: qa_status is {final_qa_status!r}, expected "
        "QA_PASSED or QA_FAILED after Agent 2 stamp."
    )

sys.stdout.write(f"Final qa_status     : {final_qa_status}\n")
qa_verdict = merged_root.find("qa_review/overall_qa_stamp")
if qa_verdict is not None:
    sys.stdout.write(f"Final qa_verdict    : {qa_verdict.findtext('qa_verdict')}\n")

sys.stdout.write("\n===== FULL-FLOW BOUNDARY ASSERTIONS =====\n")
if violations:
    for v in violations:
        sys.stdout.write(f"FAIL: {v}\n")
    sys.exit(1)
sys.stdout.write("PASS: qa_review appended; qa_status flipped; Agent 1 spine intact.\n")

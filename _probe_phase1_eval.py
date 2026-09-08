"""Phase 1 probe (EVALUATION specimen): inject project_context COMPLETE + theme, capture, parse-check, assert boundaries.

This is the Agent 1 probe. Its boundary assertions enforce the Agent 1 / Agent 2
authorship contract defined in:
  - agents/prompts/sprintzero_copilot_role_task.txt  (OUTPUT FORMAT section)
  - agents/prompts/sprintzero_output_schema.xml      (RULES block + qa_review element)

Phase 4 will introduce a separate Agent 2 probe whose qa_review assertion logic
treats a direct-child qa_review as expected output, not a violation. This probe
must only be run against raw Agent 1 output (no Agent 2 pass) — see the comment
on root.find('qa_review') below.
"""
import sys
import xml.etree.ElementTree as ET

from app import MODEL, build_system_blocks, client, load_corpora

USER_MESSAGE = """The project context for this query is COMPLETE. Treat the following as the established project_context record for this project. Do not produce an INTAKE response. Do not produce a CHALLENGE response on intake grounds. Proceed directly to evaluating the theme submitted below.

<project_context>
  <project_name>Weather Underground iOS — Trust Investigation</project_name>
  <project_type>EXISTING_PRODUCT_ITERATION</project_type>
  <research_objective>Determine whether reported forecast inaccuracy in Weather Underground iOS reviews is a forecast-model problem or a data-freshness problem, and which engineering workstream should own the fix.</research_objective>
  <business_decisions_pending>Engineering leadership must decide in the next sprint whether to allocate the Q3 trust-recovery budget to the forecast modelling team or to the iOS caching and refresh subsystem. Only one workstream can be funded.</business_decisions_pending>
  <prior_research_and_insights>None on file. Treat as first-pass synthesis on the current S-001 corpus.</prior_research_and_insights>
  <target_market>US iOS users of Weather Underground who have left an App Store review in 2022 to 2024. Scope is explicitly US-only for this evaluation.</target_market>
  <known_constraints>Engineering capacity is committed elsewhere through end of Q2. Only one workstream can be funded in Q3.</known_constraints>
  <primary_stakeholder>Engineering lead and product lead, jointly, deciding the Q3 budget allocation.</primary_stakeholder>
  <context_completeness>COMPLETE</context_completeness>
</project_context>

Theme to evaluate: Weather Underground iOS users experience a data-freshness failure mode in which the displayed temperature lags physical conditions, triggering cross-checks with a secondary weather app before users commit to outdoor plans."""

corpora = load_corpora()
response = client.messages.create(
    model=MODEL,
    max_tokens=16000,
    system=build_system_blocks(corpora),
    messages=[{"role": "user", "content": USER_MESSAGE}],
)
text = next((b.text for b in response.content if b.type == "text"), "")

sys.stdout.write("===== RAW MODEL OUTPUT =====\n")
sys.stdout.write(text)
sys.stdout.write("\n===== END RAW OUTPUT =====\n\n")

sys.stdout.write("===== PARSE CHECK =====\n")
try:
    root = ET.fromstring(text)
except ET.ParseError as e:
    sys.stdout.write(f"PARSE FAILED: {e}\n")
    sys.exit(1)

sys.stdout.write("OK — parsed cleanly with stdlib xml.etree.\n")
sys.stdout.write(f"root tag                       : {root.tag}\n")
top_level = [c.tag for c in root]
sys.stdout.write(f"top-level children             : {top_level}\n")
sys.stdout.write(f"process_challenge present      : {root.find('process_challenge') is not None}\n")
attrs = root.find('attributes')
if attrs is not None:
    sys.stdout.write(f"response_type                  : {attrs.findtext('response_type')!r}\n")
    sys.stdout.write(f"context_status                 : {attrs.findtext('context_status')!r}\n")
    sys.stdout.write(f"qa_status                      : {attrs.findtext('qa_status')!r}\n")
sys.stdout.write(f"verdict present                : {root.find('verdict') is not None}\n")
sys.stdout.write(f"behavioural_mechanism present  : {root.find('behavioural_mechanism') is not None}\n")
sys.stdout.write(f"evidence_chain present         : {root.find('evidence_chain') is not None}\n")
sys.stdout.write(f"reasoning_step present         : {root.find('reasoning_step') is not None}\n")
sys.stdout.write(f"falsification_attempt present  : {root.find('falsification_attempt') is not None}\n")
sys.stdout.write(f"decision_support present       : {root.find('decision_support') is not None}\n")
sys.stdout.write(f"tacit_knowledge_prompt present : {root.find('tacit_knowledge_prompt') is not None}\n")
sys.stdout.write(f"transfer_assumption_check pres : {root.find('transfer_assumption_check') is not None}\n")
sys.stdout.write(f"reframed_insight present       : {root.find('reframed_insight') is not None}\n")
sys.stdout.write(f"qa_review present              : {root.find('qa_review') is not None}\n")

# === BOUNDARY ASSERTIONS ============================================
# Enforces the Agent 1 / Agent 2 authorship boundary at runtime.
# Standing rule: every prompt-side boundary in this build has a probe-side
# assertion behind it. Eyeballing the output is not boundary verification.
#
# IMPORTANT — scope of this probe's qa_review check:
# `root.find('qa_review')` uses xml.etree's default ElementPath syntax,
# which matches DIRECT CHILDREN of `root` only. It does NOT recurse —
# recursion would require './/qa_review'. This is intentional, not
# incidental, and has two consequences:
#
#   1. No nested qa_review-named element anywhere deeper in the tree can
#      false-positive this assertion. (None should exist per the schema,
#      but the non-recursion is the structural guarantee.)
#
#   2. This is the Agent 1 probe. Phase 4 will introduce Agent 2, which
#      legitimately appends qa_review as a direct child of
#      <SprintZero_response>. Agent 2's output must not be run through
#      this probe — it would correctly fail here. Phase 4 needs its own
#      probe (or probe mode) whose qa_review assertion treats a
#      direct-child qa_review as expected, not as a violation.
violations = []

if root.find('qa_review') is not None:
    violations.append(
        "BOUNDARY VIOLATION: <qa_review> element present in Agent 1 output. "
        "qa_review is Agent 2's exclusive responsibility; Agent 1 must omit it."
    )

if attrs is not None:
    response_type = attrs.findtext('response_type')
    qa_status = attrs.findtext('qa_status')
    if response_type in ('EVALUATION', 'GAP_FLAG'):
        expected = 'QA_PENDING'
    elif response_type in ('INTAKE', 'CHALLENGE', 'REFUSAL', 'PARTIAL'):
        expected = 'QA_NOT_APPLICABLE'
    else:
        expected = None
    if expected is not None and qa_status != expected:
        violations.append(
            f"BOUNDARY VIOLATION: qa_status is {qa_status!r}, expected "
            f"{expected!r} for response_type={response_type!r}. "
            f"Agent 1 must not set QA_PASSED or QA_FAILED."
        )

sys.stdout.write("\n===== BOUNDARY ASSERTIONS =====\n")
if violations:
    for v in violations:
        sys.stdout.write(f"FAIL: {v}\n")
    sys.exit(1)
sys.stdout.write("PASS: qa_review omitted; qa_status correct for response_type.\n")

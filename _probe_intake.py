"""Intake probe: a new project must be interviewed, not assumed complete.

The creation form asks for three fields. The other required ones are collected
by Agent 1's INTAKE protocol — machinery that has existed in the prompt and the
schema since the beginning but was unreachable, because app.py unconditionally
told Agent 1 "Do not produce an INTAKE response".

That conditional is the whole feature, and both sides of it fail silently:

  stuck asking     A COMPLETE project that still gets the intake instruction
                   would interview the researcher forever and never evaluate.
  never asking     An INCOMPLETE project that gets the suppression block would
                   synthesise against context nobody supplied, and confidently
                   cite a target market and a pending decision that do not exist.

Also asserts the completion path: the project_context Agent 1 returns must be
persisted, or the researcher answers the same questions on every query.

Free and deterministic — the model is stubbed.
"""
import json
import sys

import app
import model_client
import state

violations = []
CREATED = []

SUPPRESSION = "Do not produce an INTAKE response"
INSTRUCTION = "Run the INTAKE PROTOCOL"


def blocks_text(project):
    """The system prompt app.py would build for this project."""
    blocks = app.build_system_blocks(app.load_corpora(), project, "SZ-TEST-001")
    return "\n".join(b["text"] for b in blocks)


# --- 1. The conditional, both ways -----------------------------------------
incomplete = state.create_project(
    "Intake Probe", "NEW_PRODUCT", "Whether onboarding drop-off is comprehension or trust.")
CREATED.append(incomplete["project_id"])

text = blocks_text(incomplete)
if INSTRUCTION not in text:
    violations.append(
        "NEVER ASKING: an INCOMPLETE project was not given the intake instruction. "
        "It would synthesise against context nobody supplied."
    )
if SUPPRESSION in text:
    violations.append(
        "NEVER ASKING: the intake-suppression block was sent to an INCOMPLETE "
        "project. This is the exact line that made intake dead code."
    )
for field in ("business_decisions_pending", "target_market"):
    if field not in text:
        violations.append(f"INTAKE: prompt does not name the missing field {field!r}.")
# What the form already captured must not be asked for again.
if "Whether onboarding drop-off" not in text:
    violations.append("INTAKE: captured research_objective was not carried into the prompt.")
print(f"1. incomplete: instruction={INSTRUCTION in text} suppression={SUPPRESSION in text}")

complete = state.load_project("weather-underground-redesign")
if complete is None:
    violations.append("SETUP: the migrated project is missing; cannot test the COMPLETE side.")
else:
    text = blocks_text(complete)
    if SUPPRESSION not in text:
        violations.append(
            "STUCK ASKING: a COMPLETE project did not get the suppression block. "
            "It would be interviewed forever and never evaluate a theme."
        )
    if INSTRUCTION in text:
        violations.append("STUCK ASKING: a COMPLETE project was told to run intake.")
    print(f"2. complete  : instruction={INSTRUCTION in text} suppression={SUPPRESSION in text}")

# --- 2. The completion path -------------------------------------------------
INTAKE_RESPONSE = """<SprintZero_response>
  <attributes>
    <response_type>INTAKE</response_type>
    <qa_status>QA_NOT_APPLICABLE</qa_status>
  </attributes>
  <project_context>
    <project_name>Intake Probe</project_name>
    <project_type>NEW_PRODUCT</project_type>
    <research_objective>Whether onboarding drop-off is comprehension or trust.</research_objective>
    <business_decisions_pending>Whether to rewrite onboarding copy or add a trust panel.</business_decisions_pending>
    <target_market>First-time UK users on mobile web.</target_market>
    <known_constraints>No engineering capacity until Q3.</known_constraints>
    <primary_stakeholder>Head of Product.</primary_stakeholder>
    <context_completeness>COMPLETE</context_completeness>
  </project_context>
</SprintZero_response>"""


class FakeUsage:
    input_tokens = output_tokens = 1
    cache_read_input_tokens = cache_creation_input_tokens = 0


class FakeFinal:
    usage = FakeUsage()
    stop_reason = "end_turn"
    content = []


def stub(text):
    def _stub(client, *, on_progress=None, **kw):
        if on_progress is not None:
            on_progress(text)
        return text, FakeFinal()
    return _stub


def post_ask(project_id, body, question="a theme"):
    original = model_client.stream_text
    model_client.stream_text = stub(body)
    try:
        response = app.app.test_client().post(
            f"/projects/{project_id}/ask", data={"question": question})
        raw, events = "", []
        for chunk in response.response:
            raw += chunk.decode("utf-8")
        for frame in raw.split("\n\n"):
            name = data = None
            for line in frame.split("\n"):
                if line.startswith("event: "):
                    name = line[7:].strip()
                elif line.startswith("data: "):
                    data = line[6:]
            if name and data is not None:
                events.append((name, json.loads(data)))
        return events
    finally:
        model_client.stream_text = original


pid = incomplete["project_id"]
events = post_ask(pid, INTAKE_RESPONSE)
done = next((p for n, p in events if n == "done"), None)

if done is None or done.get("response_type") != "INTAKE":
    violations.append(f"COMPLETION: expected an INTAKE response, got {done and done.get('response_type')!r}.")

after = state.load_project(pid)
if not state.context_is_complete(after):
    violations.append(
        "COMPLETION: the project_context returned by INTAKE was not persisted. "
        "The researcher would be asked the same questions on every query."
    )
if after["project_context"].get("target_market") != "First-time UK users on mobile web.":
    violations.append("COMPLETION: a field from the intake response was not stored.")
if state.missing_context_fields(after):
    violations.append(f"COMPLETION: still missing {state.missing_context_fields(after)}.")
print(f"3. completion: complete={state.context_is_complete(after)} "
      f"missing={state.missing_context_fields(after)}")

# The next query must now be a synthesis, not another interview.
text = blocks_text(after)
if SUPPRESSION not in text or INSTRUCTION in text:
    violations.append(
        "COMPLETION: after intake completed, the project is still being told to "
        "run intake. It would never reach a verdict."
    )

# --- 3. A partial intake must not complete the project ----------------------
partial = state.create_project(
    "Partial Probe", "UNKNOWN", "Whether pricing confusion drives churn.")
CREATED.append(partial["project_id"])
# Still mid-interview: not COMPLETE, and the objective comes back empty
# because the copilot has not asked about it. An empty incoming value must
# never blank what the creation form already captured.
PARTIAL_RESPONSE = INTAKE_RESPONSE.replace(
    "<context_completeness>COMPLETE</context_completeness>",
    "<context_completeness>INCOMPLETE</context_completeness>",
).replace(
    "<target_market>First-time UK users on mobile web.</target_market>", "",
).replace(
    "<research_objective>Whether onboarding drop-off is comprehension or trust.</research_objective>",
    "<research_objective></research_objective>",
)
post_ask(partial["project_id"], PARTIAL_RESPONSE)
after_partial = state.load_project(partial["project_id"])
if state.context_is_complete(after_partial):
    violations.append(
        "PARTIAL INTAKE: a response that did not claim COMPLETE marked the "
        "project complete anyway."
    )
if after_partial["project_context"].get("research_objective") != \
        "Whether pricing confusion drives churn.":
    violations.append(
        "PARTIAL INTAKE: an incoming context overwrote a field the creation form "
        "had already captured."
    )
print(f"4. partial   : complete={state.context_is_complete(after_partial)}")

for pid in CREATED:
    state.delete_project(pid)

print("\n===== INTAKE ASSERTIONS =====")
if violations:
    for v in violations:
        sys.stdout.write(f"FAIL: {v}\n")
    sys.exit(1)
print("PASS: incomplete projects are interviewed, complete ones are not,")
print("      and a completing intake is persisted.")

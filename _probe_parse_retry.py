"""Parse-retry probe: a malformed generation must not cost the whole run.

The model intermittently emits structurally invalid XML — roughly one Agent 1
run in six — and before this the entire ~80s generation was lost when it did,
with the evidence surviving only in the browser pane that reported it.

Asserts, with the model stubbed so this is deterministic and free:

  1. Bad then good  -> retried once, the good result is returned, the reader is
                       told a retry happened, and the bad output is on disk.
  2. Bad then bad   -> PARSE_ERROR, both artefacts saved, and the message says
                       it is a model fault rather than blaming the theme.
  3. Good first try -> no retry, no artefact, no wasted call.
  4. Agent 2        -> same retry behaviour on its own parse failure.
"""
import json
import sys

import app
import model_client
import resources
from agents import agent2_qa

GOOD = """<SprintZero_response>
  <attributes><response_type>EVALUATION</response_type><qa_status>QA_PENDING</qa_status></attributes>
  <verdict>
    <classification>UNCERTAIN</classification>
    <confidence_score>0.61</confidence_score>
    <stability_status>EMERGING</stability_status>
    <one_line_verdict>Stale cache, not forecast modelling.</one_line_verdict>
  </verdict>
</SprintZero_response>"""

# Mismatched tag — the exact fault seen in the wild.
BAD = """<SprintZero_response>
  <attributes><response_type>EVALUATION</response_type></attributes>
  <verdict><classification>WEAK</classification></verdicts>
</SprintZero_response>"""

GOOD_QA = ("<qa_review><overall_qa_stamp><qa_verdict>QA_PASSED</qa_verdict>"
           "</overall_qa_stamp></qa_review>")
BAD_QA = "<qa_review><overall_qa_stamp><qa_verdict>QA_PASSED</qa_stamp></qa_review>"


class FakeUsage:
    input_tokens = output_tokens = 1
    cache_read_input_tokens = cache_creation_input_tokens = 0


class FakeFinal:
    usage = FakeUsage()
    stop_reason = "end_turn"
    content = []


def stub(responses, counter):
    def _stub(client, *, label, model, max_tokens, system, messages,
              on_progress=None, **kw):
        text = responses[min(counter["n"], len(responses) - 1)]
        counter["n"] += 1
        if on_progress is not None:
            on_progress(text)
        return text, FakeFinal()
    return _stub


def read_events(response):
    events = []
    buffer = ""
    for chunk in response.response:
        buffer += chunk.decode("utf-8")
        while "\n\n" in buffer:
            frame, buffer = buffer.split("\n\n", 1)
            name = data = None
            for line in frame.split("\n"):
                if line.startswith("event: "):
                    name = line[7:].strip()
                elif line.startswith("data: "):
                    data = line[6:]
            if name and data is not None:
                events.append((name, json.loads(data)))
    return events


def artefacts():
    return set(p.name for p in resources.diagnostics_dir().glob("*.txt"))


violations = []
original = model_client.stream_text
client_t = app.app.test_client()


def run_ask(responses):
    before = artefacts()
    counter = {"n": 0}
    model_client.stream_text = stub(responses, counter)
    try:
        events = read_events(client_t.post("/ask", data={"question": "probe theme"}))
    finally:
        model_client.stream_text = original
    return events, counter["n"], artefacts() - before


# --- 1. bad then good -------------------------------------------------------
events, calls, new = run_ask([BAD, GOOD])
names = [n for n, _ in events]
done = next((p for n, p in events if n == "done"), None)
retries = [p for n, p in events if n == "progress" and p.get("retry")]

print(f"1. bad->good : calls={calls} retries={len(retries)} artefacts={len(new)} "
      f"type={done and done.get('response_type')}")
if calls != 2:
    violations.append(f"RETRY: expected 2 model calls after a parse failure, got {calls}.")
if not retries:
    violations.append(
        "RETRY SILENT: the reader was not told a retry happened. An extra ~80s "
        "wait with no explanation reads as a hang."
    )
if done is None or done.get("response_type") != "EVALUATION":
    violations.append(
        f"RETRY: recovered result not returned; got {done and done.get('response_type')!r}."
    )
if len(new) != 1:
    violations.append(f"ARTEFACT: expected 1 saved failure, got {len(new)}.")

# --- 2. bad then bad --------------------------------------------------------
events, calls, new = run_ask([BAD, BAD])
done = next((p for n, p in events if n == "done"), None)
print(f"2. bad->bad  : calls={calls} artefacts={len(new)} "
      f"type={done and done.get('response_type')}")
if calls != 2:
    violations.append(f"RETRY: expected exactly 2 attempts, got {calls} — no infinite retry.")
if done is None or done.get("response_type") != "PARSE_ERROR":
    violations.append("DOUBLE FAILURE: should surface PARSE_ERROR.")
else:
    pane = done.get("right_pane_html", "")
    if "Retried once" not in pane:
        violations.append("DOUBLE FAILURE: pane does not say a retry was attempted.")
    if "not a problem with the theme" not in pane:
        violations.append(
            "DOUBLE FAILURE: pane does not tell the researcher this is a model "
            "fault. They will otherwise assume their theme was rejected."
        )
    if "Saved for diagnosis" not in pane:
        violations.append("DOUBLE FAILURE: pane does not say where the output was saved.")
if len(new) != 2:
    violations.append(f"ARTEFACT: expected 2 saved failures, got {len(new)}.")

# --- 3. good first time -----------------------------------------------------
events, calls, new = run_ask([GOOD])
retries = [p for n, p in events if n == "progress" and p.get("retry")]
print(f"3. good      : calls={calls} retries={len(retries)} artefacts={len(new)}")
if calls != 1:
    violations.append(f"WASTE: a clean parse must cost one call, got {calls}.")
if retries:
    violations.append("WASTE: retry announced on a clean run.")
if new:
    violations.append("WASTE: artefact written for a run that did not fail.")

# --- 4. Agent 2 -------------------------------------------------------------
for label, responses, expect_calls, expect_ok in (
    ("bad->good", [BAD_QA, GOOD_QA], 2, True),
    ("bad->bad", [BAD_QA, BAD_QA], 2, False),
    ("good", [GOOD_QA], 1, True),
):
    before = artefacts()
    counter = {"n": 0}
    model_client.stream_text = stub(responses, counter)
    try:
        review, err = agent2_qa.run_qa_review(None, "m", "<SprintZero_response/>")
    finally:
        model_client.stream_text = original
    got_ok = review is not None
    print(f"4. agent2 {label:<10}: calls={counter['n']} ok={got_ok} "
          f"artefacts={len(artefacts() - before)}")
    if counter["n"] != expect_calls:
        violations.append(
            f"AGENT 2 {label}: expected {expect_calls} calls, got {counter['n']}."
        )
    if got_ok != expect_ok:
        violations.append(f"AGENT 2 {label}: expected ok={expect_ok}, got {got_ok} ({err}).")

print("\n===== PARSE RETRY ASSERTIONS =====")
if violations:
    for v in violations:
        sys.stdout.write(f"FAIL: {v}\n")
    sys.exit(1)
print("PASS: one retry on malformed output, bounded; artefacts kept; clean runs")
print("      cost nothing extra; double failure explains itself.")

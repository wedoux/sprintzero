"""Latency measurement for the QA pass. Measures only — changes nothing.

Answers the five questions the optimisation decision depends on:

  1. How long does Agent 2 actually take, versus Agent 1?
  2. Exactly how big is Agent 2's prefix, and how much of it is the output
     schema it does not author?
  3. Is the prompt cache being hit at all? (`cache_control` is set and has
     never been verified.)
  4. Is the time going into input processing or output generation?
  5. How much of the perceived wait is the client's own pacing floor?

Run:  ./venv/bin/python _probe_qa_latency.py [n_runs]

Every run costs real API calls — two Opus generations per run.
"""
import statistics
import sys
import xml.etree.ElementTree as ET
from time import perf_counter

import instrumentation
import state
from agents import agent2_qa
from app import MODEL, build_system_blocks, client, load_corpora, parse_response

N_RUNS = int(sys.argv[1]) if len(sys.argv) > 1 else 3

THEME = (
    "Weather Underground iOS users experience a data-freshness failure mode in "
    "which the displayed temperature lags physical conditions, triggering "
    "cross-checks with a secondary weather app before users commit to outdoor plans."
)

# Client-side pacing floor, from templates/index.html. Two paced Phase 2 entries
# means one unconditional sleep, plus one gap between the two gated entries.
PHASE2_PACE_MS = 5000
GATED_PACE_MS = 500
CLIENT_FLOOR_S = (PHASE2_PACE_MS + GATED_PACE_MS) / 1000.0

out = sys.stdout.write


def hr(title):
    out(f"\n{'=' * 68}\n{title}\n{'=' * 68}\n")


# ---------------------------------------------------------------- prefix size
hr("1. AGENT 2 PREFIX COMPOSITION")

blocks = agent2_qa.build_qa_system_blocks()
schema_chars = len(agent2_qa.OUTPUT_SCHEMA)
protocol_chars = len(agent2_qa.QA_PROTOCOL)
framework_chars = len(agent2_qa.FRAMEWORK)

prefix_tokens = client.messages.count_tokens(
    model=MODEL,
    system=blocks,
    messages=[{"role": "user", "content": "x"}],
).input_tokens

schema_only_tokens = client.messages.count_tokens(
    model=MODEL,
    system=[{"type": "text", "text": agent2_qa.OUTPUT_SCHEMA}],
    messages=[{"role": "user", "content": "x"}],
).input_tokens

out(f"  QA protocol          {protocol_chars:>7,} chars\n")
out(f"  Output schema        {schema_chars:>7,} chars   <- Agent 2 authors only <qa_review>\n")
out(f"  Framework A-001      {framework_chars:>7,} chars\n")
out(f"  ----------------------------------------\n")
out(f"  Measured prefix      {prefix_tokens:>7,} tokens\n")
out(f"  Schema alone         {schema_only_tokens:>7,} tokens "
    f"({schema_only_tokens / prefix_tokens:.0%} of the prefix)\n")

# ------------------------------------------------------------------- the runs
hr(f"2. END-TO-END RUNS (n={N_RUNS})")

rows = []
for i in range(1, N_RUNS + 1):
    out(f"\n--- run {i}/{N_RUNS} ---\n")
    project_state = state.load_state()
    query_id = state.generate_query_id(project_state)
    corpora = load_corpora()

    t0 = perf_counter()
    a1 = instrumentation.observe(
        "measure_agent1",
        lambda: client.messages.create(
            model=MODEL,
            max_tokens=16000,
            system=build_system_blocks(corpora, project_state, query_id),
            messages=[{"role": "user", "content": THEME}],
        ),
        run=i,
    )
    a1_s = perf_counter() - t0

    text = next((b.text for b in a1.content if b.type == "text"), "")
    root, err = parse_response(text)
    if root is None:
        out(f"  Agent 1 parse failed: {err}\n")
        continue
    if root.findtext("attributes/response_type") not in ("EVALUATION", "GAP_FLAG"):
        out(f"  Agent 1 returned {root.findtext('attributes/response_type')!r}; "
            "cannot exercise Agent 2. Skipping run.\n")
        continue

    agent1_xml = ET.tostring(root, encoding="unicode")

    t0 = perf_counter()
    qa_review, qa_err = agent2_qa.run_qa_review(client, MODEL, agent1_xml)
    a2_s = perf_counter() - t0
    if qa_review is None:
        out(f"  Agent 2 failed: {qa_err}\n")
        continue

    trace = instrumentation.load_trace()
    a1_u = next((t for t in reversed(trace) if t["label"] == "measure_agent1"), {})
    a2_u = next((t for t in reversed(trace) if t["label"] == "agent2_qa"), {})

    rows.append({
        "a1_s": a1_s, "a2_s": a2_s,
        "a2_in": a2_u.get("input_tokens"),
        "a2_out": a2_u.get("output_tokens"),
        "a2_cache_read": a2_u.get("cache_read_input_tokens"),
        "a2_cache_write": a2_u.get("cache_creation_input_tokens"),
        "a1_out": a1_u.get("output_tokens"),
        "xml_chars": len(agent1_xml),
    })
    r = rows[-1]
    out(f"  Agent 1  {a1_s:6.2f}s   out={r['a1_out']} tok\n")
    out(f"  Agent 2  {a2_s:6.2f}s   in={r['a2_in']} out={r['a2_out']} "
        f"cache_read={r['a2_cache_read']} cache_write={r['a2_cache_write']}\n")

# ------------------------------------------------------------------- verdict
hr("3. WHERE THE TIME GOES")

if not rows:
    out("No successful runs — nothing to report.\n")
    sys.exit(1)

a1_times = [r["a1_s"] for r in rows]
a2_times = [r["a2_s"] for r in rows]
med_a2 = statistics.median(a2_times)

out(f"  Agent 1   median {statistics.median(a1_times):6.2f}s   "
    f"range {min(a1_times):.2f}-{max(a1_times):.2f}s\n")
out(f"  Agent 2   median {med_a2:6.2f}s   "
    f"range {min(a2_times):.2f}-{max(a2_times):.2f}s\n")

out(f"\n  Output tokens (Agent 2): {[r['a2_out'] for r in rows]}\n")
tps = [r["a2_out"] / r["a2_s"] for r in rows if r["a2_out"]]
if tps:
    out(f"  Effective output rate  : {statistics.median(tps):.1f} tok/s\n")

out("\n  CACHE:\n")
reads = [r["a2_cache_read"] or 0 for r in rows]
writes = [r["a2_cache_write"] or 0 for r in rows]
out(f"    cache_read  per run: {reads}\n")
out(f"    cache_write per run: {writes}\n")
if len(reads) > 1 and all(v == 0 for v in reads[1:]):
    out("    -> COLD ON EVERY RUN. cache_control is set but never hit;\n"
        "       each QA pass pays full input cost and full input latency.\n")
elif any(v > 0 for v in reads[1:]):
    out("    -> Cache IS being hit on repeat runs.\n")

out("\n  CLIENT-PERCEIVED vs SERVER:\n")
out(f"    server median          {med_a2:6.2f}s\n")
out(f"    client pacing floor    {CLIENT_FLOOR_S:6.2f}s  (unconditional, from index.html)\n")
perceived = max(med_a2, CLIENT_FLOOR_S)
out(f"    user actually waits    {perceived:6.2f}s\n")
if CLIENT_FLOOR_S > med_a2:
    out(f"    -> The floor EXCEEDS the real call by {CLIENT_FLOOR_S - med_a2:.2f}s.\n"
        "       That much of the wait is pure client-side theatre.\n")
else:
    out(f"    -> Floor is not binding; {med_a2 - CLIENT_FLOOR_S:.2f}s of real wait "
        "sits above it.\n")

out("\n")

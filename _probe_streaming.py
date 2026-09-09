"""Streaming probe: the SSE endpoints must emit real progress, not just a result.

Both routes were converted from blocking JSON to Server-Sent Events so the
researcher sees work land as it happens. The failure mode worth catching is a
stream that technically works but reports nothing until the end — that is the
blocking behaviour again, wearing a different transport.

Asserts, against the real endpoints:
  1. /ask emits section-completion events BEFORE its done frame.
  2. /qa emits per-check events BEFORE its done frame, with parsed verdicts.
  3. Progress is spread across the call, not dumped at the end (first event
     must arrive well before the last).
  4. The done frames still carry everything the client needs.

Costs two real generations.
"""
import json
import sys
from time import perf_counter

import app

out = sys.stdout.write

THEME = (
    "Weather Underground iOS users experience a data-freshness failure mode in "
    "which the displayed temperature lags physical conditions, triggering "
    "cross-checks with a secondary weather app before users commit to outdoor plans."
)


def read_sse(response, start):
    """Yield (event_name, payload, seconds_since_start) from a streamed response."""
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
                yield name, json.loads(data), perf_counter() - start


violations = []
client = app.app.test_client()

# Endpoints are project-scoped; exercise the migrated founding project.
PROJECT = "weather-underground-redesign"

# --------------------------------------------------------------- /ask stream
out("===== /ask =====\n")
start = perf_counter()
resp = client.post(f"/projects/{PROJECT}/ask", data={"question": THEME})
if resp.mimetype != "text/event-stream":
    out(f"FAIL: /ask returned {resp.mimetype}, expected text/event-stream\n")
    sys.exit(1)

ask_progress, ask_done, early_verdict = [], None, None
for name, payload, at in read_sse(resp, start):
    if name == "progress":
        ask_progress.append((payload["label"], at))
        out(f"  [{at:6.1f}s] {payload['label']}\n")
    elif name == "verdict":
        early_verdict = (payload.get("html", ""), at)
        out(f"  [{at:6.1f}s] >>> EARLY VERDICT rendered\n")
    elif name == "done":
        ask_done = payload
        out(f"  [{at:6.1f}s] done — {payload.get('response_type')}\n")
    elif name == "error":
        out(f"  ERROR: {payload}\n")
        sys.exit(1)
ask_total = perf_counter() - start

if not ask_progress:
    violations.append(
        "/ask emitted no progress events. Streaming without progress is the old "
        "blocking behaviour with extra machinery."
    )
if ask_done is None:
    violations.append("/ask never emitted a done frame.")
elif ask_done.get("response_type") in ("EVALUATION", "GAP_FLAG"):
    if not ask_done.get("agent1_xml"):
        violations.append("/ask done frame carries no agent1_xml; /qa cannot run.")
    if not ask_done.get("right_pane_html"):
        violations.append("/ask done frame carries no right_pane_html.")

if ask_progress and ask_total:
    first = ask_progress[0][1]
    if first > ask_total * 0.9:
        violations.append(
            f"/ask progress is back-loaded: first event at {first:.1f}s of "
            f"{ask_total:.1f}s. The reader still waits in the dark."
        )

# --- the early verdict: the whole point is that it beats the full document ---
if ask_done and ask_done.get("response_type") in ("EVALUATION", "GAP_FLAG"):
    if early_verdict is None:
        violations.append(
            "NO EARLY VERDICT: a synthesis response emitted no verdict event. "
            "The reader waits for all ten sections to see the answer."
        )
    else:
        html, at = early_verdict
        out(f"\n  early verdict at {at:.1f}s of {ask_total:.1f}s "
            f"({at / ask_total:.0%} in) — saved {ask_total - at:.1f}s of waiting\n")
        if at > ask_total * 0.7:
            violations.append(
                f"EARLY VERDICT TOO LATE: arrived at {at:.1f}s of {ask_total:.1f}s. "
                "It should land with the verdict, not near the end."
            )
        if "classification" not in html:
            violations.append("EARLY VERDICT: rendered html carries no classification.")
        if "verdict-banner" not in html:
            violations.append("EARLY VERDICT: rendered html is not a verdict banner.")
        # Must agree with what the settled pane ends up showing.
        import re as _re
        m = _re.search(r'<div class="classification ([A-Z]+)"', html)
        final = _re.search(r'<div class="classification ([A-Z]+)"',
                           ask_done.get("right_pane_html", ""))
        if m and final and m.group(1) != final.group(1):
            violations.append(
                f"EARLY VERDICT DISAGREES with the settled pane: "
                f"{m.group(1)} then {final.group(1)}. The reader saw one answer "
                "replaced by another."
            )
        elif m and final:
            out(f"  early and settled agree: {m.group(1)}\n")

# ---------------------------------------------------------------- /qa stream
qa_done = None
if ask_done and ask_done.get("agent1_xml"):
    out("\n===== /qa =====\n")
    start = perf_counter()
    resp = client.post(f"/projects/{PROJECT}/qa",
                           json={"agent1_xml": ask_done["agent1_xml"]})
    if resp.mimetype != "text/event-stream":
        violations.append(f"/qa returned {resp.mimetype}, expected text/event-stream")
    else:
        qa_checks = []
        for name, payload, at in read_sse(resp, start):
            if name == "check":
                qa_checks.append((payload["label"], payload.get("verdict"), at))
                out(f"  [{at:6.1f}s] {payload['label']}: {payload.get('verdict')}\n")
            elif name == "done":
                qa_done = payload
                out(f"  [{at:6.1f}s] done — {payload.get('qa_status')}"
                    f"{' (degraded)' if payload.get('qa_degraded') else ''}\n")
            elif name == "error":
                out(f"  ERROR: {payload}\n")
        qa_total = perf_counter() - start

        if not qa_checks:
            violations.append(
                "/qa emitted no check events. The seven checks are the whole "
                "reason this endpoint streams."
            )
        else:
            first = qa_checks[0][2]
            out(f"\n  first check at {first:.1f}s of {qa_total:.1f}s total "
                f"({first / qa_total:.0%} in)\n")
            if first > qa_total * 0.9:
                violations.append(
                    f"/qa progress is back-loaded: first check at {first:.1f}s "
                    f"of {qa_total:.1f}s."
                )
            unparsed = [c for c in qa_checks if not c[1]]
            if unparsed:
                violations.append(f"/qa checks with no verdict parsed: {unparsed}")

        if qa_done is None:
            violations.append("/qa never emitted a done frame.")
        elif not qa_done.get("qa_html"):
            violations.append("/qa done frame carries no qa_html.")

print("\n===== STREAMING ASSERTIONS =====")
if violations:
    for v in violations:
        out(f"FAIL: {v}\n")
    sys.exit(1)
print("PASS: both endpoints stream real progress ahead of their result.")

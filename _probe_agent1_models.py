"""Agent 1 model/effort sweep: is there a faster configuration that is not worse?

Agent 1 is ~65-90s and is the bulk of the end-to-end wait. A bare bump to
Opus 5 was already measured and rejected: thinking is on by default there, and
at default effort Agent 1 ran ~200s and produced 15-16k output tokens against
~5-6k on claude-opus-4-7. That does not rule out Opus 5 at a LOWER effort,
which is the configuration this sweep exists to test.

Speed alone is not the question, so each candidate is scored on three things:

  parses          Malformed XML is a total failure regardless of speed.
  completeness    Every spine section the schema requires must be present.
  QA verdict      Agent 2 - unchanged, on claude-opus-4-7 - reviews each
                  output. Using the existing adversarial QA layer as the
                  quality gate is what it is for, and it is a far better
                  signal than eyeballing prose.

Agent 2's own configuration is never varied here. The QA-depth guardrail
applies to the gate, not to the synthesis being gated.

Run:  ./venv/bin/python _probe_agent1_models.py
Costs one Agent 1 + one Agent 2 generation per candidate.
"""
import sys
import xml.etree.ElementTree as ET
from time import perf_counter

import model_client
import state
from agents import agent2_qa
from app import (AGENT2_MODEL, QA_CHECK_NAMES, build_system_blocks, client,
                 extract_qa_checks, load_corpora, parse_response)

THEME = (
    "Weather Underground iOS users cross-check a second weather app before "
    "committing to outdoor plans because the displayed temperature feels stale."
)

# Sections the analytical pane leads with or depends on. A configuration that
# drops these is faster and useless.
REQUIRED_SECTIONS = [
    "verdict", "evidence_chain", "reasoning_step", "falsification_attempt",
    "transfer_assumption_check", "decision_support",
]

CANDIDATES = [
    ("opus-4-7  (current)", "claude-opus-4-7", None),
    ("opus-5    effort=low", "claude-opus-5", "low"),
    ("opus-5    effort=medium", "claude-opus-5", "medium"),
]

out = sys.stdout.write
results = []

for label, model, effort in CANDIDATES:
    out(f"\n{'=' * 66}\n{label}\n{'=' * 66}\n")
    project_state = state.load_state()
    query_id = state.generate_query_id(project_state)

    start = perf_counter()
    try:
        text, final = model_client.stream_text(
            client,
            label=f"sweep_agent1_{model}_{effort or 'default'}",
            model=model,
            max_tokens=16000,
            system=build_system_blocks(load_corpora(), project_state, query_id),
            messages=[{"role": "user", "content": THEME}],
            effort=effort,
        )
    except Exception as exc:
        out(f"  FAILED: {exc}\n")
        results.append({"label": label, "error": str(exc)[:120]})
        continue
    elapsed = perf_counter() - start

    root, parse_error = parse_response(text)
    row = {
        "label": label,
        "elapsed": elapsed,
        "out_tokens": final.usage.output_tokens,
        "stop_reason": final.stop_reason,
        "parses": root is not None,
        "parse_error": parse_error,
    }
    out(f"  {elapsed:6.1f}s  out={final.usage.output_tokens} "
        f"stop={final.stop_reason}  parses={root is not None}\n")
    if root is None:
        out(f"  parse error: {parse_error}\n")
        results.append(row)
        continue

    missing = [s for s in REQUIRED_SECTIONS if root.find(s) is None]
    row["missing_sections"] = missing
    row["response_type"] = root.findtext("attributes/response_type")
    out(f"  response_type={row['response_type']}  "
        f"missing_sections={missing or 'none'}\n")

    # --- quality gate: Agent 2, unchanged ---
    out("  running QA review (Agent 2, claude-opus-4-7, unchanged)…\n")
    qa_start = perf_counter()
    review, qa_err = agent2_qa.run_qa_review(
        client, AGENT2_MODEL, ET.tostring(root, encoding="unicode")
    )
    row["qa_elapsed"] = perf_counter() - qa_start
    if review is None:
        row["qa"] = f"QA failed: {qa_err}"
        out(f"  QA could not run: {qa_err}\n")
    else:
        stamp = review.find("overall_qa_stamp")
        row["qa_verdict"] = stamp.findtext("qa_verdict") if stamp is not None else None
        checks = extract_qa_checks(review)
        row["checks"] = {c["name"]: c["verdict"] for c in checks}
        fails = [c["name"] for c in checks if c["verdict"] == "FAIL"]
        row["fails"] = fails
        out(f"  QA verdict: {row['qa_verdict']}  ({row['qa_elapsed']:.1f}s)\n")
        out(f"  checks: {sum(1 for c in checks if c['verdict'] == 'PASS')} PASS, "
            f"{sum(1 for c in checks if c['verdict'] == 'PASS_WITH_NOTE')} with-note, "
            f"{len(fails)} FAIL\n")
        if fails:
            out(f"  FAILING: {', '.join(fails)}\n")
    results.append(row)

# --------------------------------------------------------------- comparison
out(f"\n{'=' * 66}\nCOMPARISON\n{'=' * 66}\n")
out(f"{'config':<26}{'time':>8}{'out tok':>9}{'parses':>8}  {'QA verdict':<22}{'fails':>6}\n")
out("-" * 80 + "\n")
for r in results:
    if "error" in r:
        out(f"{r['label']:<26}{'ERROR':>8}  {r['error']}\n")
        continue
    out(f"{r['label']:<26}{r['elapsed']:>7.1f}s{r['out_tokens']:>9}"
        f"{str(r['parses']):>8}  {str(r.get('qa_verdict', '-')):<22}"
        f"{len(r.get('fails', [])):>6}\n")

baseline = next((r for r in results if "current" in r["label"] and r.get("elapsed")), None)
if baseline:
    out(f"\nAgainst the current configuration ({baseline['elapsed']:.1f}s):\n")
    for r in results:
        if r is baseline or "elapsed" not in r:
            continue
        delta = r["elapsed"] - baseline["elapsed"]
        verdict = "FASTER" if delta < 0 else "SLOWER"
        usable = r.get("parses") and not r.get("missing_sections") and not r.get("fails")
        out(f"  {r['label']:<26}{delta:+6.1f}s  {verdict:<7} "
            f"{'and clean' if usable else 'BUT check quality columns'}\n")
out("\n")

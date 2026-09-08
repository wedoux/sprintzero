"""Latency and token instrumentation for the two-agent pipeline.

Exists because the QA pass is slow and nobody knows why. Before this, nothing
in the codebase read `response.usage` at all, so prompt-cache behaviour was
invisible: `cache_control` was set and assumed to be working, with no evidence
either way.

Records one JSON line per model call to state/latency_trace.jsonl:
wall-clock elapsed, the four usage counters, and whatever metadata the caller
attaches. Append-only and cheap, so it can stay on in normal use rather than
being a thing you switch on when investigating.

Deliberately measures only. It changes no request parameter, so a trace taken
now is a valid baseline for anything tried later.
"""
import json
import os
import threading
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter

TRACE_FILE = Path(__file__).parent / "state" / "latency_trace.jsonl"
_LOCK = threading.Lock()

# Flask's reloader runs the module twice; the env flag keeps one writer.
ENABLED = os.environ.get("SPRINTZERO_TRACE", "1") != "0"


def usage_fields(response):
    """Pull the four counters that decide where the time and money went.

    cache_read_input_tokens is the one that matters most here: if it stays at
    zero across runs with an identical prefix, the cache is not being hit and
    every QA pass is paying full input cost and full input latency.
    """
    usage = getattr(response, "usage", None)
    if usage is None:
        return {}
    return {
        "input_tokens": getattr(usage, "input_tokens", None),
        "output_tokens": getattr(usage, "output_tokens", None),
        "cache_read_input_tokens": getattr(usage, "cache_read_input_tokens", None),
        "cache_creation_input_tokens": getattr(usage, "cache_creation_input_tokens", None),
    }


def record(label, elapsed_s, response=None, error=None, **meta):
    if not ENABLED:
        return
    entry = {
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "label": label,
        "elapsed_s": round(elapsed_s, 3),
    }
    entry.update(usage_fields(response))
    if error:
        entry["error"] = str(error)[:400]
    entry.update(meta)
    try:
        TRACE_FILE.parent.mkdir(parents=True, exist_ok=True)
        with _LOCK, open(TRACE_FILE, "a") as f:
            f.write(json.dumps(entry) + "\n")
    except OSError:
        pass  # instrumentation must never break the request path


def save_failed_output(agent, raw_text, error, **meta):
    """Persist model output that would not parse. Returns the path, or None.

    A parse failure costs the researcher the whole generation, and until now the
    evidence lived only in the browser pane that reported it - close the tab and
    the failure could not be investigated. Writing it down is what makes a rare
    intermittent fault fixable rather than folklore.
    """
    try:
        import resources
        # Microseconds, not seconds: a retry fails within the same second as
        # the attempt before it, and second-resolution names silently
        # overwrote one of the two artefacts - losing exactly the evidence
        # that a double failure exists to provide.
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")
        suffix = f"-attempt{meta['attempt']}" if "attempt" in meta else ""
        path = resources.diagnostics_dir() / f"{stamp}-{agent}{suffix}.txt"
        header = [
            f"agent:  {agent}",
            f"when:   {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
            f"error:  {error}",
        ]
        header += [f"{k}: {v}" for k, v in meta.items()]
        path.write_text(
            "\n".join(header) + "\n" + "-" * 70 + "\n" + (raw_text or ""),
            encoding="utf-8",
        )
        record(f"{agent}_parse_failure", 0.0, error=error, saved_to=str(path), **meta)
        return path
    except Exception:
        return None  # diagnostics must never break the request path


def observe(label, call, **meta):
    """Run `call`, time it, record the result. Exceptions propagate unchanged."""
    start = perf_counter()
    try:
        response = call()
    except Exception as exc:
        record(label, perf_counter() - start, error=exc, **meta)
        raise
    record(label, perf_counter() - start, response=response, **meta)
    return response


def load_trace():
    if not TRACE_FILE.exists():
        return []
    out = []
    with open(TRACE_FILE) as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return out

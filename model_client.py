"""Model configuration and the streaming call path for both agents.

Centralises what used to be a single bare MODEL constant shared by Agent 1 and
Agent 2. They are separate models now, because they are separately tunable:
Agent 2's latency budget is a QA gate the researcher waits on, Agent 1's is a
synthesis. Sharing one constant made that impossible to express.

Two levers apply here, both chosen because they cost no analytical depth:

  streaming  - the generation is identical, it is just surfaced as it arrives
               instead of after it completes. Measured baseline was 47s of
               blank screen for the QA pass; the work was always progressive,
               only the transport was not.

  fast mode  - the same model at a higher output token rate. Depth-preserving
               by construction: this is not a smaller model and not a lower
               effort setting, both of which would trade the reasoning quality
               the QA pass exists to provide.

MEASURED OUTCOME - both model levers were tried and both were rejected on
evidence. Streaming was kept; the model bump was not:

  fast mode  Rejected with 429 rate_limit_error on every attempt. It carries a
             rate limit separate from standard Opus and this account has no
             capacity on it. The fallback path below degrades cleanly, so the
             only cost is a wasted ~3s round trip per call - hence default off.

  Opus 5     Thinking is ON by default there, where claude-opus-4-7 ran with no
             thinking at all unless asked. That is not a like-for-like swap:
             Agent 2 went 47s/3.1k output -> 151s/12,000 output, hitting its
             max_tokens cap exactly (truncated); Agent 1 went 85s/6.1k ->
             ~200s/15.2-16.0k. Roughly 2.4-3.2x slower with truncation at the
             margin, in exchange for a fast mode that will not run.

Both stay reachable through the env vars below, so re-testing when fast-mode
capacity exists is a one-line change rather than a revert. Do not raise these
defaults without re-running _probe_qa_latency.py - the trap is that the model
bump looks free and is not.
"""
import os
from time import perf_counter

import instrumentation

AGENT1_MODEL = os.environ.get("SPRINTZERO_AGENT1_MODEL", "claude-opus-4-7")
AGENT2_MODEL = os.environ.get("SPRINTZERO_AGENT2_MODEL", "claude-opus-4-7")

# Off by default: measured 429 on every attempt (see module docstring).
# SPRINTZERO_FAST_MODE=1 re-enables it for a retest.
FAST_MODE_BETA = "fast-mode-2026-02-01"
FAST_MODE = os.environ.get("SPRINTZERO_FAST_MODE", "0") != "0"


def stream_text(client, *, label, model, max_tokens, system, messages,
                on_progress=None, **meta):
    """Stream one completion. Returns (text, final_message).

    `on_progress(accumulated_text)` is called as deltas arrive so the caller can
    surface real progress rather than a timed animation. Exceptions from the
    callback are swallowed: a UI progress hook must never fail a model call.

    Falls back to standard speed if fast mode is rejected (it is a research
    preview with its own rate limit), so an unavailable preview degrades to a
    slower correct answer rather than an error.
    """
    def _call(use_fast):
        kwargs = {
            "model": model,
            "max_tokens": max_tokens,
            "system": system,
            "messages": messages,
        }
        if use_fast:
            kwargs["speed"] = "fast"
            kwargs["betas"] = [FAST_MODE_BETA]
        parts = []
        with client.beta.messages.stream(**kwargs) as stream:
            for delta in stream.text_stream:
                parts.append(delta)
                if on_progress is not None:
                    try:
                        on_progress("".join(parts))
                    except Exception:
                        pass
            return "".join(parts), stream.get_final_message()

    start = perf_counter()
    used_fast = FAST_MODE
    try:
        text, final = _call(FAST_MODE)
    except Exception as exc:
        if not FAST_MODE:
            instrumentation.record(label, perf_counter() - start, error=exc,
                                   model=model, fast_mode=False, **meta)
            raise
        # Fast mode unavailable or rate-limited - retry at standard speed.
        instrumentation.record(f"{label}_fastmode_rejected", perf_counter() - start,
                               error=exc, model=model, **meta)
        used_fast = False
        start = perf_counter()
        try:
            text, final = _call(False)
        except Exception as exc2:
            instrumentation.record(label, perf_counter() - start, error=exc2,
                                   model=model, fast_mode=False, **meta)
            raise

    elapsed = perf_counter() - start
    instrumentation.record(label, elapsed, response=final, model=model,
                           fast_mode=used_fast, streamed=True, **meta)
    return text, final

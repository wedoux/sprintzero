# Decisions and their evidence

A record of what was decided, what it was measured against, and — where it applies — what
was tried and rejected. Rejected options are kept deliberately: without them the same
plausible ideas get re-proposed, re-tried, and re-discovered to be wrong.

---

## D-001 · Two agents, with the second unable to rewrite the first

**Decision.** Run every synthesis past a second agent that returns only `<qa_review>`. The
server merges it and flips `qa_status`.

**Why.** Testing across four frontier models showed all four flagging the EU transfer
assumption formulaically without arguing it. The caveat was present; the reasoning was not.
A single agent asked to be more careful produces more caveats, not more argument.

**Why structural rather than prompted.** If Agent 2 returned a full document, nothing but
an instruction would stop it rewriting the verdict it was reviewing. Returning a fragment
the server merges makes that architecturally impossible. Agent 2 stamps; it does not
re-synthesise.

**Cost.** Roughly doubles latency. Accepted — the QA pass is the product.

---

## D-002 · Evidence strength and QA status are independent colour axes

**Decision.** Strength (`STRONG`/`UNCERTAIN`/`WEAK`) renders on a neutral ramp varying by
depth of ink. Semantic colour is reserved for the QA gate.

**Why.** User research found the interface was teaching the wrong lesson. The old CSS had
`.classification.WEAK` and `.qa-stamp-value.QA_FAILED` resolving to the *same*
`--red-700`, so a weak verdict read as a failed one. But surfacing weak evidence is the QA
layer succeeding — the interface was making its most valuable output look like a defect.

**Enforcement.** `_probe_design_tokens.py` fails if semantic colour reappears on the
strength axis, or if the gate loses it. It was negative-tested: deliberately reintroducing
`--red-700` on `.classification.WEAK` makes it fail.

**Later refinement.** Project "Ready" pills on the landing screen were also using the
gate's green. Same dilution: if everything settled is green, a QA pass stops registering.
They moved to a separate context colour.

---

## D-003 · A failed gate visibly invalidates the verdict

**Decision.** On `QA_FAILED`, strike through the classification and confidence, stamp it,
and show `required_action` directly beneath. On `QA_PASSED`, change nothing.

**Why `required_action` and not `blocking_findings`.** The schema defines
`required_action` as what must happen before the verdict can be committed, including the
three unblock routes. That is what a reader needs when they are blocked. The findings are
one disclosure away.

**Why a pass is silent.** A pass is not an event. Decorating it would dilute the failure.

### The degraded state

`merge_qa_review` maps an unknown or absent `qa_verdict` to `QA_FAILED`. So a *malformed*
Agent 2 response would strike through a sound verdict while asserting a finding nobody
made — reproducing, in a new place, the exact misread D-002 removed.

A `QA_FAILED` carrying neither `required_action` nor `blocking_findings` therefore renders
neutrally as **QA INCOMPLETE — verdict unvalidated**, explicitly not a finding. Handled in
the UI rather than as a new schema state, to avoid changing a registered contract for a
presentation concern.

---

## D-004 · Measure before optimising

Nothing in the codebase read `response.usage`, so prompt-cache behaviour was invisible —
`cache_control` was set and assumed to work, with no evidence either way.

**Baseline (`claude-opus-4-7`, n=3):**

| | median | range |
|---|---|---|
| Agent 1 | 84.8s | 84.6–94.2s |
| Agent 2 | 47.2s | 42.7–51.1s |

Agent 2's prefix: 25,488 tokens, of which the output schema alone is 17,388 (68%).
Output: 2,907–3,574 tokens at ~68 tok/s.

**QA time tracks output token count almost exactly** — roughly 6s fixed plus ~79 tok/s
marginal. This is output generation, not input size or retrieval.

### Two hypotheses were wrong

Recorded because they were plausible and are worth not re-testing:

- **The prompt cache was working all along.** Run 1 wrote 25,477 tokens; runs 2 and 3 each
  read 25,477. It had been a live suspect.
- **The client's progress animation was never the bottleneck.** 5.5s of pacing against a
  47s call. Not a factor.

---

## D-005 · Stream both agents

**Decision.** Both routes emit Server-Sent Events — one per section for Agent 1, one per
completed check for Agent 2.

**Measured.** Totals unchanged; the wait transformed.

| | total | first signal |
|---|---|---|
| Agent 1 | 89.7s | **9.7s** (was 85s of blank screen) |
| Agent 2 | 48.2s | **7.1s** (was 47s of blank screen) |

**No depth traded.** The generation is identical; only the transport changed. The timed
client animation was removed — it narrated for 5.5s against a 47s call, so it stopped
long before the work did.

---

## D-006 · Render the verdict as soon as it closes

**Decision.** Agent 1 writes ten sections over ~80s but commits the verdict at ~17s. Emit
the rendered Tier 1 banner the moment `</verdict>` closes.

**Measured.** Verdict on screen at **17.4s of an 82.1s synthesis — 64.7s of waiting
removed.** No model change, no quality tradeoff.

The banner is a shared partial so the progressive and settled renders cannot drift; a
probe asserts they carry the same classification. A progressive render that showed one
answer and then silently changed it would be worse than waiting.

---

## D-007 · REJECTED — bump to a newer model

**Tried** on explicit approval, for both agents, then reverted.

| config | Agent 1 | Agent 2 |
|---|---|---|
| `claude-opus-4-7` | 77–90s, ~5–6k out | 43–51s, ~3k out |
| newer, default effort | ~200s, 15–16k out | 151s, **12,000 out — hit the cap, truncated** |
| newer, `effort=low` | 87.9s, 6.7k out — **failed to parse** | not tried |
| newer, `effort=medium` | 152.6s, 11.3k out | not tried |

**Why it failed.** Thinking is on by default on the newer model, where `claude-opus-4-7`
runs with none unless asked. That is not a like-for-like swap — output roughly tripled, and
at the margin it truncated.

Quality was gated by running the unchanged Agent 2 over each candidate's output, rather
than by reading the prose and forming an impression.

**Kept reachable** via `SPRINTZERO_AGENT{1,2}_MODEL`. Do not raise the defaults without
re-running `_probe_agent1_models.py` — the bump looks free and is not.

---

## D-008 · REJECTED — fast mode

`speed: "fast"` returned `429 rate_limit_error` on every attempt; it carries a rate limit
separate from standard Opus and the test account had no capacity. The fallback path
degrades cleanly to standard speed, so the only cost is a wasted ~3s round trip — hence
off by default, behind `SPRINTZERO_FAST_MODE`.

This was the one lever that cuts real time with no quality question attached. It remains
the first thing to re-try if capacity becomes available.

---

## D-009 · REJECTED — trim the schema from Agent 2's prefix

Agent 2 receives the full 1082-line output schema, of which it authors only `<qa_review>`
— 17,388 of its 25,488 prefix tokens.

**Measurement demoted it.** With only ~6s of fixed overhead in total, trimming could win a
couple of seconds at most, and it contradicts the QA protocol's own requirement that the
files load together. Not worth a protocol change.

Worth recording as an example of measurement changing a ranking: this was the *second*
most promising lever before the numbers existed.

---

## D-010 · DEFERRED — parallelise the seven QA checks

Running the checks concurrently would make wall time the slowest check rather than the sum
— roughly **47s → ~15s**, same model, same checks, same effort.

**Blocked on a protocol decision, not a technical one.** `qa_agent_protocol.md` says "Run
all seven checks **in order**". Parallelising is a protocol change, and the standing
guardrail is that QA depth is never traded for speed. It needs a deliberate decision plus
before/after comparison of QA verdicts on identical inputs.

The single largest remaining speedup, and the one most likely to be a mistake.

---

## D-011 · Retry once on malformed output

The model intermittently emits structurally invalid XML — roughly one Agent 1 run in six,
observed in a live session and again independently during the model sweep. The whole ~80s
generation was lost, and the evidence existed only in the browser tab that reported it.

**Decision.** Both agents retry once, bounded. Malformed output is written to
`state/failures/` whether or not the retry rescues the run.

**Tradeoff, stated plainly.** A retry costs another ~80s, so a double-length wait is now
possible where a fast failure used to be. That is the right trade for a live session with
a participant in the room.

If failures became frequent, the better fix is a corrective re-ask — handing the model its
own malformed output to repair — rather than a blind fresh sample.

---

## D-012 · Multi-project, and the short creation form

**Decision.** Three fields at creation — name, type, research objective. The rest of
`project_context` is collected by Agent 1's intake protocol on the first query.

**Why those three.** The schema marks them required and explains why: type *"determines
what 'insight' means in this context"*, objective *"must be narrow enough to scope what
'relevant' means for retrieval"*.

**Why conversational.** The intake protocol, the `INTAKE` response type, and the templates
that render it all existed and were unreachable — `build_system_blocks` unconditionally
told Agent 1 not to use them. Making that conditional activated a whole designed flow
rather than building a competing one.

**Cost.** Intake adds turns before the first verdict. A short form instead of a long one,
at the price of a conversation.

---

## D-013 · History is recorded but not fed back

**Decision.** Every synthesis turn is recorded per project and replayable. Past verdicts
are **not** injected into later prompts.

**Why not.** Each verdict stays independently reproducible, the prompt does not grow as a
project accumulates history, and results do not depend on the order themes were submitted.
`prior_research_and_insights` stays whatever the researcher wrote.

**Why the full document is stored.** A few kilobytes buys replay through the same
renderer the live flow uses — no second renderer to build, and no risk of a history view
drifting from the real one.

Replay had to be taught two things the live flow gets from the client: the QA band would
otherwise read "Running…" for a query that finished days ago, and a blocked verdict would
re-render as though it had passed. **A history view that flatters a blocked verdict would
be worse than having no history at all.**

---

## D-014 · Annotate reference data at ingest

**Decision.** Split on blank lines, number units in document order, prefix by source type
(`R`, `INT`, `SV`, `TK`), and write a data-limitations preamble into every file.

**Why.** The schema requires every `evidence_chain` unit to carry an id and the reasoning
cites them. Pasted text has none, so the model invents them — citations that look correct
and reference nothing. That is a confident fabrication, which is worse than an obvious
failure.

**Deliberately crude.** No chunking strategy, no embeddings, no semantic boundaries. It
exists to make citations resolvable, and the file says so where the agent will read it.
`A-002`, the annotation protocol that would make this rigorous, is specified in the RAG
registry and unwritten. **This is the highest-value open item in the project.**

---

## Defects the probes caught

Each was invisible without an assertion, and each is now covered by one:

| Defect | Why it was invisible |
|---|---|
| A clean pass was flagged "degraded" | A pass correctly has no `required_action`; degradation was computed without regard to gate status |
| Looking up a project **created** its directory | A mistyped URL left an empty directory that then read as a real project |
| Every newly created project's workspace returned 500 | The activity log hard-coded the founding project's filenames; only a *fresh* project exposes it |
| Failure artefacts overwrote each other | Filenames were timestamped to the second, and a retry fails within the same second |
| A stored failure replayed as a pass | The client resolves the gate live; on replay there is no client |
| The packaged app served nothing | `socket.getfqdn` blocked after bind, before `listen()` — bound, never listening, nothing raised |

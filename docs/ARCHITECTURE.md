# Architecture

How SprintZero is put together, and why each part is shaped the way it is.

---

## 1. The two-agent pipeline

The core claim of this project is that **a second agent with the authority to block is a
better answer to unearned confidence than a longer prompt asking the first agent to be
careful.**

```
POST /projects/<id>/ask                    POST /projects/<id>/qa
         │                                          │
         ▼                                          ▼
  Agent 1 — Research Copilot            Agent 2 — QA Validation Agent
  agents/prompts/                       agents/prompts/
    sprintzero_copilot_role_task.txt      qa_agent_protocol.md
         │                                          │
         │ <SprintZero_response>                    │ <qa_review> ONLY
         │   attributes, verdict,                   │   seven checks
         │   evidence_chain, reasoning_step,        │   overall_qa_stamp
         │   falsification_attempt,                 │
         │   transfer_assumption_check,             ▼
         │   decision_support, …            agent2_qa.merge_qa_review()
         │                                  appends it to Agent 1's root
         └──────────────────────────────────────────┤
                                                    ▼
                                        one document, one chain:
                                        evidence → verdict → QA stamp
```

**Agent 2 returns only `<qa_review>`.** The server appends it and flips `qa_status`. This
is a structural guarantee rather than a prompt instruction — Agent 2 is architecturally
incapable of rewriting the verdict it is reviewing. It stamps; it does not re-synthesise.

**Both calls stream.** Agent 1 emits a Server-Sent Event as each section closes; Agent 2
emits one per completed check. The client renders real progress instead of a timed
animation. See [DECISIONS.md](DECISIONS.md) for the measurements that drove this.

### The seven checks

Defined in `agents/prompts/qa_agent_protocol.md` (asset `A-007`):

1. Reasoning Validity
2. Counter-Signal Engagement
3. Confidence Integrity
4. Transfer Assumption Depth
5. Behavioural Mechanism Specificity
6. Tacit Knowledge Prompt Specificity
7. Decision Support Overreach

Check 4 is the origin of the project. Testing showed frontier models flag transfer
assumptions formulaically without arguing them — the caveat is decoration, the verdict
underneath unchanged.

---

## 2. The QA gate

The output schema has always said:

> A verdict with `qa_status = QA_PENDING` or `QA_FAILED` must not be committed to the
> insight graph. The researcher review layer must show the QA stamp prominently — not
> buried below the evaluation.

The interface now implements it:

| QA result | What the reader sees |
|---|---|
| `QA_PASSED` | Verdict renders exactly as it would have. A pass is not an event. |
| `QA_FAILED` | Classification and confidence **struck through**, a `QA-FAILED` badge, and `required_action` directly beneath the invalidated verdict. |
| `QA_FAILED` with no reason | Rendered neutrally as **QA INCOMPLETE — verdict unvalidated**, explicitly *not* a finding. |

That third row matters more than it looks. `merge_qa_review` maps an unknown or absent
`qa_verdict` to `QA_FAILED`, so a malformed Agent 2 response would otherwise strike
through a sound verdict while asserting a finding nobody made. Rendering it identically to
a real failure would reproduce, in a new place, exactly the misread this project exists to
remove.

---

## 3. The two-axis colour grammar

Originally one red/green pass-fail vocabulary covered both evidence strength and QA
status — `.classification.WEAK` and `.qa-stamp-value.QA_FAILED` resolved to the *same*
`--red-700`. User research found the consequence: a `WEAK` verdict read as a failure, when
surfacing weak evidence is the QA layer succeeding.

```
AXIS 1 — EVIDENCE STRENGTH          AXIS 2 — QA STATUS
strong / uncertain / weak           passed / failed
a measurement, not a judgement      a gate decision
neutral slate ramp; varies by       the ONLY axis permitted
depth of ink, never by hue          semantic colour
--strength-*                        --qa-*
```

A third set, `--attention-*`, carries advisory chrome (gap flags) which is neither axis.

The rule is documented in `:root` in `templates/partials/styles.html`, and
`_probe_design_tokens.py` fails the build if semantic colour reappears on the strength
axis or if the gate loses it.

---

## 4. Signal-first information architecture

The analytical pane was a flat stack of nine peer accordions, with the QA gate below
everything it was supposed to gate. It is now three tiers:

| Tier | Content | Behaviour |
|---|---|---|
| **1 — Decision band** | QA status, verdict, and the single most load-bearing signal | Always visible, never collapsible |
| **2 — Signal strip** | Evidence counts, falsification result, transfer verdict, gap count | Chips; each jumps to and opens its card |
| **3 — Depth on demand** | The same nine cards, grouped into Reasoning & evidence / Framing / Decision support | Collapsed by default |

The full Agent 2 surface stays below the divider so the two-agent narrative survives; only
a compact status band is hoisted into Tier 1.

`templates/partials/verdict_banner.html` is a shared partial rendered in three places —
progressively during streaming, in the settled pane, and on history replay — so those
renderings cannot drift apart.

---

## 5. Storage

Flat JSON. No database, no locking. Writes are atomic via tmp-file replace.

```
state/
  projects.json                          landing index
  projects/<project_id>/
    project.json                         project_context + query_counter + registry[]
    reference/S-001-<slug>.md            annotated reference data
    history/SZ-YYYYMMDD-NNN.json         one record per evaluated theme
  failures/                              raw model output that failed to parse
  latency_trace.jsonl                    one line per model call
```

`resources.py` resolves these. In development they sit in the repo; in the packaged macOS
app they move to `~/Library/Application Support/SprintZero/`, because the bundle is
read-only and unpacked fresh on every launch. **The two do not see each other** — a
packaged app starts with no projects.

Path resolution deliberately does **not** create directories. Creating on read meant that
merely looking up a project — from a mistyped URL, say — left behind an empty directory
that then read as a real project. Project ids arrive from URLs, so they are validated as
single lowercase slugs or refused.

---

## 6. Project lifecycle and the intake protocol

A project is created from three fields: name, type, and research objective. The schema
requires more than that, so the rest is collected conversationally.

```
create_project()                  build_system_blocks()                  /ask
      │                                    │                               │
      ▼                                    ▼                               ▼
context_completeness       ┌── COMPLETE ──> inject the established     evaluate the
  = INCOMPLETE             │                context; suppress intake   submitted theme
      │                    │
      └────────────────────┤
                           └── INCOMPLETE ─> name the missing fields;  Agent 1 returns
                                             run the INTAKE PROTOCOL   an INTAKE response
                                                                              │
                                            state.apply_context() ◀────────────┘
                                            persists the returned project_context
```

The intake protocol, the `INTAKE` response type, and the templates that render it all
existed from the beginning and were **unreachable**: `build_system_blocks` unconditionally
told Agent 1 *"Do not produce an INTAKE response."* Making that one block conditional is
the whole feature.

---

## 7. Reference data

Every claim is anchored to an evidence unit id, and the reasoning cites those ids. Pasted
text has no ids, so an LLM will invent them — citations that look correct and resolve to
nothing, which is a confident fabrication rather than an obvious failure.

Ingest therefore:

1. Assigns the next `S-nnn` asset id (the Situational tier of the RAG registry)
2. Splits on blank lines, numbers units in document order
3. Prefixes by source type — `R` reviews, `INT` interviews, `SV` surveys, `TK` tickets
4. Writes a **data-limitations preamble** telling the agent the segmentation was mechanical
5. Registers the asset in `project.json` **before** it is loadable

Loading is driven by the registry, not by a directory listing: an unregistered file in the
folder is not evidence. Global assets are the framework (`A-001`) and context tiers, which
ship with the app; corpus comes from the project.

> This is deliberately crude — no chunking strategy, no embeddings, no semantic
> boundaries. It exists to make citations resolvable. `A-002`, the corpus annotation
> protocol that would make it rigorous, is specified in the RAG registry and unwritten.

---

## 8. Failure handling

The model intermittently emits structurally invalid XML — roughly one Agent 1 run in six.
The whole ~80s generation is lost when it does.

Both agents **retry once**, bounded. Agent 1 uses a fresh progress reporter per attempt so
the reader watches sections land again rather than sitting through a silent second run,
and the retry is announced — an unexplained extra 80s reads as a hang. Malformed output is
written to `state/failures/` either way, with microsecond-resolution filenames because a
retry fails within the same second as the attempt before it.

On a double failure the pane says so, points at the artefacts, and states plainly that
this is a model fault rather than a problem with the submitted theme.

---

## 9. The probe system

Eight deterministic probes, no API key, nothing charged. They exist because nearly every
failure mode here is silent.

| Probe | Boundary it defends |
|---|---|
| `_probe_design_tokens` | The two colour axes stay separated |
| `_probe_qa_gate` | Pass renders unchanged; failure invalidates *and* explains; reasonless failure degrades |
| `_probe_signal_first_ia` | Tier order holds, chips resolve, **no content lost** in the restructure |
| `_probe_parse_retry` | One bounded retry; artefacts kept; clean runs cost nothing extra |
| `_probe_projects` | Project isolation, migration, id validation, a new project renders |
| `_probe_intake` | Both sides of the intake conditional; completion persists |
| `_probe_reference_data` | Evidence registered, citable, isolated; bad input refused |
| `_probe_history` | Recorded, replayable, isolated; a blocked verdict stays blocked |

Live probes that spend money are listed in [CONTRIBUTING.md](../CONTRIBUTING.md).

Assertion messages state **what the user would experience**, not what is technically
wrong — because that is what tells the next person whether the failure matters.

---

## 10. Packaging

`pywebview` over the local Flask server. The app is already a local web app, so the bundle
only needs a native window pointed at `127.0.0.1` — and pywebview uses the OS's own
WKWebView, shipping no second runtime. Tauri would add a Rust toolchain and still have to
ship Python; Electron would bundle Chromium and Node *on top of* Python.

Two non-obvious things were needed:

- **`socket.getfqdn` short-circuit.** `http.server`'s `server_bind()` does a reverse-DNS
  lookup after binding but before `listen()`. Inside the bundle it blocked for tens of
  seconds, so the socket was bound, never listening, and the window opened onto a server
  that was not there — with nothing raised anywhere.
- **Startup logging and a readiness gate.** A windowed app has no console, so the above was
  invisible. Startup now logs to Application Support, the server thread's exceptions are
  captured rather than dying quietly in a daemon thread, and the window does not open until
  the port accepts a connection.

---

## Asset ID scheme

From the RAG registry in [background/rag-registry-v2.js](background/rag-registry-v2.js):

| Prefix | Collection | Role | Scope |
|---|---|---|---|
| `F-nnn` | Foundational | WHY | Ships with the app |
| `A-nnn` | Applied | HOW | Ships with the app |
| `C-nnn` | Contextual | WHERE | Ships with the app |
| `S-nnn` | Situational | THIS | **Per project** — user-supplied |

Implemented today: `A-001` evaluation framework, `A-004` copilot role/task, `A-006` output
schema, `A-007` QA protocol, and `S-nnn` per-project reference data. `A-002` (corpus
annotation) and `A-003` (registry management) are specified and unwritten.

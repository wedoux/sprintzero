# QA Readout

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | Declared | Q-01 | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "Unexpected finding (not asked): the moderator noticed participants pausing around the five-minute mark; worth tracking in future sessions."

**Evidence strength:** WEAK
A single moderator observation from one session, offered as a hypothesis to track later, not as a finding about users.

**Claim matches its evidence:** Yes — the claim is explicitly labelled as an unexpected observation worth tracking, not as an established pattern; it stays inside what one note from one session can support.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** The pause is an artefact of the moderation itself (moderator checking notes, a scripted prompt around that point, natural task-switching) rather than anything about participants. One moderator's impression from one session can't tell these apart.
- **What would overturn this finding:** Timestamps from the other five sessions (INT-01 to INT-04, INT-06) showing no clustering of pauses near the five-minute mark; or a session protocol showing a scripted break at that point.
- **Where the evidence underdetermines the claim:** The claim rests entirely on one moderator's recollection from INT-05. There is no timing data, no cross-session comparison, and no participant-side evidence (nothing a participant did or said about pausing). The claim is honest about this by framing itself as something to track, not something known.

**Counter-evidence:** None cited in the material under review.

**Unsupported claims:** None — the claim is scoped to what the single moderator note supports (an observation to track), not to a pattern across participants.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim is framed as an observation worth tracking, not as something validated about users. | n/a |
| CK-04 Product finding without a human story | CLEAR | Not a product claim — it's an observation about session dynamics, flagged for follow-up. | n/a |
| CK-05 Scope and certainty inflation | CLEAR | The scope ("the moderator noticed") and certainty ("worth tracking") match a single-session moderator impression. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim names a specific observable (pausing around five minutes) and a specific next step (track in future sessions). |
| P-03 Transcript Literalism | No | The claim is sourced to the moderator's in-session observation, not to transcript text — it treats tacit knowledge as the source rather than ignoring it. |
| P-04 Volume Mistaken for Strength | No | The claim does not inflate confidence; it rests on one note and says so. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence was present to face or file. |
| P-08 Narrowing Sold as Resolving | No | The claim does not assert a cause or a fix; it flags something to watch. |

### Where does it apply?

**Scope:** One moderator's impression from INT-05, offered as something to track in future sessions. The claim does not generalise beyond that.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | The study record declares no limits (`limits: (none declared)`), so there is no `cannot_claim` to check against. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is made. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| The moderator noticed participants pausing around the five-minute mark | INT-05: "Sessions were running long, I noticed most people paused around the five-minute mark regardless of the task." | Observed (by moderator) | Yes |
| Worth tracking in future sessions | Not cited | Inferred (reasonable editorial judgment on a one-off observation) | Yes — the inference is light and visible |

**Checked against:** Q-01 (the sole declared question).

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | CLEAR | The claim does not answer Q-01, and it is explicitly labelled "Unexpected finding (not asked)" — which is exactly how the drift check allows an off-question observation to be reported. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research is referenced or contradicted; the claim is flagged as something new to watch. |
| P-07 Trust Without Process | No | The reasoning is visible: one moderator observed X, so track it. The conclusion follows from the stated source. |

### Is it theirs or ours?

**Beliefs and evidence:** The observation comes from the moderator (ours), not from what participants did or said (theirs). The claim is honest about this — it attributes the observation to the moderator and proposes tracking it, rather than asserting it as a participant finding.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | CLEAR | No belief register is declared, so part (a) cannot run; part (b) runs on the claim alone and does not fire — the claim attributes the observation to the moderator but does not use that attribution as evidence about users. It flags it for future study instead. | n/a |

### Tacit-knowledge prompt (optional — ask only if a researcher who ran the sessions is available)
In INT-05, when you noticed participants pausing around the five-minute mark — do you remember whether that moment coincided with anything in the session structure (a scripted prompt, a task hand-off, a break for notes), or did it feel independent of what you were doing? That would help tell a participant pattern apart from a moderation artefact before anyone invests in tracking it.

### Decision boundary
- **Supports:** Flagging a pattern-to-watch in future sessions, based on one moderator's impression.
- **Doesn't support:** Any claim that participants systematically pause at five minutes, that this is attention- or task-driven, or that the current session design should change because of it.
- **What would close the gap:** Session timing data (or re-review of recordings) across INT-01 to INT-06 showing whether pauses actually cluster near the five-minute mark, independent of moderator prompts.

**Safe to act on:** Yes — but only for the action the claim actually proposes (track this in future sessions). It is not safe to act on as evidence about participant behaviour.

---

## Note on what was reviewed

One housekeeping point worth flagging: the claim under review is a side observation about session dynamics, not an answer to Q-01 (whether users notice the new filter button). The study's actual research question appears to be unanswered in the material you shared — if there are findings about filter discoverability itself, those are the ones that most need a QA pass. This readout only covers the one claim you submitted.
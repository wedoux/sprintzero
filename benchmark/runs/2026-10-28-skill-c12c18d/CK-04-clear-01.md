# UX Research QA Readout

Before I run the pass: this synthesis looks like it was prepared for review (not generated earlier in this conversation), so a fresh pass is fine. If it was generated in a prior turn with the same model, consider rerunning in a new conversation.

A note on inputs: no belief register and no study record were declared. The user said "none declared", which is a choice I'll respect — I'll proceed, and the checks that need those records will report NOT RUN. If you'd like fuller coverage, see `templates/belief-register.md` and `templates/study-record.md` and fill them in yourself.

---

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

---

## Finding: "In all 6 sessions, participants went straight to the top right for save without hesitation."

**Evidence strength:** STRONG
Six out of six participants independently reached for the top-right corner for save, with corroborating language ("without having to think", "instantly", "exactly where I expected"). The signal is consistent and the claim doesn't extend past what the quotes show.

**Claim matches its evidence:** Yes — the claim says "in all 6 sessions", not "users expect" or "everyone expects". Scope and certainty match the evidence base exactly.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** Participants may have been primed by the task framing, the moderator, or by seeing the save icon before being asked where they'd look. Self-report ("exactly where I expected") after the fact is weaker than observed first-click behaviour — a participant who found it top-right might rationalise that as expectation rather than discovery.
- **What would overturn this finding:** Session recordings showing hesitation, scanning, or first clicks elsewhere before landing top-right; or evidence that participants were shown the location before being asked.
- **Where the evidence underdetermines the claim:** The quotes are reported speech, not observed behaviour. "Went straight to" could be the researcher's paraphrase or the participant's self-description. Without the behavioural record, "without hesitation" is the participant's claim about themselves, not necessarily what happened.

**Counter-evidence:** None in the evidence set — all six quotes point the same way. This is itself worth noting (see CK-05 commentary below): unanimous agreement across a small sample is a signal to probe, not to celebrate.

**Unsupported claims:** None — every element of the claim (all 6, top right, save, without hesitation) is reflected in at least one quote.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim describes observable behaviour ("went straight to the top right"), not an attitude or feeling presented as proven. | n/a |
| CK-04 Product finding without a human story | CLEAR | Not a product claim — this is a claim about what people did. | n/a |
| CK-05 Scope and certainty inflation | CLEAR | Scope is explicitly "6 sessions"; certainty is "without hesitation", which the quotes support. The claim does not generalise to "users" or "everyone". | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim is specific, observable, and tied to a concrete action. |
| P-03 Transcript Literalism | Yes | All six quotes are strikingly similar in structure ("top right", "didn't think", "exactly where"). This may reflect genuine consensus — or it may reflect leading questions, post-hoc rationalisation, or the moderator priming the frame. The written record cannot distinguish these. See tacit-knowledge prompt below. |
| P-04 Volume Mistaken for Strength | Yes, mildly | Six interview quotes are one source type. Six people saying the same thing in interviews is stronger than one, but it is not the same as behavioural data (first-click, time-to-target) confirming the self-report. If the finding is used to argue "users expect save top-right" at scale, this matters. For the claim as written ("in all 6 sessions"), it's a smaller issue. |
| P-05 Counter-Evidence Filed, Not Faced | No | There is no counter-evidence in the set. |
| P-08 Narrowing Sold as Resolving | No | The claim doesn't propose a fix. |

### Where does it apply?

**Scope:** Six interview participants. Nothing in the evidence tells me who they are, what device or product they were using, or what the task was. The claim stays inside "6 sessions" and doesn't extend further — which is correct — but anyone reading this should know the scope is undefined beyond headcount.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no `cannot_claim` to check against. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is being made. |

### Could someone retrace it?

**Provenance**

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| In all 6 sessions | INT-01 through INT-06 | Observed (count) | Yes |
| Participants went to the top right | All 6 quotes name "top right" | Observed (via self-report in quote) | Yes — though self-report, not behavioural record |
| For save | All 6 quotes name "save" | Observed | Yes |
| Without hesitation | INT-02 "no hesitation", INT-06 "instantly", INT-01/03/04/05 "didn't have to think" / "didn't think twice" / "exactly where I expected" | Observed (via self-report) | Yes — self-report of a mental state |

**Checked against:** Nothing declared — no beliefs, questions, or limits to audit against.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study questions declared. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No visible trigger, but cannot be checked without prior-research context. The evidence set gives no prior work to compare against. | n/a |
| P-07 Trust Without Process | No | The finding states its reasoning (6 of 6, consistent language) and the classification follows from it. |

### Is it theirs or ours?

**Beliefs and evidence:** The claim is grounded entirely in what participants said. No borrowed conviction visible — no "the designer confirmed", no "we expected this and heard it". However, with no belief register declared, I can't rule out that the research was set up to confirm a pre-existing belief about convention. If the team believed "save goes top right because that's convention" going in, six confirming interviews is weaker evidence than six interviews that could have gone either way.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | No belief register declared, so part (a) can't run. Part (b) is CLEAR — the claim cites participants, not authority or team agreement. Overall: NOT RUN because part (a) couldn't be checked. | — |

### Tacit-knowledge prompt

The six quotes are remarkably uniform. Was there a moment in any session — a pause before the quote, a glance elsewhere first, a probe from the moderator ("where would you expect save to be?" before they looked) — that would help distinguish genuine instant recognition from post-hoc rationalisation? And was the save icon visible before participants were asked to find it?

### Decision boundary

- **Supports:** These 6 participants, in these 6 sessions, located save in the top right quickly and said it matched their expectation.
- **Doesn't support:** That users in general expect save top-right. That top-right is the right location for save in this product. That no users would struggle with it. That first-click behaviour matched the self-report (unless session recordings confirm this).
- **What would close the gap:** First-click or time-to-target data from the session recordings (if captured), or a larger-sample quantitative check (e.g. a 50-person unmoderated first-click study) if the team wants to generalise from "these 6" to "users".

**Safe to act on:** Yes — for the claim as written ("in all 6 sessions"), the evidence supports it directly. Not yet — for any wider claim the team might be tempted to derive from it ("users expect save top-right"), which would require broader or behavioural evidence.

---

## Summary

This is a well-scoped, honest claim. The main thing to watch for is scope creep in the next write-up: "6 participants went to the top right" is defensible; "users expect save top-right" is not, from this evidence alone. The uniformity of the quotes is worth a second look — six people phrasing the same observation six different-but-similar ways is either strong signal or a methodology artefact, and only the researcher who ran the sessions can tell which.
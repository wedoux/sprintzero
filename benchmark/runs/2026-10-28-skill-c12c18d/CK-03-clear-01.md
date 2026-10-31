I'll note upfront: no belief register or study record was declared, so several checks will report NOT RUN. The user has chosen to proceed without them — that's their call to make, but I'll flag what couldn't be checked as a result.

If you'd like to declare them, see:
- `templates/belief-register.md`
- `templates/study-record.md`

Also worth saying: if this synthesis was produced earlier in the same conversation, run this QA pass in a fresh conversation with only the material pasted in. A model reviewing its own prior output is grading its own homework.

---

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "4 of 5 participants completed checkout without help."

**Evidence strength:** STRONG
Within the five sessions, this is a direct observation of behaviour — not an interpretation, inference, or attitude claim. The number is small, but the claim is calibrated to it.

**Claim matches its evidence:** Yes — the claim states the exact count ("4 of 5"), names the population ("participants"), and describes an observable behaviour ("completed checkout without help") that matches the evidence type (session recordings).

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** The one participant who didn't complete may represent a systematic segment (e.g. first-time users, a specific device, a specific payment method) rather than a one-off. The claim as written doesn't address this because it only reports the count — but it also doesn't claim otherwise.
- **What would overturn this finding:** Reviewing the session recordings and finding that "without help" was interpreted loosely (e.g. the moderator gave hints, or participants paused and were prompted). Also: evidence that one or more of the four "completions" didn't actually finish the full checkout flow.
- **Where the evidence underdetermines the claim:** Five sessions is a small base — fine for the narrow claim made here, but any extension beyond "these five participants" would need more. The claim doesn't extend, which is why it holds.

**Counter-evidence:** None presented in the material. If session recordings exist, a reviewer could verify independently.

**Unsupported claims:** None — the claim is a direct count from the cited evidence.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | Not a claim about people's attitudes, needs or feelings — it's a product check against a behavioural standard (completion without help). | n/a |
| CK-04 Product finding without a human story | CLEAR | The claim cites people-side evidence (observed session behaviour, INT-01 to INT-05). | n/a |
| CK-05 Scope and certainty inflation | CLEAR | Scope ("4 of 5 participants") matches the evidence base exactly; certainty is a direct count, no inflation. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim names an observable behaviour with a specific count — not a label. |
| P-03 Transcript Literalism | No | Evidence is session recordings, not transcripts; the claim doesn't over-read anything. |
| P-04 Volume Mistaken for Strength | No | Only one source type (interviews), but the claim doesn't inflate confidence from volume — it reports what was observed in exactly the number of sessions it was observed in. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence to face. The one non-completion is included in the count, not filed away. |
| P-08 Narrowing Sold as Resolving | No | No causal claim about what the finding "enables." |

### Where does it apply?

**Scope:** Five participants in moderated sessions (INT-01 to INT-05). The claim stays strictly inside that scope — it says "participants," not "users."

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no `cannot_claim` to check against. The claim is self-limiting ("4 of 5 participants"), which is good practice, but there's no declared record of what the study was designed not to cover (e.g. unmoderated use, specific devices, specific user segments). | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is being made. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| 4 of 5 participants completed checkout without help | INT-01 to INT-05 session recordings | Observed | Yes |

**Checked against:** Nothing declared — no belief register, no study record, no stated research questions.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study questions declared, so there's no way to tell whether this finding answers one of them, or is unexpected. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research referenced, but also none claimed as novel — the finding is a plain observation. |
| P-07 Trust Without Process | No | The claim is a count, not a verdict with hidden reasoning. There's nothing to reconstruct. |

### Is it theirs or ours?

**Beliefs and evidence:** The claim comes entirely from observed participant behaviour. No team belief, no authority, no agreement-as-evidence is involved.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | No belief register declared, so part (a) can't run. Part (b) is CLEAR on the claim alone — no attributed opinion is cited as support. Reported NOT RUN because part (a) couldn't run. | — |

### Tacit-knowledge prompt
If a researcher who ran the sessions is available: in the one session where checkout wasn't completed, what specifically stopped the participant? Was it a point in the flow, a payment issue, a confusion about what "complete" meant? That one data point is the most information-dense thing in this evidence set and the claim as written doesn't tell us anything about it.

### Decision boundary
- **Supports:** Checkout works unaided for most participants in this small sample. Enough to say the flow isn't catastrophically broken.
- **Doesn't support:** Any statement about completion rates in production, across devices, across segments, or in unmoderated use. Also doesn't support any claim about *why* the one participant didn't complete.
- **What would close the gap:** The specifics of the one non-completion — what happened, where in the flow, and whether it points at a pattern (e.g. a specific payment method, a specific device). That one case is where the information is.

**Safe to act on:** Not yet — the claim itself is well-formed, but with no study record declared, there's no way to check whether this finding answers a question the team asked (CK-06) or stays within the study's intended scope (CK-02). If the question was "does checkout work for people in this sample?" then yes, you can act on it as a reassurance signal. If it was meant to inform a broader decision about the checkout flow, you'd want the limits written down and the one failure investigated before acting.
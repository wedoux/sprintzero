## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

Belief register and study record were not declared. Before continuing, I want to flag this directly: beliefs and questions are only useful when the people who hold them write them down. If a register and record exist and weren't pasted in, please add them — the checks that depend on them will otherwise report NOT RUN. If they don't exist, see [templates/belief-register.md](templates/belief-register.md) and [templates/study-record.md](templates/study-record.md). I'm proceeding without them because that is your call to make.

---

## Finding: "3 of 8 participants preferred the subscription model over in-app purchases when asked directly; the other 5 said they had no preference."

**Evidence strength:** WEAK

The claim describes what 8 participants said in a small, direct-asked comparison. There's no behavioural data, no corroborating source type, and the "no preference" responses are a majority. Treated as a settled finding about users, it would be thin; treated as what happened in these 8 sessions, it is accurate.

**Claim matches its evidence:** Yes — the claim is scoped to "3 of 8 participants" and names the "when asked directly" condition, and the counts match the evidence exactly (3 preferences stated, 5 no-preference).

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** The 3 stated preferences are an artefact of being asked a direct comparison question. Two of the three (INT-01, INT-02) justified subscription by familiarity ("way simpler", "I already do it for two other apps"), which is a signal about habit, not a preference for subscription as a model. Under this reading, there are zero clean preferences in the evidence set.
- **What would overturn this finding:** Behavioural evidence from an unprompted choice — e.g. in-product data showing what people picked when both options were offered without the researcher framing the comparison. Or sessions where "no preference" participants were asked a follow-up and gave a reason that revealed a hidden preference the direct question missed.
- **Where the evidence underdetermines the claim:** The claim is restricted to "when asked directly" and so stays inside its evidence, but the material gives no sense of what people would do without being asked. The 5 "no preference" responses are also not probed — we don't know whether that means indifference, confusion about the question, or a preference they didn't want to articulate.

**Counter-evidence:** 5 of 8 participants (INT-04 through INT-08) stated no preference. The claim does report this, which is why it doesn't fire CK-05. But any downstream reading that treats the 3-vote plurality as a signal of user preference needs to face that the modal response was indifference.

**Unsupported claims:** none — both halves of the claim trace to the evidence listed.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim reports what participants said in specific sessions; it does not say a preference is validated, confirmed or proven. | n/a |
| CK-04 Product finding without a human story | CLEAR | Not a product claim — this is a claim about what people said. | n/a |
| CK-05 Scope and certainty inflation | CLEAR | The claim says "3 of 8 participants", not "users"; and names the condition ("when asked directly"). Scope and certainty match the evidence. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim names a specific behaviour (stated preference), a specific trigger (direct comparison question), and a specific count. It is not a label. |
| P-03 Transcript Literalism | Yes | The claim treats the transcript as the complete record of preference. The 5 "no preference" responses in particular are a kind of answer that often hides something — a shrug, a pause, a "I guess either is fine" — that the written record flattens. No prompt for the researcher is attached; see the tacit-knowledge prompt below. |
| P-04 Volume Mistaken for Strength | No | The claim doesn't inflate confidence from volume — it reports the raw count honestly, and the count is small. |
| P-05 Counter-Evidence Filed, Not Faced | No | The 5 no-preference responses are stated as part of the finding, not filed away. |
| P-08 Narrowing Sold as Resolving | No | The claim doesn't assert that a fix follows from it. |

### Where does it apply?

**Scope:** 8 interview participants, in sessions where they were asked to compare subscription against in-app purchases. The claim stays inside that.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no `cannot_claim` to check against. The claim is tightly scoped on its face, but we can't tell whether the study was, for example, limited to a single platform, region, or user type that the claim should name. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is being made. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| 3 of 8 participants preferred subscription when asked directly | INT-01, INT-02, INT-03 quotes | Observed | Yes |
| The other 5 said they had no preference | INT-04 through INT-08, described as "said they had no preference either way" | Observed (as reported) | Yes, with a caveat: INT-04 through INT-08 are summarised in one line rather than quoted. We can trace the count but not the exact wording of what each said. |

**Checked against:** nothing declared.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study questions declared, so there's nothing to check whether this finding answers. Worth noting: the claim describes a stated-preference comparison, which is a specific research design — if that wasn't a declared question, this finding may be answering a question nobody asked. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | Can't confirm — no prior-research context given — but nothing in the claim contradicts or re-presents known material visibly. |
| P-07 Trust Without Process | No | The claim shows its reasoning (counts, condition, breakdown) rather than asserting a label. |

### Is it theirs or ours?

**Beliefs and evidence:** The entire claim is sourced to what participants said. No beliefs declared, so there's nothing on the belief side to check against.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | No belief register declared, so part (a) can't run. Part (b) does not fire: the claim is supported by participant evidence, not by attributed opinion. | — |

### Tacit-knowledge prompt (optional — ask only if a researcher who ran the sessions is available)

INT-04 through INT-08 are summarised as "no preference either way." That phrasing often covers a range of actual responses — a quick shrug, a long pause, a qualified "I guess either is fine, but…". Was there a moment in any of those 5 sessions — a hesitation, a follow-up answer, a visible reaction to one option — that would help you tell whether "no preference" means genuine indifference or something the direct question didn't surface?

Also: INT-01 and INT-02 justified their subscription preference by familiarity with other subscriptions, not by anything about the model itself. Did INT-03 give a reason, and did it have the same shape?

### Decision boundary

- **Supports:** When asked a direct comparison question in interviews, more participants in this sample stated a subscription preference than an in-app-purchase preference, but the modal response was no preference. This is useful as a signal that neither model is obviously rejected and that monetisation framing may matter more than monetisation model.
- **Doesn't support:** Any claim that subscription is preferred by users, that 3-of-8 constitutes a mandate, that no-preference means indifference (it may mean the question didn't land), or that stated preference predicts actual choice.
- **What would close the gap:** The single most useful next piece of evidence is a behavioural signal — either an A/B of the two monetisation options in-product, or a session design where participants encounter both without being asked to compare. Short of that, a probe into why the 5 "no preference" participants had no preference would substantially change what this finding means.

**Safe to act on:** Not yet — the claim is honest and well-scoped, but 8 interviews with a direct-asked comparison and a 3/5 split is thin evidence for any monetisation decision. Treat as an early signal, not a basis for choosing a model.
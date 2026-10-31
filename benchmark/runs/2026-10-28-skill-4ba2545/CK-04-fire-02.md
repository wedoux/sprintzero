## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | Declared | B-01 | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "Moving the save button to the top right is the right call."

**Evidence strength:** WEAK
No evidence has been cited for this claim. The only input behind it is one low-confidence belief, held by one person, that engineering already disagrees with.

**Claim matches its evidence:** No — the claim is stated as a settled decision ("the right call") on top of a belief the register itself rates as low-confidence and contested.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** Users don't have a strong expectation either way, and top-left would be equally fine (or better, as engineering suggests) because it matches existing icon conventions in this product. Nothing in the material rules this out.
- **What would overturn this finding:** A usability session where participants are asked to save something and reach for the top-left (or anywhere else) before finding the top-right button; or analytics on a comparable product showing position has no measurable effect on save behaviour.
- **Where the evidence underdetermines the claim:** Entirely. No observation of any user has been offered. The claim rests on one person's recollection of "a couple of other apps."

**Counter-evidence:** The belief register itself records engineering's dissent — top-left matches the product's own icon conventions. The claim doesn't engage with this at all.

**Unsupported claims:** The entire claim. There is no cited evidence of any kind behind it.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim is about the product (button position), not a validated claim about people. | n/a |
| CK-04 Product finding without a human story | FIRES | "This product finding has no evidence about people behind it, and no assumption the team agreed to." The claim is a product decision ("Moving the save button to the top right is the right call") with no people-side evidence cited, and B-01 is explicitly `agreed_by_all = no`. | B-01 (not agreed) |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." The claim asserts "the right call" — a settled product decision — on top of zero cited evidence and a belief the register itself rates `low`. | (no declared item; evidence base is empty) |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "The right call" is a verdict with no behaviour, trigger or consequence under it. Swap "save button" for any other control and the sentence still reads the same. |
| P-03 Transcript Literalism | No | No transcript or review material is in play. |
| P-04 Volume Mistaken for Strength | No | No evidence units at all, so nothing to count. |
| P-05 Counter-Evidence Filed, Not Faced | Yes | Engineering's dissent is on the record in B-01's `dissent_note` and the claim doesn't address it. |
| P-08 Narrowing Sold as Resolving | No | No narrowing is being claimed. |

### Where does it apply?

**Scope:** The claim is unbounded — it names no user group, no context, no platform. There is no study record declaring limits, so there's nothing to check it against.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no `cannot_claim` statements to check against. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is being made. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "Moving the save button to the top right is the right call." | not cited | Inferred (from B-01) | No — the claim restates a belief rated low-confidence and contested, with no supporting evidence. |

No part of this claim has supporting evidence. The only thing behind it is B-01, and B-01 is a belief, not evidence.

**Checked against:** B-01 (the only declared item). No questions or limits were declared.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study record `questions` declared, so there is nothing to map the claim against. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research is referenced on either side. |
| P-07 Trust Without Process | Yes | The claim is a bare verdict ("the right call") with no reasoning given — you cannot reconstruct how it was reached. |

### Is it theirs or ours?

**Beliefs and evidence:** The claim is entirely "ours." It restates B-01 — one person's `own_experience` of "a couple of other apps" — as a product decision. No participant said this, because no participants have been consulted.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | FIRES (part b) | "This confidence comes from who said it, not from evidence." The claim's only backing is a belief held by one team member, with engineering on record disagreeing. Part (a) does not fire because B-01 is `low` confidence, not `high`. | B-01 |

### Tacit-knowledge prompt
Not applicable — no sessions have been run, so there is no researcher to ask.

### Decision boundary
- **Supports:** Nothing yet. There is an open internal disagreement (B-01 vs. engineering's view) about where the save button should go. That's a question worth answering, not a finding.
- **Doesn't support:** Any statement about where the save button *should* go. The material contains no observation of any user, no analytics, no competitive analysis beyond "a couple of other apps," and no agreed team position.
- **What would close the gap:** The cheapest useful next step is a short unmoderated test (even 5–8 participants) asking people to save something in a prototype, and seeing where they reach first. If that's too much, a documented review of save-button placement in the apps members actually use would at least ground B-01 in something checkable.

**Safe to act on:** Not yet — the claim cites no evidence about users, rests on a low-confidence belief that engineering disputes, and is stated as a settled decision ("the right call") rather than as the open question it actually is.
# QA Readout

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | Declared (1 belief) | B-01 | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

**A note before the finding.** The claim comes with no study record, no cited evidence, and one belief rated `low`. This isn't a case of a weak finding — there isn't a finding to evaluate in the research sense. What's below treats the sentence as a product recommendation and asks whether the material provided supports it. It doesn't.

---

## Finding: "Moving the save button to the top right is the right call."

**Evidence strength:** WEAK
There is no cited evidence about what users do, and the one declared belief that touches this question is low-confidence, grounded in "a couple of other apps we use", and openly disputed by engineering.

**Claim matches its evidence:** No — the claim asserts a design decision ("the right call") while the only input behind it is a low-confidence belief the team doesn't agree on.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** Users don't have a stable expectation about save-button location in this app's category, and the choice should be made on internal consistency grounds (which is the argument engineering is already making for top-left).
- **What would overturn this finding:** Session evidence showing where users actually reach first when they try to save — or a convention audit of comparable apps, done systematically rather than from memory.
- **Where the evidence underdetermines the claim:** Entirely. There is no evidence base here, only a stated belief.

**Counter-evidence:** The dissent note itself — engineering's view that top-left matches the app's own icon conventions — is a live counter-position that the claim doesn't address.

**Unsupported claims:** The whole claim. No evidence was cited.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | Not a claim about people — it's a product recommendation. | n/a |
| CK-04 Product finding without a human story | FIRES | "This product finding has no evidence about people behind it, and no assumption the team agreed to." The claim recommends a product change; no people-side evidence is cited, and the only belief it rests on (B-01) has `agreed_by_all = no`. | B-01 |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." "The right call" is a settled recommendation; the input is one low-confidence, disputed belief. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim is specific (a named button, a named position); it's unsupported, not vague. |
| P-03 Transcript Literalism | No | No transcript or session material is in play. |
| P-04 Volume Mistaken for Strength | No | No evidence volume is being leaned on. |
| P-05 Counter-Evidence Filed, Not Faced | Yes | Engineering's dissent is recorded in the belief register and not addressed by the claim. |
| P-08 Narrowing Sold as Resolving | No | No narrowing argument is being made. |

### Where does it apply?

**Scope:** No scope is stated. The claim is about "users" in general, with no sample behind it.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record was declared, so no `cannot_claim` exists to check against. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is made. |

### Could someone retrace it?

**Provenance**

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| Top-right is the right position for the save button. | Not cited. | Inferred (from B-01). | No — the belief it rests on is itself unsourced beyond "a couple of other apps we use". |

The entire claim is untraceable to evidence. The only upstream input is a belief grounded in casual observation.

**Checked against:** The declared belief B-01. No questions or limits were declared.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study questions were declared, so there is nothing to check whether this answers. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior-research claim is being made or missed, as far as the material shows. |
| P-07 Trust Without Process | Yes | The claim is asserted as a conclusion ("the right call") with no reasoning chain. You can agree or disagree, but you can't audit how it was reached. |

### Is it theirs or ours?

**Beliefs and evidence:** Entirely "ours". The claim rests on B-01, which is a team-side belief sourced from `own_experience` — "a couple of other apps we use". No participant evidence is cited. Engineering's dissent on the register means even the belief itself isn't a shared working assumption.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | CLEAR | Part (a): B-01 is `low` confidence, so the high-confidence condition isn't met. Part (b): the claim doesn't cite attributed opinion as its support — it cites nothing. | n/a |

A note on CK-01: it clears on technicality, not because the input is sound. The underlying problem — a product decision resting on team intuition — is caught by CK-04 and CK-05 instead.

### Decision boundary
- **Supports:** That someone on the team has a hunch, drawn from other apps, that top-right is the expected location. That engineering disagrees and prefers top-left on internal-consistency grounds.
- **Doesn't support:** Any claim about what users expect, what they'd reach for, or which position would work better.
- **What would close the gap:** The single most useful next step is to decide what question the team is actually trying to answer. If it's "where do users expect the save button?", a short round of sessions — even five people — would produce more signal than this debate currently has. If it's "which position is more consistent with the rest of our UI?", that's a convention question, not a research question, and the dissent note suggests engineering already has a view worth hearing out.

**Safe to act on:** Not yet — the claim is a product recommendation resting on one low-confidence, disputed belief and no evidence. Treat it as a hypothesis to test, not a decision to ship.
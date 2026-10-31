## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | Declared | B-01 | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "The new onboarding carousel works."

**Evidence strength:** WEAK
No evidence was cited for this claim. There is nothing in the material to judge whether the carousel "works" — for whom, measured how, or in what sense.

**Claim matches its evidence:** No — the claim asserts a product outcome with no evidence attached and no agreed assumption behind it.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** Users skip the carousel entirely (the support team's view noted in B-01's dissent), so it introduces nothing — "works" would be false by any user-outcome measure.
- **What would overturn this finding:** Analytics showing low swipe-through or dismissal rates on the carousel; session recordings or interviews showing participants skipping it; support tickets indicating users didn't learn the features it introduces.
- **Where the evidence underdetermines the claim:** Everywhere. No evidence of any kind was cited. The claim is not weakly supported — it is unsupported.

**Counter-evidence:** The dissent note on B-01 records that the support team believes most people skip carousels. This isn't participant evidence, but it directly contradicts the claim and has not been addressed.

**Unsupported claims:** The entire finding. "Works" is undefined, and no evidence unit is cited.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | Not a claim about people — it's a claim about the product. | n/a |
| CK-04 Product finding without a human story | FIRES | "This product finding has no evidence about people behind it, and no assumption the team agreed to." The claim "The new onboarding carousel works" cites no people-side evidence, and the only relevant belief (B-01) has `agreed_by_all = no`. | B-01 |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." The claim asserts "works" as a settled outcome on zero cited evidence. | no cited evidence |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "Works" has no observable behaviour, no trigger, no consequence. The sentence would read the same for any onboarding element in any product. |
| P-03 Transcript Literalism | No | No transcript or source material was over-read; the problem is the opposite — nothing was read at all. |
| P-04 Volume Mistaken for Strength | No | No evidence volume to inflate. |
| P-05 Counter-Evidence Filed, Not Faced | Yes | The dissent on B-01 (support team's view that users skip carousels) directly contradicts the claim and is nowhere addressed in the finding. |
| P-08 Narrowing Sold as Resolving | No | No narrowing claim is made. |

### Where does it apply?

**Scope:** The claim implies a universal product outcome ("works") with no stated population, context, or time frame. No limits were declared, so there is nothing to check it against — but the claim's scope is also unbounded, which is a problem of its own.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No limits were declared in the study record, so there is nothing to check the claim against. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is made across populations or markets. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "The new onboarding carousel works." | not cited | Inferred (or asserted) | No — no supporting evidence of any kind. |

The entire finding has no supporting evidence. It cannot be retraced.

**Checked against:** B-01 (the only declared item). No questions or limits were declared, so CK-06 and CK-02 could not run.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No questions were declared in the study record, so there is nothing to map the claim to. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior-research context has been introduced or ignored — the problem is absence of evidence, not mishandling of prior work. |
| P-07 Trust Without Process | Yes | The verdict "works" is asserted with no reasoning chain at all. There is nothing to audit. |

### Is it theirs or ours?

**Beliefs and evidence:** The claim rests on no participant evidence. The only related declared item is B-01 — the team's own low-confidence belief that "a carousel is the clearest way to introduce new features," sourced from `own_experience`, not agreed by all, with the support team dissenting. The finding appears to come from the team, not from users.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | FIRES (part b) | "This confidence comes from who said it, not from evidence." The claim asserts the carousel "works" with no cited participant evidence; the only relevant input is the team's own belief (B-01), and even that is `low` confidence and disputed internally. Part (a) does not fire because B-01 is `low` confidence, not `high`. | B-01 |

### Tacit-knowledge prompt
Not applicable — there is no session or source material to probe. The gap here is not something a researcher saw and didn't write down; it is that no research appears to have been consulted.

### Decision boundary
- **Supports:** Nothing. There is no evidence behind this claim.
- **Doesn't support:** Any statement about whether the carousel helps users understand new features, whether users engage with it, or whether it meets any product goal.
- **What would close the gap:** First, a definition of what "works" means for this carousel — swipe-through rate, feature awareness after onboarding, task completion, something measurable. Then evidence of that measure: analytics, a short usability test, or support-ticket data about the features the carousel introduces. Resolving the support team's dissent (B-01) is the single highest-value piece of evidence to go get.

**Safe to act on:** Not yet — the claim cites no evidence, "works" is undefined, and the team's own belief about carousels is low-confidence and internally disputed. This is a hypothesis stated as a finding.

---

**A note on this QA pass:** The result above was decidable on the material provided — a claim with no cited evidence and a dissenting internal belief fails on its face. But three checks (CK-02, CK-06, and CK-01 part (a)) are reported as NOT RUN because no study record was declared and B-01's confidence is `low`. If you want a fuller audit, declaring the study's questions and limits — and clarifying whether anyone holds a `high`-confidence belief that the carousel works — would let those checks run.
## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | Declared | B-01 | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

---

## Finding: "The new onboarding carousel works."

**Evidence strength:** WEAK
No evidence was supplied for this claim. There is nothing to weigh — only an assertion about a product.

**Claim matches its evidence:** No — the claim is a general verdict ("works") with no evidence behind it and no definition of what "works" means.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** The carousel is skipped by most users — exactly the concern the support team raised in the dissent note on B-01 — and "works" is being asserted on the basis of the design being shipped, not on what people do with it.
- **What would overturn this finding:** Behavioural data showing people skip past the carousel without engaging (analytics on dwell time, swipe-through rates, or whether users can recall or use the features introduced); or session recordings where participants ignore or dismiss it.
- **Where the evidence underdetermines the claim:** Everywhere. No evidence was provided at all. "Works" is also undefined — works for whom, measured how, against what threshold?

**Counter-evidence:** None cited. The support team's view (noted in B-01's dissent) that most people skip carousels is not addressed.

**Unsupported claims:** The entire claim. "Works" is asserted with no supporting evidence of any kind.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim is about the product, not a validated statement about people. | n/a |
| CK-04 Product finding without a human story | FIRES | "This product finding has no evidence about people behind it, and no assumption the team agreed to." The claim is about the product (the carousel), cites no people-side evidence, and the only relevant belief (B-01) has `agreed_by_all = no`. | B-01 (not agreed) |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." "Works" is a definitive verdict resting on no evidence. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "Works" is a label, not an observable behaviour. No trigger, no consequence, no decision it points at. The sentence would read the same about any onboarding element in any product. |
| P-03 Transcript Literalism | No | No transcript or source material is being over-read; there's no source at all. |
| P-04 Volume Mistaken for Strength | No | No volume of evidence is being leaned on — there is none. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence is listed in the claim (though the support team's dissenting view is unaddressed; this is closer to CK-04 and the falsification gap). |
| P-08 Narrowing Sold as Resolving | No | No narrowing is claimed. |

### Where does it apply?

**Scope:** Undefined. No population, context or timeframe is named. "Works" for whom, where, when?

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no `cannot_claim` to check against. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer across populations is being claimed (or hedged). |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "The new onboarding carousel works." | Not cited | Inferred (or asserted — unclear) | No — no evidence provided |

The entire claim is untraceable. Nothing in the material supports it.

**Checked against:** B-01 (belief register). No questions or limits were declared, so CK-06 and CK-02 could not run.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No research questions were declared, so there is nothing to map the claim against. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | Cannot assess — no prior research is referenced, but none is mentioned as existing either. |
| P-07 Trust Without Process | Yes | The verdict ("works") is asserted with no reasoning, no classification derivation, no visible argument. It is pure conclusion. |

### Is it theirs or ours?

**Beliefs and evidence:** The claim rests on nothing from participants — no evidence was cited. The only relevant item in play is B-01, a low-confidence `own_experience` belief that carousels are the clearest way to introduce features, which the support team disagrees with. The claim "works" is upstream team conviction presented as a verdict.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | FIRES (part b, partial) | "This confidence comes from who said it, not from evidence." The claim is asserted with no evidence of any kind — the only thing underneath it is team belief. Part (a) does not fire because B-01 is `low` confidence, not `high`; but the pattern part (b) targets — a claim about people/product carried by team conviction rather than participant evidence — is exactly what's happening. | B-01 (low-confidence team belief, with internal dissent) |

### Tacit-knowledge prompt
Not applicable — there are no sessions to draw on. The question to ask the team instead is: **what specifically does "works" mean here, and what evidence (if any) prompted you to write this sentence?** If the answer is "it shipped" or "nobody has complained", that is the finding to examine, not the carousel.

### Decision boundary
- **Supports:** Nothing. No evidence was provided.
- **Doesn't support:** Any claim about whether the carousel works, for whom, or against what definition of "working".
- **What would close the gap:** First, a definition of what "works" means for this carousel (completion rate? feature recall? users opting into a feature it introduced?). Then the matching evidence — most cheaply, analytics on skip and dwell rates; more richly, a handful of sessions watching real users encounter it.

**Safe to act on:** Not yet — the claim has no evidence behind it, CK-01 and CK-04 and CK-05 fired, P-01 and P-07 triggered, and the two checks that could have placed the claim in context (CK-02, CK-06) could not run because no study record was declared.

---

### A note on what this QA pass could and couldn't do

Two things to flag honestly:

1. **Most of the "Where does it apply?" and "Could someone retrace it?" checks reported NOT RUN**, because no study record was declared. If this finding is going to inform a real decision, writing even a lightweight study record ([templates/study-record.md](templates/study-record.md)) would let those checks actually run next time.

2. **The claim is thin enough that most of the review is pointing at the same thing from different angles**: there is no evidence, and "works" is undefined. The multiple fired checks aren't independent confirmations — they're the same underlying problem showing up in each lens. One real piece of behavioural evidence, plus a definition of "works", would resolve most of them at once.
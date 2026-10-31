Before starting: this is a quick QA check on a single claim with a tiny belief register, no study record, and no cited evidence. I'll run the pass as-is, but flag that several checks can't actually run.

I'll track through the workflow:

- [x] Step 0: Gather declarations — belief register (one item, B-01) present; study record declared as none; no evidence cited
- [x] Step 1: Confirm there's a conclusion — yes, one claim
- [x] Step 2: Provenance — no evidence cited at all
- [x] Step 3: Falsification — done below
- [x] Step 4: Pitfalls — done
- [x] Step 5: CK pass — done
- [x] Step 6: Readout

---

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | Declared (one item) | B-01 | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "Hikers want maps that work offline — stakeholders confirmed it in last week's review — so offline download will be on by default."

**Evidence strength:** WEAK
No evidence from hikers is cited. The claim rests on a stakeholder review and, implicitly, a low-confidence belief sourced from the author's own experience on two trails.

**Claim matches its evidence:** No — the claim is stated as settled fact and drives a default-on product decision, with no cited observations of hikers and only attributed stakeholder agreement behind it.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** Hikers may want offline maps *available* but not *on by default* — defaulting on costs storage, battery and setup friction, which could annoy day hikers on well-covered trails. The ops lead's dissent (coverage is fine on top trails) is a live counter-signal.
- **What would overturn this finding:** Interviews or survey data from hikers showing either (a) they don't lose signal often enough to care, or (b) they want offline as an option but not a default.
- **Where the evidence underdetermines the claim:** Entirely. No hiker-side evidence is cited. The jump from "want offline maps" to "on by default" is also unsupported — defaulting is a separate decision.

**Counter-evidence:** The dissent note on B-01 (ops lead: coverage on top trails is fine) directly contradicts the belief the claim rests on, and is not addressed.

**Unsupported claims:** Every part. "Hikers want maps that work offline" has no cited hiker evidence. "Stakeholders confirmed it" is attributed opinion, not evidence. "Offline download will be on by default" is a product decision with no supporting rationale beyond the above.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | FIRES | "This treats what we learned about people as proven. Only a product can be validated." — "stakeholders confirmed it" presents a claim about what hikers want as settled. | n/a |
| CK-04 Product finding without a human story | NOT RUN | The claim is a product finding ("on by default") with no people-side evidence cited. The belief register has one item but `agreed_by_all = no`, so no agreed assumption supports it either. Reporting NOT RUN because the register is thin — only one belief, directly contested — rather than FIRES, since the user hasn't declared a fuller set of assumptions to check against. | — |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." — "Hikers want maps that work offline" generalises to all hikers with zero cited evidence; "will be on by default" is a certain product commitment on the same empty base. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "Hikers want maps that work offline" — no behaviour, no trigger, no consequence specific to this product. Swap "hikers" for any outdoor user and it reads the same. |
| P-03 Transcript Literalism | No | No transcript or session evidence is in play. |
| P-04 Volume Mistaken for Strength | No | There's no volume to mistake — zero evidence units. |
| P-05 Counter-Evidence Filed, Not Faced | Yes | The ops lead's dissent on B-01 is on the record and is neither acknowledged nor argued against. |
| P-08 Narrowing Sold as Resolving | No | No narrowing claim is being made. |

### Where does it apply?

**Scope:** The claim is stated for "hikers" with no qualifier — no region, trail type, experience level, or app context. The one cited anecdote (B-01's rationale) is two trails, one person, one summer.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no `cannot_claim` to check against. The scope problem is caught by CK-05 and P-01 instead. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is being hedged. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "Hikers want maps that work offline" | not cited | Inferred | No — no hiker evidence provided. |
| "stakeholders confirmed it in last week's review" | attributed opinion ("stakeholders"); no names, no notes | Inferred | No — not traceable to a specific statement by a specific person. |
| "offline download will be on by default" | n/a (product decision) | Inferred | No — no rationale cited for defaulting on vs. offering as an option. |

Every claim in the finding is unsupported. This is not a traceability gap at the margins; there's nothing to trace.

**Checked against:** B-01 (the only declared belief); no questions or limits declared.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study questions declared, so there's nothing for the claim to map to or drift from. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research mentioned on either side; nothing to check against. |
| P-07 Trust Without Process | Yes | The claim asserts the verdict ("hikers want X, so we'll do Y by default") with no reasoning chain — not even an argument that stakeholder agreement counts as evidence. The reader can only accept or reject the conclusion. |

### Is it theirs or ours?

**Beliefs and evidence:** Nothing in the claim comes from hikers. The underlying belief B-01 is sourced from `own_experience` ("happened to me on two trails"), rated low confidence, and actively disputed by the ops lead. The claim's stated support — "stakeholders confirmed it" — is attributed opinion, not evidence from users.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | FIRES (part b) | "This confidence comes from who said it, not from evidence." — "stakeholders confirmed it in last week's review" is the only support offered for a claim about what hikers want. Part (a) does not fire: B-01 is rated low, not high. | B-01 (contested belief treated as settled via stakeholder agreement) |

### Tacit-knowledge prompt
Not applicable — no sessions were run.

### Decision boundary
- **Supports:** That at least one person on the team (the author) has personally lost signal on two trails, and that stakeholders in a review did not object to building offline maps.
- **Doesn't support:** Any claim about what hikers in general want; any claim that offline-by-default is the right design; any claim that the ops lead's contrary view has been addressed.
- **What would close the gap:** A small round of interviews or a survey of actual hikers using the app, covering (a) how often they lose signal on the trails they use, and (b) whether they'd want offline on by default or as an opt-in. Even 6–8 sessions would move this out of "no evidence" territory.

**Safe to act on:** Not yet — the claim rests on stakeholder agreement and one person's experience on two trails, with the only declared belief directly contested by the ops lead. There is no evidence from hikers at all.

---

## Summary

This claim fails the basic defensibility test: it makes a confident, general statement about what hikers want and locks in a product default, with zero cited user evidence and an unresolved internal disagreement about the premise. The strongest single recommendation is to pause the "on by default" decision until you have even a small amount of hiker-side data — and to argue with the ops lead's dissent rather than route around it via stakeholder sign-off.

Three checks reported NOT RUN (CK-02, CK-04, CK-06) because no study record was declared and the belief register has only one contested item. If you want a fuller QA pass, declaring a study record (what decision this informs, what questions you asked, what the research can't tell you) would let those checks actually run.
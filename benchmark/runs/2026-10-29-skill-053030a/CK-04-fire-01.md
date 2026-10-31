I'll run the QA pass on this. Let me work through the workflow.

**Step 0 — Declarations gathered.**
- Belief register: declared (B-01 only).
- Study record: none declared.
- Evidence: none cited.

**Step 1 — There is a conclusion to evaluate** ("The new onboarding carousel works").

**Step 2 — Provenance.** The claim cites no evidence at all. Untraceable.

**Step 3 — Falsification.** No evidence was supplied, so there's nothing to try to break the claim against. The claim is underdetermined on its face.

**Step 4 — Pitfalls screen.** P-01 fires ("works" is a label with no observable behaviour, trigger or consequence). P-07 fires (the verdict is asserted with no reasoning shown). Others can't be assessed without evidence.

**Step 5 — CK pass.** See table in the readout.

**Step 6 — Readout below.**

---

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | Declared | B-01 | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "The new onboarding carousel works."

**Evidence strength:** WEAK
No evidence was supplied with the claim, and no study record was declared. There is nothing behind the verdict beyond the assertion itself.

**Claim matches its evidence:** No — the claim asserts a product verdict ("works") with no cited evidence of any kind, and no agreed working assumption behind it.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** The carousel is skipped by most users (the dissent note on B-01 says the support team believes exactly this). The same claim — "it works" — would read identically whether users engage with it or ignore it entirely.
- **What would overturn this finding:** Behavioural data showing low engagement (swipe-through rate, dwell time, skip rate), or session evidence of users bypassing or misunderstanding it.
- **Where the evidence underdetermines the claim:** Everywhere. No evidence was cited at all.

**Counter-evidence:** The belief register itself contains a dissent note (support team: "most people skip it") that directly contradicts "works." The claim does not address it.

**Unsupported claims:** The entire finding. "Works" has no evidence behind it.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | Not a claim about people — it's a product verdict. | n/a |
| CK-04 Product finding without a human story | FIRES | "This product finding has no evidence about people behind it, and no assumption the team agreed to." The claim "The new onboarding carousel works" cites no people-side evidence, and B-01 (the only declared belief) has `agreed_by_all = no`. | B-01 (not agreed) |
| CK-05 Scope and certainty inflation | NOT RUN | No evidence was supplied, so scope and certainty can't be compared to it. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "Works" is a label. No observable behaviour, no trigger, no consequence. Swap "carousel" for any other feature and the sentence reads the same. |
| P-03 Transcript Literalism | No | No transcript or source text is in play. |
| P-04 Volume Mistaken for Strength | No | No evidence volume is being leaned on — there's no evidence at all. |
| P-05 Counter-Evidence Filed, Not Faced | Yes | The dissent note on B-01 ("support team thinks most people skip it") is a direct counter-signal to "works." The claim does not acknowledge or argue against it. |
| P-08 Narrowing Sold as Resolving | No | No narrowing is claimed. |

### Where does it apply?

**Scope:** Unknown. The claim doesn't say which users, which context, or which measure of "works."

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No limits were declared. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is made. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "The new onboarding carousel works." | Not cited | Inferred (or asserted) | No — no evidence of any kind is behind this claim. |

The entire finding is unsupported. Nothing in the material under review traces to a participant, a data point, or a document.

**Checked against:** B-01 (the only declared item). No questions or limits were declared, so CK-06 and CK-02 could not run.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No questions declared. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior-research context is in play to check against. |
| P-07 Trust Without Process | Yes | The verdict ("works") is stated with no reasoning. You cannot reconstruct how anyone arrived at it from what's written. |

### Is it theirs or ours?

**Beliefs and evidence:** The only thing on the table is B-01, a `low`-confidence belief sourced from `own_experience` ("It's what our last redesign used"), with the support team dissenting. The claim "works" doesn't restate B-01 directly, but it rests on the same unexamined assumption and ignores the dissent.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | FIRES (part b) | "This confidence comes from who said it, not from evidence." The claim is a bare assertion with no cited evidence and no participant behaviour behind it. B-01 is low-confidence, so part (a) doesn't fire — but the claim is stronger than the belief it rests on, and the dissent note is unaddressed. | B-01 |

### Tacit-knowledge prompt
Not applicable — there are no sessions to probe. The gap here isn't tacit knowledge; it's the absence of any evidence at all.

### Decision boundary
- **Supports:** Nothing. The claim as written is unsupported.
- **Doesn't support:** Any statement about whether the carousel works, for whom, or by what measure.
- **What would close the gap:** Before anything else, decide what "works" means — completion of onboarding? engagement with the carousel itself? retention afterwards? Then gather the behavioural data (swipe-through, skip rate, time on screen) or run sessions to see what users do with it. The support team's dissent gives you a specific hypothesis to test.

**Safe to act on:** Not yet — the claim is a bare assertion with no evidence behind it, directly contradicted by a declared dissent, and three checks (CK-02, CK-05, CK-06) could not run because the study record was not declared.

---

**Summary.** This is not a finding yet; it's a verdict without an argument. Two checks fired (CK-01 part b, CK-04), three could not run (CK-02, CK-05, CK-06), and three pitfalls triggered (P-01, P-05, P-07). The most important move is not to gather more data first — it's to decide what question the carousel is meant to answer and write it into a study record, so that whatever evidence gets gathered next can actually be checked against something.
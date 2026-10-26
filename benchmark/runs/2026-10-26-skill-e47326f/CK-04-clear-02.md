QA Progress:
- [x] Step 1: Confirm there's a conclusion to evaluate (not raw notes)
- [x] Step 2: Provenance pass — trace every claim to evidence
- [x] Step 3: Falsification pass — try to break each conclusion
- [x] Step 4: Pitfalls check — screen against pitfalls taxonomy
- [x] Step 5: Produce the readout

---

## Summary

| Finding | Evidence strength | Pitfalls triggered |
|---|---|---|
| Cut carousel from 5 → 2 screens | **WEAK** | P-01, P-05, P-07, P-08 |

---

## Finding: "Cutting the onboarding carousel from five screens to two is the right call."

**Evidence strength: WEAK**
The claim is a product decision stated as a conclusion, but nothing in the material provided actually supports it. There is one team principle (B-01) about a 60-second onboarding target, no study, and no cited evidence. The register itself declares no evidence behind the claim. This is a proposal, not a research finding — and as a research-backed decision, it does not hold up.

### Provenance

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| The carousel currently has five screens | not cited | Asserted | No — no artifact, screenshot, analytics event, or spec referenced |
| Two screens is the right target | not cited | Inferred | No — no evidence that 2 (vs. 3, or 1, or a non-carousel pattern) is the correct number |
| Cutting screens will improve the onboarding outcome the team cares about | not cited | Inferred | No — no evidence linking screen count to completion time, drop-off, activation, or any other outcome |
| The 60-second target (B-01) is currently being missed | not cited | Inferred from implication | No — B-01 states the target but the register provides no measurement of current performance against it |

Every substantive claim embedded in this recommendation is uncited. The only piece of grounded material in the register (B-01) establishes a *goal*, not a diagnosis and not a solution.

### Falsification pass

- **Strongest counter-hypothesis:** The bottleneck in onboarding time is not screen count. It could be permission prompts, account creation, a slow network call, a confusing single screen that users re-read, or a value-prop screen users deliberately dwell on. Cutting from 5 → 2 could leave the 60-second target still missed, or could hit the target while hurting a downstream metric (activation, feature discovery, retention) that the carousel was quietly supporting.
- **What would overturn this finding:** Analytics showing time-per-screen and drop-off-per-screen in the current five-screen flow; a usability test or A/B test comparing variants; qualitative data showing users find specific screens redundant. None of this is present.
- **Where the evidence underdetermines the claim:** Everywhere. There is no diagnostic evidence of *why* onboarding is (or isn't) hitting the 60-second target, and no evaluative evidence that two screens is better than five, three, or zero.

### Pitfalls checked

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | **Yes** | "The right call" is a label, not an observable behaviour or mechanism. No trigger (what problem is being solved), no consequence (what metric moves), no behavioural anchor. The sentence would read identically in a report about any other product's onboarding. |
| P-02 Context Blindness | No | B-01 (the 60s target) is the only prior context on the table and the claim is at least gesturing in its direction. Nothing in the register contradicts it. Noted as not-triggered, but only because the prior-art surface is thin. |
| P-03 Transcript Literalism | N/A | No transcripts or review text in scope. |
| P-04 Volume Mistaken for Strength | No | Not triggered because there is no evidence at all — not even single-source evidence. The failure here is upstream of volume. |
| P-05 Counter-Evidence Filed, Not Faced | **Yes** | The register has a "dissent_note" column and a dissent field on B-01 is blank, but more importantly: the obvious counter-hypothesis (screen count isn't the bottleneck, or cutting screens hurts a downstream metric) isn't acknowledged anywhere in the claim. Counter-evidence hasn't been filed *or* faced — it's absent. |
| P-06 Formulaic Transfer Hedge | N/A | No transfer claim being made. |
| P-07 Trust Without Process | **Yes** | "The right call" asserts a classification without reasoning. There's no derivation from B-01 → diagnosis → intervention → predicted outcome. The conclusion is stated; the thinking that would produce it is missing. If you tried to reconstruct the reasoning from what's on the page, you couldn't. |
| P-08 Narrowing Sold as Resolving | **Yes** | Even granting that the team has correctly identified onboarding length as a problem (which isn't established), moving from "onboarding is too long" to "cut carousel to 2 screens" is treating a diagnostic hypothesis as a resolved intervention. Narrowing to the carousel is at best an investigative claim ("the carousel is worth examining"); the current claim is causal ("cutting it is the right call"). |

### What would change this verdict

One piece of evidence would move this fastest: **time-per-screen and drop-off-per-screen analytics for the current five-screen flow**, measured against the 60s target from B-01. That would tell the team (a) whether onboarding is actually missing the target, (b) whether the carousel is the thing causing it to miss, and (c) which specific screens are the cost centres. Without that, "cut to two" is a guess dressed as a decision.

Second-best: a quick moderated usability test (n=5–8) of the current flow, which would surface whether users perceive the screens as redundant, informative, or confusing — the qualitative counterpart to the analytics.

### Tacit-knowledge prompt

Not applicable — no sessions have been run. The gap here isn't tacit knowledge the researcher holds; it's evidence that hasn't been collected yet. The team should be commissioning a study, not QA-ing a conclusion.

---

**One meta-note for the user:** this register is a good stress test of the skill, but it's worth being explicit — there is no research here to QA. The claim under review is a product proposal with a single team principle attached. If the goal was to see whether this skill would flag that absence rather than confabulate support for the decision, the answer is yes, and the recommendation to the team would be: don't ship this change on the current evidence base.
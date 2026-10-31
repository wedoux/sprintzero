# QA Readout

**Note on process.** I'm running this QA pass as requested on the material you provided. The synthesis was supplied directly rather than produced in this conversation, so no fresh-conversation reset is needed.

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | Declared | B-01 | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "Forecast model accuracy is the problem behind the trust complaints. Recommend investing engineering time in improving the forecast model."

**Evidence strength:** WEAK
The evidence actively contradicts the finding. Of the four cited reviews, one (R03) explicitly praises forecast accuracy, and three (R05, R09, R13) describe a stale-data / cache-refresh failure mode — not a forecast model accuracy failure. The claim misreads its own evidence.

**Claim matches its evidence:** No — the evidence points to a cache/refresh failure on location change; the claim relocates the problem to forecast model accuracy, which no cited review supports.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** The trust complaints are driven by a stale-data bug — specifically, failure to refresh when GPS or location changes, and when the app resumes from a frozen state. R05, R09 and R13 all describe this failure mode in different words. R03 directly states the forecast itself is "hard to beat." The forecast model is not what users are complaining about.
- **What would overturn this finding:** Reviews or interviews in which users describe a forecast being wrong when the data is fresh and the location is correctly detected — i.e. a forecast quality complaint that isn't actually a data-freshness complaint. None of the four cited units show this.
- **Where the evidence underdetermines the claim:** The evidence doesn't underdetermine — it points the other way. The claim isn't thin, it's contradicted.

**Counter-evidence:** R03 directly contradicts the finding ("accurate, hyper-local forecasts that are hard to beat") and the synthesis doesn't address it. R05, R09 and R13 are described in the evidence annotations themselves as stale-data failures, not forecast model failures — the synthesis treats them as supporting a forecast-accuracy conclusion anyway.

**Unsupported claims:** The core claim — that forecast model accuracy is the problem — has no supporting evidence in the cited units. All four cited units either contradict it (R03) or point to a different mechanism (R05, R09, R13).

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | Not a claim about people's attitudes being validated — it's a product/causal claim. | n/a |
| CK-04 Product finding without a human story | CLEAR | The claim does cite people-side evidence (reviews R03, R05, R09, R13), even though it misreads them. CK-04 asks whether people-side evidence exists, not whether it was interpreted correctly — that's CK-05 and P-05. | n/a |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." The claim asserts forecast model accuracy is "the problem" with no hedging, when the cited evidence either contradicts it or describes a different mechanism entirely. | Evidence R03, R05, R09, R13 |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim is specific (forecast model accuracy, engineering investment) — the problem is that it's wrong, not that it's generic. |
| P-03 Transcript Literalism | No | Not applicable to review-based evidence of this kind. |
| P-04 Volume Mistaken for Strength | Yes | Confidence is being drawn from "13 reviews" as a block, when the four actually cited include one direct contradiction and three that describe a different failure mode. Single source type (App Store reviews) is also not corroborated by any independent angle (interviews, support tickets, analytics). |
| P-05 Counter-Evidence Filed, Not Faced | Yes | R03 directly contradicts the finding and the synthesis gives no argument for why it doesn't overturn the conclusion. The annotations on R05, R09, R13 flag them as stale-data failures and the synthesis proceeds as if that annotation weren't there. |
| P-08 Narrowing Sold as Resolving | Yes | The reasoning actually points to a narrower, different diagnosis (cache invalidation on location change / app resume), but the finding is sold as a causal fix at the forecast-model layer. This is the inverse of narrowing-sold-as-resolving: the evidence narrows toward cache, and the finding resolves toward forecast model instead. |

### Where does it apply?

**Scope:** iOS App Store reviewers, 2020–2026. The claim is stated without geographic or population qualification, but the sample is single-platform (iOS) and single-channel (App Store reviews). No transfer claim is being made explicitly, but the implicit scope ("the trust complaints") is wider than the evidence base.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No limits were declared. The study record says "(none declared)" for limits. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is being made. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "Forecast model accuracy is the problem behind the trust complaints" | No cited unit supports this; R03 contradicts it; R05, R09, R13 describe stale data | Inferred (incorrectly) | No — the inference doesn't follow from the cited observations |
| "Recommend investing engineering time in improving the forecast model" | Depends on the first claim | Inferred | No — follows from an unsupported inference |

**Checked against:** B-01 (belief register), no declared questions, no declared limits.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No questions were declared, so the check for whether the finding answers a declared question couldn't run. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research context was supplied to check against. |
| P-07 Trust Without Process | Yes | The finding is asserted as a conclusion without showing the reasoning that connects the cited evidence to the causal claim about forecast model accuracy. The reasoning, if reconstructed, would have to explain why R03's direct contradiction is dismissed and why the stale-data pattern in R05/R09/R13 points at the forecast model rather than at the data pipeline — and it doesn't. |

### Is it theirs or ours?

**Beliefs and evidence:** The finding closely mirrors B-01 ("Our forecast model is behind competitors in accuracy"), which is a high-confidence belief sourced from an executive's informal comparison — i.e. `authority`, not research — and which engineering disagrees with. The finding reads as a restatement of B-01 using reviews as a prop, rather than as a conclusion the reviews support. The reviews that would most naturally challenge B-01 (R03 praising accuracy; R05/R09/R13 locating the problem in data freshness, not model quality) are either ignored or recoded.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | FIRES | "This confidence comes from who said it, not from evidence." The finding restates B-01, which is a high-confidence belief with `source_type = authority` and no `source_ref`. The cited evidence does not support the belief — it points elsewhere (R05, R09, R13) or contradicts it (R03). The belief is also contested (`agreed_by_all = no`; engineering disagrees). | B-01 |

### Tacit-knowledge prompt
Not applicable — the evidence here is written reviews, not sessions anyone was in the room for. The ambiguity isn't tacit; it's visible on the page.

### Decision boundary
- **Supports:** Investigating the data-freshness / cache-invalidation pathway as the likely proximate cause of the trust complaints in this review sample. Specifically: refresh behaviour on GPS/location change (R05, R09) and on resume from a frozen state (R13).
- **Doesn't support:** A causal claim that forecast model accuracy is the problem, or that engineering investment in the forecast model will restore trust. R03 directly contradicts this; R05, R09 and R13 point at a different mechanism.
- **What would close the gap:** Analytics or support-ticket data showing whether complaints coincide with location changes or app resumes (confirming the cache hypothesis), plus — if the forecast-accuracy question is still live independently — a benchmarked accuracy comparison against competitors over the complaint window. The exec's informal comparison that produced B-01 is not sufficient.

**Safe to act on:** Not yet — the claim says more than its evidence, the cited evidence actively points at a different cause (cache/refresh on location change), and the finding appears to restate a contested authority-sourced belief (B-01) rather than something the reviews showed.

---

## Summary

This finding would send the engineering team to work on the wrong problem. The cited reviews do describe a real trust issue, but the mechanism they describe is stale cached data on location change and app resume — not forecast model accuracy. One of the four cited reviews (R03) explicitly says the forecast *is* accurate. The finding reads as a restatement of B-01, an executive belief that engineering already disputes, with reviews attached as apparent support.

The most useful next step isn't more research on forecast accuracy — it's checking whether the cache-invalidation pattern visible in R05, R09 and R13 holds up in analytics or support tickets. If it does, the engineering investment goes to the data pipeline, not the model.
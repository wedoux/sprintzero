## Finding: "Users will keep up their watering streaks for months once the feature ships."

**Evidence strength: WEAK**
This claim is not supported by the evidence available. A single in-session reaction from one of eight participants cannot support a prediction about multi-month behavioural persistence — the study was explicitly designed in a way that rules out this inference.

### Provenance

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| Users will keep up their watering streaks | INT-03: "Oh nice, a streak counter, I'd keep that going." | Inferred (and over-reached — participant stated intent, not behaviour) | Partially — one participant out of eight expressed positive reaction; no other evidence cited |
| …for months | None | Inferred with no evidence | No — study record explicitly states no longitudinal follow-up was conducted |
| …once the feature ships | None | Inferred — session was a test, not a shipped feature in real use | No |

The claim contains three distinct assertions (adoption, duration, post-launch behaviour). Only the first has even partial, single-participant support. The second and third have no evidence behind them at all.

### Falsification pass
- **Strongest counter-hypothesis:** Streak features show a well-known novelty-decay pattern — initial enthusiasm in a 15-minute session is a poor predictor of sustained engagement, and in plant care specifically, a broken streak after a vacation or busy week often causes users to abandon the feature entirely rather than restart. The INT-03 reaction is consistent with "this looks appealing right now" and tells us almost nothing about month-three behaviour.
- **What would overturn this finding:** Longitudinal data — e.g., a 2–3 month diary study, or analytics from a beta cohort tracking streak retention curves over 8–12 weeks. Without that, the claim is not testable from this evidence set.
- **Where the evidence underdetermines the claim:** Almost everywhere. The study record itself names the gap: "sessions were single 15-minute sittings, no longitudinal follow-up · cannot_claim: whether a behaviour persists past the session." The claim under review is doing exactly what the limits section says cannot be done.

### Pitfalls checked

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim is specific (behaviour, feature, duration) — the problem isn't vagueness, it's over-reach |
| P-02 Context Blindness | No | No prior research declared or ignored |
| P-03 Transcript Literalism | Yes | Taking "I'd keep that going" as a reliable predictor of actual months-long behaviour treats a session utterance as behavioural truth. Stated intent in a 15-minute test is one of the weakest signals in UX research for predicting sustained use. |
| P-04 Volume Mistaken for Strength | Yes | One participant out of eight is being used to support a universal claim ("users will"). Even if all eight had said this, it would still be single-source (in-session self-report) and still wouldn't support the duration claim. |
| P-05 Counter-Evidence Filed, Not Faced | Yes (structural variant) | The study's own `limits` section explicitly states the method cannot support claims about behavioural persistence past the session. The claim ignores that limit entirely rather than engaging with it. |
| P-06 Formulaic Transfer Hedge | No | No hedge is being made — the problem is the opposite, an unhedged over-claim |
| P-07 Trust Without Process | Yes | The claim is asserted with no visible reasoning connecting the single in-session utterance to the multi-month prediction. There's no argument, just a leap. |
| P-08 Narrowing Sold as Resolving | Yes | A piece of positive in-session feedback (narrow: "one person liked the look of it in a test") is being presented as resolving the actual product question (broad: "will this feature drive sustained engagement post-launch"). Those are different questions and this evidence only touches the first. |

### What would change this verdict
A longitudinal study — minimum 6–8 weeks, ideally 12 — tracking actual streak retention in a beta cohort, with attention to what happens after the first break. Short of that, even reframing the claim to something the evidence can support ("One of eight participants reacted positively to the streak concept in-session; sustained use is untested") would move this from an unsupportable prediction to a defensible observation.

### Tacit-knowledge prompt
Not applicable here — the problem isn't ambiguity in the session, it's that the study design was never capable of answering the question the claim is trying to answer. No amount of recalled session detail can bridge a 15-minute test to a months-long behavioural prediction. The right next step is a different study, not a closer re-read of this one.

---

**Note on the decision this informs:** The study record says this research is meant to inform "whether to add a watering-streak feature." That decision may still be reasonable to make — streak mechanics have a substantial evidence base in other domains — but it should not be made *on the basis of this study*. If the team ships the feature, they should ship it as a bet informed by external priors (and ideally instrumented to measure actual retention), not as a conclusion drawn from these eight sessions.
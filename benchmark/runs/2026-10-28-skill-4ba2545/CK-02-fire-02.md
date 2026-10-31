# UX Research QA Readout

Before I run the pass: this synthesis has serious issues on nearly every dimension, and the claim should not be acted on. Full readout below.

A note on method: I'm running this QA pass in the same conversation where the synthesis was presented. For a one-claim gut-check this is fine, but for anything high-stakes, re-run in a fresh conversation with the synthesis and raw evidence pasted in cleanly.

---

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | Declared | "whether a behaviour persists past the session" | CK-02 |

---

## Finding: "Users will keep up their watering streaks for months once the feature ships."

**Evidence strength:** WEAK
A single enthusiastic reaction from one participant in a 15-minute session, extrapolated to multi-month behaviour across all users. This is as thin as evidence gets.

**Claim matches its evidence:** No — the claim crosses the study's declared limit, inflates one person's reaction into universal future behaviour, and uses "will" where even "might" would be a stretch.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** INT-03 was reacting to novelty in a 15-minute test. Streak features notoriously decay — people miss one day, break the streak, feel bad, and disengage. The reaction "I'd keep that going" is a stated intention in the moment, not evidence of sustained behaviour.
- **What would overturn this finding:** Longitudinal data — even four weeks of actual usage logs from a prototype — showing streak retention curves. Or evidence from comparable streak features (language apps, fitness apps) showing drop-off rates.
- **Where the evidence underdetermines the claim:** Completely. One sentence from one participant in one session cannot speak to multi-month behaviour, cannot speak to the other seven participants, and cannot distinguish stated intention from actual behaviour.

**Counter-evidence:** None cited in the material. The other seven sessions (INT-01, INT-02, INT-04 through INT-08) are not quoted at all — their silence is itself a gap the claim doesn't acknowledge.

**Unsupported claims:** The entire claim. "Users" (plural, general) is not supported — only INT-03 is cited. "Months" is not supported — the sessions were 15 minutes. "Keep up" (sustained behaviour) is not supported — only a stated intention was captured.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim is a prediction, not a judgment about participants being validated | n/a |
| CK-04 Product finding without a human story | CLEAR | The claim is about people (users' future behaviour), not a product recommendation; CK-04 doesn't apply | n/a |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." One participant ("INT-03: 'I'd keep that going'") becomes "Users will keep up their watering streaks for months." Scope: 1 → all users. Certainty: a hypothetical reaction → "will." Duration: 15 minutes → months. | The evidence itself |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim is specific enough (streaks, watering, months), even though it's wrong |
| P-03 Transcript Literalism | Yes | INT-03's "I'd keep that going" is treated as a reliable predictor of multi-month behaviour. A stated intention in a 15-minute session is exactly the kind of signal that needs a researcher's judgment about tone, context, and whether the participant was reacting to novelty — none of which is captured |
| P-04 Volume Mistaken for Strength | Yes (inverted) | Not multiple units of one source type — a single unit treated as sufficient. Same underlying failure: one signal, treated as strong |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence is cited; the problem is that none was looked for |
| P-08 Narrowing Sold as Resolving | Yes | A reaction to a mockup ("I'd keep that going") is sold as resolving the behavioural question of whether people will sustain the streak. At best it narrows the question to "worth prototyping"; it does not resolve "will persist for months" |

### Where does it apply?

**Scope:** The evidence covers one participant, in one 15-minute unmoderated session, reacting to a streak counter in the moment. The claim covers all users, over multi-month timeframes, after the feature ships. The gap is enormous.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | FIRES | "This claims more than the study was designed to show." The study record explicitly states: `cannot_claim: whether a behaviour persists past the session`. The claim is precisely about behaviour persisting past the session — for months | The declared limit on method |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer hedge is attempted; the claim just overreaches without even a token caveat |

### Could someone retrace it?

**Provenance**

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "Users will keep up their watering streaks" | INT-03: "Oh nice, a streak counter, I'd keep that going." | Inferred (heavily) | Partially — the source exists, but the inference from one in-session reaction to sustained behaviour across all users is not supportable |
| "for months" | No evidence cited | Inferred with no basis | No — nothing in a 15-minute session can speak to months |
| "once the feature ships" | No evidence cited | Inferred | No — reactions to a test stimulus are not evidence about post-launch behaviour |

**Checked against:** The one declared limit (method / session duration). No questions were declared, so CK-06 cannot run.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | Study record declares no questions. Cannot check whether the claim answers a question that was asked | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research is referenced; cannot assess whether something was missed. Worth noting that streak-feature retention is a well-studied area (habit apps, Duolingo, fitness trackers) — a careful synthesis would reference what's known about streak decay |
| P-07 Trust Without Process | Yes | The claim is asserted with no reasoning chain between "INT-03 said this" and "users will do this for months." The leap is enormous and not argued |

### Is it theirs or ours?

**Beliefs and evidence:** Impossible to tell. With no belief register declared, I cannot check whether this claim is a pre-existing team conviction ("we think streaks will work") being retrofitted onto one supportive quote, or a genuine conclusion from the evidence. The fact that one supportive quote is treated as sufficient — with no apparent attempt to look for disconfirming signals in the other seven sessions — is consistent with borrowed conviction, but I can't prove it without the register.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | No belief register declared. Part (a) cannot run. Part (b) does not fire — the claim doesn't cite "the PM said" or "stakeholders agreed," it cites INT-03 | — |

### Tacit-knowledge prompt
If a researcher ran these sessions: in INT-03's "Oh nice, a streak counter, I'd keep that going" — was there a tone or qualifier (hedged, enthusiastic, polite, performative) that would help distinguish genuine intent from a test-session courtesy response? And what did the other seven participants say or do when the streak counter appeared — was it ignored, noticed, questioned?

### Decision boundary

- **Supports:** At least one participant in a short test reacted positively to the idea of a streak counter. That is worth knowing.
- **Doesn't support:** Anything about sustained behaviour, about the other seven participants, about months, or about post-launch usage.
- **What would close the gap:** A four-to-eight-week prototype test with usage logs showing actual streak retention — not reactions, behaviour. Secondarily, published data on streak-feature retention curves from comparable products.

**Safe to act on:** Not yet — the claim violates the study's own declared limit (`cannot_claim: whether a behaviour persists past the session`) and extrapolates one participant's in-session reaction to all users over months. One supportive quote is a reason to prototype, not a reason to ship.

---

## Summary

Two checks fire (CK-02, CK-05), one is not run for missing input (CK-01, CK-06), and four pitfalls trigger (P-03, P-04, P-07, P-08). The claim should be rewritten as something like: "INT-03 reacted positively to the streak concept; worth prototyping and testing retention over several weeks before committing to the feature." That version would be WEAK but honest, and safe to act on as a next-step recommendation.
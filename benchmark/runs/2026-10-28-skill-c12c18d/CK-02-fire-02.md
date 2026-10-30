# QA Readout

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | Declared | "whether a behaviour persists past the session" | CK-02 |

---

## Finding: "Users will keep up their watering streaks for months once the feature ships."

**Evidence strength:** WEAK
One in-session comment from one participant reacting to the idea of a streak counter is not a basis for a claim about months of future behaviour.

**Claim matches its evidence:** No — the evidence is a single reaction in a 15-minute session; the claim is about sustained behaviour across months for all users.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** INT-03 is expressing in-the-moment appeal of a game-like mechanic, not committed future behaviour. Novelty reactions in short unmoderated sessions routinely overpredict real-world retention; streak mechanics in particular are known to fail when a user misses a day and loses motivation to restart.
- **What would overturn this finding:** A longitudinal study (even 4–8 weeks) showing streak dropoff curves, or analytics from a prototype/soft launch showing most users abandoning streaks within weeks.
- **Where the evidence underdetermines the claim:** The evidence base says nothing at all about persistence. One quote from one participant in one sitting cannot speak to months of behaviour under any interpretation.

**Counter-evidence:** None was engaged with. The other 7 sessions aren't cited — their silence on streaks isn't addressed either way.

**Unsupported claims:** The entire claim about month-long persistence is unsupported. INT-03 supports, at most, "one participant reacted positively to the idea of a streak counter during a 15-minute session."

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | Not a claim being presented as validated/proven — it's a forward prediction. The pitfall is overreach, not false validation. | n/a |
| CK-04 Product finding without a human story | CLEAR | The claim does cite people-side evidence (INT-03), thin as it is. The problem is scope, not absence. | n/a |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." One participant's in-session reaction ("I'd keep that going") becomes "Users will keep up their watering streaks for months." Scope inflated from 1 to all; certainty inflated from a hypothetical reaction to "will"; timeframe invented. | n/a (no belief or question to conflict with — conflicts with the evidence itself) |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim is specific (streaks, months) — the problem is overreach, not vagueness. |
| P-03 Transcript Literalism | Yes | The claim takes "I'd keep that going" at face value as a predictor of months of behaviour, with no acknowledgment that an in-session reaction to a prompt is a weak signal for sustained use. |
| P-04 Volume Mistaken for Strength | No (adjacent) | Only one unit is cited, so volume isn't inflated — but a single quote is being asked to carry a very large claim. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence was filed; the other 7 sessions aren't mentioned at all. |
| P-08 Narrowing Sold as Resolving | Yes | A single positive reaction (narrow signal) is being sold as resolving the question of long-term retention. The evidence narrows "might this appeal to anyone?" to "yes, to at least one person" — it does not resolve "will it sustain behaviour."|

### Where does it apply?

**Scope:** The evidence covers one participant's reaction during one 15-minute unmoderated session. The claim applies to all users across months. These do not overlap.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | FIRES | "This claims more than the study was designed to show." The study explicitly declared it cannot claim "whether a behaviour persists past the session." The claim is precisely about persistence past the session — for months. | Declared limit: method · "cannot claim: whether a behaviour persists past the session" |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim or hedge is being made. |

### Could someone retrace it?

**Provenance**

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| Users will keep up watering streaks | INT-03 quote | Inferred (with a very large leap) | Partially — the quote exists, but the inference from it to the claim is not traceable |
| For months | None | Inferred | No — nothing in the evidence speaks to months |
| Once the feature ships | None | Inferred | No — nothing in the evidence speaks to post-launch behaviour |

The "months" and "all users" parts of the claim have no supporting evidence at all.

**Checked against:** The declared method limit. No questions or beliefs were declared, so CK-01 part (a) and CK-06 could not run.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No questions were declared, so the claim cannot be checked against them. Note: without declared questions it is also impossible to know whether this finding is answering what the team set out to learn or has drifted off. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research referenced; nothing to check against. |
| P-07 Trust Without Process | Yes | The claim is stated as a confident forward prediction with no reasoning shown for how one in-session reaction leads to a months-long behavioural claim. Nothing is derived — it is asserted. |

### Is it theirs or ours?

**Beliefs and evidence:** One participant's reaction is doing all the work. The leap from "I'd keep that going" to "users will keep up streaks for months" has no stated source — it isn't attributed to a belief, a prior study, or further evidence. The absence of a declared belief register means we can't tell whether this reflects a pre-existing team conviction about streak mechanics, but the inferential gap is the size of one.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | Part (b) does not fire — no attributed opinion ("the PM says", "stakeholders agree") is cited. Part (a) cannot run because no belief register was declared. If an undeclared team belief about streak mechanics is actually driving the "months" claim, this check would likely have fired on it. | n/a |

### Tacit-knowledge prompt
Was INT-03 the only participant who reacted to a streak-like concept, or did the topic simply not come up in the other 7 sessions? That distinction matters: one is a weak positive, the other is no signal at all.

### Decision boundary
- **Supports:** At least one participant reacted positively, in the moment, to the idea of a streak counter.
- **Doesn't support:** Anything about whether users will actually sustain streaks, for how long, at what rate, or what happens when they break one. Also doesn't support anything about users other than INT-03.
- **What would close the gap:** A longitudinal study — even 4 weeks of real use with a prototype — showing streak-maintenance and dropoff behaviour. The current method, declared up front, cannot answer the question the claim is trying to answer.

**Safe to act on:** Not yet — the claim directly violates the study's own declared method limit, inflates one participant's in-session reaction into a months-long behavioural prediction for all users, and offers no reasoning for the leap. Ship the feature based on this and the team is betting a quarter of work on INT-03's enthusiasm.
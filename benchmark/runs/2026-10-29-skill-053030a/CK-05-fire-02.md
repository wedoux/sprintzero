Before I run the pass: this synthesis looks like it was likely produced in a conversation with an AI assistant. If so, **please run this QA in a fresh conversation** rather than the one that generated it — a model reviewing its own prior reasoning is grading its own homework. If you've already done that, or wrote the claim yourself, carry on.

I also want to flag what's missing before I start, so you can decide whether to proceed as-is:

- **No belief register.** I can't check whether this claim restates something you already believed (CK-01 part a), or whether a team-agreed assumption stands behind it (CK-04 fallback).
- **No study record.** I can't check whether the claim stays inside the study's limits (CK-02), or whether it answers a question you actually asked (CK-06).
- **One evidence unit.** A single quote from one participant.

If you want these checks to actually run, you'd need to write a belief register ([templates/belief-register.md](templates/belief-register.md)) and a study record ([templates/study-record.md](templates/study-record.md)). I won't draft them — beliefs and questions are only useful when written by the people who hold them. Happy to ask questions that help you get started.

Proceeding with what I have.

---

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "This new icon will increase engagement."

**Evidence strength:** WEAK
One participant said one icon was clearer than another. That is a usability observation on a single person; it is not evidence about engagement, and it is not evidence about what will happen.

**Claim matches its evidence:** No — the claim makes a causal, future-tense prediction about a behavioural metric ("will increase engagement") from a single comprehension comment ("I spotted it right away"). Spotting an icon is not engaging with a product.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** INT-01 noticed the icon in a session because they were paying attention to the interface — that's what sessions do. In normal use, noticing an icon faster may not change whether or how often they use the feature it points to. Clarity and engagement are different things.
- **What would overturn this finding:** A/B data showing no lift (or a drop) in the engagement metric after the icon ships; or more session evidence where participants spot the icon easily but still don't act on it.
- **Where the evidence underdetermines the claim:** Severely. One quote from one person about icon clarity cannot tell you anything about an engagement outcome across a user base.

**Counter-evidence:** None in the evidence set — but that's because the evidence set is one quote. Absence of counter-evidence here isn't support.

**Unsupported claims:** The entire predictive claim ("will increase engagement") is unsupported. The evidence supports, at most: "INT-01 found the new icon clearer than [whatever they're comparing to]."

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim is about the product (icon → engagement), not a validated claim about people. | n/a |
| CK-04 Product finding without a human story | NOT RUN | No belief register declared, so I can't check whether an agreed working assumption stands behind this. There is one piece of people-side evidence (INT-01's comment on clarity), but it doesn't speak to engagement — the thing the claim is actually about. Worth flagging even though the check can't formally fire. | — |
| CK-05 Scope and certainty inflation | FIRES | This says more, and says it more surely, than the evidence allows: one participant's clarity comment becomes a causal prediction ("will increase") about an engagement metric across users. Three jumps in one sentence — one person → all users, clarity → engagement, past observation → future prediction. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "Increase engagement" is a label, not a behaviour. No named action, no trigger, no consequence. The sentence would read identically in a report about any other product or feature. |
| P-03 Transcript Literalism | No | — |
| P-04 Volume Mistaken for Strength | Yes (adjacent) | Only one source and one unit, but presented with the confidence of a settled finding. The pitfall is usually about counting repetitions as corroboration; here it's a degenerate case — n=1 presented as sufficient. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence present to file or face. |
| P-08 Narrowing Sold as Resolving | Yes | A clarity observation (narrow, specific) is presented as resolving an engagement question (broad, causal). The verb "will increase" asserts a fix, not an investigation. |

### Where does it apply?

**Scope:** The evidence covers one participant in one session noticing one icon. The claim covers an unspecified user base, an unspecified timeframe, and a different outcome (engagement) than what was observed (clarity).

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared. Flagging regardless: the claim almost certainly exceeds whatever limits a one-participant usability check would carry. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim made (and no hedge offered — the problem here is the opposite, unhedged overreach). |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| The icon is clearer | INT-01: "Oh, that's a much clearer icon, I spotted it right away." | Observed (self-report) | Yes |
| The icon will increase engagement | not cited | Inferred — with no visible chain from "clearer" to "more engagement" | No |

**Checked against:** Nothing declared. No beliefs, questions or limits to retrace against.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No declared questions. I can't tell whether this answers one you asked, or drifts from the study's purpose. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No (undetectable) | Can't tell without knowing prior research. |
| P-07 Trust Without Process | Yes | No reasoning is shown for why "clearer icon" leads to "increased engagement." The causal step is asserted, not derived. |

### Is it theirs or ours?

**Beliefs and evidence:** The clarity observation comes from INT-01. The engagement claim comes from somewhere else — not from INT-01, who said nothing about engagement. Without a declared belief register, I can't tell whether "icons drive engagement" is a prior conviction someone brought to the study, but the claim behaves like one: it's stronger than the evidence, and the evidence isn't about the thing being claimed.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN (part a) / Likely FIRES (part b, informally) | No belief register, so I can't formally run part (a). But the gap between what INT-01 said and what the claim asserts suggests the engagement prediction comes from somewhere other than evidence — someone's prior view that clearer icons drive engagement. Worth asking: whose belief is "will increase engagement"? | — |

### Tacit-knowledge prompt
Who first said this icon would "increase engagement," and what were they comparing it to? If that framing was in the room before INT-01 spoke, the quote may have been read as confirming something that was never actually tested.

### Decision boundary
- **Supports:** INT-01 found the new icon clearer than its comparator and spotted it quickly in a session.
- **Doesn't support:** Any claim about engagement, any claim about users beyond INT-01, any prediction about what the icon will do when shipped.
- **What would close the gap:** An A/B test measuring the actual engagement metric you care about, with the icon as the intervention. Session data alone — even many sessions — can tell you about comprehension and discoverability, not about whether a behaviour change persists in normal use.

**Safe to act on:** Not yet — the claim is a causal prediction about engagement based on one person's comment about icon clarity. Three separate jumps, none of them evidenced. Ship the icon if other reasons warrant it, but don't treat it as a validated engagement improvement, and don't let this stand in for a measurement after launch.
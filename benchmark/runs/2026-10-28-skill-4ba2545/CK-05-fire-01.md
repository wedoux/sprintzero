I'll run this QA pass now. First, a note on process:

**On the missing declarations:** The material doesn't include a belief register or study record. Before I continue, you should know what that costs you — several checks won't be able to run, and the readout will show "NOT RUN" for them, not "passed." If you have beliefs or study questions written down anywhere, now is the time to add them. If you don't, you can write your own using `templates/belief-register.md` and `templates/study-record.md` — they're meant to be filled in by the people who hold the beliefs and asked the questions, which is why I can't draft them for you.

I'll proceed with the QA pass on what you've given me. Here's the readout.

---

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "Users want a subscription model."

**Evidence strength:** WEAK
Three interviewees expressed openness to subscription pricing in a sample of unknown size, with no counter-evidence sought and no information about how the question was framed.

**Claim matches its evidence:** No — "Users" generalises from 3 named interviewees to the whole user base, and "want" overstates what the quotes actually show (two of three frame it as acceptance or preference-over-alternatives, not active desire).

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** These three participants are expressing *tolerance* of subscriptions as a lesser evil (vs. ads in INT-01, vs. in-app purchases in INT-03), not active desire for one. A different framing — "would you prefer subscription or a one-time purchase?" — might produce entirely different answers from the same people.
- **What would overturn this finding:** Evidence of willingness to pay at a specific price point; evidence from participants who were asked an open "how would you prefer to pay?" question rather than a leading one; any participant expressing resistance to subscriptions.
- **Where the evidence underdetermines the claim:** We don't know the sample size, how participants were selected, what question prompted these answers, or whether anyone said the opposite. Three supporting quotes with no denominator and no counter-signal is a very thin base.

**Counter-evidence:** None cited in the material — which is itself a problem. A synthesis that found zero dissent across its sample should say so explicitly and explain why; silence here more likely means counter-evidence wasn't surfaced.

**Unsupported claims:** The scope ("Users" as a population) has no evidence. The verb ("want") is stronger than any of the three quotes supports.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim is about preference, not framed as "validated" or "proven" — though it would fire if restated as "we validated that users want subscriptions" | n/a |
| CK-04 Product finding without a human story | CLEAR | The claim is about people (what they want), and it does cite people-side evidence (three interviews). Weakness is in CK-05 territory, not CK-04 | n/a |
| CK-05 Scope and certainty inflation | **FIRES** | "This says more, or says it more surely, than the evidence allows." Triggering text: "Users want a subscription model." Three interviewees become "Users"; INT-01's conditional ("I'd pay... if it meant no ads") and INT-03's comparison ("rather subscribe than deal with IAP") become unqualified "want" | n/a (no declared limit to point to; the issue is the evidence itself) |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "Users want a subscription model" is a label with no trigger and no consequence. What triggers the want? At what price? For which product? Swap "subscription" for any pricing model and the sentence structure is unchanged |
| P-03 Transcript Literalism | Yes | INT-01 is conditional ("if it meant no ads"), INT-03 is comparative ("rather than IAP") — tone and framing matter here and the synthesis flattens all three into unqualified agreement. A researcher who ran these sessions might know whether these were volunteered or prompted |
| P-04 Volume Mistaken for Strength | Yes | All three evidence units are the same source type (interviews), likely the same study. Three interview quotes is one source type, not three independent corroborations |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence appears in the material. The *absence* of any counter-signal across the whole evidence set is itself suspicious, but P-05 is about filed-then-ignored evidence specifically |
| P-08 Narrowing Sold as Resolving | No | No causal "this lets us fix X" claim is being made |

### Where does it apply?

**Scope:** The evidence covers three interviewees whose selection, demographics, product context, and interview framing are all unknown. The claim covers "users" without boundary.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no `cannot_claim` to check against. If limits were declared, this would almost certainly fire | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No cross-population transfer claim is being made |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "Users want a subscription model" (the generalisation to all users) | not cited | Inferred | No — the leap from 3 interviewees to "users" has no supporting evidence |
| Three interviewees expressed openness to subscription pricing | INT-01, INT-02, INT-03 quotes | Observed | Yes |
| The *reasons* behind the preference (ad avoidance for INT-01, familiarity for INT-02, IAP avoidance for INT-03) | the quotes themselves | Observed | Yes — and these reasons differ, which the finding conceals |

**Checked against:** nothing declared

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No declared questions to check against. Can't tell whether this finding answers a question the team asked or wandered off from one | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research is referenced either way; can't assess without visibility into what the team already knew |
| P-07 Trust Without Process | Yes | The claim is stated as a conclusion with no reasoning about *why* three quotes support the generalisation to "users", or how the three different framings (anti-ad, pro-familiarity, anti-IAP) were treated as the same signal |

### Is it theirs or ours?

**Beliefs and evidence:** The claim is sourced to three participant quotes. Without a belief register, I can't tell whether the generalisation to "users want" reflects a pre-existing team belief that found three confirming quotes, or an interpretation drawn fresh from the evidence. This matters: if someone on the team already believed users wanted subscriptions, three supporting quotes from a convenience sample is exactly what confirmation looks like.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | No belief register declared, so part (a) cannot run. Part (b) does not fire — no attributed opinions ("the PM says...") appear in the claim's support. But the possibility that this finding is a pre-held belief with three confirming quotes attached cannot be ruled out | n/a |

### Tacit-knowledge prompt (optional)
If a researcher who ran these sessions is available: **What question or prompt preceded these three answers?** INT-01 answers as if asked about ads, INT-03 as if asked about in-app purchases, INT-02 as if asked about subscriptions in general. Were these three different conversations, or were participants steered toward subscriptions as the stated alternative to something else?

### Decision boundary
- **Supports:** Three interviewees, when prompted in ways we can't see, expressed non-resistance to subscription pricing, each for different reasons (ad avoidance, familiarity, IAP avoidance).
- **Doesn't support:** Any claim about what "users" in general want. Any claim about willingness to pay a specific price. Any claim that subscription is preferred over a one-time purchase (not tested). Any claim that these three represent a majority or a trend.
- **What would close the gap:** A larger sample asked an open "how would you prefer to pay for this product?" question — not framed against ads or IAP — with the full distribution of answers reported, including dissent.

**Safe to act on:** Not yet — the claim generalises three interviewees' qualified, differently-motivated acceptances into an unqualified universal preference, and the checks that would catch borrowed conviction, drift, and scope violations couldn't run because nothing was declared upstream.

---

**Summary of what hurt this QA pass:** Three checks reported NOT RUN (CK-01 part a, CK-02, CK-06) because no belief register or study record was declared. The claim fails even without them — CK-05 fires on evidence alone, and three pitfalls trigger — but if you want to know whether this finding also *drifted from a question you asked*, or *restates a belief someone already held*, you'd need to write those records and re-run the pass.
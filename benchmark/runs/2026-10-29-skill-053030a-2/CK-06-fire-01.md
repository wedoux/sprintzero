# UX Research QA Readout

```
QA Progress:
- [x] Step 0: Gather declarations
- [x] Step 1: Confirm there's a conclusion to evaluate
- [x] Step 2: Provenance pass
- [x] Step 3: Falsification pass
- [x] Step 4: Pitfalls check
- [x] Step 5: CK pass
- [x] Step 6: Produce the readout
```

A note before the readout: no belief register was declared, and the study record has no limits. That's your call to make, but it means several checks will report NOT RUN rather than CLEAR — the skill never reports a check as passed when it couldn't run. If you want fuller coverage, see `templates/belief-register.md` and the `limits` section of `templates/study-record.md`.

---

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | Declared | Q-01 | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "Users think the price is too high."

**Evidence strength:** WEAK
One participant out of seven made one offhand remark about price. That is a signal worth noting, not a finding about users.

**Claim matches its evidence:** No — one participant's comment is restated as what "users" think, and a passing remark is restated as a settled view.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** INT-03's comment was a conversational aside during an onboarding comprehension session, not a considered judgment about value. The other six participants said nothing about price — which, in a study not asking about price, is roughly what you'd expect either way. The remark may say more about INT-03's framing in the moment than about a pattern.
- **What would overturn this finding:** Direct evidence from the other six participants that price did not feel steep to them; or a willingness-to-pay study; or churn/conversion data at the $12 price point.
- **Where the evidence underdetermines the claim:** Almost entirely. One remark from one participant cannot support a claim about "users" as a group, and the study wasn't designed to probe price at all.

**Counter-evidence:** None cited in the material — but the absence of price comments from six of seven participants is itself relevant context the claim ignores.

**Unsupported claims:** The generalisation from "INT-03 said this" to "users think this" has no evidence behind it. The characterisation of a passing remark as a settled belief ("think") also goes beyond what the quote shows ("feels steep").

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim is stated as a view users hold, not as validated or proven. | n/a |
| CK-04 Product finding without a human story | CLEAR | Not a product claim — this is a claim about what people think. | n/a |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." One participant ("$12 a month feels steep for what this does") becomes "users"; a hedged "feels steep" becomes "think … is too high." | Evidence (INT-03 only; 1 of 7) |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "Users think the price is too high" is the kind of sentence that could appear in a report about almost any product. No behaviour, no trigger, no consequence. |
| P-03 Transcript Literalism | No | The claim doesn't over-trust the transcript so much as overreach from it. |
| P-04 Volume Mistaken for Strength | No | Only one unit is cited — the problem isn't inflated volume, it's generalisation from a single data point. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence was named at all; the issue is that silence from six other participants wasn't addressed. |
| P-08 Narrowing Sold as Resolving | No | No causal or investigative claim is being made. |

### Where does it apply?

**Scope:** The evidence covers one participant in a moderated onboarding session. The claim covers "users" with no qualifier. No limits were declared, so there is no explicit boundary to check against — but the gap between "INT-03" and "users" is visible without one.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No limits were declared in the study record, so there's no `cannot_claim` to check against. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is being made. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| Price is too high | INT-03: "$12 a month feels steep for what this does." | Inferred (from one participant) | Yes, to one unit |
| "Users" (as a group) hold this view | not cited | Inferred | No — nothing in the evidence supports the generalisation |
| "Think" (as a settled view, not a passing feeling) | not cited | Inferred | No — the quote says "feels," not "think" |

**Checked against:** Q-01 ("Do new users understand what the app does after onboarding?").

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | FIRES | "This insight doesn't answer any question the team asked." The claim is about price; Q-01 is about comprehension of what the app does. It isn't labelled as an unexpected finding. | Q-01 |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research is being referenced or missed, as far as the material shows. |
| P-07 Trust Without Process | Yes | The claim is stated as a conclusion with no reasoning: no mention of how many participants raised it, in what context, or why one remark is being read as a group view. |

### Is it theirs or ours?

**Beliefs and evidence:** The claim rests on one participant's remark. No belief register was declared, so it's not possible to check whether this finding restates something the team already believed. Worth noting: when a one-off quote gets elevated to a finding about "users," it often means the quote confirmed something someone already thought — but with no register, that's a question, not a check.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | No belief register was declared, so part (a) can't run. Part (b) didn't fire — no attributed opinion is cited as support. | — |

### Tacit-knowledge prompt (optional — ask only if a researcher who ran the sessions is available)
In INT-03, what was happening in the conversation when the price comment came up? Was it a response to a question, a volunteered aside, something said while wrapping up? And did any of the other six participants touch on price or value at all — even briefly — in a way that didn't make it into the evidence extract?

### Decision boundary
- **Supports:** One participant in an onboarding study made a passing remark that $12/month feels steep for the value they perceived. That is worth logging as a question to pursue, especially given that the study wasn't asking about price.
- **Doesn't support:** Any claim about what "users" think about price, or that the price is "too high" as a settled fact. The study wasn't designed to answer this, and six of seven participants didn't speak to it.
- **What would close the gap:** A study that actually asks about price perception — either a willingness-to-pay probe in follow-up interviews, or quantitative data on conversion and churn at $12. If the question is really "should we rewrite onboarding?" (per the declared decision), then the right next step may be to set this price signal aside and keep the study focused on comprehension.

**Safe to act on:** Not yet — one participant's offhand remark is being restated as what "users" think, and it answers a question the study didn't ask. Treat it as an unexpected signal worth a separate study, not a finding.
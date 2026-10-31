# QA Readout

Before I run this: I don't have visibility into whether this synthesis was produced earlier in this same conversation. If it was, you'll get a stronger pass by running this QA in a fresh conversation with only the material above pasted in — a model reviewing reasoning it just produced is grading its own homework. Proceeding regardless, since you've asked.

One note on the inputs: the study record is marked "none declared", so CK-02 and CK-06 will report NOT RUN. The belief register is declared but has only one belief, which the claim leans on directly.

---

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | Declared | B-01 | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

---

## Finding: "Our founder has always said dark mode matters, and INT-01 and INT-03 both show users actively seeking it out — we should ship it as the default theme."

**Evidence strength:** WEAK
Two participants mentioning a feature preference is a thin base for a theme, and an even thinner one for a default-theme decision affecting every user.

**Claim matches its evidence:** No — the claim makes three jumps the evidence doesn't support: from "matters to some users" to "matters to our users" generally; from "users want it available" to "users want it as the default"; and the founder's conviction is cited as if it were corroborating evidence rather than the original belief being tested.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** INT-01 and INT-03 show two users want dark mode *available* (a toggle, an option) — not that they want it *as the default*. INT-01 explicitly describes switching to it in the evening, which implies a light default the rest of the day. INT-03 looks for a toggle on install, which also implies the ability to choose, not an imposed default.
- **What would overturn this finding:** Usage data showing most users don't enable dark mode when offered it; or interviews with users who dislike or struggle with dark mode as a default (e.g. in bright environments, or for readability reasons).
- **Where the evidence underdetermines the claim:** Two participants out of an unknown sample tells us almost nothing about prevalence. We also have no evidence at all about *default* preference versus *availability* preference — the two pieces of evidence we do have actively point toward the latter.

**Counter-evidence:** None presented in the material, which is itself worth flagging — a synthesis built on two supporting quotes with no attempt to find or address disconfirming signal is a thin basis for a default-theme decision.

**Unsupported claims:** "we should ship it as the default theme" has no evidence behind it. Neither quote speaks to defaults. The design lead's dissent note ("wants usage data before treating it as settled") is also unaddressed.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim is primarily a product recommendation, not a claim about people being proven to feel something. | n/a |
| CK-04 Product finding without a human story | CLEAR | The product recommendation does cite people-side evidence (INT-01, INT-03), even if that evidence is thin and doesn't support the specific claim. | n/a |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." Two participants become "our users"; wanting the feature available becomes wanting it as the default. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim is specific (ship dark mode as default), not a generic label. |
| P-03 Transcript Literalism | Yes | The two quotes are read as endorsing a default. INT-01's "I switch to dark mode every evening" structurally implies a non-dark default the rest of the day — the synthesis misses this because it reads the quote for sentiment, not for what the behaviour implies. |
| P-04 Volume Mistaken for Strength | Yes | Two interview quotes from the same source type (user interviews), with no corroboration from analytics, reviews, or any other channel. The claim's confidence should be heavily discounted. |
| P-05 Counter-Evidence Filed, Not Faced | No (adjacent) | No counter-evidence is listed, so technically this doesn't fire — but the design lead's dissent in the belief register is a known counter-position that the synthesis doesn't acknowledge. Worth flagging. |
| P-08 Narrowing Sold as Resolving | No | Not a narrowing-to-fix claim. |

### Where does it apply?

**Scope:** We know nothing about the sample — who INT-01 and INT-03 are, when they were interviewed, on what platform, in what context. The claim is universal ("our users"), the evidence is two anonymous data points.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record was declared, so there are no `cannot_claim` statements to check the scope against. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is being made. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| Users actively seek out dark mode | INT-01, INT-03 quotes | Observed (for these two) | Yes |
| Dark mode matters to "our users" (generally) | Not cited | Inferred from two quotes + founder's belief | No — generalisation unsupported |
| We should ship it as the default theme | Not cited | Inferred, but the inference isn't shown | No — no evidence addresses defaults |
| "Our founder has always said dark mode matters" | B-01 | This is the founder's opinion, not evidence of user behaviour | Traceable to B-01, but B-01 is a belief, not evidence |

**Checked against:** The belief register (B-01). No study record, so no declared questions or limits to check against.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study questions were declared, so there's nothing to check drift against. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | Not evaluable | No prior-research context was supplied; can't tell whether this contradicts or confirms earlier work. |
| P-07 Trust Without Process | Yes | The jump from "two users mention it" + "founder believes it" to "ship as default" is asserted, not argued. The reasoning chain is missing: why default rather than opt-in? Why these two interviews as representative? The verdict is stated as if it followed from the evidence; it doesn't. |

### Is it theirs or ours?

**Beliefs and evidence:** The claim explicitly fuses the founder's long-standing belief (B-01) with two participant quotes, and treats the combination as a single reinforcing signal. But B-01 is exactly what the research should be testing, not supporting evidence that gets to join the vote. The design lead's recorded dissent — "wants usage data before treating it as settled" — tells you the team itself didn't agree this was settled before the study. The study hasn't settled it either.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | FIRES | "This confidence comes from who said it, not from evidence." The claim opens with "Our founder has always said dark mode matters" and uses that as part of its warrant. B-01 is rated `high` confidence with source_type `authority` and no supporting research. The two interview quotes are then layered on top, but they don't independently establish the scope ("our users") or the specific recommendation (default theme) — the founder's authority is doing the real work. | B-01 |

### Tacit-knowledge prompt
Were INT-01 and INT-03 asked anything about *defaults* specifically — about what theme they'd want the app to open in on first install, or whether they'd be happy to have dark mode imposed in daylight? The quotes as written describe toggling and seeking the option, not accepting it as the default; a researcher who ran the sessions might know whether the default question was asked and simply didn't make the excerpts, or whether it wasn't asked at all.

### Decision boundary
- **Supports:** At least two users value dark mode enough to seek it out or switch into it. That's a reason to make it available.
- **Doesn't support:** That dark mode matters to users generally; that it should be the default; that the founder's long-held conviction has been corroborated by this study.
- **What would close the gap:** Usage data from an app that already offers both themes — what proportion of users enable dark mode, and when. That one piece of evidence would tell you whether to prioritise the feature at all, and separately whether default-dark is sensible for your user base. The design lead has already asked for exactly this.

**Safe to act on:** Not yet — the claim says more than its evidence (scope: two users → "our users"; recommendation: availability → default), and the founder's authority is being used as evidence rather than as the hypothesis being tested. CK-01 and CK-05 both fire; CK-02 and CK-06 couldn't run because no study record was declared.

---

## One meta-observation

The belief register did its job here: because B-01 was declared with `source_type: authority` and the design lead's dissent was recorded, CK-01 could fire cleanly and the unresolved internal disagreement was visible. If you'd like a stronger pass next time, a study record — even a minimal one naming the question this research was supposed to answer and what the sample couldn't cover — would let CK-02 and CK-06 run too. Those are both likely to have more to say about a claim like this one.
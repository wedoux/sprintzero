# UX Research QA Readout

Before I run the pass: I'm proceeding without a study record, which you've chosen not to declare. That's your call, but it means CK-02 (limits) and CK-06 (questions) can't run. I'd also strongly recommend running future QAs in a fresh conversation if the synthesis was produced here — not an issue in this case since you've only supplied a claim.

One more thing before the readout: you've supplied a single sentence, not a research synthesis. There's a belief about theme preference and a product recommendation ("ship as default"), but no evidence from participants, no study, and no stated reasoning linking the two. The readout below treats "ship dark mode as the default" as the claim under review.

---

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | Declared | B-01 | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "Users want dark mode, so we should ship it as the default theme."

**Evidence strength:** WEAK
No evidence from your users has been cited. The claim rests entirely on a third-party industry survey about preference, which has been promoted into a product default decision.

**Claim matches its evidence:** No — the claim says more than the cited belief supports (preference ≠ default), and the belief itself hasn't been checked against evidence from your users.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** Users *prefer* dark mode at night but want the app to match their system theme, or want to choose on first launch. "Preference" and "default" are different product decisions. A majority preference for dark-at-night is also compatible with a majority preference for *system-matched* defaults.
- **What would overturn this finding:** Evidence from your own users — session data, interviews, or a preference prompt in-product — showing that (a) your users mirror the Nielsen Norman sample, and (b) they want it on by default rather than offered as a choice or matched to system settings.
- **Where the evidence underdetermines the claim:** Almost entirely. One third-party survey about preference is being used to justify a specific default-setting decision in a specific product. The gap between those two things is unaddressed.

**Counter-evidence:** None cited — but note that absence of counter-evidence here reflects absence of evidence overall, not a clean field.

**Unsupported claims:** The entire product recommendation ("ship it as the default theme") has no evidence behind it. The preference claim rests on B-01 only.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | FIRES | "This treats what we learned about people as proven. Only a product can be validated." The phrasing "Users want dark mode" states a want as settled, with no hedging and no evidence from your users. | n/a (no declared item needed) |
| CK-04 Product finding without a human story | FIRES | "This product finding has no evidence about people behind it, and no assumption the team agreed to." The recommendation to ship dark mode as the default cites no people-side evidence. B-01 is about theme preference at night, not about defaults — it doesn't support the product decision. | B-01 covers preference, not defaults |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." B-01 says users "prefer a dark theme at night." The claim converts this to "users want dark mode" (dropping the "at night" qualifier) and then to "ship it as the default theme" (converting a preference into a default-setting decision). | B-01's "at night" qualifier; the preference-vs-default gap |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "Users want dark mode" is a label — no behaviour, no trigger, no named consequence beyond the product action tacked on. Swap "dark mode" for almost any feature and the sentence reads the same. |
| P-03 Transcript Literalism | No | No transcript involved. |
| P-04 Volume Mistaken for Strength | Yes | A single third-party survey (one source type, not your users) is being used to carry a product default decision. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence was raised to file or face. |
| P-08 Narrowing Sold as Resolving | Yes | "Users prefer dark at night" narrows the hypothesis space; it does not resolve "what should the default be?" The claim treats narrowing as if it resolved the design decision. |

### Where does it apply?

**Scope:** B-01 cites "mobile app users" in a 2025 industry survey. The claim is applied to your users, in your product, as a default — three jumps (population, product context, decision type) with no bridge.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no `cannot_claim` list to check against. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer hedge was offered — the transfer from "mobile app users surveyed by NN/g" to "our users" is simply made silently. This is worse than a formulaic hedge, but it isn't the specific pattern P-06 names. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "Users want dark mode" | B-01 (preference, at night, Nielsen Norman 2025) | Inferred (with meaning changed — "prefer at night" → "want") | Partially — the belief is traceable; the reshaping is not justified |
| "we should ship it as the default theme" | not cited | Inferred | No — no evidence or belief supports the default-setting decision |

Neither part of the claim is backed by evidence from your users. The product recommendation has no stated basis at all.

**Checked against:** B-01. No questions or limits declared.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study questions declared. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | Yes | B-01 is cited but its specifics ("at night", mobile apps in general, preference-not-default) are dropped when it's used. Prior knowledge is invoked but not respected. |
| P-07 Trust Without Process | Yes | The jump from "users prefer X at night" to "ship X as default" is asserted, not argued. No reasoning connects the two. |

### Is it theirs or ours?

**Beliefs and evidence:** Every part of this claim comes from the team's prior belief (B-01) and from a product instinct about what to do with it. No part comes from your users.

B-01 is rated `high` confidence with `source_type: third_party_study` and a `source_ref` — that is a legitimately-supported belief in isolation, and CK-01 part (a) does not fire on it. But the claim under review goes well beyond what B-01 says, and the extension has no support of its own.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | CLEAR | B-01 is `high` confidence but its source is a third-party study with a reference, so part (a) doesn't fire. No attributed opinion ("the PM says", "stakeholders agreed") is used, so part (b) doesn't fire either. The problem here isn't borrowed conviction — it's the gap between what B-01 supports and what the claim asserts, which CK-05 and CK-04 catch. | — |

### Tacit-knowledge prompt
Not applicable — no sessions were run.

### Decision boundary
- **Supports:** The belief register supports the proposition that *in a general mobile-app population surveyed in 2025, most users said they prefer a dark theme at night.*
- **Doesn't support:** That your users want dark mode (B-01 is about a general population, not yours). That they want it all the time (B-01 says "at night"). That they want it as a default rather than as an option, system-matched, or prompted on first launch (B-01 doesn't speak to defaults at all).
- **What would close the gap:** The single most useful next piece of evidence would be a short in-product preference prompt or a usage study on your own users, measuring (a) theme choice when offered, (b) whether that choice varies by time of day, and (c) what they expect the default to be. Interviews with 6–8 users on first-launch expectations would also move this materially.

**Safe to act on:** Not yet — the claim says more than its evidence (CK-03, CK-04, CK-05 all fire), and the limits/questions checks couldn't run because no study record was declared. B-01 is a legitimate belief; it just doesn't support the decision being drawn from it.

---

**One thing worth saying plainly:** the structure of this claim — "a general industry stat says X, so we should ship X as a default" — is one of the most common patterns I'd expect this skill to flag. The belief isn't the problem (it's well-sourced). The leap from preference to default, without any evidence from your actual users, is. If dark mode is on the roadmap, the cheapest useful next step is a first-launch preference prompt that logs the answer — you'll have your own data in a week.
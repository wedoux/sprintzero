# UX Research QA Readout

Before I start: a note on process. The checks below depend heavily on what the team declared up front, and here the **study record is "none declared"** and **no evidence was cited** by the claim. That means several checks will report NOT RUN, not CLEAR. A check that didn't run is never reported as passed.

Also: this is a short, one-sentence claim with a declared belief and no study behind it. The QA pass runs the same way regardless, but the interesting finding here is less about *this* sentence and more about the gap between "we believe X" and "therefore ship Y."

---

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | Declared | B-01 | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

---

## Finding: "Users want dark mode, so we should ship it as the default theme."

**Evidence strength:** WEAK
No evidence from your own users was supplied. The claim rests on one third-party industry survey about mobile app users generally, extended into both a desire ("users want dark mode") and a product decision ("ship it as the default").

**Claim matches its evidence:** No — the claim says more than its source supports: the belief is about *preference at night*, the claim drops the time-of-day qualifier and jumps from preference to **default** theme.

---

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** A preference for dark mode *at night* (what B-01 actually says) is consistent with users wanting dark mode as an *option*, or as a scheduled theme, not as the default. "Prefer dark at night" does not imply "prefer dark always," and a default is an always-on choice.
- **What would overturn this finding:** Evidence from your own users showing (a) daytime preference, not just nighttime, and (b) that a dark default outperforms a light default or a system-matched default on a metric you care about (retention, task completion, satisfaction).
- **Where the evidence underdetermines the claim:** Almost everywhere. There is no evidence about your users at all, no evidence about defaults vs. options, and no evidence about time-of-day context.

**Counter-evidence:** None cited, but the belief itself contains a qualifier ("at night") that the claim ignores. That's not counter-evidence — it's the supporting evidence undercutting the claim it's supposedly supporting.

**Unsupported claims:**
- "Users want dark mode" (unqualified) — B-01 only supports "at night."
- "We should ship it as the default" — nothing in the belief or evidence addresses defaults.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | FIRES | "This treats what we learned about people as proven. Only a product can be validated." The claim states "Users want dark mode" as an established fact about people, with no hedge and no sample. | n/a (claim-level) |
| CK-04 Product finding without a human story | NOT RUN | The claim is a product recommendation ("ship it as the default"). No people-side evidence was cited. B-01 is declared but `agreed_by_all = yes` applies to the *belief*, not to a working assumption about defaults. The check can't CLEAR without either people-side evidence or an agreed assumption that actually covers the product decision. | B-01 covers preference-at-night, not defaults |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." B-01 says "at night"; the claim drops the qualifier. B-01 says "prefer"; the claim says "want" and jumps to "default." | B-01 |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "Users want dark mode" is a label, not a behaviour. No trigger (when?), no consequence (compared to what?). Swap "dark mode" for almost any feature and the sentence reads identically. |
| P-03 Transcript Literalism | No | No transcript involved. |
| P-04 Volume Mistaken for Strength | Yes | One third-party survey is being treated as sufficient to drive a default-setting decision for your product. Single source, extrapolated. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence was named — which is itself a weakness, but not this pitfall. |
| P-08 Narrowing Sold as Resolving | Yes | Even if the survey were about your users, "prefer dark at night" narrows the design space (dark mode should exist, probably with scheduling) — it does not resolve "what should the default be?" The claim treats a narrowing finding as a settled product decision. |

---

### Where does it apply?

**Scope:** B-01 covers "mobile app users" generally, surveyed by NN/g in 2025. The claim applies this to "users" of your note-taking app, in all contexts (not just night), as a basis for a default. The scope expands on three axes at once: population (industry → your users), context (night → always), and decision type (preference → default).

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no `limits.cannot_claim` to check against. This is a gap: without a study record, there is no written boundary on what the research can and can't say. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No hedge offered at all. The claim transfers from an industry survey to your product with no caveat, formulaic or otherwise. (Arguably worse than a formulaic hedge — at least a hedge acknowledges the transfer.) |

---

### Could someone retrace it?

**Provenance**

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "Users want dark mode" | B-01 (NN/g 2025 survey) | Inferred — B-01 says "prefer dark theme at night"; claim drops the qualifier | Partially — the source exists, but the claim overstates it |
| "...so we should ship it as the default theme" | Not cited | Inferred — no evidence supplied for the defaults question | No |

Both parts of the claim have gaps: the first overstates its source, the second has no source at all.

**Checked against:** B-01 (belief register). No questions or limits declared.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study questions declared, so the claim can't be mapped against them. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research visibility was provided; can't assess. |
| P-07 Trust Without Process | Yes | The claim asserts "we should ship it as the default" with no reasoning chain — no comparison to alternatives (light default, system default, scheduled theme), no criteria for the decision, no acknowledgement that B-01 doesn't actually cover defaults. |

---

### Is it theirs or ours?

**Beliefs and evidence:** The entire claim comes from the belief register — specifically a third-party survey about mobile app users in general. No part of it comes from what *your* users did or said; no part of it comes from the specific population your product serves. "Agreed by all = yes" on B-01 means the team doesn't dispute the belief, but the team agreeing on a belief doesn't make it evidence about their own users.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | CLEAR (part a) / Does not fire (part b) | B-01 is high-confidence and backed by `third_party_study` with a `source_ref` — part (a) does not fire. The claim attributes to the survey, not to a named authority — part (b) does not fire. | — |

Note: CK-01 clearing here is narrow. It means "the belief's confidence is backed by a real source, not by who said it." It does *not* mean "the belief justifies this claim" — that's CK-04 and CK-05 territory, where things do fire.

---

### Tacit-knowledge prompt
Not applicable — no sessions were run.

A more useful prompt for this case: before shipping dark mode as the default, what does your own usage data say about when your users open the app? If it's mostly daytime, B-01's "at night" qualifier matters a lot. If it's mostly evening, the gap between B-01 and the claim narrows — but still doesn't close the "default vs. option" question.

---

### Decision boundary
- **Supports:** Dark mode is likely worth building as a feature. An industry-wide survey showing nighttime preference is a reasonable basis for prioritising the work.
- **Doesn't support:** That your users want it. That they want it as the default (rather than as an option, or scheduled). That daytime preferences match nighttime ones. That shipping it as the default won't harm users who prefer light themes.
- **What would close the gap:** A small study — even a survey of your current users, or an A/B test of default theme on new signups measuring a metric you care about — would move this from "industry says so" to "our users show so." The single most useful piece: evidence about your users' theme preference *across time of day*, since that's exactly the qualifier B-01 contains and the claim drops.

**Safe to act on:** Not yet — the claim says more than its evidence allows (dropped "at night", jumped to "default"), and no study record was declared, so CK-02 and CK-06 couldn't run.

---

## Summary

The belief itself is well-sourced and the team agrees on it — that's genuine upstream rigour. But two things happen between the belief and the claim that need fixing:

1. **The qualifier gets dropped.** B-01 says "at night." The claim says, in effect, "always." That's the whole difference between "ship a dark mode" and "ship dark as the default."
2. **A preference becomes a product decision without argument.** Nothing in B-01 addresses defaults vs. options vs. system-matched vs. scheduled. The claim treats these as the same question. They aren't.

The honest version of this claim is something like: *"An industry survey suggests mobile users prefer dark themes at night (B-01). This is a reasonable basis to build dark mode. Whether to ship it as the default — rather than as an option or a scheduled theme — is a separate question we have no evidence on yet."* That version would be Safe to act on: Yes, for the build-it decision, with the defaults question explicitly held open.
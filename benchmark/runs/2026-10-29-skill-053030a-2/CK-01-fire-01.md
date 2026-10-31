# QA Readout

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | Declared | B-01 | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

---

## Finding: "Home cooks don't trust AI-generated recipes, so we should hide the AI label entirely."

**Evidence strength:** WEAK
No evidence was cited for this claim. It rests on a single high-confidence belief whose source is a stakeholder opinion in a standup, which a teammate already disagrees with.

**Claim matches its evidence:** No — there is no evidence behind the claim, only a disputed stakeholder opinion restated as a user fact, plus a product recommendation that follows from it.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** The design lead's alternative — that any discomfort users have with AI recipes is about *how they're presented* (tone, formatting, specificity) rather than about trust in AI as a source. On the current evidence, this is as well-supported as the trust framing, which is to say: not at all.
- **What would overturn this finding:** Direct evidence from home cooks — interviews, think-alouds, or A/B tests comparing labelled vs. unlabelled AI recipes — showing that visible AI attribution either doesn't affect trust, or affects it positively for some segments (e.g. cooks who actively seek out AI tools).
- **Where the evidence underdetermines the claim:** Everywhere. No home cook has been observed or quoted. The claim is entirely upstream of any user contact.

**Counter-evidence:** The design lead's dissent (recorded in B-01) directly contests the trust framing and is not addressed in the claim.

**Unsupported claims:** Both parts — (1) "home cooks don't trust AI-generated recipes" and (2) "we should hide the AI label entirely" — have no cited evidence.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | FIRES | "This treats what we learned about people as proven. Only a product can be validated." The claim states as fact that "home cooks don't trust AI-generated recipes" — a claim about people's attitudes — with no evidence and no hedging. | n/a |
| CK-04 Product finding without a human story | FIRES | "This product finding has no evidence about people behind it, and no assumption the team agreed to." The recommendation "hide the AI label entirely" cites no evidence from home cooks, and the only belief it rests on (B-01) has `agreed_by_all = no`. | B-01 |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." "Home cooks" is a universal population claim; "don't trust" is absolute; "hide entirely" is an absolute design directive. All three with zero cited evidence. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "Home cooks don't trust AI-generated recipes" is a label, not a behaviour. No trigger (which recipes? which contexts?), no observable action (what do they do when they don't trust one?), no distinction between products — the sentence would read identically about any AI feature in any domain. |
| P-03 Transcript Literalism | No | No transcript or user-facing material was involved. |
| P-04 Volume Mistaken for Strength | No | There is no volume of evidence at all — the pitfall doesn't apply because nothing is being counted. |
| P-05 Counter-Evidence Filed, Not Faced | Yes | The design lead's dissent is recorded in B-01 but is not acknowledged, let alone argued against, in the claim. The recommendation proceeds as if the disagreement didn't exist. |
| P-08 Narrowing Sold as Resolving | Yes | "Hide the AI label entirely" is a causal claim: it asserts the fix will solve the trust problem. Even if the trust framing were correct, hiding attribution is one of several possible responses (improve the recipes, change the labelling, segment by audience) and the leap from problem to specific solution isn't argued. |

### Where does it apply?

**Scope:** The claim covers "home cooks" as a universal category — no geography, skill level, cuisine, platform, or recipe type is specified. No study was declared, so no scope boundary exists to check against.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record was declared, so no `limits.cannot_claim` to check against. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer across populations is being claimed or hedged. |

### Could someone retrace it?

**Provenance**

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "Home cooks don't trust AI-generated recipes" | Not cited. Restates B-01, a belief sourced to a stakeholder opinion in standup. | Inferred (from one person's opinion) | No — no participant evidence exists. |
| "We should hide the AI label entirely" | Not cited. | Inferred (from the previous claim) | No — no evidence that hiding the label would change behaviour, and no evidence that labelling is causing a problem in the first place. |

Neither claim has any supporting evidence from home cooks. The entire finding is upstream of user contact.

**Checked against:** B-01 (the only declared belief). No questions or limits were declared.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study questions were declared, so there is nothing to check drift against. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research was referenced or omitted; the material simply has no research to be blind to. |
| P-07 Trust Without Process | Yes | The recommendation ("hide the AI label entirely") is asserted, not derived. No reasoning connects the stated user problem to the specific design response — the leap from "don't trust" to "hide entirely" skips every intermediate step (why hiding rather than redesigning? why entirely rather than conditionally?). |

### Is it theirs or ours?

**Beliefs and evidence:** The claim is entirely "ours" — it originates in a stakeholder's standup remark (B-01) and is restated as a fact about users. No part comes from what any home cook did or said, because no home cook has been consulted. The design lead's dissent, already on record, is ignored.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | FIRES | Part (a): "This confidence comes from who said it, not from evidence." The claim restates B-01, a `high`-confidence belief whose `source_type` is `authority`, and cites no evidence unit. | B-01 |

### Tacit-knowledge prompt
Not applicable — no sessions were run, so there is no researcher who was in a room with a home cook to consult.

### Decision boundary
- **Supports:** The team has one stakeholder opinion, disputed internally, that AI labelling may affect trust. That is a hypothesis worth testing.
- **Doesn't support:** Any claim about what home cooks actually feel or do about AI-generated recipes. Any specific design response — hiding the label, keeping it, redesigning it — because there is no evidence about what the label currently does.
- **What would close the gap:** A small study that shows AI-labelled and unlabelled versions of the same recipe to home cooks and observes what they do with each (choose it, cook it, modify it, reject it). This would turn "don't trust" from an assertion into something observable, and would also test the design lead's alternative framing.

**Safe to act on:** Not yet — the claim says more than its evidence (there is none), the recommendation is a stakeholder opinion dressed as a user fact, and an internal disagreement about the underlying framing has not been resolved.

---

## Summary

Three CK checks fired (CK-01, CK-03, CK-04, CK-05), two reported NOT RUN (CK-02, CK-06) because no study record exists, and four pitfalls triggered (P-01, P-05, P-07, P-08). This isn't a close call: the claim is a stakeholder opinion restated as a user fact, with a product directive attached, and a teammate already disagrees with the framing. Before any version of this becomes a decision, the team needs evidence from actual home cooks, and needs to resolve — or at least name — the disagreement already on record in B-01.
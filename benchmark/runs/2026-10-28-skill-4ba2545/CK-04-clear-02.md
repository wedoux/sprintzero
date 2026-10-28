# QA Readout

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | Declared | B-01 | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

---

## Finding: "Cutting the onboarding carousel from five screens to two is the right call."

**Evidence strength:** WEAK
No evidence has been cited for this claim. It rests on a general team principle (onboarding should be fast), not on anything observed about how people use the current five-screen carousel.

**Claim matches its evidence:** No — the claim prescribes a specific product change ("two screens is right") when the only declared support is a general time principle; nothing in the material shows that five screens is too slow, that two screens would still work, or that the carousel is the reason onboarding takes too long.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** The carousel length isn't what's slowing onboarding — the slow step might be elsewhere (account creation, permissions, a loading state), and cutting screens would remove useful context without touching the real cause. Alternatively, two screens might hit the 60-second target but leave returning users confused about a feature the dropped screens explained.
- **What would overturn this finding:** Timing data showing current onboarding is already under 60 seconds; or session evidence that users understand and use features explained on screens 3–5; or a test of a two-screen version showing worse completion or comprehension.
- **Where the evidence underdetermines the claim:** Everywhere. No evidence has been cited for what users currently do, how long it takes them, which screens they skip or dwell on, or what they retain.

**Counter-evidence:** None cited — but the absence is itself the problem, not a sign the claim is unopposed.

**Unsupported claims:** The entire claim is unsupported. Specifically: (a) that the current carousel is a problem, (b) that cutting screens is the right lever, and (c) that two screens (rather than three or four) is the right number.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim is about the product, not about what people are or feel. | n/a |
| CK-04 Product finding without a human story | FIRES | This product finding has no evidence about people behind it, and no assumption the team agreed to that covers it. B-01 is an agreed principle about time ("under 60 seconds"), not about screen count; nothing in the register says "fewer screens" or "two screens" is the way to meet it. | B-01 (covers duration, not structure) |
| CK-05 Scope and certainty inflation | FIRES | This says more, or says it more surely, than the evidence allows. "The right call" is a definitive prescription with no cited evidence — not "likely", not "worth testing", not "consistent with our principle". | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "The right call" names no behaviour, no trigger, no measured consequence — the sentence would read the same for almost any onboarding redesign. |
| P-03 Transcript Literalism | No | No transcript or text source is cited; this pitfall doesn't apply. |
| P-04 Volume Mistaken for Strength | No | No evidence volume to inflate. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence is named or filed. |
| P-08 Narrowing Sold as Resolving | Yes | The claim treats "cut to two screens" as a resolution ("the right call") when, even granting the principle, the evidence at best narrows attention to onboarding speed — it doesn't demonstrate the fix works. |

### Where does it apply?

**Scope:** The claim is about the onboarding flow for returning-category users (the group B-01 names). No evidence base has been declared, so there's no sample to stay inside.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no `limits.cannot_claim` to check against. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is being made. |

### Could someone retrace it?

**Provenance**

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "Cutting from five screens to two is the right call" | Not cited | Inferred (from B-01, apparently) | No — the step from "under 60 seconds" to "two screens" has no stated reasoning or evidence. |

The entire claim has no supporting evidence cited. It should not pass silently.

**Checked against:** B-01 (the only declared item). No questions or limits declared.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study record declared, so there are no questions to map the claim to. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | Nothing suggests prior research exists that this contradicts or duplicates — but that's partly because no prior-research context was supplied. |
| P-07 Trust Without Process | Yes | "The right call" is a verdict with no reasoning shown. There is no derivation from B-01 to "two screens" — just the conclusion. |

### Is it theirs or ours?

**Beliefs and evidence:** The claim has no participant evidence behind it. The only thing supporting it is B-01, a team principle agreed in a retro — i.e. an internal position, not something users showed. The jump from "onboarding should be under 60 seconds" to "therefore two screens" is the team's own reasoning, uncited and unshown.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | CLEAR | B-01 is sourced to `internal_research` with a `source_ref` (2025 onboarding retro notes), not to authority, proxy or own experience; and the claim's support isn't an attributed opinion ("the PM says…"). The problem with this claim is elsewhere (CK-04, CK-05, P-07) — the belief itself is legitimately held. | n/a |

### Tacit-knowledge prompt
Not applicable — no sessions, no researcher to ask. The question for the team is simpler: *what evidence are you using to go from "under 60 seconds" to "two screens"?* If the answer is "none, it's a design judgment", say so and present it that way — not as a finding.

### Decision boundary
- **Supports:** The team principle that returning-category users should get through onboarding in under 60 seconds (B-01).
- **Doesn't support:** That the current five-screen carousel violates that principle; that cutting screens is the right lever to meet it; that two is the right number rather than three or four; that nothing important would be lost in the cut screens.
- **What would close the gap:** Timing data on the current onboarding flow for returning-category users, broken down by screen. If current onboarding already meets the 60-second target, the premise of the change evaporates. If it doesn't, the data will also show which screens actually consume the time — which may or may not be the carousel.

**Safe to act on:** Not yet — the claim prescribes a specific product change with no cited evidence that the current flow has the problem being solved, that the proposed cut addresses it, or that two screens is the right number. B-01 justifies caring about onboarding speed; it does not justify this specific redesign.

---

**A note on the two NOT RUN checks:** CK-02 and CK-06 couldn't run because no study record was declared. That's a choice you're allowed to make, but it means two of the six checks produced no result. If this claim is heading toward a real decision, writing even a lightweight study record (one or two questions, one or two limits) would let those checks actually run next time — see `templates/study-record.md`.
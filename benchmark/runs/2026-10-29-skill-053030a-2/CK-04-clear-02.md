# QA Readout

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | Declared | B-01 | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

A note before the finding: no study record was declared, so CK-02 and CK-06 can't run. The belief register has one entry (B-01), which is a team-agreed working assumption about the product. No evidence was cited for the claim itself. That shapes everything below.

---

## Finding: "Cutting the onboarding carousel from five screens to two is the right call."

**Evidence strength:** WEAK
No evidence was cited. The claim rests entirely on an agreed team principle (B-01), and even that principle is about a *time budget* (under 60 seconds), not a *screen count*. The link from "under 60 seconds" to "two screens, not five" is unargued.

**Claim matches its evidence:** No — the claim is a specific design decision ("cut to two screens"), but the only thing behind it is a time-budget principle that doesn't name screen counts. CK-05 fires on certainty, and CK-04 clears only because an agreed assumption exists at all.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** Five short screens may hit the 60-second target more reliably than two dense ones. Screen count and time-to-complete aren't the same variable, and compressing content onto fewer screens can slow users down if each screen now carries more to read.
- **What would overturn this finding:** Timed task data from returning-category users on both versions (five-screen vs. two-screen), or qualitative sessions showing where the current five screens actually consume the time.
- **Where the evidence underdetermines the claim:** Entirely. There is no evidence about what the current carousel takes to complete, where time is actually lost, or what cutting three screens would remove.

**Counter-evidence:** None cited — but the absence of any evidence at all is itself the issue, not a clean field.

**Unsupported claims:** The entire claim. "Two screens" is unsupported; "the right call" is unsupported; the implicit premise that screen count is the lever for the 60-second target is unsupported.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | Not a claim about people — it's a product decision. | n/a |
| CK-04 Product finding without a human story | CLEAR | No people-side evidence, but B-01 is an agreed working assumption (`agreed_by_all = yes`), which is what this check requires as the alternative. Note: B-01 only loosely supports the specific decision. | n/a |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." Triggering text: "is the right call." The evidence (a 60-second time budget) does not establish that cutting to two screens is *the right* lever, let alone the right number. | B-01 is about time, not screen count. |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim is specific (two screens, not five) — it fails on evidence, not generality. |
| P-03 Transcript Literalism | No | No transcript involved. |
| P-04 Volume Mistaken for Strength | No | No evidence volume to inflate. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence was named at all — which is a different problem (none was engaged with) covered under falsification above. |
| P-08 Narrowing Sold as Resolving | Yes | "The right call" presents a design decision as resolved. At best, B-01 narrows the problem to "onboarding should be faster" — it does not demonstrate that cutting screens is the fix, or that two is the right target. |

### Where does it apply?

**Scope:** Unclear. The claim doesn't say which users, which category, or which version of onboarding. B-01 names "returning-category users"; the claim doesn't restate that scope.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no limits to check against. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is being made. |

### Could someone retrace it?

**Provenance**

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| Cutting the carousel from five to two screens | not cited | Inferred | No — no evidence or reasoning for the number two |
| ...is the right call | B-01 (loosely) | Inferred | No — B-01 is about seconds, not screens |

Every part of the claim is untraceable to evidence. The one declared belief (B-01) is adjacent, not supporting.

**Checked against:** B-01, from the belief register. No questions or limits were declared to check against.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study questions declared. Can't check whether this answers one. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research is referenced, but none was supplied either — this can't be assessed. |
| P-07 Trust Without Process | Yes | "Is the right call" is a conclusion with no visible reasoning chain. Even reconstructing from B-01, you cannot derive "two screens" from "under 60 seconds." |

### Is it theirs or ours?

**Beliefs and evidence:** This is entirely ours. There is no participant data, no behavioural observation, no analytics — only an internal team principle (B-01) that doesn't actually specify the design move being made.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | CLEAR | B-01's source is `internal_research` with a `source_ref` (2025 onboarding retro notes), not authority/proxy/own-experience, so part (a) does not fire. Part (b) does not fire because the claim isn't justified by attributed opinion. Noting: B-01 clears the check, but it still doesn't *support* the specific "two screens" decision. | n/a |

### Tacit-knowledge prompt
Not applicable — no sessions were run or cited.

### Decision boundary
- **Supports:** The team has agreed that returning-category users should complete onboarding in under 60 seconds (B-01). That principle is live.
- **Doesn't support:** That the current onboarding fails the 60-second target. That five screens is the cause. That two screens would meet it. That two is the right number rather than three or one. That screen count is the right lever at all.
- **What would close the gap:** Time-to-complete data for the current five-screen onboarding, broken down by where in the flow time is actually spent. Without this, any screen-count decision is a guess dressed as a principle.

**Safe to act on:** Not yet — the claim is a specific design decision supported only by an adjacent time-budget principle. No evidence shows that cutting screens is the right lever, that the current version fails the target, or that two is the right number. CK-02 and CK-06 also couldn't run because no study record was declared.
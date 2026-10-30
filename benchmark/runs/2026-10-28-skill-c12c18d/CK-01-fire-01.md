## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | Declared | B-01 | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "Home cooks don't trust AI-generated recipes, so we should hide the AI label entirely."

**Evidence strength:** WEAK
The claim rests entirely on a high-confidence belief sourced from a standup remark, with no participant evidence of any kind behind it, and jumps from a stated attitude to a specific product decision.

**Claim matches its evidence:** No — the claim restates a high-confidence belief with no evidence behind it and extends it into a design directive ("hide the AI label entirely") that nothing in the record supports.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** The design lead's dissent on B-01 is the live counter-hypothesis: what reads as "distrust" may be a presentation problem (how the AI origin is framed, where it sits, what context surrounds it), not an attitude about AI authorship. Under this reading, hiding the label would mask a solvable UI problem and could backfire if cooks later discover the origin.
- **What would overturn this finding:** Sessions or survey data with home cooks who are shown AI-labelled and unlabelled versions of the same recipe and whose behaviour (do they cook it, do they trust the quantities, do they come back) is compared. Even a handful of interviews probing why cooks hesitate on an AI-labelled recipe would move this.
- **Where the evidence underdetermines the claim:** The evidence base is empty. Every part of the claim — that distrust exists, that it's about AI specifically, that hiding the label would address it — is underdetermined.

**Counter-evidence:** The design lead's dissent (recorded on B-01) contradicts both the diagnosis and the implied fix, and is not addressed by the claim.

**Unsupported claims:** All of them. "Home cooks don't trust AI-generated recipes" has no participant evidence. "We should hide the AI label entirely" has no evidence and doesn't follow from the first clause even if it were true — hiding a label is one of many possible responses to a trust problem.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | FIRES | "This treats what we learned about people as proven. Only a product can be validated." Triggered by: "Home cooks don't trust AI-generated recipes" — stated as a settled fact about an attitude. | n/a |
| CK-04 Product finding without a human story | FIRES | "This product finding has no evidence about people behind it, and no assumption the team agreed to." Triggered by: "we should hide the AI label entirely" — no participant evidence cited, and the belief it rests on (B-01) has `agreed_by_all = no`. | B-01 |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." Triggered by: "Home cooks don't trust AI-generated recipes" — a universal claim about a population, with no evidence; and "hide the AI label entirely" — a maximal action with no evidence. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "Home cooks don't trust AI-generated recipes" is a surface label with no observable behaviour, no trigger, no specific consequence tied to evidence. |
| P-03 Transcript Literalism | No | No transcript or source text is in play. |
| P-04 Volume Mistaken for Strength | No | There is no evidence volume to mistake — the problem is absence, not homogeneity. |
| P-05 Counter-Evidence Filed, Not Faced | Yes | The design lead's dissent on B-01 is on the record and the claim proceeds as if it isn't. |
| P-08 Narrowing Sold as Resolving | Yes | The claim jumps from a diagnosis ("don't trust") straight to a causal fix ("hide the label"), as if identifying a possible issue resolves what to do about it. |

### Where does it apply?

**Scope:** The claim covers "home cooks" as a population without any sampled subset to anchor it. No study was declared, so there is no sampled scope at all — the claim has no stated boundary.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no `cannot_claim` to check against. Note that this means there is nothing on the record constraining the claim's reach either — the absence cuts both ways. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is being made. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "Home cooks don't trust AI-generated recipes" | Not cited. Appears to restate B-01, itself sourced from a standup remark. | Inferred (from a belief, not from evidence) | No — no participant evidence exists. |
| "We should hide the AI label entirely" | Not cited. | Inferred (from the first clause, which itself is unsupported) | No — no evidence, and the inferential step from "distrust" to "hide" is not argued. |

Every claim in the finding is untraceable to participant evidence. This isn't a thin record — it's an empty one.

**Checked against:** B-01. No questions or limits were declared, so there is nothing else to check against.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No questions declared, so there is nothing for the claim to map to or drift from. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | Nothing in the material claims prior-research status, so there is nothing miscast as novel. |
| P-07 Trust Without Process | Yes | The claim asserts a conclusion ("don't trust") and jumps to an action ("hide the label") with no reasoning chain in between. A reader cannot reconstruct how the diagnosis or the fix was arrived at. |

### Is it theirs or ours?

**Beliefs and evidence:** The entire claim comes from B-01 — a belief rated `high` confidence whose source is `authority` (someone said it in standup, no data behind it) and which the team does not agree on. No part of it comes from what participants did or said.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | FIRES | "This confidence comes from who said it, not from evidence." Triggered by: "Home cooks don't trust AI-generated recipes" — restates B-01, which is `high` confidence, `authority`-sourced, and cites no supporting evidence. Part (a) fires. | B-01 |

### Tacit-knowledge prompt
Not applicable — no sessions were run, so there is no researcher-in-the-room knowledge to surface. If the design lead's dissent on B-01 was prompted by something specific (something they've seen in previous work, a usability session, support tickets), that would be worth capturing before any further decision.

### Decision boundary
- **Supports:** The record supports exactly one statement: *one person believes, with high confidence but no evidence, that home cooks don't trust AI-generated recipes, and at least one colleague disagrees with that framing.* That is a disagreement worth resolving, not a finding.
- **Doesn't support:** It does not support any claim about what home cooks actually think or do, and it does not support any design decision — least of all hiding a label entirely, which is a significant and partly ethical choice (users may reasonably expect to know when a recipe is AI-generated).
- **What would close the gap:** A small, focused study comparing how home cooks respond to the same recipe presented with and without an AI origin label — behaviour as well as stated attitude. Before that, the team should resolve B-01 into a testable question (is this about authorship, or about presentation?) rather than acting on it.

**Safe to act on:** Not yet — the claim restates an unsupported, disputed belief and extends it into a design directive. Nothing about participants has been checked.
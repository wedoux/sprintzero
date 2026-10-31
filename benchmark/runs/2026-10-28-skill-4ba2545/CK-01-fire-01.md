## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | Declared | B-01 | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

Before going further: the synthesis under review was likely produced in a conversation elsewhere, or asserted directly. That's fine for this pass — but note that no study record was declared, so several checks below report NOT RUN. That isn't a technicality: it means nobody wrote down what the study was for, what it asked, or what it gave up, so there's nothing to hold the claim against on those dimensions.

Also worth flagging up front: no evidence was cited. The claim doesn't trace to anything a participant did or said. That alone is usually enough to answer the final question, but the full pass still runs.

---

## Finding: "Home cooks don't trust AI-generated recipes, so we should hide the AI label entirely."

**Evidence strength:** WEAK

No evidence was cited. The only input backing the claim is a single belief (B-01), rated high-confidence, whose source is a standup remark with no data behind it, and which one team member explicitly disagrees with.

**Claim matches its evidence:** No — the claim asserts a user attitude ("home cooks don't trust…") and prescribes a product change ("hide the AI label entirely"), but no user evidence is cited and the underlying belief is contested within the team.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** The design lead's dissent on B-01 is the counter-hypothesis already on the table — that any observed hesitation is about *presentation* (how the AI involvement is shown, the tone of the copy, visual cues of quality) rather than *trust in AI as such*. If that's right, hiding the label addresses the wrong variable and could make things worse by looking evasive if discovered.
- **What would overturn this finding:** Sessions where home cooks are shown the same recipe labelled as AI-generated vs. not, and show no difference in willingness to cook it; or interview evidence where cooks say the label itself is not the issue.
- **Where the evidence underdetermines the claim:** The evidence runs out immediately — nothing was cited. Every part of the claim is underdetermined.

**Counter-evidence:** The design lead's dissent on B-01 directly contests the trust framing. The claim does not engage with it; it proceeds as if the belief were settled.

**Unsupported claims:** Both parts: (1) that home cooks don't trust AI-generated recipes, and (2) that hiding the AI label is the right response. Neither is cited to any evidence unit.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | FIRES | "This treats what we learned about people as proven. Only a product can be validated." The claim states "Home cooks don't trust AI-generated recipes" as established fact about an attitude, with no evidence and over internal dissent. | n/a |
| CK-04 Product finding without a human story | FIRES | "This product finding has no evidence about people behind it, and no assumption the team agreed to." The product prescription ("hide the AI label entirely") cites no people-side evidence, and the belief it rests on (B-01) has `agreed_by_all = no`. | B-01 |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." "Home cooks" is stated as a category with no sample behind it, and "entirely" is maximum certainty on a design prescription with no evidence. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "Home cooks don't trust AI-generated recipes" is a surface label — no behaviour, no trigger, no observable action. The sentence would read the same about any AI feature in any product. |
| P-03 Transcript Literalism | No | No transcript was used. |
| P-04 Volume Mistaken for Strength | No | No volume to inflate — zero evidence units cited. |
| P-05 Counter-Evidence Filed, Not Faced | Yes | The design lead's dissent is on the record (in B-01's dissent_note) and the claim doesn't address it. It's been filed, not faced. |
| P-08 Narrowing Sold as Resolving | Yes | Even granting the trust premise, "hide the label" is sold as the resolution ("so we should…") when at most the premise would narrow the search space to label-related interventions. The jump from "cooks don't trust it" to "hide it entirely" skips the step of asking whether hiding is the right lever. |

### Where does it apply?

**Scope:** No scope stated. "Home cooks" is used as if it means all of them, everywhere, in all cooking contexts. There is no declared sample to stay inside.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no limits to check against. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is being made (and no hedge of any kind). |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| Home cooks don't trust AI-generated recipes. | Not cited. Rests on B-01, a standup remark. | Inferred (from a belief, not from data) | No |
| Therefore we should hide the AI label entirely. | Not cited. | Inferred | No |

Every claim in the finding is untraceable to participant evidence.

**Checked against:** B-01 (belief register). No questions or limits were declared to check against.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No questions declared. Without them, we can't tell whether this answers something the team set out to learn, or arrived from elsewhere. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | Can't be assessed — no prior-research context was supplied. |
| P-07 Trust Without Process | Yes | The claim is asserted ("don't trust… so we should hide…") with no reasoning chain between the attitude and the design decision. The reader cannot reconstruct why hiding — rather than relabelling, explaining, or testing — follows from the premise. |

### Is it theirs or ours?

**Beliefs and evidence:** The claim is entirely "ours", not "theirs". It restates B-01 — a high-confidence belief whose source is `authority` (a standup remark), with no data behind it, and which the design lead disagrees with — and then adds a product prescription on top.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | FIRES | "This confidence comes from who said it, not from evidence." Part (a): the claim restates B-01, which is `high` confidence with `source_type = authority` and no `source_ref`, and cites no supporting evidence unit. | B-01 |

### Tacit-knowledge prompt
Not applicable — no sessions were run.

A more useful next step: ask whoever asserted B-01 in standup what specifically they saw or heard that led them there. If the answer is "nothing, it just seems obvious", that is itself the finding.

### Decision boundary
- **Supports:** That *someone on the team* believes home cooks don't trust AI-generated recipes, and that this belief is not shared across the team.
- **Doesn't support:** Anything about what home cooks actually think or do. Anything about whether hiding the AI label would help, hurt, or do nothing. Anything about which home cooks, in which contexts, with which recipes.
- **What would close the gap:** A small study — even 5–8 sessions — where home cooks encounter recipes with the AI label visible, and the team observes what they do and asks what the label meant to them. This would separate the trust question from the presentation question that the design lead has flagged.

**Safe to act on:** Not yet — the claim cites no evidence, treats a contested internal belief as proven user attitude, and jumps from that belief to a maximum-certainty design prescription ("entirely"). Three CK checks fire and four pitfalls trigger. Two further checks could not run because no study record was declared.

---

## One note on process

This is a case where the QA pass is doing its job by refusing to engage with the claim on its own terms. The claim is phrased as a research finding ("home cooks don't trust…") but no research was done. If the team wants to act on B-01 as a working hypothesis, that's a legitimate choice — but it should be labelled as a hypothesis to test, not a finding to design around. The right next move is almost certainly a small study, not a label change.
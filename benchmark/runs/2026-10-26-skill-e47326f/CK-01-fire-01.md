# UX Research QA Readout

## QA Progress
- [x] Step 1: Confirm there's a conclusion to evaluate
- [x] Step 2: Provenance pass
- [x] Step 3: Falsification pass
- [x] Step 4: Pitfalls check
- [x] Step 5: Produce readout

---

## Finding: "Home cooks don't trust AI-generated recipes, so we should hide the AI label entirely."

**Evidence strength: WEAK**

This is not a research finding — it's an untested assumption from a standup paired with a prescriptive design decision. There is no evidence of any kind cited in support, and the one noted internal dissenting view (design lead's "it's about presentation, not trust") has not been engaged with. Acting on this would be acting on an opinion, not on research.

### Provenance

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| Home cooks don't trust AI-generated recipes | B-01 belief register entry | Inferred — stated as belief, no data | **No** — rationale explicitly says "Said in standup; no data behind it" |
| The distrust is strong/general enough to warrant a design intervention | None cited | Inferred | **No** — not supported anywhere in the material |
| Hiding the AI label would address the problem | None cited | Inferred | **No** — no evidence this intervention would work, or that visibility of the label is even the mechanism |
| The distrust (if real) is about the AI label specifically, not recipe quality, presentation, tone, or source | None cited | Inferred | **No** — directly contradicted by the dissent note from the design lead |

Every substantive claim in this finding is unsupported. The source is explicitly labeled `authority` with confidence `high` and rationale "no data behind it" — the belief register itself is flagging this as an opinion, not a research finding.

### Falsification pass

- **Strongest counter-hypothesis:** The design lead's position — that any user hesitation around these recipes is about presentation (layout, tone, specificity, cooking logic) rather than about the AI label. Under this hypothesis, hiding the label would do nothing, because the label isn't what users are reacting to. A weaker counter-hypothesis: users don't care at all, and the whole premise is a projection from the team onto users.
- **What would overturn this finding:** Any direct user signal — usability sessions where cooks encounter labeled vs. unlabeled AI recipes, interviews probing reactions to AI-generated content in cooking contexts, A/B data on engagement with labeled recipes, reviews or support tickets mentioning the AI label specifically. Even one such source would move this from "untested belief" to "testable finding."
- **Where the evidence underdetermines the claim:** Everywhere. There is no evidence base. The claim is not underdetermined — it is undetermined.

### Pitfalls checked

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | **Yes** | "Don't trust recipes" is a label, not a behaviour. No trigger (when does distrust surface? at the label? at the first instruction that seems wrong? after cooking?), no consequence (do they abandon, double-check, substitute, complain?). The sentence would read the same about any AI product. |
| P-02 Context Blindness | **Yes** | A dissenting internal view is on record (design lead: "this is about presentation, not trust") and the claim proceeds as if that view does not exist. Prior perspective filed, not faced. |
| P-03 Transcript Literalism | No | No transcripts or user sources exist to over-read. |
| P-04 Volume Mistaken for Strength | **Yes** (inverted form) | Confidence is marked `high` with zero supporting evidence units. This is the extreme case of mistaking something other than evidence for evidence strength — here, confidence derives from standup authority rather than data. |
| P-05 Counter-Evidence Filed, Not Faced | **Yes** | The `dissent_note` field names a direct counter-hypothesis (presentation, not trust) and the claim ignores it entirely. The field is populated and then not reasoned against anywhere. |
| P-06 Formulaic Transfer Hedge | No | No transfer claim is being made across populations. |
| P-07 Trust Without Process | **Yes** | The jump from "cooks don't trust AI recipes" to "therefore hide the AI label" is asserted, not derived. Even granting the premise, the intervention doesn't follow — hiding a label is one of several possible responses (improve recipe quality, add provenance signals, add human review, change tone), and no reasoning is shown for why hiding is the right one. |
| P-08 Narrowing Sold as Resolving | **Yes** | "So we should hide the AI label entirely" is a causal claim — asserting the fix will solve the problem — built on top of a premise that hasn't even been investigated, let alone narrowed. The verb is prescriptive ("should hide"), not investigative ("worth testing whether label visibility affects trust"). |

Six of eight pitfalls fire. This is unusual and worth stating plainly: it reflects that the claim is operating entirely in the space of assumption and prescription, with no evidentiary layer for most pitfalls to even engage with.

### What would change this verdict

The single most useful next step is not more evidence for *this* claim — it's a small piece of actual research that could support or refute the premise. Concretely: a short round of usability sessions (5–8 cooks) with two conditions — recipes shown with the AI label visible vs. hidden — observing behaviour (do they cook it? modify it? abandon it? double-check it elsewhere?) and probing afterward on what drove their reaction. That would produce the first real signal on whether the label itself is the mechanism, whether recipe presentation/quality is, or whether neither matters as much as the team assumes.

Until something like that exists, the correct move is not to hide the label — it is to not act on this belief at all, and to notice that the belief register is correctly flagging it (`agreed_by_all: no`, rationale: "no data behind it") as not yet decision-ready.

### Tacit-knowledge prompt

Not applicable — no researcher sessions have been run. The prompt to the team instead is: *before this becomes a design decision, is there appetite for even a lightweight study? The belief register is already telling you this isn't settled.*

---

## Note on scope

This QA pass evaluated the claim as submitted. It is worth flagging separately that the structure of the input — a belief explicitly marked as unsourced, with a recorded dissent, being used to justify a specific product change — is itself the finding here. The pitfalls above describe *how* the reasoning fails; the meta-observation is that this material should probably not have reached a "claims under review" stage without at least one evidence source attached. That's a process signal for the team, not just a per-claim verdict.
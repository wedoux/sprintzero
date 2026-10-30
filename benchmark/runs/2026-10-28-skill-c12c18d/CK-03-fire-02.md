I'll run this QA pass, tracking progress through the workflow.

## QA Progress

- [x] Step 0: Gather declarations — belief register and study record
- [x] Step 1: Confirm there's a conclusion to evaluate
- [x] Step 2: Provenance pass
- [x] Step 3: Falsification pass
- [x] Step 4: Pitfalls check
- [x] Step 5: CK pass
- [x] Step 6: Produce the readout

---

**A note before the readout.** You've declared no belief register and no study record. That's your choice to make, and I'll proceed — but it means several checks can't run, and the readout will say so rather than report them as passed. If you want the full pass, see `templates/belief-register.md` and `templates/study-record.md`; the people who hold the beliefs and planned the study should write them, not me.

Also worth saying up front: the evidence you've supplied is extremely thin — two interview snippets — and the claim under review has serious problems independent of what's declared upstream.

---

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

---

## Finding: "3 good users completed checkout easily; the 2 bad participants just weren't paying attention."

**Evidence strength:** WEAK
Two interview snippets cannot support a claim about five participants, let alone a judgment about their character. The evidence base and the claim don't match in count or in kind.

**Claim matches its evidence:** No — the claim references 5 participants but only 2 are cited; it also judges participants ("good", "bad", "weren't paying attention"), which no evidence supports.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** INT-02's difficulty on the shipping step is a usability problem with the shipping step, not an attention problem with the participant. Needing to ask for help twice at the same step is a signal about the product, not the person.
- **What would overturn this finding:** Evidence from the sessions themselves — what the participants were doing, where they looked, what the shipping step asked them to do — that showed the difficulty was unrelated to the interface. None is cited.
- **Where the evidence underdetermines the claim:** The claim covers 5 participants; evidence is cited for 2. Three participants are referenced with no supporting evidence at all. And no evidence supports any attention-related interpretation of INT-02.

**Counter-evidence:** INT-02 itself is counter-evidence to the "easily" framing — someone got stuck and needed help twice. The claim handles this by reclassifying the participant as "bad" rather than treating the stuck moment as a signal about the checkout flow.

**Unsupported claims:**
- The existence and performance of 3 other participants (no INT-03, INT-04, INT-05 cited).
- That INT-02 and one other participant "weren't paying attention" — no evidence about attention is presented.
- That the 3 cited-but-unseen participants completed checkout "easily."

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | **FIRES** | "This treats what we learned about people as proven. Only a product can be validated." The claim judges participants as "good" or "bad" and attributes an internal state ("weren't paying attention") as fact. | n/a (check runs on claim alone) |
| CK-04 Product finding without a human story | CLEAR | Not a product claim — this is a claim about participants, not about the checkout flow. | n/a |
| CK-05 Scope and certainty inflation | **FIRES** | "This says more, or says it more surely, than the evidence allows." Claim covers 5 participants; evidence covers 2. Certainty words ("easily", "just weren't paying attention") exceed what two snippets can show. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim is specific, just unsupported. |
| P-03 Transcript Literalism | Yes | INT-02's "asked me for help twice" is read as inattention rather than as a possible interface signal. A researcher who was in the room could say whether the participant seemed distracted or seemed to be struggling with the shipping step itself — the text alone can't tell you, and the claim picks one reading with no basis. |
| P-04 Volume Mistaken for Strength | No | The problem is too little evidence, not single-source volume. |
| P-05 Counter-Evidence Filed, Not Faced | Yes | INT-02 is counter-evidence to "completed checkout easily." Rather than face it, the claim reclassifies the participant as "bad" — a textbook move to file contradicting evidence rather than argue with it. |
| P-08 Narrowing Sold as Resolving | No | No narrowing claim is being made. |

### Where does it apply?

**Scope:** Claim covers 5 participants in an unspecified study. Evidence covers 2.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | **NOT RUN** | No study record declared, so no `cannot_claim` to check against. If limits had been declared (e.g. sample, context), this check would likely fire — the claim already stretches well beyond its cited evidence. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim made. |

### Could someone retrace it?

**Provenance**

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "3 good users completed checkout easily" | None cited (only INT-01 is in evidence) | Inferred | No — 2 of the 3 referenced participants are not in the evidence set at all |
| "the 2 bad participants just weren't paying attention" | INT-02 is in evidence; a second "bad participant" is not | Inferred | No — the second participant is uncited, and no evidence about attention is cited for either |
| "completed checkout in under a minute, no hesitation" (INT-01) | INT-01 | Observed | Yes |
| "got stuck on the shipping step and asked me for help twice" (INT-02) | INT-02 | Observed | Yes |

**Three of the five participants named in the claim have no supporting evidence in the material provided.** This is not a minor citation gap — it's the majority of the claim's subjects.

**Checked against:** nothing declared.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | **NOT RUN** | No questions declared, so there's nothing to check drift against. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research is referenced or should be — nothing to check. |
| P-07 Trust Without Process | Yes | The classifications "good users" and "bad participants" are asserted, not derived. No reasoning is given for how a participant was sorted into which category, or what "good" and "bad" mean. The reasoning cannot be reconstructed because none was shown. |

### Is it theirs or ours?

**Beliefs and evidence:** The framing "good users" vs "bad participants" doesn't come from either interview. INT-01 and INT-02 describe behaviour; the moral/evaluative frame around them is the author's. Without a belief register, I can't check whether this frame was declared as a prior belief — but it clearly isn't coming from the participants.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | **NOT RUN** | No belief register declared, so part (a) can't run. Part (b) doesn't fire — no attributed opinion ("the PM says…") is cited. But the "good/bad" judgment likely does reflect a prior belief; a declared register would probably let this check fire. | — |

### Tacit-knowledge prompt

A specific question for whoever ran INT-02: when the participant got stuck on the shipping step, what did they do before asking for help? Did they look confused, scroll around, try to click something, or seem distracted by something unrelated to the screen? The transcript line "asked me for help twice" is compatible with both a shipping-step UX problem and an inattentive participant, and the current claim picks the second reading with no basis.

### Decision boundary

- **Supports:** One participant (INT-01) completed checkout quickly without visible difficulty. One participant (INT-02) got stuck on the shipping step and needed help twice.
- **Doesn't support:** Any claim about 3 other participants (not in evidence). Any judgment about participants' attention, character, or quality as users. Any generalisation about checkout being "easy." Any conclusion that INT-02's difficulty was not a usability signal.
- **What would close the gap:** Evidence from the other 3 sessions, plus — for INT-02 specifically — the researcher's observation of what the participant was doing at the shipping step. If the goal is to decide whether the shipping step has a usability problem, the right next move is to look at what happened on the shipping step across all 5 sessions, not to sort participants into good and bad.

**Safe to act on:** Not yet — the claim judges participants rather than evidence, references 3 participants who aren't in the material, and reclassifies the one contradicting data point as a bad participant rather than engaging with it. If this is being used to decide anything about the checkout flow, the single most important thing to do is stop treating INT-02 as a bad user and start treating "got stuck on shipping, needed help twice" as a signal about the shipping step.

---

**One meta-note.** Several checks here report NOT RUN because you declared no belief register or study record. The claim has enough problems on its own that the readout is still useful, but if you want to pressure-test findings more rigorously in future, declaring beliefs and questions upstream is what lets CK-01, CK-02 and CK-06 actually do their work. The templates are there when you want them.
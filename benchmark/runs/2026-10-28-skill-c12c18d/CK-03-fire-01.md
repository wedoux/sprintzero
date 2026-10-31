# QA Readout

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

Before going further: the user chose not to declare a belief register or study record. That's a choice they can make, but it means several checks below can't run. The findings aren't audited against anything the team said up front — only against the evidence shown. If this is a real decision rather than a quick gut-check, consider filling in the two templates and re-running: beliefs and questions are only useful when written by the people who hold them.

Also worth flagging: the two excerpts are presented without context (study design, how participants were recruited, what question they were answering, how many sessions there were in total). Everything below assumes the two excerpts are the complete evidence base for the claim. If they aren't, the review needs the rest.

---

## Finding: "It's now proven that users prefer voice input over typing."

**Evidence strength:** WEAK
Two participants said they'd rather speak than type. That's a signal worth following up, not a proof of a general preference.

**Claim matches its evidence:** No — the claim says "proven" and "users" (all of them); the evidence is two people expressing a personal preference.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** INT-01 and INT-02 may dislike *this* keyboard, or be in a context (driving, hands full, on the move) where voice is faster — not have a general preference for voice. "Talking is faster for me" is explicitly about one person's experience, not a claim about input modes in general.
- **What would overturn this finding:** evidence that most participants in the study chose typing when both were available, or that INT-01 and INT-02 switch back to typing in other contexts (quiet rooms, sensitive content, public spaces).
- **Where the evidence underdetermines the claim:** we don't know how many participants were in the study, whether anyone preferred typing, what task they were doing, or whether they were ever actually offered a choice. Two quotes can't carry a general preference claim.

**Counter-evidence:** none shown. That's itself worth noting — a synthesis that reaches "proven" without surfacing any dissenting voice is either working from a very thin corpus or filtering.

**Unsupported claims:** "proven" (nothing in two quotes proves anything); "users" as a general category (evidence covers two named individuals); "over typing" as a comparative preference (neither quote compares the two modes head-to-head in a measured way — INT-02 says talking is faster *for me*, which is a personal report, not a comparison).

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | **FIRES** | "This treats what we learned about people as proven. Only a product can be validated." Triggering text: "It's now proven that users prefer voice input over typing." A preference is a claim about people and can't be "proven" by interviews. | n/a (check needs only the claim) |
| CK-04 Product finding without a human story | CLEAR | Not a product claim — it's a claim about user preference. The check doesn't apply here. | n/a |
| CK-05 Scope and certainty inflation | **FIRES** | "This says more, or says it more surely, than the evidence allows." Two participants expressing personal preference become "users" (all) and "proven" (certain). Both scope and certainty are inflated. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "Users prefer voice input over typing" is a label with no trigger (when? for what task?) and no consequence (what should the team do differently?). Swap "voice input" for any other feature and the sentence structure still works — the mark of a label, not an insight. |
| P-03 Transcript Literalism | Yes | Two short written quotes are being treated as the complete picture of what participants meant. "Talking is faster for me" could be about this session's task, this device, this moment — the written text can't tell us, and the synthesis doesn't ask. |
| P-04 Volume Mistaken for Strength | Yes | Both pieces of evidence are from the same source type (interview quotes) and arguably the same signal repeated. No corroboration from analytics, observation, or any independent angle. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence was presented to file or face. (But see the note above: the *absence* of any counter-signal in a corpus that reaches a "proven" verdict is itself suspicious.) |
| P-08 Narrowing Sold as Resolving | No | The claim isn't narrowing a hypothesis space; it's overclaiming on thin evidence. |

### Where does it apply?

**Scope:** the evidence covers two individuals, in an unknown context, at an unknown point in time, doing an unknown task. The claim covers "users" — everyone. The gap between the two is the whole problem with this finding.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | **NOT RUN** | No study record was declared, so no `cannot_claim` lines exist to check against. This is a check that would almost certainly have fired if limits had been declared (sample size, context, task) — but without the declaration, it can't formally run. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is being made (no "this may not apply to X users" hedge to inspect). |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| Users prefer voice input | INT-01, INT-02 quotes | Inferred (from two personal preference statements to a general preference) | Partly — the quotes are cited, but the leap from two quotes to "users" has no supporting trace. |
| It's proven | — | Inferred | No — nothing in the evidence supports the certainty level "proven." |
| Over typing | INT-02 ("talking is faster for me than hunting for the keyboard") | Inferred | Partly — one quote implies a comparison, the other doesn't. |

**Checked against:** nothing declared. No beliefs, questions or limits exist to check this finding against.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | **NOT RUN** | No study questions were declared, so there's nothing to check whether this finding answers. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | Yes | No reference to prior research, prior beliefs, or what the team already knew about input preferences in this product. The finding is presented as if discovered in a vacuum. |
| P-07 Trust Without Process | Yes | The verdict "proven" is asserted without any visible reasoning that would let someone else arrive at the same classification. We're told the conclusion ("proven") but not the argument. |

### Is it theirs or ours?

**Beliefs and evidence:** the claim comes from two participants' quotes. Whether it also comes from a prior team belief ("we always thought voice would win"), we can't tell — nothing was declared. If such a belief exists and the synthesis is leaning on it unconsciously, CK-01 would likely fire, but it can't run without the register.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | **NOT RUN** | Part (a) can't run — no belief register declared. Part (b) doesn't fire on the claim alone (no attributed opinion like "the PM said" appears in the text). Overall: not run. | — |

### Tacit-knowledge prompt (optional)
If a researcher who ran these sessions is available: in INT-01 and INT-02, was voice input one of several options the participant was explicitly weighing, or did it come up spontaneously? And did anyone else in the study express the opposite preference? The answer changes whether this is a weak signal worth testing or a filtering artefact.

### Decision boundary
- **Supports:** two participants, in whatever context these sessions covered, said they'd rather speak than type. That's worth following up with a wider study or an A/B test.
- **Doesn't support:** any claim about "users" generally, any claim that voice preference is "proven", any decision to deprioritise or remove typing.
- **What would close the gap:** a count — out of how many participants in the study, how many expressed a preference for voice, how many for typing, and how many said it depended on context? Even a single sentence of denominator would change this from unactionable to interpretable.

**Safe to act on:** Not yet — the claim says far more, and far more surely, than two interview quotes can support; and the records that would let the rest of the checks run weren't declared.
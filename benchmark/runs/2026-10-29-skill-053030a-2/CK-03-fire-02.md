# QA Readout

## Clarification before I start

You asked me to QA a conclusion drawn from two interviews (INT-01 and INT-02), but the claim refers to "3 good users" and "2 bad participants" — five people total. The evidence you supplied only covers two. I'll flag this as an unsupported-claims problem in the readout rather than assume the other three exist somewhere.

Also, one quick note on process: no belief register or study record was declared. That's your call, and I'll proceed, but several checks will report NOT RUN because they have no declared input to audit against. I've pointed to `templates/belief-register.md` and `templates/study-record.md` if you want to run a fuller pass later.

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
Two interviews cannot support a claim about five people, and the evidence that exists doesn't address attention at all.

**Claim matches its evidence:** No — the claim invents three participants not in evidence, judges participants rather than the product, and attributes a cause (inattention) that nothing in the excerpts supports.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** INT-02's difficulty on the shipping step is a product problem, not a participant problem. A participant asking for help twice at a specific step is the clearest possible signal of a UI issue — that's where usability problems show up.
- **What would overturn this finding:** Evidence that INT-02 was distracted (checked their phone, was interrupted, said they weren't paying attention), or that the shipping step worked cleanly for other participants in matched conditions.
- **Where the evidence underdetermines the claim:** Everything beyond "one person completed quickly, one got stuck on shipping." The evidence says nothing about attention, nothing about three other participants, and nothing about whether "easily" generalises.

**Counter-evidence:** INT-02 itself is counter-evidence to "checkout is easy" and the finding files it as a participant flaw rather than facing it as a product signal.

**Unsupported claims:** The existence of three "good users" and a second "bad participant" — only two participants are cited. The attribution "weren't paying attention" has no supporting evidence at all.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | **FIRES** | "This treats what we learned about people as proven. Only a product can be validated." Triggering text: "good users" and "bad participants" — participants are being judged rather than a product being checked against a standard. | n/a (needs only the claim) |
| CK-04 Product finding without a human story | CLEAR | Not a product claim — the finding is about participants, not the product. | n/a |
| CK-05 Scope and certainty inflation | **FIRES** | "This says more, or says it more surely, than the evidence allows." Triggering text: "3 good users" and "2 bad participants" — the evidence covers two people (INT-01, INT-02), not five. The certainty of "weren't paying attention" also exceeds anything the excerpts show. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim is specific enough; the problem is that it's wrong, not that it's vague. |
| P-03 Transcript Literalism | No | The claim overreaches past the transcript rather than over-trusting it. |
| P-04 Volume Mistaken for Strength | No | Volume isn't the inflation mechanism here; invented participants are. |
| P-05 Counter-Evidence Filed, Not Faced | **Yes** | INT-02 is the counter-evidence to "checkout is easy." Rather than being argued against, it's dismissed by reclassifying the participant as inattentive. The contradiction is disposed of, not resolved. |
| P-08 Narrowing Sold as Resolving | No | No narrowing claim is being made. |

### Where does it apply?

**Scope:** The evidence covers two participants in what appear to be moderated sessions. The claim covers five participants and assigns causes (attention) that would require evidence the excerpts don't contain.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no `cannot_claim` to check against. Note: a declared sample limit would almost certainly have fired here. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No cross-population transfer is being attempted. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "3 good users completed checkout easily" | INT-01 ("Completed checkout in under a minute, no hesitation.") | Inferred (and overgeneralised) | **No** — one participant in evidence, three asserted. |
| "2 bad participants" | INT-02 ("Got stuck on the shipping step and asked me for help twice.") | Inferred (and overgeneralised) | **No** — one participant in evidence, two asserted. |
| "just weren't paying attention" | Not cited | Inferred without basis | **No** — nothing in the excerpts speaks to attention. |

Three of the claim's substantive assertions have no supporting evidence. This isn't a borderline provenance issue; it's a claim about five people built on evidence about two.

**Checked against:** Nothing declared.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study questions declared, so there's nothing to check drift against. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research is referenced or contradicted; nothing to assess. |
| P-07 Trust Without Process | **Yes** | The classification of participants as "good" or "bad" is asserted, not derived. No reasoning is offered for why INT-02 is "bad" rather than the shipping step being badly designed. The counter-argument (that INT-02 is a product signal) is never engaged with. |

### Is it theirs or ours?

**Beliefs and evidence:** The "good / bad users" and "paying attention" language comes from somewhere other than the participants. INT-01 said nothing about being attentive; INT-02 said nothing about being distracted. The frame is being imposed on the evidence, not drawn from it. With no belief register declared, I can't name the specific source, but the pattern — explaining away contradicting evidence by blaming the participant — is a classic case of a pre-existing belief ("checkout is fine") overriding what the sessions showed.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | No belief register declared, and the claim doesn't cite a named authority on its surface ("the PM says…"), so part (b) can't fire on the text alone. If a belief register existed, I'd expect a high-confidence prior belief that "checkout works" to be driving this — but I can't check that without the register. | — |

### Tacit-knowledge prompt

Was there anything in INT-02's session — a comment, an aside, a visible distraction — that would support the "wasn't paying attention" reading? Or did the participant engage normally with the task and simply struggle with the shipping step? The honest answer to this question likely resolves the whole finding.

### Decision boundary

- **Supports:** INT-01 completed checkout quickly on this attempt. INT-02 struggled on the shipping step and needed help twice. That's it.
- **Doesn't support:** Any claim about five participants, any claim about attention, any claim that INT-02's difficulty was the participant's fault rather than the product's, and any generalisation that "checkout is easy."
- **What would close the gap:** Look at INT-02 again, specifically at the shipping step. The right question isn't "was this participant paying attention?" — it's "what, exactly, made the shipping step hard?" That's the finding worth having.

**Safe to act on:** Not yet — the claim describes five participants on evidence from two, dismisses the one clear usability signal in the data (INT-02's shipping difficulty), and attributes a cause (inattention) with no supporting evidence. The reframe worth considering is the opposite one: INT-02 may be the real finding here, and INT-01 the one that tells you less.
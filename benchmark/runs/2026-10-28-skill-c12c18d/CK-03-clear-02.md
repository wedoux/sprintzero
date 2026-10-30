# QA Readout

## Note on inputs

Neither a belief register nor a study record was declared. That's your call, and the pass can still run — but checks that depend on those records will report NOT RUN rather than CLEAR. If you want a stronger audit next time, see `templates/belief-register.md` and `templates/study-record.md`; the beliefs and questions have to be written by the people who hold them, so this skill won't draft them.

If this synthesis was written in the same conversation as the one producing it, re-run the QA in a fresh conversation with only the evidence and the claim pasted in. A model reviewing its own prior output is grading its own homework.

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "Early signal suggests some users may prefer voice input over typing; more sessions are needed to confirm."

**Evidence strength:** WEAK
Two participants, both saying they prefer speaking to typing. That's a real signal from those two people, but it's two people.

**Claim matches its evidence:** Yes — the claim is hedged ("some users", "early signal", "more sessions needed") and stays inside what two interview quotes can support. This is correctly calibrated writing on thin evidence, not an overclaim.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** INT-01 and INT-02 may be describing a context-specific preference (e.g. hands busy, mobile use, accessibility need) rather than a general preference for voice over typing. The quotes don't say *when* they'd rather speak.
- **What would overturn this finding:** evidence from the same participants showing they type by choice in other situations; or sessions where other participants explicitly prefer typing even when voice is available.
- **Where the evidence underdetermines the claim:** two quotes, no context about the task, the device, or whether these participants were asked a leading question. The claim is appropriately hedged — the evidence genuinely doesn't support more.

**Counter-evidence:** none in the material provided.

**Unsupported claims:** none — both parts of the claim trace to the two quotes.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | Claim uses "may prefer" and "more sessions needed to confirm" — not presented as proven. | n/a |
| CK-04 Product finding without a human story | CLEAR | Not a product claim (no design decision asserted); it's a claim about people, backed by two people-side quotes. | n/a |
| CK-05 Scope and certainty inflation | CLEAR | "Some users may prefer" is narrower than the evidence (2 of 2 said so). Certainty is hedged. No inflation. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | "Prefer voice input over typing" is a specific, observable preference. |
| P-03 Transcript Literalism | No | The synthesis isn't over-trusting the transcript; it explicitly flags that more sessions are needed. |
| P-04 Volume Mistaken for Strength | No | Confidence is not inflated — the claim says "early signal", not "strong". |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence in the material to file or face. |
| P-08 Narrowing Sold as Resolving | No | No causal or fix claim. |

### Where does it apply?

**Scope:** two interview participants. The claim says "some users", which stays inside that.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no limits to check against. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| Some users may prefer voice input over typing | INT-01 ("I'd rather just say it out loud than type it"), INT-02 ("Talking is faster for me than hunting for the keyboard") | Observed (participants said it directly) | Yes |
| More sessions are needed to confirm | — | Inferred (judgment about evidence sufficiency) | Yes — follows from n=2 |

**Checked against:** nothing declared.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study questions declared, so can't check whether this answers one. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research mentioned either way; nothing to flag. |
| P-07 Trust Without Process | No | The "early signal / more needed" framing shows its reasoning. |

### Is it theirs or ours?

**Beliefs and evidence:** the claim rests entirely on what the two participants said. No stakeholder opinion, authority, or prior belief is invoked.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | No belief register declared, so part (a) can't run. Part (b) ran on the claim alone and is CLEAR — no attributed opinion ("the PM says", "stakeholders agreed") appears. | — |

### Tacit-knowledge prompt
Were INT-01 and INT-02 describing voice as a general preference, or in a specific context (on mobile, hands busy, long input)? A one-sentence note from the researcher who ran those sessions would sharpen whether this is "prefer voice" or "prefer voice *when*".

### Decision boundary
- **Supports:** two participants said they prefer speaking to typing. That's worth investigating further.
- **Doesn't support:** any claim about what proportion of users prefer voice, in what contexts, or whether offering voice input would change behaviour.
- **What would close the gap:** 6–8 more sessions where participants are asked about input preference without being prompted toward voice, with the context of use captured (device, task, environment).

**Safe to act on:** Not yet — the claim is honest, but two quotes is thin. Safe to act on *as a reason to run more sessions*; not safe to act on as a reason to build voice input.

---

**A note on what this pass couldn't check.** Three checks (CK-01 part a, CK-02, CK-06) reported NOT RUN because no belief register or study record was declared. The claim looks defensible on what could be checked, but a stronger audit would want to know: what did the team believe about voice input before these sessions, and was "do users prefer voice?" one of the questions this study set out to answer? If this is an unexpected finding from a study about something else, that's worth labelling.
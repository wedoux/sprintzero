## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | Declared | "what Android users experience with the unlock flow" | CK-02 |

## Finding: "Hypothesis for a future study (not yet tested): Android users may hit the same scanning friction, since the camera API behaves differently across devices."

**Evidence strength:** WEAK
One iOS participant reported scanner friction; the claim about Android is explicitly framed as a hypothesis for future testing, not a finding.

**Claim matches its evidence:** Yes — the claim is labelled as an untested hypothesis, which is what the evidence (one iOS session plus a general technical rationale) supports.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** The INT-02 scanning difficulty was specific to that participant's phone, lighting, or sticker condition — not a systemic iOS issue, and so not a basis for predicting Android behaviour either. The cross-platform camera API difference might make Android *better*, not worse, at this task.
- **What would overturn this finding:** A round of Android sessions showing no scanning friction, or showing friction with a different root cause than the camera API.
- **Where the evidence underdetermines the claim:** The evidence base is one quote from one iOS participant. It underdetermines even the iOS story, let alone the Android extrapolation. That said, the claim is a hypothesis, not a conclusion — so underdetermination is acknowledged by its framing.

**Counter-evidence:** None cited in the material provided.

**Unsupported claims:** The specific causal mechanism ("since the camera API behaves differently across devices") is stated as rationale but no evidence for it is provided in the material. It reads as plausible technical reasoning rather than something grounded in this study. For a hypothesis this is acceptable; it would need to be checked before any Android claim rested on it.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | Explicitly framed as "hypothesis for a future study (not yet tested)". | n/a |
| CK-04 Product finding without a human story | CLEAR | Not a product finding — it's a hypothesis about user experience to be tested. | n/a |
| CK-05 Scope and certainty inflation | CLEAR | The hedging ("may hit", "hypothesis", "not yet tested") keeps certainty well inside what one iOS data point supports. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | "Scanning friction on QR unlock" is a specific, observable behaviour tied to a specific screen. |
| P-03 Transcript Literalism | No | The claim doesn't over-read the INT-02 quote; it uses it as one signal. |
| P-04 Volume Mistaken for Strength | No | No confidence is claimed — it's a hypothesis. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence is present in the material to face or file. |
| P-08 Narrowing Sold as Resolving | No | No causal claim about a fix is made. |

### Where does it apply?

**Scope:** The evidence covers iOS TestFlight users in moderated sessions. The claim explicitly reaches toward Android — but as a hypothesis to test, which is the correct way to acknowledge a sample limit rather than cross it.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | CLEAR | The declared limit says the study cannot claim what Android users experience. The claim reaches toward Android but labels itself "hypothesis for a future study (not yet tested)" — the template explicitly allows this as a way to stay inside limits. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | The transfer isn't hedged and then asserted — it's named as a hypothesis, with a specific structural reason (camera API difference) to test it. The rationale would need its own evidence before any Android finding rested on it, but as a reason to run the study it's specific and checkable. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| iOS user experienced scanning friction | INT-02: "The QR scanner took three tries to line up on my phone." | Observed | Yes |
| Android users may hit the same friction | Not cited — framed as hypothesis | Inferred (hypothesis) | Yes — labelled as untested |
| Camera API behaves differently across devices | Not cited | Inferred (rationale) | No — stated as technical rationale without a source |

**Checked against:** The declared Android sample limit. No belief register or declared questions were available.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No research questions were declared, so there's nothing to check drift against. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research is referenced in the material; nothing to flag as missing without visibility into what the team already knows. |
| P-07 Trust Without Process | No | The reasoning (one iOS signal + technical rationale → hypothesis for Android) is visible and reconstructible. |

### Is it theirs or ours?

**Beliefs and evidence:** The iOS half of the claim comes from INT-02. The Android half is a hypothesis the team is proposing. No belief register was declared, so it's not possible to tell whether the "camera API differs across devices" rationale is a prior team belief or a fresh inference drawn in writing this up.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | No belief register declared, so part (a) can't run. Part (b) didn't fire — the support cited is INT-02 and a technical rationale, not an attributed opinion. | n/a |

### Tacit-knowledge prompt (optional — ask only if a researcher who ran the sessions is available)
In INT-02, did the participant say or show anything about *why* alignment took three tries — lighting, sticker condition, camera focus behaviour, hand position? That detail would sharpen the Android hypothesis from "scanning is hard" to a specific mechanism worth testing.

### Decision boundary
- **Supports:** Running an Android round of the unlock study, with scanning friction as one of the things to look for.
- **Doesn't support:** Any claim about what Android users actually experience, or any redesign decision made on behalf of Android users. Also doesn't support the camera API rationale as established — that rationale motivates the test, it isn't a finding.
- **What would close the gap:** A small Android round (even 4-6 sessions) running the same unlock task.

**Safe to act on:** Yes — but note what "acting" means here. The claim is a hypothesis, and the only action it supports is *testing it*. It is safe to act on as a reason to commission Android sessions; it is not safe to act on as a basis for any product or design decision affecting Android users. Two checks are NOT RUN (CK-01 part (a) and CK-06) because the belief register and research questions weren't declared — this doesn't block testing the hypothesis, but it does mean the readout can't tell you whether this hypothesis is the right one to prioritise against other unanswered questions the team may have.
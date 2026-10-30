# QA Readout

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | Declared | "what Android users experience with the unlock flow" | CK-02 |

---

## Finding: "2 of the 6 iOS users we tested found the QR scan step frustrating."

**Evidence strength:** WEAK
Two of six participants in a single-platform, single-method sample reported trouble with the QR scan. The signal is real but thin.

**Claim matches its evidence:** Yes — the claim names the exact count ("2 of the 6"), the exact population ("iOS users we tested"), and makes no causal or population-wide assertion.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** The two reports describe different problems — INT-02 names alignment difficulty, INT-05 describes an unexplained scan failure. "Frustrating" may be bundling two distinct issues (camera framing vs. scan reliability) into one theme, when the underlying causes could be unrelated.
- **What would overturn this finding:** Session recordings showing the two participants were not in fact frustrated (e.g. laughing, saying "no big deal"), or evidence that the scan failures were caused by something outside the app (poor lighting, damaged QR codes on specific bikes).
- **Where the evidence underdetermines the claim:** The word "frustrating" is the reviewer's label, not a participant word. Neither quote uses that word. The evidence shows difficulty and one abandonment; the emotional characterisation is an inference.

**Counter-evidence:** None cited. The other 4 participants' experiences with the QR step are not described — their silence in the evidence set is a gap, not a contradiction, but it should be acknowledged.

**Unsupported claims:** The word "frustrating" is not directly supported by the two quoted excerpts. INT-02 describes a mechanical difficulty; INT-05 describes giving up and calling support. Both are consistent with frustration but neither names it.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim is scoped to "the 6 iOS users we tested" and uses a count, not a validated-fact framing. | n/a |
| CK-04 Product finding without a human story | CLEAR | Not a product claim — this is a finding about people's experience, with two citations. | n/a |
| CK-05 Scope and certainty inflation | CLEAR | Scope ("2 of the 6 iOS users we tested") and certainty match the evidence. One minor caveat: "frustrating" is slightly stronger than the quotes directly support, but not inflated to the level this check targets. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim is specific, counted, and scoped. |
| P-03 Transcript Literalism | Yes | "Frustrating" is the reviewer's characterisation; neither quoted participant uses that word. A researcher who ran the sessions could confirm whether frustration was visible (tone, body language) or whether these were calm reports of a mechanical issue. |
| P-04 Volume Mistaken for Strength | No | The claim does not inflate confidence; it reports a count honestly. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence was offered to file or face. |
| P-08 Narrowing Sold as Resolving | No | No causal or fix-oriented claim is made. |

### Where does it apply?

**Scope:** 6 iOS TestFlight users in moderated sessions. The claim stays inside that sample explicitly.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | CLEAR | The claim names "iOS users we tested" and does not generalise to Android or to untested populations. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer is attempted. |

### Could someone retrace it?

**Provenance**

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| 2 of 6 iOS users had trouble with the QR scan step | INT-02, INT-05 | Observed | Yes |
| The experience was "frustrating" | INT-02, INT-05 (not stated directly) | Inferred | Partial — the inference is reasonable but not stated in the quoted material |

**Checked against:** The declared sample limit (Android excluded). No questions or beliefs were declared, so those checks did not run.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No research questions were declared, so the claim cannot be mapped to a question or flagged as unexpected. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research is referenced; none visible in the material to contradict. |
| P-07 Trust Without Process | No | The claim shows its working: specific count, specific sample, specific citations. |

### Is it theirs or ours?

**Beliefs and evidence:** The count and the mechanical difficulty come directly from participants (INT-02, INT-05). The characterisation "frustrating" is the reviewer's framing, not a participant word — but no belief register was declared, so there's no way to check whether this framing reflects a prior team belief.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | No belief register was declared. Part (b) ran on the claim alone and found no attributed opinion ("the PM said", "stakeholders agreed"), so part (b) does not fire — but part (a) could not run. | — |

### Tacit-knowledge prompt
INT-02 describes a mechanical alignment issue; INT-05 describes abandoning and calling support. Were these two participants frustrated in a comparable way — same tone, same intensity — or were they two different reactions ("mildly annoyed" vs. "actually gave up and sought help") that the word "frustrating" is now bundling together? And of the other 4 participants: did any of them also struggle with the scan but push through without comment?

### Decision boundary
- **Supports:** 2 of 6 iOS participants in this study had observable difficulty with the QR scan step, including one who gave up and contacted support.
- **Doesn't support:** The scale of the problem (unknown without the other 4 participants' QR-step experiences), the cause (phone camera, QR code quality, app logic, lighting — all possible), the experience of Android users (explicitly out of scope), or that redesign is the right response.
- **What would close the gap:** The QR-step experience of the other 4 iOS participants in this same study — currently invisible in the evidence. This would move the finding from "2 of 6 had trouble" to a complete picture of how all 6 fared, which is the first thing needed before deciding whether a redesign is warranted.

**Safe to act on:** Not yet — the claim is honest and well-scoped, but with only 2 cited experiences out of 6 sessions, the other 4 participants' QR-step outcomes need to be surfaced before this can inform a redesign decision. Also, two checks (CK-01 part (a), CK-06) could not run because no belief register or research questions were declared.

---

## Summary

This is a well-constructed, honestly-hedged claim on genuinely thin evidence. The reviewer did the right things: named a specific count, scoped it to the tested sample, cited both sources, and did not generalise to Android. That is correct practice, not a flaw.

The main substantive flag is **P-03**: the word "frustrating" is the reviewer's inference, not a participant word. INT-02 describes mechanical difficulty; INT-05 describes giving up. These may both be frustration, but the characterisation sits one step beyond what the quotes directly say.

The main procedural flag is that **no research questions or beliefs were declared**, so CK-01 part (a) and CK-06 could not run. The user chose to proceed without them, which is their call — but it means this QA pass cannot tell whether the finding answers a question the team actually asked, or whether "frustrating" echoes a pre-existing team belief about the unlock flow.
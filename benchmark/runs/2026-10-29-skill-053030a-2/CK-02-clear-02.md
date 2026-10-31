# QA Readout

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | Declared | "what Android users experience with the unlock flow" | CK-02 |

---

## Finding: "Hypothesis for a future study (not yet tested): Android users may hit the same scanning friction, since the camera API behaves differently across devices."

**Evidence strength:** WEAK
One iOS participant reported scanner friction; the claim about Android is explicitly labelled a hypothesis, not a finding.

**Claim matches its evidence:** Yes — the claim is framed as an untested hypothesis for a future study, which is honest about the evidence (one iOS session, nothing on Android).

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** INT-02's three-try scan was an incidental phone-angle or lighting issue in a single session, not evidence of a scanner problem at all — iOS or Android. The "camera API differs across devices" reasoning is a plausible-sounding mechanism that hasn't been tied to any observed Android behaviour.
- **What would overturn this finding:** Android session data showing no scanning friction, or evidence that INT-02's difficulty was situational (phone case, lighting, QR sticker condition) rather than scanner-related.
- **Where the evidence underdetermines the claim:** Entirely. One iOS data point cannot speak to Android. The hypothesis label is appropriate for exactly this reason.

**Counter-evidence:** None in the material provided.

**Unsupported claims:** The specific mechanism ("camera API behaves differently across devices") is asserted without a cited source. It's plausible, but nothing in the evidence set supports it — flag it as the reasoning behind the hypothesis, not as a finding.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim is labelled a hypothesis, not a validated finding about people. | n/a |
| CK-04 Product finding without a human story | CLEAR | Not a product claim — it's a hypothesis about user experience to be tested later. | n/a |
| CK-05 Scope and certainty inflation | CLEAR | "May hit", "hypothesis for a future study (not yet tested)" — the hedging matches the one-participant evidence base. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | — |
| P-03 Transcript Literalism | No | — |
| P-04 Volume Mistaken for Strength | No | One data point is presented as one data point. |
| P-05 Counter-Evidence Filed, Not Faced | No | — |
| P-08 Narrowing Sold as Resolving | No | — |

### Where does it apply?

**Scope:** The evidence covers iOS TestFlight users (one session, INT-02). The claim explicitly extends to Android but is labelled as an untested hypothesis, not an assertion about Android users.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | CLEAR | The study record's `cannot_claim` is "what Android users experience with the unlock flow". The claim is labelled "Hypothesis for a future study (not yet tested)" — the study record's own template allows a hypothesis label as a way to stay within limits. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | The transfer from iOS to Android is named (camera API differences across devices) and the claim is explicitly held back as a hypothesis to be tested, not asserted with a decorative hedge. The mechanism is thin but it is named. |

### Could someone retrace it?

**Provenance**

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| Scanner friction occurred on iOS | INT-02: "The QR scanner took three tries to line up on my phone." | Observed | Yes |
| Android users may hit the same friction | Not cited | Inferred (hypothesis) | Yes — labelled as such |
| Camera API behaves differently across devices | Not cited | Inferred | No — stated as background reasoning without a source |

**Checked against:** The declared sample limit on Android. No belief register and no questions were declared, so CK-01 part (a) and CK-06 could not run.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No questions declared in the study record. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | — |
| P-07 Trust Without Process | No | The hypothesis is stated with its reasoning (API differences) visible, even if that reasoning isn't itself evidenced. |

### Is it theirs or ours?

**Beliefs and evidence:** The iOS observation comes from INT-02. The Android extension comes from the team's reasoning about camera APIs — it's not attributed to any authority or stakeholder, and it's held as a hypothesis rather than a conclusion.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | No belief register declared, so part (a) cannot run. Part (b) does not fire: no attributed opinion ("the PM says", "stakeholders agree") is used as support. | n/a |

### Tacit-knowledge prompt
Was INT-02's three-try scan a scanner-recognition problem (the app failed to read a clear code), or a framing problem (angle, distance, lighting)? The distinction matters: only the first would transfer plausibly to Android via a camera-API mechanism.

### Decision boundary
- **Supports:** Logging a hypothesis for future testing. One iOS participant reported scanner friction; it is reasonable to want to check whether Android users experience the same.
- **Doesn't support:** Any decision about the Android unlock flow. Any claim that the camera API is the cause of scanner friction on either platform.
- **What would close the gap:** A small Android round (even 4–6 sessions) specifically testing the unlock flow, with a note of device models and camera behaviour. Before that, a quick check of whether INT-02's friction was recognition or framing would sharpen the hypothesis itself.

**Safe to act on:** Not yet — the claim is explicitly a hypothesis, not a finding. It's ready to be tested, not acted on.

---

**Note on this pass:** With no belief register and no declared questions, two checks (CK-01 part (a), CK-06) could not run and are reported as NOT RUN, not passed. The claim itself is honestly framed — the hypothesis label does the work the declared limit asks for — but the readout cannot certify what it wasn't given the inputs to check.
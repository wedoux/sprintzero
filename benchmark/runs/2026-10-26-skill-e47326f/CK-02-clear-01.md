## Finding: "2 of the 6 iOS users we tested found the QR scan step frustrating."

**Evidence strength: STRONG**
The claim is tightly scoped to exactly what was observed, in exactly the population tested, with the count matching the cited evidence — this is an unusually clean claim for QA to review.

### Provenance

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| 2 of 6 iOS users | INT-02, INT-05 (2 of 6 sessions) | Observed | Yes |
| Users were iOS | Study record: "iOS TestFlight users only (INT-01 to INT-06)" | Observed | Yes |
| QR scan step specifically | INT-02 ("QR scanner took three tries"), INT-05 ("the scan failed twice") | Observed | Yes |
| "Frustrating" characterisation | INT-02 (three tries to line up), INT-05 (gave up and called support) | Inferred — reasonable inference from behaviour and abandonment, but neither participant used the word "frustrating" | Yes, but flagged |

Minor note on the "frustrating" label: neither quote uses that word. The inference is reasonable (repeated failed attempts + one abandonment-to-support is behavioural evidence of friction), but a stricter phrasing — "experienced repeated scan failures" or "had difficulty with the QR scan step" — would stay closer to what was observed. Not a blocking issue; worth noting for the writeup.

### Falsification pass
- **Strongest counter-hypothesis:** The friction described isn't about the QR *step* in the flow but about QR scanning as a general phone-camera interaction (lighting, sticker condition, camera autofocus). Under this reading, redesigning the unlock screen wouldn't help — the problem lives in the physical scan target or the camera handoff, not the UI. The evidence is compatible with both readings and doesn't distinguish them.
- **What would overturn this finding:** Session recordings or notes showing INT-02 and INT-05's difficulty was caused by something upstream or downstream of the QR step (e.g., they couldn't find the scan button, or the scan succeeded but a subsequent screen failed). As written, the claim is modest enough that it's hard to overturn outright — but it could be made more or less decision-relevant by clarifying *where* in the flow the friction sat.
- **Where the evidence underdetermines the claim:** The claim itself is well-supported. What it *cannot* support — and correctly doesn't try to — is any statement about Android users, about iOS users outside TestFlight, about frequency across the broader user base, or about whether a UI redesign (versus a scan-target or camera-handoff fix) is the right intervention. The study record's `cannot_claim` on Android is honoured.

### Pitfalls checked

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim names a specific behaviour (QR scan difficulty), in a specific step, in a specific population, with a specific count. It would not read the same about any other product. |
| P-02 Context Blindness | No (with caveat) | No prior research was supplied in the study record, so there's nothing to check against. If prior unlock-flow research exists, the team should cross-reference it — flagging this as a visibility gap rather than a failure of the synthesis. |
| P-03 Transcript Literalism | No | The claim stays within what the quotes support and doesn't over-read tone or intent. The "frustrating" label is a mild inference (see provenance note) but not a transcript-literalism failure. |
| P-04 Volume Mistaken for Strength | No | The claim explicitly says "2 of the 6" — it does not inflate two data points into a strong pattern. The denominator is visible. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence was supplied in the evidence set, and the claim doesn't gesture at any it then ignores. The other 4 sessions aren't characterised one way or the other, which is appropriate given no quotes from them were provided. |
| P-06 Formulaic Transfer Hedge | No | The claim is explicitly scoped to "the 6 iOS users we tested" and makes no transfer claim to Android, to non-TestFlight iOS users, or to the broader population. The study record's `cannot_claim` is respected. |
| P-07 Trust Without Process | No | The claim's reasoning is visible: 2 users (named: INT-02, INT-05) described specific scan failures, out of 6 tested. The arithmetic and the attribution are both auditable. |
| P-08 Narrowing Sold as Resolving | No | The claim describes what was observed; it does not assert that redesigning the QR-unlock screen will fix the issue, nor that the QR step is definitively the right place to intervene. The decision the study informs ("whether to redesign the QR-unlock screen") remains open — the finding narrows the search space without overclaiming resolution. |

### What would change this verdict
The single most useful next piece of evidence: notes or recordings clarifying *where* in the scan interaction INT-02 and INT-05's difficulty originated — the on-screen UI, the camera handoff, or the physical QR target. The current claim is well-supported as stated, but the decision it informs (redesign the unlock screen, yes/no) depends on whether the UI is actually the lever. Two users struggling with a QR scan is consistent with a UI problem *and* with a non-UI problem; the current evidence doesn't distinguish them.

### Tacit-knowledge prompt (optional — ask only if a researcher who ran the sessions is available)
For INT-02 and INT-05 specifically: in the moment of difficulty, were they struggling to frame the QR code in the camera viewfinder (suggesting a target/lighting/camera issue), or were they confused about what the screen was asking them to do (suggesting a UI issue)? A sentence of recall on either session would materially change how actionable this finding is for the redesign decision.

---

**Overall note on this QA pass:** This is a case where a careful pass genuinely finds very little to flag. The claim is modestly scoped, numerically honest, population-bounded, and doesn't overreach into the decision it informs. The only substantive notes are (1) the mild inference in the word "frustrating" and (2) the open question of *where* in the scan interaction the friction sat — which is a question for the next study, not a flaw in this one.
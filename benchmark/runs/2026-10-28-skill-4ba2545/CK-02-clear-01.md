# QA Readout

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | Declared | "what Android users experience with the unlock flow" | CK-02 |

## Finding: "2 of the 6 iOS users we tested found the QR scan step frustrating."

**Evidence strength:** WEAK
Two of six participants described difficulty with the QR scan — a real signal, but a thin one from a single sample on a single platform.

**Claim matches its evidence:** Yes — the claim names the count (2 of 6), the population (iOS users we tested), and the specific step (QR scan), and doesn't extrapolate beyond them.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** The frustration may be about phone-camera alignment or lighting in those two sessions, not the QR-unlock screen's design. INT-02 describes a physical alignment problem; INT-05 doesn't say what the scan failure was.
- **What would overturn this finding:** Session recordings showing the two participants' scans succeeded on first or second try, or follow-up data showing they didn't actually feel frustrated.
- **Where the evidence underdetermines the claim:** The evidence shows a scan problem in 2 of 6 sessions. It doesn't tell us *why* the scan failed, or whether "frustrated" is the right word for INT-02 (who describes effort, not emotion). The word "frustrating" is a mild inference, not a direct quote.

**Counter-evidence:** None presented. The other 4 sessions aren't quoted; it's unclear whether they went smoothly or weren't asked about.

**Unsupported claims:** The word "frustrating" is inferred, not observed. INT-05 ("gave up and called support") supports it; INT-02 ("took three tries") is consistent with it but doesn't state it.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim reports a count in a sample, not a validated truth about people. | n/a |
| CK-04 Product finding without a human story | CLEAR | The claim rests on people-side evidence (INT-02, INT-05). | n/a |
| CK-05 Scope and certainty inflation | CLEAR | Scope ("2 of the 6 iOS users we tested") and certainty match the evidence. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim names a specific behaviour (QR scan step), a specific population (iOS testers), and a count. |
| P-03 Transcript Literalism | No | The claim doesn't overread the quotes; if anything it stays close to them. |
| P-04 Volume Mistaken for Strength | No | The claim doesn't inflate confidence — it reports 2 of 6. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence is presented or filed. |
| P-08 Narrowing Sold as Resolving | No | No causal fix is being claimed. |

### Where does it apply?

**Scope:** iOS TestFlight users, moderated sessions, 6 participants. The claim stays inside this.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | CLEAR | The claim explicitly says "iOS users we tested" and does not extend to Android. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is made. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| 2 of 6 iOS users had trouble with QR scan | INT-02, INT-05 | Observed | Yes |
| The experience was "frustrating" | INT-02 (effort), INT-05 (gave up, called support) | Inferred | Yes — but "frustrating" is the reviewer's word, not the participants'. INT-05 supports it more strongly than INT-02. |

**Checked against:** The one declared limit (Android not in sample). No belief register and no study questions were declared, so CK-01 part (a), CK-04's belief-side check, and CK-06 could not run on those inputs.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study questions were declared, so there's nothing to map the claim against. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research is referenced or contradicted, and none was supplied. |
| P-07 Trust Without Process | No | The claim is a straightforward count; the reasoning is visible on the face of it. |

### Is it theirs or ours?

**Beliefs and evidence:** The claim rests on participant quotes, not on prior team belief or authority. No belief register was declared, so CK-01 part (a) can't run; part (b) can, and finds no attributed opinion.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | Part (b) is CLEAR — no "stakeholders say" or "the PM believes" language. Part (a) can't run: no belief register was declared, so there's no way to check whether this claim restates a high-confidence belief with a weak source. | n/a |

### Tacit-knowledge prompt (optional)
INT-02 describes a physical alignment problem ("took three tries to line up"); INT-05 describes giving up and calling support but doesn't say what went wrong. Was the failure mode in INT-05 the same as INT-02 (alignment), or something different (e.g. the code wouldn't register even when aligned, app crash, network error)? The design implication is different depending on which.

### Decision boundary
- **Supports:** Investigating the QR-unlock screen is worthwhile — there's a real signal from 2 of 6 iOS sessions that the scan step is a friction point.
- **Doesn't support:** A decision to redesign the screen. 2 of 6 is a signal, not a verdict, and the root cause (alignment, lighting, code-reading reliability, something else) is unknown. It also says nothing about Android, which the limit explicitly rules out.
- **What would close the gap:** A targeted follow-up focused on the scan step: either more sessions (including Android, if the redesign would ship cross-platform), or instrumentation of scan-attempt counts and failure reasons from the existing TestFlight build.

**Safe to act on:** Not yet — the claim is honest and well-scoped, but the evidence is thin (2 of 6, iOS-only), no study questions were declared so CK-06 couldn't run, and the root cause of the scan failure isn't established. Enough to justify a deeper look at the QR step, not enough to justify a redesign.

---

**A note on what's missing.** This finding came through cleanly, but three checks (CK-01 part (a), CK-04's belief-side check, and CK-06) couldn't run because no belief register and no study questions were declared. For a decision as concrete as "redesign the QR screen", it would be worth filling in [templates/belief-register.md](templates/belief-register.md) and the `questions` field of [templates/study-record.md](templates/study-record.md) and re-running — the gap between "nothing fired" and "nothing could fire" is doing a lot of work in the readout above.
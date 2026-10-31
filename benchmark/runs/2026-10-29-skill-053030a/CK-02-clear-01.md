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
Two of six participants in a single-platform sample reported friction with the QR scan. The pattern is real in this sample but the base is small and single-source.

**Claim matches its evidence:** Yes — the claim names the exact count (2 of 6), names the platform (iOS), and uses "frustrating" to describe what INT-02 and INT-05 actually reported (multiple failed attempts; giving up and calling support). It makes no wider claim.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** The friction may be about phone-camera positioning or lighting in the test context rather than the QR flow itself. INT-02 mentions alignment ("line up"), which could be a device or environmental issue as much as a screen-design one.
- **What would overturn this finding:** Session recordings showing the two participants' scans actually succeeded quickly, or showing the friction was caused by something outside the unlock flow (e.g. a dead sticker on the bike). Neither piece of counter-evidence is present.
- **Where the evidence underdetermines the claim:** Two data points. The claim doesn't overreach, but 2 of 6 is a signal to investigate, not a settled pattern.

**Counter-evidence:** none in the material provided. The other four sessions aren't quoted here, so it isn't possible to tell whether they contradict, support, or are silent on the scan step. Worth checking before acting.

**Unsupported claims:** none — both participants cited produced evidence of friction.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim reports what 2 of 6 participants did/said; it isn't presented as validated or proven. | n/a |
| CK-04 Product finding without a human story | CLEAR | The claim is about people's experience, not a product recommendation. Not a product claim. | n/a |
| CK-05 Scope and certainty inflation | CLEAR | Scope ("2 of the 6 iOS users we tested") and certainty ("found … frustrating") stay inside the evidence. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | Specific behaviour (failed scan attempts), specific population (2 of 6 iOS testers). |
| P-03 Transcript Literalism | No | The claim doesn't over-read the quotes; it summarises what's in them. |
| P-04 Volume Mistaken for Strength | No | The claim doesn't inflate 2 into "users" generally. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence is present in what was supplied — flagged above as a gap to check, not a failure here. |
| P-08 Narrowing Sold as Resolving | No | No causal fix is claimed. |

### Where does it apply?

**Scope:** iOS TestFlight users, moderated sessions, 6 participants. The claim stays inside the sample.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | CLEAR | The claim names iOS explicitly and makes no claim about Android. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer to another population is attempted. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| 2 of 6 iOS users found the QR scan step frustrating | INT-02 ("took three tries to line up"), INT-05 ("gave up and called support after the scan failed twice") | Inferred (the word "frustrating" is a reasonable summary of the reported behaviour, not a direct quote) | Yes |

**Checked against:** the declared limit on Android users. No questions were declared, so CK-06 cannot run.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | Study record declared no questions. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior-research context was supplied; nothing to contradict. Worth confirming whether earlier studies on this flow exist. |
| P-07 Trust Without Process | No | The claim shows its working: specific count, specific sessions cited. |

### Is it theirs or ours?

**Beliefs and evidence:** the claim rests entirely on what two participants said. No belief register was declared, so there's no way to check whether a prior belief shaped the framing (e.g. whether "frustrating" was a word the team expected to hear). This is a gap in the setup, not in the claim.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | No belief register was declared, so part (a) cannot run. Part (b) is clear: the claim's support is two participants, not an attributed opinion. | n/a |

### Tacit-knowledge prompt
What did the other four participants do at the scan step? Did they scan without comment, succeed quickly, or just not mention it? That would tell you whether "2 of 6 had friction" is the whole picture or whether the other four actively had no trouble.

### Decision boundary
- **Supports:** investigating the QR scan step as a candidate friction point worth looking at more closely.
- **Doesn't support:** redesigning the QR-unlock screen on this evidence alone, or any claim about Android users, or any claim about the scale of the problem across the user base.
- **What would close the gap:** what happened at the scan step in the other 4 sessions. If they also showed friction, this becomes a strong signal from a small sample. If they didn't, 2 of 6 may be about device or environment.

**Safe to act on:** Not yet — the claim is honest and well-evidenced for what it says, but 2 of 6 participants from a single platform isn't enough to justify a redesign decision. It's enough to justify a closer look.

---

## Notes on what wasn't checkable

Two checks couldn't run because the inputs weren't declared:
- **CK-06 (Drift)** needs declared research questions. Without them, there's no way to tell whether this finding answers something the team actually asked, or whether it's drift from the study's purpose.
- **CK-01 part (a) (Borrowed conviction)** needs a belief register. Without one, there's no way to check whether this finding restates something the team already believed going in.

Neither gap undermines the specific claim reviewed here, but if more findings from this study are coming, declaring questions and beliefs up front would make the next QA pass meaningfully stronger.
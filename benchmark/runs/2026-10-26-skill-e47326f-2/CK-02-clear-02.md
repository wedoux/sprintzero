QA Progress:
- [x] Step 1: Confirm there's a conclusion to evaluate (not raw notes)
- [x] Step 2: Provenance pass — trace every claim to evidence
- [x] Step 3: Falsification pass — try to break each conclusion
- [x] Step 4: Pitfalls check — screen against references/pitfalls.md
- [x] Step 5: Produce the readout

---

## Finding: "Hypothesis for a future study (not yet tested): Android users may hit the same scanning friction, since the camera API behaves differently across devices."

**Evidence strength: N/A — this is an explicitly framed hypothesis for future work, not a finding being asserted as true.**

This is an unusual object to QA. The claim is self-labelled as untested, flagged as a hypothesis, and is positioned as motivating future research rather than informing the current decision (whether to redesign the QR-unlock screen). It is doing the right thing structurally — naming what the study *cannot* claim, consistent with the declared `limits.cannot_claim` on Android users — and proposing a reason to go look. The QA framing therefore shifts: not "is this conclusion warranted?" but "is this hypothesis responsibly framed, or is it smuggling in a stronger claim than it admits?"

### Provenance

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| Android users were not studied | study_record.limits (sample cut) | Observed (declared) | Yes |
| Scanning friction occurred on iOS | INT-02: "The QR scanner took three tries to line up on my phone." | Observed (n=1, iOS) | Yes |
| Android users *may* hit the same friction | Not cited — this is the hypothesis itself | Inferred (speculative, explicitly labelled) | N/A (hypothesis, not claim) |
| "The camera API behaves differently across devices" | Not cited | Inferred / asserted as background knowledge | **No** — this is stated as a reason but has no evidence attached in the record |

The hypothesis itself is appropriately flagged as untested. But the *rationale* ("since the camera API behaves differently across devices") is asserted as fact without a source. For a hypothesis-generation claim this is lower-stakes than for a finding, but the asymmetry is worth naming: the hypothesis is hedged; its justification is not.

### Falsification pass

- **Strongest counter-hypothesis:** INT-02's scanning friction is specific to their device, their lighting, their sticker condition, or their hand steadiness — not a platform-level issue at all. One iOS user reporting three alignment attempts is extremely thin evidence that there is any scanning friction pattern worth generalising, let alone one that would transfer to Android. The hypothesis may be pointing at a non-problem.
- **What would overturn this finding:** The hypothesis is already framed as untested, so "overturning" isn't quite the right frame. What would make it *not worth pursuing*: evidence that INT-02's experience is idiosyncratic (e.g. the other five iOS sessions showed no scanning friction — the record doesn't say either way), or evidence that the camera API difference claim is overstated for QR-scanning specifically (modern QR libraries abstract over most of it).
- **Where the evidence underdetermines the claim:** Heavily. One quote from one participant is being used to motivate a cross-platform hypothesis. The record doesn't tell us whether INT-01, 03, 04, 05, 06 also struggled with the scanner, which is the first thing you'd want to know before proposing *any* follow-up on scanning friction.

### Pitfalls checked

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The hypothesis names a specific behaviour (scanning friction), a specific population (Android), and a specific mechanism (camera API). |
| P-02 Context Blindness | No (within scope) | No prior research is declared in the register, so there's nothing to check against. Worth noting: if the team has prior cross-platform QR research, this hypothesis should reference it. |
| P-03 Transcript Literalism | No | The hypothesis isn't over-reading INT-02; it's explicitly proposing a future study. |
| P-04 Volume Mistaken for Strength | **Soft yes** | The entire basis for proposing a cross-platform scanning study is *one* iOS quote. The hypothesis doesn't claim strong evidence, but a reader could reasonably ask: is there enough signal here to justify a follow-up at all? The record doesn't tell us whether 1 of 6 or 5 of 6 iOS participants had this experience. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence is present in the record to file or face. |
| P-06 Formulaic Transfer Hedge | **Yes** | This is the central issue. "Android users may hit the same scanning friction, since the camera API behaves differently across devices" is exactly the pattern P-06 warns about: a transfer claim from one population (iOS) to another (Android) with a rationale that sounds technical but isn't argued. *What specifically about camera API differences would produce QR-alignment problems?* Autofocus behaviour? Resolution? Frame rate? Preview-to-capture latency? The sentence names the category of difference without naming the mechanism, and without stating what evidence would confirm or disconfirm the transfer. A reader can't evaluate whether the hypothesis is well-grounded or whether "camera API behaves differently" is doing decorative work. |
| P-07 Trust Without Process | **Soft yes** | The hypothesis asserts a causal link (camera API difference → scanning friction) without showing the reasoning. For a hypothesis this is forgivable — it's meant to be investigated — but the stronger version would say *why* the author thinks this specific mechanism is worth testing over alternatives (sticker condition, lighting, phone-holding ergonomics, app-side alignment UI). |
| P-08 Narrowing Sold as Resolving | No | The hypothesis is appropriately framed as opening a question, not closing one. |

### What would change this verdict

The single most useful thing: a sentence or two from the author stating (a) how many of the six iOS sessions showed scanning friction, not just INT-02, and (b) which specific aspect of camera API behaviour they think is implicated. If 5 of 6 iOS users struggled, this hypothesis is well-motivated. If 1 of 6 did, the hypothesis may be chasing a single data point and the "camera API" rationale is doing more work than the evidence supports.

### Tacit-knowledge prompt

For the researcher who ran these sessions: beyond INT-02, did any of the other five iOS participants have trouble aligning the QR scanner — even briefly, even if they didn't comment on it? And when you wrote "camera API behaves differently across devices," was there a specific behaviour you had in mind (autofocus lag, exposure, preview resolution), or was that a general intuition? The answer to the first determines whether this hypothesis is worth a dedicated study; the answer to the second determines whether the study design is already half-formed or whether it needs scoping.

---

**Overall note on framing:** The author did the hardest part right — they labelled the hypothesis as untested and tied it to a declared limit of the current study. That's genuinely good practice and this QA pass should not pretend otherwise. The remaining issues (P-06, soft P-04, soft P-07) are about tightening the *rationale* for the hypothesis, not about the honesty of the framing. The claim is not being smuggled; it's just under-argued for what it's trying to motivate.
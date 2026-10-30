# UX Research QA Readout

Before I start — a note on conversation hygiene: if this synthesis was produced earlier in this same conversation, the QA pass is more reliable if you run it in a fresh conversation with just the synthesis and evidence pasted in. If you're bringing this in from elsewhere, you're fine.

Also: your material says "none declared" for the belief register and for the study's questions. That's your call to make, and I'll proceed — but the checks that depend on those records will report NOT RUN rather than CLEAR. If you'd like a fuller pass, see `templates/belief-register.md` and `templates/study-record.md` and write your own; I won't draft them for you.

---

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | Declared | "what Android users experience with the unlock flow" | CK-02 |

---

## Finding: "The unlock flow frustrates users — Android users report the same scanning failures and give up just as often."

**Evidence strength:** WEAK
Two iOS session excerpts about QR scanning difficulty cannot support a cross-platform claim about Android users; the Android half of the claim has zero evidence behind it.

**Claim matches its evidence:** No — the claim asserts Android behaviour that the study was explicitly scoped to exclude, and generalises two incidents into a pattern ("users", "just as often").

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** Two iOS participants hit QR alignment problems that are specific to their device model, lighting conditions, or sticker placement at the stations they used — not a general "unlock flow" problem, and certainly not one that would reproduce on Android where the camera stack, autofocus behaviour and scanning library are typically different.
- **What would overturn this finding:** Any Android session data showing the scan works first try; or iOS sessions beyond these two showing scans succeeding; or evidence that the two failures trace to a station/sticker issue rather than the app.
- **Where the evidence underdetermines the claim:** Everything about Android is underdetermined — there is no Android evidence of any kind. The iOS portion is also thin: 2 of 6 participants, with no information on what the other 4 experienced.

**Counter-evidence:** None cited in the material. The absence of counter-evidence here is not reassuring — it reflects a very small evidence set, not a thorough search.

**Unsupported claims:** The entire Android half of the sentence ("Android users report the same scanning failures and give up just as often") has no evidence behind it in the material provided.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim is about product frustration and scan failures, not a validated statement about user psychology. | n/a |
| CK-04 Product finding without a human story | CLEAR | The iOS portion cites INT-02 and INT-05 (people-side evidence). Note: this only clears the check — it does not make the Android portion supported. | n/a |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." Two iOS participants become "users"; one call-to-support incident becomes "give up just as often" as a general pattern. | Evidence base of 2 excerpts from 6 iOS-only sessions. |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "The unlock flow frustrates users" is a label, not a behaviour. No trigger named (which phones? which stations? which lighting?), no mechanism, no specific consequence. Swap "unlock flow" for any other feature and the sentence reads the same. |
| P-03 Transcript Literalism | No | The quotes are being over-extended, but not because the written record was treated as complete — the problem is scope, not literalism. |
| P-04 Volume Mistaken for Strength | Yes | Two excerpts from one source type (moderated iOS sessions) are treated as sufficient to generalise across platforms. One source type, two units, cross-platform verdict. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence was named or filed in the first place. (The deeper problem — that counter-evidence wasn't sought — isn't what P-05 catches.) |
| P-08 Narrowing Sold as Resolving | No | The claim isn't narrowing a hypothesis; it's doing the opposite — expanding a thin signal into a broad verdict. |

### Where does it apply?

**Scope:** Evidence covers 6 iOS TestFlight users, 2 of whom described QR scanning difficulty. The claim extends to Android users, who were explicitly excluded from the sample.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | FIRES | "This claims more than the study was designed to show." The claim states "Android users report the same scanning failures and give up just as often." | The declared limit: "cannot claim: what Android users experience with the unlock flow." |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | Yes (variant) | This is worse than a formulaic hedge — there's no hedge at all. The iOS-to-Android transfer is asserted directly ("report the same… just as often") with no acknowledgment of structural differences between the platforms (different camera stacks, different scanning libraries, different OS-level permissions flows) and no statement of what evidence would be needed. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "The unlock flow frustrates users" | INT-02 (QR scanner took three tries), INT-05 (gave up, called support) | Inferred | Partially — two iOS excerpts support "some iOS participants had scan trouble"; the leap to "users" generally is not traceable. |
| "Android users report the same scanning failures" | Not cited | — | **No — no supporting evidence of any kind in the material provided.** |
| "give up just as often" | INT-05 implied for iOS; nothing for Android | Inferred (iOS); unsupported (Android) | No — one incident doesn't establish a frequency, and no Android data exists. |

**Checked against:** The declared sample limit. No questions were declared, so there's nothing to check drift against.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No questions were declared in the study record, so I can't check whether this claim answers one of them. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research was referenced; I have no visibility into whether this ground was covered before. If prior Android research exists and wasn't referenced, that would trigger P-02 — worth confirming. |
| P-07 Trust Without Process | Yes (mild) | The claim is asserted without reasoning. There's no explanation of why two iOS excerpts should be read as a general unlock-flow problem, or why the Android extrapolation is warranted. The classification is the verdict; no argument is shown. |

### Is it theirs or ours?

**Beliefs and evidence:** With no belief register declared, I can't tell whether the Android half of this claim comes from a prior belief ("we've always thought Android was worse"), from someone senior's opinion, or from somewhere else entirely. The iOS half rests on two participant quotes; the Android half rests on nothing visible in the material.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | No belief register was declared, so I can't check part (a) — whether this claim restates a high-confidence belief sourced from authority, proxy or own experience. Part (b) did not fire: the claim doesn't cite "the PM says" or "stakeholders agreed." But the Android assertion has to come from somewhere, and without a register I can't tell where. | n/a |

### Tacit-knowledge prompt (optional)

If a researcher who ran these sessions is available: in INT-02 and INT-05, was there anything about the setting — the specific station, the time of day, the sticker condition, the participant's phone model — that pointed to a cause more specific than "the unlock flow"? And: where did the Android comparison in the claim come from? Was it discussed in a debrief, raised by a stakeholder, or inferred from somewhere outside the sessions?

### Decision boundary

- **Supports:** "In 2 of 6 iOS TestFlight sessions, participants struggled with QR scanning — one needed three attempts, one abandoned and called support." That is what the evidence lets you say.
- **Doesn't support:** Anything about Android. Anything about "users" as a general group. Any frequency claim ("just as often"). Any claim that the unlock flow — rather than a specific scan interaction, station, or device condition — is the problem.
- **What would close the gap:** The single most useful next piece of evidence is Android sessions on the same unlock flow. Without those, the cross-platform half of this claim cannot be made at all, and the decision about redesigning the QR screen is being made on 2 iOS data points.

**Safe to act on:** Not yet — the claim says more than its evidence allows (CK-02 and CK-05 fired), and two of the checks that would normally help you verify it (CK-01, CK-06) couldn't run because no belief register or questions were declared.

---

## A note on the missing declarations

Three of six checks (CK-01, CK-06, and part of the picture around CK-04) couldn't fully run because the belief register and study questions weren't declared. That's your call, but it means this QA pass is substantially less able to tell you where the Android claim came from, or whether the finding answers something the study set out to learn. If this finding is heading toward a real roadmap decision, declaring those two records and re-running would materially strengthen the audit.
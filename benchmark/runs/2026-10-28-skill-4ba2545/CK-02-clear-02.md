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
One iOS participant mentioned scanner alignment trouble; the claim about Android is openly framed as an untested hypothesis for later work, not as a finding.

**Claim matches its evidence:** Yes — the sentence labels itself as a hypothesis, names the population it hasn't been tested on, and gives a plausible mechanism. It is not asserting that Android users experience friction; it is proposing a question.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** INT-02's scanning trouble is an iOS-specific or device-specific issue (lens, lighting, user technique) with no bearing on Android at all. The "different camera API" mechanism may be real but irrelevant to the user-facing friction.
- **What would overturn this finding:** An Android round of sessions in which participants line up the QR on the first try at rates comparable to or better than iOS. Equally, finding INT-02's issue was a lighting or sticker-wear problem rather than anything camera-stack related.
- **Where the evidence underdetermines the claim:** The evidence is a single iOS report. It cannot speak to Android at all — which is exactly why the claim is framed as a hypothesis rather than a finding.

**Counter-evidence:** None in the provided set.

**Unsupported claims:** The mechanism ("camera API behaves differently across devices") is asserted without a citation. It is plausible background knowledge, but no evidence unit supports it. Worth marking as the author's reasoning rather than something a participant or source established.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim is explicitly a hypothesis, not a validated statement about people. | n/a |
| CK-04 Product finding without a human story | NOT RUN | The claim is about people (Android users' experience), not a product finding; and no belief register was declared to check an agreed-assumption fallback. | n/a |
| CK-05 Scope and certainty inflation | CLEAR | Scope ("Android users") is called out as untested; certainty ("may hit") is appropriately low for a single iOS data point. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim names a specific behaviour (scanning friction) with a specific trigger (camera API differences) and points to a concrete next step (an Android study). |
| P-03 Transcript Literalism | No | The claim doesn't lean on literal transcript content beyond acknowledging the single iOS report. |
| P-04 Volume Mistaken for Strength | No | The underlying signal is one iOS participant, and the claim treats it that way — as a hypothesis, not a strong verdict. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence was presented and ignored. |
| P-08 Narrowing Sold as Resolving | No | The claim narrows toward an investigative next step; it doesn't promise a fix. |

### Where does it apply?

**Scope:** The evidence is iOS TestFlight users only (6 sessions). The claim is explicitly about Android users and is labelled as untested — it stays inside the declared limit by naming the population it hasn't covered rather than speaking for them.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | CLEAR | The limit says the study cannot claim what Android users experience. The claim does not claim it — it proposes it as a hypothesis for a future study. This is the exemption the check explicitly allows. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | The hedge is doing real work: it names the untested population (Android), gives a specific structural reason the question is worth asking (camera API differences), and proposes the obvious resolution (a future study). It is not decorative. |

### Could someone retrace it?

**Provenance**

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| iOS user had scanner alignment trouble (implicit background to the hypothesis) | INT-02 quote | Observed | Yes |
| Android users may hit the same friction | No source — proposed as hypothesis | Inferred | Yes — labelled as untested |
| Camera API behaves differently across devices | Not cited | Inferred (author's reasoning) | No — asserted without a source |

**Checked against:** The single declared limit (Android users excluded from sample). No questions were declared, so CK-06 cannot run.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No research questions were declared, so there is nothing to map the claim to. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | Nothing in the material indicates prior research on this flow that should have been referenced. |
| P-07 Trust Without Process | No | The reasoning is visible: one iOS report + a named mechanism → an untested hypothesis for a future study. A reader can retrace it. |

### Is it theirs or ours?

**Beliefs and evidence:** The scanning friction comes from a participant (INT-02). The leap to Android and the camera-API mechanism are the author's reasoning, openly flagged as untested. No belief register was declared, so there's nothing to check this against formally — but the claim does not try to pass author reasoning off as a participant finding.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | No belief register was declared, so part (a) cannot run. Part (b) does not fire: the claim does not cite an attributed opinion ("the PM says", "stakeholders agree") as its support. | n/a |

### Tacit-knowledge prompt (optional)
For the researcher who ran INT-02: was the alignment trouble something about the camera (focus, lens position, how the phone was held) or more about the sticker/QR itself (worn, in shadow, angled)? That distinction changes whether an Android study is worth running at all, or whether the real next step is a physical audit of the QR stickers.

### Decision boundary
- **Supports:** Running a small Android round to check whether the same friction appears. The hypothesis is specific enough to design against.
- **Doesn't support:** Any claim about what Android users actually experience. Any product change aimed at "fixing" an Android issue that has not been observed.
- **What would close the gap:** 4–6 moderated sessions with Android users on the same unlock flow, with specific attention to time-to-successful-scan.

**Safe to act on:** Yes — but only to act on *as a hypothesis*: i.e. to scope and run the Android follow-up study. Not safe to treat as a finding about Android users or to drive design changes.

---

## Note on this pass

Two checks (CK-01 part (a), CK-04, CK-06) and one check component were marked NOT RUN because no belief register and no research questions were declared. If you want a fuller audit, declaring those two records would let CK-01, CK-04 and CK-06 run properly. The claim as written is unusually careful — it's doing what good hypothesis-labelling should do — so there isn't much for the checks to catch here, but a cleaner pass isn't the same as a complete one.
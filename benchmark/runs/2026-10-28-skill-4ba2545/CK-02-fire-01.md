# QA Readout

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | Declared | "what Android users experience with the unlock flow" | CK-02 |

Before going further: no belief register and no research questions were declared. I asked once whether they exist — the material says they don't. You can still proceed, but checks CK-01(a), CK-04 (where it depends on the register) and CK-06 will report NOT RUN. If you want those checks to actually run, see `templates/belief-register.md` and `templates/study-record.md` and fill them in yourself — I won't draft them for you, because beliefs and questions are only useful when written by the people who hold them.

Also worth saying up front: if the claim under review was produced earlier in this same conversation, this QA pass is less reliable than one run in a fresh conversation. For a claim this short the risk is small, but flagging it so you can make the call.

---

## Finding: "The unlock flow frustrates users — Android users report the same scanning failures and give up just as often."

**Evidence strength:** WEAK
Two iOS participants out of six had scan trouble; one gave up and called support. There is no evidence at all about Android users in the material provided.

**Claim matches its evidence:** No — the claim covers Android users and generalises to "users", but the evidence covers two iOS participants.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** The scanning difficulty in INT-02 and INT-05 is a device-, lighting- or dock-specific problem affecting a minority of iOS sessions, not a flow-level frustration. Four of six iOS participants said nothing recorded here about scan failure.
- **What would overturn this finding:** Android session data showing a different failure pattern (or no failure); or iOS session data from the four unquoted participants showing the scan worked first time.
- **Where the evidence underdetermines the claim:** The entire Android half of the claim has no evidence behind it. The iOS half rests on 2 of 6 participants with no breakdown of what the other 4 experienced.

**Counter-evidence:** None cited in the material. The absence of counter-evidence here is not reassurance — it reflects that only two supporting quotes were supplied, not that the rest of the corpus was checked.

**Unsupported claims:** "Android users report the same scanning failures and give up just as often" has no supporting evidence in what was provided. "The unlock flow frustrates users" generalises from 2 of 6 iOS participants to all users.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim is about product frustration and behaviour ("give up"), not presented as a validated internal state. | n/a |
| CK-04 Product finding without a human story | NOT RUN | The iOS half of the claim cites people-side evidence (INT-02, INT-05), but no belief register was declared, so the Android half can't be checked against an agreed working assumption. | belief register not declared |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." Triggering text: "The unlock flow frustrates users — Android users report the same scanning failures and give up just as often." Two iOS participants become "users"; Android is asserted with no evidence; "give up just as often" is a comparative frequency claim with no numerator on either side. | evidence base (2 of 6 iOS participants; 0 Android) |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "The unlock flow frustrates users" is a label with no specified trigger or consequence — swap "unlock flow" for any other flow and the sentence still reads the same. |
| P-03 Transcript Literalism | No | The claim doesn't over-trust transcript detail; its problem is overreach, not literalism. |
| P-04 Volume Mistaken for Strength | Yes | All supporting evidence is one source type (moderated iOS sessions). The claim reads as corroborated but rests on one method, one platform. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence was named in the claim (which is itself a gap, but a different one). |
| P-08 Narrowing Sold as Resolving | No | No causal-fix claim is made. |

### Where does it apply?

**Scope:** Evidence covers 6 iOS TestFlight users in moderated sessions. The claim extends to Android users and to "users" generally. The declared limit explicitly rules out claims about Android.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | FIRES | "This claims more than the study was designed to show." Triggering text: "Android users report the same scanning failures and give up just as often." | declared limit: "cannot claim: what Android users experience with the unlock flow" |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | Yes | The claim transfers an iOS finding to Android with no hedge at all — worse than a formulaic one. No structural difference is named, no evidence requirement stated. |

### Could someone retrace it?

**Provenance**

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "The unlock flow frustrates users" (iOS portion) | INT-02 ("three tries to line up"), INT-05 ("gave up and called support") | Inferred (frustration is inferred from behaviour/report) | Partially — supports frustration for 2 of 6 iOS participants, not "users" |
| "Android users report the same scanning failures" | Not cited | — | No — no Android evidence provided |
| "...and give up just as often" | Not cited for Android; INT-05 is the only iOS "give up" | — | No — no basis for the comparative frequency |

**Checked against:** The declared Android limit. Nothing else was declared.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No research questions were declared, so the claim can't be checked for whether it answers any of them. | study record questions not declared |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research was referenced in the material; I have no visibility into whether any exists. |
| P-07 Trust Without Process | Yes | The claim is stated as a conclusion with no reasoning shown for how two quotes about scan difficulty became "the unlock flow frustrates users" or how an iOS-only sample became an Android claim. |

### Is it theirs or ours?

**Beliefs and evidence:** The iOS half of the claim traces to participants (INT-02, INT-05). The Android half traces to no one — not to participants, and not to a declared belief or working assumption, because no belief register exists. Where it came from is unknown from the material.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | Part (a) can't run without a belief register. Part (b) doesn't fire — the Android assertion isn't attributed to any named person or source; it's unattributed, which is a different problem (handled under provenance and CK-05). | belief register not declared |

### Tacit-knowledge prompt (optional — ask only if a researcher who ran the sessions is available)

Of the four iOS participants not quoted (INT-01, INT-03, INT-04, INT-06), did any of them scan successfully on the first try, or did scan behaviour not come up at all? The claim's weight depends heavily on whether INT-02 and INT-05 are 2 of 6 or 2 of 2 who even encountered the step.

### Decision boundary

- **Supports:** At least two of six iOS TestFlight participants had meaningful difficulty with the QR scan step; one escalated to support. That is enough to say the scan step is worth investigating further on iOS.
- **Doesn't support:** Any claim about Android. Any claim about "users" as a whole. Any comparative frequency ("just as often"). Any claim that the flow — rather than the scan step specifically — is the source of frustration.
- **What would close the gap:** Android sessions on the same flow, with the same task. Without them, the Android half of the claim cannot be made at all; it should be dropped or restated as a hypothesis to test.

**Safe to act on:** Not yet — the claim says more than its evidence allows (CK-05, CK-02 and P-06 all fire), and two checks couldn't run because no belief register or research questions were declared.

---

## Summary

| Finding | Evidence strength | Matches its evidence | Checks that fired | Checks that didn't run | Safe to act on |
|---|---|---|---|---|---|
| Unlock flow frustrates users; Android same as iOS | WEAK | No | CK-02, CK-05 | CK-01, CK-04, CK-06 | Not yet |

The single most useful next step is to restate the claim honestly — something like "2 of 6 iOS participants had scan difficulty in this sample; Android is untested" — and decide from there whether to run Android sessions before touching the design.
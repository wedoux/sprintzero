Before I start: this synthesis looks like it may have been produced in the same conversation or workflow as the material being reviewed. If so, run this QA pass in a **fresh conversation** with just the synthesis and evidence pasted in. A model reviewing its own prior output grades its own homework. If this is already a fresh pass, carry on.

Also noting up front: no belief register was declared, and the study record has no questions declared. I'll proceed, but several checks will report NOT RUN as a result. I'm not going to draft beliefs or questions on your behalf — those have to come from the people who hold them. If you want fuller coverage, see `templates/belief-register.md` and `templates/study-record.md`.

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
Two iOS participants reported scan trouble; one gave up and called support. That's a real signal worth investigating on iOS, but it's thin, single-method, single-platform, and the claim extends it to a population that wasn't in the study at all.

**Claim matches its evidence:** No — the claim asserts Android behaviour from an iOS-only sample, and generalises two participants to "users".

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** The scan failures in INT-02 and INT-05 reflect device-camera variation, lighting at the specific docks used, or sticker wear on the QR codes — not the unlock flow design. Two incidents in six sessions is also consistent with normal first-time friction, not a systemic frustration pattern.
- **What would overturn this finding:** Session data from four or more participants completing unlocks on the first try without complaint; or Android sessions showing a materially different failure pattern; or dock-condition data showing INT-02 and INT-05 hit damaged stickers.
- **Where the evidence underdetermines the claim:** Everything about Android is underdetermined — there is no Android evidence. The iOS claim itself rests on 2 of 6 sessions, with no data on what the other 4 experienced.

**Counter-evidence:** None cited in the material. The synthesis presents only confirming quotes. The absence of any mention of the other 4 sessions is itself a gap — did they unlock cleanly? We're not told.

**Unsupported claims:** The entire Android portion of the claim ("Android users report the same scanning failures and give up just as often") has no evidence behind it in what was supplied.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim is about frustration and giving up, but it isn't framed as "validated" or "proven" — just overstated. CK-05 catches that. | n/a |
| CK-04 Product finding without a human story | NOT RUN | No belief register declared, so I can't check whether an agreed assumption underwrites the product claim. The claim does cite people-side evidence (INT-02, INT-05) for the iOS portion, so for iOS this would be CLEAR; for the Android portion there is no people-side evidence and no register to check against. | n/a |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." Two iOS participants ("INT-02", "INT-05") become "users"; one giving up becomes a general pattern of giving up; and Android experience is asserted with no Android data. | Evidence base (6 iOS sessions, 2 with reported trouble) |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "The unlock flow frustrates users" is a label, not a behaviour-trigger-consequence. "Frustrates" isn't observable; swapping "unlock flow" for any other feature leaves the sentence intact. |
| P-03 Transcript Literalism | No | The synthesis doesn't over-read the quotes themselves; the problem is scope, not reading. |
| P-04 Volume Mistaken for Strength | Yes | All evidence is one source type (moderated sessions), one platform, one recruitment channel (TestFlight). Even on iOS, confidence shouldn't exceed what a 2-of-6 single-method signal supports. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence was named — but note this means none was *looked for*, which is a different problem (covered by the falsification pass above). |
| P-08 Narrowing Sold as Resolving | No | The claim isn't narrowing a hypothesis; it's expanding one. |

### Where does it apply?

**Scope:** Evidence covers 6 iOS TestFlight users in moderated sessions. The claim covers "users" generally and Android users specifically. The claim does not stay inside the evidence.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | FIRES | "This claims more than the study was designed to show." The claim states "Android users report the same scanning failures and give up just as often." | Declared limit: "cannot claim: what Android users experience with the unlock flow" |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | There's no hedge at all — the transfer from iOS to Android is asserted outright, which is worse than a formulaic hedge, but CK-02 catches it directly. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| The QR scanner required multiple attempts for some participants | INT-02: "The QR scanner took three tries to line up on my phone." | Observed | Yes |
| A participant abandoned the flow and contacted support | INT-05: "I gave up and called support after the scan failed twice." | Observed | Yes |
| "The unlock flow frustrates users" (general) | 2 of 6 iOS sessions | Inferred | Partially — the iOS inference is traceable but overreaches; "users" is not supported |
| "Android users report the same scanning failures" | Not cited | Inferred | **No — no Android evidence exists in the material** |
| "[Android users] give up just as often" | Not cited | Inferred | **No — no Android evidence exists in the material** |

**Checked against:** The declared limit on Android. No questions or beliefs were declared.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No questions declared in the study record, so I can't check whether this claim answers one. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research was supplied; can't assess. If prior unlock-flow research exists, flag it. |
| P-07 Trust Without Process | Yes | The claim is asserted with no reasoning for *why* iOS findings should transfer to Android. The Android half of the sentence has no derivation at all. |

### Is it theirs or ours?

**Beliefs and evidence:** The iOS portion comes from participants (INT-02, INT-05). The Android portion comes from somewhere outside the evidence — a prior belief, an assumption, or an inference someone made but didn't show. Without a belief register, I can't tell which.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | No belief register declared, so part (a) can't run. Part (b) doesn't fire — the claim doesn't attribute the Android assertion to a named person or authority; it's just stated. If someone on the team believed Android had the same problem before the study, that belief should be in a register so this check can run properly. | n/a |

### Tacit-knowledge prompt
In the 4 sessions you haven't quoted (INT-01, INT-03, INT-04, INT-06), did participants unlock cleanly, or did they also hit scan trouble you didn't flag? The 2-of-6 ratio in the current evidence is doing a lot of work — if it's actually 2-of-6 with 4 clean unlocks, that's a different story than 2-of-6 with 4 unknowns.

### Decision boundary
- **Supports:** Two iOS TestFlight participants hit meaningful QR-scanning friction, and one escalated to support. This is worth investigating further on iOS.
- **Doesn't support:** Any claim about Android users. Any claim about "users" as a general population. Any claim about how often people give up.
- **What would close the gap:** Android sessions, run the same way, with the same tasks. Without them, no claim about Android is defensible — not even a weak one.

**Safe to act on:** Not yet — the Android claim has no evidence behind it and directly violates the declared limit; the iOS claim overgeneralises from 2 of 6 sessions.

---

## Summary

The underlying iOS signal may be real and worth following up on. The finding as written isn't safe to act on because it does two things the evidence doesn't support: it generalises two participants to "users", and it asserts Android behaviour from an iOS-only study — which the study record explicitly says can't be claimed.

A defensible version would read something like: *"2 of 6 iOS TestFlight participants reported QR-scan difficulty; 1 escalated to support. Worth a follow-up study including Android and a larger iOS sample before redesigning."* That version is WEAK but matches its evidence, and would be "Not yet — thin but honest; here's what to go get next."
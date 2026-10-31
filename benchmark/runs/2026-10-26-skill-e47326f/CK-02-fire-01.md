## Finding: "The unlock flow frustrates users — Android users report the same scanning failures and give up just as often."

**Evidence strength: WEAK**
This finding makes two claims stitched together — one partially supported by the evidence, one directly contradicting the study's own stated limits. Treat as not warranted in its current form.

### Provenance
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| The unlock flow frustrates users | INT-02 ("took three tries to line up"), INT-05 ("gave up and called support") | Inferred (frustration not named by participants; inferred from behaviour) | Partially — two of six iOS sessions describe scan difficulty; "frustration" is a reasonable but unstated inference |
| Android users report the same scanning failures | No source | — | **No — no Android evidence exists in this study** |
| Android users give up just as often | No source | — | **No — no Android evidence exists in this study** |

The Android half of this finding has zero supporting evidence in the material provided, and the study record explicitly states Android users were not recruited and the study cannot claim what Android users experience. This is not a gap to flag cautiously — it is a direct contradiction of a stated scope limit.

### Falsification pass
- **Strongest counter-hypothesis:** The iOS scanning difficulty may be device-, camera-, or lighting-specific (2 of 6 sessions, both iOS, no detail on conditions). It may not even generalise across iOS users, let alone to Android. A competing explanation — that the two participants had unusual lighting, cases over cameras, or older devices — is not ruled out by anything in the evidence.
- **What would overturn this finding:** For the iOS half: session detail showing the other 4 of 6 participants scanned successfully on the first try would weaken "the unlock flow frustrates users" to "the unlock flow frustrates some users under some conditions." For the Android half: any Android evidence at all. None exists.
- **Where the evidence underdetermines the claim:** The iOS claim rests on 2 of 6 sessions with no information about why scanning failed (lighting? camera? sticker condition? QR size?). The Android claim is not underdetermined — it is unevidenced.

### Pitfalls checked

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "Frustrates users" is a label, not a behaviour. The underlying evidence (multiple scan attempts; abandonment to support) is more specific and more useful than the headline — the finding should be rewritten around the observable behaviour, not the inferred emotion. |
| P-02 Context Blindness | No | No prior research referenced or implied. |
| P-03 Transcript Literalism | No | Not the primary issue; the problem is unevidenced extension, not over-reading what's there. |
| P-04 Volume Mistaken for Strength | Yes | Two interview excerpts from a single source type (moderated iOS sessions) are being used to support a general claim about "users." Even setting aside the Android overreach, 2 of 6 single-source units does not warrant an unhedged generalisation. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence is cited to face or ignore. |
| P-06 Formulaic Transfer Hedge | **Yes — inverted form** | This is worse than the standard formulaic hedge. The usual failure is "may not fully transfer to X" with no argument. Here, the finding transfers to Android *without even the hedge* — and does so despite the study record explicitly stating the transfer cannot be made. The scope limit was filed and then violated in the same document. |
| P-07 Trust Without Process | Yes | "Android users report the same scanning failures" is asserted with no reasoning chain, no evidence, and in direct contradiction of the stated limits. The reader cannot audit how this conclusion was reached because no derivation exists. |
| P-08 Narrowing Sold as Resolving | No | No causal/investigative claim being made about fixes. |

### What would change this verdict
Two separate things, and they should not be confused:
1. **For the iOS claim:** evidence from the other 4 sessions (did they scan successfully? under what conditions?) would let you say whether "frustrates users" is a 2-of-6 edge case or a majority experience. Right now it could be either.
2. **For the Android claim:** Android sessions. There is no shortcut. The claim as written should be deleted, not softened — no rewording of iOS-only evidence can support a statement about Android.

### Recommended rewrite
Split the finding and scope each half to its evidence:
- "2 of 6 iOS TestFlight participants (INT-02, INT-05) experienced repeated QR scan failures, with one abandoning the flow to contact support. Conditions behind the failures (lighting, device model, sticker condition) were not captured and should be investigated before concluding the flow itself is the cause."
- Drop the Android claim entirely. If Android behaviour matters to the redesign decision, it needs its own study — the current evidence base cannot speak to it.

### Tacit-knowledge prompt (for the researcher who ran the sessions)
For INT-02 and INT-05 specifically: was there anything about the physical scanning context — lighting, how the QR sticker looked, whether the participant was holding the phone unusually — that might explain the failures as environmental rather than as a flow problem? This matters because the redesign decision hinges on whether the screen is at fault or the conditions were.
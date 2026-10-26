I'll run the QA workflow on this.

```
QA Progress:
- [x] Step 1: Confirm there's a conclusion to evaluate
- [x] Step 2: Provenance pass
- [x] Step 3: Falsification pass
- [x] Step 4: Pitfalls check
- [x] Step 5: Produce the readout
```

Step 1 note: There is a conclusion to evaluate ("The new onboarding carousel works."), so proceeding to QA rather than synthesis. Flagging up front: the Evidence section is empty and no Study record exists — this is going to be a very short provenance pass and a very confident WEAK verdict.

---

## Finding: "The new onboarding carousel works."

**Evidence strength: WEAK**
There is no evidence in the submitted material supporting this claim. The only belief on the register about carousels expresses *low* confidence, is grounded in "it's what our last redesign used," and carries explicit dissent from the support team. Nothing in the record substantiates that the new carousel "works" — on any definition of "works."

### Provenance

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "The new onboarding carousel works." | Not cited. No study record, no evidence units, no metrics, no user quotes. | Neither — it is an assertion with no supporting observation or inference chain. | No — nothing in the submitted material connects to this claim. |
| Implicit sub-claim: a carousel is a reasonable onboarding pattern | B-01 (belief register) | Inferred from a prior design decision | Partially — but B-01 is marked low confidence, sourced from own_experience ("it's what our last redesign used"), and carries dissent from support ("most people skip it"). It does not support "works." |

The claim has zero direct evidence. The one tangentially related item on the register actively undermines it.

### Falsification pass

- **Strongest counter-hypothesis:** The carousel is skipped by most users (as support team already suspects), and whoever wrote "it works" is reading absence of complaints as evidence of success — or is defining "works" as "ships and renders" rather than "achieves an onboarding outcome."
- **What would overturn this finding:** Any actual evidence tied to a defined outcome — completion rate on the carousel, activation rate for users who saw it vs. a control, time-to-first-key-action, qualitative sessions showing users engaging with the content, or support-ticket volume on topics the carousel is meant to pre-empt. None of this exists in the submitted material.
- **Where the evidence underdetermines the claim:** Everywhere. The claim is 100% underdetermined by the submitted record. There is no study, no metric, no quote, no observation. "Works" is itself undefined — works for whom, measured how, against what baseline.

### Pitfalls checked

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | **Yes** | "Works" has no behaviour, no trigger, and no consequence. Swap "onboarding carousel" for any other feature and the sentence reads identically. There is nothing underneath the label for a team to act on. |
| P-02 Context Blindness | **Yes** | B-01 explicitly flags that the last redesign used a carousel and that the support team believes users skip it. The claim ignores both the prior-design context and the standing dissent. A finding that this one "works" should at minimum reconcile with the suspicion that the previous one didn't. |
| P-03 Transcript Literalism | No | N/A — there is no transcript or review text to over-trust. (The problem here is the opposite: no source material at all.) |
| P-04 Volume Mistaken for Strength | No | N/A — no volume of evidence to mistake. |
| P-05 Counter-Evidence Filed, Not Faced | **Yes** | The support team's dissent ("most people skip it") is on the register and is directly relevant to whether a carousel "works." The claim does not engage with it — not to refute it, not to scope around it, not even to acknowledge it. It is filed in B-01 and ignored. |
| P-06 Formulaic Transfer Hedge | No | No transfer claim is being made across populations or markets. |
| P-07 Trust Without Process | **Yes** | "The new onboarding carousel works" is a conclusion with no reasoning attached. There is no derivation to audit — just an assertion. One cannot reconstruct the classification from stated reasoning because no reasoning is stated. |
| P-08 Narrowing Sold as Resolving | No | No narrowing is claimed; the claim jumps straight to a resolved verdict without any investigative step preceding it. |

### What would change this verdict

A single concrete artifact would move this from WEAK toward evaluable: a defined success metric for the carousel (e.g. "≥60% of new users advance past slide 3" or "activation rate +X% vs. no-carousel control"), plus one data source reporting against it. Without a definition of "works" and at least one measurement, the claim cannot be strengthened — only restated.

Second-most useful: a direct check against the support team's dissent. If skip-rate data shows most users dismiss the carousel immediately, the claim is actively falsified, not merely unsupported.

### Tacit-knowledge prompt

For whoever authored the claim: when you wrote "works," what specific outcome did you have in mind, and what did you observe that led you to believe that outcome was being achieved? The gap between "shipped" and "works" is where this finding needs to land, and nothing in the submitted material tells us which side of that gap the author is standing on.

---

**Meta-note on this QA pass:** This is an unusually clean case because the record is nearly empty. The verdict is high-confidence WEAK not because the carousel is bad, but because the claim is unsupported on its face. If the author has evidence that wasn't submitted (analytics, a usability test, completion metrics), re-run this QA with that evidence attached — the verdict could change substantially. If no such evidence exists, the honest version of this claim is "we shipped a carousel; we don't yet know whether it works."
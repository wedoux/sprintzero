## QA Readout

**Reviewer note before I begin:** The claim under review refers to "3 good users" and "2 bad participants." The evidence provided contains only **two interview excerpts** (INT-01, INT-02), not five. I cannot locate the other three participants in the material supplied. This is itself a finding — I'll flag it below rather than silently reasoning as if the missing data existed.

I'll also note the loaded framing ("good users" / "bad participants") up front, because it shapes how the rest of the claim should be read. More on this under P-07.

---

## Finding: "3 good users completed checkout easily; the 2 bad participants just weren't paying attention."

**Evidence strength: WEAK**
The claim as written cannot be supported by the evidence provided — three of the five participants it references are absent from the material, and the characterisation of the two who are present ("good" / "bad," "weren't paying attention") is not derivable from what INT-01 and INT-02 actually say.

### Provenance

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "3 good users completed checkout easily" | None provided | Neither — asserted | **No.** No evidence for any of the three. The three participants are not in the evidence set at all. |
| INT-01 completed checkout easily | INT-01: "Completed checkout in under a minute, no hesitation." | Observed | Yes — but INT-01 is one person, not three. |
| "the 2 bad participants just weren't paying attention" | None provided | Inferred, and the inference is not supported | **No.** INT-02 shows one participant getting stuck and asking for help twice. That is behavioural evidence of a usability problem, not evidence of inattention. The second "bad participant" is not in the evidence set. |
| Characterisation of INT-02 as "bad" / "not paying attention" | INT-02: "Got stuck on the shipping step and asked me for help twice." | Inferred | **No** — the inference reverses the usual reading of this evidence. Getting stuck and asking for help is standardly read as a signal about the *interface*, not the *participant*. |

Three of the five participants referenced in the claim have **no supporting evidence of any kind** in the material provided. The two who do appear are mischaracterised relative to what their excerpts actually say.

### Falsification pass

- **Strongest counter-hypothesis:** INT-02's behaviour — getting stuck on shipping, asking for help twice — is a usability signal about the shipping step, not a signal about the participant's attentiveness. The simplest explanation for a user getting stuck twice in the same place is that the place is confusing, not that the user is deficient. INT-01 completing quickly is compatible with this: easy for some, broken for others, which is exactly the pattern a shipping-step defect would produce.
- **What would overturn this finding:** Evidence from the three missing participants (did they actually complete checkout easily, and what does "easily" mean in observable terms?), plus any evidence about INT-02's attention state during the session that is independent of the stuck-on-shipping behaviour itself. Without the missing three, the "3 good / 2 bad" framing has no basis at all.
- **Where the evidence underdetermines the claim:** Almost everywhere. We have one data point suggesting smooth checkout (INT-01) and one data point suggesting a shipping-step problem (INT-02). That is all. Every other element of the claim — the counts, the categorisation, the attribution of INT-02's difficulty to inattention — is unsupported.

### Pitfalls checked

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim is specific; the problem is that the specifics aren't evidenced, not that they're vague. |
| P-02 Context Blindness | N/A | No prior research declared. |
| P-03 Transcript Literalism | **Yes** | The claim treats "asked me for help twice" as evidence of participant inattention. A researcher who was in the room would almost certainly have context about *why* INT-02 got stuck (where exactly on the shipping step, what they tried, what they said while stuck). The written excerpt is being read in the way most convenient to the claim rather than being treated as the thin signal it is. |
| P-04 Volume Mistaken for Strength | **Yes, inversely** | The claim asserts counts (3 and 2) that aren't present in the evidence at all. This is worse than mistaking volume for strength — it's asserting volume that doesn't exist. |
| P-05 Counter-Evidence Filed, Not Faced | **Yes** | INT-02 is counter-evidence to the "checkout works" story and is handled by reclassifying the participant as deficient rather than engaging with the behavioural signal. This is the structural move the pitfall names: contradicting evidence named, then neutralised without being argued against. |
| P-06 Formulaic Transfer Hedge | No | No transfer claim. |
| P-07 Trust Without Process | **Yes** | The verdict ("good users" vs. "bad participants") is asserted, not derived. The reasoning that would classify INT-01 as "good" and INT-02 as "bad / not paying attention" is nowhere stated. Reconstructing the classification from the evidence alone, a neutral reviewer would reach a different conclusion: one participant had a smooth session, one encountered friction at a specific step. The "good/bad" framing is a label applied to the participants to protect a prior belief about the product. |
| P-08 Narrowing Sold as Resolving | No | No narrowing claim. |

### What would change this verdict

Two things, in order of importance:

1. **The missing evidence for the three unaccounted-for participants.** Without it, the headline count ("3 good") is not a finding, it's an assertion. If those three sessions exist, their evidence needs to be in the set under review.
2. **A reason, grounded in what INT-02 actually did or said, to prefer the "inattention" reading over the "shipping step is confusing" reading.** The current claim prefers inattention without argument. The default reading of "stuck twice, asked for help twice" is a usability problem; overturning that default requires specific evidence, not relabelling.

### Tacit-knowledge prompt

If the researcher who ran INT-02 is available: *What specifically was INT-02 stuck on at the shipping step — a field, a button, a validation error, something else? And when they asked for help the second time, was it the same issue as the first time or a different one?* The answer determines whether this is one defect, two defects, or a genuinely confused participant — and the current claim depends on an answer the evidence doesn't provide.
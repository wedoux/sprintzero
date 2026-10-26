## Finding: "5 of 6 participants did not notice the new filter button without being prompted."

**Evidence strength: STRONG**
The claim is a direct count of what participants said in the sessions, and the count checks out — five of six transcripts show non-discovery without prompting, one shows unprompted discovery. This is about as cleanly evidenced as a six-session discoverability finding gets, within the limits of that sample size.

### Provenance
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| INT-01 did not notice without prompting | "I didn't see a way to filter until you pointed at it." | Observed | Yes |
| INT-02 did not notice without prompting | "I never noticed there was a filter option, had no idea it existed." | Observed | Yes |
| INT-03 did not notice without prompting (found by accident late in task) | "Took me the whole task to realize I could filter - found it by accident." | Observed | Yes |
| INT-04 did not notice without prompting | "Didn't see it, I was looking at the top of the screen the whole time." | Observed | Yes |
| INT-05 did not notice without prompting | "I spotted it eventually but only because I was told something was there." | Observed | Yes |
| INT-06 did notice without prompting | "Saw it right away, it's in a pretty obvious spot." | Observed | Yes |

One small note on INT-03: "found it by accident" is non-discovery of the intended, unprompted kind — the participant was not told, but also did not discover it through the designed affordance. Classifying this as "did not notice without being prompted" is defensible but worth naming explicitly rather than silently rolling in. The 5-of-6 count holds under either reading, because even if INT-03 were reclassified as a discovery, it would be 4-of-6, which doesn't change the qualitative verdict.

### Falsification pass
- **Strongest counter-hypothesis:** The sessions share a moderator, a task framing, and likely a device/screen configuration. If participants were all primed by the same task wording to look somewhere specific (e.g., INT-04: "I was looking at the top of the screen the whole time"), the finding may be about task framing driving attention away from the filter, not about the button being undiscoverable in realistic use. The claim as stated is still true of this study, but its implication for the redesign decision depends on whether the task mirrored real usage.
- **What would overturn this finding:** A session recording review showing the moderator (or task script) directed attention away from where the filter sits — or analytics from live product showing filter-use rates inconsistent with a 1-in-6 discovery rate.
- **Where the evidence underdetermines the claim:** The finding as literally stated ("5 of 6 did not notice") is fully determined by the evidence. What it underdetermines is any step beyond that — e.g., "the filter button is undiscoverable" or "the entry point needs redesign." Six participants is enough to raise a strong flag, not enough to characterise the discovery rate with precision.

### Pitfalls checked

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim names a specific observable (noticing the filter button), a specific condition (without being prompted), and a specific count. It's not a label like "filter is confusing" — it's a behavioural count. |
| P-02 Context Blindness | No | No prior research is referenced in the study record, and none is declared. Flagging this would require knowing prior work exists; nothing in the record suggests it does. If the team has prior discoverability research on this surface, that should be checked, but it's not a defect in the claim as submitted. |
| P-03 Transcript Literalism | No (with a caveat) | The claim is a count of stated non-discovery, which the transcripts support directly. The caveat is that *downstream* claims built on this finding (e.g., "the button needs to move") would benefit from a researcher's read on whether non-discovery looked like genuine not-seeing-it versus seeing-it-and-dismissing-it. For the literal count under review, the transcripts are sufficient. |
| P-04 Volume Mistaken for Strength | No | Six moderated sessions is a single source type, which would normally argue for discounting confidence. But the claim is scoped to exactly that source — "5 of 6 participants" — not generalised to "users" at large. The verdict is strong *for the claim as stated*. If the claim were rewritten as "users don't notice the filter button," P-04 would fire hard. |
| P-05 Counter-Evidence Filed, Not Faced | No | INT-06 is the counter-signal, and the claim faces it directly by including it in the denominator ("5 of 6," not "participants"). The counter is in the count, not filed off to the side. |
| P-06 Formulaic Transfer Hedge | No | No transfer claim is made — the finding is scoped to the study participants. |
| P-07 Trust Without Process | No | The verdict is a count; the reasoning is the count. Reconstruction is trivial. |
| P-08 Narrowing Sold as Resolving | No | The claim doesn't assert a fix or a cause — it describes a behaviour. A reader could overreach from here (e.g., "move the button and the problem is solved"), but the claim itself doesn't. |

### What would change this verdict
The claim as written is well-evidenced; nothing would meaningfully change it short of discovering that the transcripts were misquoted. What would change the *usefulness* of this finding for the redesign decision is one of:
- A quick check on whether the task framing drew attention away from the filter's location (if so, the discovery rate in realistic use may differ from 5-of-6).
- Live analytics on filter engagement, if available, as an independent corroboration.

### Tacit-knowledge prompt
For INT-03 and INT-04 specifically: did their non-discovery look like the filter was in a blind spot (eye-tracking-style — never looked there), or like they looked near it and didn't register it as a filter control? Those two patterns point at different redesign responses (move it vs. restyle it), and the transcripts don't distinguish between them.

---

**One meta-note on this QA pass:** this is an unusually clean claim to review — a direct, scoped, numerical count against six short transcripts that all contain the relevant statement. The adversarial posture this skill applies by default didn't surface a real defect, and I want to flag that honestly rather than manufacture one. If the claim under review were instead "the filter button is undiscoverable" or "users can't find filters," several pitfalls would fire; the discipline of scoping the claim to "5 of 6 participants in this study" is what makes it hold up.
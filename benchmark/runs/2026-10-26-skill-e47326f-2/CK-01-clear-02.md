## Finding: "Our founder has always said dark mode matters, and INT-01 and INT-03 both show users actively seeking it out — we should ship it as the default theme."

**Evidence strength: WEAK**
The evidence supports that *some* users want dark mode available; it does not support shipping it as the default theme, and the founder's long-standing opinion is not evidence at all — it's the belief under test.

### Provenance
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| Founder has said dark mode matters since launch | B-01 rationale ("authority", no source_ref) | Observed (that the founder said it) | Partially — the statement is recorded, but there's no evidence attached to *why* the founder believes it |
| INT-01 wants dark mode | INT-01 quote (evening use, eye strain) | Observed | Yes |
| INT-03 wants dark mode | INT-03 quote (seeks toggle on install) | Observed | Yes |
| Users are "actively seeking it out" (as a general pattern) | Generalisation from 2 interviews | Inferred | Weakly — 2 units, same source type |
| Dark mode should ship **as the default theme** | Not cited anywhere | Inferred (and a leap) | **No** — nothing in the evidence speaks to default vs. opt-in |

The jump from "two users want it available" to "ship it as the default" has no supporting evidence at all. Neither INT-01 nor INT-03 says they want dark as the *default* — INT-01 switches to it in the evening (implying light is fine during the day), and INT-03 looks for a *toggle* (implying opt-in).

### Falsification pass
- **Strongest counter-hypothesis:** Users want dark mode *available as a toggle*, not as the default. INT-01's "every evening" and INT-03's "look for a toggle" both actively point this direction. A dark default could annoy the majority of users who never asked for it and are accustomed to light UI.
- **What would overturn the "ship as default" claim:** Usage data showing most users who have dark mode available keep it on all day, or survey/interview data where users explicitly say they'd prefer dark as the starting state. Neither exists in this evidence set.
- **Where the evidence underdetermines the claim:** Everything about defaults. Also: no evidence about what proportion of the user base cares at all — 2 interviews cannot speak to prevalence. The design lead's dissent in B-01 (wanting usage data) is pointing at exactly this gap and should not be waved off.

### Pitfalls checked

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim is specific (ship as default theme), even though it's unsupported. |
| P-02 Context Blindness | **Yes** | The belief register records explicit dissent from the design lead ("wants usage data before treating it as settled"). The claim proceeds as if that dissent doesn't exist. Also: no study record is declared, so there's no prior research baseline — the synthesis treats 2 interviews as sufficient without saying so. |
| P-03 Transcript Literalism | No | Not the primary issue here; the quotes are short but the problem is overreach, not over-trusting tone. |
| P-04 Volume Mistaken for Strength | **Yes** | Two interview units, same source type (interviews), being treated as corroboration. INT-01 and INT-03 are one signal repeated, not two independent angles. No reviews, analytics, support tickets, or survey data are cited. |
| P-05 Counter-Evidence Filed, Not Faced | **Yes** | The design lead's dissent is recorded in the belief register and then entirely ignored in the claim. It's filed, not faced. Also: INT-01's "every evening" is itself counter-evidence to the default-theme claim and gets re-used as supporting evidence instead. |
| P-06 Formulaic Transfer Hedge | No | No transfer claim is being made. |
| P-07 Trust Without Process | **Yes** | "Our founder has always said" is cited as if it were evidence. It's not — it's the belief being tested (B-01, source_type: authority, confidence: high, rationale: "founder has said so"). Using the belief to justify itself is circular. |
| P-08 Narrowing Sold as Resolving | **Yes** | Even if we granted "users want dark mode available" (narrowing), the claim jumps to "ship as default" (resolving). Those are different decisions and the evidence only speaks to the first. |

### What would change this verdict
Usage data from a dark-mode toggle in production — specifically, the proportion of users who enable it and whether they keep it on across time-of-day. That single piece of evidence would separate "available as toggle" from "default theme" and would also address the design lead's explicit request. Short of that, a survey question asking users to choose between light-default, dark-default, and system-default would resolve the specific claim being made.

### Tacit-knowledge prompt
To whoever ran INT-01 and INT-03: did either participant say anything — in a moment that didn't make it into the quote above — about whether they'd want dark mode to be *on by default* when they first open the app, versus a toggle they switch to themselves? The quotes as written point toward toggle behaviour (INT-01 "switches to it in the evening"; INT-03 "looks for a toggle"), but a session moment could clarify whether that's genuinely their preference or just how they described current workarounds.

---

**Summary for the register:** B-01 should not be upgraded on the basis of this evidence. The two interviews support a weaker and different claim ("some users want dark mode available as a toggle"), and the design lead's dissent is the correct position given what's actually in the evidence set. The founder's stated belief remains an untested authority claim, not a validated finding.
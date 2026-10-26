## Finding: "Our founder has always said dark mode matters, and INT-01 and INT-03 both show users actively seeking it out — we should ship it as the default theme."

**Evidence strength: WEAK**
The evidence supports that *some* users like dark mode and seek it out — it does not support making it the default theme for all users.

### Provenance

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| Founder has always said dark mode matters | Not cited — founder opinion, no research evidence | Neither (external assertion) | No — founder belief is not user evidence |
| INT-01 actively seeks dark mode | INT-01: "I switch to dark mode every evening without being asked" | Observed | Yes |
| INT-03 actively seeks dark mode | INT-03: "First thing I do after installing any app is look for a dark mode toggle" | Observed | Yes |
| Users (generally) actively seek dark mode | INT-01, INT-03 | Inferred — generalised from n=2 | Partially — the two cited participants do, extension beyond them is not supported |
| We should ship dark mode as the default theme | Not cited | Inferred — and the inference is a leap | No — nothing in the evidence speaks to defaults, only to the existence of a toggle |

Two independent claims in the recommendation have no evidence behind them: that the founder's long-standing opinion is a user-research signal (it isn't — it's a prior belief), and that dark mode should be the *default* (the evidence shows users want it *available*, which is a different product decision).

### Falsification pass
- **Strongest counter-hypothesis:** The two cited quotes support shipping dark mode as a *toggleable option*, not as the default. INT-01 "switches to" dark mode (implying the current default is light and they change it); INT-03 looks for a "toggle" (implying they expect to opt in). Both quotes are, if anything, evidence *against* dark-default — they describe behaviour that assumes a light default with dark available.
- **What would overturn this finding:** Evidence from a representative sample of the actual user base showing majority preference for dark-at-install, OR analytics from a comparable product showing dark-default improves a key metric. Neither exists here.
- **Where the evidence underdetermines the claim:** Everything beyond "at least two interviewees like dark mode and seek the toggle." The evidence base is n=2, single-source (interviews only), and silent on defaults, on the rest of the user population, on time-of-day usage patterns, and on whether light-mode users would be harmed by the switch.

### Pitfalls checked

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim is specific (ship dark mode as default) — the problem is evidence, not vagueness |
| P-02 Context Blindness | Partial | The founder's long-standing belief is cited as if it were corroborating evidence. It isn't — it's a prior that the research should test, not confirm. If prior research on theme preference exists, it isn't referenced. |
| P-03 Transcript Literalism | Yes | Both quotes contain structural hints (INT-01 "switches to" — from what?; INT-03 "looks for a toggle" — expects opt-in) that argue *against* dark-default. The synthesis reads the text for sentiment ("they like dark mode") and misses what the behavioural language implies about defaults. |
| P-04 Volume Mistaken for Strength | Yes | n=2, single source type (interviews), and the recommendation is stated with confidence sufficient to justify a default-theme change. Two interviews is one data point about enthusiasts, not a signal about the user base. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence was raised to be filed — the real failure is that counter-evidence inside the quotes themselves (the "switch" and "toggle" language) was never engaged with at all. |
| P-06 Formulaic Transfer Hedge | No | No transfer hedge is made; the recommendation is unhedged. |
| P-07 Trust Without Process | Yes | The recommendation ("ship as the default theme") is asserted, not derived. There is no reasoning chain from "two users seek a toggle" to "default for all users" — the leap is unargued. |
| P-08 Narrowing Sold as Resolving | Yes | The evidence narrows the hypothesis space to "dark mode has some demand" and is then presented as resolving a product decision ("ship as default"). Narrowing ≠ resolution. The evidence identifies dark mode as worth investigating further; it does not demonstrate that default-dark is the right choice. |

### What would change this verdict
A representative preference signal — either (a) survey data from the actual user base on default theme preference at install, or (b) analytics from a dark-default rollout experiment (even a small one) showing retention, session length, or satisfaction improves vs. light-default. Absent either, the defensible recommendation is "ship dark mode as a toggleable option," which the current evidence *does* support.

### Tacit-knowledge prompt
In the INT-01 and INT-03 sessions, did either participant say anything about what they expect when they first install an app — specifically, whether they'd want dark to be on by default, or whether the act of toggling it themselves is part of what they like? Both quotes use language ("switch to," "look for a toggle") that implies they expect to opt in, and it would help to know whether that was explicit or just phrasing.

---

**Meta-note on the review itself:** The claim bundles three separable things — a founder opinion, a user-evidence summary, and a product recommendation — into one sentence, which is itself a reasoning smell. In a cleaner synthesis these would be stated separately so each could be evaluated on its own merits. Flagging because it's the kind of structural issue that lets weak recommendations hide inside stronger-sounding summaries.
## Finding: "Our users want dark mode — the PM says everyone she's spoken to prefers it, so we should ship it as the default."

**Evidence strength: WEAK**
There is no cited research behind this claim — only a secondhand, informal report of unspecified conversations. It cannot support a product decision as consequential as changing the default theme.

### Provenance

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "Our users want dark mode" | Not cited — attributed to the PM's conversations | Inferred | No — no transcripts, notes, counts, or participant descriptions provided |
| "Everyone she's spoken to prefers it" | PM's verbal report | Inferred (reported, not observed by the synthesis) | No — "everyone" is unquantified; no sampling frame given |
| "We should ship it as the default" | Recommendation stated in the claim | Inferred | No — no evidence links preference strength to a default-setting decision |

Every substantive claim in this finding is unsupported by any cited evidence. The PM's report may be real, but it is not research — it has no documented participants, no method, no record, and no way to audit who was asked, how, or what they actually said.

### Falsification pass

- **Strongest counter-hypothesis:** The PM has been speaking to a self-selecting slice of users — likely engaged, likely technical, likely vocal — whose stated preference for dark mode does not generalise to the broader user base. Dark-mode preference is a well-known case where enthusiast populations diverge sharply from mainstream ones, and changing the *default* (as opposed to offering the option) is the decision most sensitive to this skew.
- **What would overturn this finding:** A representative preference signal — e.g. an in-app survey across the active user base, A/B test data on theme-switch behaviour when both are offered, or analytics on current OS-level dark-mode adoption among the user base. Even a documented list of who the PM spoke to and what they said would be a start.
- **Where the evidence underdetermines the claim:** Everywhere. The evidence is a secondhand summary of unspecified conversations. It cannot distinguish between "a strong, representative preference" and "a vocal minority the PM happens to hear from."

### Pitfalls checked

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "Users want dark mode" is a label, not a behaviour. No trigger, no context, no observable action. The sentence would read identically in a report about any product. |
| P-02 Context Blindness | Yes | No reference to prior research, existing analytics (OS theme settings, current theme-toggle usage), or any established knowledge about this user base. The claim is presented as if discovered fresh. |
| P-03 Transcript Literalism | No (but adjacent) | There is no transcript to be literal about — the problem is more severe: there is no record at all. Flagging for completeness: the PM's recollection is itself a lossy transcript of conversations we can't audit. |
| P-04 Volume Mistaken for Strength | Yes | "Everyone she's spoken to" treats repetition within a single, unsampled source (the PM's conversational circle) as strength. Ten people from the same slice is one signal repeated ten times. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence is named — which is itself a problem, but a different one. The claim doesn't file counter-evidence; it ignores that counter-evidence could exist. |
| P-06 Formulaic Transfer Hedge | No | No hedge is present. The claim is unhedged, which given the evidence base is arguably worse. |
| P-07 Trust Without Process | Yes | The verdict "we should ship it as the default" is asserted without any derivation. There is no reasoning chain between "PM heard preferences" and "change the default for everyone" — the leap from informal preference to product default is the entire decision, and it's unspoken. |
| P-08 Narrowing Sold as Resolving | Yes | Even if the preference signal were real, "users prefer dark mode" would narrow the question (people like the option) — it would not resolve "should it be the default?" Preference-when-asked and default-setting are different decisions; the claim conflates them. |

### What would change this verdict

A representative measurement of theme preference across the active user base — ideally an in-app survey or A/B test — distinguishing between (a) wanting dark mode available, (b) preferring it when switched to, and (c) wanting it as the default. Current analytics on OS-level dark-mode settings among users would be a cheap first signal. Without one of these, the claim cannot move off WEAK regardless of how many more conversations the PM has.

### Tacit-knowledge prompt

Ask the PM directly: *Who specifically have you spoken to about this, roughly how many, and in what setting? Were you asking about dark mode specifically, or did it come up unprompted? And did anyone express a preference for light mode or no strong preference — or is the "everyone" claim literally everyone?* The answers will usually reveal the sampling problem on their own, without needing to run new research.

---

**Summary for the stakeholder:** This isn't a research finding — it's a hallway conversation being treated as one. Shipping a default-theme change on this basis is a decision the current evidence cannot support. The right next step is not "argue with the PM" but "get a representative signal," which is cheap and fast for a question like this.
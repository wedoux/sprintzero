## QA Readout

```
QA Progress:
- [x] Step 1: Confirm there's a conclusion to evaluate (not raw notes)
- [x] Step 2: Provenance pass — trace every claim to evidence
- [x] Step 3: Falsification pass — try to break each conclusion
- [x] Step 4: Pitfalls check — screen against references/pitfalls.md
- [x] Step 5: Produce the readout using templates/readout.md
```

A note before the readout: this QA pass is cleanest when run in a fresh conversation with only the synthesis and the underlying evidence pasted in — a model reviewing its own prior output grades its own homework. In this case there's no prior turn to worry about, so proceeding.

---

## Finding: "Early signal suggests some users may prefer voice input over typing; more sessions are needed to confirm."

**Evidence strength: WEAK**

The finding is a defensible hedge, but it's doing almost no work: it restates what two people said, labels it an "early signal," and defers to future research without specifying what that research would need to show. The underlying evidence is thin and single-sourced, and the finding neither commits to a position nor sharpens the question.

### Provenance

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "Some users may prefer voice input over typing" | INT-01 ("I'd rather just say it out loud than type it"), INT-02 ("Talking is faster for me than hunting for the keyboard") | Observed (self-reported preference, not observed behaviour) | Yes |
| "Early signal" | — | Inferred (characterisation of n=2 as a signal) | No — the characterisation is asserted, not derived |
| "More sessions are needed to confirm" | — | Inferred | Yes, trivially — but what the sessions should test is not specified |

Note the gap between what the participants actually said and what the finding claims. INT-01 states a preference ("I'd rather"). INT-02 gives a reason ("talking is faster for me"). Neither has been observed using voice input or typing in context; both are stated preferences in what appears to be an interview setting, with no task, no comparison, and no friction data.

### Falsification pass

- **Strongest counter-hypothesis:** Both participants are describing a context-specific preference (e.g., when their hands are busy, when composing short messages, when the keyboard is physically awkward) rather than a general preference for voice over typing. INT-02's phrasing — "hunting for the keyboard" — specifically suggests a situational friction (perhaps mobile, perhaps a device without a ready keyboard) rather than a modality preference. The finding generalises past what either quote supports.
- **What would overturn this finding:** Observed behaviour showing these same users typing when voice was available, or interview follow-ups revealing the preference is conditional on context the finding doesn't name. Even one such instance would reframe this from "preference for voice" to "preference for voice in [specific condition]."
- **Where the evidence underdetermines the claim:** Almost everywhere. We don't know what task they were considering, what device, what alternative, what the friction with typing actually is, or whether their stated preference matches their actual behaviour. The evidence supports "two people said they prefer voice in some unspecified context" and not much more.

### Pitfalls checked

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | **Yes** | "Users prefer voice input over typing" has no trigger (when? what task?) and no consequence (what should the team do?). Swap "voice input" for any other feature preference and the sentence reads identically. The finding is a label, not a behaviour. |
| P-02 Context Blindness | No (with caveat) | No prior research is declared, so this can't be checked. Worth flagging to the researcher: is voice-vs-typing preference something the team has studied before? If so, this finding should reference it. |
| P-03 Transcript Literalism | **Yes** | Two short quotes are being treated as the full picture. A researcher who ran these sessions almost certainly knows what prompted each statement — what the participant was doing, what they were comparing against — and none of that context is in the finding. |
| P-04 Volume Mistaken for Strength | **Yes** | Two interviews, same source type, both self-reported preference (no behavioural corroboration, no analytics, no secondary channel). The finding correctly hedges with "early signal," but doesn't name the single-source problem — it implies the weakness is just about sample size, when it's also about source homogeneity. |
| P-05 Counter-Evidence Filed, Not Faced | No | There's no counter-evidence in the set to face. |
| P-06 Formulaic Transfer Hedge | **Yes** | "More sessions are needed to confirm" is exactly the decorative hedge this pitfall names. It sounds rigorous but argues nothing: it doesn't say what the sessions should test, what population they should sample, or what result would change the verdict. Replace "voice input" with any other topic and the sentence still works. |
| P-07 Trust Without Process | **Yes** | "Early signal suggests" is the conclusion, not the reasoning. The finding doesn't explain *why* two matching quotes constitute a signal rather than noise, or what the threshold for "signal" is. The reader can agree or disagree with the label but can't audit the thinking. |
| P-08 Narrowing Sold as Resolving | No | The finding doesn't claim to resolve anything, so this doesn't apply. |

### What would change this verdict

One piece of context from the researcher: **what task or situation prompted each of these statements?** If both participants were describing the same context (e.g., composing messages while walking), the finding could be sharpened to a specific, testable claim: "Users prefer voice input to typing when [X]." If the contexts were different, the two quotes probably shouldn't be grouped as the same signal in the first place. Either outcome is more useful than the current hedge.

### Tacit-knowledge prompt

For the researcher who ran INT-01 and INT-02: in each session, what was the participant actually doing or imagining doing when they expressed the preference? Specifically — was INT-02's phrase "hunting for the keyboard" about a particular device or situation (mobile, car, hands occupied), or a general statement about typing? That one detail probably determines whether this is a modality finding or a context finding, and they're very different things for a product team.
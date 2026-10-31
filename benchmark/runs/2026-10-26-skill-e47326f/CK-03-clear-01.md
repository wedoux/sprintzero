## Finding: "4 of 5 participants completed checkout without help."

**Evidence strength: UNCERTAIN**
The headcount itself is likely accurate as a description of the sessions, but as a *finding* it's underspecified — we don't know what "completed" or "without help" mean operationally, and a 5-person sample with no context cannot carry much weight on its own.

### Provenance
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| 4 of 5 participants completed checkout | INT-01 through INT-05 session recordings | Observed | Partial — the evidence line asserts "checkout completion observed" but doesn't define what counted as completion, nor which participant was the exception |
| Completion was "without help" | INT-01 through INT-05 session recordings | Inferred | No — the evidence line mentions completion was observed; it does not say whether help was offered, requested, declined, or whether the sessions were moderated at all |

The "without help" qualifier is doing significant work in this claim and has no cited support. If the sessions were unmoderated, "without help" is trivially true for everyone and uninformative. If they were moderated, we need to know what the moderator did or didn't do.

### Falsification pass
- **Strongest counter-hypothesis:** Participants completed checkout *despite* struggling — e.g. with long hesitations, visible confusion, or workarounds — and "completed without help" compresses a messy behavioural picture into a clean binary. The 1 of 5 who didn't complete may also be the most informative session, and this framing buries them.
- **What would overturn this finding:** Time-on-task data, error counts, or qualitative notes from the recordings showing that "completion" involved substantial friction; or confirmation that sessions were moderated and help was in fact offered and declined/accepted in ways the headline doesn't capture.
- **Where the evidence underdetermines the claim:** We have no definition of "completed" (reached confirmation screen? submitted payment? abandoned cart recovered?), no definition of "without help" (unmoderated? moderator present but silent? help requested and refused?), and no information about the one participant who didn't complete — which is often the most diagnostic case in a 5-person study.

### Pitfalls checked

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | **Yes** | "Completed checkout without help" is a surface label, not a behaviour. No trigger, no consequence, no specific action a team could do differently based on this. Would read identically in a report about any checkout flow. |
| P-02 Context Blindness | No (cannot assess) | No prior research declared in the study record. Flagging that we have no visibility into whether this confirms, contradicts, or re-discovers prior work. |
| P-03 Transcript Literalism | **Yes** | The claim treats the recordings as yielding a clean binary (completed / didn't; helped / unhelped) when session recordings carry hesitation, body language, verbal frustration, and moderator micro-interventions that a headcount erases. |
| P-04 Volume Mistaken for Strength | **Yes** | n=5, single source type (session recordings only). "4 of 5" has the shape of a statistic but is one source of signal with a sample too small to generalise from. If this were presented as STRONG evidence that checkout works, that would be overreach. |
| P-05 Counter-Evidence Filed, Not Faced | **Yes** | The 1 of 5 who didn't complete is counter-evidence to a "checkout works" reading, and the framing files it ("4 of 5...") without facing it. What happened in that session? |
| P-06 Formulaic Transfer Hedge | No | No transfer claim is being made. |
| P-07 Trust Without Process | **Yes** | The claim is an assertion of outcome with no reasoning for why these 5 participants, this task, or this definition of "completion" supports whatever downstream conclusion is implied. Reader cannot audit how "completed" or "without help" were operationalised. |
| P-08 Narrowing Sold as Resolving | No (not yet) | Would fire if this finding were used to claim "checkout is not a problem" — but as stated it doesn't make that leap. Watch for it in the next step. |

### What would change this verdict
Two things, in order:
1. **A definition of the terms.** What specifically counted as "completed"? Was the session moderated, and if so, what was the moderator's protocol around help? Without this, the finding is uninterpretable regardless of the headcount.
2. **The 5th participant's session.** What happened? A single failure in n=5 is 20% of the sample and is almost certainly where the actionable signal lives.

### Tacit-knowledge prompt
For the one participant who didn't complete: was there a specific moment — a page, a field, a decision — where you could see them disengage or get stuck? And for the four who did complete: did any of them show behaviour (long pauses, repeated clicks, backtracking, verbal frustration) that the "completed without help" summary doesn't capture?

---

**Overall note to the user:** This "finding" is really a descriptive statistic from a usability session, not a synthesised insight. Before QA-ing it further, it's worth asking what conclusion this number is meant to support — "checkout is working" is a very different claim from "checkout needs no further investigation," and the evidence here supports neither without more context.
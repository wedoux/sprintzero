I'll run the QA pass on the claim "Users want a subscription model" against the three interview excerpts provided.

**Progress:**
- [x] Step 1: Confirm there's a conclusion to evaluate — yes, there's a stated finding
- [x] Step 2: Provenance pass
- [x] Step 3: Falsification pass
- [x] Step 4: Pitfalls check
- [x] Step 5: Readout

---

## Finding: "Users want a subscription model."

**Evidence strength: WEAK**

Three interviewees expressed openness to subscriptions, but each framed it as *conditional on an alternative they dislike* (ads, in-app purchases) — not as a positive preference for subscription as a model. The claim as written overreaches the evidence in several directions at once.

### Provenance

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| Users want a subscription model | INT-01, INT-02, INT-03 | Inferred — and the inference is shaky | Partially — see below |
| INT-01 would accept a subscription | INT-01: "I'd pay a flat monthly fee if it meant no ads." | Observed, but *conditional on removing ads* — this is an anti-ads preference, not a pro-subscription preference | Yes |
| INT-02 is comfortable with subscriptions | INT-02: "Subscription makes sense to me, I already do it for two other apps." | Observed — closest to a genuine subscription preference, though "makes sense" ≠ "wants" | Yes |
| INT-03 prefers subscription | INT-03: "I'd rather subscribe than deal with in-app purchases." | Observed, but framed as the lesser of two evils vs. IAPs — not a positive want | Yes |
| "Users" (the generalisation) want this | — | Inferred from n=3 self-selected speakers | No — the leap from three quotes to "users" has no supporting evidence |

The word "want" in the finding is doing heavy lifting that none of the three quotes actually support. Two of the three speakers are expressing a *preference-against-something-else*, not a *preference-for-subscription*.

### Falsification pass

- **Strongest counter-hypothesis:** Users don't want a subscription model — they want *not to see ads* and *not to deal with IAPs*. Subscription is the only alternative monetisation model that was named or implied in the interview framing, so it appears to "win" by default. A one-time purchase, a freemium tier, or an ad-free upgrade could plausibly score the same or better with the same three people.
- **What would overturn this finding:** Evidence that these same participants, when offered a choice between subscription and a one-time purchase (or any non-subscription ad-free option), still chose subscription. None of the three quotes rule this out.
- **Where the evidence underdetermines the claim:** We have no information about (a) how the question was framed to elicit these answers, (b) what alternatives were presented, (c) price sensitivity, (d) what categories of app these people subscribe to or whether this app is similar, (e) how many interviewees were asked and *didn't* say this, or (f) anything about the broader user base.

### Pitfalls checked

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | **Yes** | "Users want a subscription model" is a label, not a behaviour. No trigger (when do they want it?), no consequence (vs. what alternative, at what price?), no observable action. The sentence would read identically in a report about any app. |
| P-02 Context Blindness | Can't assess | No belief register or prior study record was provided. Flagging this as a gap: if the team has prior pricing research, this finding should reference it. |
| P-03 Transcript Literalism | **Yes** | These are three one-line quotes stripped of context. We don't know what question preceded them, what alternatives were on the table, or whether the interviewer led. A researcher who ran the sessions almost certainly knows things these quotes don't capture. |
| P-04 Volume Mistaken for Strength | **Yes** | Three units from a single source type (interviews). Even if we accepted every quote at face value, n=3 interviews is one source, not three independent corroborating angles. STRONG-sounding language ("users want") is not warranted. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence was presented — but this is itself suspicious. A clean three-for-three result from three interviews, with no dissent noted, suggests either very narrow sampling or counter-signals that weren't surfaced. |
| P-06 Formulaic Transfer Hedge | No | No transfer claim is being made. |
| P-07 Trust Without Process | **Yes** | The finding is asserted ("users want a subscription model") with no visible reasoning connecting the three quotes to the conclusion. The leap from "three people said subscription-adjacent things" to "users want this" is not argued, it's just made. |
| P-08 Narrowing Sold as Resolving | **Yes (mild)** | If this finding is being used to justify "ship a subscription model," that's a causal claim (subscription will succeed) resting on investigative-strength evidence (three people didn't object to the idea). The evidence supports "investigate subscription as a monetisation option worth testing," not "users want it." |

### What would change this verdict

A forced-choice question — ideally in a survey with a larger n, or at minimum in follow-up interviews — presenting participants with **multiple** monetisation models (subscription, one-time purchase, freemium, ad-supported free) and asking them to rank or choose. If subscription still wins when a non-ad, non-IAP alternative is available, the finding gets meaningfully stronger. Without that, the current evidence is consistent with "users want anything that isn't ads or IAPs."

### Tacit-knowledge prompt (if a researcher who ran these sessions is available)

For INT-01 and INT-03 specifically: when they framed subscription as better than ads (INT-01) or better than IAPs (INT-03), did you probe on what they'd prefer if a one-time purchase or ad-free upgrade were available? And were any interviewees asked about monetisation who *didn't* endorse subscription — if so, what did they say, and why aren't they in this evidence set?

---

**Summary for the decision-maker:** This finding should not drive a monetisation decision in its current form. The evidence supports a narrower, investigative claim — "subscription is worth testing against other non-ad, non-IAP models" — not the stated claim that users want it.
I'll run the QA pass on this. Before I do — a note on the setup:

You've declared no belief register and no study record. That's your call to make, but it means several checks can't run (CK-01 part a, CK-02, CK-04, CK-06). If you want those to run, see `templates/belief-register.md` and `templates/study-record.md` and write your own — I won't draft them for you, because beliefs and research questions are only useful when written by the people who hold them. I can ask questions that help you get started if you'd like.

Proceeding with what's here.

---

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "Users want a subscription model."

**Evidence strength:** WEAK
Three interviewees said something favourable about subscriptions; the claim generalises this to "users" and treats a stated preference as a want.

**Claim matches its evidence:** No — the claim is scoped to "users" (all of them) when the evidence covers three people, and it asserts a want when the evidence shows stated willingness in a conversation. CK-05 fires; P-01 is triggered.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** These three participants are agreeing with a frame the interviewer put in front of them. People routinely say they'd pay for things in interviews and don't, when asked to. The evidence is consistent with "three people reacted positively when subscriptions came up" and gives us no way to tell that apart from a genuine preference.
- **What would overturn this finding:** Behavioural evidence — conversion rates on a subscription offer, or churn from an existing one. Or interview evidence where participants raised subscriptions unprompted, rather than responding to them. Or any participant who pushed back.
- **Where the evidence underdetermines the claim:** We don't know what question was asked, whether subscriptions were introduced by the participant or the interviewer, what the alternatives were (ads? one-off purchase? free?), or how many people were spoken to in total. If these are three excerpts from three interviews, that's a signal. If they're three excerpts from thirty, that's close to the opposite.

**Counter-evidence:** None present in the material — which is itself worth flagging. Three quotes all pointing the same way, with no dissent and no "well, but…", is unusually clean and should lower confidence, not raise it (see P-04).

**Unsupported claims:** The jump from "three people said favourable things about subscriptions" to "users want a subscription model" is unsupported by the evidence provided. "Want" is also stronger than any of the quotes — INT-01 says "I'd pay if…", INT-02 says it "makes sense", INT-03 states a preference between two options. None of these are expressions of active want.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim is not presented as validated or proven; it's asserted, which is a different problem (caught by CK-05 / P-01). | n/a |
| CK-04 Product finding without a human story | CLEAR | Not a product claim — it's a claim about people (what users want). | n/a |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." Triggering text: *"Users want a subscription model."* Scope: 3 interviewees → "users". Certainty: stated willingness in an interview → "want". | n/a (no declared record to conflict with; the gap is between claim and evidence) |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "Users want a subscription model" is a label, not an observable behaviour. No trigger, no consequence, no specific decision it points at. Swap "subscription model" for almost any monetisation choice and the sentence reads the same. |
| P-03 Transcript Literalism | Yes | The quotes are treated as the complete record. We don't see what was asked, what tone was used, or whether participants hesitated. "I'd pay a flat monthly fee if it meant no ads" is a conditional, and the condition (no ads) is doing real work in that sentence — the finding drops it. |
| P-04 Volume Mistaken for Strength | Yes | Three evidence units, all the same source type (interviews), all pointing the same way, no dissent. This is one signal expressed three times, not three independent signals. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence is listed and dismissed — the problem here is that none was sought or surfaced, which is a different failure (sits under P-04 and the falsification pass). |
| P-08 Narrowing Sold as Resolving | No | No narrowing claim is made. |

### Where does it apply?

**Scope:** The evidence covers three interview participants. We don't know who they are, how they were recruited, what product context they were asked about, or what proportion of the sample they represent. The claim covers "users" with no scope at all.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no `cannot_claim` to check against. If limits had been declared (e.g. "sample: three paying app users in the US"), this check would almost certainly fire. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim being made (and no hedge either, which is part of the problem — the claim transfers silently from 3 people to all users). |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| Users want a subscription model | INT-01, INT-02, INT-03 | Inferred (heavily — the claim is much broader and stronger than any single quote) | Partially — the quotes are cited, but the leap from them to the claim is not argued |

**Checked against:** Nothing declared. There is no belief register to tell us whether this finding confirms a prior belief or contradicts one, and no research questions to tell us whether this is what the study set out to learn or an unexpected finding.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No questions declared, so can't check whether the finding answers one or is unexpected. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | Unknown | Can't assess — no prior research declared. If subscription appetite has been studied before (either internally or in the category), this finding doesn't reference it. Worth checking before anyone acts. |
| P-07 Trust Without Process | Yes | The finding states a conclusion with no reasoning. We don't see how the researcher got from three favourable quotes to "users want a subscription model" — the inference is just asserted. If I only saw the finding and not the quotes, I couldn't reconstruct the argument. |

### Is it theirs or ours?

**Beliefs and evidence:** All three quotes are from participants, so what's here is theirs. But without a belief register, we don't know whether "users want subscriptions" was something the team already believed before the study — in which case the three favourable quotes may have been given more weight than contradicting signal (if any existed), or sought out in the interview itself. This is unknowable from the material.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | Part (a) can't run without a belief register. Part (b) doesn't fire — the support is participant quotes, not attributed opinion ("the PM says…"). But the possibility that this was a pre-existing belief looking for confirmation can't be ruled out. | n/a |

### Tacit-knowledge prompt
Two specific questions, if the researcher who ran the sessions is available:
1. In each of INT-01, INT-02 and INT-03, who introduced the word "subscription" — the participant or you? If it came from the interview script, these quotes are reactions to a frame you offered, not spontaneous preferences.
2. How many interviews were in the full set, and did anyone express hesitation about subscriptions, prefer ads, or push back on paying at all? Three favourable quotes with no counter-signal is the shape of a selected sample, not a conclusive one.

### Decision boundary
- **Supports:** Three interview participants reacted favourably when subscriptions came up, with specific conditions (no ads, familiarity with other subscription apps, preference over in-app purchases). That's a signal worth following up.
- **Doesn't support:** That "users" (plural, generic) "want" (active preference, not conditional willingness) "a subscription model" (undifferentiated from any specific offer). None of those three generalisations survive contact with the evidence.
- **What would close the gap:** The simplest useful next step is to look at the full interview set these three came from. If they're 3 of 3, the finding is early but intact; if they're 3 of 20 with the other 17 saying something different, the finding changes shape entirely. Second-best: a small test — put a subscription offer in front of users and measure conversion.

**Safe to act on:** Not yet — the claim says much more than three favourable interview quotes can support, and three of three key checks couldn't run because nothing was declared upstream. Treat this as a hypothesis worth testing, not a finding to build on.
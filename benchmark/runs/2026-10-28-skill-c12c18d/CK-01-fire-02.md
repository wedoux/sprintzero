I'll run the QA pass on this claim. First, let me walk through the workflow transparently.

## Workflow progress

- [x] Step 0: Gather declarations — **none declared** for either register
- [x] Step 1: Confirm there's a conclusion to evaluate — yes, a shipping recommendation
- [x] Step 2: Provenance pass — no evidence cited
- [x] Step 3: Falsification pass — see below
- [x] Step 4: Pitfalls check
- [x] Step 5: CK pass
- [x] Step 6: Readout

**Note on declarations.** You've marked both the belief register and the study record as "none declared." That's your call to make, and I'll proceed — but it means several checks can't run. Belief registers and study records are only useful when written by the people who hold the beliefs and asked the questions, so I won't draft them for you. If you want fuller coverage on a future pass, see `templates/belief-register.md` and `templates/study-record.md`.

**Note on conversation hygiene.** If this claim was produced earlier in this same conversation, consider re-running in a fresh conversation with only the claim and evidence pasted in. A model reviewing its own prior output grades its own homework.

---

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "Our users want dark mode — the PM says everyone she's spoken to prefers it, so we should ship it as the default."

**Evidence strength:** WEAK
The claim rests entirely on one person's informal report of unspecified conversations, with no cited evidence from users and no description of how many people, which people, or in what context.

**Claim matches its evidence:** No — the claim generalises from "the PM has spoken to some people" to "our users want" and jumps to "ship as default," which goes well beyond what the stated support shows.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** The people the PM spoke to are a self-selecting subset (likely engaged, likely to voice preferences), and their preference for dark mode in conversation doesn't predict either (a) what the broader user base prefers or (b) what they'd want as a *default* versus an option. Preference for availability ≠ preference as default.
- **What would overturn this finding:** A representative survey or usage data showing most users either don't prefer dark mode, prefer it situationally, or would be disrupted by it being default. Even a count of how many people the PM actually spoke to, and who they were, would materially change the picture.
- **Where the evidence underdetermines the claim:** Almost entirely. We don't know how many people, who they are, whether they're representative, what question they were asked, whether they want it available or want it as the default, or whether any non-PM evidence exists.

**Counter-evidence:** None cited — but the absence of any attempt to look for disconfirming evidence is itself a weakness, not a strength.

**Unsupported claims:** All three component claims are unsupported by cited evidence: (1) "our users want dark mode," (2) "everyone [the PM has] spoken to prefers it," (3) "we should ship it as the default."

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | FIRES | "This treats what we learned about people as proven. Only a product can be validated." The claim states "our users want dark mode" as settled fact about user preference. | n/a (claim-only check) |
| CK-04 Product finding without a human story | NOT RUN | The product recommendation ("ship it as the default") cites no people-side evidence, and no belief register was declared, so I can't check whether an agreed working assumption supports it. | — |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." Scope inflates from "everyone [the PM has] spoken to" (unknown N, unknown selection) to "our users." Certainty inflates from a preference report to a shipping-as-default recommendation. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "Our users want dark mode" is a label, not a behaviour. No trigger, no context, no observable action — the sentence would read the same for any product. |
| P-03 Transcript Literalism | No | No transcript or source text is in play. |
| P-04 Volume Mistaken for Strength | Yes | Even taking the PM's report at face value, it's one source type (informal conversations filtered through one person). No corroboration from an independent angle. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence was raised to be filed or faced — but note this is because none was sought, not because none exists. |
| P-08 Narrowing Sold as Resolving | No | Not the failure mode here. |

### Where does it apply?

**Scope:** Unknown. The claim says "our users" but the stated support covers only "everyone [the PM has] spoken to" — an unspecified group of unspecified size in an unspecified context.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no `cannot_claim` limits to check against. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is being made between populations. |

### Could someone retrace it?

**Provenance**

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "Our users want dark mode" | Not cited | Inferred (from PM's report) | No — no underlying evidence identified |
| "The PM says everyone she's spoken to prefers it" | PM's statement | Observed (that she said it); Inferred (that it's accurate or representative) | No — the PM's conversations are not documented, and the number and identity of people are unknown |
| "We should ship it as the default" | Not cited | Inferred (recommendation drawn from the above) | No — no evidence supports the leap from preference to default |

**None of the three component claims has supporting evidence that someone could retrace.**

**Checked against:** Nothing declared — no beliefs, questions, or limits to check against.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study questions declared, so I can't check whether this finding answers any of them. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | Yes | No reference to prior research on dark-mode preferences, usage patterns, or defaults, and no acknowledgement of whether this question has been studied before — internally or in the industry. |
| P-07 Trust Without Process | Yes | The jump from "PM says people she spoke to prefer it" to "ship as default" is asserted, not argued. No reasoning chain is shown for why conversational preference should determine the default. |

### Is it theirs or ours?

**Beliefs and evidence:** The entire claim traces to the PM's authority. Nothing in it comes from documented participant behaviour or statement. "Everyone she's spoken to" is attributed opinion mediated through one person.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | FIRES (part b) | "This confidence comes from who said it, not from evidence." The support for the claim is "the PM says" — an attributed opinion rather than cited participant evidence. Part (a) can't run because no belief register was declared. | n/a (no declared belief to name) |

### Tacit-knowledge prompt
If the PM is available: *How many people have you spoken to, who are they relative to our broader user base, and did any of them say they'd want dark mode as the default versus as an available option? Did anyone push back or express a different preference?*

### Decision boundary

- **Supports:** That at least some users the PM has encountered have expressed a preference for dark mode. That it's worth investigating further.
- **Doesn't support:** That "our users" broadly want dark mode. That dark mode should be the default (as opposed to available). That shipping it as default would be received well by the user base at large.
- **What would close the gap:** The single most useful next step is a representative signal — either (a) a short in-product survey asking current users their preference between light default, dark default, and system default, or (b) analytics from a soft-launched toggle showing adoption rates. Either would move this from "one person's informal read" to something that could justify a default change.

**Safe to act on:** Not yet — the claim rests on attributed opinion from one person with no documented participant evidence, and jumps from "some people prefer it" to "ship as default" without supporting that leap. Investigating further is reasonable; shipping as default on this basis is not.
I'll run the QA pass on this. First, a note on inputs:

**No belief register, no study record declared.** I'll proceed as the workflow allows, but several checks will report NOT RUN. I'd normally ask once whether these exist — if not, the templates at `templates/belief-register.md` and `templates/study-record.md` are there for you to fill in yourself. The checks that depend on them are only useful when the people who held the beliefs and asked the questions write them down.

Also worth flagging up front: with a single evidence unit and a single claim, this is a very thin pass. The result below is what the checks say, but the real recommendation is "go get more evidence before acting", which you probably already know.

---

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

---

## Finding: "This new icon will increase engagement."

**Evidence strength:** WEAK
One participant said one icon was clearer than (presumably) another. That is a single reaction from a single person about recognisability, not a measurement of engagement.

**Claim matches its evidence:** No — the claim makes a causal, forward-looking prediction about engagement from a single comment about icon clarity.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** INT-01 noticed the icon in a session where they were primed to look at the interface. "Spotted it right away" is about findability in a test setting, not about whether anyone will use the feature more often in real use. Clarity and engagement are different things — a clearer icon could be noticed and still ignored.
- **What would overturn this finding:** Behavioural data showing engagement with the feature behind the icon is flat or lower after the change — or qualitative evidence from other participants that the icon is clear but the feature isn't worth engaging with.
- **Where the evidence underdetermines the claim:** Almost entirely. One quote from one participant about noticing an icon cannot support a claim about engagement across users.

**Counter-evidence:** None supplied — but the absence of corroborating evidence is itself the issue, not a clean bill of health.

**Unsupported claims:** The entire claim. "Will increase" (causal, future-tense) and "engagement" (a behavioural outcome) are both unsupported by a comment about visual clarity.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | Not a claim about people — it's a prediction about a product outcome. | n/a |
| CK-04 Product finding without a human story | FIRES | "This product finding has no evidence about people behind it, and no assumption the team agreed to." The claim is about product impact (engagement). The one piece of people-side evidence (INT-01 on icon clarity) does not speak to engagement, and no belief register exists to supply an agreed working assumption linking clarity to engagement. | No belief register; no evidence unit about engagement behaviour. |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." One person saying an icon is clear becomes a confident prediction ("will increase") about an unrelated outcome (engagement) across all users. | Evidence set is one comment from INT-01 about clarity. |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "Engagement" is a surface label with no behaviour, no trigger, no cost named. Swap the product and the sentence reads identically. |
| P-03 Transcript Literalism | No | The quote is being over-extended, not over-trusted as text. |
| P-04 Volume Mistaken for Strength | Yes | One evidence unit is being used to support a confident forward prediction. Even one source type with ten units would be thin here; one unit is thinner. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence was supplied to face or file. |
| P-08 Narrowing Sold as Resolving | Yes | At best, the quote narrows "is the new icon more findable than the old?" towards yes-for-one-person. It does not resolve "will the product see more engagement?" The claim treats a narrowing signal (clarity) as if it resolved a causal question (engagement). |

### Where does it apply?

**Scope:** Evidence covers one participant's reaction in one session. The claim covers all users and future behaviour. These do not match.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no `cannot_claim` to check against. If limits had been declared, this claim would almost certainly cross them. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer across populations is being claimed or hedged. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| The icon is clearer (to INT-01) | INT-01: "Oh, that's a much clearer icon, I spotted it right away." | Observed | Yes |
| The new icon will increase engagement | Not cited | Inferred (and the inference is a large leap) | No — the leap from "clearer to one person" to "will increase engagement" is nowhere in the evidence. |

**Checked against:** nothing declared. No beliefs, questions or limits exist to check this finding against.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No declared questions. Cannot tell whether this answers one, misses them all, or is an unexpected finding. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | Can't be assessed — no prior research context supplied. |
| P-07 Trust Without Process | Yes | The claim is asserted, not derived. No reasoning chain is shown linking "spotted it right away" to "will increase engagement" — if the reader strips the verdict, they can't reconstruct it. |

### Is it theirs or ours?

**Beliefs and evidence:** INT-01's observation is theirs (one person's). The link from "clearer icon" to "more engagement" is ours — it is not in anything the participant said. Without a belief register, there is no declared working assumption to carry that leap either.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | No belief register declared. Part (b) does not fire on the claim as written (no attributed opinion is cited as support — the problem is that nothing is cited as support for the engagement part). | n/a |

### Tacit-knowledge prompt
If a researcher ran INT-01: was INT-01 comparing the new icon to a specific old one, or reacting in isolation? And did they do anything with the feature behind the icon, or only notice it?

### Decision boundary
- **Supports:** The new icon was noticeable to one participant in a session. That is a small signal that findability may have improved.
- **Doesn't support:** Any claim about engagement, about "users" generally, or about what will happen after the change ships.
- **What would close the gap:** Behavioural data — a before/after look at how often the feature behind the icon is used, ideally with the icon as the only variable changed. If the question is really about findability rather than engagement, more sessions with other participants comparing old and new would do it.

**Safe to act on:** Not yet — one quote about icon clarity cannot support a prediction about engagement, and CK-04 and CK-05 both fire. If the real decision is "ship the clearer icon", that may well be fine on its own merits; but don't ship it expecting an engagement lift this evidence doesn't show.
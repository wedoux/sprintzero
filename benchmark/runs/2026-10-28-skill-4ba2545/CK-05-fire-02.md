I'll run the QA pass on this. First, the setup check.

**On declarations:** You've declared "none" for both the belief register and study record. That's your call — I'll proceed, but several checks will report NOT RUN as a result. If you want a fuller pass, see [templates/belief-register.md](templates/belief-register.md) and [templates/study-record.md](templates/study-record.md). Beliefs and questions are only useful when written by the people who hold them, so I won't draft them for you — but I can ask prompting questions if you want.

**On the material:** This is minimal — one participant quote, one claim. I'll run the checks on what's here.

---

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "This new icon will increase engagement."

**Evidence strength:** WEAK
One participant said one icon was clearer than something unspecified. That is a single reaction to a visual, not evidence about engagement.

**Claim matches its evidence:** No — the claim leaps from "one person spotted an icon" to a causal prediction about aggregate engagement. Three separate overreaches: one person → users in general; "spotted it right away" → "engagement"; past observation → future causal claim ("will increase").

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** INT-01 noticed the icon in a test setting where they were primed to look at the UI; in real use, noticing an icon faster doesn't change whether or how much people use the product. Clarity of an icon and engagement with a product are not the same construct.
- **What would overturn this finding:** engagement metrics (sessions, task completions, return visits) from a cohort using the new icon vs. a cohort using the old one, showing no difference or a drop.
- **Where the evidence underdetermines the claim:** the evidence speaks to perceived clarity for one person at one moment. It says nothing about engagement, nothing about other participants, nothing about behaviour over time.

**Counter-evidence:** none in the material. The absence of counter-evidence here is itself a problem — only one data point was supplied.

**Unsupported claims:** the entire claim beyond "INT-01 found this icon clearer than [something]" is unsupported. "Engagement" is not mentioned in the evidence. "Increase" is not demonstrated. "Will" is a prediction with no basis.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim is about a product outcome (engagement), not a validated claim about people. | n/a |
| CK-04 Product finding without a human story | NOT RUN | There is people-side evidence (INT-01), but it doesn't speak to engagement — so the claim about engagement has no people-side evidence behind it. With no belief register declared, I can't check whether an agreed assumption fills the gap. | n/a |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." One participant saying "I spotted it right away" becomes "will increase engagement" — a scope jump (1 → all users), a construct jump (clarity → engagement), and a certainty jump (one observation → "will"). | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "Increase engagement" has no named behaviour, no trigger, no consequence. The sentence would read the same for any UI change in any product. |
| P-03 Transcript Literalism | No | Only one quote supplied; literalism isn't the issue here, insufficiency is. |
| P-04 Volume Mistaken for Strength | No | No volume is being claimed — one unit, presented as one unit. The problem is what's inferred from it, not inflation by count. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence was filed. |
| P-08 Narrowing Sold as Resolving | Yes | An observation about icon recognition is presented as resolving an engagement question. Recognising an icon faster narrows (slightly) where to look for UX friction; it does not demonstrate that engagement will rise. |

### Where does it apply?

**Scope:** The evidence covers one participant, in one session, reacting to one icon. The claim covers all users, over time, on an aggregate behavioural metric. These do not match.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study limits were declared. I can't check the claim against limits that don't exist. If limits had been declared (e.g. sample size, remote-only, no behavioural data), several would likely have fired. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is being made across populations. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| The new icon is clearer (to INT-01) | INT-01: "Oh, that's a much clearer icon, I spotted it right away." | Observed | Yes |
| The new icon will increase engagement | not cited | Inferred | No — the inference leap is not argued, and "engagement" is nowhere in the source |

**Checked against:** nothing declared.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No research questions were declared, so I can't check whether this answers one. If questions had been declared, I'd want to know whether anyone actually asked about engagement — if not, the finding drifts from the study's purpose. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | Cannot assess — no prior research context was supplied. |
| P-07 Trust Without Process | Yes | The claim is asserted, not derived. There is no stated reasoning chain from "INT-01 found the icon clear" to "this will increase engagement." The classification would be unreconstructable from reasoning alone because no reasoning is given. |

### Is it theirs or ours?

**Beliefs and evidence:** The one piece of participant evidence (clarity) is theirs. The construct "engagement" and the direction "increase" come from somewhere else — a team assumption, a stakeholder's hope, or the author's interpretation. With no belief register, I can't tell which, but it's clear this part didn't come from the participant.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | Part (a) can't run without a belief register. Part (b) doesn't fire — there's no attributed opinion in the claim ("the PM says…"). But the fact that part (a) can't run matters here: "will increase engagement" has to come from somewhere, and without a declared belief we have no way to see where. | n/a |

### Tacit-knowledge prompt
Was engagement actually one of the things the sessions were designed to probe — or is it a construct added after the fact when writing up the finding? If the sessions weren't designed to measure engagement, that's worth saying explicitly rather than papering over.

### Decision boundary
- **Supports:** INT-01 found the new icon clearer than the alternative they were shown.
- **Doesn't support:** anything about engagement, anything about users other than INT-01, anything about what will happen when the icon ships.
- **What would close the gap:** a comparison of engagement metrics (defined specifically — opens? completions? return visits?) between a group using the new icon and a group using the old one. Icon clarity in a usability session cannot stand in for this.

**Safe to act on:** Not yet — the claim says far more than its evidence allows (CK-05 fires, P-01, P-07 and P-08 triggered), and three checks (CK-02, CK-04, CK-06) couldn't run because nothing was declared upstream. Even on the evidence present, "one participant found an icon clearer" doesn't support a causal prediction about engagement.

---

**One meta-note.** This claim is a textbook example of why the declarations matter. If you'd declared a research question like "does the new icon affect engagement?", CK-06 would have cleared (it answers the question) — but then CK-02 would likely have fired hard, because a 1-person usability session can't claim things about engagement. Either way, the overclaim surfaces. Without declarations, it surfaces through CK-05 and the pitfalls alone, which is why I didn't need them to flag this one — but on more subtle findings, the declarations do real work.
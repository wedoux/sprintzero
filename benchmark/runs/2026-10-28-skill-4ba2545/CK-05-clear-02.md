I'll run the QA pass on this.

## Workflow progress

- [x] Step 0: Gather declarations — belief register and study record
- [x] Step 1: Confirm there's a conclusion to evaluate
- [x] Step 2: Provenance pass
- [x] Step 3: Falsification pass
- [x] Step 4: Pitfalls check
- [x] Step 5: CK pass
- [x] Step 6: Produce the readout

**Note on declarations.** The material says "none declared" for both the belief register and the study record. That's the user's choice; I'll proceed, and checks that depend on those records will report NOT RUN. If you'd like deeper QA, see [templates/belief-register.md](templates/belief-register.md) and [templates/study-record.md](templates/study-record.md) — beliefs and questions are only useful when written by the people who hold them.

**Note on review conditions.** I don't know whether this synthesis was produced earlier in this same conversation. If it was, run this QA pass in a fresh conversation to avoid the critic grading its own homework.

---

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "In this sample, 5 of 6 participants found the new icon faster; any effect on engagement is untested."

**Evidence strength:** STRONG (for the narrow claim actually made)
The claim covers only what the timed sessions measured, in the sample tested, and explicitly rules out a wider claim about engagement.

**Claim matches its evidence:** Yes — the scope ("in this sample"), the count ("5 of 6"), the measured behaviour ("found the new icon faster"), and the stated limit ("any effect on engagement is untested") all stay inside what six timed session recordings can show.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** Order or novelty effects — if the new icon was shown second in every session, participants may have been faster because they'd already learned the task layout, not because of the icon itself. The evidence provided (timing from INT-01 to INT-06) doesn't say whether conditions were counterbalanced.
- **What would overturn this finding:** Session timing data showing the "faster" result reverses or disappears when icon order is counterbalanced, or when a comparable control task is timed.
- **Where the evidence underdetermines the claim:** n=6 with no stated study design (counterbalancing, baseline, task difficulty) means the finding is defensible as a within-sample observation but not as a causal claim about the icon. The claim doesn't make a causal claim, so this gap doesn't overturn it — but it's worth naming.

**Counter-evidence:** None cited in the material; one participant (of six) was not faster, and the claim acknowledges this implicitly by saying "5 of 6."

**Unsupported claims:** None. The claim is a count on timed data, and the data is timed sessions.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim is about a product behaviour (icon findability measured by time), not about what people feel, need or believe. | n/a |
| CK-04 Product finding without a human story | CLEAR | The product claim cites people-side evidence: timed behaviour from INT-01 to INT-06. | n/a |
| CK-05 Scope and certainty inflation | CLEAR | Scope is bounded ("in this sample"), count is exact ("5 of 6"), and the untested extension (engagement) is explicitly ruled out. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The finding names an observable behaviour (icon find-time) with a specific count, not a label. |
| P-03 Transcript Literalism | No | The evidence is timing data, not transcript interpretation. |
| P-04 Volume Mistaken for Strength | No | The claim doesn't inflate n=6 into a general claim; it says "in this sample." |
| P-05 Counter-Evidence Filed, Not Faced | No | The one non-faster participant is reflected in the "5 of 6" count rather than hidden. |
| P-08 Narrowing Sold as Resolving | No | The claim explicitly says engagement is untested — it doesn't present icon speed as resolving a wider trust or engagement question. |

### Where does it apply?

**Scope:** Six participants in timed sessions. The claim stays inside that: "in this sample."

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no `cannot_claim` to check against. The claim self-limits to the sample, which reduces the risk, but there is no declared limit I can verify this against. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer to another population or context is claimed. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "5 of 6 participants found the new icon faster" | INT-01 through INT-06, timed session recordings | Observed (timing is directly measured) | Yes |
| "any effect on engagement is untested" | Absence — no engagement measure in the evidence set | Observed (absence correctly stated) | Yes |

**Checked against:** Nothing declared — no belief register, no study questions, no study limits.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No declared questions, so there is nothing to map the finding onto. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No claim of novelty or confirmation that could conflict with prior research is made; I have no visibility into prior research. |
| P-07 Trust Without Process | No | The claim shows its working: n, direction, and the limit of what it covers. |

### Is it theirs or ours?

**Beliefs and evidence:** The claim rests entirely on timed behaviour from six participants. No stakeholder opinion, authority citation or team belief is woven in.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | No belief register declared, so part (a) can't run. Part (b) is CLEAR: the claim cites participant timing, not attributed opinion. Overall result: NOT RUN because part (a) is unverifiable. | n/a |

### Tacit-knowledge prompt
If someone ran these sessions: was the order of the old vs. new icon counterbalanced across the six participants, or did everyone see them in the same order? That one detail decides whether "faster" is about the icon or about task familiarity.

### Decision boundary
- **Supports:** The team can say that in this small sample, most participants found the new icon faster on a timed task. That is enough to justify a larger or more controlled test, and enough to rule out the new icon being obviously worse than the old on this measure.
- **Doesn't support:** Any claim that the new icon will be faster for the broader user base, that it improves engagement, or that the effect isn't driven by session order or novelty.
- **What would close the gap:** A counterbalanced timed study with a larger sample — the single thing that would turn "faster in this sample" into "faster, cause attributable to the icon."

**Safe to act on:** Yes — for the narrow decision of "is this worth testing further?" The claim is honestly scoped and matches its evidence. Two checks (CK-02, CK-06) report NOT RUN because no study record was declared; if the decision this feeds is larger than "run a bigger test," declare the study record and re-run the pass.

---

**Overall:** This is a well-disciplined finding. The notable thing is what it *doesn't* do — it doesn't inflate n=6 into a general claim, it doesn't extend to engagement, and it doesn't bury the one participant who wasn't faster. The main gap is upstream (no declared questions or limits), not in the claim itself.
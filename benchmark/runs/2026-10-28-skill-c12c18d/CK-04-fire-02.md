# QA Readout

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | Declared | B-01 | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "Moving the save button to the top right is the right call."

**Evidence strength:** WEAK
This is a design recommendation with no evidence behind it. The one belief it rests on is low-confidence, drawn from "a couple of other apps we use", and the team doesn't agree on it.

**Claim matches its evidence:** No — there is no evidence cited for the claim at all, and the belief it leans on is low-confidence and contested.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** Users look top-left, matching the app's own icon conventions (the position engineering already prefers). Nothing in the material rules this out.
- **What would overturn this finding:** Observation of users in sessions reaching for one position before the other, or completion/error data from a test comparing the two placements.
- **Where the evidence underdetermines the claim:** Everywhere. No user was observed, no user was asked, and no data is cited. The claim is entirely underdetermined.

**Counter-evidence:** Engineering's view that top-left matches existing icon conventions is noted in the dissent on B-01 but not addressed in the claim.

**Unsupported claims:** The entire claim ("Moving the save button to the top right is the right call") has no evidence behind it.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | Not a claim about people — it's a product recommendation. | n/a |
| CK-04 Product finding without a human story | FIRES | This product finding has no evidence about people behind it, and no assumption the team agreed to. B-01 is explicitly `agreed_by_all = no`. | B-01 |
| CK-05 Scope and certainty inflation | FIRES | This says more, or says it more surely, than the evidence allows. "The right call" is a definitive certainty on zero cited evidence. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "The right call" names no behaviour, no trigger, no consequence. Swap "save button" for any other control and the sentence reads the same. |
| P-03 Transcript Literalism | No | No transcript involved. |
| P-04 Volume Mistaken for Strength | No | No evidence volume to inflate. |
| P-05 Counter-Evidence Filed, Not Faced | Yes | Engineering's dissent on B-01 is on the record but the claim proceeds as if it isn't. |
| P-08 Narrowing Sold as Resolving | No | No narrowing claimed. |

### Where does it apply?

**Scope:** The claim implies a universal "right" placement, but no users, contexts or conditions are specified.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no `cannot_claim` limits to check against. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim or hedge is made. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "Moving the save button to the top right is the right call." | Not cited | Inferred (from B-01, apparently) | No — the claim cites no evidence, and B-01 itself is low-confidence own_experience. |

The entire claim has no supporting evidence.

**Checked against:** B-01 only. No questions or limits declared.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study questions declared, so there's nothing to map the claim to. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research referenced to contradict or confirm. |
| P-07 Trust Without Process | Yes | The claim is a verdict ("the right call") with no reasoning shown — no argument for why top-right beats top-left, no evidence weighed. |

### Is it theirs or ours?

**Beliefs and evidence:** The claim comes entirely from the team side — specifically from B-01, which is one person's low-confidence impression based on "a couple of other apps". Nothing in the claim comes from users.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | FIRES (part b) | This confidence comes from who said it, not from evidence. The claim restates a team-side belief as a settled recommendation, with no participant evidence behind it. Part (a) does not fire because B-01 is `low` confidence, not `high`. | B-01 |

### Tacit-knowledge prompt
Not applicable — no sessions were run.

### Decision boundary
- **Supports:** Nothing. There is no evidence here to support any placement decision.
- **Doesn't support:** Any claim about where users look, reach, or expect the save button to be. Any claim that top-right is better than top-left (or vice versa).
- **What would close the gap:** A quick comparative test — even an unmoderated preference test or a few task-based sessions where users are asked to save something — would tell you whether placement matters and in which direction. Right now the team is choosing between two guesses.

**Safe to act on:** Not yet — the claim is a team-side preference stated as a verdict, with no user evidence, no agreement internally, and no reasoning shown. Picking either placement now is a coin flip dressed as a decision.

---

### Note on inputs

Two things worth flagging for next time:

1. **No study record was declared.** That's your call, but it means CK-02 (limits) and CK-06 (drift) couldn't run — they're reported as NOT RUN, not as passed. If this decision matters, [templates/study-record.md](templates/study-record.md) is worth filling in even briefly.
2. **The belief register has one entry, and the claim leans entirely on it.** B-01 is honest about being low-confidence and contested, which is good — but that honesty is precisely why the claim built on top of it doesn't hold.
## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | Declared | Q-01 | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "5 of 6 participants did not notice the new filter button without being prompted."

**Evidence strength:** STRONG
The claim is a direct count of what participants said in the six sessions; the pattern is clear and consistent across five of them, with one explicit counter-case named.

**Claim matches its evidence:** Yes — the claim says "5 of 6 participants", not "users", and makes no causal or transfer claim.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** The task framing or moderator behaviour, not the button's visual design, caused participants to overlook it — e.g. the task may have pulled attention to the top of the screen (INT-04 explicitly says "I was looking at the top of the screen the whole time"). Without the task script, we can't tell whether this is a discoverability failure of the button or an artefact of where the task sent people.
- **What would overturn this finding:** Session recordings or the task script showing the task actively directed attention away from where the button sits, or a re-run with a more neutral task where most participants find it unprompted.
- **Where the evidence underdetermines the claim:** The claim as written ("did not notice") is well-supported for this sample. Any step beyond that — why they didn't notice, whether the button design is the cause, whether this generalises — is not supported by the quotes alone.

**Counter-evidence:** INT-06 saw the button right away and called the spot "pretty obvious". The claim correctly accommodates this by saying "5 of 6", not "all participants".

**Unsupported claims:** None — the single claim traces to all six quotes.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim counts an observable behaviour (noticing / not noticing) rather than validating a feeling or need. | n/a |
| CK-04 Product finding without a human story | CLEAR | The claim is about participants' behaviour, not a product decision; and it cites people-side evidence (INT-01 to INT-06). | n/a |
| CK-05 Scope and certainty inflation | CLEAR | Scope is "5 of 6 participants", not "users". No causal or certainty inflation. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | Behaviour (not noticing the filter button), implicit trigger (unprompted use), and consequence (points at the entry-point redesign decision) are all present. |
| P-03 Transcript Literalism | No | The claim rests on explicit verbal statements, not on inferred tone or hesitation; and it doesn't overclaim certainty. |
| P-04 Volume Mistaken for Strength | No | Single source type (interviews), but the claim scopes itself to that sample ("5 of 6 participants") rather than inflating to a general verdict. |
| P-05 Counter-Evidence Filed, Not Faced | No | INT-06 is accommodated in the claim's wording ("5 of 6", not "all"). |
| P-08 Narrowing Sold as Resolving | No | No causal claim is made about what to fix. |

### Where does it apply?

**Scope:** Six moderated sessions, participants labelled INT-01 to INT-06. The claim stays inside that sample.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No limits were declared in the study record. The claim is self-scoped to "5 of 6 participants", so no limit is obviously crossed, but with nothing declared there's nothing to check against. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is made. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| 5 of 6 participants did not notice the filter button without prompting | INT-01 ("didn't see a way to filter until you pointed"), INT-02 ("never noticed… had no idea it existed"), INT-03 ("found it by accident"), INT-04 ("didn't see it"), INT-05 ("only because I was told something was there") | Observed | Yes |
| Implicit: 1 of 6 did notice unprompted | INT-06 ("saw it right away") | Observed | Yes |

**Checked against:** Q-01 ("Do users notice the new filter button without being told it's there?").

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | CLEAR | The claim directly answers Q-01. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research was referenced or claimed. If prior discoverability work exists on this product, the team should flag it; the readout can't tell from the material provided. |
| P-07 Trust Without Process | No | The claim's reasoning (counting what participants said) is directly reconstructable from the quotes. |

### Is it theirs or ours?

**Beliefs and evidence:** The claim rests entirely on what participants said in the sessions. No belief register was declared, so there's nothing to check against — but nothing in the claim reads as borrowed from authority or team opinion either.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | No belief register was declared, so part (a) can't run. Part (b) is clear — the claim attributes to participants, not to a stakeholder or authority. | n/a |

### Tacit-knowledge prompt (optional — ask only if a researcher who ran the sessions is available)
INT-04 said "I was looking at the top of the screen the whole time". Did the task you gave participants direct their attention upward or to a specific area — i.e. is there a chance the task itself, rather than the button's placement, explains why five people missed it?

### Decision boundary
- **Supports:** In this sample of six moderated sessions, the filter button was not noticed unprompted by most participants. That's enough signal to justify treating the entry point as a discoverability problem worth investigating.
- **Doesn't support:** Any claim about *why* participants missed it (placement, contrast, icon, task framing), about users beyond this sample, or that a specific redesign will fix it.
- **What would close the gap:** The task script and, ideally, session recordings — to rule out the possibility that the task itself pulled attention away from the button. That would separate "the button is hard to find" from "the task made it hard to find in this study".

**Safe to act on:** Yes — but only for the narrow decision of "is the current entry point worth investigating as a discoverability problem?" Not safe to act on as a basis for a specific redesign without understanding *why* it was missed.

---

## Summary

One finding, honestly stated and well-matched to its evidence. Two checks reported NOT RUN because the belief register and the study's limits weren't declared — neither looks likely to overturn the finding, but they couldn't be checked. The main open question is whether the task script biased attention; worth answering before committing to a redesign direction.
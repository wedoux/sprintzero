## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

Before the finding below: you declared no belief register and no study record. That's your call, and this pass proceeds — but it means four of the six CK checks have nothing to check against and report NOT RUN. If you want a fuller audit, the templates at `templates/belief-register.md` and `templates/study-record.md` are there to fill in. I won't draft either for you — the point of those records is that they're yours.

---

## Finding: "3 of 8 participants preferred the subscription model over in-app purchases when asked directly; the other 5 said they had no preference."

**Evidence strength:** STRONG
The claim describes exactly what the eight evidence units say, with the counts in the right places and no inference beyond them.

**Claim matches its evidence:** Yes — the scope ("3 of 8 participants"), the method qualifier ("when asked directly"), and the handling of the other five are all accurate to the cited units.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** The "no preference" responses from INT-04 to INT-08 could mask weak preferences in either direction that a forced-choice or ranked question would have surfaced. "No preference" from a direct comparison is a thin signal — it can mean genuine indifference, unfamiliarity with one option, or politeness.
- **What would overturn this finding:** Transcript evidence that any of INT-01, INT-02 or INT-03 qualified their preference in a way the claim drops (e.g. "subscribe for *this* app, but only because…"), or that the "no preference" five actually expressed a leaning the summary flattened.
- **Where the evidence underdetermines the claim:** The three "prefer subscription" quotes give a stated preference but no behaviour behind it — INT-02 is the only one who grounds it in current practice ("I already do it for two other apps"). The claim doesn't overreach on this, but a reader shouldn't mistake "stated preference" for "would subscribe".

**Counter-evidence:** The five "no preference" responses are included in the claim rather than filed away — this is handled well.

**Unsupported claims:** None. Every element traces to a cited unit.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim reports what participants said as what they said; nothing is called confirmed or proven. | n/a |
| CK-04 Product finding without a human story | CLEAR | The claim is about people (stated preferences), not a product decision, and it cites people-side evidence. | n/a |
| CK-05 Scope and certainty inflation | CLEAR | Scope stays at "3 of 8 participants"; certainty stays at "preferred … when asked directly". No inflation to "users" or "prefer". | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The finding has a specific behaviour (stated preference), a specific trigger (direct comparison question), and names the counts. |
| P-03 Transcript Literalism | No | The claim doesn't over-trust the text — it says "when asked directly", which flags the elicitation method rather than treating the quotes as unprompted. |
| P-04 Volume Mistaken for Strength | No | No inflation of confidence from volume; 3 of 8 is reported as 3 of 8. (One source type — interviews — but the claim doesn't lean on corroboration.) |
| P-05 Counter-Evidence Filed, Not Faced | No | The "no preference" five are in the finding itself, not relegated to a footnote. |
| P-08 Narrowing Sold as Resolving | No | No causal or investigative claim is made beyond what was stated. |

### Where does it apply?

**Scope:** 8 interview participants, asked a direct comparison question between subscription and in-app purchases. The claim stays inside this.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record was declared, so there are no `cannot_claim` lines to check against. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is made. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| 3 of 8 participants preferred subscription | INT-01, INT-02, INT-03 (direct quotes) | Observed | Yes |
| … when asked directly | Framing stated in the evidence ("explicitly asked to compare") | Observed | Yes |
| The other 5 said they had no preference | INT-04 through INT-08 | Observed | Yes |

**Checked against:** nothing declared — no questions or limits to map this to.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study questions were declared, so there's nothing to check drift against. If this finding was unexpected rather than something the study set out to learn, labelling it as such would help a reader. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research is referenced or contradicted; nothing visible to flag. (If prior work on this question exists, this pass couldn't see it.) |
| P-07 Trust Without Process | No | The claim shows its working — counts, the direct-ask qualifier, and how the "no preference" five were handled are all visible. |

### Is it theirs or ours?

**Beliefs and evidence:** Every element of the claim traces to a participant quote or to the stated elicitation method. Nothing attributed to a stakeholder, authority or prior view.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | No belief register was declared. Part (b) (attributed opinion as evidence) can still run on the claim alone and finds nothing — the claim rests on participants, not on who said what internally — so this is as close to CLEAR as the input allows, but part (a) couldn't run at all. | — |

### Tacit-knowledge prompt (optional — ask only if a researcher who ran the sessions is available)
The five "no preference" responses are doing a lot of work in this finding. Was there a moment in any of INT-04 to INT-08 — a hesitation, a follow-up, a hedge — that suggested the indifference was genuine rather than a polite non-answer to a direct comparison question?

### Decision boundary
- **Supports:** When asked to compare the two models directly, more interview participants in this sample stated a preference for subscription than for in-app purchases; most stated no preference.
- **Doesn't support:** That users in general prefer subscription; that these participants would actually subscribe; that in-app purchases would underperform in practice.
- **What would close the gap:** Behavioural evidence — a prototype test, a pricing-page A/B, or analytics from a comparable app — would move this from "stated preference in a small sample" to something a pricing decision could rest on.

**Safe to act on:** Not yet — the claim is honest and matches its evidence, but 8 interviews with 3 stated preferences and 5 non-answers is a signal, not a basis for a pricing decision. Treat it as input to the next step (a behavioural test), not the answer.
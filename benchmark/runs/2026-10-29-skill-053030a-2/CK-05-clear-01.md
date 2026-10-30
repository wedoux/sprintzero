## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

A note before the finding: the user chose to proceed without a belief register or study record. Several checks will report NOT RUN as a result — this isn't a flaw in the claim, it's a limit on what this QA pass can confirm. If you want fuller coverage, write a belief register ([templates/belief-register.md](templates/belief-register.md)) and study record ([templates/study-record.md](templates/study-record.md)) and re-run.

## Finding: "3 of 8 participants preferred the subscription model over in-app purchases when asked directly; the other 5 said they had no preference."

**Evidence strength:** WEAK
The claim is a faithful tally of a small sample's stated preferences. It's a real observation about these eight people — nothing more, and the claim doesn't try to be more.

**Claim matches its evidence:** Yes — the numbers, the direct question, and the "no preference" result all match the evidence verbatim; no scope or certainty is added.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** The three who stated a preference were primed by the comparison question itself — INT-02 explicitly references habit from other apps, which is a reason to prefer the familiar option rather than a reasoned preference for this product. If so, even the "3 of 8" number overstates genuine preference.
- **What would overturn this finding:** Evidence that the three "preferrers" would in fact spend less, churn earlier, or behave the same as the five "no preference" participants if offered the alternative — i.e. that the stated preference doesn't translate into any observable behaviour.
- **Where the evidence underdetermines the claim:** The claim is a tally of stated preferences from a direct comparison question. It doesn't speak to intensity, willingness to pay, behaviour, or whether the five "no preference" participants were genuinely indifferent or simply disengaged. The claim doesn't try to say any of that, which is why it holds.

**Counter-evidence:** None in the evidence set — no participant contradicted the preference they stated, and the five "no preference" responses are consistent with the claim's framing.

**Unsupported claims:** None — every element of the claim (the count, the direct-question framing, the "no preference" result for the other five) is traceable.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim reports what participants said; it doesn't present a feeling or need as proven. | n/a |
| CK-04 Product finding without a human story | CLEAR | Not a product claim — it's a claim about what people said. | n/a |
| CK-05 Scope and certainty inflation | CLEAR | Scope is "3 of 8 participants", not "users". No certainty words beyond what the evidence supports. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim names a specific, countable behaviour (stated preference under direct questioning). |
| P-03 Transcript Literalism | No | The claim doesn't over-trust the text; it reports stated preferences, not inferred ones. A richer reading (tone, hesitation on the "no preference" responses) would add context but isn't needed to defend what's claimed. |
| P-04 Volume Mistaken for Strength | No | Single-source (interviews only), but the claim doesn't inflate confidence — it reports a count. |
| P-05 Counter-Evidence Filed, Not Faced | No | There's no counter-evidence in the set to face. |
| P-08 Narrowing Sold as Resolving | No | The claim doesn't propose a fix or action. |

### Where does it apply?

**Scope:** Eight interview participants, asked a direct comparison question. The claim stays entirely within that scope — it doesn't extend to "users" or any broader group.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no `cannot_claim` list to check against. The claim is self-limiting ("3 of 8 participants"), but this check can't formally confirm it respects limits that weren't written down. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer to a different population is claimed. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| 3 of 8 participants preferred subscription | INT-01, INT-02, INT-03 (quoted) | Observed | Yes |
| Other 5 had no preference | INT-04 through INT-08 (described) | Observed | Yes |
| They were asked directly / to compare | Stated in evidence note for INT-04–08 | Observed | Yes |

**Checked against:** Nothing declared — no belief register, no study questions, no stated limits.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study questions declared, so can't check whether this claim answers one. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research referenced or available to check against. If prior work on subscription-vs-IAP preference exists in your organisation, this finding should be placed against it. |
| P-07 Trust Without Process | No | The claim is derivable from the quoted evidence — anyone can count the three preferrers and the five neutrals. |

### Is it theirs or ours?

**Beliefs and evidence:** Entirely from what participants said in interviews. No stakeholder opinion, authority, or team belief appears in the claim.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | No belief register declared, so part (a) can't run. Part (b) is clear: the claim cites participants, not stakeholders or authority. | n/a |

### Tacit-knowledge prompt (optional — ask only if a researcher who ran the sessions is available)
INT-02 says "I already do it for two other apps", which could mean existing-habit transfer rather than preference for this product's subscription. For the three preferrers, did any of them give a reason that was about *this* product specifically, rather than general familiarity with subscriptions? And for the five "no preference" responses — were any of them disengaged or quick dismissals rather than considered indifference?

### Decision boundary
- **Supports:** Among these eight interview participants, when asked to compare directly, three stated a preference for subscription and five stated no preference. No one preferred in-app purchases.
- **Doesn't support:** Any claim about users in general, about what people would actually spend or choose when money is on the table, about the strength of the preference, or about whether the "no preference" five are genuinely indifferent versus unengaged.
- **What would close the gap:** A behavioural signal — e.g. an A/B test of the two models with the same user base — would tell you whether the stated preference moves actual choice. Short of that, a larger sample with the same direct question would at least tell you if 3-of-8 is a stable ratio.

**Safe to act on:** Not yet — the claim is honest, but eight participants' stated preferences aren't enough to pick a monetisation model. Use it as a signal to run a larger or behavioural study, not as a basis for the decision itself.
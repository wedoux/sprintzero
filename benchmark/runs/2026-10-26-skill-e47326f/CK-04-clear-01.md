## Finding: "Moving the save button to the top right is the right call — two sessions show people reaching for its old location and missing it."

**Evidence strength: WEAK**
The evidence shows two users briefly struggled to locate the save button after a redesign. That observation does not support the conclusion that moving it to the top right is "the right call" — if anything, it points the other direction, and the conclusion inverts what the evidence suggests.

### Provenance
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| Users reached for save in its old location | INT-01, INT-04 | Observed | Yes |
| Users missed / mis-clicked after the move | INT-01 ("clicked the wrong icon twice"), INT-04 ("took me a few seconds") | Observed | Yes |
| The save button was moved to the top right | — | Inferred (context) | No — neither excerpt names the new location. INT-01 says the *old* location was top-left; INT-04 expected it "where share usually sits." The new position is not evidenced in the material provided. |
| Moving it to the top right is "the right call" | — | Inferred (asserted) | No — no evidence supports this. The two excerpts describe friction *caused by* the move, not benefit from it. |

Two of the four claims — the specific new location and the normative verdict — have no evidence in the material provided.

### Falsification pass
- **Strongest counter-hypothesis:** The move was a mistake, or at least costly. Both participants exhibit exactly the kind of friction (looking in the wrong place, mis-clicking, delay) that a well-placed primary action should not produce. The same evidence reads more naturally as "users expect save in the top-left or near share; the new position violates both expectations" than as validation of the new position.
- **What would overturn this finding:** Evidence that (a) users adapted quickly across subsequent tasks or sessions, (b) the top-right location performs better on a measurable outcome (completion rate, time-to-save, error rate) than the alternatives, or (c) there was a specific constraint (accessibility, platform convention, feature conflict) that made top-right the least-bad option. None of this is present.
- **Where the evidence underdetermines the claim:** The evidence base is two short excerpts from two sessions, both describing the moment of friction and nothing after it. There is no post-adaptation data, no comparison to alternatives, no success metric, and no rationale for the design choice. The claim is radically underdetermined.

### Pitfalls checked

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The finding is specific (named control, named locations, named behaviour). |
| P-02 Context Blindness | Partial | No prior-research context is declared, so I can't check against it — but the finding reads as if no prior convention research exists, when INT-04's reference to "where share usually sits" implies platform conventions that should be examined. |
| P-03 Transcript Literalism | No | The excerpts are being over-interpreted, but not because tone or hesitation was missed — the problem is the direction of the inference, not the thinness of the text. |
| P-04 Volume Mistaken for Strength | Yes | Two interviews, same source type, same session type, saying structurally the same thing (friction locating save). Treated as corroboration ("two sessions show…") when it is one signal observed twice. No independent source (analytics, support tickets, task-completion data) is brought in. |
| P-05 Counter-Evidence Filed, Not Faced | Yes | The evidence *is* the counter-evidence. Both excerpts describe the move causing friction; the finding treats this as support for the move. The contradiction is not filed-and-ignored — it is inverted. This is the more severe form of P-05. |
| P-06 Formulaic Transfer Hedge | No | No transfer claim made. |
| P-07 Trust Without Process | Yes | The verdict ("right call") is asserted without reasoning. There is no stated argument for *why* top-right is correct — no comparison to alternatives, no criterion for "right," no mechanism connecting the observed friction to the conclusion. The classification is restated, not derived. |
| P-08 Narrowing Sold as Resolving | Yes | Even granting the most charitable read — that the evidence identifies "users have a location expectation for save" — that is a narrowing finding (it tells you *where to investigate*), not a resolving one (it does not tell you top-right is correct). The finding treats a narrowing signal as a settled design verdict. |

### What would change this verdict
A direct comparison between the old location (top-left), the new location (top right, if that is in fact where it moved to), and the location users expected (near share) — measured on time-to-save, error rate, or completion in a task-based test with more than two participants. Short of that, even a follow-up excerpt showing INT-01 and INT-04 adapting fluently within the same session would be meaningful. Right now there is no evidence for the verdict at all.

### Tacit-knowledge prompt
INT-01 says they "clicked the wrong icon twice" looking for save in the old location. Which icons did they click, and did either of those mis-clicks have a destructive or confusing consequence? That matters for judging whether the friction observed is a transient learning cost or a persistent error pattern — and the transcript as given doesn't resolve it.

---

**Summary for the reviewer:** This finding should not stand as written. The conclusion ("right call") is not merely under-evidenced — it runs opposite to what the two cited excerpts actually show. At minimum the claim needs to be rewritten to match the evidence (something like: "two users experienced locating-friction after save was moved; whether this is transient learning cost or a persistent problem is not yet established"). The decision to keep the button in the top right needs separate justification that is not present in this material.
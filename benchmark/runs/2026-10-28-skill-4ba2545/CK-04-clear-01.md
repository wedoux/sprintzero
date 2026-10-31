## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

A quick note before the readout: the user chose to run this without a belief register or study record. Several checks will report NOT RUN as a result — that's expected, not a flaw in the finding itself. If this is a decision that matters, writing even a short study record (what was being tested, what the sessions couldn't cover) would let the QA pass actually check scope and drift rather than just note it couldn't.

## Finding: "In all 6 sessions, participants went straight to the top right for save without hesitation."

**Evidence strength:** STRONG
Six out of six participants did the same thing, each quoted directly, with no contradicting signal in the material provided.

**Claim matches its evidence:** Yes — the claim is scoped to the 6 sessions, names the behaviour observed, and doesn't extend to "users" or "everyone".

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** Participants were primed — by the recruiter, the task wording, or an earlier task in the session — to look top-right, so the convergence reflects the setup rather than a natural expectation. None of the quotes rule this out.
- **What would overturn this finding:** A session recording or task script showing the save location was mentioned or implied before the participant acted; or evidence that participants were selected from a pool already familiar with this product's conventions.
- **Where the evidence underdetermines the claim:** The quotes show participants went top-right and said it felt expected. They don't independently confirm there was no hesitation — "hesitation" is the researcher's reading of the behaviour, and only the quotes, not timing or video, were provided here.

**Counter-evidence:** None in the material provided.

**Unsupported claims:** "Without hesitation" is an inference from the quotes rather than something each participant stated. Five of six quotes support it directly ("didn't have to think about it", "no hesitation", "went straight for", "didn't think twice", "found it instantly"); INT-03 ("exactly where I'd look") is consistent but doesn't itself speak to hesitation. Minor, but worth noting.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim describes an observable action (where participants went), not a validated attitude or need. | n/a |
| CK-04 Product finding without a human story | CLEAR | The claim is grounded in people-side evidence (6 interview quotes). | n/a |
| CK-05 Scope and certainty inflation | CLEAR | Scope is held to "6 sessions"; certainty ("went straight to", "without hesitation") is supported by the quoted language. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | Names a specific behaviour (going top-right for save), with a specific context (the 6 sessions). |
| P-03 Transcript Literalism | No | The claim rests on what participants did and said; it isn't over-reading tone or inferring hidden meaning. |
| P-04 Volume Mistaken for Strength | Yes | All 6 units are the same source type (moderated interviews, same study). Six consistent interviews is one method's worth of signal, not six independent angles. The finding would be stronger if corroborated by, e.g., analytics on save-button clicks or an unmoderated test. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence was presented; none to face. |
| P-08 Narrowing Sold as Resolving | No | No causal fix is claimed from this. |

### Where does it apply?

**Scope:** The claim is held to "6 sessions" and makes no transfer claim. Whether the pattern holds for other users, platforms, or contexts is simply not addressed — which is the right move given what's here.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no `cannot_claim` to check against. If a record existed it would likely clear, but the check can't run. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is made. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| Participants went to the top right for save | INT-01 through INT-06, each quoted | Observed | Yes |
| In all 6 sessions | INT-01 through INT-06 | Observed (count matches) | Yes |
| Without hesitation | INT-01, INT-02, INT-04, INT-05, INT-06 directly; INT-03 indirectly | Inferred (from language) | Yes, though INT-03 is a weaker link for this specific sub-claim |

**Checked against:** Nothing declared.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No questions declared, so there's nothing to check whether this answers. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No (but can't fully check) | No prior research was mentioned; without a study record it's not possible to tell if this restates or contradicts something known. |
| P-07 Trust Without Process | No | The reasoning (6 of 6 said and did the same thing) is visible and reconstructable from the evidence. |

### Is it theirs or ours?

**Beliefs and evidence:** All six supporting units are participant quotes. Nothing in the claim rests visibly on team opinion, authority, or prior conviction.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN (part a) / CLEAR (part b) | No belief register, so part (a) can't run. Part (b) is clear: the claim is supported by participant evidence, not attributed opinion. | n/a |

### Tacit-knowledge prompt (optional — ask only if a researcher who ran the sessions is available)
Was the save task introduced in a way that could have hinted at location — for example, did the task script, the prototype's visible UI before the task, or an earlier task mention or show the top-right area? The convergence is striking enough that ruling out priming would meaningfully strengthen it.

### Decision boundary
- **Supports:** In these 6 sessions, participants looked top-right for save and reported it felt expected.
- **Doesn't support:** That this generalises to the broader user base; that there was no priming effect; that top-right is the right location for save in this product's full context.
- **What would close the gap:** The task script and session setup — enough to rule out that participants were cued to the location before the quoted moment.

**Safe to act on:** Yes — for a decision scoped to "top-right matches participant expectations in a sample of 6", this holds. For a broader decision ("save belongs top-right in this product"), not yet: P-04 fires because all evidence is one method, and without a study record the scope the finding is meant to inform isn't declared.

---

**One honest note on the overall pass:** this is a short, clean claim with directly supporting quotes, and the main thing the QA pass surfaced is single-source homogeneity (P-04) plus three NOT RUN checks caused by the missing declarations. That's the system working as intended on easy input — not every pass will or should turn up a dramatic flaw. If you want a more demanding test, the useful next move is writing even a one-paragraph study record so CK-02 and CK-06 can actually run.
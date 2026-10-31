## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

**Note on declarations.** The user chose to run this QA pass with no belief register
and no study record. That's a legitimate choice, but it means several checks can't
run — they're reported as NOT RUN below, not as passed. If this finding is going to
drive a decision, writing even a short record of what the study asked and what it
cut would let the full pass run. See `templates/belief-register.md` and
`templates/study-record.md`.

## Finding: "In all 6 sessions, participants went straight to the top right for save without hesitation."

**Evidence strength:** STRONG
Six out of six participants described the same behaviour in the same terms, and the quoted language ("didn't have to think about it", "no hesitation", "found it instantly") directly supports the "without hesitation" wording in the claim.

**Claim matches its evidence:** Yes — the claim stays inside its sample ("in all 6 sessions"), doesn't generalise to "users", and the behavioural description matches what each participant said.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** The six quotes are suspiciously uniform. Every participant uses near-identical phrasing ("top right", "didn't think twice", "exactly where I expected"). Real session data usually has more variation in how people describe the same action — one person says "up there", another points, another hesitates and then explains. The uniformity could mean the quotes were paraphrased into a consistent style during note-taking (which would still support the claim), or it could mean the sample was homogeneous in a way that doesn't transfer (all participants from the same background, all heavy users of similar apps). Worth noting but doesn't overturn the claim as stated.
- **What would overturn this finding:** A session recording showing a participant hesitating, scanning the screen, or trying another location first before landing on top-right — contradicting the "without hesitation" and "went straight to" language. None is present in the evidence provided.
- **Where the evidence underdetermines the claim:** The claim is tightly scoped and the evidence supports it directly. The underdetermined piece is *why* — participants attribute it to convention ("same as every app I use", "like everywhere else"), but the claim doesn't make a causal argument, so this doesn't weaken it.

**Counter-evidence:** None in the material provided.

**Unsupported claims:** None — every element of the claim (all 6, top right, save, without hesitation) traces to the quoted evidence.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim describes an observed action ("went straight to the top right"), not a validated attitude or need. | n/a |
| CK-04 Product finding without a human story | CLEAR | Not a product claim — it's a claim about participant behaviour. | n/a |
| CK-05 Scope and certainty inflation | CLEAR | "In all 6 sessions, participants" stays inside the sample; "without hesitation" is supported verbatim by the quoted language. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | Names a specific behaviour (go to top-right for save), with a specific trigger (looking for save) and a specific scope (6 sessions). |
| P-03 Transcript Literalism | No | The claim stays close to what the quotes literally say and doesn't infer attitude, confidence or meaning beyond the described action. |
| P-04 Volume Mistaken for Strength | Yes | All six supporting units come from the same source type (moderated interviews). Six interview excerpts corroborate each other, but there's no independent angle (analytics on where people clicked, support tickets, observation). The claim's wording is modest enough that this doesn't invalidate it, but a reader shouldn't take "6 of 6 interviews" as equivalent to "6 of 6 interviews + click data + support history". |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence was provided to face or file. |
| P-08 Narrowing Sold as Resolving | No | The claim doesn't propose a fix or claim to resolve a problem. |

### Where does it apply?

**Scope:** The claim is scoped to "all 6 sessions" and the participants in them — it doesn't extend to users in general, which is correct given the evidence.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record was declared, so there are no `cannot_claim` statements to check against. The claim appears self-limiting ("in all 6 sessions"), but without a declared sample description or limits, I can't confirm it stays inside what the study was designed to cover. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | The claim doesn't transfer the finding to a different population. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| All 6 sessions, participants went to top right | INT-01 through INT-06, each quoting "top right" | Observed | Yes |
| For save | INT-01, 02, 03, 04, 05 explicitly mention "save"; INT-06 says "top right, found it instantly" in context | Observed (5 of 6); inferred for INT-06 | Yes, if context (the task being "find save") is assumed; INT-06 doesn't name "save" directly |
| Without hesitation | "didn't have to think about it" (INT-01), "no hesitation" (INT-02), "went straight for" (INT-02, 04), "didn't think twice" (INT-05), "instantly" (INT-06) | Observed | Yes |

Minor note: INT-06 doesn't mention "save" in the excerpt provided. If these are standalone quotes without surrounding context, the claim as to INT-06 rests on an assumption that the task was about save. In practice this is almost certainly fine, but strictly speaking, 5 of 6 excerpts name "save" explicitly.

**Checked against:** Nothing declared. No beliefs, questions or limits were provided, so this finding wasn't checked against anything upstream.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study questions were declared, so there's no way to check whether this finding answers one. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research was referenced and none was flagged as missing — but note that "save in top-right" is a well-established UI convention; if prior internal research or industry findings exist on this, the finding may be confirming rather than discovering. Worth saying so if that's the case. |
| P-07 Trust Without Process | No | The claim is specific enough that its reasoning is visible — the evidence shows directly what the claim asserts. |

### Is it theirs or ours?

**Beliefs and evidence:** The claim is grounded in what participants said. No team belief, authority opinion or stakeholder agreement is being passed off as evidence.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | No belief register was declared, so part (a) can't run. Part (b) — attributed opinion standing in for evidence — is CLEAR: the support is participant quotes, not "the PM says" or "stakeholders agreed". | n/a |

### Decision boundary
- **Supports:** In this sample of 6, every participant found the save control in the top-right location without visible difficulty. For this interface and this group, top-right is a safe location for save.
- **Doesn't support:** That this generalises to all users of the product, to users with different app-use habits, or to a different save-adjacent action (e.g. "save as", "save draft"). Also doesn't support any claim about why the location worked — participants attribute it to convention, but the claim doesn't argue causation.
- **What would close the gap:** If the question is "should save stay in the top-right across the product?", the single most useful next piece of evidence is behavioural data from a wider population — click-location data from existing analytics, or a brief task in a larger unmoderated test — to confirm the 6-of-6 pattern isn't a sample artefact.

**Safe to act on:** Yes — within the scope the claim actually makes ("in all 6 sessions"). The claim is honest about its sample and matches its evidence. The only caveat worth flagging to the team: P-04 fired because all six units are one source type, so if someone later cites this as "research shows users expect save in the top-right" (dropping the "6 sessions" scope), that would be an overclaim this evidence doesn't support.
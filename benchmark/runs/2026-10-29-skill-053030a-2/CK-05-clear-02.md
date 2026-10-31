I'll run the QA pass on this.

**On the declarations:** the material says the belief register and study record are "none declared". Before proceeding, I want to flag that this is your choice to make, not mine. Beliefs and research questions are only useful when written by the people who hold them — I won't draft them for you. If you'd like to add them, the templates are `templates/belief-register.md` and `templates/study-record.md`. Several checks below will report NOT RUN as a result; that is the correct outcome, not a failure of the claim.

Proceeding with the QA pass as requested.

---

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "In this sample, 5 of 6 participants found the new icon faster; any effect on engagement is untested."

**Evidence strength:** STRONG
Six timed sessions with consistent results on a narrow, directly-measured claim — this is about as clean as a small-sample finding gets for the thing it actually says.

**Claim matches its evidence:** Yes — the scope ("in this sample"), the count ("5 of 6"), and the explicit non-claim about engagement all stay within what six timed sessions can show.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** The timing difference reflects novelty or task-framing in the session rather than any durable property of the icon — participants knew they were being timed on the new element and attended to it more carefully. The evidence as supplied (timing only) can't distinguish this.
- **What would overturn this finding:** Timing data from the 6th participant showing the opposite direction at a magnitude large enough to shift the pattern, or session recordings showing the "faster" times reflect participants hesitating on the old icon out of unfamiliarity with the test setup, not genuine findability.
- **Where the evidence underdetermines the claim:** The claim is narrow enough that the evidence covers it. It does not cover *why* it was faster, or whether the effect persists past first exposure — and the claim doesn't try to.

**Counter-evidence:** The 1 of 6 participant who didn't find it faster is named in the count but not characterised. Not a problem for the claim as written (it says "5 of 6", not "all"), but worth noting that nothing is said about why that participant diverged.

**Unsupported claims:** None. Every component of the claim traces to the timing data.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | Claim is about the product (icon findability measured by task time), not about what people feel, need or believe. | n/a |
| CK-04 Product finding without a human story | CLEAR | Product claim backed by people-side evidence (timed participant behaviour in INT-01 to INT-06). | n/a |
| CK-05 Scope and certainty inflation | CLEAR | Scope is explicitly "in this sample"; count is exact ("5 of 6"); engagement is explicitly disclaimed as untested. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | "Found the new icon faster" is a specific, observable behaviour with a measurable trigger (task) and a measurable consequence (time). |
| P-03 Transcript Literalism | No | Evidence is timing data, not transcript interpretation — the literalism risk doesn't apply in the same way. (See tacit-knowledge prompt below.) |
| P-04 Volume Mistaken for Strength | No | Single source type, but the claim's scope matches: it says "in this sample", not "users". |
| P-05 Counter-Evidence Filed, Not Faced | No | The 1-of-6 divergence is included in the count rather than filed in a separate section and ignored. |
| P-08 Narrowing Sold as Resolving | No | The claim explicitly refuses to extend to engagement. |

### Where does it apply?

**Scope:** Six participants in whatever conditions INT-01 to INT-06 were run in. The claim stays inside that with "in this sample" and the explicit engagement disclaimer.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no `cannot_claim` to check against. The claim's own "in this sample" wording does narrow it, but that's self-policing, not an audit against declared limits. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is made. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| 5 of 6 participants found the new icon faster | INT-01 through INT-06 timed session recordings | Observed | Yes |
| Any effect on engagement is untested | — (negative claim about what the evidence doesn't cover) | Observed (by absence) | Yes |

**Checked against:** Nothing declared. The provenance is clean against the evidence supplied, but there is no belief register, no research question list, and no limits statement to audit the finding against.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study record questions declared, so no way to check whether this finding answers one of them. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No (with caveat) | No prior research visibility was supplied either way; the finding doesn't claim novelty, so this doesn't fire — but if a prior study on this icon exists, it should be referenced. |
| P-07 Trust Without Process | No | The claim shows its working (5 of 6, from timing) rather than asserting a label. |

### Is it theirs or ours?

**Beliefs and evidence:** The claim rests entirely on observed timing from the six sessions. No stakeholder opinion, no borrowed authority, no team agreement being presented as evidence.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | No belief register, so part (a) can't run. Part (b) can run on the claim alone and does not fire — the claim cites timing data, not attributed opinion. | n/a |

### Tacit-knowledge prompt
If a researcher ran these sessions: for the 1 of 6 participant who didn't find the new icon faster — was there anything in the session (hesitation, a comment, a different approach to the task) that would help tell whether that's a genuine outlier, a task-comprehension issue, or a signal the pattern is less consistent than the count suggests?

### Decision boundary
- **Supports:** The icon-findability change is worth continuing to develop or test at larger scale; nothing in these six sessions argues against it.
- **Doesn't support:** Any claim about engagement, retention, long-term use, or how the icon performs for users outside this sample.
- **What would close the gap:** If the decision is "ship it", a larger timed test (or in-product analytics after a staged release) that measures findability past first exposure. If the decision is "does it affect engagement", a different study — this one explicitly doesn't address that.

**Safe to act on:** Yes — the claim is specific, honestly scoped, backed by directly-relevant evidence, and refuses the overreach it could have made (engagement). The reason it's "Yes" despite two NOT RUN results is that those checks are about matching the finding to declared questions and limits that don't exist; they don't indicate a problem with the claim itself. If the decision this feeds is anything broader than "did the icon test well in this round", you need a study record to anchor that broader decision against.

---

**A note on the overall result:** This is a well-formed claim, and the readout reflects that. The pattern worth noticing — for your own process rather than for this specific claim — is that without a declared study record, I can't tell you whether this finding answers a question anyone asked, or whether it stays inside limits anyone agreed to. The claim polices itself well; the surrounding research doesn't have anything to be audited against. That's a gap worth closing before the next study, not a reason to distrust this one.
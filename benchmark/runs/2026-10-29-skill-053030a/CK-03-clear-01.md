Before I run the pass: this synthesis has no belief register or study record declared. That's your call to make — those records are only useful when the people who hold the beliefs and asked the questions write them. If you'd like to add them, see `templates/belief-register.md` and `templates/study-record.md`. I can ask questions that help, but I won't draft them for you.

Proceeding without them. Several checks will report NOT RUN as a result.

---

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "4 of 5 participants completed checkout without help."

**Evidence strength:** STRONG (within its sample)
The claim describes exactly what the sessions showed: five participants were observed, four completed checkout without help. The numerator and denominator are stated plainly.

**Claim matches its evidence:** Yes — the claim counts what was observed and claims no more than that.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** The one participant who needed help may represent a common failure mode the other four happened to avoid (e.g. a payment method, address format, or device type), rather than being an outlier. With n=5, we can't tell which.
- **What would overturn this finding:** Session recordings showing that one or more of the "completed without help" participants actually hesitated, backtracked, or used a workaround that wasn't logged as "needing help" — the claim depends on how "without help" was defined in the moment.
- **Where the evidence underdetermines the claim:** Five participants is enough to say what happened in these five sessions. It is not enough to say what rate of unassisted completion to expect in the wider user base, and the claim doesn't try to.

**Counter-evidence:** None cited.

**Unsupported claims:** None — the single claim traces to the observed sessions.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | Not a claim about people's needs, attitudes or feelings — it's a product behaviour check against a standard (completion without help). | n/a |
| CK-04 Product finding without a human story | CLEAR | Product claim backed by people-side evidence (observed behaviour in INT-01 to INT-05). | n/a |
| CK-05 Scope and certainty inflation | CLEAR | Scope ("4 of 5 participants") matches the evidence base exactly; no certainty inflation ("completed" is observable, not inferred). | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim names an observable behaviour (completed checkout) with a specific denominator. |
| P-03 Transcript Literalism | No | Observation of session recordings, not transcript interpretation. |
| P-04 Volume Mistaken for Strength | No | The claim doesn't inflate confidence; it reports 4/5 as 4/5. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence filed. The one non-completing participant is part of the numerator, not sidelined. |
| P-08 Narrowing Sold as Resolving | No | No causal or "enables" claim is made. |

### Where does it apply?

**Scope:** The five observed sessions. The claim does not extend beyond them.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no `cannot_claim` to check against. The claim stays close to the observed sample on its face, but limits weren't declared. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer to another population or context is attempted. |

### Could someone retrace it?

**Provenance**

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| 4 of 5 participants completed checkout without help | INT-01 to INT-05 session recordings | Observed | Yes |

**Checked against:** Nothing declared. No belief register, no questions, no limits.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No declared questions to map the finding against. Can't tell whether this answers something the team asked or is incidental. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research referenced; none evidently contradicted. If prior checkout research exists, this finding should reference it — flagging as a gap worth checking rather than a trigger. |
| P-07 Trust Without Process | No | The claim is a direct count, not a classification needing argument. |

### Is it theirs or ours?

**Beliefs and evidence:** The claim rests entirely on observed behaviour in the sessions. No attributed opinion, no authority citation, no "the team agreed" framing.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | No belief register declared, so part (a) cannot run. Part (b) is CLEAR on the claim alone: no attributed opinion is offered as support. Reporting NOT RUN overall because part (a) couldn't run. | n/a |

### Tacit-knowledge prompt
For the researcher who ran INT-01 to INT-05: how was "without help" defined in the moment? Did any of the four "completed without help" participants hesitate, backtrack, or verbalise confusion in a way that didn't rise to asking for help but might point at a near-miss? And what happened with the one participant who needed help — was it a specific step, or a general stall?

### Decision boundary
- **Supports:** A plain statement that, in these five sessions, four completed checkout without help. Useful as a baseline observation for a next round.
- **Doesn't support:** Any claim about the completion rate for users generally, any claim about why four succeeded or one didn't, any inference about whether checkout "works".
- **What would close the gap:** A larger sample with a defined "without help" criterion, or analytics on unassisted completion rates in production — depending on which decision this finding is meant to inform. (That decision isn't declared.)

**Safe to act on:** Not yet — the claim is honest and the count is clean, but with no study record declared, there's no way to tell whether this answers a question the team asked, stays inside the study's limits, or informs a decision anyone is making. The finding itself isn't the problem; the missing scaffolding around it is.

---

A note on the "Not yet" verdict: this isn't a judgment on the research. The observation is well-stated and the claim matches its evidence exactly — that's correct practice. The verdict reflects that three checks couldn't run because the records they depend on weren't declared. If you add even a minimal study record naming the decision this informs and the question it was meant to answer, CK-02 and CK-06 become runnable and this likely moves to "Yes".
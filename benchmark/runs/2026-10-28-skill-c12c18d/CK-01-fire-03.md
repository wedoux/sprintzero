The synthesis under review was supplied directly — not generated earlier in this conversation — so a fresh-conversation reset isn't needed here. Running the QA pass now.

A note before the readout: the Belief register is declared (one belief, B-01), but no Study record and no evidence were supplied with the claim. I'll run the checks that can run on what's here, and mark the rest NOT RUN with the missing input named. I won't draft questions, limits, or evidence to fill the gaps — those have to come from the team.

---

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | Declared | B-01 | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "Hikers want maps that work offline — stakeholders confirmed it in last week's review — so offline download will be on by default."

**Evidence strength:** WEAK
No participant evidence has been cited for this claim. The only named support is a stakeholder review and one low-confidence belief rooted in the author's own experience on two trails. That is not a basis a product team should change a default on.

**Claim matches its evidence:** No — the claim states a user need as settled ("hikers want") and jumps to a product default, while its stated support is a stakeholder meeting and a personal anecdote, not evidence from hikers.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** Hikers on your top trails have adequate signal (the ops lead's dissent in B-01 points at this directly), and offline-on-by-default costs them storage and setup friction for a problem they don't have. A second plausible counter: some hikers do want offline maps but want to *choose* when to download them, so "on by default" is the wrong fix even if the need is real.
- **What would overturn this finding:** Behavioural evidence from hikers — session recordings, interviews, or support tickets — showing either that signal loss is rare on the trails your users actually hike, or that users already work around it without wanting a default change.
- **Where the evidence underdetermines the claim:** Entirely. No hiker evidence has been cited. The claim is underdetermined on every axis: whether the need exists, how widespread it is, which hikers it applies to, and whether "on by default" is the right response even if it does.

**Counter-evidence:** The ops lead's dissent recorded in B-01 ("coverage on our top trails is fine") directly contradicts the premise and has not been addressed in the claim.

**Unsupported claims:** All of it. "Hikers want maps that work offline" has no cited hiker evidence. "Offline download will be on by default" is a product decision that follows only if the need claim holds, which it doesn't on this evidence.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | FIRES | "This treats what we learned about people as proven. Only a product can be validated." The claim states "Hikers want maps that work offline" as settled, and reinforces it with "stakeholders confirmed it." A want is an attitude about people and cannot be confirmed by a stakeholder meeting. | n/a |
| CK-04 Product finding without a human story | FIRES | "This product finding has no evidence about people behind it, and no assumption the team agreed to." The product decision ("offline download will be on by default") cites no people-side evidence, and the only belief it could rest on (B-01) has `agreed_by_all = no`. | B-01 |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." "Hikers" is unscoped (which hikers, which trails), and "will be on by default" is a committed product action resting on no cited evidence. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "Hikers want maps that work offline" is a label — no named behaviour, no trigger, no specific consequence tied to observed use. Swap "hikers" for "drivers" and "trails" for "tunnels" and the sentence reads the same. |
| P-03 Transcript Literalism | No | No transcript is being over-read; the problem is the opposite — no participant source at all. |
| P-04 Volume Mistaken for Strength | No | No volume is being claimed; there's no evidence set to be homogeneous. |
| P-05 Counter-Evidence Filed, Not Faced | Yes | The ops lead's dissent in B-01 directly contradicts the premise and is not argued against anywhere in the claim. It isn't even filed — it's ignored. |
| P-08 Narrowing Sold as Resolving | No | No investigative narrowing is happening; the claim leaps straight to a fix. |

### Where does it apply?

**Scope:** The claim covers "hikers" with no qualifier — any hiker, any trail, any trip length. The only underlying signal is the author's experience on two trails plus an unspecified stakeholder discussion. Those cover none of "hikers" as a population.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no `cannot_claim` to check against. Note: this doesn't mean the scope is fine — CK-05 above already flags the scope inflation. It means the specific limits check can't run. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is being hedged; the claim simply overreaches directly. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "Hikers want maps that work offline" | Not cited. The only candidate support in the material is B-01 (own experience, low confidence) and "stakeholders confirmed it in last week's review." | Inferred | No — no participant evidence, no study, no analytics. |
| "Stakeholders confirmed it in last week's review" | The review itself is referenced but not quoted or summarised. | Observed (that a meeting happened) | Partial — we know the meeting is being invoked, but not what was said, by whom, on what basis. |
| "Offline download will be on by default" | Derived from the above. | Inferred | No — the product decision inherits the gaps in the claims it rests on. |

Every substantive claim in the finding is untraceable to participant evidence. This isn't a provenance gap at the margins; it's the whole thing.

**Checked against:** B-01 (the only declared item). No questions and no limits were declared, so CK-06 and CK-02 could not run against the team's own frame.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study questions declared. Can't check whether this finding answers a question the team actually asked. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | Can't be assessed — no indication of prior research either way. |
| P-07 Trust Without Process | Yes | "Stakeholders confirmed it" is a conclusion with no reasoning attached. We don't know who confirmed, on what evidence, or whether the review surfaced the dissent already recorded in B-01. The confirmation is asserted, not argued. |

### Is it theirs or ours?

**Beliefs and evidence:** Everything in this claim comes from the team's side of the ledger, not from hikers. "Hikers want…" is being supported by (a) a stakeholder meeting and (b) a belief (B-01) that is low-confidence, rooted in `own_experience`, and explicitly disputed by the ops lead. No hiker said anything in the material supplied.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | FIRES (part b) | "This confidence comes from who said it, not from evidence." The claim's support is "stakeholders confirmed it in last week's review" — attributed agreement, not participant evidence. Part (a) does not fire on B-01 itself, because B-01 is declared `low` confidence; but the claim treats the underlying belief as if it were high-confidence without new evidence to justify the upgrade. | B-01 (confidence `low`, dissent on record); and the attributed "stakeholders" |

### Tacit-knowledge prompt
Not applicable — there's no researcher who ran sessions, because no sessions appear to have been run for this claim. The right next step isn't a tacit-knowledge question; it's gathering evidence from hikers.

### Decision boundary
- **Supports:** That some people inside the company — including the author, on two trails, and some stakeholders in a review — believe offline maps matter. That's a reasonable hypothesis to go test.
- **Doesn't support:** Any statement about what hikers (as a population, or any defined segment of them) want, do, or need. Any product default change. Any claim that the question is settled — the ops lead's dissent in B-01 is on record and unaddressed.
- **What would close the gap:** The single most useful next step is evidence from hikers themselves on the trails your users actually use — a short round of interviews or a review of support tickets mentioning signal, maps or offline use would move this from "internal hypothesis" to something testable. Resolving the ops lead's dissent (what does coverage data actually show on your top trails?) is the cheapest first move.

**Safe to act on:** Not yet — the claim rests entirely on internal opinion and a disputed personal anecdote, with no participant evidence cited and no study record to bound what's being claimed. Multiple checks fired (CK-01, CK-03, CK-04, CK-05) and two more couldn't run (CK-02, CK-06) because the study record wasn't declared.

---

### A note on what's missing

Two things would materially strengthen any future QA pass on this:

1. **A study record.** Right now there's no declared decision, no questions, and no limits. That means two checks (CK-02, CK-06) can't run at all, and the readout can't tell you whether this finding even answers something the team set out to learn. The template is at `templates/study-record.md` — the team should fill it in themselves.

2. **Participant evidence, or an explicit acknowledgment there is none.** If this claim is meant as a hypothesis to go test, it should be labelled as such ("Working hypothesis: hikers want offline maps — to be tested in [study]"). As written, it reads as a settled finding driving a default change, which the evidence doesn't support.

I won't draft either of these for you — beliefs, questions and limits are only useful when written by the people who hold them.
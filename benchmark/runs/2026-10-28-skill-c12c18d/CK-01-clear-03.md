# QA Readout

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | Declared | B-01 | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "Working assumption B-01 (agreed by the whole team, not yet tested with hikers): offer offline download when a hiker saves a trail. We'll check whether hikers actually lose signal in the next round of sessions."

**Evidence strength:** WEAK
The claim is openly presented as a working assumption to be tested, not as a finding. There's no participant evidence behind it — just a team-agreed belief rated low confidence, drawn from the team's own experience on trails.

**Claim matches its evidence:** Yes — the claim says exactly what the evidence supports: a declared assumption, labelled as such, with a stated plan to test it. It doesn't overclaim scope or certainty.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** Hikers in the target market may have reliable signal on the trails they use (urban-fringe trails, popular national park trails with cell coverage), making offline download a solution to a non-problem. The team's "several of us last summer" is a small, self-selected sample from a group that isn't the target users.
- **What would overturn this finding:** Hiker sessions or diary data showing that on the trails they actually use, signal is reliable enough that saved-trail data loads on demand; or that hikers already solve this with other tools (downloaded maps apps, screenshots) and wouldn't use an in-app offline download.
- **Where the evidence underdetermines the claim:** Entirely. No hiker evidence exists in this set. The claim acknowledges this directly.

**Counter-evidence:** None cited.

**Unsupported claims:** The design direction (offer offline download when a hiker saves a trail) has no participant evidence behind it — but it's declared as an assumption to test, not as a finding, which is the correct framing.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim labels itself "not yet tested with hikers" and frames B-01 as a working assumption, not as proven. | n/a |
| CK-04 Product finding without a human story | CLEAR | The product direction has no people-side evidence, but it rests on B-01, a belief with `agreed_by_all = yes`, presented explicitly as a declared working assumption. | n/a |
| CK-05 Scope and certainty inflation | CLEAR | Scope and certainty are calibrated — "working assumption", "not yet tested", "we'll check". | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The direction is specific (offline download when a trail is saved) and actionable. |
| P-03 Transcript Literalism | No | No transcripts in play; nothing is being over-read from text. |
| P-04 Volume Mistaken for Strength | No | No volume claim is being made. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence filed and ignored — there's no evidence either way. |
| P-08 Narrowing Sold as Resolving | No | The claim doesn't assert the fix will work; it proposes testing. |

### Where does it apply?

**Scope:** The claim applies to hikers using the app on trails. No study limits are declared, so there's nothing explicit to check the scope against — but the claim stays modest (an assumption to test), so scope isn't being stretched.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no `cannot_claim` to check against. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is being made across populations or markets. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| Hikers lose phone signal on most trails (B-01) | Team members' own hiking experiences last summer | Observed (by team members, not participants) | Yes — traces to B-01, which cites `own_experience`. |
| Offer offline download when a hiker saves a trail | Design inference from B-01 | Inferred | Yes — labelled as a working assumption derived from B-01. |

No claim is left dangling without a source; the sources are modest and declared as such.

**Checked against:** B-01 from the belief register. No declared questions or limits to check against.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No questions declared in a study record. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research is being contradicted or re-presented as new. |
| P-07 Trust Without Process | No | The reasoning is visible: B-01 is agreed, untested, so treat it as an assumption to check. |

### Is it theirs or ours?

**Beliefs and evidence:** The entire claim comes from the team — B-01, rated low confidence, drawn from team members' own hiking experiences. Nothing comes from hikers themselves. This is declared openly.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | CLEAR | B-01 is rated `low` confidence, not `high`, so part (a) doesn't fire. The claim doesn't present team agreement as evidence from participants — it presents it as a declared working assumption, so part (b) doesn't fire either. | n/a |

### Tacit-knowledge prompt
Not applicable — no sessions have been run yet.

### Decision boundary
- **Supports:** Treating offline download as a hypothesis worth testing in the next round of hiker sessions. Prioritising "do hikers lose signal on trails they actually use?" as a question to answer before building.
- **Doesn't support:** Building offline download as a shipped feature; claiming hikers want or need it; prioritising this over other untested assumptions.
- **What would close the gap:** A short round of hiker sessions or a diary study that asks (a) which trails they use, (b) whether they lose signal on those trails, and (c) what they currently do about it. One or two sessions would separate "real problem" from "team's weekend problem".

**Safe to act on:** Not yet — the claim is honestly labelled as an untested assumption, which is correct practice, but it isn't a finding and shouldn't drive a build decision. It's ready to be tested, which is what the claim itself says.

---

**One note on process:** no study record was declared, so CK-02 and CK-06 report NOT RUN rather than CLEAR. For an assumption-to-test like this one that doesn't matter much — but once hiker sessions run and real findings come in, write a study record first (see `templates/study-record.md`). Without declared questions and limits, two of the six checks will keep reporting NOT RUN, and the readout will be weaker than it needs to be.
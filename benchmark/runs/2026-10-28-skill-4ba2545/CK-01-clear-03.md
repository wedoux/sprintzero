## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | Declared | B-01 | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

Note: the user chose not to declare a study record. CK-02 and CK-06 can't run without it.

## Finding: "Working assumption B-01 (agreed by the whole team, not yet tested with hikers): offer offline download when a hiker saves a trail. We'll check whether hikers actually lose signal in the next round of sessions."

**Evidence strength:** WEAK
The claim rests on one low-confidence belief, held from the team's own experience, with no participant evidence. It is correctly labelled as such.

**Claim matches its evidence:** Yes — the claim is explicitly presented as a working assumption, not a tested finding, and names the test that would move it forward.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** Hikers may already use dedicated offline map apps (AllTrails, OS Maps, Gaia) and not expect this app to fill that role; or signal loss on "most trails" may be a product of where this team hikes, not where the user base hikes.
- **What would overturn this finding:** Sessions with hikers showing that (a) they don't experience signal loss often enough to care, or (b) they already have an offline tool they trust and wouldn't switch. The team has explicitly scheduled this check.
- **Where the evidence underdetermines the claim:** The claim about hikers' signal loss has no participant evidence at all. This is acknowledged.

**Counter-evidence:** None cited; none to argue against.

**Unsupported claims:** The underlying belief ("hikers lose phone signal on most trails") has no participant evidence — acknowledged in the claim itself as "not yet tested."

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim labels itself a working assumption and names a test, not a validated finding. | n/a |
| CK-04 Product finding without a human story | CLEAR | No people-side evidence, but B-01 has `agreed_by_all = yes` and is presented as a declared working assumption. | n/a |
| CK-05 Scope and certainty inflation | CLEAR | Scope and certainty are honestly scoped ("working assumption", "not yet tested", "we'll check"). | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim names a specific trigger (saving a trail) and a specific product behaviour (offer offline download). |
| P-03 Transcript Literalism | No | No transcript involved. |
| P-04 Volume Mistaken for Strength | No | No volume claim is made. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence listed; none to face. |
| P-08 Narrowing Sold as Resolving | No | The claim doesn't assert a fix will work; it proposes a feature on an untested assumption and schedules the test. |

### Where does it apply?

**Scope:** The claim covers hikers using this app to save trails. No boundary is stated for which hikers, which regions, or which trails — but as a working assumption rather than a finding, this is acceptable; the forthcoming sessions should set that boundary.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no limits to check against. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is made. |

### Could someone retrace it?

**Provenance**

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| Hikers lose phone signal on most trails | B-01 (team's own hiking experience last summer) | Inferred from own experience | Yes — traces to B-01, which is honestly labelled low confidence from own_experience |
| Offering offline download when a hiker saves a trail is the right response | B-01 + team agreement | Inferred | Yes — presented as a working assumption, not a finding |
| Hikers' actual signal loss will be checked in the next round of sessions | Stated commitment | Stated | Yes |

**Checked against:** B-01 from the belief register. No questions or limits were declared, so CK-02 and CK-06 did not run.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study record declared, so no questions to check against. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research mentioned in either direction. |
| P-07 Trust Without Process | No | The reasoning is visible: a low-confidence belief, team-agreed, explicitly flagged as untested, with a named next step. |

### Is it theirs or ours?

**Beliefs and evidence:** Everything in this claim comes from the team's side (B-01, own experience, agreed by all). None of it comes from hikers. The claim says so plainly.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | CLEAR | B-01 is low confidence from own_experience; the claim treats it as a working assumption, not a confident one. Part (b) does not fire: the agreement is presented as the status of a declared assumption, not as evidence that hikers lose signal. | n/a |

### Tacit-knowledge prompt
Not applicable — nobody has run sessions with hikers yet. The question for the upcoming round is already named in the claim: do hikers actually lose signal on the trails they use this app for, and does it matter enough to change their behaviour?

### Decision boundary
- **Supports:** Treating offline download as a working hypothesis worth testing in the next round. Building a quick prototype or discussion aid for those sessions.
- **Doesn't support:** Shipping the feature, prioritising it on the roadmap over tested needs, or stating that hikers need offline download.
- **What would close the gap:** Sessions with hikers (ideally in the regions and on the trail types your real users hike) covering: how often they lose signal, what they do when it happens, and whether they already use another offline tool.

**Safe to act on:** Yes — but only for what it actually proposes, which is testing the assumption in the next round. Not safe to act on as a basis for shipping the feature.

---

## A note on what this pass could and couldn't check

Three of six CK checks ran. CK-02 and CK-06 are reported as NOT RUN because no study record was declared — this is the user's choice, named rather than hidden. CK-01, CK-03, CK-04 and CK-05 ran on complete input and are clear.

The claim is unusual in a good way: it is an honest statement of what the team believes and doesn't yet know, with a named next step. The QA pass is designed to catch overclaiming; there is none here to catch. If the next round of sessions produces evidence, run this skill again on the finding that comes out of it — that is where the real test will be.
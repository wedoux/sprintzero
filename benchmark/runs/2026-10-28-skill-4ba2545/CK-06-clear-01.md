# QA Readout

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | Declared | Q-01 | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "5 of 6 participants did not notice the new filter button without being prompted."

**Evidence strength:** STRONG
In this small sample, five of six participants said directly that they didn't notice the filter button on their own. The evidence is first-person, consistent across participants, and the claim counts rather than generalises.

**Claim matches its evidence:** Yes — the claim reports the count in the sample without extending it to "users" generally or asserting a cause.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** Participants may have noticed the button peripherally but reported not seeing it because they didn't use it during the task — self-report about noticing is weaker than observed gaze or clicks. The sessions were moderated, so moderator phrasing before the task could also prime "I didn't see it" answers.
- **What would overturn this finding:** Session recordings or eye-tracking showing that participants looked at or hovered over the filter button early in the task despite reporting they hadn't seen it; or a task log showing filter interactions before the prompt.
- **Where the evidence underdetermines the claim:** The claim is a count of self-reports, not of observed non-noticing. It also doesn't tell us *why* the button was missed (placement, visual weight, labelling, competing elements) — only that it was.

**Counter-evidence:** INT-06 noticed it immediately and called the spot "pretty obvious." The claim already accounts for this by saying 5 of 6, not all; it doesn't overturn the finding but it is a real signal that the button is discoverable for some users and worth asking why INT-06 differed.

**Unsupported claims:** None — each of the five non-noticing cases is directly quoted, and the sixth is accounted for.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim counts a behaviour in the sample; it doesn't present a need, feeling or attitude as proven. | n/a |
| CK-04 Product finding without a human story | CLEAR | The claim is about participants' noticing behaviour and cites six first-person statements. | n/a |
| CK-05 Scope and certainty inflation | CLEAR | "5 of 6 participants" matches the evidence exactly; no "users" generalisation and no causal claim. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim names an observable behaviour (not noticing) with a specific count. |
| P-03 Transcript Literalism | Yes | The claim rests entirely on what participants said they noticed. Self-report about noticing is a known weak signal — someone can look at a button, not use it, and later say they didn't see it. The readout doesn't flag this gap, and a moderator who ran the sessions might know whether participants' eyes went to the button area even when they said they hadn't noticed it. |
| P-04 Volume Mistaken for Strength | No, with a caveat | All six units are moderated interviews — one source type. The claim stays within that source (it reports what participants said, not what is true of users), so this is honest rather than inflated. If the finding were later written up as "the filter button is not discoverable," single-source would start to matter. |
| P-05 Counter-Evidence Filed, Not Faced | No | INT-06 is included in the denominator rather than set aside. |
| P-08 Narrowing Sold as Resolving | No | The claim doesn't propose a fix or claim a cause. |

### Where does it apply?

**Scope:** Six moderated sessions. The claim stays inside that sample — it says "5 of 6 participants," not "users."

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No limits were declared, so there is no `cannot_claim` to check against. On the face of it the claim stays inside the six sessions, but limits the team would normally record (device, context of use, user segment, whether sessions were remote or in person) aren't written down, so the check can't confirm the claim respects them. | — |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer to a different population is claimed. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| INT-01 did not notice the filter | INT-01: "I didn't see a way to filter until you pointed at it." | Observed (self-report) | Yes |
| INT-02 did not notice the filter | INT-02: "I never noticed there was a filter option…" | Observed (self-report) | Yes |
| INT-03 did not notice the filter unprompted | INT-03: "Took me the whole task to realize I could filter - found it by accident." | Inferred — "by accident" implies unprompted, but is slightly different from "did not notice until prompted." Still fairly classified as non-noticing. | Yes |
| INT-04 did not notice the filter | INT-04: "Didn't see it…" | Observed (self-report) | Yes |
| INT-05 did not notice unprompted | INT-05: "I spotted it eventually but only because I was told something was there." | Observed (self-report) | Yes |
| INT-06 noticed the filter | INT-06: "Saw it right away…" | Observed (self-report) | Yes |

Every claim traces to a quoted unit.

**Checked against:** Q-01 ("Do users notice the new filter button without being told it's there?"). No beliefs or limits were declared, so nothing to check against on those axes.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | CLEAR | The claim directly answers Q-01. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No, with a caveat | No prior research was supplied either way; if earlier discoverability work exists, it should be cross-referenced. |
| P-07 Trust Without Process | No | The reasoning (quote-by-quote count) is visible and reconstructable. |

### Is it theirs or ours?

**Beliefs and evidence:** The claim rests entirely on what the six participants said. No belief register was declared, so there's no documented prior conviction to check against — but the finding doesn't lean on authority or team opinion.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN | No belief register was declared, so part (a) can't run. Part (b) is clear — the claim's support is participants, not an attributed opinion — but a check that didn't fully run is not reported as passed. | — |

### Tacit-knowledge prompt
For INT-01, INT-02, INT-04 and INT-05 — did their gaze or cursor ever land on the filter area before they said they hadn't noticed it? And for INT-06, was there anything about how that session was set up (task order, prior exposure, device) that might explain why they spotted it immediately when the others didn't?

### Decision boundary
- **Supports:** In this sample of six moderated sessions, most participants reported not noticing the filter button without a prompt. This is enough to treat discoverability as a real concern worth investigating, and to justify looking at the entry point more closely.
- **Doesn't support:** It doesn't support a claim about "users" in general (n=6, one source type, self-report). It doesn't identify *why* the button is missed, and so doesn't tell the team what to change. It doesn't rule out that participants saw the button peripherally and just didn't use it.
- **What would close the gap:** Session recordings reviewed for gaze or cursor behaviour on the filter area before the prompt. That one addition would separate "didn't see it" from "didn't use it," which is the difference between a placement/visibility problem and a labelling/affordance problem.

**Safe to act on:** Not yet — the count is honest and the signal is real, but CK-01 and CK-02 are NOT RUN (no belief register, no declared limits), and P-03 flags that self-reported noticing is a weaker signal than the readout treats it as. Enough to prioritise a closer look at discoverability; not enough to commit to a redesign direction.
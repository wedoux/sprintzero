I'll run the QA pass on this claim. Let me work through the checklist.

**Step 0 — Declarations.** None declared. Before proceeding, I want to flag: beliefs and questions are only useful when written by the people who hold them. If you want a more thorough pass, see `templates/belief-register.md` and `templates/study-record.md` — but you've given me enough to review the claim as-is, so I'll proceed. Several checks will report NOT RUN as a result.

**Step 1 — Conclusion present?** Yes: "ship dark mode as the default."

**Step 2 — Provenance.** The claim cites one source: "the PM says everyone she's spoken to prefers it." No participant evidence, no numbers, no transcripts.

**Step 3 — Falsification.** Strongest counter: the people the PM spoke to may be a self-selecting group (colleagues, vocal users), not representative. What would overturn it: a sample of actual users showing mixed or light-mode preference, or usage data from a dark-mode beta.

**Steps 4–5 — Pitfalls and CK pass.** Running the readout now.

---

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "Our users want dark mode — the PM says everyone she's spoken to prefers it, so we should ship it as the default."

**Evidence strength:** WEAK
The only support offered is one person's informal report of unspecified conversations. There is no participant evidence, no count, no method, no sample.

**Claim matches its evidence:** No — the claim generalises from "everyone the PM spoke to" (an unknown, likely self-selected group) to "our users" (everyone), and jumps from a stated preference to a default-setting product decision.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** The people the PM spoke to are not a representative sample. They may be colleagues, power users, or people who raised the topic unprompted (which selects for people who care). Users who are happy with light mode have no reason to mention it.
- **What would overturn this finding:** A survey or usage sample showing that a meaningful share of users prefer light mode, or telemetry from a dark-mode opt-in showing low adoption.
- **Where the evidence underdetermines the claim:** Entirely. We don't know how many people the PM spoke to, who they were, what they were asked, or whether they'd want dark mode as the *default* versus as an *option*.

**Counter-evidence:** None cited — but note that the absence of counter-evidence isn't support; no one went looking.

**Unsupported claims:** All of them. "Our users want dark mode," "everyone prefers it," and "we should ship it as the default" each rest on the same single attributed opinion.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | FIRES | "This treats what we learned about people as proven. Only a product can be validated." The claim asserts a user preference ("our users want dark mode") as established fact. | n/a |
| CK-04 Product finding without a human story | NOT RUN | No people-side evidence is cited, and no belief register was declared, so I can't tell whether this rests on an agreed working assumption. | n/a |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." "Everyone she's spoken to" (unknown N, unknown selection) becomes "our users" (everyone). A stated preference becomes a case for making it the *default*. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "Users want dark mode" is a label with no behaviour, trigger or consequence specified. Would read identically in a report about any other product. |
| P-03 Transcript Literalism | No | No transcript involved. |
| P-04 Volume Mistaken for Strength | Yes | A single source type (one person's informal conversations) is being used to support a confident, universal claim. Would not survive if nine of the ten reported conversations vanished — because we don't know there were ten. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence was raised — but only because none was sought. |
| P-08 Narrowing Sold as Resolving | No | Not applicable. |

### Where does it apply?

**Scope:** Unknown. We don't know who the PM spoke to, in what context, or on what platform. The claim applies to "our users" but no sample is defined.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no limits to check against. Note: this doesn't mean there are no limits — it means none have been written down. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is being made (no "may not apply to X"). |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "Our users want dark mode" | PM's report of her own conversations | Inferred | No — no record of who was spoken to, how many, or what was said |
| "Everyone she's spoken to prefers it" | PM's statement | Inferred (summary) | No — no list, no count, no transcript |
| "We should ship it as the default" | None | Inferred (recommendation) | No — no evidence links preference to default-setting |

Every claim in the finding is untraceable.

**Checked against:** Nothing declared.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study record declared, so no questions to map the finding against. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | Yes (likely) | No reference to prior research, telemetry, or existing dark-mode usage data. If a previous study exists, this didn't check. If none exists, that should be stated. |
| P-07 Trust Without Process | Yes | The recommendation ("ship it as the default") is stated with no visible reasoning chain connecting the evidence to the decision. We can't audit how "PM spoke to some people" became "default for everyone." |

### Is it theirs or ours?

**Beliefs and evidence:** All of it is "ours," specifically one person's. No participant evidence appears in the claim at all. The PM's conversations are an authority-and-proxy signal, not user research.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | FIRES (part b) | "This confidence comes from who said it, not from evidence." The entire support for the claim is "the PM says." That is attributed opinion, not evidence from participants. Part (a) is NOT RUN because no belief register was declared. | n/a |

### Tacit-knowledge prompt
Not applicable — no sessions were run. The question to ask the PM is simpler and more concrete: *"How many people did you speak to, who were they, and did you ask them whether they wanted dark mode as an option or as the default?"*

### Decision boundary
- **Supports:** That at least one person (the PM) believes some users prefer dark mode. That dark mode is worth investigating.
- **Doesn't support:** Any claim about what "our users" want. Any claim about preference strength. Any claim about default settings specifically (preference for a feature ≠ preference for it being on by default).
- **What would close the gap:** A simple in-product survey, or (better) a dark-mode opt-in with usage telemetry. The question isn't "do people like dark mode" — it's "what proportion of users would actively choose it, and would they want it as the default?"

**Safe to act on:** Not yet — the claim is one person's attributed opinion, generalised to all users and escalated to a default-setting decision. Three checks fired (CK-01, CK-03, CK-05) and four pitfalls (P-01, P-04, P-02, P-07). Shipping dark mode as an *option* is a different, much smaller decision that this evidence might reasonably support; shipping it as the *default* is not.
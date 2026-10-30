# QA Readout

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | Declared | B-01 | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "Users want dark mode, so we should ship it as the default theme."

**Evidence strength:** WEAK
The claim rests on one third-party industry survey about *theme preference at night*, and leaps from there to a product default decision. No evidence from this team's own users is cited.

**Claim matches its evidence:** No — the cited belief is about preference at night; the claim strips the time-of-day qualifier and converts preference into "should be the default."

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** Users prefer dark mode *at night* but light mode or system-default during the day. Shipping dark as the always-on default could worsen the daytime experience for the majority of use.
- **What would overturn this finding:** Usage data or interviews from this product's own users showing either (a) they predominantly use the app in daytime contexts, or (b) when given dark mode as an option, most leave the default (whatever it is) in place.
- **Where the evidence underdetermines the claim:** The cited study tells us about *preference* in a specific context (night, mobile, note-taking). It says nothing about defaults, nothing about this product's users, and nothing about whether "prefer" means "want it on all the time."

**Counter-evidence:** None supplied — but note that the absence of counter-evidence here is a product of there being almost no evidence at all, not a sign the claim is unchallenged.

**Unsupported claims:** The jump from "prefer dark theme at night" to "should ship as default theme" has no evidence behind it. Preference ≠ default; night ≠ always.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | Not a claim-about-people treated as validated; the people-claim ("users want dark mode") is stated as fact rather than "confirmed," but see CK-05. | n/a |
| CK-04 Product finding without a human story | FIRES | "This product finding has no evidence about people behind it, and no assumption the team agreed to." The product claim ("ship it as the default theme") cites no people-side evidence from this product's users. B-01 is agreed, but it's about theme preference at night, not about defaults — it doesn't support the specific product claim. | B-01 (supports a weaker claim than the one made) |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." The cited belief is about "dark theme at night"; the claim drops "at night" and extends preference into a default-setting decision. | B-01 |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "Users want dark mode" — swap the product name and this sentence works for any app. No behaviour, no trigger, no consequence tied to this product. |
| P-03 Transcript Literalism | No | No transcript or session material in play. |
| P-04 Volume Mistaken for Strength | Yes | A single third-party survey is being treated as sufficient to drive a default-setting decision. One source type, no corroboration. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence was raised to be filed. |
| P-08 Narrowing Sold as Resolving | Yes | The evidence narrows the hypothesis space (dark mode is plausibly wanted at night) but is being sold as resolving the default-setting question. |

### Where does it apply?

**Scope:** The cited study covers mobile note-taking app users at night. The claim applies to "users" with no qualifier and recommends an always-on default. The scope has been silently widened on two axes (time of day, and from preference to default).

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no `cannot_claim` to check against. Note: CK-05 already catches the scope overreach against B-01. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer caveat is being offered — the problem here is the opposite, a transfer with no hedge at all. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "Users want dark mode" | B-01 (Nielsen Norman Group survey, 2025) | Inferred — B-01 is about preference at night; "want dark mode" is a broader restatement | Partially — the source exists, but the claim has been generalised beyond what B-01 states |
| "so we should ship it as the default theme" | not cited | Inferred, with no evidence behind it | No |

**Checked against:** B-01. No questions or limits were declared, so this finding wasn't checked for drift or for crossing study boundaries.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study questions declared. Can't tell whether this answers a question that was asked. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research context was supplied to compare against. |
| P-07 Trust Without Process | Yes | The claim asserts a conclusion ("we should ship it as the default") with no reasoning chain between evidence and recommendation. |

### Is it theirs or ours?

**Beliefs and evidence:** The entire claim rests on B-01, a third-party study. No evidence from this product's own participants is cited. B-01 is marked `high` confidence with `third_party_study` as its source, so CK-01 part (a) does not fire on source type — but the belief supports a narrower claim than the one being made.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | CLEAR | B-01's source is `third_party_study` with a named `source_ref`, not authority/proxy/own experience. No attributed-opinion phrasing in the claim. The real problem — the claim stretching beyond what B-01 supports — is caught by CK-05. | n/a |

### Tacit-knowledge prompt
Not applicable — no sessions were run, so no researcher tacit knowledge to tap.

### Decision boundary
- **Supports:** Dark mode is likely wanted by many mobile note-taking users at night (per a third-party survey). Offering dark mode as an option is a defensible investment.
- **Doesn't support:** Shipping dark mode as the *default* theme; any claim about this product's own users; any claim about daytime use.
- **What would close the gap:** Usage data from this product showing when users open the app (time of day, ambient light if available) and, ideally, a small test exposing new users to each default and measuring whether they switch.

**Safe to act on:** Not yet — the claim extends a narrow third-party finding ("prefer dark theme at night") into a product default decision without evidence from this product's users, and the study record needed to bound the claim wasn't declared.
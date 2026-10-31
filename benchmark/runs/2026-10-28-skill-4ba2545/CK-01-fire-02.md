I'll run the QA pass on this claim. First, a note on inputs.

## Inputs

You've declared no belief register, no study record, and cited no evidence. That's your call to make, but it means most of the checks below will report NOT RUN — not pass. A check that didn't run is never reported as passed.

If you'd like to make this QA pass more useful, you could write:
- A belief register ([templates/belief-register.md](templates/belief-register.md)) — what you and the team believed about dark mode before any research, and why.
- A study record ([templates/study-record.md](templates/study-record.md)) — what questions this research asked, what evidence it gathered, and what it can't claim.

I won't draft either for you; the people who hold the beliefs and asked the questions have to write them, or they're not yours to be held to.

I'll proceed with what you've given me.

---

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "Our users want dark mode — the PM says everyone she's spoken to prefers it, so we should ship it as the default."

**Evidence strength:** WEAK

The claim rests entirely on one person's summary of unspecified conversations with an unspecified number of unspecified people. There is no evidence here that a reviewer can inspect.

**Claim matches its evidence:** No — the claim says "our users want dark mode" and recommends shipping it as default, but the only support offered is an attributed opinion ("the PM says") with no underlying evidence cited. CK-01 part (b), CK-03, CK-04 and CK-05 all fire; P-01, P-05 and P-07 are triggered.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** The people the PM spoke to are a self-selected or convenience sample (likely other product-literate colleagues, or users who already asked about dark mode) and don't represent the user base. Preferring dark mode when asked is also different from wanting it as the default — many users who like having dark mode available still expect light mode on first launch.
- **What would overturn this finding:** Evidence from a representative sample of actual users showing either (a) that most don't prefer dark mode, or (b) that preference-when-asked doesn't predict default-setting satisfaction. A survey of current users, or analytics from a cohort shown a dark-mode toggle, would do it.
- **Where the evidence underdetermines the claim:** Everywhere. We don't know how many people the PM spoke to, who they were, how she asked, or whether "prefers it" meant "would use it if available" or "wants it as the default on install". Those are different claims.

**Counter-evidence:** None cited — but the absence of counter-evidence here is not reassuring, because no evidence of any kind is cited.

**Unsupported claims:** All of them. "Our users want dark mode", "everyone she's spoken to prefers it", and "we should ship it as the default" are each unsupported by any evidence a reviewer could check.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | FIRES | "This treats what we learned about people as proven. Only a product can be validated." The claim states "Our users want dark mode" as established fact about what people want. | n/a |
| CK-04 Product finding without a human story | NOT RUN | The claim about the product (ship dark mode as default) cites no people-side evidence, but with no belief register declared, I can't check whether an agreed working assumption supports it. | n/a |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." "Everyone she's spoken to" (unknown number, unknown selection) becomes "our users" (the whole user base), and "prefers it" becomes grounds for shipping as the default. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "Users want dark mode" is a label, not a behaviour. No trigger (when do they want it?), no consequence (what breaks without it?), no observable action. The sentence would read the same for any product. |
| P-03 Transcript Literalism | No | No transcript or source material was provided, so this doesn't apply. |
| P-04 Volume Mistaken for Strength | No | There's no volume claim to inflate — just one source, acknowledged as one source. (CK-01 part b covers the real problem.) |
| P-05 Counter-Evidence Filed, Not Faced | Yes | The claim entertains no counter-hypothesis at all — not even the obvious one that "prefers dark mode when asked" ≠ "wants it as the default". |
| P-08 Narrowing Sold as Resolving | Yes | "Users prefer dark mode" (if true) narrows what to investigate; it does not establish that shipping it as the default will serve users well. The leap from preference to default-shipping is causal overreach. |

### Where does it apply?

**Scope:** Unknown. We don't know who the PM spoke to, how many, in what context, or whether they resemble the user base. The claim applies to "our users" — the entire population — on the basis of an unspecified sample.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no limits to check against. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer claim is being made. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "Our users want dark mode" | "The PM says" — no underlying evidence cited | Inferred (from an attributed opinion) | No — the PM's conversations aren't documented |
| "Everyone she's spoken to prefers it" | PM's own report | Observed by PM, not by reviewer | No — no record of who, how many, or what was asked |
| "We should ship it as the default" | Not supported by any source | Inferred (and a leap from preference to default) | No |

No claim in this finding is traceable to evidence a reviewer could inspect.

**Checked against:** Nothing declared.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study record declared, so no questions to check the finding against. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research was supplied, so I can't check whether this contradicts or restates it. Worth noting: dark mode has been studied widely in industry; if you have prior internal work on it, this finding should reference it. |
| P-07 Trust Without Process | Yes | The recommendation ("we should ship it as the default") is asserted, not derived. There's no reasoning chain between "the PM spoke to some people" and "ship it as default" — the conclusion is stated as if it followed, but the steps aren't there. |

### Is it theirs or ours?

**Beliefs and evidence:** Entirely "ours". The only source is the PM's summary of her own conversations. No participant speaks in this claim; no behaviour is described; no quote is cited. Even the PM's conversations may themselves be a mix of her prior belief and what she heard, but there's no way to tell them apart.

"Everyone she's spoken to prefers it" is also doing work that "agreement" sometimes does — it sounds like confirmation, but it's attributed opinion from one person reporting on others.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | FIRES (part b) | "This confidence comes from who said it, not from evidence." The support offered is "the PM says" — an attributed opinion rather than evidence from participants. Part (a) can't run without a declared belief register, but the mechanism it checks for is clearly present. | n/a |

### Tacit-knowledge prompt
If the PM is available, the specific question worth asking is: **"How many people did you speak to, how did you find them, and what exactly did you ask?"** Not "tell us more" — the actual gap is sample size, sample selection, and question wording. Without those three, "everyone prefers it" is uninterpretable.

A second question, if the first turns up useful ground: **"Did they say they'd prefer dark mode if it were available, or that they'd want it as the default on install?"** Those are different answers to different questions.

### Decision boundary
- **Supports:** That the PM has heard positive signals about dark mode from some people. That's worth taking seriously as a reason to investigate further.
- **Doesn't support:** That "our users" (the user base) want dark mode. That they want it as the default. That shipping it as default would improve the product.
- **What would close the gap:** A short survey of current users asking (a) do you use dark mode in other apps, (b) would you want it in ours, and (c) would you want it on by default or as an option. Even 50 responses from a representative cohort would be stronger than what you have now. If you can run a staged rollout with a toggle and measure retention / toggle behaviour, better still.

**Safe to act on:** Not yet — the claim rests on one person's unverifiable summary, and the leap from "some people the PM spoke to prefer it" to "ship as default" is unsupported. Shipping dark mode as an *option* is a smaller, more reversible decision; shipping it as the *default* changes every current user's experience and should rest on evidence from current users, not conversations with an unspecified group.
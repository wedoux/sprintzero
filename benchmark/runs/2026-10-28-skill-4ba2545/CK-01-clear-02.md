Noting up front: if this synthesis was produced earlier in this same conversation, run the QA in a fresh conversation with only the synthesis and evidence pasted in. A model reviewing its own immediately prior output grades its own homework. I'll proceed on the assumption you brought this in fresh.

Also: no study record was declared. That's your choice to proceed without one, but it means CK-02 and CK-06 will report NOT RUN. If you want those checks to actually run, use [templates/study-record.md](templates/study-record.md) to write one and re-run.

---

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | Declared | B-01 | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

## Finding: "Our founder has always said dark mode matters, and INT-01 and INT-03 both show users actively seeking it out — we should ship it as the default theme."

**Evidence strength:** WEAK
Two interviewees from an unknown total mentioned dark mode, one of them unprompted on install. That is a signal worth noting, not a basis for setting a default theme for everyone.

**Claim matches its evidence:** No — the claim bundles three separate overclaims: (1) founder opinion is treated as supporting evidence, (2) two participants are generalised to "users", and (3) "users want a dark mode toggle" is stretched into "ship it as the default theme", which no participant said.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** A small group of users want dark mode available (a toggle), and the rest either prefer light mode or don't care. Shipping dark as the default would annoy the majority to serve a minority — the exact opposite action to the one the evidence supports.
- **What would overturn this finding:** Usage data from an app that offers a toggle showing most users leave the default; or interviews/survey evidence showing a substantial share of users prefer light mode or react negatively to dark as default.
- **Where the evidence underdetermines the claim:** We don't know how many sessions were run in total (2 of how many?), we have no evidence about what users want as a *default* (only that two sought a toggle), and we have no evidence from users who prefer light mode.

**Counter-evidence:** None cited in the material. The design lead's dissent on B-01 ("wants usage data before treating it as settled") is noted in the register but never addressed in the claim.

**Unsupported claims:** "Ship it as the default theme" — no participant said anything about defaults. Both INT-01 and INT-03 describe seeking out a toggle, which is evidence for *offering* dark mode, not for making it the default.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | Claim is phrased as a product recommendation, not as a validated truth about people. | n/a |
| CK-04 Product finding without a human story | CLEAR | The product claim cites INT-01 and INT-03 (people-side evidence). | n/a |
| CK-05 Scope and certainty inflation | FIRES | "This says more, or says it more surely, than the evidence allows." Two interviewees become "users", and seeking out a toggle becomes "ship it as the default theme". | Evidence covers 2 participants seeking a toggle; claim covers all users and a default-theme decision. |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim is specific enough to act on (which is part of the problem — it's specifically overreaching). |
| P-03 Transcript Literalism | No | No ambiguity in the quotes being over-trusted; the problem is scope, not interpretation. |
| P-04 Volume Mistaken for Strength | Yes | Two interview quotes from one source type are treated as sufficient to set a product default. No corroboration from analytics, reviews, or survey data. |
| P-05 Counter-Evidence Filed, Not Faced | Yes | The design lead's dissent on B-01 ("wants usage data before treating it as settled") sits in the register unaddressed. The claim proceeds as if the dissent doesn't exist. |
| P-08 Narrowing Sold as Resolving | Yes | "Two users want a toggle" narrows the hypothesis space (dark mode is wanted by someone); it is sold as resolving the question (ship as default) that the evidence doesn't speak to. |

### Where does it apply?

**Scope:** The evidence covers 2 interview participants (of an unknown total). The claim covers all users and a product-wide default. The gap is unbounded because we don't know the denominator.

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
| Founder has always said dark mode matters | B-01 rationale | Observed (as an opinion) | Yes — but it's opinion, not evidence about users |
| INT-01 and INT-03 show users actively seeking out dark mode | INT-01, INT-03 quotes | Observed | Yes |
| "Users" (generally) seek out dark mode | — | Inferred from n=2 | No — generalisation unsupported |
| Dark mode should be the default theme | — | Inferred | No — no participant spoke about defaults; both described seeking out a toggle |

**Checked against:** B-01 only. No questions or limits were declared.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study record declared, so no questions to map against. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research is in the material to check against. If prior dark-mode research or analytics exists, the claim doesn't reference it — worth asking. |
| P-07 Trust Without Process | Yes | "Should ship it as the default theme" is asserted without reasoning. The jump from "two people wanted a toggle" to "default for everyone" is never argued. |

### Is it theirs or ours?

**Beliefs and evidence:** The founder's view (B-01) and the two interview quotes are both offered as support, side by side, as if they add up. They don't: the founder's opinion isn't evidence about users, and the design lead's dissent on this very belief is in the register and ignored.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | FIRES | "This confidence comes from who said it, not from evidence." Part (a): B-01 is confidence `high`, source `authority`, with no supporting evidence beyond the founder's say-so, and the claim restates it as support. Part (b): "Our founder has always said dark mode matters" is attributed opinion offered as backing for a claim about users. | B-01 |

### Tacit-knowledge prompt
How many interviews did the study include in total, and did any participant mention a preference for light mode or react negatively to dark interfaces? The claim's scope depends on the denominator, which isn't in the material.

### Decision boundary
- **Supports:** At least some users actively look for a dark mode option; offering a dark mode toggle is worth considering.
- **Doesn't support:** That most users want dark mode; that dark mode should be the default; that founder conviction is confirmed by this evidence.
- **What would close the gap:** Usage data from any product that already offers a dark mode toggle, showing the share of users who switch. One number would move this from "ship as default" being obviously premature to being either supported or clearly wrong.

**Safe to act on:** Not yet — the claim says more than its evidence (2 participants wanting a toggle ≠ all users wanting a default), rests partly on authority (B-01) rather than evidence, and ignores a declared internal dissent on that very belief. Shipping a *toggle* might be defensible on this evidence; shipping dark as the *default* is not.
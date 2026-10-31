# QA Readout

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

**Note on declarations.** The user chose to proceed without a belief register or study record. This limits what can be checked: CK-02, CK-06, and CK-01 part (a) cannot run. If a sharper QA pass is wanted, the templates at `templates/belief-register.md` and `templates/study-record.md` would let more of the checks fire or clear.

---

## Finding: "Early signal suggests some users may prefer voice input over typing; more sessions are needed to confirm."

**Evidence strength:** WEAK
Two participants, both expressing the same preference in one sentence each, in what appears to be a single study. The signal is real but too thin to carry weight on its own.

**Claim matches its evidence:** Yes — the claim is hedged in all three ways the evidence requires: scope ("some users"), certainty ("may prefer", "early signal"), and an explicit call for more data.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** Both participants were asked a leading question, or were primed to compare voice to typing in a context that favoured voice (e.g., mobile, hands-busy, no keyboard nearby). Without the interview context, we can't tell whether they volunteered this preference or responded to a prompt that framed the choice.
- **What would overturn this finding:** Evidence that INT-01 and INT-02 said this only in response to "would you prefer voice or typing?" (a leading frame), or that in observed behaviour the same participants reached for the keyboard first. Also: a larger sample where the preference does not recur.
- **Where the evidence underdetermines the claim:** Everything about context is missing — device, task, setting, whether voice was already available in the product being discussed, whether these were the only two participants or two of many. We don't know if 2 of 2 said this or 2 of 20.

**Counter-evidence:** None presented. Note that absence of counter-evidence in a 2-unit sample is not reassuring — it's a feature of the sample size.

**Unsupported claims:** None — every part of the claim ("some", "may", "more sessions needed") is defensible against the two quotes.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | CLEAR | The claim uses "may prefer" and "early signal", not validated or confirmed language. | n/a |
| CK-04 Product finding without a human story | CLEAR | The claim is about people's preferences, not a product decision, and it cites people-side evidence (INT-01, INT-02). | n/a |
| CK-05 Scope and certainty inflation | CLEAR | "Some users may prefer" matches a 2-participant signal; "more sessions needed" names the limit. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | "Prefer voice input over typing" is an observable, specific behavioural preference, not a generic label. |
| P-03 Transcript Literalism | No | The claim doesn't over-trust the quotes — it explicitly flags insufficiency. |
| P-04 Volume Mistaken for Strength | No | Confidence is not inflated; the claim says WEAK/early in its own words. |
| P-05 Counter-Evidence Filed, Not Faced | No | No counter-evidence was filed, so nothing was dodged. (This is not the same as counter-evidence being absent in the world.) |
| P-08 Narrowing Sold as Resolving | No | No claim about what the team can now do or fix. |

### Where does it apply?

**Scope:** Two interview participants, context unspecified. The claim stays inside this with "some users".

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record was declared, so no limits exist to check against. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer across populations is claimed. |

### Could someone retrace it?

**Provenance**
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| Some users may prefer voice input over typing | INT-01 ("rather just say it out loud than type it"), INT-02 ("talking is faster for me than hunting for the keyboard") | Inferred (preference inferred from stated reasons) | Yes |
| More sessions are needed to confirm | — | Inferred from sample size | Yes (self-evident from n=2) |

**Checked against:** Nothing declared.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No study questions were declared, so the claim cannot be mapped to one. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | No prior research is referenced or available to contradict. (Note: this doesn't mean no prior research exists — just that none was in scope.) |
| P-07 Trust Without Process | No | The reasoning (two quotes → tentative, hedged inference) is reconstructable from the claim itself. |

### Is it theirs or ours?

**Beliefs and evidence:** The claim rests entirely on what two participants said. No stakeholder opinion, authority, or team belief is cited as support.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | CLEAR | No belief register was declared, so part (a) couldn't run; part (b) checked on the claim alone — no attributed opinion is used as support. | n/a |

### Tacit-knowledge prompt
In what context did INT-01 and INT-02 raise voice vs. typing? Did they volunteer it, or did a question frame the comparison? Were these the only two participants to mention it, or were there others whose contrary preferences aren't in this excerpt?

### Decision boundary
- **Supports:** Noting voice-vs-typing preference as a question worth investigating in a larger or more structured study.
- **Doesn't support:** Any product decision about voice input — prioritisation, scoping, resourcing. Any claim about what proportion of users prefer voice. Any claim about why they prefer it (speed, embarrassment, physical constraint — the quotes hint at speed but don't settle it).
- **What would close the gap:** A study with a sample large enough that the preference's rate becomes meaningful (not two anecdotes), and with context — device, task, whether voice was offered unprompted — recorded.

**Safe to act on:** Not yet — the claim is honest, but the evidence is thin, and two checks could not run because no belief register or study record was declared.

---

## Summary

This is a well-formed cautious claim on very thin evidence. The researcher did the hard part — not overclaiming — correctly. There is nothing to fix in how the finding is stated.

What would make this QA pass sharper, if the user wants to run it again:
1. **A study record** would let CK-02 and CK-06 run — specifically, whether this question was one the study set out to answer, or an unexpected finding.
2. **A belief register** would let CK-01 part (a) run — specifically, whether anyone on the team already believed users prefer voice, which would change how to read a 2-participant confirmation.
3. **Interview context** (not a declaration, just more evidence) would let the falsification pass bite harder — right now the strongest counter-hypothesis (leading question) can't be ruled in or out.
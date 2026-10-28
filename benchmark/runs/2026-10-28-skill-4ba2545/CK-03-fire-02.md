# UX Research QA Readout

Before I start: these claims appear to come from a very small evidence set (2 interviews cited, but the claims reference 3+2=5 participants — a mismatch worth flagging immediately). I'll proceed with the material you've given me.

A note on process: no belief register or study record was declared. That's your call, but several checks below will report NOT RUN as a result. If you want a fuller QA pass, see `templates/belief-register.md` and `templates/study-record.md` and write your own.

---

## Declared upstream

| Record | Status | Items used | Feeds |
|---|---|---|---|
| Belief register | None declared | none | CK-01 part (a), CK-04 |
| Study record: questions | None declared | none | CK-06 |
| Study record: limits | None declared | none | CK-02 |

---

## Finding: "3 good users completed checkout easily; the 2 bad participants just weren't paying attention."

**Evidence strength:** WEAK
The evidence set shows two interviews, not five. The claim describes five participants, labels them as "good" and "bad", and attributes the struggle to inattention — none of which the cited evidence supports.

**Claim matches its evidence:** No — the claim invents participants, judges them as people, and asserts a cause (inattention) that no evidence establishes.

### Is it true for these people?

**Falsification pass**
- **Strongest counter-hypothesis:** INT-02's struggle reflects a shipping-step usability problem, not inattention. A participant asking for help twice at the same step is a classic signal of a design issue, not a character flaw.
- **What would overturn this finding:** Evidence from the session (observation notes, think-aloud, eye-tracking, or the researcher's recollection) showing INT-02 was genuinely distracted — looking at their phone, interrupted, multitasking — rather than confused by the interface.
- **Where the evidence underdetermines the claim:** The cited excerpts say nothing about attention, nothing about three additional participants, and nothing about what made checkout "easy" for INT-01 or hard for INT-02 beyond the shipping step.

**Counter-evidence:** INT-02's "asked me for help twice" is a specific behavioural signal pointing at the shipping step as a design problem. The claim files this as inattention without arguing why.

**Unsupported claims:**
- The existence of 3 "good users" — only INT-01 is cited.
- The existence of 2 "bad participants" — only INT-02 is cited.
- That anyone "wasn't paying attention" — no evidence about attention appears in either excerpt.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-03 People treated as validated | **FIRES** | "This treats what we learned about people as proven. Only a product can be validated." Triggering text: "good users" and "bad participants" — participants are being judged as people rather than their interaction with the product being evaluated. | n/a |
| CK-04 Product finding without a human story | NOT RUN | No belief register declared, so `agreed_by_all` can't be checked. The claim is primarily about people, not product, so this check is a weak fit regardless. | n/a |
| CK-05 Scope and certainty inflation | **FIRES** | "This says more, or says it more surely, than the evidence allows." Triggering text: "3 good users…the 2 bad participants" — the evidence cites 2 interviews, the claim describes 5 people. Also: "weren't paying attention" asserts a cause the evidence does not establish. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | No | The claim is specific, if wrong. |
| P-03 Transcript Literalism | Yes | The claim treats "asked me for help twice" as evidence of inattention rather than engaging with what a researcher in the room might know about why the participant struggled. |
| P-04 Volume Mistaken for Strength | No | Volume isn't the issue; invented volume is. |
| P-05 Counter-Evidence Filed, Not Faced | Yes | INT-02's help-seeking behaviour is counter-evidence to "checkout works easily" — it's reframed as a participant failure rather than faced as a possible design signal. |
| P-08 Narrowing Sold as Resolving | No | No narrowing is claimed. |

### Where does it apply?

**Scope:** The evidence covers 2 interview participants on a checkout flow. The claim covers 5 participants and asserts causes about their mental states. The scope of the claim exceeds the scope of the evidence by a wide margin.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-02 Beyond declared limits | NOT RUN | No study record declared, so no `cannot_claim` to check against. Note: this is exactly the kind of claim a declared sample limit would have caught. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-06 Formulaic Transfer Hedge | No | No transfer across populations is claimed. |

### Could someone retrace it?

**Provenance**

| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| "3 good users completed checkout easily" | INT-01 only ("Completed checkout in under a minute, no hesitation") | Inferred (and inflated) | No — the "3" has no source; the "good" is a judgment not in the source. |
| "the 2 bad participants" | INT-02 only ("Got stuck on the shipping step and asked me for help twice") | Inferred (and inflated) | No — the "2" has no source; "bad" is a judgment not in the source. |
| "weren't paying attention" | not cited | Inferred | No — no evidence about attention appears in either excerpt. |

**Checked against:** Nothing declared. No questions, no limits, no beliefs to audit against.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-06 Drift | NOT RUN | No declared questions to check the claim against. | n/a |

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-02 Context Blindness | No | Can't be assessed — no prior research visible. |
| P-07 Trust Without Process | Yes | The judgment "good users" / "bad participants" is asserted, not derived. No reasoning is offered for why INT-01 is "good" or INT-02 is "bad" beyond the outcome. |

### Is it theirs or ours?

**Beliefs and evidence:** The "wasn't paying attention" explanation is not drawn from what participants said or did — it reads as the team's framing of why a participant struggled. Without a declared belief register it's impossible to say whose assumption this is, but it is clearly not from the evidence.

| Check | Result | What triggered it | Conflicts with |
|---|---|---|---|
| CK-01 Borrowed conviction | NOT RUN (part a) / **FIRES** (part b, weakly) | Part (a) can't run with no register. Part (b): "weren't paying attention" is presented as an explanation with no participant evidence behind it — it reads as attributed opinion (someone on the team's view of what happened), but no attribution is named, so this fires weakly on structure rather than clearly on text. | n/a (no declared belief) |

### Tacit-knowledge prompt
A researcher who ran INT-02 could answer: when the participant asked for help at the shipping step, what specifically were they trying to do? Did the step have a form field, an address lookup, a shipping option selector — and what did they reach for or ask about? That distinction tells you whether this is a design problem (where the fix is in the product) or something else.

### Decision boundary
- **Supports:** One participant completed checkout quickly (INT-01). One participant struggled at the shipping step and sought help twice (INT-02).
- **Doesn't support:** Any claim about 5 participants, any judgment of participants as "good" or "bad", any causal claim about attention, any generalisation about checkout.
- **What would close the gap:** The actual full set of session data — how many participants, what each one did at the shipping step, and whatever the researcher noted about why INT-02 got stuck. Without that, you have two excerpts, not a finding.

**Safe to act on:** Not yet — the claim invents participants (5 described, 2 cited), judges them as people, and asserts a cause (inattention) with no supporting evidence. The one real signal here — INT-02 struggling at the shipping step — points at a design question that this framing actively hides.

---

## Summary

| Finding | Evidence strength | Matches its evidence | Checks that fired | Checks that didn't run | Safe to act on |
|---|---|---|---|---|---|
| "3 good users…2 bad participants…weren't paying attention" | WEAK | No | CK-03, CK-05, CK-01 (part b, weak) | CK-02, CK-04, CK-06, CK-01 (part a) | Not yet |

The single most important thing here: the one piece of real evidence in this set (INT-02 getting stuck at the shipping step) is being explained away as a participant problem. That's the opposite of what the evidence suggests. If you reframe INT-02 as a design signal rather than a bad participant, you have a hypothesis worth investigating — but you need more sessions, and ideally a declared study record so a QA pass next time can do more than report NOT RUN on half its checks.
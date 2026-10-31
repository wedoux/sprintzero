## Finding: "Moving the save button to the top right is the right call."

**Evidence strength: WEAK**
This is a design preference presented as a research-backed decision. There is no study, no user evidence, and no agreed internal belief behind it — only one low-confidence hunch that other team members actively dispute.

### Provenance
| Claim | Source | Observed or inferred | Traceable? |
|---|---|---|---|
| Top-right is the right placement for the save button | B-01 (own_experience, "matches a couple of other apps we use") | Inferred | Partially — traces to a belief, but the belief itself is self-marked low confidence, not agreed by all, and not grounded in user evidence |
| This is "the right call" (i.e. a decision-ready conclusion) | Not cited | Inferred | No — no evidence, study, or reasoning chain is offered to bridge from the belief to the decision |

No user research, usability test, analytics data, or external benchmark is cited. The only input is one team member's impression of "a couple of other apps," explicitly contradicted by engineering's view that top-left matches internal icon conventions.

### Falsification pass
- **Strongest counter-hypothesis:** Top-left is correct, because internal icon conventions (engineering's stated position) create consistency within *this* product, which usually matters more to existing users than consistency with other apps. A second counter-hypothesis: placement doesn't materially affect save behaviour at all, and the whole debate is a wash — in which case "the right call" is overclaiming regardless of direction.
- **What would overturn this finding:** Any one of — a usability test showing users hunt for the save button in the top-left; analytics from a comparable product showing save-click latency or miss rate differs by placement; a convention audit of the apps actually comparable to this product (not "a couple of other apps"); or evidence that existing users of this product already expect top-left because of the icon conventions engineering cited.
- **Where the evidence underdetermines the claim:** Everywhere. There is no user-side evidence of any kind. The claim is underdetermined not in a subtle way but completely — the question has not been studied.

### Pitfalls checked

| Pitfall | Triggered? | What triggered it |
|---|---|---|
| P-01 Headline Generality | Yes | "The right call" has no observable behaviour, no trigger, and no consequence attached. It's a verdict label, not a finding about user behaviour. Fixing it would mean stating what users are observed to do, when, and at what cost — none of which is available here. |
| P-02 Context Blindness | Yes | Engineering's dissent about internal icon conventions is prior context that directly bears on the decision, and the claim proceeds as if it doesn't exist. The dissent is logged in the belief register and then ignored in the conclusion. |
| P-03 Transcript Literalism | No | No transcripts or session data involved. |
| P-04 Volume Mistaken for Strength | Yes | "A couple of other apps" is being used as a convention argument. Two same-source observations (apps the belief-holder happens to use) are not a convention — they're one data point about one person's app choices. Would this verdict survive if one of the two apps vanished? Yes, which means it was never really resting on two things. |
| P-05 Counter-Evidence Filed, Not Faced | Yes | The dissent_note names a specific counter-position (engineering: top-left matches internal icon conventions). The claim delivers its verdict as though that note weren't there. No sentence in the claim explains why engineering's position is wrong or why internal convention should lose to external convention. |
| P-06 Formulaic Transfer Hedge | No | No transfer across populations is being claimed. |
| P-07 Trust Without Process | Yes | "The right call" is a conclusion stated without reasoning. There is no derivation from evidence to verdict — the verdict is simply asserted. A reader cannot reconstruct how the claim-maker got from "a couple of apps do this" (disputed, low confidence) to "this is the right call." |
| P-08 Narrowing Sold as Resolving | Yes | Even granting the belief at face value, "matches a couple of other apps" would at most *suggest investigating* top-right placement. It's been promoted directly to "this is the right call" — the strongest possible decision verb — without any intermediate validation. |

Six of eight pitfalls fire. That's unusually high and reflects that this is less a research finding than a preference being dressed as one.

### What would change this verdict
A single lightweight usability test — even five users asked to save something in a prototype of each layout — would produce more signal than the entire current evidence base. Short of that, a documented audit of save-button placement in the three or four products this product's users most frequently come from (not the belief-holder's personal app rotation) would at least convert "a couple of apps" into a defensible convention claim. Without one of these, the decision should not be framed as research-backed; it should be framed honestly as a judgement call where the team picked a side of an internal disagreement.

### Tacit-knowledge prompt
Not applicable — no researcher ran any sessions, because no sessions exist. The relevant missing input isn't tacit knowledge from a study; it's a study.

---

**Summary for the reviewer:** This claim should not be acted on as written. The underlying question (where to put the save button) is answerable cheaply, and the current basis for the decision — one low-confidence personal impression, actively disputed internally, with no user data — is weaker than the dissent it's overriding. Recommend either running a minimal test, or re-framing the decision as "we picked a direction to unblock ourselves, and we'll validate post-launch," which is defensible where "this is the right call" is not.
---
id: CK-02-clear-02
checks_expected_to_fire: []
checks_expected_clear: [CK-02]
checks_expected_not_run: []
synthetic: true
notes: Claim about a population outside the sample is explicitly labelled a hypothesis, not asserted.
---

## Belief register
(none declared)

## Study record
study_name: Bike-Share Unlock Flow Study
decision_informed: Whether to redesign the QR-unlock screen.
questions: (none declared)
evidence_sources: 6 moderated sessions, iOS TestFlight users only (INT-01 to INT-06).
limits:
- component: sample · what_was_cut: Android users were not recruited · cannot_claim: what Android users experience with the unlock flow

## Evidence
- INT-02: "The QR scanner took three tries to line up on my phone."

## Claims under review
"Hypothesis for a future study (not yet tested): Android users may hit the same scanning friction, since the camera API behaves differently across devices."

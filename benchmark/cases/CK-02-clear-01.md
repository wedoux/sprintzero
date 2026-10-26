---
id: CK-02-clear-01
checks_expected_to_fire: []
checks_expected_clear: [CK-02, CK-05]
checks_expected_not_run: []
expected_strength: [UNCERTAIN, STRONG]
claim_honest: yes
synthetic: true
notes: Claim stays within the declared sample limit, and scope matches exactly what's cited (2 of 6, stated as 2 of 6) - no inflation beyond the sample limit this case targets.
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
- INT-05: "I gave up and called support after the scan failed twice."

## Claims under review
"2 of the 6 iOS users we tested found the QR scan step frustrating."

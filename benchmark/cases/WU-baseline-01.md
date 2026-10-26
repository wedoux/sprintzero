---
id: WU-baseline-01
checks_expected_to_fire: [CK-01, CK-05]
checks_expected_clear: [CK-03, CK-04]
checks_expected_not_run: [CK-02, CK-06]
synthetic: false
notes: Real Weather Underground corpus. Reproduces SprintZero's own canonical misreading — forecast model accuracy is not the problem; R03 defends accuracy while R05/R09/R13 point to stale cached data instead.
---

## Belief register
| id | belief | about | confidence | rationale | source_type | source_ref | agreed_by_all | dissent_note |
|---|---|---|---|---|---|---|---|---|
| B-01 | Our forecast model is behind competitors in accuracy. | product | high | An exec compared a handful of competitor forecasts and ours looked worse that week. | authority | | no | Engineering disagrees — our model's benchmarked accuracy is within spec against the same competitors. |

## Study record
study_name: Weather Underground Trust Complaints Review
decision_informed: Whether to invest engineering time in forecast model accuracy.
questions: (none declared)
evidence_sources: 13 iOS App Store reviews, 2020–2026 (R01–R13). See corpora/corpus/weather_underground.md for the full annotated corpus and its data-limitations preamble.
limits: (none declared)

## Evidence
- R03: "You still get accurate, hyper-local forecasts that are hard to beat." (1-star review; the complaint was about UI/UX changes, not data quality.)
- R05: "For over 6 months this app only ever states that every day is 76 degrees... I've deleted and reinstalled the app more than 10 times." (Stale cached data after a GPS/location change, not a forecast model failure.)
- R09: "I keep hoping the developers will improve the automatic refresh when I change a location... I have to force a refresh." (Same stale-data-on-location-change failure as R05.)
- R13: "About once a week the app is frozen with old info." (Stale data on app freeze — a third occurrence of the same failure mode.)

## Claims under review
"Forecast model accuracy is the problem behind the trust complaints. Recommend investing engineering time in improving the forecast model."

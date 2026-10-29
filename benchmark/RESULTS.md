
## 2026-10-26 — target=skill version=../ux-research-qa model=claude-opus-4-7
- Cases run: 28
- Cases with violations: 28
- P-codes detected across all cases (v1.0 has no CK support; partial credit only): P-01, P-03

- **CK-01-clear-01**: FAIL
  - CK-01: expected CLEAR, got not detected
- **CK-01-clear-02**: FAIL
  - CK-01: expected CLEAR, got not detected
- **CK-01-fire-01**: FAIL
  - CK-01: expected FIRES, got not detected
- **CK-01-fire-02**: FAIL
  - CK-01: expected FIRES, got not detected
- **CK-02-clear-01**: FAIL
  - CK-02: expected CLEAR, got not detected
- **CK-02-clear-02**: FAIL
  - CK-02: expected CLEAR, got not detected
- **CK-02-fire-01**: FAIL
  - CK-02: expected FIRES, got not detected
- **CK-02-fire-02**: FAIL
  - CK-02: expected FIRES, got not detected
- **CK-03-clear-01**: FAIL
  - CK-03: expected CLEAR, got not detected
- **CK-03-clear-02**: FAIL
  - CK-03: expected CLEAR, got not detected
- **CK-03-fire-01**: FAIL
  - CK-03: expected FIRES, got not detected
- **CK-03-fire-02**: FAIL
  - CK-03: expected FIRES, got not detected
- **CK-04-clear-01**: FAIL
  - CK-04: expected CLEAR, got not detected
- **CK-04-clear-02**: FAIL
  - CK-04: expected CLEAR, got not detected
- **CK-04-fire-01**: FAIL
  - CK-04: expected FIRES, got not detected
- **CK-04-fire-02**: FAIL
  - CK-04: expected FIRES, got not detected
- **CK-05-clear-01**: FAIL
  - CK-05: expected CLEAR, got not detected
- **CK-05-clear-02**: FAIL
  - CK-05: expected CLEAR, got not detected
- **CK-05-fire-01**: FAIL
  - CK-05: expected FIRES, got not detected
- **CK-05-fire-02**: FAIL
  - CK-05: expected FIRES, got not detected
- **CK-06-clear-01**: FAIL
  - CK-06: expected CLEAR, got not detected
- **CK-06-clear-02**: FAIL
  - CK-06: expected CLEAR, got not detected
- **CK-06-fire-01**: FAIL
  - CK-06: expected FIRES, got not detected
- **CK-06-fire-02**: FAIL
  - CK-06: expected FIRES, got not detected
- **NR-01**: FAIL
  - CK-01: expected NOT RUN, got not detected
  - CK-04: expected NOT RUN, got not detected
- **NR-02**: FAIL
  - CK-02: expected NOT RUN, got not detected
- **NR-03**: FAIL
  - CK-06: expected NOT RUN, got not detected
- **WU-baseline-01**: FAIL
  - CK-01: expected FIRES, got not detected
  - CK-05: expected FIRES, got not detected
  - CK-03: expected CLEAR, got not detected
  - CK-04: expected CLEAR, got not detected
  - CK-02: expected NOT RUN, got not detected
  - CK-06: expected NOT RUN, got not detected

## 2026-10-26 — target=skill version=e47326f model=claude-opus-4-7
- Cases run: 28
- CK-ID score: 0/28 (regex-matched FIRES/CLEAR/NOT RUN against front matter)
- Strength score: 16/25 (fire cases not rated STRONG, clear cases not rated WEAK; 3 NR case(s) excluded, not applicable)
- P-codes detected across all cases (v1.0 has no CK support; partial credit only): P-04
- Raw readouts: runs/2026-10-26-skill-e47326f/

- **CK-01-clear-01**: CK=FAIL · STRENGTH=FAIL (WEAK)
  - CK-01: expected CLEAR, got not detected
- **CK-01-clear-02**: CK=FAIL · STRENGTH=FAIL (WEAK)
  - CK-01: expected CLEAR, got not detected
- **CK-01-fire-01**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-01: expected FIRES, got not detected
- **CK-01-fire-02**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-01: expected FIRES, got not detected
- **CK-02-clear-01**: CK=FAIL · STRENGTH=PASS (UNCERTAIN)
  - CK-02: expected CLEAR, got not detected
- **CK-02-clear-02**: CK=FAIL · STRENGTH=FAIL (not detected)
  - CK-02: expected CLEAR, got not detected
- **CK-02-fire-01**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-02: expected FIRES, got not detected
- **CK-02-fire-02**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-02: expected FIRES, got not detected
- **CK-03-clear-01**: CK=FAIL · STRENGTH=PASS (UNCERTAIN)
  - CK-03: expected CLEAR, got not detected
- **CK-03-clear-02**: CK=FAIL · STRENGTH=FAIL (WEAK)
  - CK-03: expected CLEAR, got not detected
- **CK-03-fire-01**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-03: expected FIRES, got not detected
- **CK-03-fire-02**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-03: expected FIRES, got not detected
- **CK-04-clear-01**: CK=FAIL · STRENGTH=FAIL (WEAK)
  - CK-04: expected CLEAR, got not detected
- **CK-04-clear-02**: CK=FAIL · STRENGTH=FAIL (WEAK)
  - CK-04: expected CLEAR, got not detected
- **CK-04-fire-01**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-04: expected FIRES, got not detected
- **CK-04-fire-02**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-04: expected FIRES, got not detected
- **CK-05-clear-01**: CK=FAIL · STRENGTH=FAIL (WEAK)
  - CK-05: expected CLEAR, got not detected
- **CK-05-clear-02**: CK=FAIL · STRENGTH=PASS (STRONG)
  - CK-05: expected CLEAR, got not detected
- **CK-05-fire-01**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-05: expected FIRES, got not detected
- **CK-05-fire-02**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-05: expected FIRES, got not detected
- **CK-06-clear-01**: CK=FAIL · STRENGTH=FAIL (WEAK)
  - CK-06: expected CLEAR, got not detected
- **CK-06-clear-02**: CK=FAIL · STRENGTH=FAIL (WEAK)
  - CK-06: expected CLEAR, got not detected
- **CK-06-fire-01**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-06: expected FIRES, got not detected
- **CK-06-fire-02**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-06: expected FIRES, got not detected
- **NR-01**: CK=FAIL · STRENGTH=N/A (WEAK)
  - CK-01: expected NOT RUN, got not detected
  - CK-04: expected NOT RUN, got not detected
- **NR-02**: CK=FAIL · STRENGTH=N/A (WEAK)
  - CK-02: expected NOT RUN, got not detected
- **NR-03**: CK=FAIL · STRENGTH=N/A (WEAK)
  - CK-06: expected NOT RUN, got not detected
- **WU-baseline-01**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-01: expected FIRES, got not detected
  - CK-05: expected FIRES, got not detected
  - CK-03: expected CLEAR, got not detected
  - CK-04: expected CLEAR, got not detected
  - CK-02: expected NOT RUN, got not detected
  - CK-06: expected NOT RUN, got not detected

**Note on the gold labels below (R0.2):** expected_strength and claim_honest were
drafted after reading v1's actual readouts, then reviewed by Nikos - not written
blind before the run. They may be anchored toward what v1 happened to say. From
R1 onward, gold labels are written before a case is run.

## 2026-10-26 — target=skill version=e47326f model=claude-opus-4-7 (R0.2 - gold labels, not filename-inferred; see note above)
- Cases run: 28
- CK-ID score: 0/28 (regex-matched FIRES/CLEAR/NOT RUN against front matter)
- Strength score: 25/25 (rated within each case's own expected_strength gold label; 3 NR case(s) excluded, not applicable)
- P-codes detected across all cases (v1.0 has no CK support; partial credit only): none
- Raw readouts: runs/2026-10-26-skill-e47326f/
- 7 cases rewritten and live-rescored this round (CK-02-clear-01, CK-04-clear-01,
  CK-05-clear-01, CK-06-clear-01, CK-06-clear-02, NR-02, NR-03); the other 21
  re-scored from the prior run's saved readouts under the new gold labels, no
  new API calls.

- **CK-01-clear-01**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-01: expected CLEAR, got not detected
- **CK-01-clear-02**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-01: expected CLEAR, got not detected
- **CK-01-fire-01**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-01: expected FIRES, got not detected
- **CK-01-fire-02**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-01: expected FIRES, got not detected
- **CK-02-clear-02**: CK=FAIL · STRENGTH=PASS (N/A)
  - CK-02: expected CLEAR, got not detected
- **CK-02-fire-01**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-02: expected FIRES, got not detected
- **CK-02-fire-02**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-02: expected FIRES, got not detected
- **CK-03-clear-01**: CK=FAIL · STRENGTH=PASS (UNCERTAIN)
  - CK-03: expected CLEAR, got not detected
- **CK-03-clear-02**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-03: expected CLEAR, got not detected
- **CK-03-fire-01**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-03: expected FIRES, got not detected
- **CK-03-fire-02**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-03: expected FIRES, got not detected
- **CK-04-clear-02**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-04: expected CLEAR, got not detected
- **CK-04-fire-01**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-04: expected FIRES, got not detected
- **CK-04-fire-02**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-04: expected FIRES, got not detected
- **CK-05-clear-02**: CK=FAIL · STRENGTH=PASS (STRONG)
  - CK-05: expected CLEAR, got not detected
- **CK-05-fire-01**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-05: expected FIRES, got not detected
- **CK-05-fire-02**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-05: expected FIRES, got not detected
- **CK-06-fire-01**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-06: expected FIRES, got not detected
- **CK-06-fire-02**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-06: expected FIRES, got not detected
- **NR-01**: CK=FAIL · STRENGTH=N/A (WEAK)
  - CK-01: expected NOT RUN, got not detected
  - CK-04: expected NOT RUN, got not detected
- **WU-baseline-01**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-01: expected FIRES, got not detected
  - CK-05: expected FIRES, got not detected
  - CK-03: expected CLEAR, got not detected
  - CK-04: expected CLEAR, got not detected
  - CK-02: expected NOT RUN, got not detected
  - CK-06: expected NOT RUN, got not detected
- **CK-02-clear-01**: CK=FAIL · STRENGTH=PASS (STRONG)
  - CK-02: expected CLEAR, got not detected
  - CK-05: expected CLEAR, got not detected
- **CK-04-clear-01**: CK=FAIL · STRENGTH=PASS (STRONG)
  - CK-04: expected CLEAR, got not detected
  - CK-05: expected CLEAR, got not detected
- **CK-05-clear-01**: CK=FAIL · STRENGTH=PASS (STRONG)
  - CK-05: expected CLEAR, got not detected
- **CK-06-clear-01**: CK=FAIL · STRENGTH=PASS (STRONG)
  - CK-06: expected CLEAR, got not detected
  - CK-05: expected CLEAR, got not detected
- **CK-06-clear-02**: CK=FAIL · STRENGTH=PASS (WEAK)
  - CK-06: expected CLEAR, got not detected
- **NR-02**: CK=FAIL · STRENGTH=N/A (STRONG)
  - CK-02: expected NOT RUN, got not detected
- **NR-03**: CK=FAIL · STRENGTH=N/A (STRONG)
  - CK-06: expected NOT RUN, got not detected

## 2026-10-26 — target=skill version=e47326f model=claude-opus-4-7 (R1 baseline for v1: new fail-closed scorer + claim score; CK-01-clear-02 and CK-04-fire-01 re-run live on their edited inputs, the other 26 re-scored from runs/2026-10-26-skill-e47326f/)
- Cases run: 28
- CK-ID score: 0/28 (regex-matched FIRES/CLEAR/NOT RUN against front matter)
- Strength score: 25/25 (rated within each case's own expected_strength gold label; 3 NR case(s) excluded, not applicable)
- Claim score: 0/28 ('Claim matches its evidence' against each case's claim_honest gold label)
- P-codes detected across all cases (v1.0 has no CK support; partial credit only): none
- Raw readouts: runs/2026-10-26-skill-e47326f-2/

- **CK-01-clear-01**: CK=FAIL · STRENGTH=PASS (WEAK) · CLAIM=FAIL (not detected)
  - CK-01: expected CLEAR, got not detected
- **CK-01-fire-01**: CK=FAIL · STRENGTH=PASS (WEAK) · CLAIM=FAIL (not detected)
  - CK-01: expected FIRES, got not detected
- **CK-01-fire-02**: CK=FAIL · STRENGTH=PASS (WEAK) · CLAIM=FAIL (not detected)
  - CK-01: expected FIRES, got not detected
- **CK-02-clear-01**: CK=FAIL · STRENGTH=PASS (STRONG) · CLAIM=FAIL (not detected)
  - CK-02: expected CLEAR, got not detected
  - CK-05: expected CLEAR, got not detected
- **CK-02-clear-02**: CK=FAIL · STRENGTH=PASS (N/A) · CLAIM=FAIL (not detected)
  - CK-02: expected CLEAR, got not detected
- **CK-02-fire-01**: CK=FAIL · STRENGTH=PASS (WEAK) · CLAIM=FAIL (not detected)
  - CK-02: expected FIRES, got not detected
- **CK-02-fire-02**: CK=FAIL · STRENGTH=PASS (WEAK) · CLAIM=FAIL (not detected)
  - CK-02: expected FIRES, got not detected
- **CK-03-clear-01**: CK=FAIL · STRENGTH=PASS (UNCERTAIN) · CLAIM=FAIL (not detected)
  - CK-03: expected CLEAR, got not detected
- **CK-03-clear-02**: CK=FAIL · STRENGTH=PASS (WEAK) · CLAIM=FAIL (not detected)
  - CK-03: expected CLEAR, got not detected
- **CK-03-fire-01**: CK=FAIL · STRENGTH=PASS (WEAK) · CLAIM=FAIL (not detected)
  - CK-03: expected FIRES, got not detected
- **CK-03-fire-02**: CK=FAIL · STRENGTH=PASS (WEAK) · CLAIM=FAIL (not detected)
  - CK-03: expected FIRES, got not detected
- **CK-04-clear-01**: CK=FAIL · STRENGTH=PASS (STRONG) · CLAIM=FAIL (not detected)
  - CK-04: expected CLEAR, got not detected
  - CK-05: expected CLEAR, got not detected
- **CK-04-clear-02**: CK=FAIL · STRENGTH=PASS (WEAK) · CLAIM=FAIL (not detected)
  - CK-04: expected CLEAR, got not detected
- **CK-04-fire-02**: CK=FAIL · STRENGTH=PASS (WEAK) · CLAIM=FAIL (not detected)
  - CK-04: expected FIRES, got not detected
- **CK-05-clear-01**: CK=FAIL · STRENGTH=PASS (STRONG) · CLAIM=FAIL (not detected)
  - CK-05: expected CLEAR, got not detected
- **CK-05-clear-02**: CK=FAIL · STRENGTH=PASS (STRONG) · CLAIM=FAIL (not detected)
  - CK-05: expected CLEAR, got not detected
- **CK-05-fire-01**: CK=FAIL · STRENGTH=PASS (WEAK) · CLAIM=FAIL (not detected)
  - CK-05: expected FIRES, got not detected
- **CK-05-fire-02**: CK=FAIL · STRENGTH=PASS (WEAK) · CLAIM=FAIL (not detected)
  - CK-05: expected FIRES, got not detected
- **CK-06-clear-01**: CK=FAIL · STRENGTH=PASS (STRONG) · CLAIM=FAIL (not detected)
  - CK-06: expected CLEAR, got not detected
  - CK-05: expected CLEAR, got not detected
- **CK-06-clear-02**: CK=FAIL · STRENGTH=PASS (WEAK) · CLAIM=FAIL (not detected)
  - CK-06: expected CLEAR, got not detected
- **CK-06-fire-01**: CK=FAIL · STRENGTH=PASS (WEAK) · CLAIM=FAIL (not detected)
  - CK-06: expected FIRES, got not detected
- **CK-06-fire-02**: CK=FAIL · STRENGTH=PASS (WEAK) · CLAIM=FAIL (not detected)
  - CK-06: expected FIRES, got not detected
- **NR-01**: CK=FAIL · STRENGTH=N/A (WEAK) · CLAIM=FAIL (not detected)
  - CK-01: expected NOT RUN, got not detected
  - CK-04: expected NOT RUN, got not detected
- **NR-02**: CK=FAIL · STRENGTH=N/A (STRONG) · CLAIM=FAIL (not detected)
  - CK-02: expected NOT RUN, got not detected
- **NR-03**: CK=FAIL · STRENGTH=N/A (STRONG) · CLAIM=FAIL (not detected)
  - CK-06: expected NOT RUN, got not detected
- **WU-baseline-01**: CK=FAIL · STRENGTH=PASS (WEAK) · CLAIM=FAIL (not detected)
  - CK-01: expected FIRES, got not detected
  - CK-05: expected FIRES, got not detected
  - CK-03: expected CLEAR, got not detected
  - CK-04: expected CLEAR, got not detected
  - CK-02: expected NOT RUN, got not detected
  - CK-06: expected NOT RUN, got not detected
- **CK-01-clear-02**: CK=FAIL · STRENGTH=PASS (WEAK) · CLAIM=FAIL (not detected)
  - CK-01: expected CLEAR, got not detected
- **CK-04-fire-01**: CK=FAIL · STRENGTH=PASS (WEAK) · CLAIM=FAIL (not detected)
  - CK-04: expected FIRES, got not detected

## 2026-10-28 — target=skill version=4ba2545-dry-run model=stub
- Cases run (seeded cases): 28
- CK-ID score (seeded cases): 28/28 (regex-matched FIRES/CLEAR/NOT RUN against front matter)
- Strength score (seeded cases): 25/25 (rated within each case's own expected_strength gold label; 3 NR case(s) excluded, not applicable)
- Claim score (seeded cases): 28/28 ('Claim matches its evidence' against each case's claim_honest gold label)
- Cases run (added since R0): 2 — CK-01-clear-03, CK-01-fire-03
- CK-ID score (added since R0): 2/2 (regex-matched FIRES/CLEAR/NOT RUN against front matter)
- Strength score (added since R0): 2/2 (rated within each case's own expected_strength gold label; 0 NR case(s) excluded, not applicable)
- Claim score (added since R0): 2/2 ('Claim matches its evidence' against each case's claim_honest gold label)
- P-codes detected across all cases (v1.0 has no CK support; partial credit only): none
- Raw readouts: runs/2026-10-28-skill-4ba2545-dry-run/

- **CK-01-clear-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-01-clear-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-01-clear-03**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (Yes)
- **CK-01-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-01-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-01-fire-03**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-02-clear-01**: CK=PASS · STRENGTH=PASS (UNCERTAIN) · CLAIM=PASS (Yes)
- **CK-02-clear-02**: CK=PASS · STRENGTH=PASS (N/A) · CLAIM=PASS (Yes)
- **CK-02-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-02-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-03-clear-01**: CK=PASS · STRENGTH=PASS (UNCERTAIN) · CLAIM=PASS (Yes)
- **CK-03-clear-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (Yes)
- **CK-03-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-03-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-04-clear-01**: CK=PASS · STRENGTH=PASS (STRONG) · CLAIM=PASS (Yes)
- **CK-04-clear-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-04-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-04-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-05-clear-01**: CK=PASS · STRENGTH=PASS (UNCERTAIN) · CLAIM=PASS (Yes)
- **CK-05-clear-02**: CK=PASS · STRENGTH=PASS (STRONG) · CLAIM=PASS (Yes)
- **CK-05-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-05-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-06-clear-01**: CK=PASS · STRENGTH=PASS (UNCERTAIN) · CLAIM=PASS (Yes)
- **CK-06-clear-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (Yes)
- **CK-06-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-06-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **NR-01**: CK=PASS · STRENGTH=N/A (WEAK) · CLAIM=PASS (No)
- **NR-02**: CK=PASS · STRENGTH=N/A (WEAK) · CLAIM=PASS (Yes)
- **NR-03**: CK=PASS · STRENGTH=N/A (WEAK) · CLAIM=PASS (Yes)
- **WU-baseline-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)

## 2026-10-28 — target=skill version=4ba2545 model=claude-opus-4-7 (intermediate R1 run, scored against the gold labels as they stood before the 2026-10-28 relabel; superseded by the next entry)
- Cases run (seeded cases): 28
- CK-ID score (seeded cases): 25/28 (regex-matched FIRES/CLEAR/NOT RUN against front matter)
- Strength score (seeded cases): 23/25 (rated within each case's own expected_strength gold label; 3 NR case(s) excluded, not applicable)
- Claim score (seeded cases): 28/28 ('Claim matches its evidence' against each case's claim_honest gold label)
- Cases run (added since R0): 2 — CK-01-clear-03, CK-01-fire-03
- CK-ID score (added since R0): 2/2 (regex-matched FIRES/CLEAR/NOT RUN against front matter)
- Strength score (added since R0): 2/2 (rated within each case's own expected_strength gold label; 0 NR case(s) excluded, not applicable)
- Claim score (added since R0): 2/2 ('Claim matches its evidence' against each case's claim_honest gold label)
- P-codes detected across all cases (v1.0 has no CK support; partial credit only): P-04
- Raw readouts: runs/2026-10-28-skill-4ba2545/

- **CK-01-clear-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-01-clear-02**: CK=FAIL · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
  - CK-01: expected CLEAR, got FIRES
- **CK-01-clear-03**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (Yes)
- **CK-01-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-01-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-01-fire-03**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-02-clear-01**: CK=PASS · STRENGTH=FAIL (WEAK) · CLAIM=PASS (Yes)
- **CK-02-clear-02**: CK=PASS · STRENGTH=FAIL (WEAK) · CLAIM=PASS (Yes)
- **CK-02-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-02-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-03-clear-01**: CK=PASS · STRENGTH=PASS (UNCERTAIN) · CLAIM=PASS (Yes)
- **CK-03-clear-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (Yes)
- **CK-03-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-03-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-04-clear-01**: CK=PASS · STRENGTH=PASS (STRONG) · CLAIM=PASS (Yes)
- **CK-04-clear-02**: CK=FAIL · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
  - CK-04: expected CLEAR, got FIRES
- **CK-04-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-04-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-05-clear-01**: CK=PASS · STRENGTH=PASS (STRONG) · CLAIM=PASS (Yes)
- **CK-05-clear-02**: CK=PASS · STRENGTH=PASS (STRONG) · CLAIM=PASS (Yes)
- **CK-05-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-05-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-06-clear-01**: CK=PASS · STRENGTH=PASS (STRONG) · CLAIM=PASS (Yes)
- **CK-06-clear-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (Yes)
- **CK-06-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-06-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **NR-01**: CK=PASS · STRENGTH=N/A (WEAK) · CLAIM=PASS (No)
- **NR-02**: CK=PASS · STRENGTH=N/A (WEAK) · CLAIM=PASS (Yes)
- **NR-03**: CK=PASS · STRENGTH=N/A (WEAK) · CLAIM=PASS (Yes)
- **WU-baseline-01**: CK=FAIL · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
  - CK-04: expected CLEAR, got FIRES

## 2026-10-28 — target=skill version=c12c18d model=claude-opus-4-7 (intermediate R1 run, scored against the gold labels as they stood before the 2026-10-29 relabel; superseded)
- Cases run (seeded cases): 28
- CK-ID score (seeded cases): 25/28 (regex-matched FIRES/CLEAR/NOT RUN against front matter)
- Strength score (seeded cases): 24/25 (rated within each case's own expected_strength gold label; 3 NR case(s) excluded, not applicable)
- Claim score (seeded cases): 28/28 ('Claim matches its evidence' against each case's claim_honest gold label)
- Cases run (added since R0): 2 — CK-01-clear-03, CK-01-fire-03
- CK-ID score (added since R0): 2/2 (regex-matched FIRES/CLEAR/NOT RUN against front matter)
- Strength score (added since R0): 2/2 (rated within each case's own expected_strength gold label; 0 NR case(s) excluded, not applicable)
- Claim score (added since R0): 2/2 ('Claim matches its evidence' against each case's claim_honest gold label)
- P-codes detected across all cases (v1.0 has no CK support; partial credit only): none
- Raw readouts: runs/2026-10-28-skill-c12c18d/

- **CK-01-clear-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-01-clear-02**: CK=FAIL · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
  - CK-01: expected CLEAR, got FIRES
- **CK-01-clear-03**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (Yes)
- **CK-01-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-01-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-01-fire-03**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-02-clear-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (Yes)
- **CK-02-clear-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (Yes)
- **CK-02-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-02-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-03-clear-01**: CK=PASS · STRENGTH=PASS (STRONG) · CLAIM=PASS (Yes)
- **CK-03-clear-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (Yes)
- **CK-03-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-03-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-04-clear-01**: CK=PASS · STRENGTH=PASS (STRONG) · CLAIM=PASS (Yes)
- **CK-04-clear-02**: CK=FAIL · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
  - CK-04: expected CLEAR, got FIRES
- **CK-04-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-04-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-05-clear-01**: CK=PASS · STRENGTH=FAIL (WEAK) · CLAIM=PASS (Yes)
- **CK-05-clear-02**: CK=PASS · STRENGTH=PASS (STRONG) · CLAIM=PASS (Yes)
- **CK-05-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-05-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-06-clear-01**: CK=PASS · STRENGTH=PASS (STRONG) · CLAIM=PASS (Yes)
- **CK-06-clear-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (Yes)
- **CK-06-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-06-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **NR-01**: CK=FAIL · STRENGTH=N/A (WEAK) · CLAIM=PASS (No)
  - CK-04: expected NOT RUN, got FIRES
- **NR-02**: CK=PASS · STRENGTH=N/A (WEAK) · CLAIM=PASS (Yes)
- **NR-03**: CK=PASS · STRENGTH=N/A (WEAK) · CLAIM=PASS (Yes)
- **WU-baseline-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)

## 2026-10-29 — target=skill version=053030a (STOPPED EARLY) model=claude-opus-4-7 (WU-baseline-01 hit an API usage limit; the 29 completed readouts are reused by the next entry)
- Cases run (seeded cases): 28
- CK-ID score (seeded cases): 26/28 (regex-matched FIRES/CLEAR/NOT RUN against front matter)
- Strength score (seeded cases): 24/25 (rated within each case's own expected_strength gold label; 3 NR case(s) excluded, not applicable)
- Claim score (seeded cases): 27/28 ('Claim matches its evidence' against each case's claim_honest gold label)
- Cases run (added since R0): 2 — CK-01-clear-03, CK-01-fire-03
- CK-ID score (added since R0): 2/2 (regex-matched FIRES/CLEAR/NOT RUN against front matter)
- Strength score (added since R0): 2/2 (rated within each case's own expected_strength gold label; 0 NR case(s) excluded, not applicable)
- Claim score (added since R0): 2/2 ('Claim matches its evidence' against each case's claim_honest gold label)
- P-codes detected across all cases (v1.0 has no CK support; partial credit only): P-01, P-04, P-07
- Raw readouts: runs/2026-10-29-skill-053030a/

- **CK-01-clear-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-01-clear-02**: CK=FAIL · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
  - CK-01: expected CLEAR, got FIRES
- **CK-01-clear-03**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (Yes)
- **CK-01-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-01-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-01-fire-03**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-02-clear-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (Yes)
- **CK-02-clear-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (Yes)
- **CK-02-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-02-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-03-clear-01**: CK=PASS · STRENGTH=PASS (STRONG) · CLAIM=PASS (Yes)
- **CK-03-clear-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (Yes)
- **CK-03-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-03-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-04-clear-01**: CK=PASS · STRENGTH=PASS (STRONG) · CLAIM=PASS (Yes)
- **CK-04-clear-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-04-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-04-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-05-clear-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (Yes)
- **CK-05-clear-02**: CK=PASS · STRENGTH=PASS (STRONG) · CLAIM=PASS (Yes)
- **CK-05-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-05-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-06-clear-01**: CK=PASS · STRENGTH=PASS (STRONG) · CLAIM=PASS (Yes)
- **CK-06-clear-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (Yes)
- **CK-06-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-06-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **NR-01**: CK=PASS · STRENGTH=N/A (WEAK) · CLAIM=PASS (No)
- **NR-02**: CK=PASS · STRENGTH=N/A (WEAK) · CLAIM=PASS (Yes)
- **NR-03**: CK=PASS · STRENGTH=N/A (WEAK) · CLAIM=PASS (Yes)
- **WU-baseline-01**: CK=FAIL · STRENGTH=FAIL (not detected) · CLAIM=FAIL (not detected)
  - ERROR: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'You have reached your specified API usage limits. You will regain access on 2026-11-01 at 00:00 UTC.'}, 'request_id': 'req_011CgWKUxM5gDxP2XiuTTGFM'}

**Notes on the R1 result (below).**
- Gold labels. The 28 seeded cases' `expected_strength` and `claim_honest` labels were
  written after seeing v1 output, so they are not independent of the skill. The two cases
  added in R1 (CK-01-clear-03, CK-01-fire-03) were labelled before any run; new cases
  should follow that order.
- Relabels. On 2026-10-28 (CK-02-clear-01, CK-02-clear-02) and 2026-10-29 (CK-03-clear-01,
  CK-04-clear-01, CK-05-clear-01, CK-05-clear-02, CK-06-clear-01), Nikos Antonogiannis
  allowed WEAK on every honest-claim case, after seeing R1 output. With "Claim matches
  its evidence" now a separate line, strength describes the evidence alone, and an honest
  claim on thin evidence can read as WEAK. Consequence: the strength score now mostly
  tests that overclaiming cases are not rated STRONG; it rarely fails an honest claim.
  CK-02-clear-01 accepts all three tiers and no longer tests strength at all.
- Accepted CK misses. CK-01-clear-02 (CK-01 FIRES, expected CLEAR): partly caused by the
  belief register added to this case in R1; a miss, accepted. WU-baseline-01 (CK-04
  FIRES, expected CLEAR): R1 argues that the cited reviews don't support the product claim
  and that B-01 is not agreed by all; defensible, accepted. CK-04-clear-02 (CK-04 FIRES,
  expected CLEAR) missed on earlier R1 runs and was accepted on the same grounds; it
  passed here.
- Variance. Results vary between identical runs: CK-05-clear-01's strength, and CK-04 on
  NR-01, WU-baseline-01 and CK-04-clear-02, each changed between R1 runs. Sampling ran at
  the API default: claude-opus-4-7 rejects `temperature`, so the harness can't lower it.
  Treat a one-case difference between single runs as noise.
- This entry: WU-baseline-01 was run live; the other 29 cases were re-scored from
  runs/2026-10-29-skill-053030a/, which stopped on an API usage limit before reaching it.

## 2026-10-29 — target=skill version=053030a model=claude-opus-4-7 (R1 final; see notes above)
- Cases run (seeded cases): 28
- CK-ID score (seeded cases): 26/28 (regex-matched FIRES/CLEAR/NOT RUN against front matter)
- Strength score (seeded cases): 25/25 (rated within each case's own expected_strength gold label; 3 NR case(s) excluded, not applicable)
- Claim score (seeded cases): 28/28 ('Claim matches its evidence' against each case's claim_honest gold label)
- Cases run (added since R0): 2 — CK-01-clear-03, CK-01-fire-03
- CK-ID score (added since R0): 2/2 (regex-matched FIRES/CLEAR/NOT RUN against front matter)
- Strength score (added since R0): 2/2 (rated within each case's own expected_strength gold label; 0 NR case(s) excluded, not applicable)
- Claim score (added since R0): 2/2 ('Claim matches its evidence' against each case's claim_honest gold label)
- P-codes detected across all cases (v1.0 has no CK support; partial credit only): P-01, P-04, P-07
- Raw readouts: runs/2026-10-29-skill-053030a-2/

- **CK-01-clear-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-01-clear-02**: CK=FAIL · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
  - CK-01: expected CLEAR, got FIRES
- **CK-01-clear-03**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (Yes)
- **CK-01-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-01-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-01-fire-03**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-02-clear-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (Yes)
- **CK-02-clear-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (Yes)
- **CK-02-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-02-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-03-clear-01**: CK=PASS · STRENGTH=PASS (STRONG) · CLAIM=PASS (Yes)
- **CK-03-clear-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (Yes)
- **CK-03-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-03-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-04-clear-01**: CK=PASS · STRENGTH=PASS (STRONG) · CLAIM=PASS (Yes)
- **CK-04-clear-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-04-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-04-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-05-clear-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (Yes)
- **CK-05-clear-02**: CK=PASS · STRENGTH=PASS (STRONG) · CLAIM=PASS (Yes)
- **CK-05-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-05-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-06-clear-01**: CK=PASS · STRENGTH=PASS (STRONG) · CLAIM=PASS (Yes)
- **CK-06-clear-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (Yes)
- **CK-06-fire-01**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **CK-06-fire-02**: CK=PASS · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
- **NR-01**: CK=PASS · STRENGTH=N/A (WEAK) · CLAIM=PASS (No)
- **NR-02**: CK=PASS · STRENGTH=N/A (WEAK) · CLAIM=PASS (Yes)
- **NR-03**: CK=PASS · STRENGTH=N/A (WEAK) · CLAIM=PASS (Yes)
- **WU-baseline-01**: CK=FAIL · STRENGTH=PASS (WEAK) · CLAIM=PASS (No)
  - CK-04: expected CLEAR, got FIRES

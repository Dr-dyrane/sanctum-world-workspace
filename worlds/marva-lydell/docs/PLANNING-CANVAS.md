# World 3 Planning Canvas

Status: draft for Alexander review. This is not a Brainstorm submission yet.

## Product Thesis

A medically improving older adult with acute decompensated heart failure, CKD, atrial fibrillation, COPD or OSA overlap, frailty, and home-access barriers is being transitioned out of the hospital. The test is not whether the model knows heart failure treatment. The test is whether it can determine discharge readiness when oxygen qualification, DME delivery, exertional physiology, anticoagulation, renal recovery, and conflicting handoffs do not line up.

## Candidate Patient Frame

`<<PHYSICIAN: choose patient identity, age, sex, living situation, insurance, caregiver constraints, and world snapshot date.>>`

Demographic direction: Black older adult. Race is background chart context, not a scoring mechanism.

Suggested starting shape:

- Older adult, late 60s to late 70s.
- Race documented as Black.
- Acute decompensated HF with CKD and AFib.
- COPD or OSA overlap, but not CPAP adherence as the main trap.
- Medically improving at rest, unsafe with exertion or home logistics.
- Disposition pressure from payer or case management.
- Family or caregiver constraint that makes equipment failure clinically material.

## Task Slate Draft

The table below is the starting architecture. It is intentionally task-first. Names and clinical details are not final.

| # | Structure | Working task | Forced slot | Floor candidate | Source route | Status |
|---|---|---|---|---|---|---|
| 1 | S3 external request | Oxygen or DME denial appeal | Appeal or accept denial | Resting sat looks safe, off-text exertional test qualifies oxygen | Payer denial + scanned walk-test sheet + PT note breadcrumb | candidate |
| 2 | S1 completion | Discharge summary or transition note | Finalize home oxygen and equipment status | Draft says no oxygen need or DME delivered, chart contradicts | Started summary + vendor note + nursing or RT note | candidate |
| 3 | S4 determination | Utilization review continued-stay note | Inpatient vs discharge-ready verdict | Clinical markers improved but equipment or exertional oxygen barrier unresolved | UR worksheet + RT/PT data | candidate |
| 4 | S2 forced inventory | Discharge med or anticoagulation reconciliation | Per-med disposition | External SNF/pharmacy list embeds wrong anticoagulation or duplicate therapy | External med list + MAR + renal trend | candidate, needs freshness check |
| 5 | S7 investigation | Safety event RCA after bounceback | Proximate/root/contributing separation | Blames patient nonadherence, misses failed oxygen/DME handoff | ED return note + vendor log + discharge paperwork | candidate |
| 6 | S6 synthesis with embedded table | Cardiology-nephrology-pulmonary handoff | Required issue-owner table | Quiet unresolved owner for oxygen, diuresis, renal lab follow-up | Specialist notes disagree; no single summary resolves | candidate |
| 7 | S5 abstraction | Quality or risk abstraction | Fixed fields | Near-miss exclusion or denominator logic tied to oxygen/readmission | Policy/reference attached if needed | hold until live workflow check |
| 8 | S3 external request | Prior authorization or post-acute appeal | Approve, deny, or request more info | Denial treats home health as enough, chart shows unsafe exertional physiology | Denial letter + functional source + off-text test | candidate |
| 9 | S1 or S6 | Post-discharge follow-up | Commit to plan | Home report says improved but objective source shows weight or oxygen deterioration | Remote-monitoring printout or nurse call log | avoid if too KM05-like |
| 10 | S3 or S2 | CDI/coding physician review | Accept or decline documented severity | Avoid pure restraint. Only use if tied to source-geometry distinction, not a known CDI trope | External query + balanced options | low priority |

## Primary Trap Families

### A. Oxygen/DME off-text readiness

Best first lever. The task does not ask, "Does the patient qualify for oxygen?" It asks for a denial appeal, discharge summary, UR note, or transition handoff where oxygen is one background item. The decisive data lives in a realistic off-text or scanned source.

Fairness route: the file is visible and realistic. The chart contains a breadcrumb. The correct answer is reachable without outside policy unless a policy file is attached.

### B. Routine handoff closure

A routine document marks a background item as done, for example equipment delivered or no oxygen need. The model finalizes the document without re-checking that background line.

Fairness route: the wrong line belongs to an external or subordinate source, or the same-author draft uses a placeholder. No same-author false assertion without correction duty.

### C. Anticoagulation transition

Useful only if it avoids OV01 reuse. Do not repeat "stop inpatient prophylaxis." A stronger variant is wrong dose, duplicate therapy, wrong hold/restart date, or external SNF list conflict tied to renal function or bleeding history.

Fairness route: forced inventory or external document. Chart contradiction is explicit.

### D. System failure RCA

The clinical event is not only a diagnosis. The deliverable forces causal analysis: proximate cause, root cause, contributing factors, corrective actions. This follows the Opus RCA example.

Fairness route: the source chain documents the system failure. The model must not get full credit for blaming patient nonadherence alone.

## Source Geometry Rules

- No world-level discharge summary that states the answer.
- No single respiratory note that resolves oxygen readiness by itself.
- Off-text or scanned evidence must be peripheral to the deliverable, not central to the task's obvious work.
- Payer, vendor, SNF, pharmacy, and case-management documents may be wrong by genre.
- World files provide raw facts. Task-level files create the forced move.
- At least 30 world-level files are planned before spec.

## Candidate Source Set

World-level raw substrate candidates:

- ED physician note.
- Admission H&P.
- Hospitalist progress notes across decongestion.
- Cardiology consult.
- Nephrology consult.
- Pulmonary or RT assessment.
- Echo report.
- CXR reports.
- BNP trend.
- BMP/renal trend.
- CBC/anemia trend.
- MAR.
- Home medication list.
- Anticoagulation history.
- Telemetry or AFib summary.
- PT evaluation with exertional tolerance.
- OT evaluation with ADL and stairs.
- RT oxygen assessment note, but not the decisive off-text test.
- Case management note.
- DME coordination note.
- Nursing note.
- Discharge rights or Medicare notice.
- Family communication note.
- Sleep or COPD history note.
- PCP summary.
- Pharmacy fill history.
- Weight/I&O flowsheet.
- Wound or skin note only if needed as noise.

Task-level candidates:

- Payer denial letter.
- Scanned exertional oxygen test or walk-test sheet.
- DME vendor delivery failure note.
- Started discharge summary or transition note.
- SNF pharmacy medication reconciliation sheet.
- UR worksheet.
- Safety event intake summary.

## Early Red-Team Questions

1. Does the task surface force the model to inspect oxygen or DME? If yes, it will likely ceiling.
2. Is the wrong move in the headline? If yes, move it to a background line.
3. Does the chart merely lack support, or does it contradict the wrong move? If merely silent, redesign.
4. Is this just KM05, KM06, OV01, OV04, or OV06 in new clothing? If yes, change the axis.
5. Can a catcher get the answer without private knowledge? If no, attach the needed source or drop it.
6. Does the task use race as an assumption rather than a documented fact? If yes, rewrite it.

## Next Step

Alexander edits this canvas. Once the task slate is approved, draft the four-part Brainstorm from the high-level version only.

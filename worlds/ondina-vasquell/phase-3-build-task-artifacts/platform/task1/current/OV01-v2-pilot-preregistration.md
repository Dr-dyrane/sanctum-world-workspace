# OV01 v2 PILOT PREREGISTRATION - locked before re-upload, AutoQC, and re-pilot

Rule: this file does not change after the pilot lands. Post-pilot reconciliation goes in a results record citing this file. The v1 prereg and its result (ceiling) stand; this v2 adds the cold trap.

## Why v2
OV01 v1 ceilinged: job 20965cc6, scores 96/92/92/82/92/95/95/95/92/92 (mean ~92, zero sub-70, lowest 82 is a strong answer). All traps sat on the warm med-rec axis (renal dosing, held agents, deep culture, sulfa allergy) which the model hunts and handles by default. Difficulty problem, not grader problem.

## Mechanism under test (v2)
A COLD verification-asymmetry trap: the preliminary discharge order set (E1-T1) carries forward inpatient enoxaparin 40 mg SC daily VTE prophylaxis (now a real active inpatient med on the MAR). The correct reconciliation DISCONTINUES it at discharge (inpatient-only prophylaxis for reduced mobility; not a home med; adds bleeding risk on aspirin + clopidogrel). It is a cold axis (not the med-rec headline), forced (it is in the carried-forward list to disposition), and exploits verification asymmetry (the model propagates an inherited carried item without re-deriving its appropriateness). Fairness: the order set is an explicitly unreconciled, wrong-by-genre external draft the model is expected to reconcile; no telegraph in the order-set note.
Central failure = continuing the carried-forward inpatient enoxaparin at discharge. Secondary (warm) failures retained: carrying admission antibiotic dosing forward; silently resuming a held agent.

## Base rates
v1 same-task: ceiling (mean ~92, 0 sub-70). Nearest analogue is KM01 med-rec (89, soft) and the completion-genre propagation family (KM02-06 floored when a cold inherited item was propagated).

## Forecast
Bimodal. Floor 0.30 to 0.55 = continues the enoxaparin (rubber-stamps the carried-forward list); catcher 0.85 to 0.95 = discontinues it and is correct on the warm axes. Expect 2 to 5 of 10 runs to continue the enoxaparin. Mean roughly 60 to 80. At least one sub-70 if the propagation lands; per King P the bankable signal is the legitimate continued-prophylaxis failure, not the mean.

## Read rules (set now)
- A floor continues (or fails to address) the inpatient VTE prophylaxis at discharge. A catcher discontinues it and engages the chart.
- Continuing enoxaparin is a real, defensible clinical failure (unnecessary anticoagulation + bleeding risk on dual antiplatelet), not cosmetic.
- Lowest genuine-failure run = failure-analysis subject; cleanest catcher = grader-analysis anchor. Failure-only, no section names.
- If still all-catch (no floor), the cold item is not cold enough or the order-set note telegraphs; re-center, do not tighten the grader.

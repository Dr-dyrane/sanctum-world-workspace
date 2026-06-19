# Marva Lydell: comorbidity + medication expansion (v2, corrected and master-packet-reconciled)

Date 2026-06-19. v2 supersedes v1 after the review of 2026-06-19. Doses go to the World Spec; name agents only here. Reconciled to W3-MASTER-PACKET Part 2 (spent levers) and Part 3 (substrate upgrade).

RATIFIED 2026-06-19: HFpEF confirmed; noise tier kept (hypothyroidism, GERD, constipation), declared noise; PAD omitted. Applied to submission/Marva_Lydell_Brainstorm.md World Setup (12 core + 3 noise = 15 named comorbidities; about 17 named baseline agents plus home oxygen and CPAP) and the docx rebuilt. Floor mechanics stay at the task/spec layer per the med-floor-to-task map below; the brainstorm carries only the clean substrate.

## The reframe that drove every correction
Substrate does NOT arm floors. "A clean, internally-consistent chart is the IDEAL substrate; floors are MANUFACTURED AT THE TASK LAYER on top of it" (FLOOR-MECHANISM-LIBRARY.md:5). The substrate's job is to be clinically clean, supply the competing-authority and quiet-baseline material, and PRESERVE genuinely silent axes for a later task to exploit. Naming or actively managing an axis primes it and kills the floor it was meant to enable. v1 inverted this; v2 fixes it.

## Corrections applied (from the review)
1. Bone-health stays SILENT: cholecalciferol only, no named secondary hyperparathyroidism, no calcitriol or sevelamer, no "no recent DEXA" callout (the callout is itself a prime). A patient on calcitriol+sevelamer has a managed, loud bone-mineral program; that is FLOOR-MECHANISM-LIBRARY.md:93's do-not-use axis.
2. Held-GDMT and "hyperkalemia integration" are ONE decision, merged. Hyperkalemia is the reason the RAAS/MRA agents are held, so the held state is the safe answer; there is no second wrong move to integrate. Held-med restart is also primed (KM03 cardiorenal restart scored ~94 and was killed). Kept as a single mechanism (held GDMT resume); hyperkalemia, if used at all, rides an external wrong-by-genre list only, low confidence (KM's salt-substitute version did not floor).
3. The med floors are real but have NO fair home in the med-rec task (Task 2 primes find-the-error; OV05 ceilinged 3x and was retired). They are RELOCATED, not deleted, to a completion or handoff frame on a background line, or to an external list. See the med-floor-to-task map.
4. Reconciled to the master packet: OSA/CPAP is SPENT (KM03 + OV04 banked it), demoted to backdrop; anemia and perfusion are spent loud axes, kept quiet.
5. ESA dropped (it makes anemia loud via Hgb targets); ferrous sulfate alone. Every comorbidity is gated load-bearing, backdrop, or noise.

Discipline caveat (FLOOR-MECHANISM-LIBRARY.md:54-63): a cold-bench ceiling is not a verdict; we have under-counted floors twice by retiring on prediction. So the ceiling-risk calls below mean "relocate and bench cold, then pilot," never "delete."

## HFpEF vs HFrEF: adopt HFpEF
A 72-year-old obese woman with CKD, AFib, HTN, and COPD is the textbook HFpEF phenotype. It also sharpens the on-thesis dyspnea-attribution ambiguity (HF vs COPD vs deconditioning vs exertional desaturation) that the transition-readiness thesis needs. The HFrEF case for a "richer held-GDMT" set is weak, because those medication floors mostly ceiling in this admin-heavy slate anyway. HFpEF GDMT is SGLT2 inhibitor + MRA + diuretic + comorbidity control, which is the agent list below.

## Comorbidities (each gated; target 12-13 clean, common, interacting)
| # | Condition | Role | Note |
|---|---|---|---|
| 1 | Heart failure, preserved EF | LOAD-BEARING | the cardiology-vs-nephrology axis and volume-vs-readiness; keep management clean, not pre-resolved |
| 2 | Atrial fibrillation, anticoagulated | LOAD-BEARING | feeds the renally-cleared DOAC dosing / external duplicate-anticoagulant lever (master packet Part 2) |
| 3 | CKD stage 3b-4 | LOAD-BEARING | renal recovery vs admission value (quiet baseline); renally-cleared dosing |
| 4 | COPD | LOAD-BEARING | dyspnea-attribution ambiguity; exertional oxygen |
| 5 | Obstructive sleep apnea | BACKDROP | SPENT (KM03/OV04). Present for realism; NOT a floor axis |
| 6 | Type 2 diabetes | LOAD-BEARING | held metformin; discharge-insulin de-escalation (task-layer, relocated) |
| 7 | Hypertension | LOAD-BEARING | held RAAS agent; hemodynamic readiness |
| 8 | Obesity | BACKDROP | OSA/HFpEF realism, functional reserve |
| 9 | Coronary artery disease (prior MI/PCI) | BACKDROP | secondary-prevention realism (statin, antiplatelet); NOT a dominant arc or floor-carrier |
| 10 | Anemia of CKD | BACKDROP, QUIET | stable, never flagged open (spent loud axis); ferrous only |
| 11 | Diabetic peripheral neuropathy | BACKDROP | functional reserve, gabapentin; not single-cause |
| 12 | Vitamin D deficiency on cholecalciferol | SILENT-AXIS SUBSTRATE | cholecalciferol only, no dx, no DEXA note; preserves the silent bone axis for a possible later over-closure task |

NOISE tier (label as noise per KM's half-thread lesson; add only for realistic filtering, never scored): hypothyroidism (levothyroxine), GERD (pantoprazole), chronic constipation (PEG/senna). Declare these noise so a later task does not accidentally treat them as load-bearing.

## Medications (HFpEF; specific agents; doses to the World Spec)
| Medication | For | Role |
|---|---|---|
| Empagliflozin | HFpEF/CKD/DM | held in acute illness; part of the held-GDMT resume lever (task-layer) |
| Spironolactone | HFpEF MRA | held in AKI for potassium; part of the held set |
| Torsemide or furosemide | congestion | volume vs renal recovery (cards vs neph) |
| Metoprolol succinate | AFib rate, CAD | rate/hemodynamics |
| Losartan or lisinopril | HTN | held RAAS agent in AKI; part of the held set |
| Apixaban | AFib | renally-cleared DOAC dosing; external duplicate-anticoagulant lever |
| Aspirin (+/- clopidogrel) | CAD/PCI | the antiplatelet half of the external duplicate-therapy list (NOT in the med-rec deliverable) |
| Metformin | T2DM | held in AKI; part of the held-GDMT resume lever |
| Insulin glargine (+ home sliding scale) | T2DM | discharge-insulin de-escalation lever (task-layer) |
| Atorvastatin | CAD/lipids | chronic protective; background |
| Cholecalciferol | vitamin D | SILENT bone axis; no calcitriol, no sevelamer |
| Ferrous sulfate | anemia | quiet; no ESA |
| Tiotropium + albuterol, home oxygen, CPAP | COPD/OSA | respiratory backdrop + the fresh oxygen/DME levers (task-layer) |
| Gabapentin | neuropathy | functional/medication-management realism |
| Levothyroxine; pantoprazole; PEG/senna | noise | reconciliation distractors only |

## Med-floor to task map (the relocation fix)
The substrate carries these agents cleanly; the FLOOR is built at the task layer, de-telegraphed, on a background line, never in the find-the-error med-rec frame.
- Held-GDMT resume (metformin / empagliflozin / RAAS / MRA held in AKI): build at Task 4 (transition-note completion) or Task 6 (consult handoff), as a background discharge-medication line the model rubber-stamps. This is the OV09 v4 engine. NOT Task 2 (med rec primes it and ceilings, OV05).
- Discharge-insulin de-escalation (stop the home sliding scale): Task 4 transition note, background line. The OV03 engine. NOT Task 2.
- Renally-cleared DOAC dosing / duplicate anticoagulant (apixaban at admission renal function, or apixaban + antiplatelet): an external SNF or pharmacy intake list that is wrong by genre (master packet Part 2 fresh lever; the OV07/OV08 external-instrument fair form), surfaced in Task 5 coordination or Task 6 handoff. NOT a med-rec catch.
- Task 2 (med rec) therefore carries a DIFFERENT, non-textbook trap or runs as a likely catcher; do not stack the above into it.

## Guardrails to hold while building the chart
- Keep quiet, never flag open: anemia, perfusion/PAD, bone-mineral status, OSA adequacy. These are spent or loud; a flagged-open axis primes the model and ceilings.
- Quiet baselines to plant (master packet Part 3.3): baseline creatinine/eGFR, dry weight, home oxygen status, baseline hemoglobin. The model must use the baseline, not the admission or discharge value. Do NOT add a "no recent DEXA" line; that primes the silent bone axis.
- Competing authorities (Part 3.1): cardiology, nephrology, pulmonology/RT each defensible-but-incomplete, none self-incriminating.
- Frozen-world and phase: this is Brainstorm/Phase-A planning only. No world file, task artifact, prompt, golden, grader, or image is authorized here.

## On ratification
Confirm HFpEF and the keep/cut on the noise tier (hypothyroidism, GERD, constipation) and the optional PAD line, and I will: expand the brainstorm World Setup to the agreed clean comorbidity list, add a named baseline-medications line (no doses, no floor mechanics), re-verify the live sheet and the no-leak/dash gates, and rebuild the docx. The floor mechanics in the map above stay at the task/spec layer, not in the brainstorm.

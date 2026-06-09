# FI-W13 - Medication Administration / Inpatient Medication Action Source

File ID: FI-W13

File Type: Medication administration / inpatient medication action source

Level: World-Level

Approximate Date / Anchor: HD1-HD6 through 05/23/2026 18:00

Author / Source: MAR / inpatient medication source

Tool / Origin: Writer-created synthetic data source

Purpose: Show medication holds, continuations, inpatient-only actions, and reassessment opportunities without creating a discharge medication list.

Supported Workflow(s) / Trap(s) / Friction(s): Discharge Medication Reconciliation; Interdisciplinary Care Plan Development and Documentation; Traps #1, #2; Cardiology vs Nephrology; Endocrinology vs Primary Team

World Boundary: contains only medication action information available through 05/23/2026 at 18:00. It contains no completed discharge medication list, post-discharge medication plan, task framing, expected output, golden response, or grader guidance.

## Medication Administration / Action Summary

Patient: Korvin Merrow

Source: MAR / inpatient medication action source.

This source records inpatient actions. It does not prove outpatient adherence, final discharge appropriateness, or correct restart timing by itself.

## Source Caveats

- MAR data show what was administered, held, or reassessed in the hospital.
- MAR data do not determine what Korvin actually took at home before admission.
- MAR data do not replace verified medication reconciliation, pharmacy history, rheumatology provenance, consultant documentation, or discharge planning.
- Inpatient-only medication actions are not baseline outpatient medications unless separately established.

## Chronic Medication Action Categories Through HD6

| Medication / category | Baseline role | Inpatient action pattern through 05/23/2026 18:00 | Reasoning implication |
| --- | --- | --- | --- |
| Sacubitril/valsartan | HFrEF guideline-directed therapy | Held early during AKI/hemodynamic vulnerability; reassessment discussed as renal/hemodynamic trend improved | Central to Cardiology vs Nephrology; early hold is not a final discharge decision |
| Carvedilol | HFrEF/CAD therapy | Temporarily held or cautiously administered depending on hemodynamic status; not a simple uninterrupted home continuation | Supports timing-sensitive restart reasoning |
| Furosemide | HFrEF volume management | Held early with poor intake/volume concern; later reassessment depends on volume and renal interpretation | Supports dehydration versus congestion reasoning |
| Spironolactone | HFrEF therapy with CKD/electrolyte relevance | Held during AKI/hyperkalemia-risk period; later reassessment not finalized by MAR alone | Supports renal/potassium safety concerns |
| Empagliflozin | HFrEF/diabetes/CKD therapy | Held during acute illness and poor intake | Supports acute-illness hold/restart complexity |
| Metformin ER | Type 2 diabetes therapy | Held during AKI/acute illness | Supports renal and intake-aware medication reconciliation |
| Insulin glargine | Basal diabetes therapy | Continued with inpatient adjustment/monitoring rather than copied exactly from home routine | Supports diabetes management complexity and discharge safety |
| Insulin lispro | Inpatient-only glycemic-management action | Used only as inpatient correctional coverage when needed; not a baseline outpatient medication | Preserves inpatient-only logic and avoids baseline medication-count drift |
| Aspirin | CAD secondary prevention | Continued unless contraindication emerged | Chronic protective therapy should not be lost casually |
| Atorvastatin | CAD/hyperlipidemia therapy | Continued | Chronic protective therapy continuity source |
| Nitroglycerin rescue medication | CAD/angina safety medication | Available as rescue medication if clinically indicated; not used as routine daily therapy | Rescue medications require reconciliation but do not drive acute course alone |
| Prednisone | PMR/steroid exposure with uncertain taper | Administered under interim inpatient plan while source reconstruction continued; home taper truth remains unresolved by MAR alone | Supports Trap #1 without proving actual pre-admission adherence |
| Gabapentin | Neuropathy symptom control | Reassessed during altered mentation/weakness; may be held or reduced depending on sedation/fall-risk concern | Supports functional/cognitive safety reasoning |
| Pantoprazole | GERD/GI protection | Continued | Supportive medication burden |
| Ferrous sulfate | Anemia support | Continued or temporarily deferred around acute intake/tolerance | Adds bowel regimen and medication-burden context |
| Alendronate | Bone-health therapy | Not administered as a routine inpatient priority; remains outpatient chronic therapy to reconcile | Supports steroid-exposure context without proving adrenal issue |
| Calcium carbonate / vitamin D combination | Bone-health support | Continued if available/tolerated | Supplement reconciliation complexity |
| Cholecalciferol | Vitamin D maintenance | Continued if available/tolerated | Supplement reconciliation complexity |
| Polyethylene glycol | Bowel regimen | Used as needed or continued based on bowel pattern | Supportive regimen and discharge instruction complexity |
| Senna | Bowel regimen | Used as needed or continued based on bowel pattern | Duplicate/supportive medication reconciliation issue |
| Acetaminophen | Pain/supportive medication | Available for pain/fever support | Benign-looking medication burden |

## Daily Medication Action Spine

### HD1-HD2

The inpatient medication pattern prioritizes acute safety:

- renal/hemodynamic-sensitive HFrEF, diabetes, and diuretic medications are held or deferred;
- chronic protective therapies that are not driving acute hemodynamic/renal risk are generally continued;
- prednisone is handled cautiously because home taper/adherence is not verified;
- inpatient correctional insulin lispro may be used for glycemic control but is not treated as a baseline medication.

### HD3-HD4

As objective trends improve, the medication question shifts from "hold during acute illness" to "what should be safely resumed, when, and under what monitoring?"

Key caution:

- MAR action history shows what happened, not what should happen next.
- Rheumatology provenance becomes available by HD4 and helps interpret intended prednisone taper, but MAR still does not prove pre-admission adherence.

### HD5-HD6 Before 18:00

Medication reassessment is active because discharge planning is plausible. The MAR supports several competing interpretations:

- Cardiology can reasonably worry that HFrEF/CAD protective medications should not be omitted indefinitely.
- Nephrology can reasonably worry that renal recovery, potassium, blood pressure, and volume status remain fragile.
- Endocrinology can reasonably worry that steroid exposure and taper ambiguity are underweighted.
- The hospitalist must reconcile actual actions, trends, source hierarchy, consultant timing, and discharge safety.

## Guardrails

FI-W13 is not a discharge medication reconciliation, final medication list, final restart plan, final steroid plan, or answer file. It must be interpreted with FI-W04, FI-W05, FI-W06, FI-W12, consultant documentation, and discharge-planning sources.

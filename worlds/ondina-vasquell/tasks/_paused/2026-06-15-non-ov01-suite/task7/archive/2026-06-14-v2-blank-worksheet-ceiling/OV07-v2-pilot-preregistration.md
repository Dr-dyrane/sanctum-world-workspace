# OV07 v2 PILOT PREREGISTRATION - locked before upload, AutoQC, and pilot

Rule: this file does not change after the pilot lands. Post-pilot reconciliation goes in a results record. v1 (half-placeholder golden, eye-exam-lookback trap) is superseded.

## Why v2
v1's golden was half-placeholder ("Value...", "apply the lookback") and its intended trap (eye-exam measurement-year lookback) is NOT a real disqualifier: the 03/15/2026 dilated exam sits inside the 2026 measurement year, so crediting it is correct. That trap would graze or make a wrong golden. v2 re-centers on a genuine, material, version-independent disqualifier and writes concrete abstracted values for every field.

## Mechanism under test (v2) - undated HbA1c
The chart documents the HbA1c only as "last A1c 8.6 percent" (admission H&P, endocrine note, outpatient summary) with NO draw date anywhere. The worksheet field is "most recent HbA1c AND date." The correct abstraction reports the value (8.6 percent) but marks the DATE unable to determine, because an undated result cannot be placed in the measurement period, and does NOT force the glycemic numerator. The central failure = treating the undated "last A1c 8.6 percent" as a dated in-period result and forcing the numerator - fabricated quality-measure capture, a material integrity failure (not a 1-of-5 deduction). This is cold (date-absence is quiet; the default is to credit a documented value), against default, survives full reconciliation, and is version-independent (any measure needs a dated test in the period - stays item-3-clean). uACR is also absent (nephropathy handled factually via CKD + ACE inhibitor, not a second trap). Other fields are clean/creditable: eye exam 03/15/2026 (do not over-read retinopathy), foot exam documented, BP 134/76.

## Deliverable framing (physician-produced) + self-containment
The deliverable is the PHYSICIAN's review and attestation of the quality department's abstraction (authored by Lillian Everet, MD, medical-director quality-review capacity; "Draft for physician sign"), not an abstractor-authored document - fixes the v1 All-Tasks-Physician-Produced fail. The quality-department worksheet is the external INPUT (E1-T7), like the HIM coder worksheet in OV02. The worksheet defines the measurement period (01/01/2026 to 06/04/2026), so no external HEDIS measurement-year knowledge is needed (item-3 clean) and the eye exam is clearly in-window.

## File-output
Prompt asks for the attestation as a document the physician can sign (natural voice, no literal path); the harness routes saved documents to /tmp/outputs, so file-save is requested without breaking the physician voice (DO-NOT-REPEAT #18 voice correction).

## Forecast (floor canon: design 0.30-0.55 + catcher >0.85)
Bimodal. Floor 0.30 to 0.55 = forces the glycemic numerator on the undated A1c (fabricated capture). Catcher >0.85 = reports the value, marks the date unable to determine, credits the dated eye exam, abstracts the rest honestly. Mean roughly 60 to 80; target at least one genuine sub-60 material miss. Approval needs one legitimate critical/material failure, not a numeric threshold.

## Read rules (set now)
- A floor forces the glycemic numerator on the undated A1c (or forces any field the record does not date/support). A catcher marks the A1c date unable to determine and does not force capture.
- Forcing a false quality numerator is a legitimate MATERIAL failure (integrity), not cosmetic. A missing /tmp/outputs file is NOT the banked floor - bank a real material miss.
- Judge by failure legitimacy/materiality, not the number; a 0.62-0.68 graze means too soft - re-center, do not tune the grader.
- Mount gate: first-trajectory find /docs = one worksheet under /docs/filesystem, nothing under /docs/.apps_data (DO-NOT-REPEAT #16).
- Lowest genuine-failure run = FA subject; cleanest catcher = GA anchor. Failure-only, two paragraphs, no section names.

## Needs Alexander's eye before/at upload (low ambiguity, but confirm)
The undated-A1c "report value, mark date unable to determine, do not force the numerator" call is an abstraction-integrity judgment grounded in the chart (A1c is genuinely undated). Confirm comfortable. Eye exam credited as a dated in-MY exam (do not over-read retinopathy) is standard.

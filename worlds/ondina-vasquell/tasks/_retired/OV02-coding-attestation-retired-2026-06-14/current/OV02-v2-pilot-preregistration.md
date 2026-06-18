# OV02 v2 PILOT PREREGISTRATION - locked before re-upload, AutoQC, and pilot

Rule: this file does not change after the pilot lands. Post-pilot reconciliation goes in a results record citing this file. The v1 prereg stands as history; this v2 adds the cold plant.

## Why v2
OV02 v1's two steers (pressure-injury principal, acute-osteomyelitis POA) both sit on LOUD/warm axes the model hunts by default, so v1 was predicted to ceiling like OV01 v1. Per the validated OV01 pattern, one COLD verification-asymmetry plant was added (Alexander ratified candidate B on 2026-06-14).

## Mechanism under test (v2)
The HIM worksheet now proposes "Acute blood loss anemia (D62)" as a secondary, basis "hemoglobin 9.8, low." The correct attestation DECLINES it and codes anemia of chronic kidney disease (D63.1) only: the hemoglobin is stable at 9.8 / 9.7 / 9.8 / 9.8 across the stay, documented as anemia of CKD, with no bleeding or transfusion. It is a cold axis (anemia is a quiet background comorbidity, not a loud world thread), forced (a proposed code line to attest), against default (the model retains "anemia of CKD" and can rubber-stamp the acute specifier), and exploits verification asymmetry (the worksheet asserts the acute etiology; the model propagates it without re-deriving the stable trend). Surface is a neutral HIM attestation worksheet, no telegraph.
Central failure = attesting acute blood loss anemia against the stable hemoglobin. Secondary (warm) failures retained: a pressure-injury principal; attesting acute osteomyelitis as established or POA.

## Base rates
Nearest analogue is OV01 v2 clean-mount (job 741ba52f): the cold verification-asymmetry mechanism produced mean 68.0, bimodal, four sub-70. No in-world OV02 base rate.

## Forecast
Bimodal. Floor 0.30 to 0.55 = attests acute blood loss anemia (or adopts a pressure-injury principal / osteomyelitis POA). Catcher 0.85 to 0.95 = declines the acute anemia specifier, codes anemia of CKD, declines pressure-injury and osteo, retains the supported comorbidities. Mean roughly 60 to 80; expect at least one sub-70 if the cold anemia line propagates.

## Read rules (set now)
- A floor attests acute blood loss anemia (the cold central miss) or adopts a worksheet-steered pressure-injury/osteo line. A catcher declines and engages the chart.
- Attesting acute blood loss anemia for a stable chronic anemia is a real coding-integrity failure (unsupported CC upcode), not cosmetic.
- Lowest genuine-failure run = failure-analysis subject; cleanest catcher = grader-analysis anchor. Failure-only, two paragraphs each, no section names.
- Mount-hygiene gate on the first trajectory: find /docs shows one worksheet, him_preliminary_coding_worksheet_05212026.docx, under /docs/filesystem, nothing under /docs/.apps_data. Confirm before trusting any score (DO-NOT-REPEAT #16).
- If still all-catch (no floor), the cold item is not cold enough; re-center, do not tighten the grader.

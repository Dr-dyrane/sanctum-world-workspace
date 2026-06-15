# RUN INSTRUCTIONS - KM09 v2
## Workflow type: Inpatient Medical Coding and DRG Assignment
## Task: KM09 v2 - Coding attestation addendum with HIM preliminary coding summary attached

---

## Why v2 exists
AO's 6/12 review returned v1 because the prompt asked for a coding addendum but no original coding document was attached. v2 fixes the file architecture without changing the proven clinical trap. The task now mounts one original coding document: `him_preliminary_inpatient_coding_summary_05252026.docx`.

## v2 mechanism
The HIM worksheet is an external preliminary coding summary for physician review. It is intentionally severity-forward: sepsis principal, metabolic encephalopathy, acute-on-chronic systolic heart failure, and a higher DRG family. The physician must prepare the final addendum from the record, accepting documented items and rejecting unsupported ones. This is fair external-document rebuttal, not a same-author draft the model is expected to trust.

## Current upload set
- prompt-task9-v2.txt
- him_preliminary_inpatient_coding_summary_05252026.docx
- golden-KM09-v2.docx
- grader-guidelines-task9-v2.txt

## Upload sequence
1. Workflow type = Inpatient Medical Coding and DRG Assignment.
2. Prompt: prompt-task9-v2.txt.
3. Mount exactly one task file: him_preliminary_inpatient_coding_summary_05252026.docx.
4. Golden: golden-KM09-v2.docx.
5. Grader: grader-guidelines-task9-v2.txt, with access to the provided chart.
6. Mount-coherence gate before pilot: first trajectory find /docs must show exactly this one task file under /docs/filesystem, no v1 no-file state, no golden, and nothing task-specific under /docs/.apps_data.

## How to read the pilot
- Central floor: final addendum sequences A41.9 sepsis or R65.2 severe sepsis as principal, carries sepsis as a secondary code, or claims the septicemia family on the worksheet's severity framing.
- Secondary floor: G93.41 metabolic encephalopathy, I50.23 acute-on-chronic HF, or a with-MCC tier claimed from those diagnoses.
- Catch: N39.0 principal under suspected-at-discharge rule, documented-only secondary set, symptom-level R41.82, kidney/UTI without-MCC tier, unsupported worksheet items rejected or routed as query opportunities.

## Expected residuals
Self-Contained Guidelines may flag because the grader is chart-aware. This is intentional: the model is synthesizing from the record plus an external worksheet, and the grader must verify true chart details before calling them unsupported.

Boundaries: no upload, AutoQC, pilot, QA, FA/GA, PL, or RLS mutation without explicit Alexander authorization for that exact step.

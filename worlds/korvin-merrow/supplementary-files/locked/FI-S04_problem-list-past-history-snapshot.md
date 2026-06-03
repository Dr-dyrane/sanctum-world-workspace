# FI-S04 - Problem List / Past History Snapshot

File ID: FI-S04

File Type: Problem list / past history snapshot

Level: Supplementary

Approximate Date / Anchor: HD1 or pre-admission import

Author / Source: Chart problem-list source

Tool / Origin: Writer-created supplementary chart file

Purpose: Provide background comorbidity/procedure texture while keeping authoritative facts in stronger sources.

Supported Workflow(s) / Trap(s) / Friction(s): Hospital Discharge Summary Generation; Discharge Medication Reconciliation; source-hierarchy texture

World Boundary: contains only low-authority imported problem-list / past-history texture available at admission. It contains no final diagnosis list, final discharge problem list, final medication reconciliation, prednisone source-of-truth answer, task framing, expected output, golden response, grader guidance, AutoQC response, DOCX artifact, or submission material.

## Imported Problem List / Past History Snapshot

Patient: Korvin Merrow

Source type: imported chart problem-list / past-history snapshot

Approximate anchor: HD1 or pre-admission import

This snapshot reflects background chart history available to clinicians. It is a low-authority orientation source and may include carried-forward or non-final problem-list phrasing.

It is not an attending assessment, consultant assessment, verified medication reconciliation, pharmacy history, rheumatology source, discharge summary, or final problem list.

## Background Problem List Texture

Problem-list entries include chronic conditions already represented in stronger locked sources:

- HFrEF.
- CAD with remote PCI / coronary stent history.
- Hypertension.
- Hyperlipidemia.
- CKD stage 3.
- Type 2 diabetes mellitus.
- Diabetic peripheral neuropathy.
- Obstructive sleep apnea.
- PMR / chronic steroid exposure history.
- Anemia of CKD.
- Osteoporosis / osteopenia related to chronic steroid exposure.
- Class I obesity.
- Chronic GERD / acid-suppression indication.
- Chronic constipation tendency.

This list provides background texture only. It does not create new diagnoses and should not be treated as a final diagnosis hierarchy.

## Procedure / History Texture

The imported history includes remote PCI / coronary stent placement and remote sleep-study history supporting OSA documentation.

This problem-list snapshot does not contain operative details, sleep-study values, acute procedural findings, inpatient procedures, or new surgical history.

## Medication And Prednisone Boundaries

This file does not contain a medication list.

It does not determine:

- home medication truth;
- final medication reconciliation;
- final discharge medication list;
- GDMT restart timing;
- diabetes discharge regimen;
- prednisone taper truth.

If prednisone, chronic steroid exposure, or PMR appears in problem-list language, that wording is background only. It does not outrank the locked prednisone source-of-truth hierarchy:

1. Rheumatology attending recommendation.
2. Verified medication reconciliation.
3. Pharmacy / refill history.
4. Family report.
5. Patient recollection.

## Source-Hierarchy Interpretation

FI-S04 is useful when a clinician wants quick background orientation.

It is not sufficient when sources disagree.

For factual conflict resolution, use the locked master source-of-truth hierarchy and relevant stronger files. This problem-list snapshot should not be used to override attending documentation, verified medication reconciliation, pharmacy history, consultant documentation, primary care documentation, family report, or patient recollection.

## Guardrails

FI-S04 must not become a prednisone source or copy-forward answer file.

It must not:

- create a final diagnosis list;
- create a final discharge problem list;
- create a medication-reconciliation answer;
- resolve PMR/prednisone ambiguity;
- replace rheumatology provenance;
- replace verified medication reconciliation;
- introduce new diagnoses or procedures;
- carry sole critical evidence.

No post-world information, discharge outcome, +7 follow-up information, +30 follow-up information, task prompt, expected output, golden response, grader guidance, AutoQC response, DOCX artifact, or submission material is present.

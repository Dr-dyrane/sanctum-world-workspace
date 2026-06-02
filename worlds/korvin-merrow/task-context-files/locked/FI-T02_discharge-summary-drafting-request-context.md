# FI-T02 - Discharge Summary Drafting Request Context

File ID: FI-T02

File Type: Discharge summary drafting request context

Level: Task-Level

Status: CANDIDATE REVIEW

Approximate Date / Anchor: 05/24/2026 / discharge anchor

Requester / Source: Attending hospitalist / discharging service requester

Workflow Category: Hospital Discharge Summary Generation

Priority Family: P0 tracker provenance

Purpose: Ask for accurate hospitalization synthesis without copying early diagnosis framing forward or creating an actual discharge summary.

Supported Workflow(s) / Trap(s) / Friction(s): Hospital Discharge Summary Generation; Traps #2, #4, #5; secondary Endocrinology vs Primary Team and Family vs Primary Team support through consultant chronology, functional/family concerns, and copy-forward avoidance

## Context Framing

This task-context file frames a future discharge-summary drafting request. It is not the discharge summary, not the prompt, and not the expected output.

The attending/discharging service needs a future reviewer to synthesize the hospitalization accurately from the locked world files. The summary should eventually reflect the ED-to-inpatient course, initial sepsis framing, mixed physiology, medication and consultant chronology, functional/discharge-readiness evidence, family concerns, and unresolved caveats without over-trusting any single visible source.

## Required World-File Synthesis

The future review must synthesize, at minimum:

| Source family | Locked file IDs | Why review is required |
| --- | --- | --- |
| ED and admission frame | FI-W01, FI-W02, FI-W03 | Establish presentation, initial sepsis-oriented reasoning, baseline deviation, near-fall context, and admission problem list. |
| Baseline and chronic context | FI-W07 | Preserve baseline function, cognition, chronic disease burden, outpatient medication context, and follow-up frame. |
| Hospitalist course | FI-W08, FI-W09, FI-W10, FI-W11 | Reconstruct HD1-HD6 evolution without copy-forward anchoring or flattening unresolved issues. |
| Objective trends | FI-W12 | Separate clinical improvement from remaining renal, hemodynamic, glucose, intake, and discharge-safety concerns. |
| Consultant chronology | FI-W14, FI-W15, FI-W16 | Capture consultant timing and reasoning without making any consultant the final authority. |
| Functional and family evidence | FI-W17, FI-W18, FI-W19, FI-W20 | Avoid missing buried functional/cognitive evidence and meaningful family baseline comparison. |
| Discharge-facing snapshot | FI-W22 | Reconcile the visible plan with the broader chart rather than treating it as a complete discharge summary. |

## Summary-Scope Frame

The future discharge-summary work should be oriented to:

- presentation and reason for admission;
- initial suspected urinary-source sepsis frame as clinically reasonable;
- hospital course by evolution, not merely by copied problem list;
- renal/HF medication and consultant sequencing uncertainty;
- prednisone-source ambiguity and endocrine risk interpretation without hidden-diagnosis drift;
- functional/cognitive status and discharge-readiness uncertainty;
- family concerns as meaningful but not independently dispositive;
- follow-up and unresolved issues evident in locked world files.

This file does not draft the summary and does not specify final wording.

## Trap Preservation

Trap #4 is primary for this context. The future reviewer must not write the hospitalization as if sepsis was either the entire answer or a false lead. Early sepsis-oriented management was reasonable, while later persistent issues required reassessment.

Trap #2 is secondary because the summary must accurately represent medication holds, reassessments, consultant tensions, and uncertainty without implying a final medication answer.

Trap #5 is active because FI-W22 is visible and organized but incomplete; it cannot substitute for the full chart.

## Friction Preservation

Endocrinology vs Primary Team is secondary. A future summary may need to mention steroid-risk interpretation and prednisone uncertainty, but it must not prove adrenal insufficiency or make endocrinology the final explanation for admission.

Family vs Primary Team is secondary. Family concerns should be visible in the future summary only through accurate synthesis of baseline deviation, functional evidence, and discharge planning context; they must not make the primary team careless or make discharge obviously unsafe by themselves.

## Source-Of-Truth Safeguards

- Attending/hospitalist documentation carries inpatient synthesis but must be reconciled with consultants, trends, functional sources, family report, and discharge-facing sources.
- Consultant notes are interpretation sources, not final disposition or medication-plan authorities.
- Functional/cognitive evidence may live outside physician summaries.
- FI-W22 is a planning snapshot and not a completed discharge summary.

## Prohibited Content

This file does not contain:

- an actual discharge summary;
- final diagnoses beyond locked facts;
- a hidden diagnosis reveal;
- a complete hospital-course answer;
- a final medication plan;
- a final disposition decision;
- a task prompt;
- an expected output;
- a golden response;
- grader guidance;
- post-discharge outcomes.

## Candidate Review Note

Candidate reviewers should verify that this file asks for accurate synthesis while preserving sepsis anchoring risk, source hierarchy, consultant defensibility, functional evidence, and FI-W22 incompleteness.

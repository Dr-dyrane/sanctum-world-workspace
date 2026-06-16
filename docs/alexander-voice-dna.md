# Dr. Alexander Voice DNA (output-text standard)

The standard for ALL output text in this repo. Every artifact a reviewer or grader reads - prompts, goldens, grader guidelines, failure and grader analyses (FA/GA), preference labels, and reviews - must read like a busy clinician working a chart, not like an AI explaining what it did.

Enforced by `tools/verify/verify_voice.py`: banned AI transitions hard-fail active deliverables (graders, prompts, goldens, FA/GA, PLs); reviews, templates, and archived copies warn. Run it before any upload or handoff.

Effective 2026-06-16, this standard governs every newly authored or re-entered note. Already-saved and delivered notes are grandfathered and are not retro-fixed; revise them only on re-entry (same rule as the FA/GA-format and KM old-format changes). `verify_voice` warnings on existing artifacts are informational, not cleanup tasks.

## Scope and how it layers

This voice governs output text. It does not replace the structural canons; it sits on top of them.

- Goldens: keep the clinical document voice in `docs/clinical-voice-lessons.md`. Alexander voice tightens prose and removes AI tells. It does not change clinical content or the physician-produced framing.
- Graders: keep the Sang five-block in `docs/grader-guidelines-lessons.md`. Alexander voice applies to the prose inside the blocks.
- FA/GA: keep failure-only and no-section-names (Abi, 2026-06-09). Alexander voice is HOW the failure is stated.
- Prompts: keep the short first-person in-role ask. Alexander voice keeps it declarative and free of meta-guidance.
- Preference labels: keep the house PL structure. Alexander voice applies to the justification prose.

## Core identity

Dr. Alexander is an internal medicine physician doing chart review, quality review, utilization review, or peer review. Clinically focused. Pragmatic. Time conscious. Direct. Comfortable with medical shorthand. More interested in clinical consequence than process, and in patient care than documentation mechanics. The writing should sound like someone reviewing charts between patients, not someone writing an academic paper.

## What Alexander notices

Focus on: missed diagnoses, missed findings, missed follow up, missed risk factors, inaccurate assessment, incomplete management plans, medication issues, disposition concerns, patient safety implications.

Do not focus on, unless explicitly required: workflow mechanics, prompting behavior, OCR behavior, file navigation, model actions, technical process detail.

## The review pattern

When identifying a problem:

1. State the omission.
2. State why it matters clinically.
3. State the consequence.

Write: "Poor CPAP adherence was not addressed. This affects assessment of OSA control and follow up planning."

Not: "The model failed to review the compliance report and therefore failed to identify the adherence issue."

## Sentence style

Short declarative statements. Examples: "The note was otherwise accurate." "The major omission was poor CPAP adherence." "This affected the assessment." "Follow up planning was incomplete." "The score is appropriate."

Avoid long sentences. Avoid multiple commas, semicolons, or nested clauses. If a sentence can be shortened without losing meaning, shorten it.

## Vocabulary

Use the natural clinical register: OSA, COPD, CHF, follow up, hospital course, disease control, adherence, assessment, management, disposition, clinical significance, medication reconciliation, risk, findings.

Prefer "poor CPAP adherence", not "suboptimal compliance with prescribed positive airway pressure therapy".

## Review writing rules

Do not narrate the evaluation process. Do not explain how information was discovered. Do not explain how the model arrived at its answer. Discuss what was missed, why it mattered, and how it affected the final assessment. The review should read like physician QA documentation.

## Humanization

Rarely write: Furthermore, Moreover, Consequently, Notably, In addition, salient finding, critical insight, robust analysis, comprehensive review.

Often write: "The note was otherwise accurate." "The major omission was..." "This affected..." "Follow up was not addressed." "The score is appropriate." "Credit is warranted for..."

## Compression rule

Before finalizing any paragraph ask: could an attending say this out loud during chart review? If yes, keep it. If no, shorten it. Remove unnecessary explanation. Remove AI transitions. Remove workflow detail. Keep the clinical point.

## Final test

A reader should conclude: this was written by a physician reviewing a chart. They should never conclude: this was written by an AI explaining what happened.

## Worked exemplar - accepted FA/GA (OV04)

This is the accepted standard. It names the failure mechanism in plain clinical language, leads with what the note did well, ties the omission to its clinical consequence, and credits the accurate parts. It does not carry evaluation scaffolding.

Failure Analysis

On Attempt 9, the model produced a solid note from the chart, correctly reconciling medications, summarizing the patient's hospital course, and documenting appropriate follow up plans. However, it missed the main finding in this case. The CPAP compliance report was available as an image file, but the model never opened or reviewed it. Because the report was not reviewed, the model missed the patient's poor CPAP adherence and the evidence of ongoing obstructive sleep apnea. The note stated the patient would continue home CPAP and did not raise any adherence concerns or recommend sleep medicine follow up. Since this information was only present in the device report, the final note was missing an important part of the patient's overall assessment.

Grader Analysis

The 0.20 score is appropriate. The note accurately captured most aspects of the hospitalization but failed to identify the poor CPAP adherence documented in the compliance report. As a result, the patient's obstructive sleep apnea was presented as stable on home CPAP despite evidence of inadequate treatment. Credit is warranted for the otherwise accurate medication reconciliation, hospital course, and follow up planning. However, the missed CPAP finding was clinically significant and affected the overall assessment, making the assigned score reasonable.

Acceptable, because it is the clinical mechanism: the report was an image file the model never opened or reviewed. Not acceptable, because it is evaluation scaffolding: OCR, "saw it in the directory listing," "confirmed from the transcript," and run or job IDs.

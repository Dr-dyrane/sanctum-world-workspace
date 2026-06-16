# Dr. Alexander Voice DNA (output-text standard)

The standard for ALL output text in this repo. Every artifact a reviewer or grader reads - prompts, goldens, grader guidelines, failure and grader analyses (FA/GA), preference labels, and reviews - must read like a busy clinician working a chart, not like an AI explaining what it did.

Enforced by `tools/verify/verify_voice.py`: banned AI transitions hard-fail active deliverables (graders, prompts, goldens, FA/GA, PLs); reviews, templates, and archived copies warn. Run it before any upload or handoff.

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

# World Spec Checklist

Source indexed: `reference/source/New Writers Version - Instruction Guide (05_24).md`

Use this checklist after Brainstorm approval and before World Spec AutoQC.

## Scope

- The World Spec is the buildable blueprint for the world.
- During onboarding, focus on the spec document only unless explicitly instructed otherwise.
- Do not proceed into synthetic file generation, task execution, golden responses, grader guidelines, or failure analysis.
- The spec should be specific enough for a non-domain-expert builder to draft realistic files.

## Canonical Sections

1. Clinical Scenario
2. Task Specifications
3. World File Plan
4. World Summary

## Section 1: Clinical Scenario

- Big Picture Summary: 1-2 paragraphs describing patient, clinical picture, task architecture, and why the world is hard.
- Patient Profile: complete relevant demographics, allergies, MRN, pre-existing conditions, and active problem list.
- Optional structured tables where useful: home medication list, hospital course timeline, decision friction table, data hierarchy note.
- Clinical History and Context: continuous authoritative narrative detailed enough to support file generation.
- Key Milestones: chronological table containing every date referenced in tasks, traps, filenames, or file descriptions.
- Clinical Complexity Overview: explain why the case is hard, not just what diagnoses exist.
- Use fictional patients, dates, names, and identifying details.

## Section 2: Task Specifications

- Plan 5-10 tasks.
- Reconcile the task section against `reference/workflows/internal-medicine-world-planning-canvas.md`; every task should retain its structure, forced slot, trap route, fairness route, source geometry, grader mode, and reachability plan from the pre-brainstorm canvas.
- At least one task should map to a P0 workflow.
- Tasks should span multiple clinical workflows and reasoning demands.
- Each task should include workflow, draft prompt, expected output, failure design, and task-level files.
- The actual task prompt must be human-written by the physician expert.
- Draft prompts should sound like real clinical requests, not test questions.
- Prompts should not reveal workflow metadata, failure design, file IDs, trap hints, or reviewer scaffolding.
- Expected output should be precise enough that graders can score consistently.
- Failure design should include the 5-6 highest-yield traps with remediations.
- Task-level files should use the E#-T# convention when needed.
- Tasks must be independent and anchored after the world snapshot.

## Section 3: World File Plan

- Design files after tasks.
- Each essential file exists because at least one task needs it.
- Use the source geometry board from `reference/workflows/internal-medicine-world-planning-canvas.md` to prove no shared world file is acting as an answer-key synthesis.
- Supplementary files add realistic noise only and must not carry trap content.
- Aim for approximately 90% essential and 10% supplementary.
- Starting 06/10/2026, new worlds need at least 30 world-level files unless project leadership grants an explicit exception. Task-level files do not count toward the world-level minimum.
- Include at least 3-4 file modalities where appropriate.
- No single file should resolve a task by itself.
- Every essential file needs either a reference/template origin or a description detailed enough for a non-domain-expert builder.
- Include dates in filenames and in documents.
- File descriptions should specify clinical content, structure, findings, exclusions, and embedded trap/friction content.
- Establish a data hierarchy when sources conflict.

## Section 4: World Summary

- Write 3-5 sentences.
- State what clinical or regulatory reasoning the world tests.
- Explain why the trap architecture works.
- Explain why the world is hard for an AI agent to navigate.

## Cross-Cutting Checks

- Every claim in a correct task answer is traceable to the task prompt, task-level files, or world-level files.
- Every date appears in the Key Milestones table.
- Every trap has an identifiable source file.
- Frictions and traps are clearly separated.
- Source-of-truth hierarchy is explicit when conflicts matter.
- Patient names, provider names, dates, medication doses, lab values, and diagnoses are consistent.
- Traps are reasonably ambiguous: buried enough to miss, discoverable enough to be fair.
- Avoid over-authoritative summary documents unless they are outdated, incomplete, or wrong in a material respect.

## AutoQC Preparation

- Run RLS World Spec AutoQC before human review.
- Address every valid AutoQC item.
- Re-upload and rerun AutoQC after edits.
- Document any false-positive disagreement with reasoning.
- Mark diagnostics reviewed before submitting.

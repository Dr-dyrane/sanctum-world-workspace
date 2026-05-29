# Brainstorm Checklist

Source indexed: `reference/New Writers Version - Instruction Guide (05_24).md`

Use this checklist before Brainstorm AutoQC and Human Brainstorm Review.

## Scope

- Brainstorm is a concept pitch, not a full spec.
- Include only high-level world design and task ideas.
- Do not include file inventories, document drafts, full timelines, golden responses, grader guidelines, or failure analysis.
- Target concise content suitable for conceptual sign-off.

## Required Sections

1. World Setup
2. Major Friction Points
3. Major Traps
4. Rough Task Ideas

## World Setup

- Name the setting and specialty explicitly.
- Describe the patient demographics, comorbidities, encounter type, and timeline shape.
- Make the patient/scenario medically coherent and internally consistent.
- Prefer a patient profile a domain expert has encountered in real practice.
- Build complexity from common interacting conditions, workflow complexity, and documentation complexity.
- Avoid stacking rare diagnoses to manufacture difficulty.

## Major Friction Points

- Include at least two realistic stakeholder or perspective conflicts.
- Name the stakeholders and what each is advocating for.
- Keep frictions distinct from traps.
- Frictions are people or perspective conflicts, such as specialist vs specialist, family vs team, PCP vs inpatient team, payer vs clinician, or regulatory framework vs clinical indication.

## Major Traps

- Include a variety of information problems.
- Describe trap type, one-line mechanism, likely source or location, and whether it is world-level or task-level.
- Favor traps that require cross-document synthesis.
- Avoid traps solvable from one file or by general medical knowledge alone.
- A strong trap should be clinically plausible, discoverable from the files, and meaningful when missed.
- Common trap types include copy-forward errors, contradictory EMR information, buried significant information, missing or insufficient information requiring uncertainty, source-of-truth ambiguity, SDOH, temporal or sequencing complexity, resume-order traps, and patient-provided inaccuracies.

## Rough Task Ideas

- Target 5-8 or more tasks for concept planning.
- Each task should map to an approved workflow category.
- At least one task should use a P0 workflow.
- Each task should name a concrete deliverable, not an open-ended question.
- Each task should identify which world elements, frictions, or traps it tests.
- Task-level traps should be distinct from world-level traps when possible.
- Tasks must be independent encounters and should be anchored after the world snapshot.

## Lead Review Expectations

- World setup is coherent and realistic.
- Frictions represent real-world clinical dilemmas.
- Traps create enough combined complexity to challenge a clinician under normal conditions.
- Tasks map to approved workflow deliverables.
- Self-containment appears achievable.
- A seasoned clinician could solve the intended tasks from the planned files alone.
- The world represents real daily work in the domain.

## Common Brainstorm Failure Patterns

- Starting with a zebra diagnosis instead of clinical workflow pain.
- Confusing frictions with traps.
- Including traps that are glaringly obvious.
- Using vague task ideas without a concrete deliverable.
- Inventing a workflow instead of mapping to the approved tracker.
- Designing tasks that would require information outside the world files.
- Letting the prompt idea hint at the trap.


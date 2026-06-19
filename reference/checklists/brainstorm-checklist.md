# Brainstorm Checklist

Source indexed: `reference/source/_superseded/instruction-doc/New Writers Version - Instruction Guide (05_24).md`

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

- Target 10 tasks for concept planning (pod rule 6/10: over 8, preferably 10, before a new world).
- Fill `reference/workflows/internal-medicine-world-planning-canvas.md` before drafting the Brainstorm. The official Brainstorm receives only the high-level outputs, but the local canvas must already account for each task surface, trap, forced slot, source route, fairness route, and grader mode.
- STRUCTURAL VARIETY IS A GATE (Abi mandate 6/10, client ask): read `docs/task-structure-dossier.md` BEFORE drafting task ideas. The slate must span at least 5 distinct structures; draft-and-finalize completion is capped at 1-2 tasks per world. Name each task's structure (S1-S8) and its native forcing function in the brainstorm.
- Design the world substrate FOR the chosen structures at this stage (a borderline case if a determination task is wanted; an external adversarial document if a ratify-or-refute task is wanted; a quiet measure-disqualifier if an abstraction task is wanted). The Korvin lesson: substrate chosen after the world is fixed cannot floor variety structures.
- Each task should map to an approved workflow category by its VERBATIM sheet string; check claim counts on the live Task Selection Categories sheet.
- At least one task should use a P0 workflow.
- Each task should name a concrete deliverable, not an open-ended question.
- Each task should identify which world elements, frictions, or traps it tests.
- Task-level traps should be distinct from world-level traps when possible.
- Use plain clinical task numbering in the reviewer-facing Brainstorm. Do not introduce local codes such as `ML01`, `ML02`, or internal build IDs unless the official template requires them.
- TEMPORAL ANCHOR IS A NON-NEGOTIABLE (instruction doc 06_02 + 06_08, plus workspace update 2026-06-18): every task encounter AND deliverable falls STRICTLY AFTER the world snapshot and at or before the present real-world date. For any new or reopened work after 2026-06-18, every evaluator-visible clinical narrative date must also be on or before 07/31/2025. A task anchored at or before the snapshot is not acceptable even if precisely stated; a late-entry note or addendum documenting a pre-snapshot encounter also fails; a future-dated task is not acceptable. Anchor tasks at varied post-snapshot timepoints. No world document may be dated after any task anchor.

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

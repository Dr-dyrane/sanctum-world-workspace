# Sanctum Core Rules

## Purpose

Project Sanctum builds realistic clinical Worlds to test frontier AI models on physician-level judgment.

The goal is not textbook recall. The goal is realistic clinical work inside messy documentation environments.

Worlds should test:

- synthesis across documents
- prioritization
- clinical uncertainty handling
- medication reasoning
- specialist conflict resolution
- safe decision-making
- recognizing when data is outdated, incomplete, or conflicting

## Core Terms

Scenario = the patient story and clinical journey.

World = the complete clinical environment: chart ecosystem, documents, timeline, competing perspectives, source conflicts, and information noise.

Task = a realistic clinician workflow performed using the World files. Tasks are independent encounters and do not depend on each other.

Trap = an information problem in the files. Examples: copy-forward error, buried finding, conflicting source of truth, temporal mismatch, outdated recommendation.

Friction = a people or perspective conflict. Examples: consultant vs consultant, family vs team, payer vs clinician.

## Quality Philosophy

Realism is the highest priority.

Complexity should come from common conditions interacting with:

- messy chart data
- medication changes
- source hierarchy problems
- competing specialist priorities
- evolving clinical context
- discharge safety concerns

Do not build rare disease puzzles. Do not rely on diagnosis recognition alone.

A strong World is solvable by a seasoned clinician from the provided files alone, but difficult for an AI that fails to synthesize, prioritize, or reconcile conflicting information.

## Physician And AI Roles

Alexander is the physician expert and source of clinical truth.

AI assists with:

- organization
- structure
- consistency checks
- formatting
- reviewer-risk auditing
- drafting from physician-supplied decisions

AI must not replace physician judgment.

AI must not invent clinical decisions, scenario concept, traps, task ideas, management plans, medication decisions, or diagnostic conclusions.

## AI Usage Boundaries

Allowed:

- brainstorming support from physician-supplied material
- boilerplate
- structured drafting
- consistency checking
- formatting
- critique against Sanctum checklists

Not allowed:

- AI-originated scenario concept
- AI-originated traps
- AI-originated task ideas
- AI-written task prompts
- AI-written golden responses
- AI-written grader guidelines

Task prompts, golden responses, and grader guidelines are 100% human-created. AI may QC them after the physician writes them, but may not write them from scratch.

## Phase Boundary

Current scope is onboarding Phase 1 only, Steps 1-6:

1. Brainstorm
2. Brainstorm AutoQC
3. Human Brainstorm Review
4. World Spec Document
5. World Spec AutoQC
6. Human World Spec Review

Do not continue into synthetic files, production task setup, agent runs, golden responses, grader guidelines, failure analysis, preference labeling, or downstream evaluation unless Alexander explicitly updates the phase.


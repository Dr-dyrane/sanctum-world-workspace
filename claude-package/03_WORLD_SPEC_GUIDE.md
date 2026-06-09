# World Spec Guide

## Purpose

The World Spec is the buildable blueprint for the World.

It tells builders/reviewers:

- patient scenario
- task architecture
- file plan
- traps and frictions
- source hierarchy
- why the World is hard

During onboarding, draft the spec only after Brainstorm GO.

## Required Sections

1. Clinical Scenario
2. Task Specifications
3. World File Plan
4. World Summary

## Section 1: Clinical Scenario

Include:

- Big Picture Summary: 1-2 paragraphs
- Patient Profile: relevant demographics, allergies, MRN, conditions, active problems
- Clinical History and Context: authoritative narrative
- Key Milestones: every date referenced in tasks, traps, files, filenames
- Clinical Complexity Overview: why this is hard, not just a diagnosis list

Optional when useful:

- home medication list
- hospital course timeline
- decision friction table
- data hierarchy note

## Section 2: Task Specifications

Plan 5-10 tasks.

Each task includes:

- workflow
- draft prompt
- expected output
- failure design
- task-level files

Rules:

- actual task prompts must be human-written by Alexander
- prompt must sound like a real clinical request
- prompt must not reveal traps, workflow metadata, file IDs, or failure design
- each task must produce a concrete, gradable output
- each task needs 5-6 high-yield traps/remediations in failure design
- tasks are independent
- tasks are anchored after the World snapshot

## Section 3: World File Plan

Design tasks before files.

File categories:

- Essential world-level: visible to all tasks, required by at least one task
- Essential task-level: task-specific required files
- Supplementary: realistic noise only; must not carry trap content

Rules:

- aim roughly 90% essential / 10% supplementary
- target at least 15-20 files unless justified
- use at least 3-4 modalities where appropriate
- no single file should resolve a task alone
- every essential file needs detailed description or reference/template origin
- include dates in filenames and documents
- specify content to include, exclude, structure, findings, and trap/friction placement
- establish source hierarchy when records conflict

## Section 4: World Summary

3-5 sentences.

Include:

- what reasoning the World tests
- why trap architecture works
- why AI will struggle

## AutoQC And Review

Before human review:

- upload World Spec to RL Studio
- run World Spec AutoQC
- address every valid item
- document false-positive disagreements
- rerun after edits
- mark diagnostics reviewed

Human review approves or sends back. Incorporate feedback and rerun AutoQC after revisions.

## Common Mistakes

- incomplete required sections
- placeholder text remains
- dates not in Key Milestones
- inconsistent names, labs, meds, doses, diagnoses
- clinical history too thin for file generation
- complexity overview restates problem list
- task expected outputs too vague
- failure design lacks plausible wrong answer/remediation
- prompt leaks trap hints or blueprint content
- files designed before tasks
- supplementary files contain trap content
- essential files underspecified
- one file resolves task
- over-authoritative summary removes reasoning need

## Approval Standard

The spec should be:

- clinically realistic
- internally consistent
- self-contained
- buildable by non-domain-expert file builders
- clear enough for reviewers/graders
- faithful to physician intent
- free of AI-invented clinical facts


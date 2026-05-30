# World Spec Required Structure

## Source-Of-Truth Rule

Source guide: `reference/New Writers Version - Instruction Guide (05_24).md`

Official local template: `reference/templates/World_Spec_Template_05_06.docx`

Official online template link: https://docs.google.com/document/d/1KT7TjQi18RQKqcZNOuwrtziX1w_V-Pd5/edit?usp=sharing&ouid=111631573631761265982&rtpof=true&sd=true

The World Spec is one document with four canonical sections:

1. Clinical Scenario
2. Task Specifications
3. World File Plan
4. World Summary

The template is the controlling structure. Examples may show depth and quality, but if examples differ from the template, follow the template.

## Section 1: Clinical Scenario

Required subsections:

- 1.1 Big Picture Summary: 1-2 paragraphs setting the scene and summarizing task architecture.
- 1.2 Patient Profile: structured clinical identity table. Keep only rows that add clinical value.
- 1.3 Clinical History and Context: continuous authoritative narrative for the whole world.
- 1.4 Key Milestones: chronological table of every date referenced in tasks, traps, or files.
- 1.5 Clinical Complexity Overview: analysis of why the world is hard, not a problem-list restatement.

Optional subsections if structurally useful:

- Home medication list
- Hospital course timeline
- Decision friction table
- Data hierarchy note

## Section 2: Task Specifications

Required for each task:

- Task title
- Workflow context: who, what, when, where
- Expected output: format, length, voice, content anchors
- Failure Design table: 5-6 highest-yield traps with remediation paths
- Task-level files using E#-T# convention, or `None. World-level files only.`
- Draft prompt in the writer's own voice as the real requester

Task prompts must be human-created by Alexander. Claude/Codex may help interview, organize, and audit, but may not write final task prompts from scratch.

## Section 3: World File Plan

Do not build files before tasks. File planning comes after task design.

Required subsections:

- 3.1 Essential Files (World-Level)
- 3.2 Essential Files (Task-Level)
- 3.3 Supplementary Files
- Total file count summary

Essential files exist because a task needs them for the correct answer. Supplementary files add realistic noise and should not change any correct answer if removed.

## Section 4: World Summary

Required length: 3-5 sentences.

Must cover:

- What clinical reasoning the world tests
- Why the trap architecture works
- Why the world is hard for an AI agent to navigate


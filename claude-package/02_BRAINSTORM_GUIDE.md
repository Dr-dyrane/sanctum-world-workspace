# Brainstorm Guide

## Brainstorm Purpose

The Brainstorm is a concept pitch for human review.

The bar is conceptual viability, not full specification quality.

Do not include:

- full file inventories
- document drafts
- full timeline
- production task prompts
- golden responses
- grader guidelines
- failure analysis

## Required Sections

1. World Setup
2. Major Friction Points
3. Major Traps
4. Rough Task Ideas

## World Setup Requirements

Include:

- setting and specialty
- patient demographics
- comorbidities
- clinical environment
- encounter type
- timeline shape
- what changes over the World

Evaluation:

- patient/scenario is coherent
- setting, specialty, encounter type, and timeline are clear
- patient fits the encounter
- domain expert would recognize the patient as realistic
- complexity comes from common conditions and workflow, not rare diagnoses

## Friction Requirements

Frictions are stakeholder or perspective conflicts.

Each friction should name:

- parties involved
- what each side is advocating
- why the disagreement matters clinically

Examples of friction types:

- specialist vs specialist
- family/caregiver vs inpatient team
- primary team vs consultant
- outpatient clinician vs inpatient team
- payer/regulatory framework vs clinician

Reject or reclassify if it is only conflicting information. Information gaps are traps, not frictions.

## Trap Requirements

Traps are information problems.

Each trap should include:

- trap type
- one-line mechanism
- planned source/location
- world-level vs task-level

Strong traps:

- are clinically plausible
- are discoverable from files
- cause meaningful error if missed
- require synthesis across multiple documents
- cannot be solved by general medical knowledge alone

Common trap types:

- copy-forward errors
- contradictory EMR information
- buried clinically significant information
- insufficient or missing information requiring acknowledged uncertainty
- source-of-truth ambiguity
- temporal or sequencing complexity
- medication reconciliation mismatch
- patient/family-provided inaccuracy
- social/discharge context affecting reasoning

## Rough Task Ideas Requirements

Target 5-8 tasks.

Each task should include:

- deliverable type
- approved workflow category if known
- which World elements it tests
- which traps/frictions it draws on
- whether it has distinct task-level traps
- anchor after the World snapshot

Tasks must be independent. Task 3 cannot assume Task 1 was completed.

At least one task should map to a P0 workflow when tracker access is available.

## Reviewer Expectations

Reviewer asks:

- Is the World realistic?
- Are frictions true people/perspective conflicts?
- Are traps varied and hard enough?
- Are task ideas concrete and workflow-based?
- Is self-containment plausible?
- Could a seasoned clinician solve from intended files alone?
- Does the World represent daily work in the domain?

## Common Failure Patterns

- zebra-driven setup
- generic scenario
- unclear setting or timeline
- frictions confused with traps
- stakeholders not named
- traps solvable from one file
- traps that are obvious or unfair
- task ideas without concrete deliverables
- invented workflows
- task ideas requiring outside information
- prompts or task descriptions that hint at traps
- AI-sounding wording

## Strong vs Weak Design

Strong:

- common comorbidities interact
- multiple documents must be reconciled
- consultant recommendations compete
- source hierarchy matters
- medication changes have consequences
- discharge safety is uncertain despite objective improvement

Weak:

- rare diagnosis stack
- one-document answer
- pure factual recall
- prompt reveals the trick
- “what is the diagnosis?” instead of real work product
- generic complexity with no chart mechanism


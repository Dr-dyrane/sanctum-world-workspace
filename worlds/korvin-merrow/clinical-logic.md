# Korvin Merrow Clinical Logic

## Active Project Context

This file preserves the evolving clinical reasoning and design philosophy for the Korvin Merrow World. It is not the final Brainstorm deliverable.

## Role Perspective

This world is designed from Alexander Udeogaranya's background as an Emergency Medicine and Internal Medicine physician managing undifferentiated adult patients in acute hospital settings and coordinating care across specialties.

## Core Mental Model

This is not a set of isolated clinical questions.

This is a complete clinical environment.

Definitions:

- Scenario = the patient story and clinical journey.
- World = the complete clinical context, chart ecosystem, documentation history, competing perspectives, and information environment.
- Tasks = realistic clinician workflows performed inside that environment.

## Purpose

Expose the gap between information recall and true clinical judgment.

The AI should not succeed by recognizing a diagnosis alone.

The world should test:

- prioritization
- pattern recognition
- synthesis across multiple documents
- handling uncertainty
- reconciling conflicting information
- safe decision-making when recommendations compete

## Clinical Environment

Emergency Medicine / Internal Medicine / acute hospital setting.

## Working Patient

62-year-old male with:

- diabetes mellitus
- hypertension
- chronic kidney disease
- cardiovascular comorbidity risk
- medication complexity
- possible steroid exposure history

## Presentation

Patient arrives with:

- altered mental status
- progressive weakness
- poor oral intake
- borderline hypotension

Initial working diagnosis: sepsis.

The case evolves beyond the first impression.

## Competing Clinical Concerns

- adrenal insufficiency from previous steroid exposure
- acute kidney injury
- electrolyte abnormalities
- medication-related complications
- possible cardiac involvement
- discharge safety concerns

## World Journey

Follow the patient through:

- emergency evaluation
- inpatient admission
- evolving diagnostic workup
- consultant recommendations
- medication changes
- treatment decisions
- discharge planning

## Expected World Documents

Potential documents may include:

- ED notes
- admission notes
- daily progress notes
- nursing documentation
- medication administration records
- laboratory trends
- imaging reports
- consultant notes
- discharge documentation

## Major Clinical Friction Themes

1. Emergency/inpatient team: focused on immediate stabilization and sepsis management.
2. Endocrinology: questions adrenal crisis/adrenal insufficiency contribution.
3. Nephrology: concerned about kidney injury and medication safety.
4. Cardiology: balances restarting long-term protective medications.
5. Family/caregivers: concerned patient has not returned to baseline despite medical stability.

## Design Principle

Do not make this a rare disease puzzle.

Complexity comes from realistic medicine:

- common diseases
- messy documentation
- competing priorities
- evolving information

## Source Of Truth

`AGENTS.md` keeps operating context.

Detailed evolving clinical design belongs under `worlds/korvin-merrow/`.

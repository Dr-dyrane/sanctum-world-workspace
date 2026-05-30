# Claude Brainstorm Review Package

Use this package for Claude review only after Alexander approves sending it. Claude is not being asked to create scenario, traps, or task ideas.

## Instructions For Claude

You are reviewing a Project Sanctum Brainstorm draft. Alexander is the physician expert and source of truth. Do not add new diagnoses, frictions, traps, tasks, medications, timelines, or clinical facts.

Your job:

1. Check the draft against the Brainstorm criteria.
2. Identify generic wording, unclear logic, missing stakeholder positions, weak trap framing, or reviewer rejection risks.
3. Preserve the physician's clinical intent.
4. Suggest tightening edits only; do not invent content.
5. Keep Brainstorm as concept pitch, not World Spec.

Do not write production task prompts, golden responses, grader guidelines, World Spec content, file inventories, exact lab values, exact dates, or synthetic documents.

## Brainstorm Criteria

Required sections:

1. World Setup
2. Major Friction Points
3. Major Traps
4. Rough Task Ideas

Evaluation:

- World setup is coherent, realistic, and clearly set in EM/IM acute hospital medicine.
- Frictions are people/perspective conflicts with stakeholders and positions.
- Traps are information problems requiring multi-document synthesis.
- Rough task ideas are realistic clinical workflows with concrete deliverables.
- Self-containment appears achievable from planned World files.
- Complexity comes from common hospital medicine, documentation, medication changes, competing recommendations, and discharge safety.
- Adrenal insufficiency is not the central reveal.

## Draft To Review

See `worlds/korvin-merrow/brainstorm.md`.

## Known Reviewer Risks To Check

- Workflow tracker mapping still pending.
- Discharge summary / med rec tasks require careful World snapshot design.
- Temporal lab trap needs concrete anchors later.
- Sepsis anchoring must remain document-driven.
- Consultant synthesis needs approved workflow label later.

## Requested Output From Claude

Return:

1. Pass/Flag table by Brainstorm section.
2. Top reviewer risks.
3. Suggested edits that preserve clinical intent.
4. Any places where wording sounds generic or AI-written.
5. Any places where a friction is actually a trap or vice versa.
6. Any places where a trap does not clearly require multi-document synthesis.


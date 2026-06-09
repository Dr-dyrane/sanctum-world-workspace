# KM04 build-phase review packet

You are red-teaming DRAFT review materials for a clinical RL-evaluation task before anything is built or uploaded. Assume zero prior context beyond the files in this packet.

## The task

World: Korvin Merrow, a 62-year-old inpatient with HFrEF/CAD, CKD3, type 2 diabetes, suspected urinary-source sepsis physiology, AKI-on-CKD, chronic prednisone exposure for PMR, functional decline, and complex discharge planning. The live world is already created with 26 agent-read files.

KM04 workflow: Consultant Synthesis / Interdisciplinary Care Plan. The deliverable is a hospitalist-led interdisciplinary plan that reconciles Cardiology, Nephrology, Endocrinology, family, functional evidence, objective trends, MAR actions, and discharge logistics. The task date is 05/24/2026.

## Deterministic setup

Do not re-select the task. The locked architecture already selected KM04. Your job is to review whether the proposed build mechanism faithfully executes that task.

## Why this packet exists

Clean KM04 likely gives a strong model the synthesis map. The chart repeatedly says both consultants can be reasonable and that FI-W22 is not a final answer. To create a fair forced slot, this packet proposes a mounted hospitalist synthesis draft that over-claims consensus and readiness. Correct behavior is to revise or refuse the draft. Failure is to ratify it.

## What to review

- `../design/KM04-design-plan-for-review.md`: design argument and source chain.
- `00-byte-verification-and-source-audit.md`: load-bearing chart facts and hashes.
- `G1-prompt-task4-escalation-DRAFT.txt`: de-telegraphed prompt draft.
- `G2-golden-and-grader-deltas-DRAFT.md`: how golden and grader would change for the mounted draft.
- `G3-mounted-synthesis-draft-SOURCE-DRAFT.md`: source concept for the mounted task file.
- `G3-mount-manifests.md`: clean vs escalation mount sets.
- `pilot-preregistration.md`: how to interpret pilot runs.
- `inputs/`: copied locked KM04 canon and FI-T04 source for local review.

## Red-team questions

1. Does the mounted draft test consultant-synthesis judgment, or does it collapse into a simple chart-reading contradiction?
2. Is the consensus overclaim tempting enough without becoming clinically unfair?
3. Are the prompt and mounted draft free of trap labels, FI IDs, architecture language, and answer-domain scaffolding?
4. Do the golden/grader deltas penalize adoption of the handed draft without docking the correct staged/conditional synthesis?
5. Is any question still being asked of Alexander that the locked world planning already answered?

## Status

Nothing is built. Nothing is uploaded. This is a review packet only.


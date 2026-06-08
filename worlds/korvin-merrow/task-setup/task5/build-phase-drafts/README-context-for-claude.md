# KM05 build-phase review packet

You are red-teaming DRAFT review materials for a clinical RL-evaluation task before anything is built or uploaded. Assume zero prior context beyond the files in this packet.

## The task

World: Korvin Merrow, a 62-year-old inpatient with HFrEF/CAD, CKD3, type 2 diabetes, suspected urinary-source sepsis physiology, AKI-on-CKD, chronic prednisone exposure for PMR, functional decline, medication-management vulnerability, and complex discharge planning. The live world is already created with 26 agent-read files.

KM05 workflow: Early Post-Discharge Follow-Up Assessment. The deliverable is an early +7 follow-up assessment anchored to 05/31/2026, based on the hospitalization evidence. The +7 anchor is not a source of new post-discharge symptoms, labs, vitals, service starts, adherence, readmissions, or outcomes.

## Deterministic setup

Do not re-select the task. The locked architecture already selected KM05. Your job is to review whether the proposed build mechanism faithfully executes that task.

## Why this packet exists

Clean KM05 likely lets a strong model preserve uncertainty and score high. To create a fair forced slot, this packet proposes a mounted outpatient pre-chart draft that over-converts hospital discharge plans into apparent +7 facts. Correct behavior is to revise the draft into verification priorities. Failure is to ratify unverified interval status.

## What to review

- `../design/KM05-design-plan-for-review.md`: design argument and source chain.
- `00-byte-verification-and-source-audit.md`: load-bearing chart facts and hashes.
- `G1-prompt-task5-escalation-DRAFT.txt`: de-telegraphed prompt draft.
- `G2-golden-and-grader-deltas-DRAFT.md`: how golden and grader would change for the mounted draft.
- `G3-mounted-followup-draft-SOURCE-DRAFT.md`: source concept for the mounted task file.
- `G3-mount-manifests.md`: clean vs escalation mount sets.
- `pilot-preregistration.md`: how to interpret pilot runs.
- `inputs/`: copied locked KM05 canon and FI-T05 source for local review.

## Red-team questions

1. Does the mounted draft test evidence-boundary judgment, or does it collapse into a simple "do not fabricate" instruction-following task?
2. Is the outpatient pre-chart draft tempting enough without becoming clinically unfair?
3. Are the prompt and mounted draft free of trap labels, FI IDs, architecture language, and answer-domain scaffolding?
4. Do the golden/grader deltas penalize ratifying unverified interval facts without docking a correct source-limited follow-up assessment?
5. Is any question still being asked of Alexander that the locked world planning already answered?

## Status

Nothing is built. Nothing is uploaded. This is a review packet only.

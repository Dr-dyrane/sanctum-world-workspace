# Ondina Vasquell - workflow map

Current operational state: OV01 only. This file preserves the workflow names for future revival, but no non-OV01 task is active after the 2026-06-15 cleanup pass.

## Active lane

| Task | Workflow to select | Priority | State |
|---|---|---|---|
| OV01 | Medication Reconciliation at Care Transitions | P0 | Active. Clean-mount pilot banked. Larry-return FA/GA ready on job `aa949641`, Attempt 6, run `28a61869`, score 0.50. |

## Parked lanes

These packets are parked at `phase-3-build-task-artifacts/platform/_paused/2026-06-15-non-ov01-suite/`. Treat them as historical candidates, not active work.

| Task | Workflow to select | Priority | State |
|---|---|---|---|
| OV03 | CDI-Coding DRG Reconciliation Review | P1 | Paused |
| OV04 | Claims Denial Analysis and Appeal Preparation | P0 | Paused |
| OV05 | Pharmacy Insurance Claim Rejection Resolution | P0 | Paused |
| OV06 | Utilization Review Concurrent Stay Documentation | P1 | Paused |
| OV07 | HEDIS Medical Record Chart Abstraction and Review | P0 | Paused |
| OV08 | Referral Intake, Triage, and Scheduling Coordination | P1 | Paused |
| OV09 | Patient Safety Indicator (PSI) Analysis and Reporting | P2 | Paused |
| OV10 | Medical Transcription and Clinical Documentation Completion | P0 | Paused |

## Retired lane

| Task | Former workflow | State |
|---|---|---|
| OV02 | Inpatient Medical Coding and DRG Assignment | Retired after repeated coding-attestation ceilings. Archive stays under `phase-3-build-task-artifacts/platform/_retired/`. |

Before reviving any parked task, verify the workflow name on the live Task Selection Categories sheet and update this map plus `OV-WORLD-STATUS.md`.

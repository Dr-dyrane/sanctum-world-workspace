# Approved Task Selection Categories + guidance (Abi, 2026-06-13) - Vagus pod

Source of truth: the 06/13/2026 PDF Task Selection Tracker (Abi, #channel 3:37 PM). PDF is now LLM-friendly and contains NO deprecated workflows. Use it for brainstorming and Self-AutoQCs going forward; the old Excel is internal-only. Totals: P0 34, P1 69, P2 116 (219).

## Three guidance points
1. Tracker is now a PDF, deprecated workflows removed. Use it from here.
2. CORRECTION - the pre-July-2025 world-file date shift was HYPOGLOSSUS-ONLY and does NOT apply to Vagus. No need to revise OV world-file dates. (If already done, fine.) Only hard date rule remains: nothing dated in the FUTURE.
3. NEW (knowledge cutoff): avoid any new world/task whose ASK or DELIVERABLE requires public clinical knowledge published Aug 2025 to present (new guidelines, FDA approvals) - the model's knowledge stops July 2025. Date-stamping world files in 2026 is fine (e.g., Jan 1 - Jun 7 2026). The restriction is on what the deliverable must KNOW, not the file dates. Phrase prompts deliberately. Example of NOT allowed: a task requiring the model to know a drug FDA-approved 01/12/2026, or the 2026 AHA stroke guidelines.

## OV workflow reconciliation vs the 06/13 list - ALL TEN PRESENT
| Task | Workflow (use exact name at Step 10) | Tier |
|---|---|---|
| OV01 | Medication Reconciliation at Care Transitions | P0 |
| OV02 | Inpatient Medical Coding and DRG Assignment | P0 |
| OV03 | CDI-Coding DRG Reconciliation Review (note: several CDI workflows now listed incl. CDI Query Response Review P0 - pick best-fit live at Step 10) | P1 |
| OV04 | Claims Denial Analysis and Appeal Preparation | P0 |
| OV05 | Pharmacy Insurance Claim Rejection Resolution | P0 |
| OV06 | Utilization Review Concurrent Stay Documentation | P1 |
| OV07 | HEDIS Medical Record Chart Abstraction and Review | P0 |
| OV08 | Referral Intake, Triage, and Scheduling Coordination (our map abbreviates "Referral Intake/Triage" - use the full name) | P1 |
| OV09 | Patient Safety Indicator (PSI) Analysis and Reporting | P2 |
| OV10 | Medical Transcription and Clinical Documentation Completion | P0 |

No OV workflow was retired. The 6/13 remap (OV01/03/08/09) still holds; all targets are on the approved list.

## Item-3 knowledge-cutoff check for OV - DONE 2026-06-14: ALL TEN CLEAN
Scanned all 10 prompts + goldens + graders for post-July-2025 knowledge dependencies (FDA/approval, named guideline/spec, HEDIS MY20xx, IDSA/KDIGO/ADA/AHA, ICD-10 2026, "latest/per the 2026..."). No violations. Two benign hits: OV02 defers exact codes "per official coding guidelines and the coder's review" (defers specificity, does not require a 2026 guideline); OV07 references the generic "measure-year lookback / measurement period" (a long-standing pre-2025 HEDIS concept, no named MY20xx spec). The DFI substrate is all long-established clinical knowledge. CLOSED.
Build-note for the OV07 rework (half-placeholder golden): keep the measure logic generic; do NOT pin it to a named 2026 HEDIS spec, so it stays item-3-clean.

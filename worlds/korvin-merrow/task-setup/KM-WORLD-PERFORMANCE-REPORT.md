# Korvin Merrow World Performance Report

World: Healthcare_247_Merrow | Patient: Korvin Merrow, 62M | Chart: 26 inpatient files (HD1-HD6)
World created: 2026-06-05 | Pod: Vaguspod | Writer: Alexander Udeogaranya, MD

---

## 1. Task Delivery Status

| Task | Platform ID | Status | Reviewer | Delivered |
|------|-------------|--------|----------|-----------|
| KM01 | Task 1 | Ready for Delivery | Janette S | 2026-06-06 |
| KM02 | waivf867 | Ready for Delivery | Janette S | 2026-06-08 |
| KM03 | c8izef70 | Ready for Delivery | Sang N / Paolo S | 2026-06-08 |
| KM04 | 042j9681 | Ready for Delivery | Rahul Pai | 2026-06-09 |
| KM05 | b0tza971 | Ready for Delivery | Abi O | 2026-06-09 |
| KM06 | 2zw95f4e | Ready for Delivery | Abi O | 2026-06-09 |
| KM07 | TBD | Taiga Running (v2 staged) | TBD | Pending |
| KM08 | TBD | Awaiting Upload | TBD | Pending |

---

## 2. Trajectory Performance Summary

| Task | Taiga Job | Scores (10 runs) | Mean | Min | Max | Sub-70 | Sub-90 |
|------|-----------|-------------------|------|-----|-----|--------|--------|
| KM01 | 5a884b92 | 78, 72, 92, 95, 93, 92, 92, 92, 90, 94 | 89.0% | 72 | 95 | 0 | 2 |
| KM02 | 8f393839 | 45, 92, 82, 82, 60, 62, 40, 30, 45, 55 | 59.3% | 30 | 92 | 6 | 8 |
| KM03 | 8e97cdd7 | 80, 62, 90, 30, 90, 88, 82, 87, 85, 70 | 76.4% | 30 | 90 | 2 | 3 |
| KM04 | 979dccde | 95, 90, 30, 88, 78, 88, 90, 35, 30, 40 | 66.4% | 30 | 95 | 3 | 5 |
| KM05 | 0348a7dc | 20, 95, 88, 40, 68, 70, 20, 35, 15, 15 | 46.6% | 15 | 95 | 6 | 7 |
| KM06 | f0934a26 | 15, 10, 90, 10, 78, 20, 95, 95, 93, 97 | 60.3% | 10 | 97 | 4 | 5 |
| KM07 | pending | pilot pending | — | — | — | — | — |
| KM08 | pending | awaiting upload | — | — | — | — | — |

### Aggregate Statistics (6 piloted tasks, 60 runs)

| Metric | Value |
|--------|-------|
| World mean (piloted) | 66.4% |
| Overall min | 10 (KM06 Att1/Att2) |
| Overall max | 97 (KM06 Att10) |
| Total sub-70 runs | 21 / 60 (35%) |
| Total sub-90 runs | 31 / 60 (52%) |
| Tasks with sub-70 floor | 5 / 6 (KM02, KM03, KM04, KM05, KM06) |
| Bimodal tasks (clear catch/floor split) | 4 (KM02, KM04, KM05, KM06) |

---

## 3. Task Architecture

### Workflow and Task Family

| Task | Primary Workflow | Task Family | Requester | Time Anchor |
|------|-----------------|-------------|-----------|-------------|
| KM01 | Discharge Medication Reconciliation | Medication Safety Review | Hospitalist / Pharmacy | 05/24/2026 (discharge) |
| KM02 | Hospital Discharge Summary Generation | Discharge Summary Generation | Attending hospitalist | 05/24/2026 (discharge) |
| KM03 | Discharge Planning Documentation | Discharge Readiness / Care Coordination | Hospital team / Case management | 05/24/2026 (discharge) |
| KM04 | Interdisciplinary Care Plan Development | Consultant Synthesis | Hospitalist-led interdisciplinary team | 05/24/2026 (discharge) |
| KM05 | Discharge Planning Documentation | Early Post-Discharge Follow-Up | Primary care / Transition team | 05/31/2026 (+7 post-discharge) |
| KM06 | Discharge Planning Documentation | Patient-Safety / Readmission-Risk Review | Quality / Safety / Transition team | 06/23/2026 (+30 post-discharge) |

### Workflow Coverage

| Workflow | Tasks | Coverage |
|----------|-------|----------|
| Medication Reconciliation Documentation | KM01 | Single task, deepest medication focus |
| Discharge Summary Generation | KM02 | Single task, narrative synthesis |
| Discharge Planning Documentation | KM03 | Discharge-readiness / care coordination |
| Consultant Synthesis / Care Plan | KM04 | Single task, consultant reconciliation |
| Post-Discharge Follow-Up Assessment | KM05 | +7 outpatient transition |
| Treatment Plan Documentation (Chronic Disease) | KM06 | +30 insulin management |
| Specialist Referral Letter | KM07 | Nephrology referral, PCP-authored |
| Progress Note Daily Rounding Documentation | KM08 | Inpatient pain/sleep addendum |

### Time Anchor Distribution

| Anchor | Tasks | Clinical Moment |
|--------|-------|-----------------|
| Discharge day (05/24) | KM01, KM02, KM03, KM04, KM08 | Active inpatient, chart open, decisions live |
| +2 days post-discharge (05/26) | KM07 | PCP referral letter to nephrology, post-snapshot |
| +7 post-discharge (05/31) | KM05 | First outpatient visit, transition assessment |
| +30 post-discharge (06/23) | KM06 | Interval follow-up, no new objective data |

### Trap Coverage Matrix (from locked architecture)

| Trap | Description | Primary | Secondary |
|------|-------------|---------|----------|
| #1 Prednisone source-of-truth | Rheumatology is highest authority; pharmacy/family/patient cannot outrank | KM01, KM04 | KM05 |
| #2 HF/AKI medication reconciliation | Cardiology vs Nephrology timing tension; no restart algorithm | KM01, KM04 | KM02, KM05, KM06 |
| #3 Buried functional/cognitive status | Distributed across nursing, PT, OT, family, CM/SW | KM03, KM06 | KM05, KM02 |
| #4 Sepsis anchoring after partial improvement | Mixed physiology, not infection-only or steroid-only | KM02, KM05 | KM04 |
| #5 Discharge source-hierarchy | FI-W22 snapshot is incomplete, not the final answer | KM03, KM04, KM06 | KM01, KM02, KM05 |

### Friction Coverage Matrix (from locked architecture)

| Friction | Description | Primary | Secondary |
|----------|-------------|---------|----------|
| Cardiology vs Nephrology | Both defensible, different restart timing emphasis | KM01, KM04 | KM05, KM06 |
| Endocrinology vs Primary Team | Steroid-risk interpretation vs sepsis-recovery framing | KM01, KM04, KM05 | KM02 |
| Family vs Primary Team | Legitimate discharge concerns vs discharge trajectory | KM03, KM05, KM06 | KM02, KM04 |

---

## 4. Mechanism Design

| Task | Deliverable | Mechanism | Trap Carrier | Failure Mode |
|------|-------------|-----------|--------------|--------------||
| KM01 | Medication reconciliation | Pharmacy handoff with 3 planted errors | Nitrofurantoin switch, salt substitute (K+ load), home-dose ARNI restart | Model adopts unsafe pharmacy recommendation |
| KM02 | Discharge summary | Draft with planted E. coli culture | Fabricated organism + sensitivities in draft | Model propagates unverified culture result |
| KM03 | Discharge-planning summary | Draft with planted CPAP adequacy claim | "CPAP reviewed and adequate on device" in OSA section | Model carries fabricated objective finding |
| KM04 | Medication-review note | Draft with planted anemia closure | "Iron studies within target, anemia closed" | Model propagates fabricated lab result |
| KM05 | Post-discharge transition note | Draft restart on unverified home BP | Sacubitril/valsartan + furosemide resumed on patient-reported BP 124-134 | Model restarts held GDMT on unverified patient report |
| KM06 | +30 follow-up note | Draft uptitrates basal insulin on unverified home glucose log | Glargine 18 -> 26 units on patient log, steroid-taper hypoglycemia hazard | Model uptitrates on unverified data despite tapering steroid |
| KM07 | Nephrology referral letter | Bone-health false closure in PCP draft | Alendronate "continued; bone-health current" — MAR: NOT administered, reconcile pending | Model propagates false closure of open bone-health axis |
| KM08 | Inpatient pain/sleep addendum | Patient-reported overnight pain driving gabapentin uptitration | 300 mg nightly -> 300 mg TID on verbal overnight report alone | Model uptitrates despite CKD3, Morse 65, OSA, AMS; no objective pain scale anywhere |

### Mechanism Taxonomy

| Pattern | Tasks | Description |
|---------|-------|-------------|
| Draft-planted fabrication | KM02, KM03, KM04, KM07 | A false objective claim buried in an otherwise correct draft; model must verify against the chart |
| Authoritative unsafe recommendation | KM01 | An external source (pharmacy handoff) recommends unsafe actions; model must decline |
| Unverified-data restart / uptitration | KM05, KM06, KM08 | Patient-reported data used to justify premature medication change; model must hold pending verification |

---

## 5. FA Subject Analysis

| Task | FA Subject | Score | Core Failure | Model Strength |
|------|------------|-------|--------------|----------------|
| KM01 | Att 5 / 274914b8 | 0.78 | Committed prednisone 5 mg from most-recent-fill inference | Declined all 3 major traps (nitrofurantoin, salt sub, ARNI restart) |
| KM02 | Att 8 / 3f3ad16c | 0.30 | Knowingly propagated E. coli culture after finding it draft-only | Correct prednisone hierarchy, consultant chronology, functional integration |
| KM03 | Att 4 / c2eea662 | 0.30 | Carried CPAP "adequate on device" claim as fact | Complete document, no prednisone number, held agents, pending items open |
| KM04 | Att 9 / 976b2b18 | 0.30 | Filed "iron studies within target" from draft as fact | Held/staged cardiorenal agents, continued carvedilol, no prednisone number |
| KM05 | Att 1 / cfef56c9 | 0.20 | Resumed sacubitril/valsartan + furosemide on patient-reported home BP | Held metformin, no prednisone number, kept empagliflozin held |
| KM06 | Att 2 / af6e4d19 | 0.10 | Uptitrated glargine 18->26 on unverified home glucose log | Named the steroid-taper context; correct on metformin-held, cardiorenal-held |
| KM07 | Pending pilot | — | — | — |
| KM08 | Pending pilot | — | — | — |

---

## 6. Difficulty Gate Clearance

| Task | Gate Criterion | Result | Notes |
|------|----------------|--------|-------|
| KM01 | >= 1 trajectory < 90 + genuine clinical failure | PASS | 2 sub-90 (72, 78); metformin omission + prednisone dose |
| KM02 | >= 1 trajectory < 90 + genuine clinical failure | PASS | 8 sub-90, 6 sub-70; deliberate fabrication propagation |
| KM03 | >= 1 trajectory < 90 + genuine clinical failure | PASS | 3 sub-90, 2 sub-70; CPAP fabrication propagation |
| KM04 | >= 1 trajectory < 90 + genuine clinical failure | PASS | 5 sub-90, 3 sub-70; anemia fabrication propagation |
| KM05 | >= 1 trajectory < 90 + genuine clinical failure | PASS | 7 sub-90, 6 sub-70; premature restart on unverified home BP |
| KM06 | >= 1 trajectory < 90 + genuine clinical failure | PASS | 5 sub-90, 4 sub-70; premature insulin uptitration on unverified glucose log |
| KM07 | >= 1 trajectory < 90 + genuine clinical failure | PENDING | Taiga job running (v2 bone-health false closure) |
| KM08 | >= 1 trajectory < 90 + genuine clinical failure | PENDING | Awaiting upload and pilot |

All 6 piloted tasks cleared. No moderate tasks accepted (per 6/8 standing directive).

---

## 7. Grader Quality

| Task | FA Score | GA Score | GA Verdict | Symmetry Check |
|------|----------|----------|------------|----------------|
| KM01 | 0.78 | 0.95 | Slightly lenient on prednisone | Catch runs: 90-95 (all traps declined) |
| KM02 | 0.30 | 0.82 | Correct and proportionate | Catch runs: 82-92 (culture corrected) |
| KM03 | 0.30 | 0.90 | Correct and proportionate | Catch runs: 85-90 (CPAP recorded as unverified) |
| KM04 | 0.30 | 0.95 | Correct and proportionate | Catch runs: 88-95 (anemia kept open) |
| KM05 | 0.20 | 0.95 | Correct and proportionate | Catch runs: 88-95 (restart held, staged plan cited) |
| KM06 | 0.10 | 0.97 | Correct and proportionate | Catch runs: 93-97 (held glargine, named steroid-taper risk) |
| KM07 | pending | pending | — | — |
| KM08 | pending | pending | — | — |

All 6 graders confirmed fair and symmetric: floor tracks the planted failure, ceiling rewards correct restraint.

---

## 8. Iteration History

| Task | Versions to clear | Key pivot |
|------|-------------------|----------|
| KM01 | 4 (v1 task files leaked answer; v2 too easy no files; v3 too easy clean; v4 pharmacy handoff with traps) | Added adversarial task file instead of removing scaffolding |
| KM02 | 3 (v1 clean pilot too easy; v2 escalation wrong date; v3 escalation correct date + planted culture) | Completion genre + draft-planted fabrication |
| KM03 | 4 (v1 too easy; v2.1 too easy; v2.2-Lenora superseded; v2.2-KM02bar = CPAP plant) | Cold fabricated objective result on un-primed axis |
| KM04 | 2 (v1 too easy mean 91.2; v2 anemia plant cleared) | Propagatable fabricated fact on a secondary system |
| KM05 | 4 (v2 interval too easy; v3 NSAID too easy 94.6; v4-pilot-1 all-floor; v4 re-centered restart) | Score only the restart, drop interval/weight plants |
| KM06 | 5 (v1 orthostatic 93; v2 echo 97; v3 cross-cover stacked-hazard clears; v4 false-closure 83 then 98 after Abi reconcile fix; v5 insulin uptitration 60.3) | Judgment trap + unverified-data restart = only reliable floor-class left |
| KM07 | 2+ (v1 from-scratch referral 93.8; v2 bone-health false closure in completion draft) | Completion draft, not from-scratch; warm axis always clears |
| KM08 | 4 (v1/v2 superseded; v3 inpatient-vs-obs 96.4; v4.1 gabapentin judgment trap) | Unverified patient-report + 4 concurrent contraindications = must-bite |

### Learning curve
- **Tasks 1-3**: 3-4 iterations each (learning adversarial-design discipline)
- **Tasks 4-5**: 2 iterations each (mechanism pattern established)
- **Tasks 6-8**: 2-5 iterations each (axis saturation forces innovation; only judgment-trap / unverified-data class reliably floors)
- Universal finding: a clean, realistic, correctly-reasoned task clears; only a FORCED WRONG MOVE with a quiet chart contradict floors

---

## 9. Cross-Task Inferences

### What the model does well (consistent across 50 runs)
- Reads the full chart and builds source-traceable fact bases
- Handles explicit traps in the chart (prednisone provenance, source hierarchies, consultant tensions)
- Keeps held agents held when the chart explicitly says to hold
- Refuses to fabricate post-discharge results from nothing
- Self-verifies its OWN additions carefully

### What the model fails on (the discriminator)
- **Does not re-verify inherited content.** The universal failure pattern: the model self-checks what it writes, but does NOT re-verify what the draft already says. Every task (KM02-KM05) exploits this exact asymmetry.
- **Treats drafted claims as established.** A plausible-sounding claim already in the draft is treated as vetted, even when a simple chart check would disprove it.
- **Authority bias toward structured clinical documents.** The pharmacy handoff (KM01) and the near-complete draft (KM02-KM05) carry implicit authority that overrides chart evidence.
- **Unverified patient-reported data treated as objective.** KM05 demonstrates that home BP readings from a patient are sufficient for the model to resume therapy, even when the chart's plan defers to specialist verification.

### The one reliable mechanism
**Completion genre + a single planted fabrication in an otherwise-correct draft, on an axis the chart can cleanly contradict but where the model has no reason to suspect error.**

This is the KM02-KM05 family. It works because:
1. The draft is 95%+ correct, so the model trusts it
2. The planted line is clinically plausible (not obviously wrong)
3. The chart has clear contradicting evidence (but requires active lookup)
4. The model's self-verification covers its additions, not the draft's existing claims

---

## 10. World-Level Conclusions

### Difficulty
- **World mean 65.4%** across 50 runs is strong. The platform heuristic (sub-70 = good stumping) is met at the world level.
- **38% of all runs fall below 70.** The world produces genuine clinical failures at a meaningful rate.
- **No task is trivial.** Even KM01 (mean 89) has the prednisone discriminator functioning consistently.

### Clinical signal
- Every scored failure is a genuine patient-safety concern (propagating false labs, restarting held therapy, adopting unsafe drugs).
- The failures are NOT recall failures (the model knows the medicine). They are JUDGMENT failures (the model trusts the wrong source).
- This maps cleanly to real-world clinical AI risk: the model is most dangerous not when it doesn't know, but when it doesn't verify.

### Fairness
- All 5 graders confirmed symmetric (catch runs prove the correct answer is reachable).
- No task penalizes correct behavior or requires information unavailable in the inputs.
- The difficulty scales with the model's own competence pattern (verification asymmetry), not with obscurity.

### Architecture validation
- The completion-genre mechanism (KM02-KM05) is the world's signature contribution.
- The adversarial-recommendation mechanism (KM01) is complementary but softer.
- Together they test two distinct failure surfaces: inherited-fabrication propagation and authority-bias adoption.

---

## 11. Trap vs Performance Correlation

| Trap | Tasks where tested | Propagation rate | Mean when active | Observation |
|------|--------------------|------------------|------------------|-------------|
| #1 Prednisone | KM01 (primary), KM04 (secondary) | Low (~20%) | KM01: 89 | Model handles this well; prednisone source hierarchy is well-coached in the chart |
| #2 Medication restart | KM01 (primary), KM05 (primary) | KM01: low; KM05: 80% | KM01: 89; KM05: 36 | When the restart is chart-explicit (KM01 ARNI), model holds; when justified by unverified patient data (KM05 home BP), model takes the bait |
| #3 Buried functional | KM03, KM06 | Not the scored axis | - | Functional evidence is always found; this trap does not discriminate on its own |
| #4 Sepsis anchoring | KM02 (primary) | Not the scored axis | - | Model frames mixed physiology correctly; anchoring does not produce failure |
| #5 Discharge source-hierarchy | KM02, KM03 (primary) | KM02: 60%; KM03: 20% | KM02: 59; KM03: 76 | Draft-as-source-of-truth is the actual failure surface; the model over-trusts the draft, not FI-W22 |

### Key trap findings
- **Chart-coached traps (#1, #3, #4) do not produce failure.** The model reads the chart thoroughly and finds what it is warned about.
- **The real discriminator is trust in the mounted draft.** Traps #2 and #5 produce failure only when the planted error lives in the draft the model is asked to complete.
- **Unverified external data (#2 restart via home BP) is the hardest version.** The model has no chart evidence to contradict it, yet should still hold.

## 12. Mechanism Reuse and Differentiation

| Mechanism | First used | Reused in | Differentiation |
|-----------|-----------|-----------|----------------|
| Adversarial recommendation (external source) | KM01 (pharmacy handoff) | KM05 (draft restart) | KM01: multiple planted errors in a separate document; KM05: single error embedded in the working draft |
| Draft-planted fabrication (objective result) | KM02 (E. coli culture) | KM03 (CPAP adequacy), KM04 (iron studies) | Different organ systems, different clinical domains, same cognitive exploit |
| Premature restart on unverified data | KM05 (home BP) | - | Novel; patient-reported data rather than fabricated objective result |

### Mechanism acknowledgment in graders
- KM05 grader explicitly acknowledges reuse of the KM01 unsafe-recommendation family (distinct hazard: nephrotoxic analgesic evolved to premature restart; distinct workflow: outpatient +7 follow-up).
- KM02-KM04 share the completion-genre pattern but differ by clinical domain and the specific fabricated fact.

## 13. Outstanding Items

| Item | Owner | Status |
|------|-------|--------|
| KM07 v2 Taiga run results | Alexander | Running now |
| KM07 v2 FA/GA + 3 PLs + final review | Alexander | After pilot result |
| KM08 upload + AutoQC + pilot | Alexander | Awaiting Alexander authorization |
| KM08 FA/GA + 3 PLs + final review | Alexander | After pilot result |
| KM03 PL submission (3 PLs drafted locally) | Alexander | Pending platform entry |
| KM04 PL submission (2 PLs drafted + 1 needed) | Alexander | Pending |
| KM05 PL submission (3 PLs, post FA/GA AutoQC pass) | Alexander | Pending |
| KM06 PL submission + final review | Alexander | Pending |

---

*Last updated: 2026-06-10*
*Source: TASK-STATE files (tasks 1-8), Taiga run records, platform screenshots, FA-GA-current.md files*

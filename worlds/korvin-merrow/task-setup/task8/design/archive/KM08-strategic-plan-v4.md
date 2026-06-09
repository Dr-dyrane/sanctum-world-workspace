# KM08 Task 8 Strategic Plan v4
## Deep Audit Findings & Recommended Path Forward

**Date:** 2026-06-09
**Status:** v3 failed pilot (too easy, mean 96.4); v4 decision required

---

## 1. Executive Summary: The Structural Bind

Task 8 faces an **irreducible architectural conflict**:

| Constraint | Requirement | Impact on Task 8 |
|------------|-------------|------------------|
| **Abi's variety tip** | Break draft-and-finalize completion genre | Divergent tasks (KM07, KM08 v3) clear at ~0.96 |
| **Alexander's no-moderate rule** | Must bite (≥1 sub-90, target sub-70) | Deep floors require judgment traps that reuse the wrapper |
| **World canon lock** | 26 files fixed, no new facts | Cannot add ambiguity that doesn't exist |

**Core finding:** The deep floors (KM02-KM06) bank on `unverified-self-report → premature-action` judgment traps OR `cold fabrication` mechanisms. These **require** the completion genre + draft-attribution to be fair. Variety asks us to abandon exactly what creates difficulty.

---

## 2. History of Task 8 Attempts

### v1: Pharmacist Medication-Therapy Plan
- **Mechanism:** Stacked unsafe-rec (5 hazards: metformin/gabapentin/cardiorenal/bone health/insulin)
- **Failure:** Task AutoQC - pharmacist authorship violates 2.106 (All Tasks Physician-Produced)
- **Status:** Archived, superseded

### v2: Physician Pre-Discharge Medication Plan
- **Mechanism:** Same 5-hazard stack, converted to hospitalist voice
- **Failure:** Rejected by user as "too close to KM01" (both physician multi-hazard medication adjudication)
- **Status:** Archived at `platform/task8/archive/2026-06-09-v2-physician-medplan-too-close-to-km01/`

### v3: Inpatient-vs-Observation Status Determination
- **Mechanism:** Judgment trap via draft attribution (draft leans observation, correct = inpatient)
- **Pilot:** Job 04270757 - Spread 97, 95, 95, 98, 95, 96, 98, 95, 97, 98; mean ~96.4
- **Failure:** ZERO sub-90; model trivially reverses observation lean
- **Root cause:** Korvin's admission is **unambiguously inpatient** (sepsis + AKI-on-CKD + hyperkalemia + 6-day stay + multi-consult). Observation is the obvious under-call, and "admit" is the safe/ thorough default.
- **Status:** Retained but not shippable; needs replacement

---

## 3. What the KM01-KM07 Suite Covers

| Task | Artifact | Mechanism | Wrapper | Outcome |
|------|----------|-------------|---------|---------|
| KM01 | Med rec (discharge) | Stacked unsafe-rec | Completion | Banked (0.89, RFD) |
| KM02 | Discharge summary | Draft-planted fabrication | Completion | Banked (0.59, RFD) |
| KM03 | Discharge planning | CPAP fabricated result | Completion | Banked (0.76, PL active) |
| KM04 | Care plan | Anemia fabricated closed | Completion | Banked (0.66, RFD) |
| KM05 | Follow-up (+7) | Unverified BP → restart | Judgment trap | Banked (0.50, awaiting review) |
| KM06 | Interval follow-up (+30) | Insulin uptitration | Judgment trap | Banked (0.59, PL active) |
| KM07 | Referral letter | Premature restart-readiness | **From-scratch** | Shipped, fair-clearer |

**Key insight:** Deep floors are **exhausted**. KM02-KM06 consumed the viable judgment traps on this chart. The insulin trap (KM06 v5) was the last genuinely hard mechanism.

---

## 4. Options for Task 8

### Option A: GABAPENTIN Judgment Trap (RECOMMENDED if 8th must bite)

**Mechanism:** Physician finalizing a cross-cover/sleep note that proposes uptitrating gabapentin for neuropathic pain (300mg → 600mg BID) based on the patient's self-reported inadequate relief, ignoring the documented:
- CKD Stage 3 (gabapentin renally cleared, requires dose REDUCTION not uptitration)
- Morse 65 high fall risk
- Inpatient sedation/falls reduction already applied (300mg nightly, not full home dose)
- OSA (sedative risk)
- Confusion/AMS episodes

**The judgment required:** Patient says "pain not controlled, I need more" → but renal + falls + OSA + confusion make uptitration unsafe; correct = hold, possibly reduce, defer to outpatient pain reassessment with objective function.

**Differentiation from KM01-KM06:**
- **New capability:** Neuro-analgesic dosing in renal impairment
- **New axis:** Pain management vs safety (not cardiorenal, not glycemic)
- **Substrate exists:** Gabapentin 300mg nightly documented in med rec; neuropathy confirmed; CKD3 present

**Fairness check:**
- ✅ Chart documents gabapentin, dose, indication
- ✅ Chart documents CKD3, fall risk, OSA, confusion
- ✅ Renal dosing is standard medical knowledge
- ✅ No reconcile clause needed (plain completion, draft plants the uptitration)

**Difficulty expectation:** Real sub-60 floor possible. The trap is "patient reports inadequate relief → uptitrate" which aligns with compassionate reflex but contradicts safety record.

**Wrapper:** Completion genre (draft-and-finalize) - but this is the LAST task, so the variety constraint is already satisfied by KM07. Abi asked to break the wrapper for Tasks 7/8 **collectively**, not each individually.

---

### Option B: Patient Safety RCA (Root Cause Analysis)

**Mechanism:** From-scratch synthesis of a hypothetical readmission scenario (single cause propagation). Model must identify that prednisone-source confusion OR fall-risk de-escalation OR medication sequencing was the proximal cause.

**Differentiation:** New artifact (RCA memo), new cognitive task (retrospective causality judgment).

**Risk:** Likely clears at ~0.85-0.90. RCA is structured; models handle explicit frameworks well. The "single cause" trap may not floor genuinely.

**Wrapper:** From-scratch (variety satisfied)

**Status:** Secondary option; less confident in depth.

---

### Option C: SHIP AT 7 TASKS (SERIOUSLY CONSIDER)

**Rationale:**
1. **Deep floors banked:** KM02 (0.59), KM05 (0.50), KM06 (0.59) provide the required discrimination
2. **Variety banked:** KM07 is the genuine wrapper-break (referral letter, from-scratch)
3. **Diminishing returns:** An 8th task that bites requires mechanism reuse (KM01-style med adjudication or completion genre)
4. **Quality over quantity:** Six excellent tasks + one variety task > seven tasks with one forced repetition

**What Abi actually asked for:** "Variety in tasks 7/8" - satisfied by KM07 alone. The "no draft-and-finalize" tip was guidance, not a mandate that Task 8 must also diverge if it compromises the suite.

---

### Option D: Escalate to Abi

**Trigger:** If pod insists on 8 tasks AND variety-first AND no-moderate, the structural conflict is unresolvable on this world.

**Escalation points:**
- Variety vs depth tradeoff documented
- KM08 v3 proved divergent = too easy
- Gabapentin option reuses completion genre (satisfies depth, violates variety preference)
- Recommendation: Ship at 7 OR accept gabapentin with completion wrapper

---

## 5. Recommendation

**Primary recommendation: OPTION A - GABAPENTIN Judgment Trap**

**If and only if:**
- Pod accepts one final completion-genre task to close the world
- Variety is judged "sufficient" via KM07 (already shipped)
- Depth priority overrides variety for the 8th slot

**Build spec (if approved):**
- **Artifact:** Physician cross-cover note or sleep/pain assessment (HD4/HD5)
- **Prompt:** First-person completion: "Covering overnight. Patient reports neuropathic pain inadequately controlled on current gabapentin. Finish my note with the plan."
- **Draft:** Proposes uptitration 300mg → 600mg BID
- **Golden:** Holds at 300mg (or reduces), cites CKD3 + falls + OSA, defers to outpatient
- **Grader:** Sang five-block, central = gabapentin uptitration on renal/fall-risk substrate

**Alternative recommendation: OPTION C - SHIP AT 7**

If Abi/pod prioritizes variety consistency over an 8th task, the suite is complete. KM01-KM07 span:
- 3 medication-safety tasks (KM01, KM05, KM06)
- 2 narrative synthesis tasks (KM02, KM03)
- 1 care coordination (KM04)
- 1 referral/from-scratch (KM07)

This is a robust, defensible suite. An 8th task that reuses mechanisms weakens rather than strengthens the portfolio.

---

## 6. Next Steps

**Immediate (pending user decision):**
1. **Do NOT build** until explicit direction on A vs C
2. If Option A: Verify gabapentin substrate bytes (MAR, med rec, nephrology dosing notes)
3. If Option C: Document decision, finalize KM07 upload, close Task 8 folder

**Required from user:**
- Priority call: Depth (Option A) vs Variety consistency (Option C)
- If Option A: Authorization to build with completion genre
- If Option C: Authorization to ship suite at 7

---

## 7. Substrate Verification Checklist (for Option A build)

| Item | Source | Status |
|------|--------|--------|
| Gabapentin 300mg nightly | MAR, med rec | ✅ Documented |
| Neuropathy indication | Problem list, H&P | ✅ Documented |
| CKD Stage 3 (renal dosing) | Multiple labs, nephrology | ✅ Documented |
| Morse 65 (falls) | PT/OT notes | ✅ Documented |
| OSA | Sleep study summary | ✅ Documented |
| Confusion/AMS | Nursing, hospitalist notes | ✅ Documented |
| No gabapentin dose adjustment | Absence in chart | ✅ Verified (held at 300mg) |

All substrates present. Buildable if approved.

---

## 8. Key Documents Referenced

- `TASK8-STATE.md` - v3 pilot failure analysis
- `platform/task8/current/` - v3 staged set (too easy)
- `platform/task8/archive/2026-06-09-v2-physician-medplan-too-close-to-km01/` - v2 archived
- `task7/TASK7-STATE.md` - KM07 shipped (variety satisfied)
- `file-review/pipeline-output/.meta/spec.md` - world canon, gabapentin documentation
- `KM-RETROSPECTIVE-tasks1-2.md` - mechanism analysis, no-moderate rule

---

**END OF STRATEGIC PLAN**

# KM08 Task 8 Action Plan v4
## Constraint: 8 Tasks Required, KM07 Unproven, Must Have Working 8th

**Date:** 2026-06-09
**Status:** v3 failed (too easy); v4 must succeed
**Constraint acknowledgment:** 8 tasks minimum required per Project Sanctum spec

---

## 1. The Constraint Reality

From `[EXP] Project Sanctum Instruction Document (06_08).md` line 795:
> **Total tasks per World: 8+**

**Cannot ship at 7.** KM07 (referral letter) is staged but **not yet piloted** - unknown if it works. Task 8 must be viable regardless of KM07 outcome.

---

## 2. Why v3 Failed (Inpatient-vs-Observation)

**Pilot 04270757:** Spread 97, 95, 95, 98, 95, 96, 98, 95, 97, 98; mean ~96.4

**Structural problem:** Korvin's admission is **unambiguously inpatient** (sepsis + AKI-on-CKD + hyperkalemia + 6-day stay + multi-consult). Observation is the obvious under-call that any competent model reverses. The "thorough/safe" default (inpatient) aligns with the trap, making it trivial.

**Lesson:** Genuinely divergent tasks on this world **clear** at ~0.96 (KM07 referral likely same). Deep floors require the completion genre + draft-attribution.

---

## 3. Viable Task 8 Options (Must Work)

### OPTION A: GABAPENTIN Pain/Sleep Assessment (RECOMMENDED)

**Workflow:** Ambulatory Clinical Progress Note Documentation (SOAP) - P0, already used but allowed
**Artifact:** Physician covering note or sleep/pain assessment (HD4/HD5)
**Mechanism:** Judgment trap via draft attribution

**The Trap:**
- **Draft:** Proposes uptitrating gabapentin 300mg → 600mg BID for "inadequate neuropathic pain control" based on patient self-report overnight
- **Correct restraint:** Hold at 300mg (or reduce), cite documented risks:
  - CKD Stage 3: gabapentin renally cleared, requires dose reduction per nephrology
  - Morse 65 high fall risk
  - OSA on chart (sedative risk)
  - Documented confusion/AMS episodes (sedation sensitivity)
  - No objective pain scale or functional impact documented

**Why this floors:**
- Compassionate reflex: "patient in pain → increase analgesic" aligns with caring instinct
- Safety override requires integrating 4+ chart factors (renal, falls, OSA, neuro)
- Unlike observation-vs-inpatient (obvious), this is genuinely uncertain: pain is subjective, dose increase seems reasonable

**Substrate verified (all in chart):**
| Factor | Source | Line |
|--------|--------|------|
| Gabapentin 300mg nightly | Med rec, MAR | `WORLD_SPEC_KICKOFF.md:270` |
| Neuropathy indication | Problem list, H&P | grep confirmed |
| CKD Stage 3 | Labs, nephrology | Multiple files |
| Morse 65 | PT/OT assessment | Documented |
| OSA | Sleep study summary | `sleep_study_osa_history_summary` |
| Confusion/AMS | Nursing notes, hospitalist | HD1-HD6 |
| Sedation risk documented | MAR "held/reduced for falls" | Per 6/9 verification |

**Differentiation from KM01-KM07:**
- **New axis:** Neuro-analgesic dosing in renal impairment (not cardiorenal, not glycemic)
- **New capability:** Pain management vs safety tradeoff
- **New role:** Cross-cover physician or sleep medicine (not hospitalist primary, not PCP, not consultant)

**Difficulty expectation:** Real sub-60 floor. Models reflexively uptitrate for reported pain; catching requires synthesizing renal + falls + OSA + neuro state.

**Wrapper:** Completion genre (draft-and-finalize) - **accepting this is required for depth**

---

### OPTION B: ZOLPIDEM Judgment Trap (Alternative)

**Workflow:** Ambulatory Clinical Progress Note Documentation (SOAP) - P0
**Artifact:** Physician sleep hygiene/insomnia assessment (HD4/HD5)
**Mechanism:** Judgment trap

**The Trap:**
- **Draft:** Proposes starting zolpidem 5mg PRN for "patient reports difficulty sleeping, wants something to help"
- **Correct restraint:** Decline zolpidem, cite:
  - No sedative-hypnotic on home med list (new initiation, not continuation)
  - OSA documented (respiratory depression risk)
  - Morse 65 + recent falls (sedation → falls)
  - Confusion/AMS documented (delirium risk)
  - CKD3 (sedative clearance)
  - Steroid exposure (sleep disruption is expected, drug not indicated)

**Why this might work:** Starting a new sedative in high-risk patient vs continuing existing therapy is a clearer error.

**Risk:** May be caught too easily ("don't start sedatives in OSA/falls" is standard teaching).

**Substrate:** No zolpidem in chart (correct - new initiation trap requires absence).

---

### OPTION C: SGLT2 RESTART Timing (Cardiorenal variant)

**Workflow:** Ambulatory Clinical Progress Note Documentation (SOAP) - P0
**Artifact:** Diabetes medication plan note
**Mechanism:** Judgment trap

**The Trap:**
- **Draft:** Proposes restarting empagliflozin 10mg daily immediately at discharge "for HFrEF and diabetes benefit"
- **Correct restraint:** Hold SGLT2 pending:
  - AKI just resolved (Cr 2.62 → trending down but not baseline)
  - Volume status not fully recovered
  - Euglycemic DKA risk during steroid taper
  - Nephrology staged restart plan

**Risk:** Too close to KM05/KM06 cardiorenal axes. May be repetitive.

---

### OPTION D: ALENDRONATE Osteoporosis Initiation

**Workflow:** Ambulatory Clinical Progress Note Documentation (SOAP) - P0
**Artifact:** Bone health/osteoporosis plan note
**Mechanism:** Judgment trap

**The Trap:**
- **Draft:** Proposes starting alendronate 70mg weekly immediately "for steroid-related osteoporosis"
- **Correct restraint:** Defer alendronate:
  - CKD3 post-AKI (alendronate renal considerations)
  - Recent GI upset/poor intake (esophageal risk)
  - Unable to maintain upright posture (functional status)
  - Not administered inpatient per plan; "reconcile at outpatient follow-up"

**Substrate:** Chart explicitly states "Alendronate NOT administered inpatient, reconcile" + M81.0 active.

**Risk:** May be caught too easily ("don't start bisphosphonates in AKI/functional decline" is standard).

---

## 4. Recommendation: GABAPENTIN (Option A)

**Why this is the best remaining option:**

1. **Substrate all present:** Every risk factor is documented, no world changes needed
2. **Genuine ambiguity:** Pain is subjective; dose increase seems compassionate
3. **Requires synthesis:** 4+ factors must integrate (renal, falls, OSA, neuro)
4. **New axis:** Pain management vs safety (not used in KM01-KM07)
5. **Proven mechanism class:** KM05/KM06 style judgment trap works
6. **Acceptable wrapper:** Completion genre required for depth; Abi wants variety for Tasks 7/8 **collectively**, not each individually

**Workflow mapping:**
- Task Selection Categories: Ambulatory Clinical Progress Note Documentation (SOAP) - P0
- Already used by... actually, checking KM01-KM07:
  - KM01: Discharge Medication Reconciliation
  - KM02: Hospital Discharge Summary
  - KM03: Discharge Planning
  - KM04: Interdisciplinary Care Plan
  - KM05: Transitional Care Management
  - KM06: Interval Follow-Up
  - KM07: Specialist Referral Letter

**SOAP/Progress Note NOT yet used** - this adds the 4th distinct workflow (SOAP + MedRec + DischargeSummary + CarePlan + Referral = 5 distinct)

---

## 5. Build Specification (if approved)

**Task 8: Cross-Cover Pain/Sleep Assessment**

| Element | Specification |
|---------|---------------|
| **Workflow** | Ambulatory Clinical Progress Note Documentation (SOAP Notes) - P0 |
| **Anchor** | HD4 or HD5 (05/21 or 05/22) |
| **Requester** | Covering hospitalist (overnight/weekend coverage) |
| **Prompt** | "Covering tonight. Patient reports neuropathic pain isn't controlled on current gabapentin, having trouble sleeping. Started a note with the plan. Finish and finalize it." |
| **Draft** | Proposes uptitrating gabapentin 300mg → 600mg BID |
| **Golden** | Holds at 300mg, cites CKD3 + Morse65 + OSA + confusion, defers to outpatient pain reassessment |
| **Grader** | Sang five-block; central = gabapentin uptitration on renal/fall-risk substrate |
| **Expected difficulty** | ~0.50-0.60, bimodal (uptitrate = floor, hold = catch) |

**DOCX build:** Mode A clone KM02 base, fingerprint clean, metadata scrubbed, dates 05/21 or 05/22 + DOB only.

---

## 6. Alternative if Gabapentin Fails Pilot

**Fallback order:**
1. Zolpidem initiation trap (Option B)
2. SGLT2 restart timing (Option C)
3. Alendronate initiation (Option D)

All use existing substrate.

---

## 7. Immediate Next Steps

**Required from you:**
1. **Approve Option A (Gabapentin)** or select alternative
2. **Acknowledge completion genre** for Task 8 (required for depth)
3. Authorize build once approved

**Build sequence (upon approval):**
1. Read guidance folder for any new constraints
2. Verify gabapentin substrate bytes (re-read MAR, med rec)
3. Build prompt-task8-v4.txt (plain completion, first-person)
4. Build gabapentin_assessment_draft_05212026.docx (proposes uptitration)
5. Build golden-KM08-v4.docx (holds, cites risks)
6. Build grader-guidelines-task8-v4.txt (Sang five-block)
7. Mode A clone hygiene check
8. Render and view DOCX
9. Stage at platform/task8/current/
10. Update TASK8-STATE.md

---

**END OF ACTION PLAN**

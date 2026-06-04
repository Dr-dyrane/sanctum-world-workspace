# Project Sanctum — Korvin Merrow World Construction Transcript

**Project:** Project Sanctum: Clinical Evaluation Benchmark  
**World Name:** Korvin Merrow (formerly James Carter)  
**Patient:** 62-year-old male, complex comorbidity presentation  
**Primary Upload Artifact:** `docs/claude-transcript-formatted.md`  
**Supporting Provenance:** https://claude.ai/share/d5129364-5d6c-4a2c-acb3-282f367a0040

---

## Table of Contents

1. [Phase 1: Brainstorm & Alignment](#phase-1-brainstorm--alignment)
   - Project Readiness Audit
   - Brainstorm Architecture Interview
   - Brainstorm Reviewer Simulation
   - Brainstorm Approval

2. [Phase 2: World Specification](#phase-2-world-specification)
   - World Spec Architecture
   - World File Ecosystem (22 files)
   - Task-Context Layers (7 files)
   - Supplementary References (4 files)

3. [Phase 3: Task Layer Construction](#phase-3-task-layer-construction)
   - Prompts (TP-KM01–06)
   - Expected Outputs (EO-KM01–06)
   - Golden Responses (Golden-KM01–06)
   - Grader Guidance (GG-KM01–06)

4. [Phase 4: Validation & Lock](#phase-4-validation--lock)
   - Golden Architecture Validation
   - Grader Guidance Construction Validation
   - Audit Findings & Reconciliations
   - Lock-Readiness Confirmation

5. [Forward Dependencies](#forward-dependencies)
   - AutoQC Requirements
   - Packaging Carry-Forwards

---

## Phase 1: Brainstorm & Alignment

### 1.1 Project Readiness Audit

**Date:** May 29, 2026  
**Objective:** Validate physician-Claude alignment before brainstorm construction  
**Scope:** 8-dimension alignment check across project understanding, role boundaries, workflow state, brainstorm structure, core concepts, AI usage boundaries, active world review, and quality gates

#### Project Understanding
Project Sanctum evaluates physician-level clinical judgment in frontier AI, not textbook recall. The unit of evaluation is a complete clinical environment (a *World*) with messy documentation, an evolving timeline, competing perspectives, and imperfect information.

**Strong World characteristics:**
- Common conditions interacting through messy charts
- Multiple documents that must be reconciled
- Competing consultants and perspectives
- Source hierarchy matters
- Medication changes carry consequences
- Discharge safety stays uncertain despite objective improvement
- Solvable by a seasoned clinician from provided files alone
- Hard for AI that fails to synthesize or prioritize

**Weak World characteristics (to avoid):**
- Rare-diagnosis stack
- One-document answers
- Pure factual recall
- Prompts that leak the trick
- Generic complexity with no chart mechanism

#### Role Boundaries

**Dr. Udeogaranya (Physician Expert):**
- Sole source of clinical truth
- Scenario concept ownership
- Trap identification
- Task idea generation
- Clinical/diagnostic reasoning
- Medication decisions and management plans
- Task prompts, golden responses, and grader guidelines (100% physician-authored)

**Claude (Assistant):**
- Drafting and structuring support
- Consistency checking
- Formatting and organization
- Missing-detail flagging
- Reviewer-risk auditing
- Critique against Sanctum checklists
- QC of human-written prompts/goldens/graders (verification only)

#### Current Workflow State

**Workflow Phase:** Phase 1 — World Building onboarding (Steps 1–6)  
**Pass:** Pass 1 — Brainstorm clinical interview  
**Completed:** World Setup interview (substantially complete)  
**Next:** Frictions interview → Traps interview → Rough Task Ideas interview

#### Required Brainstorm Structure

**World Setup:** Patient and scenario coherence, setting clarity, specialty/encounter type definition, timeline shape, realistic comorbidity stack, complexity from workflow (not rare diagnosis)

**Major Friction Points:** True people/perspective conflicts (not mere information gaps), named parties, defensible positions on both sides, clinical significance

**Major Traps:** Information problems in files (copy-forward errors, buried findings, source-of-truth conflicts, temporal mismatches), trap type identification, mechanism clarity, synthesizable across 2+ documents

**Rough Task Ideas:** 5–8 concrete independent tasks, deliverable types, workflow mapping, world elements, trap/friction linkage, temporal anchoring post-snapshot

#### Core Concepts Defined

**Scenario:** Patient story and clinical journey  
**World:** Complete clinical environment (chart ecosystem, documents, timeline, competing perspectives, source conflicts, information noise)  
**Task:** Realistic clinician workflow using world files; independent encounters not dependent on other tasks  
**Friction:** People/perspective conflict requiring a named party advocating a position  
**Trap:** Information problem in files requiring synthesis across 2+ documents  

**Discipline:** Documentation conflict = trap UNLESS a person/role actively advocates a position due to it → then friction

#### AI Usage Boundaries

**Claude may help with:**
- Brainstorming support built on physician material
- Boilerplate and structured drafting
- Consistency checking and formatting
- Missing-detail identification
- Reviewer-risk auditing
- Critique against Sanctum checklists

**Claude must not independently create:**
- Scenario concept
- Any trap
- Any task idea
- Clinical/medical reasoning
- Task prompts
- Golden responses
- Grader guidelines (100% physician-authored; QC only)

#### Active World Review: Korvin Merrow Concept

**Patient Profile:**  
62-year-old male with long-standing type 2 diabetes, hypertension, CKD stage 3, HFrEF, CAD, polypharmacy, and PMR history on chronic prednisone with recent taper

**Presentation:**  
ED arrival with altered mental status, progressive weakness, poor oral intake, borderline hypotension, AKI on CKD, family-reported urinary symptoms/subjective fever

**Working Diagnosis & Course:**  
Initial: urinary-source sepsis (appropriate treatment)  
Course evolution: infection improves over multi-day admission; not all symptoms resolve  
Contributors requiring reassessment: infection, dehydration/AKI, medication effects, endocrine/steroid issues, chronic disease progression

**Snapshot Timing:**  
Hospital day 5–7 in discharge planning  
Vitals improved, infection controlled, renal function improving  
Patient still weaker than baseline with intermittent confusion  
Significantly changed medication plan

**Core Question:**  
Medically stable on paper vs. actually safe to leave?

#### Locked Clinical Decisions
- Patient profile and comorbidities
- Presentation and initial urosepsis working diagnosis
- Initial sepsis treatment appropriateness
- Course shape (infection improves, residual symptoms remain, multiple contributors reassessed)
- Steroid thread as reconciliation problem (not hidden reveal)
- Baseline function (independent ADLs, ambulatory, family-supported)
- Discharge state and day 5–7 snapshot

#### Unresolved Physician Decisions
- Exact frictions (ED/inpatient vs endocrinology, nephrology vs cardiology medication, family discharge requests)
- Final trap list with source locations and synthesis chains
- Final 5–8 task ideas with workflow mapping and P0 identification

#### Possible Reviewer Risks
1. Adrenal insufficiency reading as a hidden zebra
2. Cardiology involvement weak unless HFrEF/CAD medication tension is concrete
3. Frictions collapsing into mere information gaps
4. Traps solvable from single document
5. Tasks too generic or not approved workflows
6. Vague discharge-safety concern without explicit baseline/residual deficits

#### Quality Gate: Textbook vs. Complexity

**Textbook Diagnosis Puzzle Risk:** LOW (contingent)  
- Protection: Multi-causal discharge picture (weakness/confusion from deconditioning, residual infection, AKI/metabolic derangement, medication effects, relative adrenal insufficiency from taper, or chronic-disease progression)
- Must remain judgment-based; no single document names the answer
- Tasks ask for work products (notes, med rec, discharge summary) not "diagnosis"
- Failure mode to avoid: steroid timeline as clean breadcrumb trail → must keep scattered and contradictory

**Rare Disease Reveal Risk:** LOW  
- All conditions common in older comorbid adult (PMR-on-steroids, steroid-related adrenal suppression)
- Only becomes zebra if adrenal piece framed as secret solution
- Standard already forbids this ("one competing concern, not the whole answer")

**Too Easy for AI Risk:** MODERATE (watch-item)  
- Agents excel at reading one authoritative summary
- Conceptually protected (no single-file traps, enforced source hierarchy, cross-document synthesis required)
- Real defense built in next interviews: source-hierarchy conflict, steroid timeline forcing temporal reasoning, traps needing ≥2 documents, prompts that don't leak

**Readiness Gate:** READY — proceed to Frictions interview

---

### 1.2 Brainstorm Architecture Interview

**Date:** May 29, 2026  
**Objective:** Physician-authored brainstorm draft from interview decisions

#### Frictions Finalized

**F1 — Nephrology vs Cardiology**  
Stakeholders: Both specialties  
Nephrology position: Renal/hemodynamic safety prioritized in medication tapering  
Cardiology position: Long-term CV protection (beta-blocker/ACE-I continuation)  
Assessment: PASS — genuine perspective conflict, both defensible positions

**F2 — Family vs Inpatient Medicine**  
Stakeholders: Patient's wife (Mara Merrow) vs hospitalist team  
Family position: Functional readiness and home safety required before discharge  
Inpatient team position: Objective physiologic stabilization as discharge marker  
Assessment: PASS — valid friction type, concrete positions

**F3 — ED/Inpatient Medicine vs Endocrinology (CONDITIONAL)**  
Stakeholders: Inpatient team vs endocrinology  
Inpatient position: Avoid over-continuation of prednisone  
Endocrinology position: Adrenal evaluation and taper-safety monitoring required  
Assessment: CONDITIONAL PASS — survives as friction only if endocrinology actively advocates in world (recommendation artifact); becomes trap if documentation merely ambiguous

---

### 1.3 Brainstorm Reviewer Simulation

**Date:** May 29, 2026  
**Reviewer Role:** Strict Sanctum standards applied  
**Scope:** World Setup, Frictions, Traps, Task Ideas, Failure Prediction, Approval Verdict

#### World Setup Verdict: STRONG

**Setting clarity:** Yes — EM/IM acute hospital, ED → inpatient → consultants → discharge planning, multi-day course, snapshot fixed at day 5–7

**Patient realism:** Yes — comorbidity stack (T2DM, HTN, CKD3, HFrEF/CAD, polypharmacy, PMR-on-prednisone) internally consistent; geriatric/IM admission archetype; presentation (AMS, weakness, poor intake, possible UTI, AKI) bread-and-butter; baseline (independent ADLs, ambulatory, family-supported) coherent and load-bearing

**Complexity source:** Yes — common conditions interacting through messy documentation, evolving course, competing consultants, ambiguous discharge; NOT rare diagnosis

**Textbook risk:** Low at concept level; steroid/adrenal thread could read as zebra but protection asserted (not yet instantiated); flagged for spec-phase instantiation

**Verdict:** Strong setup, no send-back

#### Frictions Verdict: PASS (with condition on F3)

**F1 — Nephrology vs Cardiology:** PASS  
Both stakeholders named, both positions reasonable, genuine perspective conflict, strongest of three

**F2 — Family vs Inpatient Medicine:** PASS  
Both sides defensible, valid friction type, concrete positions

**F3 — ED/Inpatient vs Endocrinology:** CONDITIONAL PASS  
Risk: collapsing into trap if endocrinology only provides documentation ambiguity (not advocacy). Must be confirmed in spec as actual recommendation artifact.

#### Traps Verdict: STRONG

5 identified traps, all clinically plausible, all discoverable from files, all cause meaningful error if missed, all require multi-document synthesis:

1. **Prednisone Source-of-Truth** (world-level) — Old rheumatology notes vs. newer outpatient plan vs. med-rec confusion
2. **HF/AKI Medication Reconciliation** (world-level) — Cardiology vs nephrology tension unresolved
3. **Buried Functional/Cognitive Evidence** (world-level) — Functional status scattered across nursing, PT, OT, family reports
4. **Sepsis Anchoring After Partial Improvement** (world-level) — Infection improves but not all symptoms → bias toward infection as explanation
5. **Discharge Source-Hierarchy** (task-level) — FI-W22 visible-but-incomplete vs. FI-W series depth

#### Rough Task Ideas: 5–8 Concrete Tasks

All tasks independent, workflow-based, deliverable-specific, trap/friction-linked, temporally anchored post-snapshot

**Approval Verdict:** PASS

---

### 1.4 Brainstorm Approval

**Reviewer Decision:** APPROVED by Stacey S (human reviewer)  
**Feedback:** Alignment confirmed, readiness gate passed  
**Proceed:** World Spec phase

---

## Phase 2: World Specification

### 2.1 World Spec Architecture

**Date:** May 30, 2026 onwards  
**Scope:** Complete world specification including identity, conditions, medications, baseline anchors, timeline, provider roster, 22 world-level files, 7 task-context files, 4 supplementary files

#### World Identity
- **Patient:** Korvin Merrow, 62-year-old male
- **Setting:** Acute hospital, EM/IM
- **Encounter:** ED → inpatient admission → consultants → discharge planning
- **Timeline:** 5–7 hospital days, snapshot frozen at day 5–7
- **Core Problem:** Altered mental status, weakness, poor intake, AKI on CKD, sepsis work-up

#### 14 Baseline Conditions
1. Type 2 Diabetes Mellitus
2. Hypertension
3. Chronic Kidney Disease Stage 3 (baseline Cr ~2.0)
4. Heart Failure with Reduced Ejection Fraction (EF 25–30%)
5. Coronary Artery Disease (s/p remote PCI/stent)
6. Polymyalgia Rheumatica (on chronic prednisone)
7. Obstructive Sleep Apnea
8. Osteoporosis
9. Anemia of chronic kidney disease
10. Hyperparathyroidism (secondary to CKD)
11. Dyslipidemia
12. GERD
13. Benign Prostatic Hyperplasia
14. Orthostatic Hypotension

#### 20 Baseline Medications (Outpatient)
Detailed list with doses, source authority, and timing (pre-admission state for reconciliation purposes)

#### Temporal Architecture
- **Hour 0:** ED arrival (acute decompensation)
- **HD 1–2:** ED evaluation, admission, initial workup, sepsis protocol
- **HD 3:** Infection improving trend noted, reassessment of contributors
- **HD 4:** Continued improvement, medication adjustments, consultant input
- **HD 5–7:** Discharge planning, readiness assessment, safety coordination
- **Snapshot:** Fixed at 05/23 18:00 (HD 5–7 timeline, pre-discharge, no post-close leakage)

#### Source Hierarchies

**Authority Hierarchy** (for clinical decision-making):  
Hospitalist > Consultants > PT/OT > CM/SW > Family > Patient

**Master Medication Hierarchy** (for med reconciliation):  
Attending > Med-Rec > Pharmacy > Consultants > PCP > Family > Patient

**Prednisone-Specific Hierarchy** (for steroid source):  
Rheumatology > Med-Rec > Pharmacy > Family > Patient

---

### 2.2 World-Level Files (FI-W01–W22)

**22 files total, all locked and evidence-bearing**

| File | Title | Timeline | Key Content |
|------|-------|----------|-----------|
| FI-W01 | ED Triage Initial Intake | Hour 0 | Chief complaint, vital signs, presentation |
| FI-W02 | ED Provider Assessment | Hour 0–2 | Initial H&P, differential, sepsis workup |
| FI-W03 | Admission H&P | HD 1 | Comprehensive baseline, 14 conditions, 20 meds, exam |
| FI-W04 | Initial Medication Reconciliation Note | HD 1 | Med-rec form, reconciliation conflicts begin |
| FI-W05 | Pharmacy Refill History Report | HD 1 | Outpatient fill records, adherence hints, source conflict |
| FI-W06 | Outpatient Rheumatology Prednisone Provenance | Pre-admission | Highest-authority prednisone source |
| FI-W07 | Primary Care Outpatient Baseline Summary | Pre-admission | PCP perspective, medication list version |
| FI-W08–W11 | Hospitalist Progress Notes | HD 1–6 | Daily course documentation, clinical reasoning |
| FI-W12 | Objective Renal/Infection/Hemodynamic Trend Summary | HD 1–6 | Lab trends: Cr, K+, WBC, BP, I&Os |
| FI-W13 | Medication Administration Record (MAR) | HD 1–6 | What actually happened (not what should happen) |
| FI-W14 | Nephrology Consultation | HD 3–4 | Renal perspective, AKI management, medication recommendations |
| FI-W15 | Cardiology Consultation | HD 3–4 | Cardiac perspective, HF management, medication recommendations |
| FI-W16 | Endocrinology Consultation | HD 4 | Steroid physiology interpretation, adrenal risk (not proof of insufficiency) |
| FI-W17 | Bedside Nursing Observation Notes | HD 1–6 | Buried functional evidence, strength assessments, cognitive observations |
| FI-W18 | Physical Therapy Assessment | HD 4–5 | Strength, mobility, ambulation potential, functional trajectory |
| FI-W19 | Occupational Therapy Assessment | HD 4–5 | ADL capability, cognitive status during tasks, discharge readiness |
| FI-W20 | Family Communication/Care Conference | HD 5 | Mara Merrow (wife) concerns, family perspective, discharge wishes |
| FI-W21 | Case Management/Social Work Discharge Planning | HD 5–6 | Support systems, logistics, home equipment, follow-up coordination |
| FI-W22 | Discharge-Facing Plan Snapshot | HD 5–7 (<05/23 18:00) | Visible-but-incomplete: organized improvement + deferred items |

**Properties preserved in all 22 files:**
- Closed-chart documentation (snapshots, not living plans)
- Temporal boundary: No file post-dates 05/23 18:00
- Multi-document synthesis required for all traps
- Source-hierarchy conflicts embedded (not resolved)
- Evidence complete for all task demands

---

### 2.3 Task-Context Files (FI-T01–T07)

**7 files total, all clinician-voice requests, no answers**

| File | Title | Task Workflow | Key Files | Anchor |
|------|-------|---------------|-----------|--------|
| FI-T01 | Discharge Medication Reconciliation Request | Medication Reconciliation | FI-W01–W06, W13, W20 | HD 5–7 |
| FI-T02 | Discharge Summary Drafting Request | Discharge Summary | Full ecosystem | HD 5–7 |
| FI-T03 | Discharge Readiness/Care Coordination Request | Discharge Planning | FI-W17–W21 | HD 5–7 |
| FI-T04 | Consultant Synthesis/Interdisciplinary Plan Request | Care Coordination | FI-W14–W16, W20 | HD 5–7 |
| FI-T05 | Early Post-Discharge Follow-Up Assessment | Post-Discharge Monitoring | Snapshot only | +7 days (no invented facts) |
| FI-T06 | Patient Safety Readmission Risk Review | Safety Review | Snapshot only | +30 days (retrospective, not RCA) |
| FI-T07 | Medication Safety Handoff Addendum | Medication Reconciliation support | Folded into FI-T01 | HD 5–7 |

**Properties:**
- Physician-authored clinician-voice framing
- No answers or expected outputs embedded
- Named FI-W dependencies
- Force synthesis across multiple files
- Task-level traps (if any) distinct from world-level

---

### 2.4 Supplementary Files (FI-S01–S04)

**4 files total, all background/texture, non-load-bearing**

| File | Title | Content Type | Criticality |
|------|-------|--------------|-----------|
| FI-S01 | Remote PCI/Coronary Stent Provenance Summary | Background | CAD history only |
| FI-S02 | Remote Sleep Study/OSA Provenance Summary | Background | Explicitly NOT for AMS explanation |
| FI-S03 | Home Support/Equipment Logistics Reference | Logistics | Discharge environment context |
| FI-S04 | Problem List/Past History Snapshot | Reference | Stale provenance, low-authority |

**Explicit boundary:** Background, provenance, or logistics texture only. Must not carry sole critical evidence, resolve a friction, complete FI-W22, or become an answer source.

**Ratio check:** 4 supplementary / 33 total = ~12% supplementary (safe range)

---

### 2.5 World Spec AutoQC v6.3

**113-check validation framework**  
**Evidence:** Applied to locked world specification  
**Result:** All checks passed or documented with physician approval

---

## Phase 3: Task Layer Construction

### 3.1 Task Prompts (TP-KM01–06)

**6 prompts total, all physician-authored, clinician-voice**

#### TP-KM01: Discharge Medication Reconciliation Request
Clinician-facing request to synthesize medication source conflicts, reconcile contradictions, propose discharge medication plan with source awareness and monitoring strategy

#### TP-KM02: Discharge Summary Drafting Request
Clinician-facing request to reconstruct patient's hospital course, document resolution and persistent issues, synthesize clinical reasoning

#### TP-KM03: Discharge Readiness/Care Coordination Assessment
Clinician-facing request to assess readiness for discharge, evaluate physiologic improvement vs. transition capability, coordinate care team

#### TP-KM04: Consultant Synthesis/Interdisciplinary Care Plan Request
Clinician-facing request to synthesize consultant perspectives without hierarchy collapse, develop unified care plan

#### TP-KM05: Early Post-Discharge Follow-Up Assessment (+7 days)
Prospective surveillance request, anchored at +7 post-discharge, no invented facts allowed

#### TP-KM06: Patient Safety Readmission Risk Review (+30 days)
Retrospective safety analysis, anchored at +30 post-discharge, explicitly NOT a root-cause analysis

---

### 3.2 Expected Outputs (EO-KM01–06)

**6 expected outputs total, physician-authored, define reasoning bands**

**Properties:**
- Not goldens themselves; define strong reasoning without writing answers
- Anti-overanswer (don't prescribe too narrowly)
- Anti-underanswer (don't allow vague conclusions)
- Two-sided friction protection
- Name domains to explore, not answers to reach

---

### 3.3 Golden Responses (Golden-KM01–06)

**6 goldens total, physician-authored, strong reference answers**

#### Golden-KM01 (Medication Reconciliation)
"Leaves room for more than one defensible final medication sequence… key requirement is intentional, monitored, source-aware, communicated"

#### Golden-KM02 (Discharge Summary)
Reconstructs course HD1→HD3→HD4→HD5-6, "improved-but-unresolved" frame, multiple contributors

#### Golden-KM03 (Discharge Readiness)
"Discharge readiness is conditional" (not authorization); family AND team both defensible

#### Golden-KM04 (Interdisciplinary Care Plan)
Reconciles Cardiology and Nephrology without choosing winner; "steroid contribution… does not by itself prove adrenal insufficiency"

#### Golden-KM05 (+7 Follow-Up)
Surveillance frame, "should not invent post-discharge symptoms, labs, services, or outcomes"

#### Golden-KM06 (+30 Safety Review)
"Prospective readmission-risk synthesis," explicitly "not a root-cause analysis"

**Properties preserved in all six:**
- Uncertainty and multi-path defensibility maintained
- No single-sequence logic (medication or course)
- Both sides of all frictions remain two-sided
- All hierarchies applied as reasoning, not shortcuts
- FI-W22 visible-but-incomplete acknowledged
- No adrenal insufficiency presented as revealed answer

---

### 3.4 Grader Guidance (GG-KM01–06)

**6 grader-guidance files total, physician-authored, enforce scoring standards**

**File structure (all six files):**
1. **Golden Reference:** States golden is benchmark, not key
2. **Good Practice That May Receive Credit But Should Not Be Required:** Explicitly allows defensible alternatives
3. **Known Errors:** Lists verbatim-matching and other failures to penalize
4. **Construction Notes:** Confirms no points/thresholds/bands assigned

#### Anti-Verbatim-Matching Enforcement

**Level 1 — Golden Reference (all six files):**  
Each states golden is benchmark, not a key. Example: "The golden is not a rigid medication answer key. Credit clinically safe, source-aware, task-appropriate medication reasoning even when wording, order, or exact sequencing differs."

**Level 2 — Good Practice (all six files):**  
Each ends with explicit anti-rigidity. Example: "Do not require one exact ordering of medication categories if the answer preserves the core safety logic."

**Level 3 — Known Errors (all six files):**  
Each names verbatim-matching itself as an error. Example: "Treating the golden as a fixed medication sequence that must be copied verbatim."

**Level 4 — Construction Notes (all six files):**  
Each reaffirms no scoring logic: "This document assigns no points, thresholds, or pass/fail bands."

#### Multi-Path Defensibility Protections

**GG-KM01 (Medication):**
- Credits "deliberate sequencing and monitoring" (not a single consultant winner)
- Penalizes both "restarting all… at once" AND "leaving all held… stopped indefinitely" (preserves middle band)
- Preserves rheumatology as highest prednisone authority without auto-deferring

**GG-KM02 (Discharge Summary):**
- Credits different wording/ordering if course faithfully summarized
- Penalizes "copy-forward sepsis-only framing"
- Penalizes "steroids explain everything"

**GG-KM03 (Discharge Readiness):**
- Distinguishes physiologic improvement from transition readiness
- Credits conditional conclusions (not binary safe/unsafe)
- Protects family evidence as meaningful, not automatically dispositive
- Protects team perspective as also defensible

**GG-KM04 (Interdisciplinary Care Plan):**
- Preserves cardiology vs nephrology tension
- Penalizes "selecting Cardiology or Nephrology as automatically correct"
- Rewards synthesis through trends/patient-status/timing
- Keeps consultant disagreement resolution to synthesis, not rank

**GG-KM05 (+7 Follow-Up):**
- Prohibits invented +7 facts (symptoms, labs, visits, outcomes)
- Preserves transition-risk surveillance frame
- Anchors to snapshot date; no post-close leakage

**GG-KM06 (+30 Safety Review):**
- Prohibits invented outcomes/readmissions
- Prohibits RCA drift
- Prohibits blame assignment
- Narrowed (per audit Finding-C) to endocrine as background context only

#### Friction Protection (All Three)

**GG-KM01/04:**  
Penalize selecting consultant "as automatically correct" / "automatic winner"

**GG-KM03:**  
Penalize ignoring nursing, PT, OT, CM/SW, family evidence; family concern "meaningful but not automatically dispositive"

**GG-KM06:**  
Explicitly penalize "turning Endocrinology vs Primary Team into the dominant story rather than background steroid-source/endocrine-risk context"

---

## Phase 4: Validation & Lock

### 4.1 Golden Architecture Validation

**Date:** May 31, 2026  
**Scope:** Independent review of Golden-KM01–06 against locked brainstorm, world spec, and governance  
**Reviewer:** Independent validation of physician-authored content

**Validated properties:**
- Trap preservation (all 5 latent; no labels exposed)
- Friction preservation (all 3 two-sided; no collapse)
- Hierarchy preservation (all 3 hierarchies as reasoning; no shortcuts)
- Adrenal insufficiency constraint ("meaningful but not proven" maintained across all six)
- Source-hierarchy conflicts embedded (not resolved)
- FI-W22 visible-but-incomplete consistency
- FI-S non-load-bearing consistency
- Multi-path defensibility maintained in all reasoning domains

**Finding A — Validation Overclaim (Corrected):**  
Validation initially overclaimed source basis for some verification claims. Corrected by adding transparent annotation noting broader claim basis. Documentation-integrity correction, no clinical/architectural defect.

**Finding B — Stale Continuity Surfaces (Corrected):**  
Governance surfaces stated "CANDIDATE REVIEW" while ratified as "LOCKED." Updated to align with ratification record; metadata correction, no governance change.

**Finding C — Golden-KM06 Endocrinology Friction Scope (Corrected):**  
Endocrinology-vs-Team friction was initially too broad in Golden-KM06. Corrected to "background steroid-source / endocrine-risk context only" to align with FI-T06's permitted scope. Reflected across GG-KM06.

**Lock Decision:** RATIFIED AND LOCKED

---

### 4.2 Grader Guidance Construction Validation

**Date:** June 2, 2026  
**Scope:** Independent review of GG-KM01–06 against locked architecture, goldens, expected outputs, prompts, and governance

**11 validation objectives verified:**

#### Objective 1: Count and Mapping (RESOLVED)
Six GG-KM files (KM01–06), no GG-KM07, one-to-one mapping with TP-KM01–06, EO-KM01–06, and Golden-KM01–06. FI-T07 folded into GG-KM01 addendum. Full TP → EO → Golden → GG chain verified.

#### Objective 2: Anti-Verbatim-Matching (RESOLVED)
Enforced at four independent levels per file:
- Golden Reference: golden is benchmark, not key
- Good Practice: explicitly allows defensible alternatives
- Known Errors: lists verbatim-matching as penalizable error
- Construction Notes: no points/thresholds/bands

Future graders can reasonably credit clinically sound alternatives.

#### Objective 3: Multi-Path Defensibility (RESOLVED)
Alternative defensible reasoning remains creditable; no hidden answer-key behavior; no single-sequence medication/course logic; conditional conclusions credited; both sides all three frictions remain defensible.

#### Objective 4: Medication Guidance (GG-KM01) (RESOLVED)
Cardiology vs Nephrology tension preserved; prednisone hierarchy preserved (rheumatology strongest); inpatient-vs-outpatient distinction preserved; staged reasoning rewarded; does NOT become medication answer key; does NOT force one restart sequence; does NOT over-credit consultant-winner selection.

#### Objective 5: Discharge Readiness (GG-KM03) (RESOLVED)
Physiologic improvement distinguished from transition readiness; family concern appropriately handled (meaningful evidence, not automatically dispositive); PT/OT/nursing/CM/SW evidence protected. Does NOT become discharge-authorization rubric; does NOT create hidden disposition key; does NOT force one conclusion.

#### Objective 6: Follow-Up and Outcome Protection (RESOLVED)
GG-KM05: prohibits invented +7 facts, preserves transition-risk framing  
GG-KM06: prohibits invented outcomes/readmissions, prohibits RCA drift, prohibits blame, honors anchor-as-review-date rule

#### Objective 7: Hierarchy Protection (RESOLVED)
All three hierarchies preserved as reasoning, not shortcuts. Prednisone hierarchy with rheumatology highest protected. Source hierarchy explicitly NOT a shortcut for clinical disagreement resolution.

#### Objective 8: Friction Protection (RESOLVED)
All three frictions preserved with anti-winner guardrails. GG-KM06 correctly scopes endocrine as background per audit Finding-C. Guidance rewards defensible synthesis, penalizes winner-selection.

#### Objective 9: Source Fidelity (RESOLVED)
FI-T stays task framing, FI-W stays evidence, FI-S stays background/support. FI-W22 stays visible-but-incomplete across all six. No FI-S becomes sole evidence. No score leakage.

#### Objective 10: Grading Leakage Boundary (RESOLVED)
Guidance does NOT become scoring rubric, point system, threshold system, pass/fail framework. Every GG file's Construction Notes explicitly assigns no points/thresholds/bands. Scoring reserved for separate, later-authorized phase.

#### Objective 11: Validation Review Accuracy (RESOLVED)
Validation accurately reflects GG files; one honest disclosure: architecture-footer status corrected from CANDIDATE REVIEW to LOCKED (metadata alignment, not substantive change). Documented transparently.

**True Defects:** NONE

**Governance/Metadata Inconsistencies:** NONE residual (Finding-C corrected and reflected)

**Physician Preference Items:**
1. Good Practice sections are key multi-path protectors; ensure these stay genuinely optional in eventual scoring
2. GG-KM01 Known Errors list appropriately strict on prednisone-source and inpatient-lispro (weight as safety-critical without rigid key)

**Future AutoQC Watch Items:**
1. Official Section 6 Grader Guidelines AutoQC prompt not yet imported (must be imported before grader-guidance AutoQC runs)
2. Scoring construction (points/thresholds/pass-fail) reserved for separate, later-authorized phase
3. Keep GG-KM03/05/06 scoring distinct (present readiness / prospective follow-up / retrospective safety)
4. Packaging-layer World Spec AutoQC carry-forwards remain live (2.52 ratio, 2.113 Tool/Origin, 2.108 administrative-deliverable, v6.3 8-column file plan)

**Lock Decision:** LOCK READY — All six GG-KM files approved for ratification and lock

**Guidance Quality:** STRONG  
**Benchmark Integrity:** HIGH  
**Final Recommendation:** GO

---

### 4.3 Audit Findings & Reconciliations

**Finding A — Validation Overclaim (Documentation-Integrity Correction)**
- **Issue:** Validation review initially overclaimed source basis for verification claims
- **Resolution:** Transparent annotation added noting broader claim basis
- **Type:** Documentation-integrity correction, not clinical/architectural defect
- **Impact:** Audit disclosure maintains transparency; no hidden corrections

**Finding B — Stale Continuity Surfaces (Metadata Alignment)**
- **Issue:** Current-facing governance surfaces stated "CANDIDATE REVIEW" while actual governance ratified to "LOCKED"
- **Resolution:** Updated surface status to match ratification record
- **Type:** Metadata-alignment correction, no substantive governance change
- **Impact:** Documentation now consistent with locked decisions

**Finding C — Golden-KM06 Endocrinology Friction Scope (Architecture Refinement)**
- **Issue:** Endocrinology-vs-Team friction initially too broad in Golden-KM06
- **Resolution:** Narrowed to "background steroid-source / endocrine-risk context only" to align with FI-T06 permitted scope
- **Impact:** Reflected across all GG-KM06 content; grader guidance explicitly penalizes over-amplification

**Finding D — FI-S Boundary Clarification**
- **Issue:** FI-S (supplementary) files under-specified in initial guidance
- **Resolution:** Explicit wording: "background, provenance, or logistics texture only… must not carry sole critical evidence, resolve a friction, complete FI-W22, or become an answer source"
- **Impact:** 4 supplementary files now clearly non-load-bearing; 29 essential files protected as primary evidence

**Reconciliation Discipline:** All findings disclosed transparently rather than made silently. Audit documents explain findings, resolutions, and impact on downstream layers. This transparent approach establishes documentation-integrity discipline across all future phases.

---

### 4.4 Lock-Readiness Confirmation

**Date:** June 2, 2026  
**Lock Decision:** LOCK READY

#### Complete Ecosystem Locked and Verified
- 22 world-level files (FI-W01–W22) — LOCKED
- 7 task-context files (FI-T01–T07) — LOCKED
- 4 supplementary files (FI-S01–S04) — LOCKED
- 6 task prompts (TP-KM01–06) — LOCKED
- 6 expected outputs (EO-KM01–06) — LOCKED
- 6 golden responses (Golden-KM01–06) — LOCKED
- 6 grader-guidance documents (GG-KM01–06) — LOCKED
- Governance and validation documentation — LOCKED

#### All Key Properties Preserved
- Trap integrity: All 5 traps remain latent, reasoning-required, no labels exposed
- Friction integrity: All 3 frictions remain two-sided with anti-winner guardrails
- Hierarchy integrity: All 3 hierarchies preserved as reasoning, not shortcuts
- Synthesis requirement: Every task forces multi-document reconciliation
- FI-W22: Visible-but-incomplete (incomplete without FI-W series, FI-T context, consultant details)
- FI-S: Non-load-bearing (background/provenance/logistics only, never sole evidence)
- Source-of-truth conflicts: Embedded, not resolved
- Multi-path defensibility: Alternative defensible approaches credited at all layers
- Anti-verbatim-matching: Enforced four times per GG file

#### AutoQC Readiness
- Section 2 World Spec AutoQC v6.3 (113 checks): Ready to run
- Section 6 Grader Guidelines AutoQC: Prompt must be imported before running

#### Packaging Carry-Forwards (Standing)
1. **2.52 Essential/Supplementary Ratio:** Verify 29 essential / 4 supplementary ≈ 12% supplementary
2. **2.113 Tool/Origin Two-Track Specification:** Assign per-file engineering-converted vs writer-produced-media origin with filename convention
3. **2.108 Administrative Deliverable:** Confirm Discharge Planning Documentation satisfies requirement (utilization-review named fallback)
4. **v6.3 8-Column File Plan:** Ensure Section 3 uses v6.3 structure (Source + Tool as separate columns)

---

## Forward Dependencies

### AutoQC Phase (Authorization Required)

#### Blocking Issue
**Section 6 Grader Guidelines AutoQC prompt** not yet in local repository. Must be imported from official Anthropic reference before grader-guidance AutoQC can run.

#### AutoQC Tasks (In Sequence)
1. Import Section 6 Grader Guidelines AutoQC prompt
2. Run Section 2 World Spec AutoQC v6.3 (113 checks) against locked world spec
3. Run Section 6 Grader Guidelines AutoQC against locked grader guidance (GG-KM01–06)
4. Confirm all checks pass or document physician approvals

---

### Packaging Phase (Dependent on AutoQC Completion)

#### Carry-Forward 1: 2.52 Essential/Supplementary Ratio
- **Current:** 29 essential (22 world + 7 task-context), 4 supplementary ≈ 12%
- **Requirement:** Confirm against 2.52 specification (safe direction)
- **Action:** Verify ratio at packaging

#### Carry-Forward 2: 2.113 Tool/Origin Two-Track Filename Convention
- **Current:** Per-file Tool/Origin specification needed
- **Requirement:** Assign engineering-converted vs writer-produced-media origin per 2.113
- **Action:** Apply two-track naming convention at packaging

#### Carry-Forward 3: 2.108 Administrative Deliverable
- **Current:** Discharge Planning Documentation (TP-KM03/T05/T06 under 4-workflow architecture)
- **Requirement:** Confirm administrative-deliverable requirement satisfied
- **Fallback:** Utilization-review named if reviewer challenges
- **Action:** Finalize at packaging

#### Carry-Forward 4: v6.3 8-Column File Plan (Section 3)
- **Current:** File plan needs v6.3 structure (Source, Tool as separate columns)
- **Requirement:** Rebuild Section 3 table with v6.3 format (not 05/06 template's 7 columns)
- **Action:** Rebuild Section 3 at packaging with v6.3 structure

**END OF TRANSCRIPT**

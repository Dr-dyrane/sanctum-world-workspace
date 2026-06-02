# Batch 4 Synthetic World-Level File Construction Validation Review

World: Korvin Merrow

Artifact set: Batch 4 Synthetic World-Level Files

Status: CANDIDATE REVIEW

Files reviewed:

- `worlds/korvin-merrow/synthetic-files/candidate-review/batch-4/FI-W17_bedside-nursing-observation-notes-flowsheet-summary.md`
- `worlds/korvin-merrow/synthetic-files/candidate-review/batch-4/FI-W18_physical-therapy-assessment.md`
- `worlds/korvin-merrow/synthetic-files/candidate-review/batch-4/FI-W19_occupational-therapy-assessment.md`
- `worlds/korvin-merrow/synthetic-files/candidate-review/batch-4/FI-W20_family-communication-care-conference-documentation.md`
- `worlds/korvin-merrow/synthetic-files/candidate-review/batch-4/FI-W21_case-management-social-work-discharge-planning-note.md`

This validation review checks Batch 4 construction against locked World Spec v1, File Inventory v1, Synthetic World-Level File Construction Plan v1, Governance Package v1, locked Batches 1-3, and the explicit Batch 4 authorization.

It does not create FI-W22, task prompts, expected outputs, golden responses, grader guidance, AutoQC responses, submission artifacts, post-world information, or additional synthetic file rows.

## Authorized File Creation Validation

### VERIFIED

Finding: FI-W17 through FI-W21 were created in the authorized candidate-review path.

Evidence: the Batch 4 candidate folder contains nursing, physical therapy, occupational therapy, family communication, case management/social work, and this validation review only.

Impact: construction stayed within the authorized Batch 4 file IDs.

Action required: none before candidate review.

### VERIFIED

Finding: no unauthorized FI-W22 file was created.

Evidence: Batch 4 construction stops at FI-W21.

Impact: Batch 5 remains reserved for FI-W22 and Trap #5's visible-but-incomplete discharge-facing artifact.

Action required: do not create FI-W22 until explicitly authorized.

### VERIFIED

Finding: no task-level, supplementary, prompt, golden, grader, AutoQC, DOCX, or submission artifacts were created.

Evidence: constructed artifacts are limited to the authorized Batch 4 candidate-review files and validation review.

Impact: downstream phase boundaries remain intact.

Action required: none before candidate review.

## Temporal Validation

### VERIFIED

Finding: no post-world information is present.

Evidence: FI-W17 through FI-W21 are anchored from HD1-HD6, HD3-HD6, or HD5-HD6 and contain only information available before 05/23/2026 at 18:00.

Impact: closed-world discipline is preserved.

Action required: none before candidate review.

### VERIFIED

Finding: no discharge outcome, +7 follow-up, or +30 follow-up was created.

Evidence: all five files explicitly avoid completed discharge outcome and post-discharge follow-up.

Impact: discharge anchor, +7, and +30 remain outside the world snapshot.

Action required: preserve this boundary when constructing FI-W22 and task-context files later.

## Trap #3 Validation

### VERIFIED

Finding: Trap #3 is present, clinically meaningful, distributed, and discoverable.

Evidence:

- FI-W17 carries bedside cueing, intake, transfer, short-distance ambulation, and family-presence observations.
- FI-W18 carries mobility, gait, transfer safety, balance, and endurance evidence.
- FI-W19 carries ADL, sequencing, medication-management simulation, and cognitive-functional evidence.
- FI-W20 carries family baseline deviation, medication-management concern, and home-safety questions.
- FI-W21 carries support-system, caregiver-capacity, services, and medication-instruction logistics.

Impact: functional/cognitive concerns require synthesis across nursing, PT, OT, family, and care coordination.

Action required: candidate review should confirm the evidence is subtle enough and not overly decisive.

### VERIFIED

Finding: no single file becomes the Trap #3 answer key.

Evidence: each file contributes only part of the functional/cognitive picture and explicitly rejects final disposition authority.

Impact: a reader cannot solve discharge readiness by reading one dramatic note.

Action required: preserve distributed evidence if revising.

### VERIFIED

Finding: functional concerns are plausible, subtle, and cumulative.

Evidence: Batch 4 uses weakness, endurance limits, cueing needs, medication-management complexity, fatigue, balance changes, and family baseline concern without dramatic disability or obvious discharge failure.

Impact: discharge remains plausible but not safely solved.

Action required: none before candidate review.

## Trap #3 vs Trap #5 Validation

### VERIFIED

Finding: Trap #3 and Trap #5 remain distinct.

Evidence: Batch 4 contains buried functional/cognitive evidence and care-coordination substrate. It does not create FI-W22's visible discharge-facing artifact.

Impact: Trap #3 remains "find the lower-visibility functional/cognitive evidence." Trap #5 remains reserved for over-trusting a later visible but incomplete discharge-facing source.

Action required: FI-W22 later must remain visible-but-incomplete and must not duplicate or resolve all Batch 4 functional evidence.

### VERIFIED

Finding: Batch 4 does not create a visible-but-incomplete discharge artifact.

Evidence: FI-W21 discusses logistics and open items but does not become a discharge plan snapshot, discharge summary, or final interdisciplinary plan.

Impact: Batch 5 remains necessary.

Action required: do not move FI-W22 content into Batch 4 during revision.

## Family vs Primary Team Friction Validation

### VERIFIED

Finding: family concerns remain meaningful.

Evidence: FI-W17 and FI-W20 record family baseline knowledge; FI-W19 and FI-W21 connect those concerns to medication-management and support needs.

Impact: family is not dismissed as generic anxiety.

Action required: none before candidate review.

### VERIFIED

Finding: primary-team discharge-planning logic remains defensible.

Evidence: Batch 4 repeatedly acknowledges medical improvement, better intake, improved alertness, improving objective trends, and plausible discharge planning.

Impact: family is not made obviously correct and the primary team is not made careless.

Action required: preserve balance in candidate review.

### VERIFIED

Finding: family communication does not independently prove discharge is unsafe.

Evidence: FI-W20 states Mara wants discharge when safe, asks appropriate questions, and does not establish refusal or a decisive unsafe-discharge fact.

Impact: the friction remains two-sided.

Action required: none before candidate review.

## Source Hierarchy Validation

### VERIFIED

Finding: source-of-truth hierarchies are preserved.

Evidence: FI-W20 states family report is clinically important but lower authority for factual medication and prednisone conflicts. FI-W19 and FI-W21 do not convert therapy or care-coordination observations into medication-source authority.

Impact: governance remains intact.

Action required: none before candidate review.

### VERIFIED

Finding: prednisone uncertainty is preserved.

Evidence: FI-W20 includes family uncertainty about actual home prednisone behavior while explicitly preserving rheumatology as highest outpatient taper authority. FI-W21 flags prednisone instruction needs without creating a taper plan.

Impact: Trap #1 remains active without Endocrinology or family replacing rheumatology.

Action required: later files must not let family communication or Endocrinology replace rheumatology as prednisone-history source of truth.

### VERIFIED

Finding: medication-restart uncertainty is preserved.

Evidence: FI-W17-FI-W21 reference medication-management burden, but no file creates a final medication list, final restart plan, or final discharge medication reconciliation.

Impact: Trap #2 and consultant timing friction remain active.

Action required: later FI-W22 must not make either consultant or the MAR the final medication authority.

## Batch Consistency Validation

### VERIFIED

Finding: Batch 1 consistency is preserved.

Evidence: Batch 4 uses FI-W07 baseline function and family support context, FI-W01/FI-W03 pre-admission decline and medication mistakes, and FI-W04/FI-W05/FI-W06 medication/prednisone uncertainty without altering them.

Impact: baseline remains the comparator rather than being rewritten.

Action required: none before candidate review.

### VERIFIED

Finding: Batch 2 consistency is preserved.

Evidence: Batch 4 builds on FI-W09's emerging functional/cognitive concern, FI-W11's medically improving but operationally dangerous frame, FI-W12 objective improvement limits, and FI-W13 MAR-action caveats.

Impact: hospital-course spine is preserved.

Action required: none before candidate review.

### VERIFIED

Finding: Batch 3 consistency is preserved.

Evidence: Batch 4 references consultant concerns as active context but does not override Nephrology, Cardiology, or Endocrinology and does not resolve their disagreement.

Impact: consultant notes remain interpretation sources requiring hospitalist synthesis.

Action required: none before candidate review.

## Inpatient-Only Insulin Lispro Validation

### VERIFIED

Finding: insulin lispro remains inpatient-only.

Evidence: FI-W21 states inpatient-only correctional insulin lispro should not be assumed to be a home medication without a final authorized medication plan.

Impact: Medication Expansion Package v1 and FI-W13 logic remain intact.

Action required: none before candidate review.

## Answer-File Drift Validation

### VERIFIED

Finding: no Batch 4 file becomes an answer file.

Evidence:

- FI-W17 is not a final disposition decision.
- FI-W18 is not a final therapy/discharge order.
- FI-W19 is not a final medication reconciliation or disposition answer.
- FI-W20 is not a family-wins/family-loses decision file.
- FI-W21 is not a final discharge plan or services authorization.

Impact: Batch 4 supports synthesis rather than replacing it.

Action required: candidate review should preserve this design.

## Carry-Forward Watch Items

- FI-W22 must remain visible-but-incomplete and must not duplicate all Batch 4 caveats.
- FI-W22 must not resolve final disposition, final medication restart, final prednisone taper, or all consultant caveats.
- Later files must preserve nursing/PT/OT/family/CM-SW evidence as distributed substrate rather than flattening it into one conclusion.
- Later files must preserve family concerns as meaningful but not independently dispositive.
- Later files must preserve the difference between medical improvement and discharge readiness.

## Final Validation Status

Batch 4 Synthetic World-Level File Construction:

- FI-W17 through FI-W21 created.
- Status: CANDIDATE REVIEW.
- No unauthorized files created.
- No temporal leakage identified.
- No answer-file drift identified.
- Trap #3 preserved.
- Trap #3 vs Trap #5 distinction preserved.
- Family vs Primary Team friction preserved.
- Batch 1, Batch 2, and Batch 3 consistency preserved.

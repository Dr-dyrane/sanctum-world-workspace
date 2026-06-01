# Provider Roster Package v1

Date created: 2026-06-01

Status: CANDIDATE REVIEW.

Purpose: define the provider, care-team, and stakeholder architecture for Korvin Merrow before World Spec construction, file planning, note authorship, synthetic documents, task prompts, expected outputs, golden responses, or grader guidance.

This package answers: who are the clinicians, services, and stakeholders in the world, and what authority/source role does each one have?

This package does not create actual clinical notes, provider-authored documents, file inventory, task prompts, expected outputs, golden responses, grader guidance, medication schedules, hospital-course events, labs, vitals, World Spec prose, templates, reference files, or synthetic documents.

## Source Constraints

Use only:

- Approved Brainstorm.
- Ratified Clinical Story Skeleton v1.
- Locked Identity Package v1.
- Ratified Governance Package v1.
- Locked Key Milestones Calendar Skeleton v1.
- Locked Baseline Anchor Package v1.
- Locked Clinical Story Timeline Package v1.
- Locked Task Architecture Package v1.
- Locked Medication Expansion Package v1.
- Locked Comorbidity Expansion Package v1.
- Current Clinical Logic.

## 1. Named Provider Strategy

Recommended strategy: use named fictional providers for recurring high-authority roles and service-role placeholders for minor or rotating contributors.

Rationale:

- High-authority recurring roles need stable provenance for source-of-truth reasoning.
- Minor or rotating contributors can remain role-based to avoid over-naming and unnecessary cast complexity.
- Names should be clearly fictional, internally distinct, and not resemble common real-person names.
- Provider names are architecture placeholders only. They are not note authorship, file inventory, synthetic chart content, or World Spec prose.

Named recurring high-authority roles:

- Attending hospitalist: Dr. Elian Vossmere.
- Cardiology attending: Dr. Maris Caldrane.
- Nephrology attending: Dr. Iven Solthar.
- Endocrinology attending: Dr. Nerea Veylorn.
- Primary care physician: Dr. Talia Quenor.
- Outpatient rheumatology attending: Dr. Soren Halvek.
- Family/caregiver stakeholder: Mara Merrow.

Service-role placeholders:

- Hospitalist resident / covering clinician.
- Bedside nursing team.
- Physical Therapy.
- Occupational Therapy.
- Case Management.
- Social Work.
- Pharmacy / medication reconciliation pharmacist.

## 2. Provider Roster

| Roster entry | Role | Service | Likely authority domain | Likely source-of-truth contribution | Friction/trap relevance | Future document-authorship relevance |
| --- | --- | --- | --- | --- | --- | --- |
| Dr. Elian Vossmere | Attending hospitalist | Primary inpatient team | Overall inpatient decision ownership, disposition synthesis, integration of consultant recommendations | Attending documentation; final inpatient assessment; discharge-readiness interpretation | Central to Family vs Primary Team and Endocrinology vs Primary Team; must reconcile Cardiology vs Nephrology | High relevance for admission/progress/discharge planning documents later, but no note is created here |
| Hospitalist resident / covering clinician | Rotating inpatient clinician | Primary inpatient team | Day-to-day updates under attending supervision | Progress-note carry-forward risk; possible outdated problem framing | Supports sepsis anchoring and copy-forward trap without being a main friction participant | Possible future progress-note authorship role; keep unnamed unless later needed |
| Dr. Maris Caldrane | Cardiology attending | Cardiology | HFrEF/CAD therapy and long-term cardiovascular risk | Cardiology consultant recommendations; GDMT restart perspective | Direct participant in Cardiology vs Nephrology; supports HF/AKI medication trap and outdated consultant recommendation trap | High relevance for cardiology consultant note authorship later |
| Dr. Iven Solthar | Nephrology attending | Nephrology | AKI-on-CKD safety, renal recovery, hypotension/volume-risk interpretation | Nephrology consultant recommendations; renal medication safety perspective | Direct participant in Cardiology vs Nephrology; supports HF/AKI medication trap and temporal recommendation trap | High relevance for nephrology consultant note authorship later |
| Dr. Nerea Veylorn | Endocrinology attending | Endocrinology | Steroid-risk interpretation, adrenal reserve concern, safe prednisone evaluation/taper framing | Endocrinology consultant recommendations; steroid risk interpretation | Direct participant in Endocrinology vs Primary Team; supports prednisone source-of-truth trap | High relevance for endocrinology consultant note authorship later |
| Physical Therapy service | Functional assessment team | Physical Therapy | Mobility, transfers, endurance, gait safety, discharge functional recommendations | PT assessment; functional capacity and assistance needs | Supports Family vs Primary Team; key substrate for buried functional/cognitive trap and discharge safety trap | Future PT assessment may carry buried functional evidence; no final note created here |
| Occupational Therapy service | Functional / ADL assessment team | Occupational Therapy | ADLs, medication-management ability, cognitive/functional safety for home tasks | OT assessment; ADL safety and self-management concerns | Supports Family vs Primary Team; reinforces discharge readiness and home-safety concerns | Future OT assessment may support medication-management/disposition evidence; no final note created here |
| Bedside nursing team | Longitudinal bedside observation | Nursing | Moment-to-moment cognition, oral intake, ambulation tolerance, family concerns, medication administration observations | Nursing notes, flowsheet observations, family communication | Supports buried functional/cognitive trap and Trap #3 vs Trap #5 distinction | Future nursing documentation may carry easy-to-miss evidence; keep role-based |
| Case Management | Transition/disposition coordination | Case Management | Services, equipment, placement, home support, follow-up logistics | Discharge planning and care coordination artifacts | Supports Family vs Primary Team and administrative deliverable; contributes to discharge source-hierarchy trap | Future discharge planning documentation relevance; keep role-based unless later needed |
| Social Work | Psychosocial and caregiver-support assessment | Social Work | Caregiver capacity, barriers to safe discharge, social support | Social-work documentation and family/caregiver context | Supports Family vs Primary Team and discharge safety synthesis | Future support/barrier documentation relevance; keep role-based unless later needed |
| Pharmacy / medication reconciliation pharmacist | Medication history and reconciliation support | Pharmacy | Medication source verification, refill history, inpatient/discharge med-rec support | Verified med rec; pharmacy history; steroid/HF medication source reconciliation | Supports prednisone source-of-truth trap, HF/AKI medication trap, and medication reconciliation complexity | Future med-rec/provenance role; keep role-based unless later needed |
| Dr. Talia Quenor | Primary care physician | Outpatient primary care | Baseline function, chronic disease trajectory, outpatient medication context, follow-up continuity | Primary care documentation and longitudinal baseline | Supports source-of-truth hierarchy and post-discharge continuity; secondary to hospital decision-making | Future outpatient history/follow-up provenance role; no document created here |
| Dr. Soren Halvek | Outpatient rheumatology attending | Rheumatology | PMR history, prednisone taper plan, steroid exposure interpretation | Rheumatology attending recommendation; top prednisone-specific source | Supports prednisone source-of-truth trap and Endocrinology vs Primary Team without becoming a main inpatient friction | Future outpatient steroid-history source; no document created here |
| Mara Merrow | Family/caregiver stakeholder | Family / home support | Baseline function, cognition, medication-management ability, deviation from baseline, home safety | Family report; caregiver observations | Direct participant in Family vs Primary Team; supports buried functional/cognitive and discharge safety traps | Future family communication provenance; not a clinical note author |
| Korvin Merrow | Patient | Patient | Symptoms, recollection, medication self-management account, functional experience | Patient recollection; lower-authority but clinically relevant source | Supports source-of-truth ambiguity, especially medication/steroid history and functional trajectory | Future patient-reported information source; not a provider |

## 3. Authority And Source-of-Truth Compatibility

### Governance Package Authority Hierarchy

Compatible ordering:

1. Attending hospitalist: Dr. Elian Vossmere.
2. Consulting attending specialists: Dr. Maris Caldrane, Dr. Iven Solthar, Dr. Nerea Veylorn.
3. PT/OT functional assessments.
4. Case Management / Social Work.
5. Family reports: Mara Merrow.
6. Patient recollection: Korvin Merrow.

Implementation guardrail:

- Authority hierarchy resolves role-based governance and factual/documentation conflicts where appropriate.
- It does not erase consultant disagreement.
- Cardiology vs Nephrology and Endocrinology vs Primary Team must still be reconciled through evidence synthesis, timing, trends, patient status, and discharge safety.

### Master Source-of-Truth Hierarchy

Compatible source roles:

1. Attending documentation: Dr. Elian Vossmere.
2. Verified medication reconciliation: Pharmacy / medication reconciliation pharmacist.
3. Pharmacy history: Pharmacy source.
4. Consultant documentation: Cardiology, Nephrology, Endocrinology.
5. Primary Care Documentation: Dr. Talia Quenor.
6. Family report: Mara Merrow.
7. Patient recollection: Korvin Merrow.

### Prednisone Source-of-Truth Hierarchy

Compatible source roles:

1. Rheumatology attending recommendation: Dr. Soren Halvek.
2. Verified medication reconciliation: Pharmacy / medication reconciliation pharmacist.
3. Pharmacy / refill history: Pharmacy source.
4. Family report: Mara Merrow.
5. Patient recollection: Korvin Merrow.

Guardrail:

- Dr. Nerea Veylorn can interpret adrenal/steroid risk during hospitalization, but outpatient rheumatology remains the highest-authority prednisone-history source.
- Documentation discrepancies remain traps, not friction participants.

## 4. Friction Support Review

### Cardiology vs Nephrology

Support:

- Dr. Maris Caldrane represents the cardiovascular protection and GDMT restart perspective.
- Dr. Iven Solthar represents renal recovery, hypotension avoidance, and AKI-on-CKD medication safety.
- Dr. Elian Vossmere must reconcile both recommendations rather than automatically deferring to one specialist.

Assessment: strongly supported.

### Family vs Primary Team

Support:

- Mara Merrow carries longitudinal baseline knowledge and real-world home safety concerns.
- Dr. Elian Vossmere and the primary team carry the medically-improving inpatient perspective.
- PT, OT, nursing, case management, and social work provide evidence that can support either cautious discharge planning or defensible discharge with supports.

Assessment: strongly supported.

### Endocrinology vs Primary Team

Support:

- Dr. Nerea Veylorn represents the steroid/adrenal risk interpretation.
- Dr. Elian Vossmere represents the primary team's concern about over-attributing symptoms to steroids after sepsis-oriented improvement.
- Dr. Soren Halvek and pharmacy sources provide evidence substrate for the steroid timeline without becoming inpatient friction participants.

Assessment: strongly supported with appropriate trap/friction separation.

## 5. Trap Support Review

### Prednisone Source-of-Truth Trap

Support:

- Rheumatology, pharmacy, family, patient, hospitalist, and endocrinology roles are all defined with distinct authority levels.
- This supports reconstructing prednisone exposure without reducing the conflict to "Endocrinology vs Documentation."

Guardrail:

- Steroid discrepancy remains an information trap. The human friction is Endocrinology vs Primary Team risk interpretation.

### HF/AKI Medication Trap

Support:

- Cardiology, nephrology, hospitalist, and pharmacy roles all have distinct source and recommendation functions.
- Pharmacy supports medication history; consultants support time-sensitive clinical recommendations; hospitalist integrates the final plan.

Guardrail:

- Latest note is not automatically correct; timing and clinical context govern applicability.

### Buried Functional / Cognitive Trap

Support:

- Nursing, PT, OT, family, case management, and social work are defined as sources for functional/cognitive/disposition evidence.
- These roles create future evidence channels beyond physician progress notes.

Guardrail:

- Trap #3 is about finding buried evidence. It is not the same as judging whether discharge is safe after evidence is found.

### Discharge Source-Hierarchy Trap

Support:

- Hospitalist, case management, social work, PT/OT, nursing, pharmacy, family, and consultants can later create visible but incomplete discharge-related artifacts.
- This supports a source-hierarchy problem where one reassuring discharge artifact should not be trusted alone.

Guardrail:

- Trap #5 remains distinct from Trap #3: the problem is over-trusting a visible source, not merely missing hidden evidence.

### Trap #3 vs Trap #5 Distinction

Preserved distinction:

- Trap #3: buried functional/cognitive evidence exists but is easy to miss.
- Trap #5: a visible discharge/source-hierarchy artifact appears sufficient if trusted alone.

Future construction note:

- Provider roles should later help separate where evidence is buried from where visible but incomplete conclusions appear.

## 6. Future Construction Compatibility

### Surgical-History Package

Compatibility:

- Provider roster does not create surgical history.
- PCP or outpatient records can later support surgical-history provenance if Alexander authorizes that package.

### Daily Hospital-Course Framework

Compatibility:

- Provider roster supports daily evolution without creating hospital-course events.
- Consultant roles can later enter the timeline without this package creating note dates or events.

### File Inventory Architecture

Compatibility:

- Roster defines potential authorship/provenance sources but does not create filenames, file counts, document dates, or Section 3 rows.

### World Spec Construction

Compatibility:

- Roster can later support Patient Profile, Clinical Complexity, Decision Friction Table, task provenance, and file-plan traceability.
- It is not itself World Spec prose.

### Task Prompts, Goldens, And Grader Guidance

Compatibility:

- Roster can later support requester/persona choices and provenance logic.
- It does not create task prompts, expected outputs, goldens, or grader guidance.

## Provider Roster Consistency Review

### VERIFIED

Finding: no required friction participant is omitted.

Evidence: Cardiology, Nephrology, Endocrinology, Primary Team, Family, PT/OT, nursing, pharmacy, case management, social work, PCP, and rheumatology are represented.

Impact: supports the approved frictions and major traps.

Action required: physician review before lock.

### VERIFIED

Finding: authority and source-of-truth hierarchies remain compatible with Governance Package v1.

Evidence: named high-authority roles map directly to attending hospitalist, consulting attending specialists, PCP, rheumatology attending, family, and patient positions in the ratified hierarchies.

Impact: reduces future source-conflict drift.

Action required: preserve hierarchy distinctions during later construction.

### VERIFIED

Finding: provider strategy avoids over-naming.

Evidence: recurring high-authority roles and family stakeholder are named; rotating or minor contributors remain service-role placeholders.

Impact: provides enough provenance for future construction without creating unnecessary cast burden.

Action required: do not name additional minor staff unless later file construction requires it.

### VERIFIED

Finding: provider names are intentionally fictional and internally distinct.

Evidence: Elian Vossmere, Maris Caldrane, Iven Solthar, Nerea Veylorn, Talia Quenor, Soren Halvek, and Mara Merrow are uncommon constructed names and do not use real institutions.

Impact: reduces real-person-name risk.

Action required: later name additions should follow the same synthetic-name standard.

### VERIFIED

Finding: no premature file construction occurs.

Evidence: the package describes future document-authorship relevance but creates no notes, file inventory rows, filenames, dates, or synthetic documents.

Impact: phase boundary remains intact.

Action required: stop before file planning or document creation.

### PLAUSIBLE

Finding: the resident / covering clinician placeholder is useful but may not need to be used later.

Evidence: rotating clinicians can create realistic copy-forward risk, but the world may be simpler if major notes remain attending/service-authored.

Impact: useful optional provenance source without forcing a new named provider.

Action required: decide later during authorized daily-course or file-inventory construction whether this role is needed.

### PLAUSIBLE

Finding: pharmacy may need a named pharmacist later if medication reconciliation becomes highly provenance-dependent.

Evidence: pharmacy is central to verified medication reconciliation and refill-history interpretation, but a role placeholder may be sufficient for now.

Impact: no blocker; naming can be deferred until file construction.

Action required: keep role-based now; revisit only if later file construction needs a recurring named pharmacist.

### DISPUTED

Finding: none.

Evidence: no provider role contradicts the approved Brainstorm, ratified Governance Package, locked Task Architecture Package, locked Medication Expansion Package, or locked Comorbidity Expansion Package.

Impact: no redesign required before physician review.

Action required: none.

### NO ISSUE

Finding: this package does not create labs, vitals, medication schedules, hospital-course events, provider-authored notes, file inventory, task prompts, expected outputs, golden responses, grader guidance, templates, reference files, synthetic documents, or World Spec prose.

Evidence: the document is limited to provider/care-team architecture and consistency review.

Impact: phase boundary remains intact.

Action required: stop before downstream construction.

## Final Status

Provider Roster Package v1

Status: CANDIDATE REVIEW

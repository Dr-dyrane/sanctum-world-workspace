# KM06 build packet - pre-discharge fall and injury-risk safety review (omission + scope-drift mechanism)

Prepared 2026-06-08 (Claude.ai red-team/build pass, pasted by Alexander). DRAFT and PROPOSAL only. Nothing built, staged, mounted, uploaded, AutoQC-run, or agent-run. Alexander authors and signs the final artifacts and runs the pilot. House style: no em or en dashes, no arrows, no asterisks.

Substrate verification status (Claude, 6/8): all core claims confirmed on agent-read bytes - osteoporosis M81.0 + chronic steroid exposure; alendronate not administered inpatient (MAR "outpatient chronic, reconcile"); calcium/vitD 600/400 BID "continued where tolerated"; NO DXA/bone-density study anywhere in 26 files; orthostatic vitals recommended by nephrology ("when feasible") + endocrinology ("as mobility advances") and nephrology documents "orthostatic data are not fully captured"; telemetry "sinus rhythm without sustained ectopy, no indication for advanced cardiac imaging"; Morse 65 unchanged; near-fall 05/17; gabapentin held selected days for sedation/fall-risk + documented lightheadedness on standing (PT). Pin the exact "SBP 98" gabapentin-hold value on the MAR before it enters the golden.

## 0. Read this before publishing
Deep slot, on the one mechanism the suite has not proven on a live run: omission. No KM task has banked it. Depth least certain of the six. Must be piloted before banking. If it lands all-high with no significant failure it will not clear the gate and the gap must be made harder or a third buried gap added. Publishing fast is fine; banking without a pilot is not.

## 1. Mechanism
Completion genre (as KM02 to KM05): the model finalizes a started safety review. Scored failure is OMISSION, not propagation: the started review competently covers proximate fall factors and is silent on two deeper care gaps the chart supports; a model finalizing it tends to inherit that scope and miss them. Secondary failure is SCOPE DRIFT into cardiorenal restart sequencing or steroid taper, or over-attribution of fall risk to a non-primary cause. No cold axis needed.

## 2. Verified substrate (agent-read bytes)
Bone-health gap (central omission): osteoporosis/osteopenia M81.0 (H&P, problem list, PC baseline, reconciliation); years chronic/intermittent glucocorticoid exposure for PMR, endocrinology notes cumulative steroid bone consequences; alendronate 70 mg weekly NOT administered inpatient (MAR outpatient-chronic-reconcile), continuation/efficacy unverified; calcium 600 / vitD 400 IU BID "continued where tolerated" (low vitD total for a glucocorticoid patient, implies inconsistent administration); NO bone-density study anywhere (no DXA/T-score). The gap is the ABSENCE of surveillance, which the model must notice rather than read off a value.
Orthostatic-monitoring gap (second omission): nephrology ordered orthostatic vitals when feasible and noted orthostatic data not complete; endocrinology recommended orthostatic vitals as mobility advances. Recommendation + incompleteness both documented.
True contributing factors (anchors the model should get): orthostatic symptoms / BP reserve post-AKI (lightheadedness on standing, gabapentin held once for SBP 98 + lightheadedness); sedating med (gabapentin 300 mg nightly held/reduced selected days); deconditioning, gait/transfer impairment, Morse 65 unchanged; cognitive/medication-management errors; near-fall at home 05/17.
Scope-drift bait (secondary failure): cardiorenal restart sequencing and steroid taper are the hot complex axes documented at length; telemetry sinus rhythm without sustained ectopy so cardiac-syncope workup not supported; anemia at chronic baseline; infection resolving. A model pivoting the safety review onto these is drifting/over-attributing.

## 3. Draft prompt (terse, completion posture, safety-team voice)
We are doing the pre-discharge safety review for Korvin Merrow in 5W-318, flagged high fall and injury risk for the transition home. I started the review pulling his risk picture together and saved the draft. Finish it into a complete review for the safety committee, with the contributing factors and the care gaps we should close before he goes home.
Guidance: three sentences, completion posture, plain clinician/safety-team voice, no enumerated gaps, no format prescription, no hint of the bone-health or orthostatic gaps.

## 4. Mounted draft (the partial review the model finalizes)
Build note: clone the mount base, facility header + demographics, no invented encounter number, date 05/23/2026 (within stay). Competent on proximate causes, deliberately thin on deeper gaps; asserts no fabricated value and no false completeness claim, so the failure is omission not propagation. NOTE (Claude): the to-finalize line is written as plain prose (no brackets), per the KM05 bracket fix.

    MERCY VALE REGIONAL MEDICAL CENTER
    Pre-Discharge Patient Safety Review, Fall and Injury Risk
    Patient: Korvin Merrow   MRN: KM-6427819   DOB: 02/18/1964
    Unit: 5W-318   Review date: 05/23/2026   Status: DRAFT for completion

    Context
    Mr. Merrow is flagged high fall and injury risk for the transition home after hospitalization
    05/18 to 05/24/2026 for suspected urinary-source infection with sepsis physiology and AKI on
    CKD stage 3, on a background of HFrEF, CAD, type 2 diabetes, PMR on chronic prednisone, OSA,
    and anemia of CKD. Morse Fall Scale 65 (high risk), unchanged across the stay. Near-fall at
    home on 05/17 preceded admission. This review consolidates the risk picture for the safety
    committee.

    Contributing factors identified
    - Orthostatic symptoms and limited blood-pressure reserve during recovery from AKI;
      lightheadedness on standing documented.
    - Sedating medication: gabapentin held or reduced on selected days for sedation and fall-risk
      concern.
    - Deconditioning and limited endurance; gait and transfer impairment; supervised ambulation
      with mild unsteadiness.
    - Cognitive and medication-management errors noted during the stay.

    Care gaps and recommendations (to complete)
    - Rolling walker and supervised mobility for the early post-discharge period.
    - First-week in-home supervision arrangement to confirm with family.

    To finalize: complete the contributing factors and the care gaps and confirm the
    recommendations for the safety committee before filing.

What the draft omits (for Alexander, not in the mount): the bone-health and orthostatic-monitoring gaps are absent from the care-gaps section. The model's job is to complete the review; the omission failure is finalizing it without adding them.

## 5. Golden (strong physician completion; reference, not a script)
Build note: completed, signed safety review, facility header, focused not padded (length/scope drift IS the secondary failure). Flags the absence of bone-density surveillance; does not invent a DXA date/result.

    Contributing factors
    Orthostatic symptoms and limited blood-pressure reserve during recovery from AKI on CKD stage
    3, the primary physiologic driver; gabapentin as a sedating medication on the regimen, held or
    reduced for sedation and a documented orthostatic episode; deconditioning and limited endurance
    with gait and transfer impairment, Morse Fall Scale 65; cognitive slowing and medication-
    management errors that compound the risk; and the near-fall at home on 05/17. Telemetry showed
    sinus rhythm without sustained ectopy, so an arrhythmic or syncopal mechanism is not supported,
    and the lightheadedness is orthostatic and medication-related rather than cardiac.

    Care gaps and recommendations
    1. Bone health and fracture risk. This patient has glucocorticoid-associated osteoporosis from
       years of steroid exposure, yet no bone-density surveillance (DXA) or fracture-risk assessment
       is documented anywhere on file, calcium and vitamin D are under-optimized at 400 IU twice
       daily and given only where tolerated, and alendronate was not administered inpatient and its
       continuation and efficacy are unverified. Because a fall in this patient carries a heightened
       and currently unmitigated fragility-fracture risk, bone-health surveillance and optimization
       is an open care gap to address with rheumatology, endocrinology, and primary care.
    2. Orthostatic vital signs. Orthostatic vitals were recommended by nephrology and endocrinology
       but are documented as not consistently obtained; orthostasis is a primary fall driver, so
       measured orthostatic vitals should be obtained and acted on before or at discharge and the
       monitoring plan carried into follow-up.
    3. Mobility and supervision. Rolling walker and supervised mobility for the early period;
       bedside commode initially; grab bars; remove loose rugs. The first-week in-home supervision
       arrangement at medication times and overnight is not yet finalized and must be set with the
       family before discharge.
    4. Medication safety. Reinforce the pre-filled organizer and family verification for the
       cognitive and medication-management risk.

    Out of scope for this review: cardiorenal restart sequencing and the steroid taper are deferred
    to cardiology, nephrology, and rheumatology and are not fall-and-injury-risk items.

## 6. Grader (terse Sang structure; full text)
Matches current KM04 grader length/shape. Omission + scope-discipline mechanism, distinct from the other five; no trap reuse to acknowledge.

    Preamble
    This task asks the physician to finalize Korvin Merrow's pre-discharge fall and injury-risk
    safety review from the inpatient record so it is ready to file with the safety committee.
    Inputs: the 26-file chart plus the started review draft. Output: the completed review, graded
    against the golden golden-KM06-v1.docx.

    Register Note
    A physician and safety-committee-facing review; clinical shorthand and a structured layout are
    expected. Grade on clinical substance, completeness, and scope discipline, not prose polish or
    length.

    Section A. Must be present and correct
    The completed review must identify the true contributing factors: orthostatic symptoms and
    limited blood-pressure reserve post-AKI, gabapentin as a sedating medication, deconditioning
    with gait and transfer impairment and a high Morse score, cognitive and medication-management
    errors, and the near-fall at home. It must also identify two care gaps the record supports:
    first, the bone-health and fracture-risk gap, glucocorticoid-associated osteoporosis with no
    documented bone-density surveillance, under-optimized calcium and vitamin D, and unverified
    alendronate continuation, leaving fragility-fracture risk unmitigated if he falls; and second,
    the orthostatic-vitals monitoring gap, orthostatic vitals recommended by nephrology and
    endocrinology but not consistently obtained. It must keep scope on fall and injury risk and
    defer cardiorenal restart sequencing and the steroid taper to the respective teams. Use the
    golden for reasoning and stance, not fixed wording.

    Section B. Acceptable variation
    Accept prose, structured, or templated formats, including reuse of the draft's structure, as
    long as both care gaps are surfaced and the scope stays on fall and injury risk. Do not require
    fixed wording, and do not penalize true chart detail absent from the terse golden. Judge against
    the record, and do not credit fabricated specifics, an invented DXA date or result, a fabricated
    fall event, or invented orthostatic numbers.

    Section C. Patterns to reason about
    These are patterns to reason about, not items to tick off.
    Missed bone-health and fracture-risk gap (central). Watch for a review that completes the
    proximate fall factors but never identifies that this glucocorticoid-osteoporosis patient has no
    documented bone-density surveillance, under-optimized calcium and vitamin D, and unverified
    alendronate continuation, leaving fracture risk unmitigated. The chart documents the osteoporosis
    and steroid exposure, alendronate not given inpatient, and no DXA anywhere; missing this is the
    central scored failure.
    Missed orthostatic-vitals gap. Watch for a review that does not flag that orthostatic vitals,
    recommended by nephrology and endocrinology, were not consistently obtained, despite orthostasis
    being a primary driver.
    Scope drift or over-attribution. Watch for an excessively long review that drifts into the
    cardiorenal restart sequencing or the steroid taper as the focus, or that attributes the fall
    risk to a non-primary cause, a cardiac or syncopal workup despite clean telemetry, anemia at
    baseline, or resolving infection, rather than the orthostatic, sedating-medication, and
    deconditioning drivers.
    Non-responsiveness. Watch for a refusal to complete the review with no usable content; the
    deliverable is the finished review.
    Correct scope and completeness. Credit, do not dock, a focused review that names the true
    contributors and both care gaps and appropriately defers the cardiorenal and steroid management
    as out of scope.

## 7. Guidance so reviewers do not flag it again
Prompt: three sentences, completion posture, plain voice, no format prescription, correct grammar; matches KM03 to KM05. Grader: terse Sang structure at current KM04 length, no scoring bands, one or two named anchors, under a page; validate Section A against the prompt as well as the files. Golden: physician/safety-facing, focused not long (length is part of the failure), self-contained with every specific traceable to the chart, facility header, no invented DXA date/value, no invented event, no em dashes. House style across all three: no em/en dashes, no arrows, no asterisks. Mechanism: omission + scope discipline, distinct from the other five (strengthens suite mechanism diversity for AutoQC 2.99).

## 8. Build checklist
Mode A clone of mount base for draft + golden; facility header/demographics consistent; no invented encounter number. styles.xml byte-identical; fingerprint diff empty; metadata scrubbed. Char audit: em/en dashes, arrows zero; no asterisks; NO brackets (convert the to-finalize line to prose). Date audit: only 05/18 to 05/24/2026 + DOB; review dated 05/23/2026; no post-discharge dates, no fabricated event date. Golden filename matches grader's named string char-for-char. Re-verify on bytes at build: no bone-density study anywhere; alendronate not administered inpatient; calcium/vitD continued where tolerated; orthostatic vitals recommended but incomplete. Golden scores full under its own grader before staging. Justify Self-Contained AutoQC warning in writing if it fires.

## 9. Honest prediction and pilot
Depth least certain of the six. Bone-health/fall link is reasonably salient, so a strong model may catch the fracture-risk gap and push the task high; the two-gap design + completion framing are what give it a chance to bite. Honest range: mean high-60s to low-80s with a significant clinical failure on runs that miss the central gap, most likely clearing the pod-lead gate but not guaranteed sub-70. Read the pilot by whether failing runs miss the bone-health gap specifically and whether the grader credits catchers and stays focused. If all-high with no significant failure, fixes in order: (1) remove the alendronate-not-given cue from the draft context, (2) add a third buried gap, (3) tighten the scope penalty. Do not bank on the strength of the other tasks; pilot it.

## DEVIATION FLAG (Claude, 6/8) - needs Alexander decision
This packet reframes KM06 from the LOCKED canon. TP-KM06 (locked) is a +30 RETROSPECTIVE patient-safety/readmission-risk review (anchor 06/23/2026) with six risk domains and the steroid Endo-vs-Primary drama as the red herring (per Golden-KM06 / GG-KM06, both status CANDIDATE REVIEW). This packet is a PRE-DISCHARGE (05/23/2026, within-stay) fall-and-injury-risk committee review with two bone/orthostatic omissions + scope-drift. The reframe is defensible on difficulty grounds (a +30 retrospective invites the outcome-invention bright-line fail and the "+N boundary = free caution" problem the KM05 red-team flagged; pre-discharge keeps the omission mechanism cleaner). BUT it diverges from the locked source chain and FI-T06 ("Readmission-Risk Review Request Context"). Decision needed: re-scope KM06 to pre-discharge and update TP/EO/Golden/GG-KM06 + FI-T06 accordingly, or keep the locked +30 framing and rework the mechanism onto it.
                                                        
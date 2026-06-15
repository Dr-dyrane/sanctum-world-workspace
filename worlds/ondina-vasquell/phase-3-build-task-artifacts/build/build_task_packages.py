#!/usr/bin/env python3
"""Emit the text artifacts (prompt, grader, run-instructions, prereg) for OV02-OV10.

Goldens are built by build_goldens.py (canonical Epic template). Prompts are the spec
draft prompts (physician voice). Graders are Sang five-block, grounded in each task's
spec grader anchors and failure design. Prompt and grader are reviewer-drafted
candidates; golden dispositions are physician-owned. OV01 was authored by hand and is
consistent with this format.
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "platform"
TASKFILES = ROOT / "task-files"

# Each task's E1-T reference file travels WITH its task (uploaded with the task, never
# in the world-file set). Copy a fresh copy into platform/taskN/current/. task8 works
# off the world chart and has no task-level file.
TASK_FILE_MAP = {
    "task1": "discharge_medication_orders_05212026.docx",
    "task2": "him_final_coding_attestation_packet_05212026.docx",
    "task3": "cdi_query_memo_05232026.docx",
    "task4": "medicare_advantage_denial_letter_05232026.docx",
    "task5": "pharmacy_benefit_rejection_05242026.docx",
    "task6": "payer_concurrent_review_request_05252026.docx",
    "task7": "quality_abstraction_worksheet_06042026.docx",
    "task9": "safety_event_intake_summary_06112026.docx",
    "task10": "started_discharge_instruction_draft_05212026.docx",
}


def copy_task_files():
    for task, fname in TASK_FILE_MAP.items():
        src = TASKFILES / fname
        dst = BASE / task / "current" / fname
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src.exists():
            shutil.copyfile(src, dst)
            print("  taskfile", task, fname)
        else:
            print("  MISSING", task, fname)


# CANONICAL WORKFLOW MAP - single source of truth for the RLS Step-10 workflow per task,
# and the official record the spec and brainstorm adopt on any resubmit. Four originals
# were retired from the platform menu on 2026-06-13 (Ed/Abi) and are remapped to the
# nearest still-open workflow. Candidates are from the 2026-06-10 snapshot - VERIFY each
# exact name + priority on the LIVE Task Selection Categories sheet before selecting.
# Change a target here once and rebuild; never hardcode a workflow anywhere else.
WORKFLOW = {
    "task1":  dict(id="OV01", title="Discharge medication reconciliation", wf="Medication Reconciliation at Care Transitions", prio="P0",
                   retired="Discharge Medication Reconciliation (hca-discharge-med-recon)"),
    "task2":  dict(id="OV02", title="Inpatient coding attestation", wf="Inpatient Medical Coding and DRG Assignment", prio="P0", retired=None),
    "task3":  dict(id="OV03", title="CDI query response", wf="CDI-Coding DRG Reconciliation Review", prio="P1",
                   retired="CDI Query Response Review (hca-clinical-doc-improvement-query)"),
    "task4":  dict(id="OV04", title="Payer denial appeal", wf="Claims Denial Analysis and Appeal Preparation", prio="P0", retired=None),
    "task5":  dict(id="OV05", title="Pharmacy rejection response", wf="Pharmacy Insurance Claim Rejection Resolution", prio="P0", retired=None),
    "task6":  dict(id="OV06", title="Continued-stay determination", wf="Utilization Review Concurrent Stay Documentation", prio="P1", retired=None),
    "task7":  dict(id="OV07", title="Quality measure abstraction", wf="HEDIS Medical Record Chart Abstraction and Review", prio="P0", retired=None),
    "task8":  dict(id="OV08", title="Vascular referral", wf="Referral Intake/Triage", prio="P1",
                   retired="Specialist Referral Letter and Documentation Preparation (hca-specialist-referral-letter)"),
    "task9":  dict(id="OV09", title="Safety event review", wf="Patient Safety Indicator (PSI) Analysis and Reporting", prio="P2",
                   retired="Patient Safety Event Investigation and Root Cause Analysis (hca-patient-safety-event)"),
    "task10": dict(id="OV10", title="Discharge-instruction completion", wf="Medical Transcription and Clinical Documentation Completion", prio="P0", retired=None),
}


def wf_header(task):
    """KM-style '## Workflow type:' header block for a RUN-INSTRUCTIONS.md."""
    m = WORKFLOW[task]
    line = f"## Workflow type: {m['wf']} ({m['prio']})\n"
    if m["retired"]:
        line += (f"REMAPPED 2026-06-13: original workflow {m['retired']} was retired from the platform menu; "
                 "this is the nearest open analogue. Deliverable framing may need a light adjustment to fit it. ")
    line += "VERIFY the exact name and priority on the live Task Selection Categories sheet before selecting (candidate from the 2026-06-10 snapshot).\n\n"
    return line


def write_workflow_record():
    """Emit the official human-facing workflow record (generated from WORKFLOW)."""
    lines = [
        "# Ondina Vasquell - official workflow map (all artifacts)",
        "",
        "Single source: build/build_task_packages.py WORKFLOW. This is the canonical Step-10 workflow per task and the mapping the spec (Section 2) and brainstorm adopt if either is resubmitted. Four originals were retired from the platform menu on 2026-06-13 (Ed/Abi) and are remapped to the nearest open workflow. VERIFY every target on the LIVE Task Selection Categories sheet before use; candidates are from the 2026-06-10 snapshot.",
        "",
        "| Task | ID | Workflow to select | Priority | Status |",
        "|---|---|---|---|---|",
    ]
    for task in sorted(WORKFLOW, key=lambda t: int(t[4:])):
        m = WORKFLOW[task]
        status = f"REMAPPED (was {m['retired']})" if m["retired"] else "unchanged (open)"
        lines.append(f"| {task} | {m['id']} | {m['wf']} | {m['prio']} | {status} |")
    lines += [
        "",
        "Remapped: task1, task3, task8, task9. task8 and task9 swaps shift framing slightly; task1 and task3 are near-equivalent.",
        "",
        "ACTIVE SUITE = 10 tasks. OV02 (Inpatient Medical Coding and DRG Assignment) REVIVED 2026-06-14 and re-centered to v5 after v4 ceilinged. Current lever: KM09 final-packet signable-option trap, where the physician must select one foot-infection-principal pathway and remove the unsupported renal-failure pathway. Suite ORDER: OV01, OV07, OV03, OV04, OV05, OV06, OV08, OV09, OV10, OV02. Internal IDs/folders kept stable. Verified vs the 06/13 PDF Task Selection Tracker - all present; use EXACT names (OV08 = 'Referral Intake, Triage, and Scheduling Coordination'). Full guidance + suite order: reference/approved-workflows-and-guidance-2026-06-13.md and OV-WORLD-STATUS.md.",
        "",
    ]
    (ROOT.parent / "WORKFLOW-MAP.md").write_text("\n".join(lines), encoding="utf-8")
    print("  wrote WORKFLOW-MAP.md")


T = {
"task2": dict(id="OV02", dos="05/22/2026 0900", golden="golden-OV02-v1.docx", ver="v5",
  prompt="HIM sent over the final coding attestation packet on Mrs. Vasquell before the claim drops. Please prepare the single version I should sign for the chart and claim file: principal diagnosis, working DRG family, supported secondary diagnoses with present-on-admission status, and one-line rationales. Put it in a document I can sign, and give me a brief summary here.",
  context="Ondina Vasquell, a 68-year-old woman admitted 05/16/2026 with a limb-threatening left diabetic foot infection and an acute kidney injury on chronic kidney disease, is being coded before the claim drops. The deliverable is the physician's final coding attestation from the external HIM final coding attestation packet (E1-T2): one signable pathway with the principal diagnosis, working DRG family, supported secondary diagnoses with present-on-admission status, and one-line rationales. The packet carries both a renal-failure default pathway and a foot-infection alternate pathway.",
  must="The response must produce ONE final signable attestation, not a decision tree or a two-option packet. The limb-threatening diabetic foot infection is sequenced as the PRINCIPAL diagnosis, because under the inpatient rule the principal is the condition chiefly responsible for occasioning the admission and she was admitted for the foot infection. The HIM packet's Pathway A, acute kidney injury or acute renal failure as principal with the renal failure DRG, is removed or expressly rejected and must not remain signable. The acute kidney injury on chronic kidney disease is retained as a SECONDARY diagnosis. The working DRG is the diabetic foot infection or cellulitis family, NOT the renal failure family or its CC/MCC tier. Documented secondaries (diabetes with foot complication, chronic kidney disease stage 3b, anemia of chronic kidney disease, peripheral arterial disease) are retained. Present-on-admission status is assigned per documented onset.",
  acceptable="Line-by-line, short-table, or attestation format is acceptable. Exact code characters and the specific DRG number may be deferred to the coder and official guidelines. The graded point is the final attestation posture: one signable foot-infection-principal pathway, acute kidney injury as a secondary, and no signable renal-failure pathway. The response may mention the rejected HIM pathway for rationale, but it must not preserve it as an option for signature, a default, a pending choice, or a coder-selected alternate. Retaining or not naming a given supported secondary is acceptable if no unsupported code is added.",
  penalize="Leaving Pathway A, acute kidney injury or acute renal failure as principal, or the renal failure DRG family signable as an option, default, pending pathway, or HIM/coder choice. Recommending the diabetic foot infection pathway while still preserving the renal-failure pathway is still a central failure because the deliverable is final. Attesting the acute kidney injury or acute renal failure as the principal diagnosis, demoting the diabetic foot infection to a secondary, dropping documented supported comorbidities, or assigning present-on-admission by assumption rather than documentation are also failures.",
  restraint="Producing one final signable attestation, re-sequencing the diabetic foot infection as the principal diagnosis, retaining the acute kidney injury on chronic kidney disease as a secondary, removing or rejecting the renal failure pathway, and crediting the documented secondaries are correct attestation behaviors and should be credited not docked.",
  fairness="The task file is an external HIM final attestation packet, not the model's own same-author draft. A provider can fairly be asked to finalize one signable pathway and remove a coder-prepared alternate that the chart does not support as principal. This is the KM09 fairness route: the wrong pathway is external, chart-contradicted, and rebuttable from the mounted record.",
  mechanism="FINAL-PACKET signable-option trap (KM09 floor shape, AKI substrate, de-duplicated from KM09 sepsis and OV03 osteo). The external HIM packet contains Pathway A, acute kidney injury on chronic kidney disease as principal with a renal failure DRG, and Pathway B, foot infection as principal. The physician must finalize ONE signable attestation, choosing the foot-infection-principal pathway and removing Pathway A. Central failure = preserving the unsupported acute kidney injury principal or renal failure DRG as a signable option, default, pending pathway, or HIM/coder choice, even if the response recommends the diabetic foot infection pathway. This targets the KM09 failure mode: hedging or option-carrying inside a final physician coding attestation.",
  forecast="Bimodal. Floor target 0.30 to 0.55 if the model recommends the foot-infection pathway but leaves the renal-failure pathway available for signature or coder choice, or signs renal failure outright. Catcher above 0.85 if it produces one final attestation with foot infection as principal, acute kidney injury secondary, renal pathway removed, and supported secondaries retained. Mean target 55 to 78. FA/GA on the 2nd-lowest run (DO-NOT-REPEAT #20)."),

"task3": dict(id="OV03", dos="05/24/2026 1000", golden="golden-OV03-v1.docx",
  prompt="CDI sent over a query on Mrs. Vasquell. Please draft my response as the attending. Go item by item against the chart and make the clinical reasoning explicit so the record stands on its own.",
  context="A clinical documentation query asks the attending to document acute osteomyelitis given the MRI marrow edema. The deliverable is an item-by-item attending response, agreeing where the record supports it and declining on clinical grounds where it does not. Sources are the full chart and the external CDI query memo (E1-T3).",
  must="Acute osteomyelitis is declined on clinical grounds with explicit reasoning, not a bare or procedural decline: the treating team characterized a deep soft tissue infection, the MRI is equivocal, the specimen has no bone, and infectious disease did not sign osteomyelitis. The reasoning is anchored on the treating team's own documentation. Genuinely supported clarifications (laterality, diabetic foot infection specificity) are accepted.",
  acceptable="Item-by-item prose or numbered format. Accepting supported clarifications is correct and expected. Wording differences are not errors. The response may engage the marrow-edema indicator directly or by characterizing it as reactive change.",
  penalize="Agreeing to add acute osteomyelitis. A bare or procedural decline with no clinical reasoning. Anchoring the decline only on ancillary observations rather than the treating assessment. Over-correcting by declining a genuinely supported item. Treating the reflect-full-severity framing as a license to add an unestablished diagnosis.",
  mechanism="Documentation-integrity judgment, reasoned clinical decline in the treating voice. Central failure = adding acute osteomyelitis under query pressure, or declining without clinical reasoning.",
  forecast="Mean roughly 72 to 86. Floors 0.30 to 0.55 (adding osteomyelitis is the central failure). Expect 2 to 4 of 10 runs to add the diagnosis or to decline without reasoning."),

"task4": dict(id="OV04", dos="05/24/2026 1500", golden="golden-OV04-v1.docx",
  prompt="The plan denied SNF for Mrs. Vasquell and case management asked me to appeal. Draft the appeal letter for my signature. Make the clinical case from the chart for the level of care she needs, and keep it tight and clinical.",
  context="A Medicare Advantage plan denied skilled nursing facility authorization, framing improving infection markers as home readiness. The deliverable is a physician appeal letter with a clear position and clinical rationale. Sources are the full chart (physical and occupational therapy, vascular study and consult, wound care, case management) and the external denial letter (E1-T4).",
  must="The appeal rebuts the improving-markers-equal-home framing by synthesizing the unresolved perfusion study, the frequency and skill of required wound care, the physical and occupational therapy findings on offloading and stairs, the second-floor walk-up, the night-working caregiver, and infection-relapse risk. Perfusion uncertainty is cited from the formal vascular study, not a reassuring pulse. The treating position is held rather than over-deferring to the payer.",
  acceptable="Letter structure and ordering may vary. The offloading device may be cited as supporting evidence. Emphasis among the functional, perfusion, wound, and home factors may vary as long as the synthesis is multi-source. Wording differences are not errors.",
  penalize="Accepting that improving markers equal home readiness. Over-deferring to payer authority. Reading perfusion as adequate from a bedside pulse rather than the noncompressible study. Omitting the offloading, stairs, or home and caregiver limits. Resting the entire appeal on the offloading device alone.",
  mechanism="Multi-source synthesis into a binding appeal, the world integration anchor. Central failure = adopting the payer's stability-equals-readiness frame or resting on a single thread.",
  forecast="Mean roughly 72 to 86. Floors 0.35 to 0.55 (a single-thread appeal or over-deference). Expect 2 to 4 of 10 runs to under-synthesize."),

"task5": dict(id="OV05", dos="05/25/2026 0900", golden="golden-OV05-v1.docx",
  prompt="The PBM kicked back the antibiotic we want to send Mrs. Vasquell home on and is pushing their preferred agent. Look at her chart and tell me how to respond, whether we substitute, appeal, hold, or file an exception, and why.",
  context="A pharmacy benefit manager rejected the planned discharge antibiotic and offered formulary-preferred substitutes. The deliverable is the prescriber response choosing among substitute, appeal, hold, or exception with rationale. Sources are the full chart (renal trend, cultures, allergy, infectious disease plan) and the external rejection notice (E1-T5).",
  must="The formulary-preferred substitute is declined with the specific reason: trimethoprim-sulfamethoxazole is contraindicated by the documented sulfa allergy, and an oral fluoroquinolone is not culture-directed and carries renal and other cautions. A renally appropriate, allergy-safe, culture-directed alternative or a formulary-exception appeal is proposed. Dosing reflects current renal function. The deep-tissue culture is used rather than the superficial swab.",
  acceptable="Proposing a specific safe alternative or a formulary exception are both acceptable. Exact agent and dose may be deferred to infectious disease confirmation. Format may vary. Wording differences are not errors.",
  penalize="Accepting the unsafe formulary substitute. Overlooking the sulfa allergy. Carrying admission renal dosing forward. Letting the superficial swab drive the choice. Choosing to hold effective therapy when a safe alternative or exception is available.",
  mechanism="Medication-safety judgment against an administrative substitution pressure. Central failure = accepting the sulfa-containing or non-culture-directed substitute, or missing the allergy or renal dosing.",
  forecast="Mean roughly 72 to 86. Floors 0.30 to 0.50 (accepting the sulfa substitute is a patient-safety failure). Expect 2 to 4 of 10 runs to accept the substitute or miss the allergy."),

"task6": dict(id="OV06", dos="05/26/2026 1100", golden="golden-OV06-v1.docx",
  prompt="As physician advisor, give me a continued-stay determination on Mrs. Vasquell for today. Walk the criteria, state your decision clearly, and base it on what the chart actually shows about whether she is safe to step down.",
  context="A physician advisor must render a continued-stay determination on a designed borderline. The deliverable is an explicit verdict with criteria-based rationale. Sources are the full chart and the external concurrent-review request (E1-T6), which is the prompt to determine, not the answer.",
  must="A binding determination is stated. Both the improvement (afebrile, normalized white count, improved creatinine) and the unresolved operational criteria (unresolved perfusion, skilled wound-care frequency, unsafe offloading and home environment) are weighed. The verdict rests on documented function and perfusion, finding continued skilled-level need justified, not on markers alone.",
  acceptable="Determination format may vary. The reasoning may lead with either side as long as both are weighed. Wording differences are not errors.",
  penalize="Reading improvement as discharge readiness. Avoiding or hedging the verdict. Applying criteria to only one side. Treating perfusion as resolved. Treating the external concurrent-review request as the answer rather than the prompt.",
  mechanism="A binding level-of-care determination on a designed borderline. Central failure = a discharge-ready verdict from improvement alone, or a hedge with no binding determination.",
  forecast="Mean roughly 70 to 84. Floors 0.35 to 0.55 (a step-down verdict from markers alone). Expect 2 to 5 of 10 runs to read improvement as readiness."),

"task7": dict(id="OV07", dos="06/04/2026 0900", golden="golden-OV07-v1.docx",
  prompt="Quality sent over the diabetes measure abstraction on Mrs. Vasquell for my sign-off. Before I sign, go through it against her chart and tell me whether I can sign it as written or what I need to correct. For each measure, state what the record actually supports: the value or finding, an exclusion, or that the documentation cannot support it, with a short why. Flag anything you need me to confirm first. Put your attestation in a saved document I can sign, and give me a brief summary here. Use plain clinical punctuation in both the document and summary; do not use em dashes or en dashes.",
  context="Ondina Vasquell's preliminary diabetes quality-measure abstraction worksheet, prepared by the quality department, is sent to the attending physician for review and sign-off. The worksheet proposes values for five fields, including an HbA1c of 8.6 percent dated to the outpatient-summary note date. The deliverable is the physician's attestation, one value, exclusion, or unable-to-determine per measure field, in the physician's voice acting in a medical-director quality-review capacity. Sources are the outpatient summary, the eye-exam result, the labs, and the renal record, plus the external quality-department abstraction worksheet (E1-T7).",
  must="The preliminary worksheet is corrected rather than signed as written. The most recent HbA1c value may be reported as 8.6 percent, but its DATE is marked unable to determine, because the 04/30/2026 date on the worksheet is the outpatient note date, not a lab draw date, and the record documents only a last A1c with no draw date. The glycemic numerator is NOT forced. The dilated eye exam (03/15/2026, mild non-proliferative retinopathy) is credited as documented and dated, without over-reading the retinopathy. The foot exam (reduced protective sensation, monofilament) and the nephropathy evidence (CKD stage 3b on an ACE inhibitor; no discrete urine albumin-creatinine result) are abstracted to the documented evidence. The most recent documented blood pressure is reported. No numerator is forced past a missing date or exclusion.",
  acceptable="Field format may vary. Reporting the HbA1c value while marking its date unable to determine is correct, not a miss. Stating that the preliminary worksheet cannot be signed as written because 04/30/2026 is only the source-note date is correct. Crediting the dated 03/15/2026 eye exam is correct. Marking a field unable to determine where the record is genuinely insufficient is correct.",
  penalize="Signing the preliminary worksheet as written. Treating the outpatient-summary note date of 04/30/2026 as the HbA1c draw date. Forcing the glycemic numerator by treating the undated last A1c of 8.6 percent as a dated in-period result (the central failure). Over-reading the mild retinopathy beyond the measure definition. Forcing any numerator the record does not date or support. Inventing an A1c draw date or a urine albumin-creatinine result not in the record.",
  ver="v3",
  restraint="Reporting the HbA1c value of 8.6 percent while marking its date unable to determine, declining to force the glycemic numerator on an undated result, not inventing a urine albumin-creatinine result or an A1c draw date, and crediting the dated 03/15/2026 eye exam as documented, are correct abstraction behaviors and should be credited not docked.",
  fairness="The task file is an external quality-department worksheet, not a same-author draft. The worksheet makes a realistic abstraction error by using a source-note date as the HbA1c result date. Correcting the worksheet is licensed by the sign-off request and rewarded; propagating the 04/30/2026 A1c date invents a material quality-measure fact.",
  mechanism="Review-and-signoff of an external preliminary worksheet with a cold verification-asymmetry plant. The worksheet asserts HbA1c 8.6 percent on 04/30/2026, but the chart only carries an undated last A1c and 04/30/2026 is the outpatient note date. Central failure = signing or carrying the worksheet's 04/30/2026 HbA1c date and forcing the glycemic numerator. Secondary = over-reading the retinopathy, or forcing a field the record does not support.",
  forecast="Mean roughly 58 to 78, bimodal. Central failure = carrying the worksheet's false 04/30/2026 A1c date into a signable attestation. Design target: a floor-worthy material miss landing 0.30 to 0.55 with at least one catcher above 0.85; expect a real sub-60 on runs that rubber-stamp the Quality worksheet. Bank a legitimate material miss, not file-output noise."),

"task8": dict(id="OV08", dos="06/08/2026 1400", golden="golden-OV08-v1.docx",
  prompt="I am sending Mrs. Vasquell to vascular surgery for the perfusion question. Draft the referral letter for my signature, and include the disposition table for source control, perfusion, antibiotics, offloading, and follow-up so they can see exactly what is open.",
  context="A vascular surgery referral letter is needed with a required disposition table. The deliverable is the letter plus a table covering source control, perfusion, antibiotics, offloading, and follow-up. Sources are the full chart.",
  must="The disposition table is present and each status is accurate, with perfusion and any pending item kept open. The narrative does not assert resolution the chart does not support. The referral asks the genuinely open perfusion and revascularization questions.",
  acceptable="Letter structure may vary. The table may carry extra accurate rows. Wording differences are not errors as long as the open items remain open.",
  penalize="A pleasant narrative that implies the case is settled. Writing perfusion as resolved. Omitting or collapsing the disposition table. Overstating the offloading status. Misstating the antibiotic course.",
  mechanism="From-scratch synthesis with an embedded forced disposition table. Central failure = a narrative that closes perfusion or other open items the table should keep open.",
  forecast="Mean roughly 74 to 88. Floors 0.40 to 0.60 (perfusion written as resolved or the table collapsed). Expect 2 to 4 of 10 runs to close an open item."),

"task9": dict(id="OV09", dos="06/11/2026 1000", golden="golden-OV09-v1.docx",
  prompt="We had a missed-offloading event on Mrs. Vasquell and I need a root cause review. Go through what the chart shows about how it happened, give me your attribution, and lay out prevention steps.",
  context="A missed-offloading event requires a root-cause review. The deliverable is a structured review with an attribution and prevention finding. Sources are the full chart (therapy, order, device, and home-layout documentation) and the safety-event intake (E1-T9).",
  must="Attribution is multifactorial and system-level (order, teaching and teach-back, device availability, and home-layout factors), not single-person blame. The prevention plan maps to the documented contributors. The review engages the chart rather than asserting a cause.",
  acceptable="Review structure may vary. Emphasis among the contributors may vary as long as the attribution stays multifactorial. Wording differences are not errors.",
  penalize="Framing the event as patient nonadherence. A single-cause conclusion. Generic prevention not tied to the contributors. Missing the offloading teach-back failure. Missing the device-availability or order contributors.",
  mechanism="Investigation with a system-versus-individual attribution judgment. Central failure = blaming the patient or concluding a single cause.",
  forecast="Mean roughly 74 to 88. Floors 0.40 to 0.60 (patient-blame attribution). Expect 2 to 4 of 10 runs to blame the patient or go single-cause."),

"task10": dict(id="OV10", dos="05/22/2026 1000", golden="golden-OV10-v1.docx", ver="v2",
  prompt="Mrs. Vasquell is going home. Please finish her discharge instructions from the chart so they are ready to give her, put them in a document I can sign, and give me a brief summary here.",
  context="A started discharge-instruction draft is complete except for the ACTIVITY section, which the resident left as a placeholder for the discharging clinician. The deliverable is the finalized patient-facing discharge instructions. Sources are the full chart and the started draft (E1-T10). The prompt does NOT point at the activity section.",
  must="The activity section is completed from the chart with the documented STRICT OFFLOADING restriction and supervised, limited-activity plan: keep weight off the left forefoot, use the offloading device when standing or walking, supervised short distances only, stairs not yet safe alone. It is NOT a routine activity clearance. Items the chart leaves open (final antibiotic, follow-up appointments still being arranged) are left open, not asserted as completed or scheduled. The rest of the draft is finalized faithfully.",
  acceptable="Plain-language patient phrasing may vary, and an activity or foot-care section heading is fine. Providing the instructions in Spanish is appropriate. Noting that items still being arranged remain open is correct. Wording differences are not errors.",
  penalize="Filling the activity section with a routine clearance (resume activity as tolerated, return to normal activity, weight-bear as comfortable) or any advice that contradicts the documented strict-offloading restriction. Asserting a still-open item (final antibiotic, follow-up) as closed or scheduled. Altering draft content beyond the placeholder.",
  restraint="Completing the activity section with the documented offloading restriction and supervised plan, and leaving genuinely open items (final antibiotic, follow-up) as pending rather than inventing a closure, are correct discharge-completion behaviors and should be credited not docked.",
  mechanism="Completion of a started discharge draft with a true placeholder on the ACTIVITY section, and the prompt does NOT point at it (de-hinted). Central failure = filling the activity section with routine activity clearance, the templated discharge default, which directly contradicts the documented strict-offloading restriction and would put weight on a limb-threatening forefoot wound. This is a MATERIAL patient-safety failure, not a one-of-many deduction. It is commission on the model's boilerplate discharge default (against the documented restriction), embedded in the draft the model finalizes; the offloading evidence is in the PT, OT, wound-care, podiatry, and nursing-offloading notes. A catcher fills with the offloading restriction; a floor normalizes.",
  forecast="Bimodal (floor canon: floor 0.15-0.40 with a catcher above 0.85). Floor = routine-clearance or normalized activity fill (the templated default), scored as a critical safety failure. Catcher = documented offloading restriction and supervised plan, open items left open. Mean roughly 60 to 80; target at least one sub-60 normalization. FA/GA on the 2nd-lowest run (DO-NOT-REPEAT #20)."),
}


# Per-task deliverable label + anchor items (named consistently across the five
# scoring bands, per AutoQC Section 6 v6.6 checks 6.7, 6.11, 6.12).
AUX = {
 "OV01": ("discharge medication reconciliation", "the discontinuation of the carried-forward inpatient enoxaparin VTE prophylaxis, the renal-current antibiotic dose, the three held agents as explicit deferred restarts, and NSAID avoidance"),
 "OV02": ("coding attestation", "one final signable foot-infection-principal pathway, acute kidney injury as secondary, the renal-failure pathway removed, and the retained documented comorbidities"),
 "OV03": ("CDI query response", "acute osteomyelitis declined on clinical grounds anchored to the treating assessment, with genuinely supported clarifications accepted"),
 "OV04": ("appeal letter", "the multi-source rebuttal of improving-markers-equal-home: unresolved perfusion, skilled wound-care need, the offloading and stairs limits, and the home and caregiver constraints"),
 "OV05": ("prescriber response", "the sulfa-allergy and non-culture-directed substitute declined, a renally dosed allergy-safe culture-directed alternative or formulary exception, current renal dosing, and the deep culture over the swab"),
 "OV06": ("continued-stay determination", "a binding verdict weighing improvement against unresolved perfusion, skilled wound-care frequency, and unsafe offloading and home environment, finding continued skilled-level need"),
 "OV07": ("measure abstraction", "the quiet lookback or exclusion that changes capture, each field valued or excluded or marked undetermined per the record, and no forced numerator"),
 "OV08": ("vascular referral letter", "the disposition table with perfusion and pending items kept open, and a narrative that asserts no resolution the chart lacks"),
 "OV09": ("root-cause safety review", "a multifactorial system-level attribution across order, teaching and teach-back, device availability, and home layout, with prevention mapped to the contributors"),
 "OV10": ("discharge instructions", "the offloading and activity section completed from the documented restriction and supervised plan, nothing chart-open closed, and the rest finalized faithfully"),
}

# OV01 grader fields (OV01 prompt/run-instructions are hand-authored; only its grader
# is regenerated here so all ten graders share the v6.6 A/B/C + five-band format).
OV01_GRADER = dict(id="OV01", golden="golden-OV01-v1.docx",
  context="Ondina Vasquell, a 68-year-old woman admitted 05/16/2026 with a limb-threatening left diabetic foot infection, is being reconciled for discharge. The deliverable is a physician discharge medication reconciliation, a clean current renally appropriate medication list with an explicit decision on each held agent. Sources are the full chart (home medication list, MAR, renal trend, infectious disease and pharmacy notes) and the external unreconciled discharge order set (E1-T1).",
  must="The inpatient enoxaparin VTE prophylaxis carried forward in the order set is discontinued at discharge; it is an inpatient-only prophylactic agent, not a home medication, and continuing it adds bleeding risk on aspirin and clopidogrel. Antibiotic dosing reflects current renal function, not the admission peak. Metformin, empagliflozin, and lisinopril are recorded as explicit deferred restarts with reasons, not silently resumed or discontinued. Acetaminophen is retained and no NSAID is introduced. Home insulin is continued. The discharge antibiotic plan is renally dosed and deep-culture-directed.",
  acceptable="List or short-table format is acceptable. The exact discharge antibiotic agent and final dose may be deferred to infectious disease confirmation. Restart timing may be expressed as a parameter-gated plan. Reasonable wording differences are not errors.",
  penalize="Continuing the carried-forward inpatient enoxaparin VTE prophylaxis at discharge. Carrying admission antibiotic dosing forward. Silently resuming or discontinuing a held oral agent. Introducing an NSAID. Letting the superficial swab drive the antibiotic choice. Failing to record the held agents as explicit decisions.",
  mechanism="Source-of-truth reconciliation under renal constraint with a cold carried-forward item. Central failure = continuing the carried-forward inpatient VTE prophylaxis (enoxaparin) at discharge, or carrying admission antibiotic dosing forward, or silently resuming or discontinuing a held agent.")


SELFQC = (
    "## Self-QC before RLS upload (CANONICAL, run every time)\n"
    "Before Step 10 upload, run the writer-edition AutoQC in claude.ai against this task's deliverables, one per upload: Section 4 (Task Prompt) with the temporal-anchoring gate FIRST, then Section 5 (Golden Response), then Section 6 (Grader Guidelines). Upload each deliverable together with its AutoQC file; every numbered check must be PASS or a justified N/A before upload. The grader must be the KM five-block that passes the live gate (Preamble, Register Note, Section A Must be present and correct, Section B Acceptable variation with the verbatim two-failure-mode clause, Section C Patterns to reason about with the correct-restraint credit), with NO scoring bands and no closing format disclaimer line. Fix locally and rerun until clean. Do NOT rely on the live RLS AutoQC to catch format issues.\n\n"
)


def grader_v66(idd, dd):
    """KM five-block grader, the format passing the live Task AutoQC as of 2026-06-13:
    Preamble, Register Note, Section A (Must be present and correct), Section B
    (Acceptable variation + the verbatim two-failure-mode clause), Section C (Patterns
    to reason about + the verbatim opener + a correct-restraint credit). NO scoring
    bands (they trip No Weight Distribution on the live gate), no format disclaimer,
    no dashes or asterisks."""
    m = dd["mechanism"]
    central = m.split("Central failure =")[-1].strip().rstrip(".") if "Central failure =" in m else "the central failure"
    two_fail = ("Two failure modes to watch for: (1) the model lists findings, doses, provider names, "
                "or other specifics not in the golden and not covered by accepted alternatives; (2) the "
                "model invents plausible clinical details absent from the source material.")
    parts = [
      "Preamble\n\n" + dd["context"] + f" The deliverable is graded against the uploaded golden, {dd['golden']}.",
      "Register Note\n\nThis is a physician-facing document; grade on clinical substance and fidelity to the documented record, not on prose polish, length, or formatting. With include_input_files=true, verify any specific (a dose, date, lab value, organism, or name) against the mounted record before treating it as invented, and credit chart-supported detail even when the terse golden omits it.",
      "Section A. Must be present and correct\n\n" + dd["must"],
      "Section B. Acceptable variation\n\n" + dd["acceptable"] + " Use the golden as your reference for supported reasoning. " + two_fail,
      "Section C. Patterns to reason about\n\nThese are patterns to reason about, not items to tick off.\n\n" + dd["penalize"] + f" The central failure to watch for is {central}.\n\nCorrect restraint, to credit not penalize. " + dd.get("restraint", "Keeping a genuinely open item (perfusion, osteomyelitis, a pending arrangement, or a deferred restart) open or routed to the right owner, rather than forcing a false resolution, is correct and should be credited not docked."),
    ]
    text = "\n\n".join(parts)
    for a, b in ((f" {chr(0x2014)} ", ", "), (f" {chr(0x2013)} ", ", "), (" - ", ", "), ("*", "")):
        text = text.replace(a, b)
    return text + "\n"


def emit():
    for task, d in T.items():
        out = BASE / task / "current"
        out.mkdir(parents=True, exist_ok=True)
        i = d["id"]
        ver = d.get("ver", "v1")
        (out / f"prompt-{i}.txt").write_text(d["prompt"] + "\n", encoding="utf-8")
        (out / f"grader-guidelines-{i}.txt").write_text(grader_v66(i, d), encoding="utf-8")
        (out / "RUN-INSTRUCTIONS.md").write_text(
            f"# platform/{task}/current - {i} {ver}\n\n"
            "Prompt and grader are reviewer-drafted candidates; the golden dispositions are physician-owned and must be confirmed by Alexander before any pilot.\n\n"
            + wf_header(task) +
            f"## Mechanism under test\n{d['mechanism']}\n\n"
            "## Mounted set\n- Shared world chart (world-files/ plus supplementary-files/).\n"
            f"- Task-level file for this task (E1-T). Upload and confirm UPLOADED, not staged, before AutoQC; confirm no filename collision with a world file.\n"
            "- Grader is chart-aware (include_input_files true): true chart specifics are credited, not flagged invented.\n\n"
            "## Fairness\n" + d.get("fairness", "Every planted pressure is contradicted by the chart, so correcting it is rewarded and propagating it is a real clinical error. The contradicting evidence is not hidden and the correct restraint is not docked.") + "\n\n"
            + SELFQC +
            "## RLS entry (save after every step)\nWorkflow type = " + WORKFLOW[task]["wf"] + " (verify on the live Task Selection Categories sheet). 1.2 prompt-" + i + ".txt. 1.3 upload the task file, Save File Changes, refresh, confirm UPLOADED. 1.4 golden " + d["golden"] + " and grader grader-guidelines-" + i + ".txt; confirm the grader names the golden by filename. Save Changes, refresh, run Task AutoQC (rerun N failing once), 2.2 note, run Trajectories.\n\n"
            "## Expectation\nSee " + i + "-" + ver + "-pilot-preregistration.md for the locked forecast and read rules.\n", encoding="utf-8")
        pre = out / f"{i}-{ver}-pilot-preregistration.md"
        if not pre.exists():  # never clobber a hand-authored (e.g. re-centered) prereg
            pre.write_text(
            f"# {i} {ver} PILOT PREREGISTRATION - locked before upload, AutoQC, and pilot\n"
            "Rule: this file does not change after the pilot lands. Post-pilot reconciliation goes in a results record citing this file.\n\n"
            f"## Mechanism under test\n{d['mechanism']}\n\n"
            "## Base rates\nOndina task; nearest analogue is the prior world's same-structure task. No in-world base rate.\n\n"
            f"## Forecast\n{d['forecast']}\n\n"
            "## Read rules (set now)\n- A floor exhibits the central failure named above; a catcher avoids it and engages the chart.\n"
            "- Deferring a genuinely physician-owned specific to the named follow-up is a catcher behavior, not a miss.\n"
            "- 2nd-lowest % run = failure-analysis subject (King P 2026-06-14, DO-NOT-REPEAT #20, not the lowest); cleanest catcher = grader-analysis anchor. Failure-only, no section names.\n", encoding="utf-8")
        print("  package", i)
    (BASE / "task1" / "current" / "grader-guidelines-OV01.txt").write_text(
        grader_v66("OV01", OV01_GRADER), encoding="utf-8")
    print("  package OV01 grader (v6.6)")
    copy_task_files()
    write_workflow_record()
    print("done; OV02-OV10 text artifacts emitted + task files placed in each task folder")


# OV02 (coding attestation) RETIRED 2026-06-14 - model-strong genre, ceilinged x3 (v1/v2/v3).
# Source entries kept above for possible commitment-trap revival; popped here so the active
# suite is 9 tasks and rebuilds do not resurrect platform/task2.
for _ret in ("task2",):  # OV02 RE-RETIRED 2026-06-14: coding genre model-strong, ceilinged x5 (v1-v5)
    T.pop(_ret, None); WORKFLOW.pop(_ret, None); TASK_FILE_MAP.pop(_ret, None)

if __name__ == "__main__":
    emit()

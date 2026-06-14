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
    "task1": "preliminary_discharge_order_set_05212026.docx",
    "task2": "him_preliminary_coding_worksheet_05212026.docx",
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
        "Remapped: task1, task3, task8, task9. task8 and task9 swaps shift framing slightly; task1 and task3 are near-equivalent. The other six are unchanged and were not on the retired list.",
        "",
    ]
    (ROOT.parent / "WORKFLOW-MAP.md").write_text("\n".join(lines), encoding="utf-8")
    print("  wrote WORKFLOW-MAP.md")


T = {
"task2": dict(id="OV02", dos="05/22/2026 0900", golden="golden-OV02-v1.docx",
  prompt="This is the preliminary coding worksheet on Mrs. Vasquell before we finalize. Go through the chart and give me your attestation line by line, principal diagnosis, present on admission, and the code families you support.",
  context="Ondina Vasquell, a 68-year-old woman admitted 05/16/2026 with a limb-threatening left diabetic foot infection, is being coded before the claim drops. The deliverable is a physician coding attestation responding to the preliminary health-information worksheet, one line per diagnosis with principal diagnosis, present-on-admission status, and supported code family. Sources are the full chart and the external preliminary coding worksheet (E1-T2), which is severity-forward.",
  must="The diabetic foot ulcer with deep soft tissue infection or cellulitis family is selected as principal, supported by the ED, podiatry, and wound notes. Acute osteomyelitis is NOT attested as established or present on admission, because the imaging is equivocal, the debrided specimen contains no bone, and infectious disease did not sign it. The pressure-injury family is not coded. Documented diabetes, chronic kidney disease with acute kidney injury, anemia, and peripheral arterial disease are retained. Present-on-admission status is assigned per documented onset.",
  acceptable="Line-by-line or short-table format is acceptable. Exact code characters and final sequencing may be deferred to the coder and official guidelines. Retaining or not naming a given supported secondary code is acceptable if no unsupported code is added. Reasonable wording differences are not errors.",
  penalize="Selecting the pressure-injury family for this neuropathic and ischemic diabetic foot ulcer. Attesting acute osteomyelitis as established or present on admission. Upcoding to an unsupported severity tier or DRG. Dropping documented supported comorbidities. Assigning present-on-admission by assumption rather than documentation.",
  mechanism="Forced-inventory coding judgment under documented uncertainty. The external worksheet steers toward a pressure-injury family and acute osteomyelitis present on admission; the chart supports neither. Central failure = adopting the worksheet's pressure-injury or osteomyelitis-POA framing.",
  forecast="Mean roughly 70 to 85. Floors 0.30 to 0.55 (attesting osteomyelitis POA or a pressure-injury principal is one central wrong line). Expect 2 to 5 of 10 runs to adopt at least one worksheet-steered code."),

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
  prompt="Please complete the diabetes measure abstraction on Mrs. Vasquell. Fill each field from the chart, and mark exclusions or unable to determine where the documentation calls for it.",
  context="A diabetes quality-measure abstraction must be completed from the record. The deliverable is one value, exclusion, or unable-to-determine per field. Sources are the outpatient summary, the eye-exam result, the labs, and the renal record, plus the abstraction worksheet (E1-T7).",
  must="The measure logic is applied honestly. The quiet lookback-window or exclusion detail that changes capture is caught and applied. Fields are valued, excluded, or marked unable to determine per the record. The HbA1c, dilated eye exam, foot exam, and nephropathy fields are abstracted to the documented evidence. No numerator or denominator is forced.",
  acceptable="Field format may vary. Marking a field unable to determine where the record is genuinely insufficient is correct, not a miss. Naming the exact measurement-year window for the abstractor to confirm is acceptable.",
  penalize="Missing the quiet lookback or exclusion that changes capture. Forcing a numerator the record does not support. Over-reading the mild retinopathy finding beyond the measure definition. Flattening the HbA1c value or date window. Missing the documented nephropathy evidence.",
  mechanism="Extraction-to-schema with a quiet disqualifier. Central failure = missing the lookback or exclusion detail and forcing capture.",
  forecast="Mean roughly 68 to 82. Floors 0.30 to 0.55 (a forced numerator past a missed exclusion). Expect 3 to 5 of 10 runs to miss the quiet detail."),

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

"task10": dict(id="OV10", dos="05/22/2026 1000", golden="golden-OV10-v1.docx",
  prompt="I started Mrs. Vasquell's discharge instructions but left the activity and foot-offloading part open. Please finish the document from her chart, fill in that section with what she should actually be doing for the foot, and leave anything that is still undecided as undecided.",
  context="A started discharge-instruction draft is complete except for the offloading and activity section, left as a true placeholder. The deliverable is the finalized patient-facing instructions. Sources are the full chart and the started draft (E1-T10).",
  must="The offloading and activity section is completed from the chart with the documented offloading restriction and supervised plan, not a routine clearance. Nothing the chart leaves open is closed. The rest of the draft is finalized faithfully.",
  acceptable="Plain-language patient phrasing may vary. Noting that items still being arranged remain open is correct. Providing the instructions in Spanish is appropriate. Wording differences are not errors.",
  penalize="Filling the placeholder with a routine activity clearance. Asserting a still-open decision as closed. Altering draft content beyond the placeholder. Softening the documented home-safety reality. Activity advice that contradicts the wound and offloading plan.",
  mechanism="Completion with a true placeholder on the scored decision. Central failure = a routine-clearance fill or closing an open decision.",
  forecast="Mean roughly 72 to 86. Floors 0.35 to 0.55 (routine-clearance fill). Expect 2 to 4 of 10 runs to fill with a routine clearance."),
}


# Per-task deliverable label + anchor items (named consistently across the five
# scoring bands, per AutoQC Section 6 v6.6 checks 6.7, 6.11, 6.12).
AUX = {
 "OV01": ("discharge medication reconciliation", "the renal-current antibiotic dose, the three held agents recorded as explicit deferred restarts, NSAID avoidance, and the deep-culture-directed plan"),
 "OV02": ("coding attestation", "the diabetic-foot-infection family as principal, acute osteomyelitis not attested as established or present on admission, no pressure-injury family, and the retained documented comorbidities"),
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
  must="Antibiotic dosing reflects current renal function, not the admission peak. Metformin, empagliflozin, and lisinopril are recorded as explicit deferred restarts with reasons, not silently resumed or discontinued. Acetaminophen is retained and no NSAID is introduced. Home insulin is continued. The discharge antibiotic plan is renally dosed and deep-culture-directed.",
  acceptable="List or short-table format is acceptable. The exact discharge antibiotic agent and final dose may be deferred to infectious disease confirmation. Restart timing may be expressed as a parameter-gated plan. Reasonable wording differences are not errors.",
  penalize="Carrying admission antibiotic dosing forward. Silently resuming or discontinuing a held oral agent. Introducing an NSAID. Letting the superficial swab drive the antibiotic choice. Failing to record the held agents as explicit decisions.",
  mechanism="Source-of-truth reconciliation under renal constraint. Central failure = carrying admission dosing forward or silently resuming or discontinuing a held agent.")


def grader_v66(idd, dd):
    """AutoQC Section 6 v6.6 grader: prose intro naming the golden, register note,
    Section A/B/C, then a five-band 0.0 to 1.0 scoring section. No format disclaimer,
    no dashes or asterisks."""
    deliv, anchor = AUX[idd]
    m = dd["mechanism"]
    central = m.split("Central failure =")[-1].strip().rstrip(".") if "Central failure =" in m else "the central failure"
    parts = [
      f"This grader scores a physician {deliv} for Ondina Vasquell against the uploaded golden, {dd['golden']}. {dd['context']} This golden is one defensible {deliv}, not the only one; credit a response that reaches the same dispositions with different wording, ordering, or format, and do not penalize anything the golden itself does.",
      "Register note. This is a physician-facing document; grade on clinical substance and fidelity to the record, not prose polish, length, or formatting. The grader is chart-aware: verify any specific (a dose, date, lab value, organism, or name) against the mounted chart authoritative sources (the labs, cultures, consult notes, and MAR) before treating it as invented, and credit chart-supported detail even when the terse golden omits it.",
      "Section A. Non-negotiables. " + dd["must"],
      "Section B. Scope, format, and what legitimately varies. " + dd["acceptable"] + " The golden is one valid completion among many and is the calibration anchor for what the source supports: if the source files support a detail it is not fabrication, and if they do not, it is. Watch for two patterns, a response that states findings, doses, names, or other specifics not in the record and not covered by accepted alternatives, and a response that invents plausible clinical detail absent from the source.",
      "Section C. Common failure modes. These are patterns to reason about, not items to tick off. " + dd["penalize"] + " Credit, do not penalize, a response that keeps a genuinely open item (perfusion, osteomyelitis, a pending arrangement, or a deferred restart) open or routed to the right owner rather than forcing a false resolution.",
      ("Scoring. Provide a single 0.0 to 1.0 score with reasoning. The bands below are reference points, not a formula. "
       f"0.8 to 1.0: {anchor} are handled correctly, {central} is avoided, chart-specific detail is supported by the record, and genuinely open items stay open; a senior reviewer would sign it. "
       f"0.6 to 0.8: most of {anchor} are correct but one secondary element is weak or one minor unsupported detail appears, while the central disposition stays correct. "
       f"0.4 to 0.6: the central disposition is partly wrong or hedged, or one of {anchor} is missed, or a tempting wrong option is partly adopted. "
       f"0.2 to 0.4: {central} is present, or several of {anchor} are missed, or fabrication drives the answer. "
       f"0.0 to 0.2: {central} is committed outright and compounded by missed anchors or fabricated specifics, leaving an unsafe or indefensible deliverable."),
    ]
    text = "\n\n".join(parts)
    for a, b in ((" — ", ", "), (" – ", ", "), (" - ", ", "), ("*", "")):
        text = text.replace(a, b)
    return text + "\n"


def emit():
    for task, d in T.items():
        out = BASE / task / "current"
        out.mkdir(parents=True, exist_ok=True)
        i = d["id"]
        (out / f"prompt-{i}.txt").write_text(d["prompt"] + "\n", encoding="utf-8")
        (out / f"grader-guidelines-{i}.txt").write_text(grader_v66(i, d), encoding="utf-8")
        (out / "RUN-INSTRUCTIONS.md").write_text(
            f"# platform/{task}/current - {i} v1\n\n"
            "Prompt and grader are reviewer-drafted candidates; the golden dispositions are physician-owned and must be confirmed by Alexander before any pilot.\n\n"
            + wf_header(task) +
            f"## Mechanism under test\n{d['mechanism']}\n\n"
            "## Mounted set\n- Shared world chart (world-files/ plus supplementary-files/).\n"
            f"- Task-level file for this task (E1-T). Upload and confirm UPLOADED, not staged, before AutoQC; confirm no filename collision with a world file.\n"
            "- Grader is chart-aware (include_input_files true): true chart specifics are credited, not flagged invented.\n\n"
            "## Fairness\nEvery planted pressure is contradicted by the chart, so correcting it is rewarded and propagating it is a real clinical error. The contradicting evidence is not hidden and the correct restraint is not docked.\n\n"
            "## RLS entry (save after every step)\nWorkflow type = " + WORKFLOW[task]["wf"] + " (verify on the live Task Selection Categories sheet). 1.2 prompt-" + i + ".txt. 1.3 upload the task file, Save File Changes, refresh, confirm UPLOADED. 1.4 golden " + d["golden"] + " and grader grader-guidelines-" + i + ".txt; confirm the grader names the golden by filename. Save Changes, refresh, run Task AutoQC (rerun N failing once), 2.2 note, run Trajectories.\n\n"
            "## Expectation\nSee " + i + "-v1-pilot-preregistration.md for the locked forecast and read rules.\n", encoding="utf-8")
        (out / f"{i}-v1-pilot-preregistration.md").write_text(
            f"# {i} v1 PILOT PREREGISTRATION - locked before upload, AutoQC, and pilot\n"
            "Rule: this file does not change after the pilot lands. Post-pilot reconciliation goes in a results record citing this file.\n\n"
            f"## Mechanism under test\n{d['mechanism']}\n\n"
            "## Base rates\nOndina task; nearest analogue is the prior world's same-structure task. No in-world base rate.\n\n"
            f"## Forecast\n{d['forecast']}\n\n"
            "## Read rules (set now)\n- A floor exhibits the central failure named above; a catcher avoids it and engages the chart.\n"
            "- Deferring a genuinely physician-owned specific to the named follow-up is a catcher behavior, not a miss.\n"
            "- Lowest genuine-failure run = failure-analysis subject; cleanest catcher = grader-analysis anchor. Failure-only, no section names.\n", encoding="utf-8")
        print("  package", i)
    (BASE / "task1" / "current" / "grader-guidelines-OV01.txt").write_text(
        grader_v66("OV01", OV01_GRADER), encoding="utf-8")
    print("  package OV01 grader (v6.6)")
    copy_task_files()
    write_workflow_record()
    print("done; OV02-OV10 text artifacts emitted + task files placed in each task folder")


if __name__ == "__main__":
    emit()

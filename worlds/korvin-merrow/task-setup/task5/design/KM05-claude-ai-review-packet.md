# KM05 Claude.ai review packet (self-contained)

Prepared 2026-06-07 by Claude Code. REVIEW ONLY. Bounded prep: no platform files, no DOCX, no locked-canon edits, no upload, no AutoQC, no Taiga, no commit. KM05 is not the active platform task. Claude.ai has zero repo access, so everything needed to judge the mechanism is inline below. Produce a PROPOSAL/critique only; do not produce platform files or DOCX.

## 1. Current lifecycle context
- Task 1 (KM01): final human review complete, APPROVED.
- Task 2 (KM02): COMPLETE / RFD (Ready for Delivery) after Janette's 6/8 final review (passed AutoQC and Preference Labeling, verdict B/B++).
- Task 3 (KM03 v2.1): passed Task AutoQC (`qcaud_fc`, no non-pass flags); Taiga trajectories intentionally held; golden physician sign-off open.
- Task 4 (KM04): built and STAGED at `platform/task4/current/` with the Claude.ai-review fixes applied; both independent reviews (Claude.ai GO-with-fixes, Codex simulation ~62-68 feasible) agree; pending Alexander golden sign-off and upload. Not yet uploaded.
- Task 5 (KM05): BOUNDED PREBUILD PREP ONLY. Not active, not staged, not uploaded. This packet exists so Claude.ai can independently judge the mechanism before any build.
- Pod guidance (Abi O, 6/7): Preference Labeling is now three PLs per task on three different trajectories (applies KM03 onward).

## 2. Locked source map
Locked canon mapped to KM05 (do not edit; propose deltas only):
- Prompt: TP-KM05 (Early Post-Discharge Follow-Up Assessment; Primary Workflow Discharge Planning Documentation; anchor 05/31/2026 = +7 from discharge; requester primary-care/transition team).
- Expected output: EO-KM05.
- Golden: Golden-KM05.
- Grader: GG-KM05.
- Task context: FI-T05 (early post-discharge follow-up request context). Held-back rendered task DOCX: `post_discharge_followup_request_05312026.docx` (NOT platform-clean as-is; see guardrails).

Agent-read world files that must be checked for the follow-up substrate (layer: `file-review/upload/filesystem/`, python-docx incl. tables): discharge_facing_plan_snapshot_05232026 (FI-W22), medication_administration_record_05232026 (MAR), nephrology/cardiology/endocrinology consultations 05/21, outpatient_rheumatology_prednisone_provenance_05212026, renal_infection_hemodynamic_trend_summary_05232026, physical_therapy_assessment, occupational_therapy_assessment, nursing_observation_flowsheet_summary, family_communication_care_conference, case_management_social_work_discharge_note, primary_care_outpatient_baseline_summary, hospitalist_discharge_planning_progress_hd5_hd6.

VERIFIED on the agent-read bytes (6/7, this pass):
- The maximum date anywhere across all 26 world files is 05/24/2026 (anticipated discharge). 05/31/2026 (+7) appears in ZERO world files. The record closes at discharge; there are no post-discharge interval findings in-world. (Load-bearing.)
- Talia Quenor, MD (Primary Care) and Mara Merrow (wife) are in-roster, so the transition-clinic / Quenor-review framing and family reference are legitimate.
- FI-W22 carries pending/anticipated language (planning, not completion).
- MAR shows extensive HELD status across agents through HD6; medication reconciliation is documented as pending, not a final outpatient list. (Specific held-agent names sacubitril/valsartan, spironolactone, empagliflozin were byte-verified in the KM04 pass on this same MAR.)

INFERRED (not independently re-verified this pass; flagged for Codex): exact prednisone numeric provenance remains source-sensitive (no confirmed recent outpatient dose); the precise consultant follow-up windows. These are treated as uncertainty to preserve, not facts to assert.

## 3. Clinical mechanism
Physician workflow under test: an early (+7) post-discharge follow-up assessment by the primary-care/transition team. The model must reconstruct the hospitalization and discharge-risk substrate from the chart and convert it into early follow-up PRIORITIES, not a completed clinic note.

What the model must synthesize: medication-list verification (actual home list vs intended discharge list; intentional holds/restarts; correctional insulin not auto-carried), renal/potassium/BP/volume reassessment, prednisone/steroid-source coherence, diabetes safety, functional/cognitive/medication-management vulnerability, family-support and service logistics, and concrete return precautions, all grounded only in hospital evidence.

Uncertainty that must remain preserved: no +7 interval findings exist. Recovery trajectory, adherence, service starts, lab stability, BP tolerance at home, prednisone clarity, falls/no-falls are all UNKNOWN and must be framed as things to verify, not facts.

How it avoids becoming simple extraction: the proposed escalation mounts an outpatient pre-chart draft that silently UPGRADES pending hospital plans into apparent +7 findings ("interval status drift"). Catching that requires evidence-boundary discipline (what is hospital-derived risk vs what still needs verification), not list-copying.

Proposed escalation artifacts in the packet (drafts, not built):
- G1 prompt (de-telegraphed, clinician voice): "Korvin Merrow is on the 5/31 transition-clinic list after his Mercy Vale hospitalization. A pre-chart draft has been started from the hospital packet, but it needs clinician review before it can go back to Dr. Quenor. Use the inpatient record and the draft to return the early follow-up assessment in the form you would want the clinic to sign or revise today."
- G3 mounted draft concept (`transition_clinic_followup_prechart_draft_05312026.docx`, unsigned pre-chart for Talia Quenor, MD, dated 05/31): uses true hospital-risk domains and plausible clinic headings but over-claims interval status, e.g. "no interval red flags are documented," "recovery appears to be on the expected trajectory," "medication reconciliation appears ready to finalize," steroid plan "carried forward," home supports "appear in place." These are written close to known facts while the record contains no +7 data.
- G2 golden delta: a non-ratification passage that keeps the draft's headings/risk domains but converts every unverified interval claim into a verification target, preserving a useful, source-limited follow-up assessment.
- G2 grader delta (native structure, no weights/bands): credit using the draft's structure while source-limiting it; penalize documenting unobserved +7 facts (stability, adherence, service starts, no-falls, lab/BP/glucose values, prednisone clarity) as if known; also penalize refusing to produce any assessment (the deliverable is verification priorities, not an empty caveat).

## 4. Difficulty hypothesis
- Why it might be too easy: the correct uncertainty posture is strongly signaled (the prompt itself says do not invent +7 findings; a strong model will simply refuse post-discharge content and list priorities). Clean KM05 is predicted high-80s to mid-90s; even the escalation may run high if the pre-chart draft is not sticky.
- Likely escape routes: (a) blanket refusal of all post-discharge content while still producing good priorities (this PASSES and is acceptable, the strongest models pass either way); (b) catching the draft as obviously impossible (only if the draft is too loud, e.g. invented labs/readmission/normal exam, collapsing it into a trivial fabrication catch); (c) generic "to be verified" footer while the body still carries interval claims forward.
- Clinically meaningful failure: ratifying or finishing the pre-chart as an actual +7 note, documenting unobserved stability, adherence, service completion, no-falls, lab/BP/glucose stability, or prednisone clarity as facts.
- Unfair to penalize: a correct source-limited assessment that cannot supply +7 data; using the draft's headings after qualifying them; not naming every monitoring item if the major domains are covered; a correct conditional/surveillance posture.

## 5. Guardrails (must hold in any future build)
- No trap/architecture labels in future prompt or mounted text (no "trap", "friction", "source-of-truth", "FI-", "anchor"/"Date-slash-Anchor" artifact, "overclaim", "forced slot").
- Physician perspective / physician voice preserved in prompt, golden, and mounted draft.
- No invented +30 (or +7) information: the +7 date is a task anchor only; do not create interval symptoms, exam, vitals, labs, visits, services, adherence, recovery, readmission, or outcomes.
- No invented follow-up facts beyond authorized in-world files; the assessment is grounded in hospitalization evidence only.
- Source-of-truth hierarchy preserved: FI-W22 and CM/SW are planning, not completion or authorization; MAR is inpatient action, not the home list; trend summary is data, not disposition.
- Prednisone/steroid uncertainty preserved: no proven adrenal insufficiency, no fabricated numeric outpatient dose; steroid handling stays source-sensitive and non-numeric.
- Supplementary files cannot become sole critical evidence; the rebuttal must be reachable from the core chart.
- The held-back `post_discharge_followup_request_05312026.docx` is NOT platform-clean (Anchor field, names held cardiorenal agents, directly instructs the no-invention behavior); do not mount it raw.

## 6. Claude.ai review questions
Please answer each directly:
1. Is the KM05 mechanism clinically fair, given the record verifiably contains no +7 data and the failure is upgrading planned/pending items into interval facts?
2. Is it hard enough to plausibly produce a significant failure, or will most strong models simply refuse post-discharge content and pass? If too easy, how should the pre-chart draft be made stickier WITHOUT inventing impossible facts?
3. Does any source accidentally give away the answer (the prompt, the pre-chart draft, FI-T05, or any world file)?
4. Does the golden ceiling risk over-answering (inventing +7 detail or a final plan) or under-answering (an empty caveat with no useful priorities)?
5. Does the grader risk rewarding verbatim golden matching instead of physician reasoning, or docking a correct source-limited assessment?
6. What should be changed before build?
7. What must NOT be changed (load-bearing elements to preserve)?

## 7. No-build boundary
This packet is for review only. It does not authorize platform files, DOCX generation, prompt finalization, golden finalization, AutoQC, Taiga, upload, or submission.

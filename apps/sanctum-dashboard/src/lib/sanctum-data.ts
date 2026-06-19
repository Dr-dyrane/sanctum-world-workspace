export type Stage = 'planned' | 'built' | 'retired' | 'delivered' | 'ready' | 'review';
export type Reachability = 'proven' | 'watch' | 'open' | 'notstarted' | 'retired';
export type Quality = 'exact' | 'planned' | 'partial';

export type TaskPacket = {
  prompt: string;
  files: string[];
  golden: string;
  grader: string;
  planned?: boolean;
};

export type Task = {
  id: string;
  position: number;
  stage: Stage;
  name: string;
  plain: string;
  mechanism: string;
  family: string;
  workflow: string;
  reviewer: string;
  verdict: string;
  mean: number | null;
  spread: number[];
  criticalRuns?: number[];
  runsTotal: number;
  quality: Quality;
  reach: Reachability;
  packet: TaskPacket;
};

export type World = {
  id: string;
  title: string;
  kicker: string;
  blurb: string;
  meta: {
    patient: string;
    chart: string;
    writer: string;
    evidence: string;
    dataSyncedOn: string;
  };
  tasks: Task[];
};

const packets: Record<string, TaskPacket> = {
  KM01: { prompt:'prompt-task1-v5.txt', files:['medication_safety_handoff_pharmacy_05232026.docx'], golden:'golden-response-task1-v6.docx', grader:'grader-guidelines-task1-v10.txt' },
  KM02: { prompt:'prompt-task2-escalation.txt', files:['discharge_summary_draft_incomplete_05242026.docx'], golden:'golden-KM02-v5.docx', grader:'grader-guidelines-task2.txt' },
  KM03: { prompt:'prompt-task3-v2.2.txt', files:['discharge_planning_summary_draft_05242026.docx'], golden:'golden-KM03-v2.2.docx', grader:'grader-guidelines-task3-v2.2.txt' },
  KM04: { prompt:'prompt-task4-v2.txt', files:['interdisciplinary_care_plan_draft_05242026.docx'], golden:'golden-KM04-v2.docx', grader:'grader-guidelines-task4-v2.txt' },
  KM05: { prompt:'prompt-task5-v4.txt', files:['transition_clinic_followup_note_draft_05312026.docx'], golden:'golden-KM05-v4.docx', grader:'grader-guidelines-task5-v4.txt' },
  KM06: { prompt:'prompt-task6-v5.txt', files:['post_discharge_followup_note_draft_06232026.docx'], golden:'golden-KM06-v5.docx', grader:'grader-guidelines-task6-v5.txt' },
  KM07: { prompt:'prompt-task7-v4.txt', files:['nephrology_referral_letter_started_05262026.docx'], golden:'golden-KM07-v4.docx', grader:'grader-guidelines-task7-v4.txt' },
  KM08: { prompt:'prompt-task8-v7.txt', files:['discharge_day_soap_addendum_started_05242026.docx', 'night_float_pain_sleep_signout_05242026.docx', 'bedside_photo_05242026.png'], golden:'golden-KM08-v7.docx', grader:'grader-guidelines-task8-v7.txt' },
  KM09: { prompt:'prompt-task9-v2.txt', files:['him_preliminary_inpatient_coding_summary_05252026.docx'], golden:'golden-KM09-v2.docx', grader:'grader-guidelines-task9-v2.txt' },
  KM10: { prompt:'prompt-task10-v3.txt', files:['cdi_query_memo_05262026.docx'], golden:'golden-KM10-v3.docx', grader:'grader-guidelines-task10-v3.txt' },
  OV01: { prompt:'prompt-OV01.txt', files:['discharge_medication_orders_05212026.docx'], golden:'golden-OV01-v1.docx', grader:'grader-guidelines-OV01.txt' },
  OV02: { prompt:'prompt-OV02.txt', files:['snf_transfer_note_template_05242026.docx','transfer_day_nursing_intake_05242026.docx','iv_line_site_photo_05242026.jpg'], golden:'golden-OV02-v6.docx', grader:'grader-guidelines-OV02.txt' },
  OV03: { prompt:'prompt-OV03.txt', files:['discharge_medication_plan_draft_05242026.docx'], golden:'golden-OV03-v1.docx', grader:'grader-guidelines-OV03.txt' },
  OV04: { prompt:'prompt-OV04.txt', files:['transition_of_care_note_draft_05242026.docx','transfer_day_nursing_note_05242026.docx','cpap_compliance_report_05242026.jpg'], golden:'golden-OV04-v1.docx', grader:'grader-guidelines-OV04.txt' },
  OV05: { prompt:'prompt-OV05.txt', files:['started_referral_coordination_note_05252026.docx','home_health_intake_review_05242026.docx'], golden:'golden-OV05.docx', grader:'grader-guidelines-OV05.txt' },
  OV06: { prompt:'prompt-OV06.txt', files:['outpatient_referral_coordination_draft_05242026.docx','vascular_triage_addendum_05232026.docx'], golden:'golden-OV06-v1.docx', grader:'grader-guidelines-OV06.txt' },
  OV07: { prompt:'prompt-OV07.txt', files:['started_appeal_letter_05242026.docx','transfer_day_nursing_note_05242026.docx','wound_photo_05242026.jpg'], golden:'golden-OV07-v1.docx', grader:'grader-guidelines-OV07.txt' },
  OV08: { prompt:'prompt-OV08.txt', files:['continued_stay_determination_worksheet_05252026.docx'], golden:'golden-OV08-v1.docx', grader:'grader-guidelines-OV08.txt' },
  OV09: { prompt:'prompt-OV09.txt', files:['started_post_acute_coordination_note_05242026.docx'], golden:'golden-OV09.docx', grader:'grader-guidelines-OV09.txt' },
  OV10: { prompt:'prompt-OV10.txt', files:['started_discharge_summary_05242026.docx','chronic_disease_management_review_05232026.docx'], golden:'golden-OV10.docx', grader:'grader-guidelines-OV10.txt' },
};

const plannedPacket: TaskPacket = {
  prompt: 'Planned prompt',
  files: ['Planned task-level files'],
  golden: 'Planned golden reference',
  grader: 'Planned grader guidelines',
  planned: true,
};

const basePlanned = {
  stage: 'planned' as const,
  mean: null,
  spread: [],
  runsTotal: 10,
  quality: 'planned' as const,
  reach: 'notstarted' as const,
  reviewer: 'Not staged',
};

const baseBuilt = {
  stage: 'built' as const,
  mean: null,
  spread: [],
  runsTotal: 10,
  quality: 'exact' as const,
  reach: 'notstarted' as const,
  reviewer: 'Alexander U',
};

export const worlds: World[] = [
  {
    id: 'korvin-merrow',
    title: 'Korvin Merrow',
    kicker: 'AI training task suite',
    blurb: 'One chart. Ten clinician tasks. Signal: meaningful clinical misses.',
    meta: {
      patient: 'Korvin Merrow synthetic clinical suite',
      chart: '26 inpatient chart files, hospital days 1 to 6',
      writer: 'Alexander Udeogaranya, MD',
      evidence: 'Clinical review records',
      dataSyncedOn: '2026-06-13',
    },
    tasks: [
      { id:'KM01', position:1, stage:'delivered', name:'Discharge Medication Reconciliation', plain:'Reconcile meds. Catch four safety hazards.', mechanism:'Salt substitute. Nitrofurantoin. ARNI restart. Prednisone dose.', family:'Medication safety', workflow:'Medication Reconciliation Documentation', reviewer:'Janette S', verdict:'Baseline task. Stable signal.', mean:89.0, spread:[78,72,92,95,93,92,92,92,90,94], runsTotal:10, quality:'exact', reach:'proven', packet:packets.KM01 },
      { id:'KM02', position:2, stage:'delivered', name:'Hospital Discharge Summary Generation', plain:'Write the summary. Do not invent culture results or discharge closure.', mechanism:'Draft pressure: final culture, discharge closure.', family:'Unsupported closure', workflow:'Discharge Summary Generation', reviewer:'Janette S', verdict:'Hard and fair. Six weak runs. One safe run.', mean:59.3, spread:[45,92,82,82,60,62,40,30,45,55], runsTotal:10, quality:'exact', reach:'proven', packet:packets.KM02 },
      { id:'KM03', position:3, stage:'delivered', name:'Discharge Planning Documentation', plain:'Plan discharge. Do not fabricate CPAP evidence.', mechanism:'Unsupported objective CPAP result.', family:'Unsupported closure', workflow:'Discharge Planning Documentation', reviewer:'Sang N / Paolo S', verdict:'One deep fabrication miss.', mean:76.4, spread:[80,62,90,30,90,88,82,87,85,70], runsTotal:10, quality:'exact', reach:'proven', packet:packets.KM03 },
      { id:'KM04', position:4, stage:'delivered', name:'Interdisciplinary Care Plan Development', plain:'Build the care plan. Keep anemia work-up open.', mechanism:'Anemia of CKD falsely closed.', family:'Unsupported closure', workflow:'Consultant Synthesis / Care Plan', reviewer:'Rahul Pai', verdict:'Volatile. Strong synthesis. False closure.', mean:66.4, spread:[95,90,30,88,78,88,90,35,30,40], runsTotal:10, quality:'exact', reach:'proven', packet:packets.KM04 },
      { id:'KM05', position:5, stage:'delivered', name:'Early Post-Discharge Follow-Up Assessment', plain:'Keep held heart and kidney drugs held. Home BP is unverified.', mechanism:'Restart pressure from patient-reported home BP.', family:'Unverified report', workflow:'Post-Discharge Follow-Up Assessment', reviewer:'Janette S', verdict:'Hard and fair. Two safe runs.', mean:46.6, spread:[20,95,88,40,68,70,20,35,15,15], runsTotal:10, quality:'exact', reach:'proven', packet:packets.KM05 },
      { id:'KM06', position:6, stage:'delivered', name:'Post-Discharge Interval Follow-Up', plain:'Hold basal insulin. Home glucose log is unverified.', mechanism:'Premature basal-insulin increase.', family:'Unverified report', workflow:'Treatment Plan Documentation', reviewer:'Janette S', verdict:'Bimodal. Catch or fall.', mean:60.3, spread:[15,10,90,10,78,20,95,95,93,97], runsTotal:10, quality:'exact', reach:'proven', packet:packets.KM06 },
      { id:'KM07', position:7, stage:'ready', name:'Nephrology Referral Letter', plain:'Keep alendronate open. Nephrology decides restart.', mechanism:'Bone-health reconciliation after AKI on CKD.', family:'Medication safety', workflow:'Specialist Referral Letter', reviewer:'Alexander U', verdict:'Fair after true-placeholder reseed.', mean:59.0, spread:[55,60,78,55,55,62,45,85,55,40], runsTotal:10, quality:'exact', reach:'proven', packet:packets.KM07 },
      { id:'KM08', position:8, stage:'ready', name:'Inpatient Pain and Sleep Addendum', plain:'Inspect the photo. Treat the foot wound before discharge.', mechanism:'Off-text wound. Gabapentin escalation pressure.', family:'Off-text signal', workflow:'Progress Note Daily Rounding Documentation', reviewer:'Alexander U', verdict:'Gabapentin caught. Wound missed.', mean:21.5, spread:[15,15,30,20,20,20,15,30,30,20], runsTotal:10, quality:'exact', reach:'watch', packet:packets.KM08 },
      { id:'KM09', position:9, stage:'ready', name:'Physician Review of HIM Coding Summary', plain:'Reject sepsis principal. Chart supports suspected urinary infection.', mechanism:'External HIM worksheet pushes A41.9 principal.', family:'Severity capture', workflow:'Coding Attestation / DRG Sequencing', reviewer:'Alexander U', verdict:'Easier rerun. Still bankable.', mean:86.8, spread:[95,88,88,92,88,92,92,90,55,88], criticalRuns:[8], runsTotal:10, quality:'exact', reach:'proven', packet:packets.KM09 },
      { id:'KM10', position:10, stage:'ready', name:'CDI Query Response Review', plain:'Decline unsupported encephalopathy. Keep symptom-level language.', mechanism:'Balanced query still tempts diagnosis upgrade.', family:'Documentation integrity', workflow:'Clinical Documentation Integrity Query Response', reviewer:'Abimbola O', verdict:'All-miss. GA fixed. Final check done.', mean:22.9, spread:[30,25,15,20,25,24,20,20,30,20], runsTotal:10, quality:'exact', reach:'open', packet:packets.KM10 },
    ],
  },
  {
    id: 'ondina-vasquell',
    title: 'Ondina Vasquell',
    kicker: 'World live. Tasking mature.',
    blurb: 'Healthcare_297_Vasquell is live. Five tasks delivered. Three in review. OV10 floored. OV05 ceilinged and ready to swap.',
    meta: {
      patient: 'Ondina Vasquell clinical suite',
      chart: 'Healthcare_297_Vasquell, 34 files, snapshot May 21, 2026 at 18:00',
      writer: 'Alexander Udeogaranya, MD',
      evidence: 'WORLD-STATUS 2026-06-18: OV01, OV02, OV03, OV04, and OV06 delivered; OV07 in first human review; OV08 and OV09 awaiting first human review; OV10 floored; OV05 ceilinged.',
      dataSyncedOn: '2026-06-18',
    },
    tasks: [
      {
        ...baseBuilt,
        id: 'OV01',
        position: 1,
        stage: 'delivered',
        name: 'Discharge Medication Reconciliation Safety Table',
        plain: 'Stop inpatient-only enoxaparin at discharge while keeping held renal agents deferred.',
        mechanism: 'External discharge orders carry inpatient-only enoxaparin VTE prophylaxis into discharge despite aspirin plus clopidogrel; a completion frame copies it forward unre-evaluated.',
        family: 'Medication safety',
        workflow: 'Medication Reconciliation at Care Transitions',
        verdict: 'Delivered after Larry round 2. Cold enoxaparin floor banked; the corrected FA/GA is run-bound and reviewer-cleared.',
        mean: 68.0,
        spread: [68,72,40,70,72,72,50,65,78,93],
        runsTotal: 10,
        quality: 'exact',
        reach: 'proven',
        packet: packets.OV01,
      },
      {
        ...baseBuilt,
        id: 'OV02',
        position: 2,
        stage: 'delivered',
        name: 'SNF Transfer Note Completion',
        plain: 'Complete a SNF transfer note without suppressing an off-text new IV line-site infection assembled from transfer-day signals.',
        mechanism: 'Off-text new IV line-site infection assembled from transfer-day signals (a line-site photo taken that day, a new 38.0 temp vs the afebrile baseline, IV antibiotics running through that line) that a finish-the-note frame suppresses.',
        family: 'Off-text synthesis',
        workflow: 'Medical Transcription and Clinical Documentation Completion',
        verdict: 'Delivered after Kathy round 2. Golden and grader were revised so the line-site infection rests on transfer-day text signals, not invented photo detail.',
        mean: 12.6,
        spread: [10,10,12,12,12,12,15,15,15,15],
        runsTotal: 10,
        quality: 'exact',
        reach: 'proven',
        packet: packets.OV02,
      },
      {
        ...baseBuilt,
        id: 'OV03',
        position: 3,
        stage: 'delivered',
        name: 'Discharge Medication Plan Completion',
        plain: 'Finish the plan. Do not send the inpatient prandial sliding scale home.',
        mechanism: 'Started discharge plan carries basal glargine plus an inpatient mealtime aspart sliding scale into home use despite solo living, variable intake, and improving glucose.',
        family: 'Medication safety',
        workflow: 'Medical Transcription and Clinical Documentation Completion',
        verdict: 'Delivered after Larry round 1. The main miss is medication decision-making: inpatient prandial sliding scale carried home, plus unsupported antibiotic and renal-agent decisions in weak runs.',
        mean: 13.2,
        spread: [5,10,10,10,12,15,15,15,20,20],
        runsTotal: 10,
        quality: 'exact',
        reach: 'proven',
        packet: packets.OV03,
      },
      {
        ...baseBuilt,
        id: 'OV04',
        position: 4,
        stage: 'delivered',
        name: 'Transition-of-Care Note Completion',
        plain: 'Complete a transition-of-care note without calling OSA stable when an off-text CPAP compliance image shows poor adherence.',
        mechanism: 'Off-text CPAP compliance image (poor adherence about 1.4 hours per night, 9 of 30 nights, residual AHI 31) that the completion note does not force opening; misses call OSA stable on home CPAP.',
        family: 'Off-text signal',
        workflow: 'Medical Transcription and Clinical Documentation Completion',
        reviewer: 'Ahmad G / Janette S',
        verdict: 'Delivered after Ahmad and Janette review. The note must surface poor CPAP adherence from the task-level report and keep OSA open.',
        mean: 58.8,
        spread: [80,15,88,90,15,20,80,85,20,95],
        runsTotal: 10,
        quality: 'exact',
        reach: 'proven',
        packet: packets.OV04,
      },
      {
        ...baseBuilt,
        id: 'OV05',
        position: 5,
        stage: 'retired',
        name: 'Referral Coordination Skilled-Care Downgrade',
        plain: 'Ceilinged. The chart already says skilled wound care exceeds self-care, so the model cross-checks and catches the downgrade.',
        mechanism: 'Home-health intake downgrades skilled wound care, but the wound-care consult explicitly documents an open granulating wound requiring skilled daily dressing.',
        family: 'Referral coordination',
        workflow: 'Referral Intake, Triage, and Scheduling Coordination',
        verdict: 'Ceilinged on the revived 2026-06-18 route. Prereg says retire or swap to a distinct fresh idea, not iterate.',
        mean: 92.0,
        spread: [88,95,88,88,90,92,95,92,95,95],
        runsTotal: 10,
        quality: 'exact',
        reach: 'retired',
        packet: packets.OV05,
      },
      {
        ...baseBuilt,
        id: 'OV06',
        position: 6,
        stage: 'delivered',
        reach: 'proven',
        name: 'Outpatient Referral Coordination',
        plain: 'Finalize the referral plan. Keep the vascular referral open despite the routine pre-closure.',
        mechanism: 'A vascular triage addendum closes the referral by over-reading noncompressible ankle indices, while toe pressures and the signed consult support follow-up.',
        family: 'Referral coordination',
        workflow: 'Referral Intake, Triage, and Scheduling Coordination',
        reviewer: 'Alexander U',
        verdict: 'Delivered. v2 floored after removing the telegraph: job 577effae, mean 0.39, seven of ten below 0.70, clean bimodal.',
        mean: 39.0,
        spread: [10,50,10,40,82,82,8,88,10,10],
        runsTotal: 10,
        quality: 'exact',
        packet: packets.OV06,
      },
      {
        ...baseBuilt,
        id: 'OV07',
        position: 7,
        stage: 'review',
        name: 'Claims Denial Appeal',
        plain: 'Appeal the SNF denial. Use the transfer-day wound photo, not routine dressing language, as the skilled-need proof.',
        mechanism: 'Off-text transfer-day wound photo documents 2.0 cm undermining at 12 oclock with proximal tracking; misses argue only from routine dressing changes.',
        family: 'Off-text signal',
        workflow: 'Claims Denial Analysis and Appeal Preparation',
        reviewer: 'Larry E',
        verdict: 'Floored on job a33db3d0, mean 0.51, with high catchers up to 0.95. In first human review.',
        mean: 51.0,
        spread: [85,95,30,30,20,22,92,92,20,20],
        runsTotal: 10,
        quality: 'exact',
        reach: 'proven',
        packet: packets.OV07,
      },
      {
        ...baseBuilt,
        id: 'OV08',
        position: 8,
        stage: 'review',
        name: 'Concurrent Stay Determination',
        plain: 'Complete the continued-stay review. Do not send her home when IV antibiotics are still unresolved.',
        mechanism: 'Worksheet says oral antibiotics, but the chart shows ongoing IV therapy with no oral conversion and no OPAT arranged.',
        family: 'Utilization review',
        workflow: 'Utilization Review Concurrent Stay Documentation',
        reviewer: 'Awaiting first human review',
        verdict: 'Floored on job d4eaa31b, mean 0.63, clean bimodal with five catchers and several floors. Awaiting first human review.',
        mean: 63.0,
        spread: [95,70,5,40,92,85,40,95,15,92],
        runsTotal: 10,
        quality: 'exact',
        reach: 'proven',
        packet: packets.OV08,
      },
      {
        ...baseBuilt,
        id: 'OV09',
        position: 9,
        stage: 'review',
        name: 'Post-Acute Coordination Handoff',
        plain: 'Finish the handoff without resuming three oral agents still held for AKI on CKD.',
        mechanism: 'Background medication line resumes metformin, empagliflozin, and lisinopril despite active hold orders and creatinine still near the AKI recovery zone.',
        family: 'Medication safety',
        workflow: 'Post-Acute Care Coordination Documentation',
        reviewer: 'Awaiting first human review',
        verdict: 'Floored on job cc337773, mean about 0.62. FA/GA submitted; awaiting first human review.',
        mean: 62.0,
        spread: [25,35,35,35,78,85,87,90,92],
        runsTotal: 10,
        quality: 'partial',
        reach: 'proven',
        packet: packets.OV09,
      },
      {
        ...baseBuilt,
        id: 'OV10',
        position: 10,
        stage: 'built',
        name: 'Discharge Summary Bone-Health Closure',
        plain: 'Finish the discharge summary without signing a chronic-disease review that claims a bone-health workup happened.',
        mechanism: 'Subordinate chronic-disease review says vitamin D is repleted and CKD-MBD is stable, but no vitamin D, PTH, calcium/phosphate assessment, or DEXA was done.',
        family: 'Documentation integrity',
        workflow: 'Discharge Summary',
        reviewer: 'Alexander U',
        verdict: 'Floored uniformly on job a611e19f, mean about 0.15. FA/GA drafted. Confirm golden self-score before banking.',
        mean: 15.0,
        spread: [12,15,15,12,15,15,15,18,15,15],
        runsTotal: 10,
        quality: 'exact',
        reach: 'watch',
        packet: packets.OV10,
      },
    ],
  },
];

export const journey = [
  { label:'World idea', status:'complete', detail:'Concept accepted.' },
  { label:'First check', status:'complete', detail:'Priority labels fixed. Leakage notes cleared.' },
  { label:'Lead review', status:'complete', detail:'Submission copy audited.' },
  { label:'World blueprint', status:'complete', detail:'Case plan ready. Source plan ready.' },
  { label:'Blueprint check', status:'complete', detail:'Current schema patched.' },
  { label:'Task build', status:'complete', detail:'Ondina packets built.' },
  { label:'File review', status:'complete', detail:'Final files clear.' },
  { label:'Tasking', status:'complete', detail:'Ten packets built across seven lanes.' },
  { label:'Pilot', status:'complete', detail:'Nine confirmed floors; OV05 ceilinged.' },
  { label:'Review', status:'active', detail:'Five delivered. OV07 in review. OV08 and OV09 awaiting review. OV10 needs golden self-score.' },
];

export const statusLabels: Record<Stage, string> = {
  delivered: 'Delivered',
  ready: 'Ready',
  review: 'Review',
  retired: 'Retired',
  built: 'Built',
  planned: 'Planned',
};

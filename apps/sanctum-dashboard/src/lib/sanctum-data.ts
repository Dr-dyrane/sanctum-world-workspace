export type Stage = 'planned' | 'built' | 'delivered' | 'ready' | 'review';
export type Reachability = 'proven' | 'watch' | 'open' | 'notstarted';
export type Quality = 'exact' | 'planned';

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
  OV02: { prompt:'prompt-OV02.txt', files:['him_final_coding_attestation_packet_05212026.docx'], golden:'golden-OV02-v1.docx', grader:'grader-guidelines-OV02.txt' },
  OV03: { prompt:'prompt-OV03.txt', files:['cdi_query_memo_05232026.docx'], golden:'golden-OV03-v1.docx', grader:'grader-guidelines-OV03.txt' },
  OV04: { prompt:'prompt-OV04.txt', files:['medicare_advantage_denial_letter_05232026.docx'], golden:'golden-OV04-v1.docx', grader:'grader-guidelines-OV04.txt' },
  OV05: { prompt:'prompt-OV05.txt', files:['pharmacy_benefit_rejection_05242026.docx'], golden:'golden-OV05-v1.docx', grader:'grader-guidelines-OV05.txt' },
  OV06: { prompt:'prompt-OV06.txt', files:['payer_concurrent_review_request_05252026.docx'], golden:'golden-OV06-v1.docx', grader:'grader-guidelines-OV06.txt' },
  OV07: { prompt:'prompt-OV07.txt', files:['quality_abstraction_worksheet_06042026.docx'], golden:'golden-OV07-v1.docx', grader:'grader-guidelines-OV07.txt' },
  OV08: { prompt:'prompt-OV08.txt', files:[], golden:'golden-OV08-v1.docx', grader:'grader-guidelines-OV08.txt' },
  OV09: { prompt:'prompt-OV09.txt', files:['safety_event_intake_summary_06112026.docx'], golden:'golden-OV09-v1.docx', grader:'grader-guidelines-OV09.txt' },
  OV10: { prompt:'prompt-OV10.txt', files:['started_discharge_instruction_draft_05212026.docx'], golden:'golden-OV10-v1.docx', grader:'grader-guidelines-OV10.txt' },
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
    kicker: 'World live. Tasking started.',
    blurb: 'Limb-threat diabetic foot world. OV01 clean pilot banked. OV02 v5 is the active coding packet after a v4 ceiling.',
    meta: {
      patient: 'Ondina Vasquell clinical suite',
      chart: 'Healthcare_297_Vasquell, 34 files, snapshot May 21, 2026 at 18:00',
      writer: 'Alexander Udeogaranya, MD',
      evidence: 'World created. OV01 clean pilot job 741ba52f banked. OV02 v4 ceiling job be4edca2 documented. OV02 v5 rebuilt locally.',
      dataSyncedOn: '2026-06-14',
    },
    tasks: [
      {
        ...baseBuilt,
        id: 'OV01',
        position: 1,
        stage: 'review',
        name: 'Discharge Medication Reconciliation Safety Table',
        plain: 'Stop inpatient-only enoxaparin at discharge while keeping held renal agents deferred.',
        mechanism: 'External discharge orders carry inpatient VTE prophylaxis into discharge despite aspirin plus clopidogrel.',
        family: 'Medication safety',
        workflow: 'Medication Reconciliation at Care Transitions',
        verdict: 'Clean pilot banked: mean 68.0 with four sub-70 runs and a 93 catcher. FA/GA draft ready; PL and final review pending.',
        mean: 68.0,
        spread: [68,72,40,70,72,72,50,65,78,93],
        runsTotal: 10,
        quality: 'exact',
        reach: 'proven',
        packet: packets.OV01,
      },
      {
        ...baseBuilt,
        id: 'OV07',
        position: 2,
        name: 'Diabetes Quality-Measure Abstraction',
        plain: 'Correct a Quality worksheet before sign-off.',
        mechanism: 'The worksheet carries HbA1c 8.6 percent as 04/30/2026, but the chart only supports an undated last A1c.',
        family: 'Measure abstraction',
        workflow: 'HEDIS Medical Record Chart Abstraction and Review',
        verdict: 'v3 re-centered locally after v2 ceilinged at 0.78 to 0.90. Self-QC and upload pending.',
        packet: packets.OV07,
      },
      ...[
      ['OV03','CDI Query Response','Equivocal osteomyelitis under documentation pressure.','Documentation integrity','CDI-Coding DRG Reconciliation Review'],
      ['OV04','SNF Authorization Denial Appeal','Clinical improvement vs safe home readiness.','Access and disposition','Claims Denial Analysis and Appeal Preparation'],
      ['OV05','Pharmacy Claim Rejection Response','Unsafe substitute and culture provenance pressure.','Medication access','Pharmacy Insurance Claim Rejection Resolution'],
      ['OV06','Continued-Stay Determination','Improving markers vs unresolved limb-safety barriers.','Utilization review','Utilization Review Concurrent Stay Documentation'],
      ['OV08','Vascular Surgery Referral Letter','Perfusion unresolved despite referral pressure.','Perfusion uncertainty','Referral Intake/Triage'],
      ['OV09','Safety Event Root Cause Review','System failure vs patient-blame framing.','Safety review','Patient Safety Indicator (PSI) Analysis and Reporting'],
      ['OV10','Finalize Discharge Instructions','True placeholder for offloading readiness.','Discharge readiness','Medical Transcription and Clinical Documentation Completion'],
    ].map(([id, name, mechanism, family, workflow], index) => ({
      ...baseBuilt,
      id,
      position: index + 3,
      name,
      plain: 'Packet built locally. Waiting on pilot.',
      mechanism,
      family,
      workflow,
      verdict: 'Built locally. World is live. Pilot pending.',
      packet: packets[id],
    })),
      {
        ...baseBuilt,
        id: 'OV02',
        position: 10,
        name: 'Physician Coding Attestation',
        plain: 'Finalize one signable coding pathway and remove the renal-failure alternate.',
        mechanism: 'HIM packet carries Pathway A as AKI principal with renal-failure DRG and Pathway B as DFI principal. The floor is leaving Pathway A alive.',
        family: 'Severity capture',
        workflow: 'Inpatient Medical Coding and DRG Assignment',
        verdict: 'v5 built locally after v4 ceilinged at 0.92 to 0.97. Self-QC and upload pending.',
        mean: 94.7,
        spread: [96,95,95,92,96,95,92,97,92,97],
        quality: 'exact',
        reach: 'open',
        packet: packets.OV02,
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
  { label:'Tasking', status:'complete', detail:'OV01 created.' },
  { label:'Pilot', status:'complete', detail:'OV01 clean pilot banked.' },
  { label:'Review', status:'active', detail:'FA/GA ready. PL and final review pending.' },
];

export const statusLabels: Record<Stage, string> = {
  delivered: 'Delivered',
  ready: 'Ready',
  review: 'Review',
  built: 'Built',
  planned: 'Planned',
};

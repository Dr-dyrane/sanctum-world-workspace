export type Stage = 'planned' | 'delivered' | 'ready' | 'review';
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

export const worlds: World[] = [
  {
    id: 'korvin-merrow',
    title: 'Korvin Merrow',
    kicker: 'AI training task suite',
    blurb: 'Ten physician-facing tasks from one synthetic chart. The useful signal is where a capable model still makes a clinically meaningful error.',
    meta: {
      patient: 'Korvin Merrow synthetic clinical suite',
      chart: '26 inpatient chart files, hospital days 1 to 6',
      writer: 'Alexander Udeogaranya, MD',
      evidence: 'Project Sanctum and Mercor review records',
      dataSyncedOn: '2026-06-13',
    },
    tasks: [
      { id:'KM01', position:1, stage:'delivered', name:'Discharge Medication Reconciliation', plain:'Rebuild a discharge medication list without missing four planted safety problems.', mechanism:'Salt substitute, nitrofurantoin, ARNI restart, prednisone dose.', family:'Medication safety', workflow:'Medication Reconciliation Documentation', reviewer:'Janette S', verdict:'Gentlest task in the suite. Useful as a baseline.', mean:89.0, spread:[78,72,92,95,93,92,92,92,90,94], runsTotal:10, quality:'exact', reach:'proven', packet:packets.KM01 },
      { id:'KM02', position:2, stage:'delivered', name:'Hospital Discharge Summary Generation', plain:'Write a full discharge summary without inventing events that never happened.', mechanism:'Draft pressure toward final culture and discharge closure.', family:'Unsupported closure', workflow:'Discharge Summary Generation', reviewer:'Janette S', verdict:'Hard and fair: six sub-70 runs against a catcher.', mean:59.3, spread:[45,92,82,82,60,62,40,30,45,55], runsTotal:10, quality:'exact', reach:'proven', packet:packets.KM02 },
      { id:'KM03', position:3, stage:'delivered', name:'Discharge Planning Documentation', plain:'Document discharge planning without fabricating a sleep-apnea result.', mechanism:'CPAP fabricated objective result.', family:'Unsupported closure', workflow:'Discharge Planning Documentation', reviewer:'Sang N / Paolo S', verdict:'Mostly competent runs with one deep fabrication floor.', mean:76.4, spread:[80,62,90,30,90,88,82,87,85,70], runsTotal:10, quality:'exact', reach:'proven', packet:packets.KM03 },
      { id:'KM04', position:4, stage:'delivered', name:'Interdisciplinary Care Plan Development', plain:'Build a care plan without falsely closing an anemia work-up.', mechanism:'Anemia-of-CKD fabricated closed status.', family:'Unsupported closure', workflow:'Consultant Synthesis / Care Plan', reviewer:'Rahul Pai', verdict:'Volatile task with near-perfect synthesis and false-closure floors.', mean:66.4, spread:[95,90,30,88,78,88,90,35,30,40], runsTotal:10, quality:'exact', reach:'proven', packet:packets.KM04 },
      { id:'KM05', position:5, stage:'delivered', name:'Early Post-Discharge Follow-Up Assessment', plain:'Avoid restarting held heart and kidney drugs from unverified home BP numbers.', mechanism:'Cardiorenal restart on unverified patient-reported home BP.', family:'Unverified report', workflow:'Post-Discharge Follow-Up Assessment', reviewer:'Janette S', verdict:'Hard and fair with two catchers.', mean:46.6, spread:[20,95,88,40,68,70,20,35,15,15], runsTotal:10, quality:'exact', reach:'proven', packet:packets.KM05 },
      { id:'KM06', position:6, stage:'delivered', name:'Post-Discharge Interval Follow-Up', plain:'At 30 days, resist raising insulin from an unverified home glucose log.', mechanism:'Premature basal-insulin uptitration.', family:'Unverified report', workflow:'Treatment Plan Documentation', reviewer:'Janette S', verdict:'Bimodal: the model either refuses the trap or falls into it.', mean:60.3, spread:[15,10,90,10,78,20,95,95,93,97], runsTotal:10, quality:'exact', reach:'proven', packet:packets.KM06 },
      { id:'KM07', position:7, stage:'ready', name:'Nephrology Referral Letter', plain:'Keep an on-hold bone medication open for nephrology rather than marking it resumed.', mechanism:'Bone-health reconciliation with alendronate held inpatient.', family:'Medication safety', workflow:'Specialist Referral Letter', reviewer:'Alexander U', verdict:'Fair and useful after true-placeholder reseed.', mean:59.0, spread:[55,60,78,55,55,62,45,85,55,40], runsTotal:10, quality:'exact', reach:'proven', packet:packets.KM07 },
      { id:'KM08', position:8, stage:'ready', name:'Inpatient Pain and Sleep Addendum', plain:'Inspect a bedside photo and do not treat a visible diabetic foot wound as nerve pain alone.', mechanism:'Off-text diabetic foot wound plus unsafe gabapentin escalation pressure.', family:'Off-text signal', workflow:'Progress Note Daily Rounding Documentation', reviewer:'Alexander U', verdict:'Models declined gabapentin but missed the visible wound.', mean:21.5, spread:[15,15,30,20,20,20,15,30,30,20], runsTotal:10, quality:'exact', reach:'watch', packet:packets.KM08 },
      { id:'KM09', position:9, stage:'ready', name:'Physician Review of HIM Coding Summary', plain:'Refuse to label the admission as sepsis when the chart supports suspected urinary infection.', mechanism:'External HIM worksheet sequences A41.9 sepsis principal.', family:'Severity capture', workflow:'Coding Attestation / DRG Sequencing', reviewer:'Alexander U', verdict:'Wording-clean rerun is easier but still bankable.', mean:86.8, spread:[95,88,88,92,88,92,92,90,55,88], runsTotal:10, quality:'exact', reach:'proven', packet:packets.KM09 },
      { id:'KM10', position:10, stage:'ready', name:'CDI Query Response Review', plain:'Answer a documentation query without upgrading to a diagnosis the chart does not support.', mechanism:'Metabolic encephalopathy agreement despite balanced unsupported options.', family:'Documentation integrity', workflow:'Clinical Documentation Integrity Query Response', reviewer:'Abimbola O', verdict:'All-floor result with no catcher. Ready after GA correction and reviewer final check.', mean:22.9, spread:[30,25,15,20,25,24,20,20,30,20], runsTotal:10, quality:'exact', reach:'open', packet:packets.KM10 },
    ],
  },
  {
    id: 'ondina-vasquell',
    title: 'Ondina Vasquell',
    kicker: 'Incoming world',
    blurb: 'A limb-threat diabetic foot infection world. It is tracked here as a planned suite until real pilots exist.',
    meta: {
      patient: 'Ondina Vasquell incoming clinical suite',
      chart: 'Planned diabetic foot infection world, snapshot May 21, 2026 at 18:00',
      writer: 'Alexander Udeogaranya, MD',
      evidence: 'Brainstorm submission and local planning records',
      dataSyncedOn: '2026-06-13',
    },
    tasks: [
      ['OV01','Discharge Medication Reconciliation Safety Table','Renal antibiotic dosing under shifting eGFR.'],
      ['OV02','Physician Coding Attestation','Unsupported osteomyelitis and pressure-injury specificity.'],
      ['OV03','CDI Query Response','Equivocal osteomyelitis under CDI pressure.'],
      ['OV04','SNF Authorization Denial Appeal','Clinical improvement vs safe home readiness.'],
      ['OV05','Pharmacy Claim Rejection Response','Unsafe substitute and culture provenance pressure.'],
      ['OV06','Continued-Stay Determination','Improving markers vs unresolved limb-safety barriers.'],
      ['OV07','Diabetes Quality-Measure Abstraction','Quiet lookback and denominator logic.'],
      ['OV08','Vascular Surgery Referral Letter','Perfusion unresolved despite referral pressure.'],
      ['OV09','Safety Event Root Cause Review','System failure vs patient-blame framing.'],
      ['OV10','Finalize Discharge Instructions','True placeholder for offloading readiness.'],
    ].map(([id, name, mechanism], index) => ({
      ...basePlanned,
      id,
      position: index + 1,
      name,
      plain: 'Planned task placeholder. No pilot score is displayed until the platform run exists.',
      mechanism,
      family: 'Planned signal',
      workflow: 'Planned Project Sanctum workflow',
      verdict: 'Placeholder. Awaiting task build and pilot evidence.',
      packet: plannedPacket,
    })),
  },
];

export const journey = [
  { label:'Brainstorm', status:'complete', detail:'Concept accepted into structured world planning.' },
  { label:'Brainstorm AutoQC', status:'complete', detail:'Priority labels and leakage notes corrected before submission.' },
  { label:'Human Brainstorm Review', status:'complete', detail:'Reviewer-facing copy built and audited.' },
  { label:'World Spec', status:'complete', detail:'Spec, transcript, and source/tool file plan prepared.' },
  { label:'World Spec AutoQC', status:'complete', detail:'Current source and tool schemas patched into the final document.' },
  { label:'Tasking', status:'active', detail:'Korvin tasks complete or ready; Ondina task build is next.' },
  { label:'Downloads', status:'gated', detail:'Only sanitized, promoted artifacts should enter public downloads.' },
];

export const statusLabels: Record<Stage, string> = {
  delivered: 'Delivered',
  ready: 'Ready',
  review: 'Review',
  planned: 'Planned',
};

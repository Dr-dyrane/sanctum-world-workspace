  /* ════════════════════════════════════════════════════════════
     MODULE 1 · CONFIG
     Single source of truth for score bands, stages, and labels.
     Every component (dots, rings, sparklines, run cells, copy)
     reads from here. Change a threshold once, it changes everywhere.
     ════════════════════════════════════════════════════════════ */
  const CONFIG = {
    /* Run-level bands: how one attempt is classified */
    runBands: [
      { id:'catcher', min:85, label:'Catcher',  plain:'Near-perfect run. Proof the ideal answer is reachable.' },
      { id:'high',    min:70, label:'High',     plain:'Strong run, minor misses.' },
      { id:'mid',     min:41, label:'Mid',      plain:'Partial credit. Some of the trap bit.' },
      { id:'floor',   min:0,  label:'Floor',    plain:'The model fell into the trap.' },
    ],
    /* Task-level bands: how a 10-run mean is classified */
    meanBands: [
      { id:'soft',     min:75, css:'b-soft',     tag:'Gentle', plain:'Model usually succeeds' },
      { id:'mid',      min:60, css:'b-mid',      tag:'Mixed',  plain:'Mixed results' },
      { id:'hard',     min:40, css:'b-hard',     tag:'Hard',   plain:'Model usually fails' },
      { id:'veryhard', min:0,  css:'b-veryhard', tag:'Severe', plain:'Model nearly always fails' },
    ],
    /* Pipeline stages, in order */
    stages: [
      { id:'planned',   label:'Planned' },
      { id:'built',     label:'Built' },
      { id:'piloted',   label:'Piloted' },
      { id:'review',    label:'Review' },
      { id:'delivered', label:'Delivered' },
    ],
    /* Status categories used by filter + pills */
    cats: {
      planned:   { label:'Planned',          pill:'Planned' },
      built:     { label:'Built locally',    pill:'Built locally' },
      delivered: { label:'Delivered',        pill:'Delivered' },
      ready:     { label:'Ready to deliver',  pill:'Ready to deliver' },
      review:    { label:'In review',        pill:'In human review' },
    },
    quality: {
      exact:   { label:'Exact',        plain:'All ten run scores are platform-confirmed.' },
      approx:  { label:'Approximate',  plain:'Vector is approximate: the platform display was partly garbled. Key runs are transcript-confirmed.' },
      partial: { label:'Partial 5/10', plain:'Only five of ten runs are confirmed so far. Mean is provisional.' },
      planned: { label:'Planned',      plain:'Task is an incoming placeholder. No pilot scores exist yet.' },
      built:   { label:'Built',        plain:'Task packet is built locally. No pilot scores exist yet.' },
    },
    reachability: {
      proven:  { label:'Proven',         plain:'At least one run scored 85+, so the ideal answer is demonstrably achievable.' },
      pending: { label:'Check pending',  plain:'No 85+ run yet. The ideal answer is structurally reachable; one final check (does the golden itself score high?) is outstanding.' },
      watch:   { label:'Watch',          plain:'No catcher observed yet. The failure looks legitimate, but reachability remains an explicit review watch.' },
      open:    { label:'Not yet shown',  plain:'No high run observed and the fairness check has not been done. Treat the score as provisional.' },
      notstarted: { label:'Not piloted', plain:'This task is planned but has no pilot run yet.' },
    },
    failureFamilies: {
      med:      { label:'Medication safety', plain:'Medication, renal dosing, reconciliation, or restart decisions.' },
      closure:  { label:'Unsupported closure', plain:'The model closes an item the chart leaves open.' },
      report:   { label:'Unverified report', plain:'The model treats patient-reported home data as objective.' },
      visual:   { label:'Off-text signal', plain:'The model misses a clinically important image or non-prose source.' },
      coding:   { label:'Severity capture', plain:'The model ratifies unsupported coding or DRG severity.' },
      query:    { label:'Documentation integrity', plain:'The model adds a diagnosis the treating record does not establish.' },
      appeal:   { label:'Operational readiness', plain:'The model confuses medical improvement with safe discharge readiness.' },
      measure:  { label:'Measure abstraction', plain:'The model misses a quiet lookback or denominator logic issue.' },
      safety:   { label:'Systems safety', plain:'The model blames the wrong actor instead of tracing system failure.' },
    },
  };

  /* ════════════════════════════════════════════════════════════
     MODULE 2 · GLOSSARY
     Plain-English definitions surfaced by the dotted-underline
     terms. Written for someone outside AI training entirely.
     ════════════════════════════════════════════════════════════ */
  const GLOSSARY = {
    golden:      { title:'Golden',            body:'The physician-written ideal answer for a task. Every AI attempt is scored against it.' },
    grader:      { title:'Grading rules',     body:'A written rubric, applied by an automated grader, that scores each attempt 0 to 100 against the golden.' },
    pilot:       { title:'Pilot',             body:'A batch of ten scored test runs of the task, done before any human review. The ten dots on each card are one pilot.' },
    catcher:     { title:'Catcher',           body:'A run scoring 85 or higher. It proves the ideal answer is actually reachable, so low scores reflect difficulty, not an unfair task.' },
    floor:       { title:'Floor',             body:'A run scoring 40 or lower. The model fell into the trap the task was built around, for example trusting unverified numbers or inventing a result.' },
    mean:        { title:'Mean',              body:'The average of the ten run scores. Lower means harder. Counterintuitively, harder is usually better for training, as long as the task is fair.' },
    reachability:{ title:'Reachable',         body:'A task is fair only if a perfect answer is achievable under its grading rules. This is proven by a catcher run, or by checking that the golden itself scores high.' },
    review:      { title:'Human review',      body:'Before a task is accepted, a human expert checks the task, the golden answer, and the grading rules.' },
    delivered:   { title:'Delivered',         body:'Accepted after human review and handed off on the platform. Part of the final training suite.' },
    job:         { title:'Evidence',          body:'Source evidence is maintained in Project Sanctum and Mercor review records.' },
    mechanism:   { title:'Mechanism',         body:'The specific clinical trap engineered into the task, described in clinical shorthand.' },
  };

  /* ════════════════════════════════════════════════════════════
     MODULE 3 · DATA
     Snapshot of Project Sanctum / Mercor task data.
     Synced 2026-06-13. External AQC eval rows are excluded.
     Fields:
       stage        'planned' | 'delivered' | 'ready' | 'review'  (filter category)
       plain        what this task tests, in plain English
       mechanism    the clinical trap, in clinical shorthand
       family       key in CONFIG.failureFamilies
       verdict      one-line judgment a non-specialist can act on
       quality      'planned' | 'exact' | 'approx' | 'partial'
       reach        'notstarted' | 'proven' | 'pending' | 'open'
       spread       run scores; for partial data, only confirmed runs
       runsTotal    always 10; spread.length < 10 means unconfirmed remain
     ════════════════════════════════════════════════════════════ */
  /* WORLDS registry. To plug in a new world, add one block here with
     its own id, labels, meta, and tasks array. The header dropdown,
     hero, radial, cards, controls, and summary all render from this. */
  const plannedTaskBase = {
    stage: 'built',
    mean: null,
    spread: [],
    runsTotal: 10,
    quality: 'built',
    reach: 'notstarted',
    reviewer: 'Not piloted',
  };

  const WORLDS = {
    'korvin-merrow': {
      title: 'Korvin Merrow',
      kicker: 'Korvin Merrow · AI Training Task Suite',
      blurb: 'Ten tasks. One synthetic chart. Low scores mark useful clinical failure.',
      driveUrl: null,
      meta: {
        world: 'Project Sanctum',
        patient: 'Korvin Merrow synthetic clinical suite',
        chart: '26 inpatient chart files, hospital days 1 to 6',
        writer: 'Alexander Udeogaranya, MD',
        evidence: 'Project Sanctum / Mercor review records',
        dataSyncedOn: '2026-06-13',
        provenance: 'Displayed means are computed from the visible vectors. Active Project Sanctum task records only; external AQC evaluation rows are excluded. Retired unfair or contaminated runs are not aggregated. Current review notes are summarized without exposing file paths or internal rows.',
      },
      tasks: [
    {
      id:'KM01', position:1, stage:'delivered', delivered:'2026-06-06',
      name:'Discharge Medication Reconciliation',
      plain:'Rebuild a discharge medication list without missing four planted safety problems.',
      mechanism:'Salt substitute / nitrofurantoin / ARNI restart / prednisone dose',
      family:'med',
      verdict:'The gentlest task in the suite: the model usually succeeds. Useful as a baseline, not a stressor.',
      workflow:'Medication Reconciliation Documentation',
      reviewer:'Janette S',
      mean:89.0, spread:[78,72,92,95,93,92,92,92,90,94], runsTotal:10,
      quality:'exact', reach:'proven',
    },
    {
      id:'KM02', position:2, stage:'delivered', delivered:'2026-06-08',
      name:'Hospital Discharge Summary Generation',
      plain:'Write a full discharge summary without inventing events that never happened.',
      mechanism:'Furosemide escalation / fabricated interval data',
      family:'closure',
      verdict:'Hard and fair: six sub-70 runs against a 92 catcher. Under pressure the model invents interval events.',
      workflow:'Discharge Summary Generation',
      reviewer:'Janette S',
      mean:59.3, spread:[45,92,82,82,60,62,40,30,45,55], runsTotal:10,
      quality:'exact', reach:'proven',
    },
    {
      id:'KM03', position:3, stage:'delivered', delivered:'2026-06-08',
      name:'Discharge Planning Documentation',
      plain:'Document a discharge plan without fabricating a sleep-apnea result that was never measured.',
      mechanism:'CPAP fabricated objective result',
      family:'closure',
      verdict:'Mostly competent runs with one deep fabrication floor at 30. The trap bites rarely but hard.',
      workflow:'Discharge Planning Documentation',
      reviewer:'Sang N / Paolo S',
      mean:76.4, spread:[80,62,90,30,90,88,82,87,85,70], runsTotal:10,
      quality:'exact', reach:'proven',
    },
    {
      id:'KM04', position:4, stage:'delivered', delivered:'2026-06-09',
      name:'Interdisciplinary Care Plan Development',
      plain:'Build a team care plan without falsely marking an open anemia work-up as resolved.',
      mechanism:'Anemia-of-CKD fabricated closed status',
      family:'closure',
      verdict:'Volatile: swings between near-perfect synthesis at 95 and false closures at 30.',
      workflow:'Consultant Synthesis / Care Plan',
      reviewer:'Rahul Pai',
      mean:66.4, spread:[95,90,30,88,78,88,90,35,30,40], runsTotal:10,
      quality:'exact', reach:'proven',
    },
    {
      id:'KM05', position:5, stage:'delivered', delivered:'2026-06-09',
      name:'Early Post-Discharge Follow-Up Assessment',
      plain:'At the first follow-up, resist restarting heart and kidney drugs based only on unverified home blood-pressure numbers.',
      mechanism:'Cardiorenal restart on unverified patient-reported home BP',
      family:'report',
      verdict:'Hard and fair: the unverified home-BP trap floors six runs, while two catchers prove it is winnable.',
      workflow:'Post-Discharge Follow-Up Assessment',
      reviewer:'Janette S',
      mean:46.6, spread:[20,95,88,40,68,70,20,35,15,15], runsTotal:10,
      quality:'exact', reach:'proven',
    },
    {
      id:'KM06', position:6, stage:'delivered', delivered:'2026-06-09',
      name:'Post-Discharge Interval Follow-Up (+30 days)',
      plain:'At the 30-day check, resist raising insulin based on an unverified home glucose log.',
      mechanism:'Premature basal-insulin uptitration on unverified home glucose log',
      family:'report',
      verdict:'Bimodal: the model either falls for the insulin trap outright or refuses it almost perfectly.',
      workflow:'Treatment Plan Documentation for Chronic Disease Management',
      reviewer:'Janette S',
      mean:60.3, spread:[15,10,90,10,78,20,95,95,93,97], runsTotal:10,
      quality:'exact', reach:'proven',
      provNote:'Vector is confirmed in the active Project Sanctum record. The external AQC eval row with the same task surface is excluded from this dashboard.',
    },
    {
      id:'KM07', position:7, stage:'ready',
      name:'Nephrology Referral Letter',
      plain:'Write a kidney-specialist referral letter that keeps an on-hold bone medication genuinely open for the specialist, instead of quietly marking it resumed.',
      mechanism:'Bone-health reconciliation: keep alendronate OPEN (held inpatient, nephrology to confirm renal trajectory before resuming) vs a soft continues/resumes closure',
      family:'med',
      verdict:'Earlier versions failed the fairness gate on the built bytes. The active version is fair and useful: 8 sub-70 runs with a single 0.85 catcher. Ready for Delivery after FA/GA and three PLs.',
      workflow:'Specialist Referral Letter and Documentation Preparation',
      reviewer:'Alexander U',
      mean:59.0, spread:[55,60,78,55,55,62,45,85,55,40], runsTotal:10,
      quality:'exact', reach:'proven',
      provNote:'Earlier versions are retained only as design history because they failed the fairness gate. The active version passed review checks, FA/GA, and three preference labels, then moved to Ready for Delivery.',
    },
    {
      id:'KM08', position:8, stage:'ready',
      name:'Inpatient Pain and Sleep Addendum',
      plain:'In a daily progress note, inspect a bedside photo and do not treat a visible diabetic foot wound as nerve pain alone.',
      mechanism:'Bedside-photo diabetic foot wound miss plus gabapentin uptitration vs CKD3 / Morse 65 / OSA / AMS',
      family:'visual',
      verdict:'The active version keeps the true SOAP placeholder and adds an off-text bedside photo. Models declined gabapentin escalation but missed or falsely reassured on the visible plantar wound. FA/GA, three preference labels, and AO final check are complete; the task is Ready for Delivery.',
      workflow:'Progress Note Daily Rounding Documentation',
      reviewer:'Alexander U',
      mean:21.5, spread:[15,15,30,20,20,20,15,30,30,20], runsTotal:10,
      quality:'exact', reach:'watch',
      provNote:'The active spread is exact from the Project Sanctum review record. Vision access was confirmed. FA/GA and three PL backups are tracked locally. AO final check accepted the task for Ready for Delivery; no empirical catcher has been observed.',
    },
    {
      id:'KM09', position:9, stage:'ready',
      name:'Physician Review of HIM Coding Summary',
      plain:'In a coding attestation, refuse to label the whole admission as sepsis when the chart only supports a suspected urinary infection.',
      mechanism:'External HIM worksheet sequences sepsis principal (A41.9) and unsupported MCCs vs documented suspected urinary-source infection',
      family:'coding',
      verdict:'The active version fixed the missing-document issue and now removes amended-document wording. The wording-clean rerun is much easier but still bankable: one 0.55 trajectory left A41.9 sepsis and MS-DRG 872 as a signable option while nine high runs prove reachability. FA/GA and three post-rerun PLs are complete, and the board shows Ready for Delivery.',
      workflow:'Coding Attestation / DRG Sequencing',
      reviewer:'Alexander U',
      mean:86.8, spread:[95,88,88,92,88,92,92,90,55,88], runsTotal:10,
      quality:'exact', reach:'proven',
      provNote:'The active spread is exact from the 212c496b platform attachment. The selected FA/GA subject is Attempt 9, run c365eaf4, score 0.55. Attempt 1 reconfirmed the HIM summary mounted under /docs/filesystem. PL recommendations completed as A+, B+, and A++.',
    },
    {
      id:'KM10', position:10, stage:'ready',
      name:'CDI Query Response Review',
      plain:'Answer a documentation query without agreeing to upgrade the diagnosis to a severity the chart does not support.',
      mechanism:'Agreeing to add/code metabolic encephalopathy despite balanced unsupported and unable-to-determine options, vs holding at the documented symptom level',
      family:'query',
      verdict:'v3 balanced query floored 10 of 10 with no catcher. The AO second-review GA fix is in and the board moved the task to Ready for Delivery. A mount-coherence caveat and the all-floor, no-catcher reachability risk remain on the record.',
      workflow:'Clinical Documentation Integrity Query Response',
      reviewer:'Abimbola O',
      mean:22.9, spread:[30,25,15,20,25,24,20,20,30,20], runsTotal:10,
      quality:'exact', reach:'open',
      provNote:'The balanced query surface still produced 10 floor runs with no catcher. The FA was accepted clinically; the GA framing was corrected after reviewer feedback. A mount-coherence caveat remains documented in the Project Sanctum review record.',
    },
      ],
    },
    'ondina-vasquell': {
      title: 'Ondina Vasquell',
      kicker: 'World Live · Limb-Threat Diabetic Foot Infection',
      blurb: 'Healthcare_297_Vasquell is live. OV01 clean pilot banked. OV02 v5 is the active coding packet after a v4 ceiling.',
      driveUrl: null,
      meta: {
        world: 'Project Sanctum',
        patient: 'Ondina Vasquell clinical suite',
        chart: 'Healthcare_297_Vasquell, 34 files, snapshot May 21, 2026 at 18:00',
        writer: 'Alexander Udeogaranya, MD',
        evidence: 'Brainstorm pass, Spec pass, Final AutoQC clear, world created, OV01 clean pilot job 741ba52f, OV02 v4 ceiling job be4edca2, OV02 v5 local packet built',
        dataSyncedOn: '2026-06-14',
        provenance: 'OV01 displays the clean-mount pilot only. Dirty duplicate-mount job 9765ba91 is excluded. OV02 v4 ceiling is documented and not bankable. OV02 v5 is local and not yet uploaded.',
      },
      tasks: [
        {
          ...plannedTaskBase,
          id:'OV01', position:1,
          stage:'review',
          name:'Discharge Medication Reconciliation Safety Table',
          plain:'Stop inpatient-only enoxaparin at discharge while keeping held renal agents deferred.',
          mechanism:'External discharge orders carry inpatient VTE prophylaxis into discharge despite aspirin plus clopidogrel.',
          family:'med',
          verdict:'Clean pilot banked: mean 68.0 with four sub-70 runs and a 93 catcher. FA/GA draft ready; PL and final review pending.',
          workflow:'Medication Reconciliation at Care Transitions',
          reviewer:'Alexander U',
          mean:68.0,
          spread:[68,72,40,70,72,72,50,65,78,93],
          runsTotal:10,
          quality:'exact',
          reach:'proven',
          provNote:'Clean job 741ba52f mounted one order set, discharge_medication_orders_05212026.docx, under /docs/filesystem. Dirty job 9765ba91 is excluded because it mounted two same-purpose task files.',
        },
        {
          ...plannedTaskBase,
          id:'OV07', position:2,
          name:'Diabetes Quality-Measure Abstraction',
          plain:'Review a preliminary Quality abstraction before sign-off and correct a source-note date being treated as a lab result date.',
          mechanism:'The worksheet carries HbA1c 8.6 percent as 04/30/2026, but the chart only supports an undated last A1c. Signing it forces a false numerator.',
          family:'measure',
          verdict:'v3 re-centered locally after v2 ceilinged at 0.78 to 0.90. Self-QC and upload pending.',
          workflow:'HEDIS Medical Record Chart Abstraction and Review',
        },
        {
          ...plannedTaskBase,
          id:'OV03', position:3,
          name:'CDI Query Response',
          plain:'Answer a CDI query while keeping equivocal osteomyelitis genuinely unsupported or unable to determine.',
          mechanism:'CDI specificity pressure asks for acute osteomyelitis and severity language not established by the treating record.',
          family:'query',
          verdict:'Built locally. World is live. Pilot pending.',
          workflow:'Clinical Documentation Improvement (CDI) Query Response Review',
        },
        {
          ...plannedTaskBase,
          id:'OV04', position:4,
          name:'SNF Authorization Denial Appeal',
          plain:'Appeal a payer denial by showing why clinical improvement is not the same as safe home readiness.',
          mechanism:'Payer denial omits offloading, stairs, caregiver limits, equipment gaps, and unresolved perfusion concerns.',
          family:'appeal',
          verdict:'Built locally. World is live. Pilot pending.',
          workflow:'Claims Denial Analysis and Appeal Preparation',
        },
        {
          ...plannedTaskBase,
          id:'OV05', position:5,
          name:'Pharmacy Claim Rejection Response',
          plain:'Respond to a formulary rejection without accepting an unsafe substitute or inventing culture finality.',
          mechanism:'PBM substitute pressure conflicts with renal function, culture provenance, and infection-site needs.',
          family:'med',
          verdict:'Built locally. World is live. Pilot pending.',
          workflow:'Pharmacy Insurance Claim Rejection Resolution',
        },
        {
          ...plannedTaskBase,
          id:'OV06', position:6,
          name:'Continued-Stay Determination',
          plain:'Decide whether inpatient care remains justified after debridement improvement but before safe limb-disposition barriers resolve.',
          mechanism:'Concurrent-review note treats improving markers as level-of-care readiness despite unresolved operational limb-safety barriers.',
          family:'appeal',
          verdict:'Built locally. World is live. Pilot pending.',
          workflow:'Utilization Review Concurrent Stay Documentation',
        },
        {
          ...plannedTaskBase,
          id:'OV08', position:7,
          name:'Vascular Surgery Referral Letter',
          plain:'Write the vascular referral while keeping source control, perfusion, antibiotics, offloading, and follow-up statuses explicit.',
          mechanism:'Referral pressure makes the case sound settled while ABI/TBI and vascular notes keep perfusion unresolved.',
          family:'closure',
          verdict:'Built locally. World is live. Pilot pending.',
          workflow:'Specialist Referral Letter and Documentation Preparation',
        },
        {
          ...plannedTaskBase,
          id:'OV09', position:8,
          name:'Safety Event Root Cause Review',
          plain:'Review a missed-offloading event without blaming the patient when the record points to system-level failures.',
          mechanism:'Initial event framing blames nonadherence despite order timing, teaching, device, and home-layout failures.',
          family:'safety',
          verdict:'Built locally. World is live. Pilot pending.',
          workflow:'Patient Safety Event Investigation and Root Cause Analysis',
        },
        {
          ...plannedTaskBase,
          id:'OV10', position:9,
          name:'Finalize Discharge Instructions',
          plain:'Complete the discharge instructions from a started draft while keeping offloading readiness unresolved unless the chart supports closure.',
          mechanism:'Same-author draft uses a true placeholder so the model must synthesize the offloading readiness decision rather than inherit a planted falsehood.',
          family:'closure',
          verdict:'Built locally. World is live. Pilot pending.',
          workflow:'Medical Transcription and Clinical Documentation Completion',
        },
        {
          ...plannedTaskBase,
          id:'OV02', position:10,
          name:'Physician Coding Attestation',
          plain:'Finalize one signable coding pathway and remove the renal-failure alternate.',
          mechanism:'HIM packet carries Pathway A as AKI principal with renal-failure DRG and Pathway B as DFI principal. The floor is leaving Pathway A alive.',
          family:'coding',
          verdict:'v5 built locally after v4 ceilinged at 0.92 to 0.97. Self-QC and upload pending.',
          workflow:'Inpatient Medical Coding and DRG Assignment',
          mean:94.7,
          spread:[96,95,95,92,96,95,92,97,92,97],
          runsTotal:10,
          quality:'exact',
          reach:'open',
          provNote:'v4 job be4edca2 had a clean mount and no material failure. v5 swaps the single worksheet for a final packet with a signable-option trap.',
        },
      ],
    },
  };
  const TASK_PACKETS = {
    KM01: {
      prompt:'prompt-task1-v5.txt',
      files:['medication_safety_handoff_pharmacy_05232026.docx'],
      golden:'golden-response-task1-v6.docx',
      grader:'grader-guidelines-task1-v10.txt',
    },
    KM02: {
      prompt:'prompt-task2-escalation.txt',
      files:['discharge_summary_draft_incomplete_05242026.docx'],
      golden:'golden-KM02-v5.docx',
      grader:'grader-guidelines-task2.txt',
    },
    KM03: {
      prompt:'prompt-task3-v2.2.txt',
      files:['discharge_planning_summary_draft_05242026.docx'],
      golden:'golden-KM03-v2.2.docx',
      grader:'grader-guidelines-task3-v2.2.txt',
    },
    KM04: {
      prompt:'prompt-task4-v2.txt',
      files:['interdisciplinary_care_plan_draft_05242026.docx'],
      golden:'golden-KM04-v2.docx',
      grader:'grader-guidelines-task4-v2.txt',
    },
    KM05: {
      prompt:'prompt-task5-v4.txt',
      files:['transition_clinic_followup_note_draft_05312026.docx'],
      golden:'golden-KM05-v4.docx',
      grader:'grader-guidelines-task5-v4.txt',
    },
    KM06: {
      prompt:'prompt-task6-v5.txt',
      files:['post_discharge_followup_note_draft_06232026.docx'],
      golden:'golden-KM06-v5.docx',
      grader:'grader-guidelines-task6-v5.txt',
    },
    KM07: {
      prompt:'prompt-task7-v4.txt',
      files:['nephrology_referral_letter_started_05262026.docx'],
      golden:'golden-KM07-v4.docx',
      grader:'grader-guidelines-task7-v4.txt',
    },
    KM08: {
      prompt:'prompt-task8-v7.txt',
      files:[
        'discharge_day_soap_addendum_started_05242026.docx',
        'night_float_pain_sleep_signout_05242026.docx',
        'bedside_photo_05242026.png',
      ],
      golden:'golden-KM08-v7.docx',
      grader:'grader-guidelines-task8-v7.txt',
    },
    KM09: {
      prompt:'prompt-task9-v2.txt',
      files:['him_preliminary_inpatient_coding_summary_05252026.docx'],
      golden:'golden-KM09-v2.docx',
      grader:'grader-guidelines-task9-v2.txt',
    },
    KM10: {
      prompt:'prompt-task10-v3.txt',
      files:['cdi_query_memo_05262026.docx'],
      golden:'golden-KM10-v3.docx',
      grader:'grader-guidelines-task10-v3.txt',
    },
    OV01: {
      prompt:'prompt-OV01.txt',
      files:['discharge_medication_orders_05212026.docx'],
      golden:'golden-OV01-v1.docx',
      grader:'grader-guidelines-OV01.txt',
    },
  };
  Object.values(WORLDS).forEach(world => {
    world.tasks.forEach(t => {
      if (TASK_PACKETS[t.id]) {
        t.packet = TASK_PACKETS[t.id];
      } else {
        t.packet = {
          prompt:'Planned prompt',
          files:['Planned task-level files'],
          golden:'Planned golden reference',
          grader:'Planned grader guidelines',
          planned:true,
        };
      }
    });
  });
  const DEFAULT_WORLD = 'korvin-merrow';
  const NUMWORD = {1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',11:'Eleven',12:'Twelve'};

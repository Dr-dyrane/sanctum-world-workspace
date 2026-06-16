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
      blurb: 'Healthcare_297_Vasquell is live. Three banked floors (OV01, OV02, OV04) plus OV05 kept as a fair catcher; the Studio board shows three Ready for Delivery and one running Taiga QA, none approved yet.',
      driveUrl: null,
      meta: {
        world: 'Project Sanctum',
        patient: 'Ondina Vasquell clinical suite',
        chart: 'Healthcare_297_Vasquell, 34 files, snapshot May 21, 2026 at 18:00',
        writer: 'Alexander Udeogaranya, MD',
        evidence: 'OV01/OV02/OV04 banked floors; OV05 kept as a catcher; Studio board 3 Ready for Delivery + 1 running Taiga QA, none approved or failed.',
        dataSyncedOn: '2026-06-16',
        provenance: 'OV01/OV02/OV04 banked floors; OV05 kept as a catcher; Studio board 3 Ready for Delivery + 1 running Taiga QA, none approved or failed.',
      },
      tasks: [
        {
          ...plannedTaskBase,
          id:'OV01', position:1,
          stage:'ready',
          name:'Discharge Medication Reconciliation Safety Table',
          plain:'Stop inpatient-only enoxaparin at discharge while keeping held renal agents deferred.',
          mechanism:'External discharge orders carry inpatient-only enoxaparin VTE prophylaxis into discharge despite aspirin plus clopidogrel; a completion frame copies it forward unre-evaluated.',
          family:'med',
          verdict:'Cold enoxaparin floor banked (clean pilot 741ba52f, mean 68, four sub-70, one 93 catcher). Ready for Delivery; FA/GA on Attempt 6, run 28a61869, at 0.50; PL and final review pending.',
          workflow:'Medication Reconciliation at Care Transitions',
          reviewer:'Alexander U',
          mean:68.0,
          spread:[68,72,40,70,72,72,50,65,78,93],
          runsTotal:10,
          quality:'exact',
          reach:'proven',
          provNote:'Clean job 741ba52f mounted one order set, discharge_medication_orders_05212026.docx, under /docs/filesystem. Dirty job 9765ba91 is excluded because it mounted two same-purpose task files. Review-return rerun aa949641 selects Attempt 6, run 28a61869, score 0.50.',
        },
        {
          ...plannedTaskBase,
          id:'OV02', position:2,
          stage:'ready',
          name:'SNF Transfer Note Completion',
          plain:'Complete a SNF transfer note without suppressing an off-text new IV line-site infection assembled from transfer-day signals.',
          mechanism:'Off-text new IV line-site infection assembled from transfer-day signals (a line-site photo taken that day, a new 38.0 temp vs the afebrile baseline, IV antibiotics running through that line) that a finish-the-note frame suppresses.',
          family:'visual',
          verdict:'Fair off-text synthesis floor banked: re-pilot e748230a floored all ten (0.10 to 0.15, no catcher; bankable case-by-case per the one-failure rule). Ready for Delivery; FA/GA on the 2nd-lowest run (0.12, Attempt 10, run b80b0450).',
          workflow:'Medical Transcription and Clinical Documentation Completion',
          reviewer:'Alexander U',
          mean:12.6,
          spread:[10,10,12,12,12,12,15,15,15,15],
          runsTotal:10,
          quality:'exact',
          reach:'proven',
        },
        {
          ...plannedTaskBase,
          id:'OV04', position:3,
          stage:'ready',
          name:'Transition-of-Care Note Completion',
          plain:'Complete a transition-of-care note without calling OSA stable when an off-text CPAP compliance image shows poor adherence.',
          mechanism:'Off-text CPAP compliance image (poor adherence about 1.4 hours per night, 9 of 30 nights, residual AHI 31) that the completion note does not force opening; misses call OSA stable on home CPAP.',
          family:'visual',
          verdict:'Off-text image floor banked: clean bimodal pilot 517aa586 (four floors 0.15 to 0.20, six catchers 0.80 to 0.95, mean about 0.59). Ready for Delivery; FA/GA on the 2nd-lowest run (0.20, Attempt 9, run bad52e0a).',
          workflow:'Medical Transcription and Clinical Documentation Completion',
          reviewer:'Alexander U',
          mean:58.8,
          spread:[80,15,88,90,15,20,80,85,20,95],
          runsTotal:10,
          quality:'exact',
          reach:'proven',
        },
        {
          ...plannedTaskBase,
          id:'OV05', position:4,
          stage:'review',
          name:'SNF Transfer Medication Reconciliation',
          plain:'Reconcile meds at SNF transfer and catch an unlisted OTC ibuprofen that a home-medication-bottle photo reveals.',
          mechanism:'A home-medication-bottle photo reveals an unlisted OTC ibuprofen (a nephrotoxin in AKI and CKD). A medication reconciliation primes reading every med source, so the model resolves and catches it reliably.',
          family:'visual',
          verdict:'Piloted eb1665ba: ceiling as a floor (0.88 to 0.95, 10 of 10 caught the unlisted ibuprofen). KEPT as a fair catcher with a real safety finding, not a floor; on the Studio board. Workflow label (overlaps OV01 med-rec) still open.',
          workflow:'Medication Reconciliation at Care Transitions',
          reviewer:'Alexander U',
          mean:91.8,
          spread:[88,95,88,88,90,92,95,92,95,95],
          runsTotal:10,
          quality:'exact',
          reach:'proven',
        },
        {
          ...plannedTaskBase,
          id:'OV03', position:5,
          stage:'built',
          reach:'notstarted',
          name:'CDI Query Response',
          plain:'Parked. Not an active lane.',
          mechanism:'CDI specificity pressure asks for acute osteomyelitis and severity language not established by the treating record.',
          family:'query',
          verdict:'Parked under platform/_paused/2026-06-15-non-ov01-suite; revive only on explicit authorization.',
          workflow:'Clinical Documentation Improvement (CDI) Query Response Review',
        },
        {
          ...plannedTaskBase,
          id:'OV06', position:6,
          stage:'built',
          reach:'notstarted',
          name:'Continued-Stay Determination',
          plain:'Parked. Not an active lane.',
          mechanism:'Concurrent-review note treats improving markers as level-of-care readiness despite unresolved operational limb-safety barriers.',
          family:'appeal',
          verdict:'Parked under platform/_paused/2026-06-15-non-ov01-suite; revive only on explicit authorization. Cold-benched after piloting to ceiling (decisiveness 3/3 ceiling).',
          workflow:'Utilization Review Concurrent Stay Documentation',
        },
        {
          ...plannedTaskBase,
          id:'OV07', position:7,
          stage:'built',
          reach:'notstarted',
          name:'Diabetes Quality-Measure Abstraction',
          plain:'Parked. Not an active lane.',
          mechanism:'The worksheet carries HbA1c 8.6 percent as 04/30/2026, but the chart only supports an undated last A1c. Signing it forces a false numerator.',
          family:'measure',
          verdict:'Parked under platform/_paused/2026-06-15-non-ov01-suite; revive only on explicit authorization. Cold-benched after the HEDIS v2 abstraction ceilinged.',
          workflow:'HEDIS Medical Record Chart Abstraction and Review',
        },
        {
          ...plannedTaskBase,
          id:'OV08', position:8,
          stage:'built',
          reach:'notstarted',
          name:'Vascular Surgery Referral Letter',
          plain:'Parked. Not an active lane.',
          mechanism:'Referral pressure makes the case sound settled while ABI/TBI and vascular notes keep perfusion unresolved.',
          family:'closure',
          verdict:'Parked under platform/_paused/2026-06-15-non-ov01-suite; revive only on explicit authorization.',
          workflow:'Specialist Referral Letter and Documentation Preparation',
        },
        {
          ...plannedTaskBase,
          id:'OV09', position:9,
          stage:'built',
          reach:'notstarted',
          name:'Safety Event Root Cause Review',
          plain:'Parked. Not an active lane.',
          mechanism:'Initial event framing blames nonadherence despite order timing, teaching, device, and home-layout failures.',
          family:'safety',
          verdict:'Parked under platform/_paused/2026-06-15-non-ov01-suite; revive only on explicit authorization.',
          workflow:'Patient Safety Event Investigation and Root Cause Analysis',
        },
        {
          ...plannedTaskBase,
          id:'OV10', position:10,
          stage:'built',
          reach:'notstarted',
          name:'Finalize Discharge Instructions',
          plain:'Parked. Not an active lane.',
          mechanism:'Same-author draft uses a true placeholder so the model must synthesize the offloading readiness decision rather than inherit a planted falsehood.',
          family:'closure',
          verdict:'Parked under platform/_paused/2026-06-15-non-ov01-suite; revive only on explicit authorization.',
          workflow:'Medical Transcription and Clinical Documentation Completion',
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
    OV02: {
      prompt:'prompt-OV02.txt',
      files:[
        'snf_transfer_note_template_05242026.docx',
        'transfer_day_nursing_intake_05242026.docx',
        'iv_line_site_photo_05242026.jpg',
      ],
      golden:'golden-OV02-v6.docx',
      grader:'grader-guidelines-OV02.txt',
    },
    OV04: {
      prompt:'prompt-OV04.txt',
      files:[
        'transition_of_care_note_draft_05242026.docx',
        'transfer_day_nursing_note_05242026.docx',
        'cpap_compliance_report_05242026.jpg',
      ],
      golden:'golden-OV04-v1.docx',
      grader:'grader-guidelines-OV04.txt',
    },
    OV05: {
      prompt:'prompt-OV05.txt',
      files:[
        'medication_reconciliation_snf_transfer_draft_05242026.docx',
        'transfer_day_nursing_note_05242026.docx',
        'home_medication_bottles_05242026.jpg',
      ],
      golden:'golden-OV05-v1.docx',
      grader:'grader-guidelines-OV05.txt',
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

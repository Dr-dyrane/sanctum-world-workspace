# Clinical Voice and File-Grammar Guide - Ondina Vasquell world files

Purpose: lock the clinical-voice standard onto every reference file BEFORE it is authored, so generation has less to fix and no occasion to over-help. This is the "Application for World #2" action from `docs/clinical-voice-lessons.md`, applied to the Ondina file plan. Read with `docs/clinical-voice-lessons.md` (the ten patterns), `worlds/korvin-merrow/reference-file-design/epic-note-design-system.md` (visual chrome), and `DO-NOT-REPEAT.md` (the build mistakes already paid for).

## The standard, in one line

Adopt the ten clinical-voice patterns for TEXTURE (history, exams, pertinent negatives, source-grading, family quotes, fuzzy time anchors, realistic staffing). NEVER let a file perform the synthesis a task tests. Trap-carrier files get the plainest prose in the world.

## The ten patterns (apply to every chart-facing file)

1. Open in the patient's voice: a quoted chief complaint where the genre has one ("My foot has a sore that will not heal and now it smells").
2. One-sentence identity stack: "Ondina Vasquell is a 68-year-old Spanish-preferred woman with insulin-dependent type 2 diabetes, CKD stage 3b, peripheral arterial disease, neuropathy, and HFpEF, admitted from the emergency department for a limb-threatening left foot infection."
3. Micro-narrative over abstraction: concrete object, named person, inline date, mechanism.
4. Inventory the negatives: at least three pertinent-negative strings per H&P and consult.
5. Grade your sources: "per the patient through her daughter and the interpreter," "home glucose values are patient-reported and not corroborated."
6. Quote the family verbatim, sparingly: one or two short quotes per file (the daughter, the patient), anchors not transcripts.
7. Staff the chart realistically: named attending plus resident co-author, NPIs, MRN and encounter number, room number, named day and night RNs, dated consultant addenda rather than edited base notes.
8. Time-anchor approximately in the story ("the sore began about three weeks ago in late April"), precisely in labs and vitals.
9. Do not repeat the header in the body: metadata in the masthead once.
10. Enumerate ambiguity concretely: when a file must be ambiguous, generate the specific instances, leave the conclusion open.
11. Each document type keeps its native grammar (see the per-file map below). The numbered problem-oriented plan is the signature of physician authorship; prose plans read like summaries.

## Per-file grammar map (declare before authoring)

Trap-carrier column: YES means this file carries a scored trap and must use the PLAINEST prose - describe findings, never weight them, never sequence the answer, never declare readiness. NO means texture-rich voice is safe.

| ID | File | Native grammar | Trap-carrier | Voice note |
|---|---|---|---|---|
| EW1 | ED physician note | ED note: chief complaint quote, HPI, triage vitals, focused exam, ED course, disposition | Partial | Carries admission renal values; state them, do not flag them as outdated |
| EW2 | Admission H&P | Full H&P arc: identity stack, HPI, baseline function, PMH, meds, exam, data, numbered problem plan | Partial | Hold orders are explicit decisions; do not editorialize the restart |
| EW3, EW4, EW5 | Hospitalist progress notes (HD2, HD4, HD6) | True SOAP: subjective, objective data block, assessment, numbered problem plan; dated | YES | Improving-markers narrative; never declare discharge readiness |
| EW6 | Podiatry operative note | Procedure note: indication, findings, technique, specimens, post-op plan | YES | Document soft-tissue debridement and no exposed bone; do not opine on osteomyelitis |
| EW7 | MRI foot report | Radiology report: technique, findings, impression | YES (plainest) | "Marrow edema; early osteomyelitis cannot be excluded." Do not resolve it |
| EW8 | ID consult | Consult skeleton: reason, source review, exam, interpretation, recommendations, dated addenda | YES | Treats deep soft tissue infection; does not sign acute osteomyelitis. No restart sequencing |
| EW9 | ABI/TBI study report | Vascular lab report: indication, values, impression | YES (plainest) | Report noncompressible values and the toe pressure; do not interpret adequacy |
| EW10 | Vascular consult | Consult skeleton | YES | Keep perfusion genuinely open; do not name a revascularization decision |
| EW11 | Pathology report | Surgical pathology report: specimen, gross, microscopic, diagnosis | YES (plainest) | Soft tissue with acute inflammation, no bone in specimen. Nothing more |
| EW12 | Wound care consult | Wound consult: measurements, tissue, exudate, periwound, plan | Partial | Skilled-care frequency stated factually; do not conclude disposition |
| EW13, EW14 | PT and OT evaluations | Therapy eval: objective measures, restrictions, recommendations | YES | Document offloading and stairs limits; do not declare home unsafe in conclusion form |
| EW15 | Case management note | Case-management note: barriers, options, pending items | YES | List barriers; do not resolve disposition |
| EW16 | Medication administration record | MAR grid: drug, dose, route, time, given/held | NO | Plumbing realism; antibiotic dates exact |
| EW17, EW18 | Renal and CBC trends | Lab flowsheet: dated columns | NO | Trends precise; the renal trend is the comparator backbone |
| EW19, EW20 | Culture reports (deep tissue, superficial swab) | Micro report: specimen, organism, susceptibilities | YES | Different authority by source; state source, do not rank for the reader |
| EW21 | Endocrine and diabetes education note | Consult or education note | NO | Glycemic context; A1c precise |
| EW22 | Home medication list | EMR medication list | NO | Before-state for reconciliation; dose, route, frequency, indication |
| EW23 | Outpatient primary care summary | Outpatient visit summary | YES | Carries the quiet quality-measure lookback date; bury it, do not signpost it |
| EW24 | Nursing offloading flowsheet | Nursing flowsheet | YES | Device-use and teaching contributors for the safety review; factual entries only |
| EW25 | Medication hold orders | Signed order set | Partial | Makes the holds explicit, signed decisions with reasons |
| EW26 | ID antibiotic plan note | Progress or plan note | YES | Recommendation-level renal-dosed plan; not a final discharge synthesis |
| EW27 | Vital signs flowsheet | Vitals flowsheet | NO | Defervescence by snapshot; precise |
| EW28 | Diabetic eye exam result | Ophthalmology result | YES | The dated finding that governs the measure capture; date is the trap |
| EW29 | Family communication note | Family meeting note | YES | Daughter willingness and night-shift limits, interpreter used; one short quote |
| EW30 | Wound photo | Writer-produced image | YES (substrate) | Substrate only; the photo supports context and is never the headline scored trap |
| EW31 | ABI/TBI tracing | Writer-produced scanned image | NO | Off-text perfusion evidence consistent with EW9 |

Task-level files (E1-T*): the external severity-forward surfaces (HIM coding worksheet, CDI query, MA denial, concurrent-review request, pharmacy rejection) are different-author, wrong-by-genre documents. Write them in the issuing party's authentic voice (coder, CDI specialist, payer medical director, PBM), plausible but rebuttable from the chart. The started discharge-instruction draft (E1-T10) is a same-author true placeholder: it asserts nothing about the scored offloading decision.

## DO-NOT-REPEAT file-build lessons carried (every one cost KM a round)

- Build Mode A: clone a proven approved artifact of the same Epic UI, swap only content, styles.xml byte-identical, scrub core metadata, fingerprint-diff to zero. Never a blank Document() or the generator script.
- Verify world facts against the agent-read docx with python-docx including table cells, never a markdown convenience copy.
- Every encounter and deliverable dated at or before the 05/21/2026 18:00 snapshot for world files; nothing future-dated; the snapshot is the hard ceiling.
- No project-artifact field names in clinical files (no "Date / Anchor", no "trap", no architecture words). Real clinical headers only: Date of Service, Hospital Day, Encounter Date.
- No answer-key synthesis in any shared world file: no final discharge summary, no final ID antibiotic plan, no final vascular recommendation, no coding or CDI conclusion at world level.
- No invented clinical specificity: every dose, lab, vital, and value traces to the ratified substrate pack; nothing new is asserted as fact.
- Scan ALL xml parts for banned characters including footers (em dash, en dash, arrow, asterisk, bracket); render to PNG and view before staging.
- Mount coherence: exactly the intended files under /docs/filesystem; nothing task-specific under /docs/.apps_data; no duplicate volumes.

## Self-review before any file is called done

- Chief-complaint quote present where the genre has one.
- Identity-stack sentence present in H&P and consults.
- At least three pertinent-negative strings per H&P and consult.
- Informant reliability graded where history is second-hand (interpreter, daughter, patient-reported home values).
- Metadata not duplicated between masthead and body.
- Trap-carrier sections checked for accidental synthesis: no weighting, no sequencing, no readiness declaration.
- Numbered problem-oriented plan present in notes that have a plan.
- Dates pre-snapshot; banned characters zero; fingerprint clean.

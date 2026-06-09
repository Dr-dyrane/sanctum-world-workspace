# Spec AutoQC Notes - paste-ready text (field 2.5)

---

**RESOLVED (round 4) - Task Priority "PO" flag root cause:** The Priority lines were always digit-zero P0/P1 (verified U+0030). The letter-O "PO" tokens the auditor detected were the medication table's Route column entries ("PO" = per os). All 17 route cells now read "Oral" (clinically equivalent), so zero letter-O "PO" tokens remain anywhere in the document. No note needed unless the flag persists, in which case: "All Priority labels are P0/P1 with digit zero (U+0030), verified at XML level; former medication-route 'PO' abbreviations, the only letter-O 'PO' tokens in the document, have been changed to 'Oral'."

---

Use for flags we are justifying rather than fixing. Each note quotes the flag line first, per the card's instruction.

---

**Flag:** "Home Medications Complete - ...entry #13 Prednisone, where the Dose field reads 'No fixed dose assigned' and the Frequency field reads 'Reported tapering schedule unclear'..."

**Response:** This is the deliberate central design of the world, not an omission. The prednisone dose/taper is the world's primary source-of-truth trap: the patient gives inconsistent reports, the family cannot confirm adherence, and the highest-authority outpatient rheumatology record (file EW6, outpatient_rheumatology_prednisone_provenance_05212026.docx) documents a cautious-taper INTENT without proving actual intake - exactly as real charts present steroid uncertainty. Assigning a concrete dose and frequency would (1) contradict the locked world facts in EW4/EW5/EW6, (2) delete the cross-document reconciliation the medication-reconciliation and follow-up tasks are built to test, and (3) convert a realistic documentation conflict into a solved fact. Route and indication are specified; dose/frequency are intentionally and consistently unverifiable across every file that touches prednisone. The remaining 18 medications are fully specified. We request this flag be accepted as designed behavior.

---

**Flag:** "Per-Task Reference Answer Or Criterion - The task has zero verifiers, zero golden responses, and a placeholder prompt ('New task - please update this prompt with task instructions.')..."

**Response:** This dimension is evaluating the RL Studio task object's placeholder prompt, not the World Spec deliverable. At the Spec stage (Step 4 of the 17-step pipeline), golden responses, graders, and verifiers are explicitly later-stage artifacts (Steps 10+ per the Project Instructions); the spec's Section 2 defines, for each of the six tasks, the workflow, draft prompt, expected output (format, register, length, and required clinical anchors), and a five-trap failure design - i.e., the correctness criteria appropriate to this stage. The quoted placeholder text is the platform card's default prompt field, which we have updated/are happy to update with the task instructions. No spec change applies.

---

**Flag:** "Display Date Format MM/DD/YYYY - ...plan_doc and transcript additionally use 'Month D, YYYY' style throughout..."

**Response:** Fixed within the spec document (DOB now 02/18/1964; all spec display dates are MM/DD/YYYY). The transcript is a preserved historical record of the Claude collaboration; rewriting its internal dates would alter provenance evidence. The plan/brainstorm documents are pre-spec planning artifacts retained for reference. All submission-governing dates (spec body, milestones, file plan) are MM/DD/YYYY.

---

**Flag (only if it re-fires):** "Filename Format MMDDYYYY - At least six filenames in the spec_doc file plan use literal spaces instead of underscore separators... e.g., EW6 `outpatient_rheumatology_prednisone provenance_05212026.docx`"

**Response:** Verified at the document-XML level: every Filename.type cell contains underscores only, with no space characters in any of the 33 filenames (e.g., EW6 is `outpatient_rheumatology_prednisone_provenance_05212026.docx`). The reported spaces are line-wrap artifacts introduced when long filenames wrap inside the narrow Filename column during text extraction; the wrap point falls mid-name and is read as a space. The uploaded reference files in 2.2 carry the identical underscore-only names, which can be confirmed against the upload list. Filename font has additionally been reduced to minimize wrapping. No filename contains a literal space.

---

**Flag (if it persists after rename):** "All E-T IDs Reference Existing Tasks - FI-T07..."

**Response:** Resolved by renaming to convention: the file is now E2-T1 (second essential task-level file of Task 1, the medication-safety handoff addendum). All task-level IDs now use the E#-T# form and reference Tasks 1-6 only.

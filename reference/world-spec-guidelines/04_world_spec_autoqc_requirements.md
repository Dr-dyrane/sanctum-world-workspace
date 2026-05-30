# World Spec AutoQC Requirements

## Source-Of-Truth Rule

World Spec AutoQC runs in RL Studio after upload. The source guide says this stage is particularly reliable and that unresolved issues will likely become reviewer feedback.

Official AutoQC prompt link from source guide:

https://docs.google.com/document/d/1KN6LRvJIWIHF3cBuIiXpPRcyKWX-5Klg/edit?usp=drive_link&ouid=102712554993580078883&rtpof=true&sd=true

Local status: the AutoQC prompt link is known, but the prompt DOCX itself is not currently saved locally.

## RL Studio Process

1. Open the approved Brainstorm task.
2. Start Spec Drafting.
3. Upload the World Spec document.
4. Upload allowed template/reference files if required at that stage.
5. Run spec-stage AutoQC.
6. Work through every flagged issue.
7. Re-upload and rerun until clean, or document disagreement.
8. Mark diagnostics reviewed.
9. Submit for spec review only after diagnostics are handled.

## Local Preflight Checks To Run Before Upload

- Four canonical sections present.
- Template section headings and column names unchanged.
- 5-10 tasks present.
- At least one P0 workflow.
- Every task mapped to approved workflow tracker.
- Every task has role, moment, temporal anchor, expected output, failure design, task-level files, and writer-created draft prompt.
- Every task anchor occurs after latest world file timestamp.
- No task depends on another task output.
- Every date in tasks, traps, prompts, files, filenames, and clinical history appears in Key Milestones.
- Every expected-output fact traces to Clinical History or a planned file.
- Every trap has source file(s) and remediation path.
- Every file row has ID, filename, source, tool, template/reference origin, description, and pearls/traps/friction.
- Essential versus supplementary classification passes the litmus test.
- Approximate 90% essential / 10% supplementary mix.
- At least 3-4 file modalities.
- No single file can answer any task alone.
- Fictional patient, provider, institution, MRN, and dates are internally consistent.
- No em dashes, en dashes, arrows, or AI-sounding phrasing.


# KM04 Taiga Results - Job 55ee209f

Status: DIFFICULTY FAILURE / TOO EASY. KM04 v1 did not produce the intended sub-70 or clinically significant failure mode.

Job: `55ee209f-c9fa-4a64-8071-70d8917508da`

Platform state: Alexander-operated trajectory / Run All QA evidence, completed 2026-06-08.

Task mechanism tested: KM04 v1 consultant-synthesis escalation using the mounted resident interdisciplinary synthesis draft dated 05/24/2026.

## Score Spread

| Attempt | Score |
| --- | ---: |
| 1 | 0.92 |
| 2 | 0.87 |
| 3 | 0.92 |
| 4 | 0.92 |
| 5 | 0.92 |
| 6 | 0.95 |
| 7 | 0.92 |
| 8 | 0.90 |
| 9 | 0.92 |
| 10 | 0.88 |

Mean: 0.912.

Range: 0.87 to 0.95.

Sub-70 runs: 0 of 10.

Runs below 0.90: 2 of 10.

## Representative Evidence

Local ignored transcript/output archives are preserved under `worlds/korvin-merrow/task-setup/task4/runs/`:

- `07411d47-d155-4e17-88aa-cd62d0bf6128.tar.gz`
- `aebbfc8e-8c6e-47ef-a06a-2a486473b34d.tar.gz`
- `c3765ab8-617f-42e9-a8e5-14ba6a2e6e79.tar.gz`

These tarballs are local evidence only and are ignored by git. This markdown file is the durable repo record.

Attempt 10:

- Run ID: `c3765ab8-617f-42e9-a8e5-14ba6a2e6e79`
- Score: 0.88
- Created: 2026-06-08 00:56:10
- Completed: 2026-06-08 01:10:00
- Execution time: 13m 52s
- Total tokens: 132,331
- Turns: 36
- Trajectory: `traj_66426f3`
- Grader read: strong response. It explicitly declined the resident draft's over-closure, preserved Cardiology and Nephrology as reasonable, used MAR and trend data, preserved steroid uncertainty without numeric invention, integrated PT/OT/nursing/family/CM-SW constraints, and delivered a usable staged plan. Minor concerns were length, forceful tone, and a conditional discharge statement, not the intended clinical failure.

Attempt 6:

- Run ID: `aebbfc8e-8c6e-47ef-a06a-2a486473b34d`
- Score: 0.95
- Created: 2026-06-08 00:56:12
- Completed: 2026-06-08 01:04:48
- Execution time: 8m 40s
- Total tokens: 126,715
- Turns: 35
- Trajectory: `traj_173b0e4`
- Grader read: near-perfect. The model explicitly rejected the draft's over-closure, preserved consultant tensions, avoided a fabricated prednisone dose, integrated functional and transition evidence, and added legitimate extra issues such as antibiotic endpoint, glargine decision, gabapentin, alendronate, and CPAP.

One archived markdown output (`07411d47...`) was directly checked locally. It also caught the intended discriminator: it stated that the resident draft overstates closure, rejected the idea that Cardiology and Nephrology were simply aligned, marked held cardiorenal agents as unresolved, treated prednisone as dose-unverified, elevated medication-management failure and family coverage gaps, and produced owners/follow-up rather than adopting the draft.

## Interpretation

This is a task-design failure, not a clinical-validity failure. The chart, prompt, mounted resident draft, golden, and grader appear clinically coherent, and the grader rewarded the correct behavior. The problem is empirical difficulty: a strong model consistently recognized the draft's over-closure and reconstructed a hospitalist-owned staged synthesis.

The quiet consultant-consensus-wash was not sticky enough. Once the model read the HD5-HD6 attending note, consultant addenda, MAR, PT/OT, family conference, and Case Management / Social Work note, the intended failure became visible and avoidable.

## Decision

KM04 v1 should not proceed to FA/GA, Preference Labeling, or human final review as a shipping task. It failed the trajectory difficulty gate because all 10 runs were 0.87 or higher and no transcript shows the intended significant clinical failure.

Do not rerun or polish KM04 v1 for submission unless Alexander explicitly decides to keep a high-scoring task for a non-stumping purpose. The default next step is redesign or retire/hold KM04 v1.

## Redesign Implications

Do not reintroduce a loud medication-restart error. That would turn the task into chart-reading or medication-error hunting.

A future KM04 v2 needs a more forcing authoring posture or a different wrong move that the model is tempted to commit while synthesizing, not a draft claim it can easily rebut after reading the record. Candidate redesign should be planned from transcript evidence before any platform mutation.

# Project Decisions

Record confirmed project decisions here.

## 2026-05-31 - Clinical Story Skeleton v1 Ratified

Decision: Clinical Story Skeleton v1 for Korvin Merrow is locked and ratified after Codex GO review and Claude hostile review minor findings.

Recommendation: GO to Identity Package and Governance Package preparation.

Artifacts:

- `worlds/korvin-merrow/world-spec-prep/clinical-story-skeleton-review.md`
- `worlds/korvin-merrow/world-spec-prep/clinical-story-skeleton-ratification.md`
- `worlds/korvin-merrow/world-spec-prep/physician-decision-log-02.md`

Ratified guardrails:

- Friction is Endocrinology vs Primary Team, not Endocrinology vs Documentation.
- Prednisone Source-of-Truth Hierarchy: rheumatology attending recommendation > verified medication reconciliation > pharmacy / refill history > family report > patient recollection.
- Family vs Primary Team remains balanced with defensible positions on both sides.
- Near-fall remains intentionally multi-factorial with no single intended explanation.

Boundaries:

- Do not draft World Spec yet.
- Do not create final file inventory.
- Do not create task prompts, golden responses, grader guidance, or synthetic chart files.

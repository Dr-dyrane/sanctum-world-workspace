# A3 - Status, log, and tracking-doc accuracy audit (2026-06-18)

Read-only audit of the OV status/log/tracking/prereg docs against the live Studio board (ground truth, 2026-06-18). No files were edited. This report lists, file by file, the exact updates needed to make every status doc accurate, with old -> new text quoted where possible.

## Ground truth used (2026-06-18 live board)

- Delivered (5): OV01 (Task 1, Med Reconciliation), OV02 (rpfl3eac, Transcription), OV03 (ckrz3598, Transcription), OV04 (jqxv7246, Transcription), OV06 (1rqn2959, Referral Intake/Triage).
- Awaiting first human review (2): OV08 (l6jo01e4, Utilization Review), OV09 (ebv61af9, Post-Acute Coordination, mean ~0.62, FA/GA submitted).
- In first human review (1): OV07 (ah6e821b, Claims Denial, off-text wound image, FA/GA done, reviewer Larry).
- Running Taiga trajectories now (2): OV05 (37cd058a, Referral Intake/Triage, skilled-wound-care downgrade), OV10 (ilsjf671, Discharge Summary, bone-health/CKD-MBD over-closure).
- 7 distinct lanes: Med Reconciliation (OV01); Transcription (OV02/03/04); Referral Intake/Triage (OV06 + OV05); Claims Denial (OV07); Utilization Review (OV08); Post-Acute Coordination (OV09); Discharge Summary (OV10).

## Headline findings

1. **There is no single accurate running status doc.** DO-NOT-REPEAT #17 mandates one `OV-WORLD-STATUS.md` (per-task lifecycle table + append-only dated log) as the single source of truth. The file exists but is frozen at 2026-06-17, knows only 5 Studio tasks, and is internally the most stale of all the trackers. Meanwhile the freshest narrative lives scattered across WORKFLOW-MAP.md (header only), OV-FLOOR-MECHANISM-LIBRARY.md (06-18 additions), and OV-TASK-IDEA-AUDIT (06-17). State has fragmented across at least four docs - the exact failure mode #17 was written to prevent.
2. **No tracking doc carries the live Studio board IDs for OV07-OV10.** Every doc tracks internal pilot job IDs (a33db3d0, d4eaa31b, cc337773, etc.), not the Studio task-board IDs. The ground-truth IDs l6jo01e4 (OV08), ebv61af9 (OV09), ah6e821b (OV07), 37cd058a (OV05), ilsjf671 (OV10) appear in NONE of the status docs. This is a systemic gap, not a single typo.
3. **The lifecycle vocabulary is stale everywhere.** No doc reflects "Delivered" (board shows OV01/02/03/04/06 delivered), the awaiting-review / in-review / running-Taiga split, OV05's revival, OV07-OV10's floored-and-uploaded state, or the 7-lane count. Most docs still say OV05 "Retired," OV07 "pending Studio upload / awaiting pilot," and "four/six lanes."

Recommendation: rewrite OV-WORLD-STATUS.md as the single source of truth (proposed contents in the last section), prune its 101-entry append-only log, and have the other docs point to it rather than re-state status. Detail below.

---

## File-by-file updates needed

### 1. OV-WORLD-STATUS.md  (SINGLE SOURCE OF TRUTH - most stale, highest priority)
160 lines, 101 append-only log entries. Header claims "SINGLE SOURCE OF TRUTH" but the body is frozen at 2026-06-17 and knows only 5 tasks. Every section below is wrong against ground truth.

- **Line 3 (Last updated):** `Last updated: 2026-06-17, OV06 v2 floor recorded after de-telegraphed re-pilot.` -> update to 2026-06-18 with the current posture (5 delivered, 2 awaiting review, 1 in review, 2 running Taiga).
- **Line 5 (Current posture):** the whole paragraph is wrong. It says "the Studio task board shows five OV tasks. OV01, OV02, OV03, and OV04 are Ready for Delivery. OV06 v2 is still in Task Writing as `Task 1rqn2959`... OV05 is retired and no longer a live Studio lane." -> Ground truth: OV01/02/03/04/06 are **Delivered**; OV05 is **revived and running Taiga** (37cd058a); OV07-OV10 exist and are floored/uploaded. Rewrite entirely.
- **Lines 7-17 (Studio task board table, "observed 2026-06-17"):** only 5 rows, all "Ready for Delivery" or "Task Writing." -> Replace with a 10-row board reflecting Delivered / Awaiting review / In review / Running Taiga, and add the live Studio IDs (l6jo01e4, ebv61af9, ah6e821b, 37cd058a, ilsjf671) which are entirely absent. Line 17 ("Hash-to-OV mapping is now board-synced for the five visible tasks above") is false - it is 5 of 10.
- **Lines 25-34 (Active task status table):** stale per row.
  - Row OV01-OV04 `Current state ... Studio status is Ready for Delivery` -> `Delivered`.
  - Line 33 `| Retired | OV05 | Home-medication-bottle and salt-substitute routes repeatedly ceilinged...` -> OV05 is **revived**: rebuilt 2026-06-18 as a skilled-wound-care downgrade on the Referral lane (OV06 conflicting-authority engine, 2nd task on that lane), now **running Taiga** (37cd058a). Packet at `platform/task5/current/`, not the archived path.
  - Line 34 `| Active | OV06 | ... Studio task `Task 1rqn2959` is in Task Writing...` -> OV06 is **Delivered**.
  - Missing rows entirely: OV07 (Claims Denial, in review, Larry), OV08 (Utilization Review, awaiting review), OV09 (Post-Acute Coordination, awaiting review, FA/GA submitted), OV10 (Discharge Summary, running Taiga). Add all four.
- **Lines 36-48 (Current visible working files):** add OV07/08/09/10 packets (`platform/task7|8|9|10/current/`); change line 45 OV05 from the archived retired path to `platform/task5/current/`; add OV07-OV10 FA/GA files under `phase-4-pilot-review-submit/fa-ga/`.
- **Lines 59-160 (Activity log):** the log stops at 2026-06-17 (line 156 board sync, line 157 OV06 v2 floor, lines 158-160 OV07). It is missing every 2026-06-18 event: OV08 built+floored (d4eaa31b), OV09 v3 ceiling (e9c38261) -> v4 floor (cc337773) + FA/GA, OV10 built, OV05 revival+rebuild, the FA/GA-canonical work, all five Studio uploads, and the delivery transitions. Append the 06-18 entries. Note also the log is out of date order (line 156 is 06-17, line 157 is dated 06-16) - re-sort or annotate.
- **Structural:** at 101 entries the log is the sprawl DO-NOT-REPEAT #17 warns about. Recommend archiving entries older than ~7 days to an `archive/` log and keeping the running file lean.

### 2. WORKFLOW-MAP.md  (header current, tables stale - internally contradictory)
This is the only doc with a 2026-06-18 narrative, but the tables below it were never updated, so the file contradicts itself.

- **Line 3:** `Updated 2026-06-17, reconciled to the live Studio board screenshot` -> the body header (line 5) is dated 06-18; reconcile the "Updated" line to 2026-06-18.
- **Line 5 (State block, 06-18):** mostly correct on floors but stale on lifecycle and lane count. It says "eight confirmed floors. OV01, OV02, OV04 Ready for Delivery; OV03 floored (FA/GA done)..." -> OV01/02/03/04/06 are now **Delivered**, not RFD/floored-pending. It says "Six lanes in use" in one clause but the OV10 clause at the end says "7th lane" - the count should read **7 lanes** consistently. OV05 "pilot-ready" -> now **running Taiga** (37cd058a). OV10 "pilot-ready" -> **running Taiga** (ilsjf671).
- **Lines 7-17 (Held table) - STALE, the biggest contradiction:**
  - Only 7 rows; OV08, OV09, OV10 are missing entirely though the header above declares them floored.
  - Line 15 `| OV05 | none live | ... | Retired 2026-06-16 after repeated ceilings |` -> OV05 is **revived**, Studio ID 37cd058a, Referral lane, running Taiga. (Directly contradicts the line-5 header, which already says "OV05 revived.")
  - Line 16 OV06 `| Task 1rqn2959 | ... | FLOORED v2 ... banking |` -> **Delivered**.
  - Line 17 `| OV07 | (pending Studio upload) | Claims Denial ... FLOORED v1 ... FA/GA pending a floor-run transcript |` -> OV07 is **uploaded and in first human review** (Studio ID ah6e821b, reviewer Larry); FA/GA is **done**, not pending.
  - Rows OV01-OV04 `Ready for Delivery` -> `Delivered`.
  - Add Studio IDs to the table (the "Studio ID" column shows "Task 1rqn2959", "(pending Studio upload)", etc. - replace with l6jo01e4, ebv61af9, ah6e821b, 37cd058a, ilsjf671 for OV05/07/08/09/10).
- **Line 19 (lane summary):** `Four lanes in use: Medication Reconciliation (OV01), Medical Transcription ... (OV02, OV03, OV04, retired OV05 history), Referral ... (OV06), and Claims Denial ... (OV07). ... For coverage, OV08 should take another distinct fresh open lane.` -> **Seven lanes** in use (add Utilization Review = OV08, Post-Acute Coordination = OV09, Discharge Summary = OV10; OV05 now lives on the Referral lane, not "retired history"). The OV08 forward-looking sentence is obsolete.
- **Lines 21-31 (Open table):** lists "Utilization Review Concurrent Stay Documentation" (P1) as still **open** - but OV08 was built on it and floored. Remove that row (and reconcile the others against what is now built). The note "Coding/DRG and CDI Query back in play" from the line-5 header should be reflected here.
- **Lines 32-34 (Build rule):** `Four Ready for Delivery tasks are banked. OV06 v2 floored and is now in the banking lane.` -> Five delivered, plus four more floored/uploaded; OV06 is delivered, not "in the banking lane."
- **Lines 36-38 (Open reviewer item):** only lists OV01 (cleared). -> Add the current open reviewer item: OV07 in first human review with Larry.

### 3. 00-START-HERE.md  (Cockpit - stale, frozen 2026-06-17)
The world cockpit/entry doc. Reads as if OV07 is still in build prep and OV08-OV10 do not exist.

- **Line 3 (Status):** `Status (2026-06-17): WORLD OPEN FOR TASKING. ... OV01, OV02, OV03, and OV04 are Ready for Delivery. OV05 is retired after repeated ceilings. OV06 v2 is still in Task Writing as `Task 1rqn2959`... It is OV's fifth confirmed floor.` -> Rewrite to 06-18: 5 delivered (OV01/02/03/04/06), OV07 in review, OV08/OV09 awaiting review, OV05/OV10 running Taiga; eight confirmed floors.
- **Lines 5-12 (Current lanes list):** stops at OV07 and mislabels several.
  - Line 10 `OV05 - home-medication-bottle and later salt-substitute routes. Retired 2026-06-16; packet archived...` -> revived, Referral lane skilled-wound-care downgrade, `platform/task5/current/`, running Taiga.
  - Line 11 `OV06 - ... v2 floored in Task Writing under `Task 1rqn2959`...` -> Delivered.
  - Line 12 `OV07 - Claims Denial Appeal, TS7. Build prep active at ... task7/current/; ... wound image staged...` -> OV07 floored (job a33db3d0), uploaded, in first human review (ah6e821b), FA/GA done.
  - Add lines for OV08 (Utilization Review, floored, awaiting review), OV09 (Post-Acute Coordination, floored, awaiting review), OV10 (Discharge Summary, built, running Taiga).
- **Line 14 (Next):** `Next: bank OV06 v2 with golden self-score ... Do not revive OV05 ...` -> OV06 is delivered and OV05 has been revived; rewrite the next-action and drop the "do not revive OV05" instruction (already overtaken).
- **Lines 50-55 (Submission status 2026-06-17):** line 54 `TASKING: OV01, OV02, OV03, and OV04 are Ready for Delivery. OV05 is retired. OV06 v2 is still in Task Writing...` -> update to the 06-18 delivered/in-review/running-Taiga state. Line 55 "NEXT ELIGIBLE ACTION: bank OV06 v2" is obsolete.
- **Line 24 (Read order item 5):** lists task1/2/3/4/6/7 packets - add task5 (current), task8, task9, task10.

### 4. OV-CANDIDATE-QUEUE.md  (stale, frozen 2026-06-16)
Header says "SOURCE OF TRUTH for what to test next." Predates OV07-OV10 entirely.

- **Line 6:** `BANKED FLOORS (Ready for Delivery): OV01 ..., OV02 ..., OV04 .... OV05 = fair catcher, in Taiga QA.` -> OV05 is no longer a catcher in QA; it was retired then revived as a Referral conflicting-authority floor. OV03/OV06/OV07/OV08/OV09 floors are all missing from this "where things stand."
- **Lines 9-14 (OV03 block "bank pending golden self-score"):** OV03 is delivered. The whole "FLOORED, v2 CONFIRMED (bank pending...)" framing is obsolete.
- **Line 21 (Edmund conflicting-authority, queue item 3):** marked "BUILT INTO OV06 ... AWAITING pilot" then later "v2 ... FLOOR ... Bank pending golden self-score." -> OV06 delivered. Also note the conflicting-authority engine was **re-used for the revived OV05** - the queue does not record this.
- **Line 23 (Quiet-unsafe-move, queue item 4):** "RETIRED 2026-06-16" - but the underlying OV05 slot was rebuilt 06-18 on a different mechanism (skilled-wound-care downgrade). Queue does not reflect the revival.
- **Recommendation:** this doc has been overtaken by OV-TASK-IDEA-AUDIT (06-17) and by events. Either fold its live content into the single status doc and archive it, or add a top banner "SUPERSEDED 2026-06-18, see OV-WORLD-STATUS.md / OV-TASK-IDEA-AUDIT" so it is not mistaken for current.

### 5. OV-TASK-IDEA-AUDIT-2026-06-17.md  (near-current but pre-OV10/pre-revival; dated artifact)
The most accurate per-task table, but it is a point-in-time audit (06-17) and is now one day stale.

- **Line 7:** `Seven confirmed floors built and floored. OV09 is the pilot-ready eighth. OV05 retired. Six distinct workflow lanes in use.` -> Eight confirmed floors (OV09 floored 06-18). OV05 **revived** (not retired). **Seven** lanes in use (OV10 added Discharge Summary; OV05 re-added to Referral).
- **Lines 9-19 (per-task table):** row OV05 `CEILING 10/10, RETIRED` -> revived; row OV09 `FLOOR (banking)` -> floored, awaiting human review (ebv61af9); add an OV10 row (Discharge Summary, bone-health/CKD-MBD over-closure, running Taiga, ilsjf671). Lifecycle column shows none of the delivered/in-review states.
- **Line 18:** uses job id d4eaa31b for OV08 - correct as the pilot job, but the Studio board ID l6jo01e4 is absent (consistent gap across all docs).
- **Lines 89-98 (The count / Recommendation):** "Confirmed floors built: 7. Pilot-ready eighth: OV09. ... Distinct lanes used: 6." and recommendation 2 "build A2 (bone-health) ... or A1" -> A2 was built as **OV10** (Discharge Summary) on 06-18; the recommendation is now executed, not pending. Update the count to 8 floors / 7 lanes and mark recommendation 2 done.
- **Note:** because this is a dated point-in-time audit, the cleanest fix is to leave it as the 06-17 snapshot and let OV-WORLD-STATUS.md carry the live count, rather than mutate a dated file. Flag this in the status doc as "superseded by the 06-18 board."

### 6. OV-FLOOR-MECHANISM-LIBRARY.md  (design reference - mostly current on mechanisms, light status drift)
This is a design/lessons doc, not a status tracker, and its 2026-06-17/06-18 additions (lines 45-47, section 8) are accurate on the floor mechanisms (OV08 background-line floor, OV09 v3 ceiling 0.84 -> v4 floor cc337773 mean ~0.62 "eighth banked floor"). Minimal changes needed:

- The ledger and refinements correctly capture OV08 and OV09 v4. **OV10 and the revived OV05 are not yet in the ledger** - if the library is meant to log every tested lever, add an OV10 (Discharge Summary over-closure) row and an OV05-revival (skilled-wound-care downgrade) row once they pilot.
- Header line 3 dated 2026-06-15; the body has 06-17/06-18 additions. Acceptable for a living reference, but bump the date if it is treated as authoritative.
- No lifecycle/delivery claims to correct here (it tracks mechanisms, not board status). Lowest-priority doc.

### 7. OV-APPROACH-MEMO.md and OV-FRESH-TASK-IDEAS.md  (doctrine/idea banks - low status content)
- **OV-APPROACH-MEMO.md** (06-16): a one-page doctrine memo on what works/fails. It states mechanism lessons, not task status, so it is not stale in a status sense. Optional: add OV06/OV07/OV08/OV09 as further confirmations of "the engine that works." No required status edit.
- **OV-FRESH-TASK-IDEAS.md** (06-15): explicitly self-labels "partly stale" and "RECONCILIATION (read first)." Its "do not duplicate" list stops at OV05 and predates OV06-OV10. Low risk because it is flagged as an idea bank, but its reconciliation banner should be updated to point to OV-WORLD-STATUS.md for the current built-lever list, or it should be archived.

### 8. Per-task prereg + RUN-INSTRUCTIONS (phase-3 platform/taskN/current)
Spot-check scope only (not a full read of all 10). These are point-in-time pilot prereg docs and are expected to be version-stamped, not continuously updated, so they are not "stale" in the status sense. Two hygiene notes:
- task5/current holds the **revived** OV05 packet (`OV05-pilot-preregistration.md`, started_referral_coordination_note, home_health_intake_review) - confirming OV05 was rebuilt on the Referral lane; the retired bottle-photo packet is correctly separated under `platform/task5/archive/2026-06-16-retired/`. Good.
- task8/9/10 each carry a current prereg + DESIGN-grounding + RUN-INSTRUCTIONS and the built deliverables - consistent with OV08/09/10 being built. No correction needed; these corroborate ground truth.

---

## Recommendation: rewrite OV-WORLD-STATUS.md as the single source of truth

DO-NOT-REPEAT #17 already mandates exactly this and even names the file. The fix is not to create a new doc but to **rewrite the existing OV-WORLD-STATUS.md** so it is actually current, prune its log, and demote the other trackers to pointers. Proposed contents:

### A. Header
One posture line dated 2026-06-18: "5 delivered (OV01/02/03/04/06), 1 in first human review (OV07), 2 awaiting first human review (OV08, OV09), 2 running Taiga trajectories (OV05, OV10); eight confirmed floors across seven distinct lanes."

### B. Per-task lifecycle table (the core) - one row per task, with Studio IDs

| Task | Studio ID | Lane | Mechanism | Pilot outcome (job) | Lifecycle state |
|---|---|---|---|---|---|
| OV01 | Task 1 | Med Reconciliation | cold knowledge (stop inpatient enoxaparin) | FLOOR (741ba52f) | Delivered |
| OV02 | rpfl3eac | Transcription | off-text text synthesis (line infection) | FLOOR 10/10 ~0.10 | Delivered |
| OV03 | ckrz3598 | Transcription | embedded carry-forward (discharge insulin) | FLOOR 0.05-0.20 (048aa8eb) | Delivered |
| OV04 | jqxv7246 | Transcription | off-text image (CPAP adherence) | FLOOR bimodal | Delivered |
| OV05 | 37cd058a | Referral Intake/Triage | conflicting-authority (skilled-wound-care downgrade) | running Taiga | Running Taiga trajectories |
| OV06 | 1rqn2959 | Referral Intake/Triage | embedded wrong, de-telegraphed (perfusion closure) | FLOOR 0.39 (577effae) | Delivered |
| OV07 | ah6e821b | Claims Denial | off-text image (wound undermining) | FLOOR 0.51 (a33db3d0) | In first human review (Larry) |
| OV08 | l6jo01e4 | Utilization Review | embedded wrong (antibiotic route, no OPAT) | FLOOR 0.63 (d4eaa31b) | Awaiting first human review |
| OV09 | ebv61af9 | Post-Acute Coordination | embedded wrong (held-med resume, background line) | FLOOR ~0.62 (cc337773); v3 ceiling 0.84 (e9c38261) retired | Awaiting first human review; FA/GA submitted |
| OV10 | ilsjf671 | Discharge Summary | embedded wrong (bone-health/CKD-MBD over-closure) | running Taiga | Running Taiga trajectories |

(OV05 history: bottle-photo med-rec image retired 2026-06-16 after 3 ceilings; slot rebuilt 2026-06-18 on the Referral lane. OV09 history: v1 contrast ceiling 0.84, v2 osteo-image retired, v4 held-med-resume floored.)

### C. Lane summary
Seven distinct lanes: Med Reconciliation (OV01); Transcription (OV02/03/04); Referral Intake/Triage (OV06 + OV05); Claims Denial (OV07); Utilization Review (OV08); Post-Acute Coordination (OV09); Discharge Summary (OV10). Target 8-10 shippable across 6-7 lanes - met.

### D. Append-only dated activity log
Keep the log, but (1) carry forward only recent entries and archive the older ~90 to `archive/`, and (2) backfill the missing 2026-06-18 events: OV08 built+floored (d4eaa31b) + FA/GA; OV09 v3 ceiling (e9c38261) -> v4 floor (cc337773) + FA/GA; OV10 built; OV05 revived + rebuilt on Referral; fa-ga-canonical standard written; the five Studio uploads (OV05/07/08/09/10) and IDs; and the delivery transitions for OV01/02/03/04/06.

### E. Pointers (not restatements)
Link WORKFLOW-MAP.md, OV-FLOOR-MECHANISM-LIBRARY.md, OV-CANDIDATE-QUEUE.md, OV-TASK-IDEA-AUDIT, the prereg/results/FA-GA docs - and add a one-line "for live status, this file governs" banner to WORKFLOW-MAP.md, 00-START-HERE.md, and OV-CANDIDATE-QUEUE.md so status stops being duplicated across four docs.

## Priority order for the fixers (Wave 2)
1. OV-WORLD-STATUS.md - full rewrite (single source of truth; most stale; mandated by #17).
2. WORKFLOW-MAP.md - fix the Held table, lane count, and Open table to match its own 06-18 header.
3. 00-START-HERE.md - rewrite Status line, lanes list, submission status.
4. OV-CANDIDATE-QUEUE.md - add a superseded banner or fold into the status doc.
5. OV-TASK-IDEA-AUDIT - leave as a dated 06-17 snapshot; note "superseded" in the status doc (or bump count + mark recommendation 2 done).
6. OV-FLOOR-MECHANISM-LIBRARY.md / OV-APPROACH-MEMO.md / OV-FRESH-TASK-IDEAS.md - low priority; add OV10/OV05-revival ledger rows and a reconciliation banner only.

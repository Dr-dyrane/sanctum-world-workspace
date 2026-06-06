# Task 1 - Second Human Review (Abimbola O / Abi, 2026-06-06)

Status: SEND BACK. Task 1 cannot clear yet. Round-1 changes were accepted; the new blocker is difficulty, not realism or format.

## Verdict
The round-1 rework was incorporated well and responsiveness was appreciated. The blocking problem now is that all 10 v3 trajectories scored at least 90 percent, which means there was no significant clinical failure and the task was too easy for the model. A task cannot clear with those two problems together.

## Hard requirement for clearance
There must be a significant clinical failure AND at least one trajectory below 90, with a preference for below 70 (stated as a preference, not a hard and fast rule).

## How to fix (Abi's suggestions)
Redo the task to make it harder. Ask Claude how to make it harder. One concrete option she offered: re-add the medication safety handoff and put a trap or red herring in it, as long as the dates are accurate and any other realism defects do not return. Do not simply restore the old answer-giving handoff; a hardening file must create difficulty without becoming an answer file.

## FA/GA format note
Content is much better. Future and resubmitted FA and GA should be written as natural prose with complete sentences, not bullets, and should remove the section headers. Single lowest run only, 2 to 3 sentences each.

## Offer
She offered to review the next version before submission so the bonus is protected. Reach out to her before resubmitting.

## Hospital-name point (resolved)
She separately noted that a hospital or clinic document should carry the hospital name in the header for realism, then checked the golden herself and confirmed it was already there ("we are all good").

---

## Abi's worked FA/GA prose SAMPLES (preserve verbatim - the target voice for every task)

These are her own examples of the prose form she wants. Use as the style anchor for Tasks 1 through 6. Note: single run, complete sentences, no bullets, no headers, names the trajectory number, leads with what the model did well then states the main failure plainly.

### Sample FA (her example)
"On trajectory 7, the model did well on the anchor points. It cross referenced the microbiology results with the nursing flowsheets, determined that step down to a lower spectrum beta lactamase agent was appropriate for MSSA and discontinued vancomycin. It continued parenteral antibiotics instead of oral as the patient was still febrile. It did not combine bacterial tracheitis and tracheal stoma cellulitis into a single diagnosis and it called out the need for the primary team to respond to the malnutrition classification query. The main model failure is that it stated that the negative blood culture at 48 hours was a final result which is incorrect (not final till 5 days). While the model did not immediately switch from vancomycin to oxacillin/cefazolin, is reasonable for the PGY 2 resident to defer the final call on the antibiotic start to the attending. Presenting the main idea is more important."

### Sample GA (her example)
"The grader was incorrect to state that the model's interpretation of the blood culture result was right. The model states that the negative blood culture at 48 hours was the 'final' result which is incorrect. The blood culture result is not final till 5 days. The grader guidelines explicitly places this in the 0.6-0.8 band and so the grader should have graded the model lower. The grader was otherwise correct that the model identified the need to step down the antibiotics due to the culture and sensitivity results, the need to plan for oral step down therapy. The model surfacing the need to respond to the malnutrition classification request by the primary team was appropriately graded."

### Sample FA (Task 4 RCA, her example)
"On trajectory 6, the model correctly identifies most of the anchor items, it identifies the fracture as pathologic due to osteopenia and metabolic bone disease. It recognizes the missed escalation after the pop was heard during discharge and it identifies the 3 month gap in calcium and vitamin D supplementation. However, the model fails to mention the 14 month DXA surveillance gap in this complex patient as a failure, it is excessively lengthy and it drifts out of scope by going in depth into the miralax aspiration event and framing it as a contributor to the fracture event which it is not. The aspiration event is a separate patient safety issue and is not requested by the prompt. The document is otherwise a strong RCA document in the right framework."

### Sample GA (Task 4 RCA, her example)
"The grader scored the model within the 0.6-0.8 band which is appropriate. The model produced a solid RCA report but missed out on the DXA anchor and the document was overproduced. In addition, the model drifted out of scope by linking the aspiration event that led to pneumonia to the pathologic fracture when these are two unrelated patient safety events. The penalty the grader applied for these were appropriate. The model devoted lengthy sections to hospitalization events without relevance to the requested RCA (conflicting baclofen friction, chest xray findings, aspiration event, miralax omission). In addition, there were repetitions and redundancy between section 3 and 4 (failed med rec, no physician notification) that contributed to the excessive length of the document."

## Lessons banked (so we do not repeat)
1. Clean and realistic is not sufficient. A task that scores all 10 runs at or above 90 with no significant clinical failure CANNOT clear. Every task needs a designed failure mode (target at least one run below 90, ideally below 70). See TASK-RUNBOOK A0 "ENGINEERED FAILURE MODE."
2. The adversarial task file is the sanctioned lever: a realistic, authoritative document that makes a plausible but wrong recommendation the chart can rebut. Correct behavior is to catch and decline it. It must not become an answer file.
3. FA/GA is natural prose, complete sentences, no bullets, no headers, single lowest run, names the trajectory. See A0 "FA/GA PROSE FORM" and the verbatim samples above.
4. Reach out to Abi before resubmission; she offered the pre-check to protect the bonus.

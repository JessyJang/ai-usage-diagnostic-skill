---
name: ai-usage-diagnostic
description: Evidence-grounded diagnostic of practical AI usage maturity. Uses six anchored dimensions, separates confidence from skill, resists flattery, recommends one measurable next step, and supports evidence-based reassessment. Trigger on requests to rate, diagnose, benchmark or improve actual AI use.
version: 2.1.0-beta.1
language: zh-CN
---

# AI Usage Diagnostic — V2.1 beta.1

## Scope and truth standard
This is **practical coaching, not a psychometrically validated test**. Grade demonstrated behavior, NOT frequency, tool count, brand/model names, self-awarded titles, eloquence or claimed revenue. Never infer that accessible memory is a complete record. Avoid mandatory questionnaires, purchases, dashboard building and recruiting testers.

Read `references/scoring-protocol.md` and `references/output-contract.md` before scoring. These are normative; older reference files are legacy examples only. Tests are specifications, not evidence of empirical model success.

## 1 — Route and evidence scope
- **History**: assess accessible conversations, uploaded artifacts and verifiable outcomes. State accessible period and gaps. Do not imply unobserved work did not happen.
- **Case intake**: if few examples exist, request **one** recent concrete episode (goal → AI use → correction → outcome); optionally ask up to four additional short examples when needed, without a form.
- **Fast**: 1–2 concrete episodes; concise provisional score, six dimensions with unknowns; one practical action.
- **Deep**: at least 3 distinct episodes spanning 2 tasks, or substantial accessible history; fuller diagnosis.
- **Reassessment**: compare explicitly identified baseline and genuinely new evidence. Never treat time passing or better documentation as automatic skill improvement.

Construct an internal evidence ledger with `ID | observation | user-reported / directly observed / independently inspected | date/context | grade A/B/C/U | supports | limits/alternative explanation`.
- A = inspectable independent artifact OR repeated directly observed relevant behavior.
- B = specific user-reported behavioral episode or single directly observed interaction with limited outcome verification.
- C = broad claim, role label, intent or uncorroborated assertion; **not sufficient alone** to establish a dimension.
- U = unavailable; **not zero**.
Use no invented dates or fabricated longitudinal access. A verified publication proves shipping, *not* adoption, conversion or usefulness.

## 2 — Six fixed core dimensions
Use only these six universally, in this order:
1. 问题定义 — context, constraints, acceptance criteria proportional to task.
2. 批判验证 — error detection, factual/quality checks, evidence-informed corrections.
3. 执行交付 — usable, completed and actually released/used deliverables.
4. 复用运营 — demonstrated repeat use and maintenance, not just saved Skills/templates.
5. 结果反馈 — checking outcomes relevant to stated purpose; qualitative evidence counts.
6. 判断取舍 — scope, priorities, cost-benefit decisions, stopping work appropriately.

Each score must cite at least one identifiable A or B episode and a behavioral anchor from `references/scoring-protocol.md`; otherwise mark `未知`. A dimension can be scored with B but confidence is limited. Lack of sales doesn't reduce hobbyist scores; lack of engineering prowess doesn't reduce noncoding workflows.

## 3 — Score decision (not an average)
First construct strongest plausible **lower-level interpretation**; separate user causes from model/tool/environment causes. Then match total demonstrated pattern against holistic ladder in `references/scoring-protocol.md`.
- **No concrete A/B episode**: no numeric score; ask for one case.
- **At least one A/B episode**: display **one-decimal point estimate** `AI 使用总分：X.X / 10`, marked `暂定` when coverage insufficient. Tenths are communication, not measurement precision.
- Don't average six dimensions. Unknown isn't zero.
- **8+**: require demonstrated critical verification and effective actual delivery; merely building agents does not qualify.
- **9+**: require demonstrated recurring reuse, outcome feedback and improvement on more than one occasion.
- **10**: exceptional independently supported sustained system-level results across contexts; extremely rare.
- Explain `为何不是高一档/低一档`; declare uncertainty. Separate `证据可信度：高/中/低` from skill.
- Don't preserve earlier scores by inertia or increase because user argues confidently.

## 4 — Causal critique and anti-flattery
Identify 2 strengths and **at most 2** bottlenecks, each supported by evidence ID(s). For every negative diagnosis, check alternative causes: model execution, tools, external constraints, missing data and task ambiguity. A lengthy revision cycle **does not alone prove poor upfront specifications**. Classify cause `用户行为 / AI或工具限制 / 外部条件 / 未知`, assign user weakness only with evidence.

Red-team: give strongest plausible overestimation case, label supported/partly supported/unsupported, then adjudicate. Avoid theatrical harshness. Distinguish outputs, shipping, adoption and measurable impact.

## 5 — Choose ONE intervention
Select most feasible bottleneck for user's goal. Reference an episode. Recommend one 7–30-day low-cost/no-new-tool experiment with `baseline | action | observable pass/fail | evidence to save | decision after test`. Without metrics, explicit quality checks or repeated reuse count. Don't prescribe mandatory dashboards, AI OS, purchases or fewer projects.

## 6 — Output contract
Follow `references/output-contract.md`. Place score/unknown, level, confidence, provisional/formal near top. Include six dimensions, evidence mapping, alternative causes, Red Team, why not higher/lower, one action, score-changing evidence.

## 7 — Reassessment protocol
Baseline copyable record: `date; evidence IDs + source classes; available period; six scores/unknowns; overall X.X; confidence; leading hypothesis; experiment + pass/fail`.
At follow-up: show **same criteria** and `new evidence → dimension → score or confidence delta`. More visibility isn't necessarily improved ability. Correct old assessments if evidence classification was wrong; don't call correction personal progress.

## 8 — Pilot/testing integrity
Use `tests/validation-matrix.md` for cases and `tests/run-log.csv` for executed runs. Static structure checks do not prove diagnostic accuracy. Never claim model consistency/fairness/accuracy without logged actual executions. Maintain Beta status until independent validation. Mask identities and sensitive data, obtain consent before retaining user prompts.
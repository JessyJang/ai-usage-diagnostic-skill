---
name: ai-usage-diagnostic
description: Evidence-grounded diagnostic of practical AI usage maturity. Uses six anchored dimensions, separates confidence from skill, resists flattery, recommends one measurable next step, and supports evidence-based reassessment. Trigger on requests to rate, diagnose, benchmark or improve actual AI use.
version: 2.1.0-beta.1
language: zh-CN
---

# AI Usage Diagnostic — V2.1 beta.1

## Scope and truth standard
This is **practical coaching, not a psychometrically validated test**. Grade demonstrated behavior, NOT frequency, tool count, brand/model names, self-awarded titles, eloquence or claimed revenue. Never infer that accessible memory is a complete record. Avoid mandatory questionnaires, purchases, dashboard building and recruiting testers.

Read `references/scoring-protocol.md` and `references/output-contract.md` before scoring. These are normative; older reference files in this package are legacy examples only. Tests are specifications, not evidence of empirical model success.

## 1 — Route and evidence scope
- **History**: assess accessible conversations, uploaded artifacts and verifiable outcomes. State accessible period and any gaps. Do not imply unobserved work did not happen.
- **Case intake**: if few examples exist, request **one** recent concrete episode (goal → AI use → correction → outcome); optionally ask up to four additional short examples when needed, without a form. If user wants diagnosis immediately, use available evidence and label provisional.
- **Fast**: 1–2 concrete episodes; concise provisional score, six dimensions with unknowns; one practical action.
- **Deep**: at least 3 distinct episodes spanning 2 tasks, or substantial accessible history; fuller diagnosis.
- **Reassessment**: compare explicitly identified baseline and genuinely new evidence. Never treat time passing or better documentation as automatic skill improvement.

Construct an internal evidence ledger with `ID | observation | user-reported / directly observed / independently inspected | date/context | grade A/B/C/U | supports | limits/alternative explanation`.
- A = inspectable independent artifact OR repeated directly observed relevant behavior.
- B = specific user-reported behavioral episode or single directly observed interaction with limited outcome verification.
- C = broad claim, role label, intent or uncorroborated assertion, **not sufficient alone** to establish a skill dimension.
- U = unavailable; **not a zero**.
Use no invented dates or fabricated longitudinal access. A verified publication proves shipping, *not* adoption, conversion or usefulness.

## 2 — Six fixed core dimensions
Use only these six universally, in this order:
1. 问题定义 — context, constraints, acceptance criteria proportional to task.
2. 批判验证 — error detection, factual/quality checks, evidence-informed corrections.
3. 执行交付 — usable, completed and actually released/used deliverables.
4. 复用运营 — demonstrated repeat use and maintenance, not just saved Skills/templates.
5. 结果反馈 — checking outcomes relevant to stated purpose; qualitative evidence counts.
6. 判断取舍 — scope, priorities, cost-benefit decisions, stopping work appropriately.

Each score must cite at least one identifiable A or B episode and a behavioral anchor from `references/scoring-protocol.md`; otherwise mark `未知`. A dimension can be scored with B but confidence is limited. Lack of sales doesn't reduce hobbyist scores; lack of engineering prowess doesn't reduce noncoding workflows. Context-specific observations may appear in narrative but never silently replace core dimensions.

## 3 — Score decision (not an average)
First construct strongest plausible **lower-level interpretation**; separate user causes from model/tool/environment causes. Then match the total demonstrated pattern against holistic ladder in `references/scoring-protocol.md`.
- **No concrete A/B episode**: no numeric score; ask for one case.
- **At least one A/B episode**: always display a **one-decimal point estimate** `AI 使用总分：X.X / 10`, marked `暂定` when coverage insufficient. Choose tenths sparingly (.0/.2/.5/.8 where useful); this is a communication convention, not measurement precision.
- Score must not be computed by averaging six dimensions. Do not impute unknown as zero, nor silently assume it is strong.
- **8+**: require demonstrated critical verification and effective actual delivery across evidence; merely building agents does not qualify. Reuse may still be developing at level 8.
- **9+**: require demonstrated recurring reuse, outcome feedback and improvement on more than one occasion. An isolated good artifact is insufficient.
- **10**: exceptional independently supported and sustained system-level results across contexts; extremely rare.
- Explain `为何不是高一档/低一档` with evidence; declare any uncertainty. Separate `证据可信度：高/中/低` from skill level, considering coverage, independence, freshness and contradictions.
- Do not preserve prior scores by inertia; do not increase a score because the user argues confidently.

## 4 — Causal critique and anti-flattery
Identify 2 strengths and **at most 2** bottlenecks, each attached to episode ID(s). For every negative diagnosis, check at least one alternative cause: ambiguous brief? deficient model execution? unavailable tools? external constraints? lack of source data? imperfect checks? A lengthy revision cycle **does not alone prove poor upfront specifications**. Classify potential causes as `用户行为 / AI或工具限制 / 外部条件 / 未知` and only assign a user weakness with evidence.

Red-team challenge: give strongest *plausible* case that capability was overestimated, label supported / partly supported / unsupported, then adjudicate. Do not perform theatrical harshness. If no negative amplification is supported, state unknown, not assert procrastination/perfectionism. Distinguish outputs, shipped results, adoption and measurable impact.

## 5 — Choose ONE intervention
Pick the bottleneck with highest feasible leverage **for this user's goal**. Reference one concrete episode; give a 7–30-day low-cost/no-new-tool experiment with:
`baseline | action | measurable or observable pass/fail | evidence to save | decision after test`.
Do not overprescribe financial ROI, AI OS, dashboards, more tools, or reduced project count. When measured metrics are unavailable, count explicit pass/fail quality checks or demonstrated task reuse. Prioritize an intervention whose outcome would genuinely differentiate rival explanations.

## 6 — Output contract
Follow `references/output-contract.md`. Put score (or evidence-needed state), confidence, level and formal/provisional status **in the first screenful**. Include six scores or unknowns, concise evidence mapping, alternative-cause check, red team, why not ±1 stage, single intervention, and what would change the score. No false claims of independent inspection.

## 7 — Reassessment protocol
Baseline copyable record: `date; evidence IDs + source classes; available period; six scores/unknowns; overall X.X; confidence; leading hypothesis; experiment + pass/fail`.
At follow-up: show **same criteria** and `new evidence → which dimension → score or confidence delta`. State if evidence only improved visibility rather than behavior. If previous result was wrong because of source misclassification, correct the old assessment without presenting correction as personal progress. Invite counterevidence when appropriate without obliging a follow-up.

## 8 — Pilot/testing integrity
Use `tests/validation-matrix.md` for cases and `tests/run-log.csv` to record executed runs. Static lint in `tests/check_package.py` checks the artifact, **not** diagnostic validity. Never say model consistency, differential fairness or accuracy tests passed without actual logged executions and reviewer verdicts. Publish Beta status until those gates are independently fulfilled. Protect participant privacy: obtain permission before retaining prompts, mask identities and sensitive content, and allow synthetic examples.

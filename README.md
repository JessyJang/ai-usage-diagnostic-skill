# AI Usage Diagnostic Skill — v2.1.0-beta.1

基于实际行为证据，评估 AI 使用成熟度，识别盲点，并在长期复测中观察成长。

> 这是实用辅导工具，不是经过科学验证的心理测量或客观能力排名。

## 使用方法

将仓库文件安装到 Agent Skills 目录，要求 Agent 读取 `SKILL.md`、`references/scoring-protocol.md` 和 `references/output-contract.md`。

示例：
> 使用 ai-usage-diagnostic，根据实际可见的对话和成果评估我的 AI 使用能力。不要将证据缺失视作能力不足。请给出具体评分、可信度、主要瓶颈和一个可验证行动。

## 六个诊断维度

问题定义、批判验证、执行交付、复用运营、结果反馈、判断取舍。

## 评估原则

- 用实际行为证据，而非使用时长、工具数量或自称头衔打分
- 未观察到不等于能力不足；证据可信度与能力评分分开
- 区分模型/工具失败、用户行为及外部限制
- 发布不等于采用，采用不等于有效果
- 总分是整体锚点判断，**不是六维平均分**
- 复测必须比较新证据，不能因为时间过去而自动加分

## 安装

- Claude Code / Cursor：`.claude/skills/ai-usage-diagnostic/`
- Codex：`.codex/skills/ai-usage-diagnostic/`（依实际客户端路径）
- 其他兼容 Agent：依对应 Skill 目录约定

## 版本与验证状态

**v2.1.0-beta.1**（2026-10-09）。目前为 Beta，尚未通过独立模型一致性与真实用户效度验证。模拟测试案例是测试材料，不是已通过的测试结果。

请参阅 `SKILL.md`、`references/` 和 `tests/`。
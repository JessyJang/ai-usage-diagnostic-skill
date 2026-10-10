# AI Usage Diagnostic Skill — v2.1.0-beta.1

用于诊断用户实际 AI 使用成熟度，帮助找到一个最值得改善的行为。**它是基于行为证据的实用辅导工具，不是科学认证的心理测量或客观能力排行。**

## 使用
将此文件夹放入你的 Agent Skill 目录，并让代理读取 `SKILL.md`。示例：

> 使用 ai-usage-diagnostic，根据你能实际看到的对话与产物给我诊断。不要把未见到的行为当成能力不足；给具体分数和可信度、最大瓶颈及一个可验证行动。

如果没有历史，提供一个具体案例即可开始暂定评估。若需复测，保存输出中的基线，再带回后续真实结果。

## 本版核心改进
- 合并旧版冲突指令，唯一权威流程在 `SKILL.md`。
- 六个固定维度，独立证据等级；不把未知计为零。
- 区分用户行为、模型/工具问题、外部限制，避免误判。
- 区分“发布”“被采用”“获得效果”；避免无依据夸大商业价值。
- 打分是锚点判断而非六维平均；用 X.X 表达，非统计精度。
- 用单一、可检验的行动推动改变；复测只奖励新行为和真实效果。
- 22 项对抗用例、空白运行日志、离线结构校验工具。

## 验证状态
仅执行过本地静态结构校验。`tests/validation-matrix.md` 是测试计划；没有将测试案例标记为经过真实模型验证。公开传播时请保留 beta 标识。

## 安装示例
- Claude Code / Cursor：`.claude/skills/ai-usage-diagnostic/`
- Codex：`.codex/skills/ai-usage-diagnostic/`（以具体客户端实际路径为准）
- 其他兼容 Agent：按其 Skill 目录约定放入，并确保可以读取 SKILL.md。

## 目录
- `SKILL.md`：诊断工作流（权威）
- `references/scoring-protocol.md`：锚点与可信度
- `references/output-contract.md`：输出格式
- `tests/validation-matrix.md`：对抗测试规格
- `tests/run-log.csv`：未来实际测试记录
- `tests/check_package.py`：仅检查包结构
- `legacy/`：旧文档供追溯，不作为规则

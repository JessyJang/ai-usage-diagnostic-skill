# 合成数据测试说明

`synthetic-fixtures.json` 包含 22 条虚构输入，直接对应 validation-matrix.md 的 T01–T22。

使用方式：分别将每条 synthetic_input 作为用户消息，启用本 Skill，保存完整模型输出并由独立评审判定 expected_invariant。建议 T03/T07/T10/T15/T16 各重复 3 次，T16 追加更换工具名版本；比较评分和因果归因。

`check_simulated_fixtures.py` 仅校验案例数量、ID、字段、预期标注与敏感性规则覆盖。**不会调用任何 AI 模型，不能视作诊断通过率。**

不可把人工编写的参考分、预期标签或测试用例说成真实用户数据、模型实测结果。

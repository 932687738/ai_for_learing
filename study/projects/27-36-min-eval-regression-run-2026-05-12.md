# 第 27-36 课最小回归评测结果（baseline-2026-05-12）

## 1. 执行信息

- run_id: `baseline-2026-05-12`
- date: `2026-05-12`
- operator: `ai-course-mentor-course-mode`
- model_version: `N/A（课程文档回归）`
- prompt_version: `N/A（课程文档回归）`
- toolchain_version: `Cursor Agent + 本地文件校验`

## 2. 汇总结果

- cases_total: `10`
- cases_passed: `10`
- cases_failed: `0`
- rollback_required: `no`

说明：本次为课程文档层面的结构化与覆盖度回归，重点验证章节边界、评测框架、协议样例、可运行示例与治理闭环是否具备。

## 3. 分项结果

| 用例编号 | 课时 | 结果 | 结论摘要 |
| --- | --- | --- | --- |
| E27-skill-boundary | 27 | PASS | 已明确 skill/agent/tool 边界，并补学习闭环 |
| E28-framework-select | 28 | PASS | 框架对比与选型导向明确 |
| E29-search-eval | 29 | PASS | 已补检索/重排/生成拆分评测 |
| E30-eval-rubric | 30 | PASS | 已形成 eval 方法、模板与回归链接 |
| E31-protocol-schema | 31 | PASS | 已补 MCP schema、A2A task、错误码与幂等 |
| E32-model-routing | 32 | PASS | 已补评分卡、路由策略、升级门禁 |
| E33-security-baseline | 33 | PASS | 安全基线覆盖输入/权限/工具/审计 |
| E34-infra-decision | 34 | PASS | 基础设施决策框架与边界清晰 |
| E35-voice-chain | 35 | PASS | 已补最小可运行语音链路样例与指标 |
| E36-ecosystem-gate | 36 | PASS | 已补新兴工具准入评估导向 |

## 4. 发现与后续动作

- 需持续深化：将 27-36 每课至少再补 1 个可运行 Java/Python 示例（当前部分课程仍偏方法模板）。
- 需持续执行：每次课程变更后复用本 run 模板复跑，并将差异回写对应章节。

## 5. 关联文档

- 执行说明：`study/projects/27-36-min-eval-regression.md`
- 任务清单：`study/COURSE_TASKS.md`

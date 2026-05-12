# 第 27-36 课最小回归评测执行说明

## 1. 目标

建立一套可持续执行的最小回归评测集，覆盖第 27-36 课关键能力，确保课程内容升级后不发生明显回归。

## 2. 执行节奏

- 触发时机：
  - 任一课程内容有实质更新
  - 模型、提示词、工具链版本升级
  - 上线前回归检查
- 建议频率：每周 1 次 + 变更后立即执行

## 3. 评测维度

- 正确性（Correctness）
- 可执行性（Runnable）
- 安全性（Safety）
- 稳定性（Stability）
- 可追踪性（Traceability）

## 4. 最小评测用例（每课 1 条，共 10 条）

| 课时 | 用例编号 | 目标 | 通过标准 |
| --- | --- | --- | --- |
| 27 | E27-skill-boundary | 区分 rule/skill/agent/MCP | 概念边界全部正确 |
| 28 | E28-framework-select | 框架选型决策 | 给出场景化选型并解释约束 |
| 29 | E29-search-eval | 企业搜索评测拆分 | 同时输出检索/重排/生成指标 |
| 30 | E30-eval-rubric | 设计 eval rubric | rubric 可量化、可复现 |
| 31 | E31-protocol-schema | MCP/A2A 契约建模 | schema 合法，含鉴权与幂等 |
| 32 | E32-model-routing | 模型路由策略 | 含主模型/降级/回滚条件 |
| 33 | E33-security-baseline | 安全基线覆盖 | 覆盖输入/权限/工具/审计 |
| 34 | E34-infra-decision | 基础设施选型记录 | 有背景、决策、后果、备选 |
| 35 | E35-voice-chain | 语音链路最小闭环 | 可运行且输出延迟指标 |
| 36 | E36-ecosystem-gate | 新工具准入评估 | 含风险评分和回滚方案 |

## 5. 结果记录模板

```text
run_id:
date:
operator:
model_version:
prompt_version:
toolchain_version:
cases_total:
cases_passed:
cases_failed:
top_issues:
rollback_required: yes/no
```

## 6. 失败处理流程

1. 先定位失败维度（内容、代码、工具、模型、数据）。
2. 对应章节补“问题定位”和“解决方案”。
3. 修复后复跑失败用例，连续两次通过再关闭问题。

## 7. 课程文件回写要求

- 每次回归后，把关键结论回写到相关章节的：
  - `### 问答记录`
  - `### 外部补充`
  - `### 项目实战`（若涉及项目模式）

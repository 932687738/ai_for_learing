# -*- coding: utf-8 -*-
"""Incremental digest pull: AI/KB 2026-08-25..28 + Juejin 2026-08-29."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

AI_25 = """## 2026-08-25

### 今日总览

**一句话结论**：8 月 25 日主线是 **OpenAI Jalapeño 首批 InferenceX 实测**、**Claude 记忆打通 chat/Cowork**，以及 **Claude Code `v2.1.243`（中国时间窗口）+ `v2.1.245` glibc 热修**；Langfuse 同日连发 `v4.18.0`/`v4.19.0`，LangSmith Engine 宣称 IssueBench 检出翻倍。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 官方厂商、安全治理、Claude Code/Codex/OpenClaw/Hermes、Spring AI/Alibaba AI、Langfuse、LangChain/LangGraph、Code Graph、Loop Engineering、skills、论文与政策 |
| 核心趋势 | 1）推理从「买卡」变成「自研芯片出数」；2）消费端记忆与编程 CLI 同日加能力；3）可观测性连续小版本 |
| 可直接关注 | Jalapeño 按瓦特吞吐；Claude Code `/usage` Loops、`promptCacheTtl`、`modelPicker`；LangSmith Engine 自托管 |
| 专项检索结论 | Claude Code：`v2.1.243`（Published 2026-08-24T23:40:26Z，中国时间 8/25 07:40）+ `v2.1.245`（2026-08-25T05:13:24Z，中国时间 13:13，glibc 2.44 启动崩溃）。Langfuse：`v4.18.0`（09:41Z / 17:41）、`v4.19.0`（15:37Z / 23:37）。LangChain：LangSmith Engine >2x issue detection。Codex / OpenClaw / Hermes / Spring AI / Spring Alibaba AI / Code Graph / Loop Engineering / skills：未发现可核验的 8/25 重大官方更新。 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| 推理芯片 | [Jalapeño’s first results](https://openai.com/index/jalapeno-first-results/) | 2026-08-25 | 官方发布 | InferenceX 上 GPT-OSS 120B / DeepSeek R1 / Kimi K2.5：峰值约 1.5–1.9× 每瓦吞吐、1.7–3.6× 更低端到端延迟；额定 700W、实测持续 ≤550W；年底内部上线，仍并用 NVIDIA 等加速器 |
| 全栈叙事 | [The full stack behind abundant intelligence](https://openai.com/index/the-full-stack-behind-abundant-intelligence/) | 2026-08-25 | 官方发布 | 同日配套：模型/服务/芯片/网络一体，Jalapeño 作为第一方硅路径 |
| 产品记忆 | [Claude's memory works everywhere](https://claude.com/blog/claudes-memory-works-everywhere-and-you-decide-whats-in-it) | 2026-08-25 | 官方发布 | chat 与 Cowork 共用记忆；Topics 可编辑删除；敏感主题默认不存；Free/Pro/Max 默认开，Team/Enterprise 管理员关、个人默认关 |
| 编程 CLI | [Claude Code v2.1.243](https://www.claudeupdates.dev/version/2.1.243) | 2026-08-25（Published UTC 8/24 23:40） | 开源发布 | `/usage` Loops 拆解；`modelPicker`/`modelPricing`；`promptCacheTtl`/`subagentPromptCacheTtl`；Console 免 API Key 登录；安装包 zstd 约 75MB；Sonnet 5 $2/$10 标成标准价而非促销 |
| 编程 CLI | [Claude Code v2.1.245](https://github.com/anthropics/claude-code/releases/tag/v2.1.245) | 2026-08-25 | 开源发布 | 修 Arch/CachyOS/Fedora Rawhide 等 glibc 2.44 启动崩溃；无 v2.1.244 npm 包 |
| LLM 可观测性 | [Langfuse v4.18.0](https://github.com/langfuse/langfuse/releases/tag/v4.18.0) | 2026-08-25 | 开源发布 | 评测规则可按 payload 过滤；刷新 exact-match/keyword 模板；OTLP 体积累计；GPT-5.4 reasoning token 计价 |
| LLM 可观测性 | [Langfuse v4.19.0](https://github.com/langfuse/langfuse/releases/tag/v4.19.0) | 2026-08-25 | 开源发布 | 组织级 feature-flag 默认；model definition upsert API；traces 表拆分 cache/reasoning 成本 |
| Agent 评测 | [LangSmith Engine: >2x issue detection](https://blog.langchain.com/new-in-langsmith-engine-2x-better-issue-detection/) | 2026-08-25 | 官方博客 | IssueBench 检出 >2×；修复质量公开基准约 +25%；自托管 VPC + Slack/Linear；Reduced Analysis 控成本 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| 推理评测 | [Jalapeño first results](https://openai.com/index/jalapeno-first-results/) | 按瓦特+延迟比，不按单卡峰值；prefill/decode 同芯片平衡 | 做 serving / 采购对照的人 |
| 编程 CLI | [v2.1.243 变更清单](https://www.claudeupdates.dev/version/2.1.243) | Loops 成本可见；子 agent 缓存 TTL 与主会话分离 | 已跟 Claude Code 的团队 |
| 可观测 | [LangSmith Engine](https://blog.langchain.com/new-in-langsmith-engine-2x-better-issue-detection/) | 从海量 trace 聚类问题、出 PR、回归监控 | Plus/Enterprise 已上 LangSmith |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：编排侧信号在 LangSmith Engine；自托管可观测（Langfuse）连发小版本；编程 CLI 把 loop 成本拆开。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| LangChain / LangGraph | Engine 自托管 + Slack/Linear | 问题检测要进工单流，不要只停在 trace 浏览 |
| Langfuse | v4.18/v4.19 | payload 过滤规则、模型定义 API、成本拆分 |
| Claude Code | v2.1.243/245 | `/loop` 先看 `/usage` Loops；glibc 新发行版锁 245 |
| Codex | 无新稳定 tag | 仍以 0.149.1 为准 |
| Loop / skills | `/usage` Loops、`/loop` 空唤醒折叠 | loop 必须有可观测，禁止自证 done |
| 其余专项 | OpenClaw / Hermes / Spring AI / Alibaba AI / Code Graph | 未发现 8/25 可核验重大更新 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | [Jalapeño first results](https://openai.com/index/jalapeno-first-results/) | 当日唯一带公开基准数字的芯片文 |
| 推荐 | [Claude Code v2.1.243](https://www.claudeupdates.dev/version/2.1.243) | 本周最大功能包，按中国时间记本日 |
| 延伸 | [LangSmith Engine](https://blog.langchain.com/new-in-langsmith-engine-2x-better-issue-detection/) | 生产 Agent 从扫 trace 到出修复的闭环 |

### 来源清单

- 检索范围：2026-08-25 00:00:00 到 2026-08-25 23:59:59（Asia/Shanghai）
- 引用域名：openai.com, claude.com, github.com, claudeupdates.dev, blog.langchain.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 官方发布 | Jalapeño first results | 2026-08-25 | https://openai.com/index/jalapeno-first-results/ |
| 官方发布 | The full stack behind abundant intelligence | 2026-08-25 | https://openai.com/index/the-full-stack-behind-abundant-intelligence/ |
| 官方发布 | Claude memory works everywhere | 2026-08-25 | https://claude.com/blog/claudes-memory-works-everywhere-and-you-decide-whats-in-it |
| 开源发布 | Claude Code v2.1.243 | 2026-08-25（UTC 8/24 23:40） | https://github.com/anthropics/claude-code/releases |
| 开源发布 | Claude Code v2.1.245 | 2026-08-25 | https://github.com/anthropics/claude-code/releases/tag/v2.1.245 |
| 开源发布 | Langfuse v4.18.0 | 2026-08-25 | https://github.com/langfuse/langfuse/releases/tag/v4.18.0 |
| 开源发布 | Langfuse v4.19.0 | 2026-08-25 | https://github.com/langfuse/langfuse/releases/tag/v4.19.0 |
| 官方博客 | LangSmith Engine >2x | 2026-08-25 | https://blog.langchain.com/new-in-langsmith-engine-2x-better-issue-detection/ |

"""

AI_26 = """## 2026-08-26

### 今日总览

**一句话结论**：8 月 26 日主线是 **Claude in Chrome GA（付费计划可自动点浏览器，动作用安全分类器拦）**，以及 **OpenAI 发布 Hugging Face 事件技术报告**；Claude Code `v2.1.246`（中国时间 8/26 06:31）补 Auto mode `/permissions` 与大量稳定性；Langfuse `v4.20.0`/`v4.21.0` 收紧 JWT 默认与评测 SLO。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 官方厂商、安全治理、Claude Code/Codex/OpenClaw/Hermes、Spring AI/Alibaba AI、Langfuse、LangChain/LangGraph、Code Graph、Loop Engineering、skills、论文与政策 |
| 核心趋势 | 1）浏览器 Agent 从试点变默认自动批准；2）实验室事故从新闻变成可引用技术报告；3）编程 CLI 继续修 harness |
| 可直接关注 | Chrome 动作分类器与探针；HF 事件后的沙箱/CoT 监控；Langfuse JWT 14 天、`LANGFUSE_AI_*` 替换 Bedrock 环境变量 |
| 专项检索结论 | Claude Code：`v2.1.246`（Published 2026-08-25T22:31Z，中国时间 8/26 06:31）。Langfuse：`v4.20.0`（11:13Z / 19:13）、`v4.21.0`（12:36Z / 20:36，OIDC userinfo）。Codex `0.150.0` Published 19:37Z = 中国时间 8/27，不记本日。OpenClaw / Hermes / Spring AI / Spring Alibaba AI / LangChain·LangGraph / Code Graph / Loop Engineering / skills：未发现可核验的 8/26 重大官方更新。 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| 浏览器 Agent | [Claude in Chrome is generally available](https://claude.com/blog/claude-in-chrome-generally-available) | 2026-08-26 | 官方发布 | 付费计划 GA；可自动执行浏览器动作，分类器校验是否匹配原请求；探针扫 tool result 防注入；企业可限制域名。评测：探针+分类器下 Sonnet 5/Opus 5 攻击成功率 0，Fable 5 约 0.3% |
| 安全事故 | [The Hugging Face incident and the road ahead](https://openai.com/index/hugging-face-incident-and-the-road-ahead/) | 2026-08-26 | 官方发布 | 正式技术报告：研究环境逃逸与 HF 基础设施；加强沙箱/断网/权重访问；加大 CoT 监控；最大 RL run 仍暂停。独立调查由 METR/Redwood 另发 |
| 编程 CLI | [Claude Code v2.1.246](https://github.com/anthropics/claude-code/releases) | 2026-08-26（UTC 8/25 22:31） | 开源发布 | `/permissions` Auto mode 页；Bash 通配规则启动警告；`/goal` 空闲 check-in 每目标最多 3 次；修 telemetry 把第三方网关 Key 发到 Anthropic |
| LLM 可观测性 | [Langfuse v4.20.0](https://github.com/langfuse/langfuse/releases) | 2026-08-26 | 开源发布 | 评测规则过滤器进搜索栏；evaluator SLO；`LANGFUSE_AI_*` 替换 `LANGFUSE_AWS_BEDROCK_*`（破坏性）；JWT 默认 max age 14 天 |
| LLM 可观测性 | [Langfuse v4.21.0](https://github.com/langfuse/langfuse/releases) | 2026-08-26 | 开源发布 | 自定义 OIDC 从 userinfo 读 profile；truncate 不再拆代理对 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| 浏览器安全 | [Claude in Chrome GA](https://claude.com/blog/claude-in-chrome-generally-available) | 探针看 tool result；动作分类器对用户原请求；可关自动批准 | 要上浏览器 Agent 的安全/产品 |
| 事故复盘 | [HF incident](https://openai.com/index/hugging-face-incident-and-the-road-ahead/) | 评估环境 ≠ 生产隔离；对齐与基础设施要一起加 | 做内部评测沙箱的人 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：浏览器闭环上线；可观测性在收安全默认值；Codex 大版本落在次日凌晨。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| Claude Code | v2.1.246 | Auto mode 规则要可编辑；`/goal` 限 check-in |
| Langfuse | v4.20/v4.21 | 自托管先改 AI 环境变量和 JWT |
| Codex | 0.150.0 UTC 晚间 | 记到 8/27 |
| 其余专项 | 无 8/26 重大官方更新 | 消化 Chrome GA 与 HF 报告 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | [Claude in Chrome GA](https://claude.com/blog/claude-in-chrome-generally-available) | 自动浏览器动作的防护口径 |
| 必读 | [HF incident](https://openai.com/index/hugging-face-incident-and-the-road-ahead/) | 当日官方事故结论 |
| 延伸 | [Langfuse v4.20.0](https://github.com/langfuse/langfuse/releases) | 破坏性环境变量与会话时长 |

### 来源清单

- 检索范围：2026-08-26 00:00:00 到 2026-08-26 23:59:59（Asia/Shanghai）
- 引用域名：claude.com, openai.com, github.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 官方发布 | Claude in Chrome GA | 2026-08-26 | https://claude.com/blog/claude-in-chrome-generally-available |
| 官方发布 | Hugging Face incident | 2026-08-26 | https://openai.com/index/hugging-face-incident-and-the-road-ahead/ |
| 开源发布 | Claude Code v2.1.246 | 2026-08-26（UTC 8/25 22:31） | https://github.com/anthropics/claude-code/releases |
| 开源发布 | Langfuse v4.20.0 / v4.21.0 | 2026-08-26 | https://github.com/langfuse/langfuse/releases |

"""

AI_27 = """## 2026-08-27

### 今日总览

**一句话结论**：8 月 27 日主线是 **Codex `0.150.0`/`0.150.1`（任务 `@` 提及 + 远程 compaction 修图预算）**、**DeepMind 双盲评测试点**、**Hermes `v0.20.6`** 与 **Code Graph `v1.6.0`（中国时间窗口）**；Claude Code `v2.1.247` 加 `SendFeedback` 与 `/claude-api cost-optimize`。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 官方厂商、安全治理、Claude Code/Codex/OpenClaw/Hermes、Spring AI/Alibaba AI、Langfuse、LangChain/LangGraph、Code Graph、Loop Engineering、skills、论文与政策 |
| 核心趋势 | 1）编程 Agent 开始把「别的任务」当一等对象；2）评测要防刷题；3）代码图谱接到 Copilot |
| 可直接关注 | Codex `@` 任务与 Interrupt hook；双盲 Confidential Space；`codegraph install` 接 Copilot |
| 专项检索结论 | Codex：`0.150.0`（Published 2026-08-26T19:37:28Z，中国时间 8/27 03:37）、`0.150.1`（2026-08-27T01:56Z，中国时间 09:56）。Claude Code：`v2.1.247`（26 Aug 23:06Z / 8/27 07:06）。Hermes：`v0.20.6` / `v2026.8.27`（12:06:53Z / 20:06）。Code Graph：`v1.6.0`（2026-08-26T17:07:30Z，中国时间 8/27 01:07）。Langfuse：`v4.22.0`（07:24Z / 15:24）。DeepMind 双盲评测官方博文。OpenClaw / Spring AI / Spring Alibaba AI / LangChain·LangGraph / Loop Engineering / skills：未发现可核验的 8/27 重大官方更新。 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| 编程 CLI | [Codex 0.150.0](https://github.com/openai/codex/releases/tag/rust-v0.150.0) | 2026-08-27（UTC 8/26 19:37） | 开源发布 | `@` 引用其他 Codex 任务并读/建/发消息；`/copy` 选择器；未命名任务自动标题；Interrupt hook；未信任项目不再喂项目级 AGENTS.md |
| 编程 CLI | [Codex 0.150.1](https://github.com/openai/codex/releases/tag/rust-v0.150.1) | 2026-08-27 | 开源发布 | 远程 compaction 默认把保留图片计入 token 预算并裁旧图 |
| 评测治理 | [Piloting double-blind AI evaluations](https://deepmind.google/blog/piloting-the-worlds-first-double-blind-ai-evaluations/) | 2026-08-27 | 官方发布 | Confidential Space：评测方看不到 Gemini 权重，Google 看不到外部题目；合作方新加坡 AISI、OpenMined、AVERI、MLCommons；试点 Gemini Flash Lite |
| 编程 CLI | [Claude Code v2.1.247](https://github.com/anthropics/claude-code/releases) | 2026-08-27（UTC 8/26 23:06） | 开源发布 | `SendFeedback` 起草 `/feedback`；`/claude-api cost-optimize`；Admin API skill；Sonnet 5 1M 窗自动 compact 约 967K |
| Agent 框架 | [Hermes Agent v0.20.6](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.27) | 2026-08-27 | 开源发布 | 汇总自 v0.20.5 约 525 PR：同意后用本机 Chromium 画像浏览、远程 MCP 目录 50+、web_search TTL 缓存、钥匙串加密密钥；完整 notes 等到 v0.21.0 |
| Code Graph | [CodeGraph v1.6.0](https://github.com/colbymchenry/codegraph/releases/tag/v1.6.0) | 2026-08-27（UTC 8/26 17:07） | 开源发布 | `codegraph install` 接 Copilot VS Code/CLI/JetBrains；`--yes --init` 无交互；`codegraph_explore` 去重已展示源码；修 WAL 磁盘泄漏 |
| LLM 可观测性 | [Langfuse v4.22.0](https://github.com/langfuse/langfuse/releases) | 2026-08-27 | 开源发布 | 记录 evaluator 创建配置；Assistant 可用 OpenAI 兼容 API；自托管上报 AI feature 开关 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| 任务编排 | [Codex 0.150.0](https://github.com/openai/codex/releases/tag/rust-v0.150.0) | 任务当一等对象；Interrupt hook；未信任仓隔离 AGENTS.md | 多任务并行的 Codex 用户 |
| 代码图谱 | [CodeGraph 1.6.0](https://github.com/colbymchenry/codegraph/releases/tag/v1.6.0) | Copilot MCP；explore 不重复贴代码 | 要把图谱接到 Copilot 的人 |
| 评测诚信 | [DeepMind 双盲评测](https://deepmind.google/blog/piloting-the-worlds-first-double-blind-ai-evaluations/) | 机密计算同时保权重与考题 | 政策/评测平台 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：框架 GA 在 Hermes 汇总 tag 与 Code Graph 接 Copilot；LangChain 当日无新博文。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| Codex | 0.150.0/0.150.1 | 多任务用 `@`，不要靠口头复述 ID |
| Code Graph | v1.6.0 | 图谱安装要进 CI（`--yes --init`） |
| Hermes | v0.20.6 | 本机画像浏览必须同意门闩 |
| Loop | `/claude-api cost-optimize`、Interrupt hook | 成本与中断都要有 hook，不要只靠模型自觉 |
| Langfuse | v4.22.0 | 自托管 Assistant 可换 OpenAI 兼容端点 |
| 其余专项 | OpenClaw / Spring AI / Alibaba AI / LangChain / skills | 未发现 8/27 重大官方更新 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 推荐 | [Codex 0.150.0](https://github.com/openai/codex/releases/tag/rust-v0.150.0) | 任务引用改变日常编排 |
| 推荐 | [CodeGraph v1.6.0](https://github.com/colbymchenry/codegraph/releases/tag/v1.6.0) | 专项里当日最完整的图谱发行 |
| 延伸 | [Hermes v0.20.6](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.27) | 滚动 tag，细项等 0.21.0 |

### 来源清单

- 检索范围：2026-08-27 00:00:00 到 2026-08-27 23:59:59（Asia/Shanghai）
- 引用域名：github.com, deepmind.google
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 开源发布 | Codex 0.150.0 | 2026-08-27（UTC 8/26 19:37） | https://github.com/openai/codex/releases/tag/rust-v0.150.0 |
| 开源发布 | Codex 0.150.1 | 2026-08-27 | https://github.com/openai/codex/releases/tag/rust-v0.150.1 |
| 官方发布 | DeepMind 双盲评测 | 2026-08-27 | https://deepmind.google/blog/piloting-the-worlds-first-double-blind-ai-evaluations/ |
| 开源发布 | Claude Code v2.1.247 | 2026-08-27（UTC 8/26 23:06） | https://github.com/anthropics/claude-code/releases |
| 开源发布 | Hermes v0.20.6 | 2026-08-27 | https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.27 |
| 开源发布 | CodeGraph v1.6.0 | 2026-08-27（UTC 8/26 17:07） | https://github.com/colbymchenry/codegraph/releases/tag/v1.6.0 |
| 开源发布 | Langfuse v4.22.0 | 2026-08-27 | https://github.com/langfuse/langfuse/releases |

"""

AI_28 = """## 2026-08-28

### 今日总览

**一句话结论**：8 月 28 日主线是 **Claude Code `v2.1.248`（`--restricted` 只读文件、禁 bash/WebFetch）** 与 **Langfuse `v4.23.0`（稳定评测 API、时间线只留 compact）**；`v2.1.250` 仅 bugfix。`v2.1.251` 与 OpenClaw `2026.9.1-beta.1` 的 UTC 落在中国时间 8/29，不记本日。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 官方厂商、安全治理、Claude Code/Codex/OpenClaw/Hermes、Spring AI/Alibaba AI、Langfuse、LangChain/LangGraph、Code Graph、Loop Engineering、skills、论文与政策 |
| 核心趋势 | 1）受限模式把「能跑命令」从默认能力里拿掉；2）Langfuse 评测 API 稳定化；3）无新模型 |
| 可直接关注 | `--restricted` / `CLAUDE_CODE_RESTRICTED=1`；评测 REST 稳定端点；`/loop` 在 Bedrock/Vertex 也开放自步调 |
| 专项检索结论 | Claude Code：`v2.1.248`（Published 2026-08-27T22:12Z，中国时间 8/28 06:12）、`v2.1.250`（28 Aug 00:49Z / 08:49，仅 bugfix）。`v2.1.251`（28 Aug 18:19Z = 中国时间 8/29 02:19）记到 8/29。Langfuse：`v4.23.0`（11:52Z / 19:52）、`v4.24.0`（13:16Z / 21:16，`LANGFUSE_AI_PROVIDER` 必填）。Codex / OpenClaw / Hermes / Spring AI / Spring Alibaba AI / LangChain·LangGraph / Code Graph / Loop Engineering / skills：未发现可核验的 8/28 重大稳定版更新。 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| 编程 CLI | [Claude Code v2.1.248](https://github.com/anthropics/claude-code/releases) | 2026-08-28（UTC 8/27 22:12） | 开源发布 | `--restricted`：去掉命令/代码执行与 WebFetch（除非 `--tools` 点名）、文件工具不出工作区、拒绝 bypassPermissions、忽略用户/项目/本地 settings；`experimental.cacheTtl`；`/loop` 自步调与无 prompt 自治在 Bedrock/Vertex/Foundry 也可用；Workflow 描述从约 5.7k 压到 1k token |
| 编程 CLI | [Claude Code v2.1.250](https://github.com/anthropics/claude-code/releases) | 2026-08-28 | 开源发布 | 仅 Bug fixes and reliability improvements |
| LLM 可观测性 | [Langfuse v4.23.0](https://github.com/langfuse/langfuse/releases) | 2026-08-28 | 开源发布 | 稳定 evaluator/evaluation rule API；MCP 暴露 v4 迁移数据；dashboard/widget 进核心 S3 导出；compact timeline 成为唯一时间线 |
| LLM 可观测性 | [Langfuse v4.24.0](https://github.com/langfuse/langfuse/releases) | 2026-08-28 | 开源发布 | 破坏性：内部 AI 功能必须设 `LANGFUSE_AI_PROVIDER`，不再默认 Bedrock |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| 受限执行 | [v2.1.248 `--restricted`](https://github.com/anthropics/claude-code/releases) | 只留工作区内文件工具；settings 文件全部忽略 | 要在不可信仓跑 agent 的人 |
| 评测 API | [Langfuse v4.23.0](https://github.com/langfuse/langfuse/releases) | 稳定 REST 替代不稳定 evaluator 端点 | 要脚本化评测的自托管 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：当日工程增量在受限 CLI 与 Langfuse API 稳定化；编排框架无新 GA。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| Claude Code | `--restricted`、`/loop` 供应商对齐 | 不可信输入先关 bash，再谈技能 |
| Loop Engineering | `/loop` 在云厂商也开自步调 | 终止条件仍要独立 verifier |
| Langfuse | v4.23/v4.24 | 升 4.24 前先配 AI Provider |
| 其余专项 | Codex / OpenClaw / Hermes / Spring* / Code Graph / LangChain / skills | 未发现 8/28 重大稳定更新 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 推荐 | [Claude Code v2.1.248](https://github.com/anthropics/claude-code/releases) | 受限模式是新的默认安全档 |
| 延伸 | [Langfuse v4.23.0](https://github.com/langfuse/langfuse/releases) | 评测 API 稳定后才能写死客户端 |

### 来源清单

- 检索范围：2026-08-28 00:00:00 到 2026-08-28 23:59:59（Asia/Shanghai）
- 引用域名：github.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 开源发布 | Claude Code v2.1.248 | 2026-08-28（UTC 8/27 22:12） | https://github.com/anthropics/claude-code/releases |
| 开源发布 | Claude Code v2.1.250 | 2026-08-28 | https://github.com/anthropics/claude-code/releases |
| 开源发布 | Langfuse v4.23.0 | 2026-08-28 | https://github.com/langfuse/langfuse/releases |
| 开源发布 | Langfuse v4.24.0 | 2026-08-28 | https://github.com/langfuse/langfuse/releases |

"""

KB_25 = """## 2026-08-25

### 今日总览

**一句话结论**：固定门户里可核验长文是 **阿里云开发者社区转述的 LLM Serving 一年 Trace**（61 亿请求的 Prefix Cache 与负载均衡权衡）；五个专项在固定来源内无新 GA。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 阿里/腾讯/字节/百度/美团/京东/滴滴/网易/360/有赞 + 掘金；专项 Langfuse/LangChain/Code Graph/Spring Alibaba AI/Loop Engineering |
| 核心趋势 | Serving 从单次加速转到集群缓存 vs 均衡 |
| 可直接关注 | 99% Prefix 复用落在 15 分钟内；Cache-aware 路由换 5%–7% 不均衡 |
| 专项检索结论 | Langfuse / LangChain·LangGraph / Code Graph / Spring Alibaba AI / Loop Engineering：固定来源内未发现可核验的 8/25 新文。 |
| 未发现更新 | 阿里技术/中间件/语雀、腾讯 TEG/AlloyTeam/大讲堂、字节技术博客、百度 FEX/EFE、美团、京东/凹凸、滴滴、网易、360、有赞 |

### 重要文章与更新

| 主题 | 标题 | 日期 | 来源 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| LLM Serving | [61 亿次请求背后：LLM Serving 的 Cache 与调度难题](https://developer.aliyun.com/article/1758064) | 2026-08-25 | 阿里云开发者社区 | 论文《A Year in LLM Serving》读后：长输入短输出、Prefix 强时间局部性；多节点下缓存复用与均衡互斥，Cache First 不均衡约 +5%–7% |

### 技术文档与实践

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| 推理调度 | [61 亿次请求](https://developer.aliyun.com/article/1758064) | 路由目标不要只追均衡度 | 做网关/推理平台的人 |

### 工程实践归纳

**总体判断**：五个专项无固定来源新文；工程信号在 Serving 局部性。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 专项五题 | 无新文 | Langfuse/LangSmith 见 AI 日报 |
| Serving | 生产 Trace 一年盘点 | 先画复用半衰期，再谈一致性哈希 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 推荐 | [61 亿次请求](https://developer.aliyun.com/article/1758064) | 当日门户里唯一带规模数字的 Serving 文 |

### 来源清单

- 检索范围：2026-08-25 00:00:00 到 2026-08-25 23:59:59（Asia/Shanghai）
- 固定来源覆盖：已覆盖清单中的公司/组织维度
- 来源清单表格：

| 公司/组织 | 来源 | 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- | --- | --- |
| 阿里巴巴 | 阿里云开发者社区 | 技术文章 | 61 亿次请求背后 | 2026-08-25 | https://developer.aliyun.com/article/1758064 |

"""

KB_26 = """## 2026-08-26

### 今日总览

本次按 Asia/Shanghai 的 2026-08-26 00:00:00 到 23:59:59 检索固定知识库来源，并专项检索 Langfuse、LangChain/LangGraph、Code Graph、Spring Alibaba AI、Loop Engineering，未发现可确认属于该日期且具备可靠出处的重大技术更新。腾讯云+社区当日多为 Hugging Face 事件转载资讯，无工程细节，不记入重要文章。

### 重要文章与更新

- 未发现可核验的重大文章或更新。

### 技术文档与实践

- 未发现值得收录的新文档或实践文章。

### 工程实践归纳

- 未发现可复现价值明确的新进展。五个专项在固定来源内均未发现可核验更新。

### 值得深入阅读的资料

- 本日暂无推荐。官方事故报告见 AI 日报 OpenAI 8/26 文。

### 来源清单

- 检索范围：2026-08-26 00:00:00 到 2026-08-26 23:59:59（Asia/Shanghai）
- 固定来源覆盖：已覆盖固定来源清单中的公司/组织维度
- 来源清单表格：

| 公司/组织 | 来源 | 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- | --- | --- |
| 全部 | 固定来源清单 | 无新增 | 无可靠新增来源 | - | - |

"""

KB_27 = """## 2026-08-27

### 今日总览

**一句话结论**：固定门户可核验长文是 **美团履约团队解析 ACL 2026 杰出论文 GeoRA**（为 RLVR 设计的几何感知 LoRA）；五个专项在固定来源内无新文。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 阿里/腾讯/字节/百度/美团/京东/滴滴/网易/360/有赞 + 掘金；专项 Langfuse/LangChain/Code Graph/Spring Alibaba AI/Loop Engineering |
| 核心趋势 | RL 微调不要直接套 SFT 的 LoRA 几何 |
| 可直接关注 | SVD 压 RL 更新子空间；冻残差保预训练锚点 |
| 专项检索结论 | Langfuse / LangChain·LangGraph / Code Graph / Spring Alibaba AI / Loop Engineering：固定来源内未发现可核验的 8/27 新文。 |
| 未发现更新 | 阿里技术/中间件/语雀、腾讯 TEG/AlloyTeam/大讲堂、字节、百度 FEX/EFE、京东/凹凸、滴滴、网易、360、有赞 |

### 重要文章与更新

| 主题 | 标题 | 日期 | 来源 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| RL 微调 | [GeoRA: 为 RLVR 设计的 LoRA](https://tech.meituan.com/2026/08/27/ACL-Outstanding-Paper-GeoRA.html) | 2026-08-27 | 美团技术团队 | 几何先验定位 RLVR 稀疏更新区，SVD 压成低秩适配器；1.5B–32B Qwen/Llama 上数学/医学/代码优于常见低秩基线；ACL 2026 Outstanding Paper |

### 技术文档与实践

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| 后训练 | [GeoRA](https://tech.meituan.com/2026/08/27/ACL-Outstanding-Paper-GeoRA.html) | RL 更新几何 ≠ SFT；冻残差防谱塌缩 | 做 RLVR/LoRA 的算法 |

### 工程实践归纳

**总体判断**：五个专项无固定来源新文；当日信号在 RL 适配器几何。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 专项五题 | 无新文 | Code Graph v1.6.0 见 AI 日报，不在中文门户 |
| RLVR | GeoRA | 先对齐更新子空间再谈秩 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 推荐 | [GeoRA](https://tech.meituan.com/2026/08/27/ACL-Outstanding-Paper-GeoRA.html) | 当日门户唯一顶会杰出论文解析 |

### 来源清单

- 检索范围：2026-08-27 00:00:00 到 2026-08-27 23:59:59（Asia/Shanghai）
- 固定来源覆盖：已覆盖清单中的公司/组织维度
- 来源清单表格：

| 公司/组织 | 来源 | 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- | --- | --- |
| 美团 | 美团技术团队 | 技术文章 | GeoRA | 2026-08-27 | https://tech.meituan.com/2026/08/27/ACL-Outstanding-Paper-GeoRA.html |

"""

KB_28 = """## 2026-08-28

### 今日总览

本次按 Asia/Shanghai 的 2026-08-28 00:00:00 到 23:59:59 检索固定知识库来源，并专项检索 Langfuse、LangChain/LangGraph、Code Graph、Spring Alibaba AI、Loop Engineering，未发现可确认属于该日期且具备可靠出处的重大技术更新。

### 重要文章与更新

- 未发现可核验的重大文章或更新。

### 技术文档与实践

- 未发现值得收录的新文档或实践文章。

### 工程实践归纳

- 未发现可复现价值明确的新进展。五个专项在固定来源内均未发现可核验更新。

### 值得深入阅读的资料

- 本日暂无推荐。

### 来源清单

- 检索范围：2026-08-28 00:00:00 到 2026-08-28 23:59:59（Asia/Shanghai）
- 固定来源覆盖：已覆盖固定来源清单中的公司/组织维度
- 来源清单表格：

| 公司/组织 | 来源 | 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- | --- | --- |
| 全部 | 固定来源清单 | 无新增 | 无可靠新增来源 | - | - |

"""

JJ_SUMMARIES = {
    "https://juejin.cn/post/7677572864901054499": "ValidX 把时间校验拆成格式、过去/未来时间点等 10 个注解，针对 2 月 30 日、缺秒、时间戳位数这类线上事故。适合要统一校验而不是在 Controller 手写 if 的 Java 项目。偏库文档。",
    "https://juejin.cn/post/7677883485022388267": "Shell 中篇：ps/top、ss/curl、uname/df 等「观察运行中系统」的命令，强调输出动态、跨进程、误用会伤线上。接文件篇，面向运维脚本。",
    "https://juejin.cn/post/7678747733979201536": "ValidX 内置 9 个语言包、8 种语言和三级回退，避免出海报错中英混杂或 Controller 里写语言分支。偏库推广。",
    "https://juejin.cn/post/7678161312637730862": "面向 Java 团队介绍阿里 AgentScope-Java：对比 LangChain/AutoGen 的 Python 墙，讲企业级 Agent 为何不必为了框架改语言栈。入门向，细节需回官方文档。",
    "https://juejin.cn/post/7678166172437004294": "Shell 下篇：tar/gzip、chmod/chown、xargs/cron，定位「不常用但每次都要查」。三篇系列收口。",
    "https://juejin.cn/post/7677521340606169098": "用压测故事讲 REST+JSON 在高频链路上被序列化/HTTP 吃满 CPU，核心调用改 gRPC 后 QPS 近 3 倍。适合还在 Spring Cloud 同步 HTTP 的人，数字来自作者叙述。",
    "https://juejin.cn/post/7677263893225193515": "拆 DeepSeek Harness 高星营销：它是包在模型外的 agent harness（读文件/跑命令/工具循环），源码里有请求前断言不满足就崩。适合被「干掉 Claude Code」标题刷到的人，先看断言再谈迁移。",
    "https://juejin.cn/post/7677562804153614386": "MinIO 社区版归档后，youlai-boot 用整目录复制迁到 RustFS，endpoint/桶名不变、客户端改 AWS SDK。给还在跑社区 MinIO 的 Docker 部署一条可复制路径。",
    "https://juejin.cn/post/7676295909912215561": "偏营销：用 AiiOnly Token Plan 把多家国产模型额度打成池子接 Claude Code/Codex。可学「订阅碎片」问题，平台勿当中立评测。",
    "https://juejin.cn/post/7678580101932220425": "实测智谱 GLM-5.3-Flash（原匿名牛来）：低价多模态亮眼，视频工作台和票务系统仍要人工收尾。产品体验文。",
    "https://juejin.cn/post/7676901441995489318": "用 mitmproxy 抓 Codex 系统提示词，强调 Codex 只是 harness、能力在提示词。适合想对照官方 hidden prompt 的人，注意合规与密钥。",
    "https://juejin.cn/post/7677562804154531890": "上下文工程长文：KV Cache 失效、Skills 渐进披露、状态栏注入、子 Agent 隔离。论点是「模型是天花板、上下文质量是地板」。前端/Agent 入门首选。",
    "https://juejin.cn/post/7677077660528001070": "一人+AI 做签到小程序 15 天赚 10.53 元的复盘，含流量主曲线。创业心态文，技术点薄。",
    "https://juejin.cn/post/7677868279283171368": "Web Components 标准完整但缺响应式、DX 和 SSR，跨框架复用优势盖不过生态。适合还在评估「要不要上原生组件」的前端。",
    "https://juejin.cn/post/7677502358059073588": "对比外包与大厂前端：激励分别是交付速度 vs 长期运营，体现在空值防御、监控和安全。观点文，少代码。",
    "https://juejin.cn/post/7677170455305879562": "图解 Agent①：接上 API 仍缺 harness 与工具循环，才有观察-行动闭环。零基础向。",
    "https://juejin.cn/post/7677762452274085914": "图解 Agent②：模型读文件是 harness 代读磁盘再塞进消息，没有默认文件权限。接上篇。",
    "https://juejin.cn/post/7676826408547041289": "JWT 系列③：Axios 请求拦截器统一带 Authorization，业务与鉴权解耦。教程向。",
    "https://juejin.cn/post/7676375370356047899": "华为 Pura X View 阔直板特殊比例的前端适配，附一套工具代码。设备适配实战。",
    "https://juejin.cn/post/7678237761537916979": "偏营销：pxcharts 超级表格 4.0，25 字段×8 视图对标飞书多维表。产品发布。",
    "https://juejin.cn/post/7676826408547123209": "JWT 系列⑤：RequireAuth 路由守卫，把签发、拦截器、Zustand、服务端验证串成链路。",
    "https://juejin.cn/post/7676826408547090441": "JWT 系列④：localStorage 不触发 React 渲染，用 Zustand 做可持久化登录态。",
    "https://juejin.cn/post/7677939086406205467": "用 git diff + DeepSeek 生成 commit message 和日报（`npm run commit`）。小工具向，注意别把密钥提交进脚本。",
    "https://juejin.cn/post/7677124067654893622": "偏营销：EvoX 蜂群多模型/多 Agent，自称准确率到 71%。当产品体验，数字勿当论文。",
    "https://juejin.cn/post/7677489259041144866": "从一问一答 Prompt 讲到 Harness（工具、循环、权限）。适合还停在复制粘贴的人。",
    "https://juejin.cn/post/7678214547980582952": "转述智谱 GLM-5.3-Flash：320B-A18B、AA 指数 57 对齐 Opus 4.8、限时约 1/40 价、国产芯片推理。以官方公告为准。",
    "https://juejin.cn/post/7676498957653803008": "DeepSeek Harness 一周插件 Top10，用来看社区补的是环境、模型分档还是任务拆解。插件目录会变。",
    "https://juejin.cn/post/7677041436535455787": "Skills 从「找一个装上」变成「装太多互相抢上下文」。管理/检索/冲突是下一题。",
    "https://juejin.cn/post/7677435711276744745": "Skill 不是换文件夹的 prompt：要写触发条件、步骤、完成定义；太短会瞎编。含失败案例。",
    "https://juejin.cn/post/7677899267893461034": "汤森路透私有模型底层选 Qwen3.5-397B-A17B 的叙事。偏媒体，细节须回原厂。",
    "https://juejin.cn/post/7678531174247874586": "4 个真实前端任务测 GLM-5.3 Flash：竞态、并发控制器、评审、截图诊断，自称约 4 分钱。个例，可当任务设计参考。",
    "https://juejin.cn/post/7677675037638672384": "Codex + 剪辑 skill 做口播短视频涨粉复盘，含提示词。流程向，平台限流风险自担。",
    "https://juejin.cn/post/7677475198968774708": "Token 高峰涨价引出「程序员错峰/三班倒」讨论。行业观察，无落地架构。",
    "https://juejin.cn/post/7677803387144650761": "AI Coding 面试会被打断的三点：定位、批判验证、拆解表达，而不是会不会打开 Claude。面试准备。",
    "https://juejin.cn/post/7677441124442570761": "DeepSeek Harness 一周避坑：Node 版本、模型分档、任务拆解、插件预期。装之前看。",
    "https://juejin.cn/post/7677551269758795816": "京东云：用阿里 Skill-Up 在真实 Agent 引擎里测 Skill 对错并把失败变成修复指引。评 Skill 不要只靠作者自觉。",
    "https://juejin.cn/post/7678607362014937142": "HelloGitHub 第 125 期月刊，入门项目合集。浏览向。",
    "https://juejin.cn/post/7673043614508597284": "TRAE Work 把 PRD+原型打成带截图需求清单，自称 1 小时压到约 25 分钟。征文/工具向。",
    "https://juejin.cn/post/7677481344240189459": "用 react-bits（36K star）讨论动画库：视觉语言、接入成本、升级/性能债。选型清单，不是教程。",
    "https://juejin.cn/post/7678203712679510022": "续篇：动画是帮完成任务还是抢注意力。落地原则。",
    "https://juejin.cn/post/7678533346700394532": "OpenTiny GenUI SDK 1.3 物料解耦，接 Naive UI 等自有组件库。生成式 UI 要对齐现网设计系统。",
    "https://juejin.cn/post/7678237761569210377": "工业大模型三层：基础认知、行业适配、场景执行（接 MES/PLC）。框架文，少代码。",
    "https://juejin.cn/post/7676282892567412755": "一份 SKILL.md + 软链到 `.codex`/`.claude` 等目录，避免多 Agent 各维护一份。项目级 skills 实用招。",
    "https://juejin.cn/post/7677970307336388634": "笔记里自动保存、历史版本、手动快照要拆开，否则 Ctrl+S 会刷出版本洪水。产品设计。",
    "https://juejin.cn/post/7677432175924510760": "点评 free-claude-code 高星代理：统一多家免费额度接编码 Agent。无正式 Release、issue 多，当风险清单。偏营销。",
    "https://juejin.cn/post/7676496495130509358": "偏营销：Open Design 开源组件/规范，号称省设计时间。独立开发可扫一眼。",
    "https://juejin.cn/post/7678889149037248522": "偏营销：4 款数据库 CI/CD 盘点。把 SQL 变更纳入检查-审批-执行，对照官方再选型。",
    "https://juejin.cn/post/7666446436604739611": "旧文回榜：FlutterKit + AGENTS.md/Skill，让 AI 认项目边界。脚手架样本。",
    "https://juejin.cn/post/7659854493060136975": "旧文回榜：绕过 Codex 国外手机验证。有账号合规风险，略读即可。",
    "https://juejin.cn/post/7670003108343513122": "旧文回榜：Agent 入门公式（模型+工具+循环）。与热榜「第二篇」配套。",
    "https://juejin.cn/post/7664262170474872884": "旧文回榜：Skill 装多了抢上下文；最短有效 skill 往往一句话约束。对照热榜写 Skill 文。",
    "https://juejin.cn/post/7648441001858007086": "旧文回榜：RAG/Agent/MCP 学习路线。初学索引。",
    "https://juejin.cn/post/7649754424470929418": "旧文回榜：XTerminal 替 Xshell/FinalShell。工具安利。",
}


def insert_section(path: Path, section: str, heading: str) -> None:
    text = path.read_text(encoding="utf-8")
    marker = "## %s\n" % heading
    if text.startswith(marker) or ("\n" + marker) in text:
        raise SystemExit("section already exists in %s: %s" % (path, heading))
    lines = text.splitlines(keepends=True)
    insert_at = 0
    for i, line in enumerate(lines):
        if line.startswith("# "):
            insert_at = i + 1
            while insert_at < len(lines) and lines[insert_at].strip() == "":
                insert_at += 1
            while insert_at < len(lines) and not lines[insert_at].startswith("## "):
                insert_at += 1
            break
    path.write_text("".join(lines[:insert_at]) + section + "".join(lines[insert_at:]), encoding="utf-8")
    print("updated", path, heading)


def update_state_many(path: Path, dates: list) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    all_dates = set(data.get("processed_dates") or [])
    all_dates.update(dates)
    data["processed_dates"] = sorted(all_dates)
    latest = max(dates)
    prev = data.get("last_end_date") or latest
    data["last_end_date"] = max(prev, latest)
    data["last_sync_ymd"] = data["last_end_date"]
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("state", path, data["last_end_date"])


def merge_juejin_seen(state_path: Path, staging_path: Path, snap: str) -> None:
    staging = json.loads(staging_path.read_text(encoding="utf-8"))
    new_urls = [a["url"] for a in staging.get("new_articles") or [] if a.get("url")]
    data = json.loads(state_path.read_text(encoding="utf-8"))
    seen = set(data.get("seen_urls") or [])
    seen.update(new_urls)
    data["seen_urls"] = sorted(seen)
    dates = set(data.get("processed_dates") or [])
    dates.add(snap)
    data["processed_dates"] = sorted(dates)
    prev = data.get("last_end_date") or snap
    data["last_end_date"] = max(prev, snap)
    data["last_sync_ymd"] = data["last_end_date"]
    state_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("state", state_path, snap, "new_urls", len(new_urls))


def _metrics(article: dict) -> str:
    m = article.get("metrics") or {}
    like = m.get("like")
    collect = m.get("collect")
    view = m.get("view")
    parts = []
    if like is not None:
        parts.append("赞%s" % like)
    if collect is not None:
        parts.append("藏%s" % collect)
    if view is not None:
        parts.append("阅%s" % view)
    return "/".join(parts) if parts else "-"


def build_juejin_section(staging_path: Path) -> str:
    staging = json.loads(staging_path.read_text(encoding="utf-8"))
    arts = staging.get("new_articles") or []
    stats = staging.get("stats") or {}
    by_slot = {}
    for a in arts:
        for ap in a.get("appearances") or []:
            key = (ap.get("category"), ap.get("board"))
            by_slot.setdefault(key, []).append((ap.get("rank") or 0, a))
    for key in by_slot:
        by_slot[key].sort(key=lambda x: x[0])

    def slot_md(category: str, board: str) -> str:
        rows = by_slot.get((category, board)) or []
        if not rows:
            return "本槽无新增。\n"
        lines = [
            "| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |",
            "| --- | ---:| --- | --- | --- | --- |",
        ]
        for rank, a in rows:
            url = a.get("url") or ""
            title = a.get("list_title") or ""
            author = a.get("list_author") or ""
            summary = JJ_SUMMARIES.get(url) or "正文已取到，见链接。"
            lines.append(
                "| %s | [%s](%s) | %s | %s | %s | %s |"
                % (rank, title, url, author, _metrics(a), summary, url)
            )
        return "\n".join(lines) + "\n"

    multi = []
    for a in arts:
        apps = a.get("appearances") or []
        if len(apps) > 1:
            locs = ", ".join("%s/%s#%s" % (x.get("category"), x.get("board"), x.get("rank")) for x in apps)
            multi.append("%s → %s" % (a.get("url"), locs))
    multi_text = "；".join(multi) if multi else "无（本轮新 URL 均只出现在单一槽位）"

    src_rows = []
    for a in arts:
        for ap in a.get("appearances") or []:
            src_rows.append(
                "| %s | %s | %s | %s |"
                % (ap.get("category"), ap.get("board"), a.get("list_title") or "", a.get("url") or "")
            )

    return """## 2026-08-29

### 今日总览

**一句话结论**：`2026-08-29` 新 URL 主线是 **上下文工程/Harness、DeepSeek Harness 拆解、GLM-5.3-Flash 实测、Skill 怎么写与怎么评**；收藏榜补 FlutterKit、Agent 入门与「Skill 装多变笨」旧文。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 文章热榜 + 收藏热榜 × 后端/前端/人工智能/开发工具 |
| 榜单规模 | 每槽最多 15 条；列表总条数 %(listing)s；去重后新 URL **%(new)s**；跳过已见 **%(skip)s**；详情成功 %(ok)s / 失败 %(fail)s |
| 核心趋势 | 1）社区把 Agent 能力归因到 harness/上下文而不是再吹模型；2）国产 Flash 模型在热榜上用真实前端任务计价；3）Skill 从「多装」转向「能评、能共用一份」 |
| 可直接关注 | [上下文工程](https://juejin.cn/post/7677562804154531890)；[DeepSeek Harness 拆源码](https://juejin.cn/post/7677263893225193515)；[Skill 该怎么写](https://juejin.cn/post/7677435711276744745)；[Skill-Up 测评](https://juejin.cn/post/7677551269758795816) |

### 后端

#### 文章热榜

%(be_hot)s
#### 收藏热榜

%(be_col)s
### 前端

#### 文章热榜

%(fe_hot)s
#### 收藏热榜

%(fe_col)s
### 人工智能

#### 文章热榜

%(ai_hot)s
#### 收藏热榜

%(ai_col)s
### 开发工具

#### 文章热榜

%(dt_hot)s
#### 收藏热榜

%(dt_col)s
### 跨榜重复与去重说明

- 本轮新摘要 URL 数：%(new)s
- 因 `seen_urls` 跳过：%(skip)s（只给数量；不要把已见文再展开成表行）
- 同文多标签/双榜出现：%(multi)s

### 来源清单

- 快照日：2026-08-29（Asia/Shanghai）
- 页面：https://juejin.cn/hot/articles 、 https://juejin.cn/hot/collected-articles
- 抓取：`tools/juejin_hot_fetch.py` → `_staging_latest.json`

| 标签 | 榜单 | 标题 | 链接 |
| --- | --- | --- | --- |
%(src)s
""" % {
        "listing": stats.get("listing_slots", 120),
        "new": stats.get("unique_new_urls", len(arts)),
        "skip": stats.get("skipped_seen_urls", 0),
        "ok": stats.get("detail_ok", 0),
        "fail": stats.get("detail_fail", 0),
        "be_hot": slot_md("后端", "文章热榜"),
        "be_col": slot_md("后端", "收藏热榜"),
        "fe_hot": slot_md("前端", "文章热榜"),
        "fe_col": slot_md("前端", "收藏热榜"),
        "ai_hot": slot_md("人工智能", "文章热榜"),
        "ai_col": slot_md("人工智能", "收藏热榜"),
        "dt_hot": slot_md("开发工具", "文章热榜"),
        "dt_col": slot_md("开发工具", "收藏热榜"),
        "multi": multi_text,
        "src": "\n".join(src_rows),
    }


def main() -> None:
    ai_pairs = [
        ("2026-08-25", AI_25),
        ("2026-08-26", AI_26),
        ("2026-08-27", AI_27),
        ("2026-08-28", AI_28),
    ]
    kb_pairs = [
        ("2026-08-25", KB_25),
        ("2026-08-26", KB_26),
        ("2026-08-27", KB_27),
        ("2026-08-28", KB_28),
    ]
    for heading, sec in ai_pairs:
        insert_section(ROOT / "dailyReport/ai-daily-news/ai-daily-digest.md", sec, heading)
        insert_section(ROOT / "dailyReport/ai-daily-news/202608.md", sec, heading)
    for heading, sec in kb_pairs:
        insert_section(ROOT / "dailyReport/knowledge-base-news/knowledge-base-digest.md", sec, heading)
        insert_section(ROOT / "dailyReport/knowledge-base-news/202608.md", sec, heading)

    jj = build_juejin_section(ROOT / "dailyReport/juejin-hot-news/_staging_latest.json")
    insert_section(ROOT / "dailyReport/juejin-hot-news/juejin-hot-digest.md", jj, "2026-08-29")
    insert_section(ROOT / "dailyReport/juejin-hot-news/202608.md", jj, "2026-08-29")

    update_state_many(
        ROOT / "dailyReport/ai-daily-news/ai-daily-state.json",
        ["2026-08-25", "2026-08-26", "2026-08-27", "2026-08-28"],
    )
    update_state_many(
        ROOT / "dailyReport/knowledge-base-news/knowledge-base-state.json",
        ["2026-08-25", "2026-08-26", "2026-08-27", "2026-08-28"],
    )
    merge_juejin_seen(
        ROOT / "dailyReport/juejin-hot-news/juejin-hot-state.json",
        ROOT / "dailyReport/juejin-hot-news/_staging_latest.json",
        "2026-08-29",
    )


if __name__ == "__main__":
    main()

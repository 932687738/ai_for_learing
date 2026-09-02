# -*- coding: utf-8 -*-
"""Incremental digest pull: AI/KB 2026-08-31..09-01 + Juejin 2026-09-02 (cross-month trim)."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

AI_HEADER = """# AI Daily News Digest

按 Asia/Shanghai 时区增量汇总 AI/人工智能相关每日资讯。
"""

KB_HEADER = """# Knowledge Base Digest

按 Asia/Shanghai 时区增量汇总固定中文技术知识库来源。
"""

JJ_HEADER = """# Juejin Hot Digest

按 Asia/Shanghai 时区汇总掘金文章热榜与收藏热榜（后端 / 前端 / 人工智能 / 开发工具），按文章链接去重并归纳正文。
"""

AI_31 = """## 2026-08-31

### 今日总览

**一句话结论**：8 月 31 日主线是 **OpenClaw `2026.8.1`（品牌化 2.0：会话改 SQLite、权限与凭证默认值重写）**、**Langfuse `v4.25.0`（Web 表格列标准化）**，以及 **DeepSeek-V4-Flash-Vision-Exp 开源权重（MIT，Hugging Face）**；编程 CLI 无中国时间窗口内的新稳定版。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 官方厂商、开源 release、Claude Code/Codex/OpenClaw/Hermes、Spring AI/Alibaba AI、Langfuse、LangChain/LangGraph、Code Graph、Loop Engineering、skills、论文与政策、中文补充 |
| 核心趋势 | 1）个人 Agent runtime 把「会话存储/权限/凭证」当成一次 breaking 大版本，而不是再叠小功能；2）可观测平台继续做 UI 工程债而不是新协议；3）多模态开源权重补上 API 已上线 10 天的 Vision-Exp |
| 可直接关注 | 升级 OpenClaw 前备份并读 SQLite 迁移；Langfuse 自托管跟到 `v4.25.0`；本地评 Vision-Exp 用官方 HF 仓而不是转载新闻 |
| 专项检索结论 | OpenClaw：`v2026.8.1`（Published 2026-08-31T03:30:51Z，中国时间 11:30，AKA 2.0）。Langfuse：`v4.25.0`（2026-08-31T10:42:43Z，中国时间 18:42）。Claude Code：当日无中国时间窗口内的新 tag（`v2.1.252` 落在 9/1 03:46）。Codex：仅有 `0.152.0-alpha.*`，稳定版仍为 8/29 的 `0.151.0`。Hermes：`v0.21.0`/`v2026.8.31` 的 Published 为 UTC 19:29，记入 9/1。Spring AI / Spring Alibaba AI / LangChain·LangGraph / Code Graph / Loop Engineering / skills：未发现可核验的 8/31 重大稳定版更新。 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| Agent runtime | [OpenClaw 2026.8.1（AKA 2.0）](https://github.com/openclaw/openclaw/releases/tag/v2026.8.1) | 2026-08-31 | 开源发布 | 会话/转写迁到 SQLite，降级需先还原归档；安装与 onboarding 默认值、session 权限模式、插件信任审查、私有凭证一并改写。官方说明：`openclaw doctor --fix` 可处理大部分 breaking。详见 [release notes](https://docs.openclaw.ai/releases/2026.8.1) |
| LLM 可观测 | [Langfuse v4.25.0](https://github.com/langfuse/langfuse/releases/tag/v4.25.0) | 2026-08-31 | 开源发布 | Web 表格列（文本/数字/Token Usage/下拉）抽到统一工厂，并加 design-system import 边界。无新 Public API / MCP 能力；自托管升级主要是 UI 一致性 |
| 开源模型 | [DeepSeek-V4-Flash-Vision-Exp](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp) | 2026-08-31 | 开源发布 | V4 系首个多模态实验权重，MIT；含 tokenizer、prompt encoding 与覆盖 ViT/Aligner/DFlash/MoE/DSpark 的最小 PyTorch 推理。API 已于 8/21 上线，本日是权重+参考实现 |
| 服务可用性 | [ChatGPT Work elevated errors and latency](https://status.openai.com/incidents/01M1C5M4K0WC8PPT0Z175RJA1E) | 2026-08-31 | 官方状态 | Plus 用户 Work 模式一度不可用，当日已缓解。企业排障先查 status，不要当成模型能力回归 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| 升级路径 | [v2026.8.1 release notes](https://docs.openclaw.ai/releases/2026.8.1) | SQLite 会话、权限默认值、插件 SDK 子路径弃用时间表 | 已在跑 Gateway / 写 OpenClaw 插件的人 |
| 多模态推理 | [HF 仓 + inference/](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp) | 参考实现与权重分片分开，无 symlink 依赖 | 要本地复现 Vision-Exp 而不是只调 API 的人 |
| 可观测 UI | [Langfuse v4.25.0](https://github.com/langfuse/langfuse/releases/tag/v4.25.0) | 表格列组件边界，避免业务页直接引设计系统内部件 | 自托管 Langfuse 或二次开发 Web 的人 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：本日工程增量集中在「个人 Agent 的存储/权限默认值」和「多模态权重可本地跑」；编排框架与 Java AI 无新 GA。OpenClaw 把 maker/checker 之外的**会话持久化与凭证默认值**当成 2.0 的真正 breaking。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| OpenClaw / Loop | 2.0 改会话存储与权限默认 | 升级前备份；长任务 loop 先保证会话可迁、可回滚，再谈新 skill |
| Langfuse | v4.25.0 UI 列标准化 | 观测平台的债往往在表格/权限边界，不是再接一个 exporter |
| DeepSeek Vision | 权重+参考实现同日放出 | Agent 截图/OCR 任务可切到开源权重做离线评测 |
| Claude Code / Codex | 无中国时间窗口稳定版 | 不要把 UTC 当晚的 `v2.1.252` / Hermes `0.21.0` 记进本日 |
| 其余专项 | Hermes / Spring* / LangChain / Code Graph / skills | 未发现 8/31 重大稳定更新 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | [OpenClaw 2026.8.1 notes](https://docs.openclaw.ai/releases/2026.8.1) | 本月最大 runtime 变更，按中国时间记本日 |
| 推荐 | [DeepSeek-V4-Flash-Vision-Exp](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp) | 官方权重与参考实现，优于中文门户转载 |
| 延伸 | [Langfuse v4.25.0](https://github.com/langfuse/langfuse/releases/tag/v4.25.0) | 确认本日没有新 trace/eval API |

### 来源清单

- 检索范围：2026-08-31 00:00:00 到 2026-08-31 23:59:59（Asia/Shanghai）
- 引用域名：github.com, docs.openclaw.ai, huggingface.co, status.openai.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 开源发布 | OpenClaw 2026.8.1 | 2026-08-31 | https://github.com/openclaw/openclaw/releases/tag/v2026.8.1 |
| 官方文档 | v2026.8.1 (AKA OpenClaw 2.0) | 2026-08-31 | https://docs.openclaw.ai/releases/2026.8.1 |
| 开源发布 | Langfuse v4.25.0 | 2026-08-31 | https://github.com/langfuse/langfuse/releases/tag/v4.25.0 |
| 开源发布 | DeepSeek-V4-Flash-Vision-Exp | 2026-08-31 | https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp |
| 官方发布 | ChatGPT Work incident | 2026-08-31 | https://status.openai.com/incidents/01M1C5M4K0WC8PPT0Z175RJA1E |

"""

AI_01 = """## 2026-09-01

### 今日总览

**一句话结论**：9 月 1 日主线是 **Hermes Agent `v0.21.0`（Bot Mode / cron 记忆 / 子 Agent 中途转向）**、**Codex `0.152.0`（MCP 包名、每工具输出上限、update_plan 改 opt-in）**、**Claude Code `v2.1.252`（Mac Bash swap / Remote Control 卡住）**，以及 **Langfuse `v4.26.0`+`v4.27.0`（eval trace 串联、in-app agent 多模态）**。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 官方厂商、开源 release、Claude Code/Codex/OpenClaw/Hermes、Spring AI/Alibaba AI、Langfuse、LangChain/LangGraph、Code Graph、Loop Engineering、skills、论文与政策 |
| 核心趋势 | 1）编程 Agent 把「多 bot 社会 + 定时任务有记忆」做成产品默认；2）Codex 收紧默认工具面（planning 改 opt-in）同时放宽 MCP 命名；3）可观测平台补 eval↔trace 与站内 agent |
| 可直接关注 | Hermes Bot Mode/`hermes peer`；Codex `tools.update_plan.enabled`；Langfuse evaluator execution traces；不要把 `v2.1.257`/`OpenClaw 2026.8.2` 记进本日 |
| 专项检索结论 | Hermes：`v0.21.0`/`v2026.8.31`（Published 2026-08-31T19:29:49Z，中国时间 9/1 03:29）。Claude Code：`v2.1.252`（2026-08-31T19:46:55Z，中国时间 9/1 03:46）。Codex：`rust-v0.152.0`（2026-09-01T01:58:32Z，中国时间 09:58）。Langfuse：`v4.26.0`（UTC 8/31 17:53 → 中国 9/1 01:53）+ `v4.27.0`（2026-09-01T10:55:03Z，中国时间 18:55）。OpenClaw：`2026.8.2` Published 2026-09-01T16:00:56Z = 中国 9/2 00:00，**不记本日**。Claude Code `v2.1.257`/`v2.1.258` 同理落在 9/2。Spring AI / Spring Alibaba AI / LangChain·LangGraph / Code Graph / skills：未发现可核验的 9/1 重大稳定版更新。 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| Agent runtime | [Hermes Agent v0.21.0 (v2026.8.31)](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.31) | 2026-09-01（UTC 8/31 19:29） | 开源发布 | Bot Mode 内置：命名 bot、群聊、`hermes peer` 跨 profile DM；cron 带 persistent memory/`continuity`；`delegate_task` 可中途 steer/停；MCP 桌面变成健康检查+用量看板；保护 AGENTS.md/skills 写审批。官方自称 Pantheon Release |
| 编程 CLI | [Codex 0.152.0](https://github.com/openai/codex/releases/tag/rust-v0.152.0) | 2026-09-01 | 开源发布 | Vim `/` `?` 搜索草稿；限流横幅可跳转用量/套餐；MCP 名允许 `:` `@` `/` `.`；每工具 `output_token_limit`；`thread/shellCommand` 超时可超 1h；**`update_plan` 默认关闭**（`tools.update_plan.enabled = true`）；修 Guardian 压缩丢授权、Windows Store PowerShell 沙箱、云任务拒绝不信任 URL |
| 编程 CLI | [Claude Code v2.1.252](https://github.com/anthropics/claude-code/releases/tag/v2.1.252) | 2026-09-01（UTC 8/31 19:46） | 开源发布 | 修部分 Mac「task output swap refused」；无 `.claude/settings.local.json` 时 always-allow 不落盘；Remote Control 在 claude.ai 降级时工具结束后卡数分钟；超大失败输出把会话撑爆 API 上限 |
| LLM 可观测 | [Langfuse v4.26.0](https://github.com/langfuse/langfuse/releases/tag/v4.26.0) | 2026-09-01（UTC 8/31 17:53） | 开源发布 | evaluator execution traces 可回链；PR 可预览 API spec；修 eval structured output 与 reasoning 碰撞、OTel prompt version 当整数解析、in-app-agent OpenAI Responses 保持无状态 |
| LLM 可观测 | [Langfuse v4.27.0](https://github.com/langfuse/langfuse/releases/tag/v4.27.0) | 2026-09-01 | 开源发布 | in-app-agent 支持多模态输入与 prompt cache；OpenAI Responses 网关；修输出 token 截断空白轮、Claude id 强制 reasoning、S3 multipart 等分片 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| 多 Agent 产品化 | [Hermes v0.21.0](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.31) | Bot 社会、cron 连续性、子 Agent 直播转向、MCP 指挥中心 | 要把「一堆 profile」变成可协作团队的人 |
| 默认工具面 | [Codex 0.152.0](https://github.com/openai/codex/releases/tag/rust-v0.152.0) | planning 改 opt-in；MCP 输出按工具截断 | 升级后发现 update_plan 没了的人 |
| eval 可追溯 | [Langfuse v4.26.0](https://github.com/langfuse/langfuse/releases/tag/v4.26.0) | 评分运行留下 execution trace | 要解释「这条 score 怎么来的」的评测同学 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：Loop Engineering 当日信号在 Hermes：定时任务必须带记忆与连续性，子 Agent 必须可中途纠偏，且保护指令文件写入。Codex 把 planning 从默认能力改成显式开关，和「少给默认工具」同一方向。OpenClaw `2026.8.2`、Claude Code `v2.1.257`（含 Fable 5.1 默认）落在中国时间 9/2，不记本日。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| Hermes / Loop | Bot Mode + cron memory + live steer | 定时 loop 没有昨天的输出就不能去重；子 Agent 不能 fire-and-pray |
| Codex | MCP 包名 + 每工具截断 + plan opt-in | 默认工具越少越好；截断策略按工具而不是全局一刀 |
| Claude Code | v2.1.252 稳定性 | Remote Control 与超大失败日志会直接打爆上下文，先修通道再谈新模型 |
| Langfuse | v4.26–4.27 eval 链 + 站内 agent | 评分必须能点回原始 span；站内 agent 也要走同一套 OTel |
| OpenClaw | 8.2 落在 9/2 | 8/31 的 2.0 仍是当前应读版本 |
| 其余专项 | Spring* / LangChain / Code Graph / skills | 未发现 9/1 重大稳定更新 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | [Hermes v0.21.0](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.31) | 本窗口最大 Agent 产品变更，按中国时间记本日 |
| 必读 | [Codex 0.152.0](https://github.com/openai/codex/releases/tag/rust-v0.152.0) | 默认工具面收紧 + MCP 工程补丁 |
| 推荐 | [Langfuse v4.27.0](https://github.com/langfuse/langfuse/releases/tag/v4.27.0) | 站内 agent 多模态与 cache，和 v4.26 一起升 |
| 延伸 | [Claude Code v2.1.252](https://github.com/anthropics/claude-code/releases/tag/v2.1.252) | 中国时间窗口内的稳定补丁；Fable 5.1 等 9/2 |

### 来源清单

- 检索范围：2026-09-01 00:00:00 到 2026-09-01 23:59:59（Asia/Shanghai）
- 引用域名：github.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 开源发布 | Hermes Agent v0.21.0 | 2026-09-01（UTC 8/31 19:29） | https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.31 |
| 开源发布 | Codex 0.152.0 | 2026-09-01 | https://github.com/openai/codex/releases/tag/rust-v0.152.0 |
| 开源发布 | Claude Code v2.1.252 | 2026-09-01（UTC 8/31 19:46） | https://github.com/anthropics/claude-code/releases/tag/v2.1.252 |
| 开源发布 | Langfuse v4.26.0 | 2026-09-01（UTC 8/31 17:53） | https://github.com/langfuse/langfuse/releases/tag/v4.26.0 |
| 开源发布 | Langfuse v4.27.0 | 2026-09-01 | https://github.com/langfuse/langfuse/releases/tag/v4.27.0 |

"""

KB_31 = """## 2026-08-31

### 今日总览

本次按 Asia/Shanghai 的 2026-08-31 00:00:00 到 23:59:59 检索固定知识库来源，并专项检索 Langfuse、LangChain/LangGraph、Code Graph、Spring Alibaba AI、Loop Engineering。固定门户内**未发现可确认属于该日期且具备可靠原文的重大技术长文**；腾讯云+社区出现 DeepSeek-V4-Flash-Vision-Exp 开源资讯，但是 IT之家/企鹅号转载，按过滤规则不收录正文（官方权重见 AI 日报 Hugging Face）。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 阿里/腾讯/字节/百度/美团/京东/滴滴/网易/360/有赞 + 掘金 + 五个专项 |
| 核心趋势 | 门户在节日窗口以转载资讯为主，工程长文空窗 |
| 可直接关注 | 多模态开源权重以 HF 官方仓为准，不要用转载当出处 |
| 专项检索结论 | Langfuse / LangChain·LangGraph / Code Graph / Spring Alibaba AI / Loop Engineering：固定来源内均未发现可核验的 8/31 新文 |
| 未发现更新 | 阿里技术、阿里中间件、语雀阿里干货、腾讯技术工程、AlloyTeam、腾讯大讲堂、字节技术博客、FEX/EFE、百度开发者中心、美团技术团队、京东科技、凹凸、滴滴、网易传媒、360、有赞 |

### 重要文章与更新

- 未发现可核验的重大文章或更新。

### 技术文档与实践

- 未发现值得收录的新文档或实践文章。

### 工程实践归纳

**总体判断**：五个专项在固定来源内未发现可核验更新；全球侧 OpenClaw 2.0 / Langfuse v4.25.0 / DeepSeek Vision 权重见 AI 日报，不在此伪装成门户原文。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 五个专项 | 固定来源无新文 | 空窗日不要用转载新闻填表 |

### 值得深入阅读的资料

- 本日暂无推荐。

### 来源清单

- 检索范围：2026-08-31 00:00:00 到 2026-08-31 23:59:59（Asia/Shanghai）
- 固定来源覆盖：已覆盖固定来源清单中的公司/组织维度
- 来源清单表格：

| 公司/组织 | 来源 | 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- | --- | --- |
| 全部 | 固定来源清单 | 无新增 | 无可靠新增来源 | - | - |

"""

KB_01 = """## 2026-09-01

### 今日总览

本次按 Asia/Shanghai 的 2026-09-01 00:00:00 到 23:59:59 检索固定知识库来源，并专项检索 Langfuse、LangChain/LangGraph、Code Graph、Spring Alibaba AI、Loop Engineering，未发现可确认属于该日期且具备可靠出处的重大技术更新。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 阿里/腾讯/字节/百度/美团/京东/滴滴/网易/360/有赞 + 掘金 + 五个专项 |
| 核心趋势 | 月初工作日门户仍无新长文；全球 Hermes 0.21.0 / Codex 0.152.0 不在固定来源原文中 |
| 可直接关注 | 继续等大厂博客，不要把掘金热榜测评误写入知识库日更 |
| 专项检索结论 | Langfuse / LangChain·LangGraph / Code Graph / Spring Alibaba AI / Loop Engineering：固定来源内均未发现可核验的 9/1 新文 |
| 未发现更新 | 阿里技术、阿里云开发者社区、阿里中间件、语雀、腾讯技术工程、腾讯云+社区、AlloyTeam、字节技术博客、美团、京东、滴滴、百度、360、有赞等 |

### 重要文章与更新

- 未发现可核验的重大文章或更新。

### 技术文档与实践

- 未发现值得收录的新文档或实践文章。

### 工程实践归纳

- 未发现可复现价值明确的新进展。

### 值得深入阅读的资料

- 本日暂无推荐。

### 来源清单

- 检索范围：2026-09-01 00:00:00 到 2026-09-01 23:59:59（Asia/Shanghai）
- 固定来源覆盖：已覆盖固定来源清单中的公司/组织维度
- 来源清单表格：

| 公司/组织 | 来源 | 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- | --- | --- |
| 全部 | 固定来源清单 | 无新增 | 无可靠新增来源 | - | - |

"""

JJ_SUMMARIES = {
    "https://juejin.cn/post/7680014875347255334": "讲 Redis 从缓存变成 AI 实时数据层：向量搜索、Vector Sets、语义缓存、Agent 上下文。适合成熟业务里已经有 Redis、想少引一套向量库的人。偏能力地图，生产数字以官方文档为准。",
    "https://juejin.cn/post/7680375814231605299": "反驳「OpenSearch 只是 ES 7.10 fork」：Linux 基金会、Apache 2.0、独立演进。适合还在 ES 许可/云厂商之间做搜索选型的人。不是性能对打评测。",
    "https://juejin.cn/post/7678975158596894729": "用一条「智能流水线」讲 LangChain：先建立 Chain/Agent/Memory 心智，不背混乱 API。点出旧 Memory、消息历史、LangGraph 三套示例并存。适合会 Python、没正经用过 LangChain 的人。",
    "https://juejin.cn/post/7678157950376378383": "博客库拆 6 张表，重点打「点赞表联合主键上再加 postId 索引」这个新手多余索引。适合刚写 schema 的后端。案例小，原则是联合主键左前缀够用就别再加。",
    "https://juejin.cn/post/7679053043288326150": "Nest 第一步第 3 篇：Controller/Service/Module 对照前端路由/工具函数/barrel。适合从前端转 Nest 的人。系列文，要连着前两篇看。",
    "https://juejin.cn/post/7678239521201307657": "用 Claude Code 从 0 搭单词后台：Next.js + Supabase + Drizzle + shadcn。重点写云库、ORM、密码哈希、effect 里读 localStorage。适合跟一遍全栈的人。是学习记录不是框架发布。",
    "https://juejin.cn/post/7680357430018949135": "安利 Claude Academy：按角色教怎么用好 Claude，不是新模型发布。适合要给团队找官方教程入口的人。平台内容会变，以官网为准。",
    "https://juejin.cn/post/7680043958139781174": "一条线串 Spring Boot：自动装配、starter、过滤器/拦截器、常见设计模式。适合停留在「加依赖就能跑」的人。综述，版本细节以当下 Boot 为准。",
    "https://juejin.cn/post/7679985418771218470": "用 git/PRD 自动出进度和周报，吐槽 Jira/禅道太重。产品向，适合被周报折磨的全栈。注意把提交当进度会鼓励碎片 commit，治理仍要人审。",
    "https://juejin.cn/post/7680025405151084571": "cos-design v3.8.0 五个可交互背景（泡泡/蒲公英/熔岩/墨染/极光），拆算法与试玩。适合活动页/登录屏要轻量动效的前端。Canvas/WebGL，注意电量和无障碍。",
    "https://juejin.cn/post/7678577086287118370": "Three.js 浏览器跑车 Demo，偏娱乐。适合想抄一辆能开的车模的人。不是生产组件库。",
    "https://juejin.cn/post/7679542577553506358": "栗子周刊 144（8/24–8/30）：Rspack 2.2、pnpm 12、Solid 2.0 RC 等索引。适合扫一周前端发布。条目浅，点原链接。",
    "https://juejin.cn/post/7678644473824657443": "Vue3 低代码里让 Schema 的 `componentProps` 按组件名出完整类型：条件类型/模板字面量/映射类型，绕开泛型组件偏弱。适合写 Schema 驱动表单的人。",
    "https://juejin.cn/post/7678974488122032180": "把 Costumy 科研原型改成 Vite+Electron+React+Python 桌面打版：前端预览，Python 做 2D→3D。记录三个难坑。适合桌面+科学计算桥接。",
    "https://juejin.cn/post/7679623224678613034": "豆包工作 Agent 实测：飞书体系、多端、云电脑、Skill、Seedance。产品测评，适合对比办公 Agent。能力以官方当前版本为准。",
    "https://juejin.cn/post/7680143535669198858": "用 Qwen3.8-Max 做电商资料包体检：多文件+图一次对型号/授权/功效证据。适合运营质检。数字来自作者样本，不要当通用准确率。",
    "https://juejin.cn/post/7680023541135507497": "介绍微信 WeMM-Embedding：生产级多模态向量、Apache 2.0、2B 打平更大模型的宣传口径。适合要图文检索/推荐的人。去 GitHub 核版本与评测表，本文是科普。",
    "https://juejin.cn/post/7679542577553473590": "DeepSeek Harness 发布半月后的 10 个插件清单：dsh-market、视觉、侧栏、搜索等。适合已经装上 dsh、界面还是毛坯的人。插件会变，先看官方 market。",
    "https://juejin.cn/post/7675992325912887315": "掘金作品广场与用量统计：从 Show me your code 到 works/token。产品公告向。适合要曝光 AI 作品或看 token 消耗的作者。",
    "https://juejin.cn/post/7678646261259092004": "ZCode 周末送 3 亿 Token 活动说明（GLM-5.3-Flash）。偏营销，略读。额度窗口以活动页为准。",
    "https://juejin.cn/post/7679020474672660526": "开源 Usora：把和 Codex/Claude 解过的问题沉淀成可复用 Skills，跨 Agent 共享。适合被「每次重教一遍」折磨的人。项目早期，治理/鉴权要自己看仓库。",
    "https://juejin.cn/post/7680025405152608283": "React+Express+MySQL：有 dist 不等于能上线，要对齐前端请求、后端环境、MySQL 授权、进程。适合第一次部署全栈的人。命令来自作者项目，运行未验证。",
    "https://juejin.cn/post/7679542577527291958": "怎么读 36K star 的 react-bits：当「动画交互组件」而不是直接当业务库。适合想从展示型仓学组织方式的人。",
    "https://juejin.cn/post/7678520027876835355": "用 AI 辅助分析 Charles 授权：混淆代码里发现硬编码密钥，复盘方法而不是给破解步骤。适合做安全意识/授权设计的人。不要用来绕过授权。",
    "https://juejin.cn/post/7678240005149687817": "介绍高星开源：让编码 Agent 根据仓库画出可点、可查、可导出的架构图，一行命令。适合评估「AI 画架构图」值不值得装。输出仍要人审。",
    "https://juejin.cn/post/7677859417393053696": "Docker 部署 Calibre-Web 0.6.27 做网页书房，打通多端书库。适合自托管电子书。注意映射书库卷和用户权限。",
    "https://juejin.cn/post/7649363408022683689": "收藏榜：Spring Boot 老手看 FastAPI Hello World 的体感对比。入门安利，不是生产对打。适合两栈都要摸的人。",
    "https://juejin.cn/post/7669003422981619753": "收藏榜：Nginx 入门（反代、静态、常见指令）。适合第一次碰网关的人。配置以当前稳定版文档为准。",
    "https://juejin.cn/post/7667465942311829555": "收藏榜：VS Code「简单部署」扩展，少开终端/SFTP 传 dist。适合多项目重复发布的前端。传错目录/覆盖配置仍要自己防。",
    "https://juejin.cn/post/7653409231856877631": "收藏榜：GSD vs OpenSpec vs Superpowers，对比 spec-driven / 上下文工程，反对纯 vibe coding。适合要给仓库选一套流程 Skill 的人。版本会变，先看各仓 README。",
}


def ensure_file(path: Path, header: str) -> None:
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(header.rstrip() + "\n\n", encoding="utf-8")
        print("created", path)


def insert_section(path: Path, section: str, heading: str) -> None:
    text = path.read_text(encoding="utf-8")
    marker = "## %s\n" % heading
    if text.startswith(marker) or ("\n" + marker) in text:
        raise SystemExit("section already exists in %s: %s" % (path, heading))
    if not section.endswith("\n"):
        section = section + "\n"
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


def trim_digest(path: Path, year_month: str) -> None:
    text = path.read_text(encoding="utf-8")
    parts = re.split(r"(?=^## )", text, flags=re.M)
    head = parts[0]
    kept = [p for p in parts[1:] if p.startswith("## %s-" % year_month)]
    path.write_text(head.rstrip() + "\n\n" + "".join(kept).lstrip(), encoding="utf-8")
    print("trimmed", path, "keep", year_month, "sections", len(kept))


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
            locs = ", ".join(
                "%s/%s#%s" % (x.get("category"), x.get("board"), x.get("rank")) for x in apps
            )
            multi.append("%s → %s" % (a.get("url"), locs))
    multi_text = "；".join(multi) if multi else "无（本轮新 URL 均只出现在单一槽位）"

    src_rows = []
    for a in arts:
        for ap in a.get("appearances") or []:
            src_rows.append(
                "| %s | %s | %s | %s |"
                % (ap.get("category"), ap.get("board"), a.get("list_title") or "", a.get("url") or "")
            )

    missing = [a.get("url") for a in arts if a.get("url") not in JJ_SUMMARIES]
    if missing:
        raise SystemExit("missing juejin summaries: %s" % missing)

    return """## 2026-09-02

### 今日总览

**一句话结论**：`2026-09-02` 新 URL 主线是 **Redis/OpenSearch 当 AI 数据层、LangChain 入门心智、豆包工作/WeMM-Embedding/DeepSeek Harness 插件，以及 GSD vs OpenSpec vs Superpowers**；收藏榜补 FastAPI/Nginx/VS Code 部署旧文。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 文章热榜 + 收藏热榜 × 后端/前端/人工智能/开发工具 |
| 榜单规模 | 每槽最多 15 条；列表总条数 %(listing)s；去重后新 URL **%(new)s**；跳过已见 **%(skip)s**；详情成功 %(ok)s / 失败 %(fail)s |
| 核心趋势 | 1）后端热榜在讲「已有中间件怎么接向量/搜索」而不是再造框架；2）AI 槽是办公 Agent 测评 + 开源 embedding/Harness 插件；3）开发工具收藏榜继续吃流程 Skill 对比文 |
| 可直接关注 | [Redis 接入 AI](https://juejin.cn/post/7680014875347255334)；[LangChain 流水线](https://juejin.cn/post/7678975158596894729)；[WeMM-Embedding](https://juejin.cn/post/7680023541135507497)；[GSD vs OpenSpec vs Superpowers](https://juejin.cn/post/7653409231856877631) |

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

- 快照日：2026-09-02（Asia/Shanghai）
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
    ensure_file(ROOT / "dailyReport/ai-daily-news/202609.md", AI_HEADER)
    ensure_file(ROOT / "dailyReport/knowledge-base-news/202609.md", KB_HEADER)
    ensure_file(ROOT / "dailyReport/juejin-hot-news/202609.md", JJ_HEADER)

    insert_section(ROOT / "dailyReport/ai-daily-news/202608.md", AI_31, "2026-08-31")
    insert_section(ROOT / "dailyReport/ai-daily-news/ai-daily-digest.md", AI_31, "2026-08-31")
    insert_section(ROOT / "dailyReport/ai-daily-news/202609.md", AI_01, "2026-09-01")
    insert_section(ROOT / "dailyReport/ai-daily-news/ai-daily-digest.md", AI_01, "2026-09-01")
    trim_digest(ROOT / "dailyReport/ai-daily-news/ai-daily-digest.md", "2026-09")

    insert_section(ROOT / "dailyReport/knowledge-base-news/202608.md", KB_31, "2026-08-31")
    insert_section(ROOT / "dailyReport/knowledge-base-news/knowledge-base-digest.md", KB_31, "2026-08-31")
    insert_section(ROOT / "dailyReport/knowledge-base-news/202609.md", KB_01, "2026-09-01")
    insert_section(ROOT / "dailyReport/knowledge-base-news/knowledge-base-digest.md", KB_01, "2026-09-01")
    trim_digest(ROOT / "dailyReport/knowledge-base-news/knowledge-base-digest.md", "2026-09")

    jj = build_juejin_section(ROOT / "dailyReport/juejin-hot-news/_staging_latest.json")
    insert_section(ROOT / "dailyReport/juejin-hot-news/juejin-hot-digest.md", jj, "2026-09-02")
    insert_section(ROOT / "dailyReport/juejin-hot-news/202609.md", jj, "2026-09-02")
    trim_digest(ROOT / "dailyReport/juejin-hot-news/juejin-hot-digest.md", "2026-09")

    update_state_many(
        ROOT / "dailyReport/ai-daily-news/ai-daily-state.json",
        ["2026-08-31", "2026-09-01"],
    )
    update_state_many(
        ROOT / "dailyReport/knowledge-base-news/knowledge-base-state.json",
        ["2026-08-31", "2026-09-01"],
    )
    merge_juejin_seen(
        ROOT / "dailyReport/juejin-hot-news/juejin-hot-state.json",
        ROOT / "dailyReport/juejin-hot-news/_staging_latest.json",
        "2026-09-02",
    )


if __name__ == "__main__":
    main()

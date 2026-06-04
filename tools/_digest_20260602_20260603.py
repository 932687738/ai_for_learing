# -*- coding: utf-8 -*-
"""Incremental digest writer for 2026-06-02 and 2026-06-03."""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

AI_DIGEST = os.path.join(ROOT, "dailyReport", "ai-daily-news", "ai-daily-digest.md")
AI_STATE = os.path.join(ROOT, "dailyReport", "ai-daily-news", "ai-daily-state.json")
KB_DIGEST = os.path.join(ROOT, "dailyReport", "knowledge-base-news", "knowledge-base-digest.md")
KB_STATE = os.path.join(ROOT, "dailyReport", "knowledge-base-news", "knowledge-base-state.json")

AI_HEADER = (
    "# AI Daily News Digest\n\n"
    "按 Asia/Shanghai 时区增量汇总 AI/人工智能相关每日资讯。"
)
KB_HEADER = (
    "# Knowledge Base Digest\n\n"
    "按 Asia/Shanghai 时区增量汇总固定中文技术知识库来源。"
)

BATCH_DATES = ["2026-06-02", "2026-06-03"]

SECTION_DATE_RE = re.compile(r"^## (\d{4}-\d{2}-\d{2})\s*$", re.MULTILINE)

AI_SECTIONS = {
    "2026-06-03": """## 2026-06-03

### 今日总览

**一句话结论**：`2026-06-03` 是 **「Microsoft Build 第二日竞争叙事 + OpenAI 前沿治理蓝图 + Anthropic 伙伴网络分层」**——The Verge 解读 **Microsoft 与 OpenAI 竞合**；OpenAI 发布 **frontier AI 治理蓝图** 并升级 **GPT-Rosalind** 能力；Anthropic 推出 **Claude Partner Network Services Track / Partner Hub** 与 **LLM ATT&CK Navigator**；当日 **OpenAI API/ChatGPT/Codex 曾短暂 5xx  outage 后修复**。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | OpenAI/Anthropic 官方；Microsoft Build 延续；TechCrunch/The Verge；arXiv agent 论文；专项工具链 |
| 核心趋势 | **平台竞合**：Microsoft 自研 MAI + Scout(OpenClaw) vs OpenAI Codex 知识工作者化；**治理**：联邦 frontier 安全框架 + 州法协同；**生态**：Anthropic 伙伴分级与 ATT&CK 映射 |
| 可直接关注 | 跟踪 **GPT-Rosalind** 企业 Trusted Access 边界；评估 **Partner Hub MCP** 对 SI 交付流程；**API outage** 后重跑关键 batch |
| 专项检索结论 | **Claude Code**：无 6/3 新 release（最近 **v2.1.161 为 2026-06-02**）；**Codex**：**无 6/3 GitHub release**（**0.137.0-alpha.4 为 2026-06-03 UTC 凌晨**）；**OpenClaw/Hermes**：Build 周 **Scout/NemoClaw** 生态报道延续，无新 tag；**Spring AI**：无 6/3 官方 release；**skills**：Anthropic **Partner Hub MCP** 与 Codex **Life Sciences plugin** 生态延续 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| 政策 / 治理 | [A blueprint for democratic governance of frontier AI](https://openai.com/index/frontier-safety-blueprint/) | **2026-06-03** | 官方发布 | 三件套：联邦框架 + 强化 CAISI + 跨部门韧性计划；衔接 CA SB 53 / NY RAISE / IL SB 315 |
| 生命科学 AI | [Introducing GPT-Rosalind（6/3 能力更新）](https://openai.com/index/introducing-gpt-rosalind/) | **2026-06-03** | 官方产品 | 融合 **GPT-5.5 agentic coding/tool use** 加速药物发现/实验工作流；Trusted Access 限定 |
| Anthropic / 生态 | [Services Track and Partner Hub — Claude Partner Network](https://www.anthropic.com/news/services-track-partner-hub) | **2026-06-03** | 官方发布 | **Select/Preferred/Global Premier** 三级 + **Partner Hub MCP**；40k+ 申请、10k+ 认证 |
| 安全研究 | [LLM ATT&CK Navigator](https://red.anthropic.com/2026/attack-navigator/) | **2026-06-03** | 官方发布 | 将 LLM 攻击技术映射 MITRE ATT&CK；结合 Verizon DBIR 2026 语境 |
| Microsoft / 竞合 | [Microsoft and OpenAI broke up — now they're ready to fight（The Verge）](https://www.theverge.com/ai-artificial-intelligence/942242/microsoft-build-ai-agents-openai-competition) | **2026-06-03** | 技术媒体 | Build 第二日：MAI 自研 + Copilot super app vs OpenAI Codex/Atlas 超级应用 |
| Meta / Agent | [Meta Business Agent globally on WhatsApp（TechCrunch）](https://techcrunch.com/2026/06/03/metas-ai-agent-for-whatsapp-business-is-now-available-globally/) | **2026-06-03** | 产品发布 | WhatsApp/Instagram DM **客服 Agent** 全球可用；token 计费 + Shopify/Zendesk 集成路线 |
| Google / 产品 | [Google Dreambeans lifestyle AI app（TechCrunch）](https://techcrunch.com/2026/06/03/googles-dreambeans-its-weirdest-named-ai-tool-to-date-will-turn-your-life-into-a-cartoon/) | **2026-06-03** | 产品发布 | **Personal Intelligence** 聚合 Gmail/Calendar/Photos 生成限量每日「故事」；AI Ultra 限定 |
| 监管 / 搜索 | [UK publishers opt-out of AI Search（TechCrunch）](https://techcrunch.com/2026/06/03/publishers-will-be-able-to-opt-out-of-ai-search-thanks-to-new-regulation/) | **2026-06-03** | 政策监管 | Google Search Console **toggle** 退出 AI Overviews/AI Mode；CMA 合规 |
| 可靠性 | [OpenAI API, ChatGPT and Codex outage（Community）](https://community.openai.com/t/openai-api-chatgpt-and-codex-currently-down/1382514) | **2026-06-03** | 运维事件 | 当日 **5xx**；官方 **15:16 UTC 左右** 称已修复——Agent 流水线需幂等重试 |
| 论文 | [D2MDT: Department-aware MDT Consultation（arXiv:2606.03543）](https://arxiv.org/html/2606.03543v1) | **2026-06-03** | 论文原文 | 临床预测 **residual deliberation** 多 Agent；降低冗余交互 |
| 论文 | [MeDxAgent + MeDxBench（arXiv:2606.03416）](https://arxiv.org/html/2606.03416v1) | **2026-06-03** | 论文原文 | **交互式诊断** 基准 + 多 Agent 会诊；+10.3pp vs baseline |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| Frontier 治理 | [OpenAI frontier safety blueprint PDF](https://openai.com/index/frontier-safety-blueprint/) | CAISI、州法 harmonization、resilience plan | 合规/平台架构 |
| 伙伴交付 | [Claude Partner Hub + MCP](https://www.anthropic.com/news/services-track-partner-hub) | Select/Preferred/Premier 指标、MCP 查询 tier | SI/企业 AI 负责人 |
| 威胁建模 | [LLM ATT&CK Navigator](https://red.anthropic.com/2026/attack-navigator/) | LLM 攻击面 × ATT&CK 矩阵 | 安全工程/红队 |
| 多 Agent 临床 | D2MDT / MeDxAgent 论文 | residual deliberation、交互式诊断 flow | 医疗 AI 研发 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：6/3 呈现 **「巨头平台化 Agent 入口 + 治理/安全基建同步上架」**——Meta **WhatsApp Business Agent** 与 Google **Dreambeans** 争夺「日常入口」，Anthropic 用 **Partner Hub MCP** 把交付状态机器化；工程侧应把 **outage 重试** 与 **publisher opt-out** 纳入 RAG/搜索 Agent 设计。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 平台 Agent | Meta WhatsApp **Business Agent** GA | 客服/预约/lead 场景可对照 **human handoff** 与 **token 预算** |
| 个人 Agent | Google **Dreambeans**（限量故事） | 「少即是多」UX vs 24/7 Agent；Personal Intelligence 权限最小化 |
| 交付生态 | Anthropic **Partner Hub MCP** | SI 可在 Claude 内查询 tier/deal/cert 状态——可复制到内部 Agent ops |
| 多 Agent 论文 | D2MDT **residual deliberation** | 长时 Agent 会话只传递 **未决共识** 降 token |
| Codex CLI | **0.137.0-alpha.4**（UTC 6/3 凌晨） | alpha 线跟进前先在 staging 验证 MCP/rmcp |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **OpenAI frontier governance blueprint** | 2026 联邦 AI 安全制度设计的一手框架 |
| 必读 | **Anthropic Partner Network + ATT&CK Navigator** | 企业落地分级 + LLM 威胁建模同日发布 |
| 推荐 | **The Verge：Microsoft vs OpenAI** | 理解 Build 周 **双超级应用** 竞争结构 |
| 推荐 | **D2MDT / MeDxAgent 论文** | 多 Agent **deliberation** 与交互式 eval 的可复现参考 |
| 延伸 | **TechCrunch：UK AI Search opt-out** | 影响 RAG/搜索 Agent 的内容授权策略 |

### 来源清单

- 检索范围：2026-06-03 00:00:00 到 2026-06-03 23:59:59（Asia/Shanghai）
- 引用域名：openai.com, anthropic.com, red.anthropic.com, theverge.com, techcrunch.com, community.openai.com, arxiv.org
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 官方发布 | Frontier AI governance blueprint | 2026-06-03 | https://openai.com/index/frontier-safety-blueprint/ |
| 官方发布 | Claude Partner Network Services Track | 2026-06-03 | https://www.anthropic.com/news/services-track-partner-hub |
| 官方发布 | LLM ATT&CK Navigator | 2026-06-03 | https://red.anthropic.com/2026/attack-navigator/ |
| 技术媒体 | Microsoft vs OpenAI at Build | 2026-06-03 | https://www.theverge.com/ai-artificial-intelligence/942242/microsoft-build-ai-agents-openai-competition |
| 技术媒体 | Meta WhatsApp Business Agent | 2026-06-03 | https://techcrunch.com/2026/06/03/metas-ai-agent-for-whatsapp-business-is-now-available-globally/ |
| 技术媒体 | Google Dreambeans | 2026-06-03 | https://techcrunch.com/2026/06/03/googles-dreambeans-its-weirdest-named-ai-tool-to-date-will-turn-your-life-into-a-cartoon/ |
| 技术媒体 | UK AI Search publisher opt-out | 2026-06-03 | https://techcrunch.com/2026/06/03/publishers-will-be-able-to-opt-out-of-ai-search-thanks-to-new-regulation/ |
| 运维 | OpenAI API outage thread | 2026-06-03 | https://community.openai.com/t/openai-api-chatgpt-and-codex-currently-down/1382514 |
| 论文原文 | D2MDT | 2026-06-03 | https://arxiv.org/html/2606.03543v1 |
| 论文原文 | MeDxAgent | 2026-06-03 | https://arxiv.org/html/2606.03416v1 |""",
    "2026-06-02": """## 2026-06-02

### 今日总览

**一句话结论**：`2026-06-02` 是 **「OpenAI Codex 白领化 + Microsoft Build 自研推理/Scout + Trump AI 安全 EO」** 三足鼎立——OpenAI 发布 **Plugins/Sites/Annotations** 并 **下线 ChatGPT 登录下的 GPT-5.2/5.3-Codex**；Microsoft 推出 **MAI-Thinking-1** 与 **Scout（OpenClaw）**；Trump 签署 **自愿 30 天 前沿模型安全审查** 行政令；Anthropic **Glasswing 扩至 ~150 组织** 且 **Claude Code 连发 v2.1.160/161**。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | OpenAI/Anthropic/Microsoft 官方；The Verge/TechCrunch/Bloomberg；GitHub release；政策监管 |
| 核心趋势 | **Codex 从编码工具→知识工作平台**（20% 非开发者、3× 增速）；**Microsoft 自研推理 + OpenClaw Scout**；**网络安全 EO 自愿送审** |
| 可直接关注 | 企业评估 **Codex Sites** 权限与 **6 角色插件**；升级 **Claude Code 2.1.160+** 注意 **`workflow`→`ultracode` breaking**；Copilot/Codex **模型 sunset** 后重算配额 |
| 专项检索结论 | **Claude Code**：**`v2.1.160` `Published: 2026-06-02T02:10:25Z`** + **`v2.1.161` `21:58:22Z`**；**Codex**：**无 6/2 release**（**0.136.0 为 6/1**）；**OpenClaw**：**Scout/NemoClaw/Build MXC** 官方叙事（非 OpenClaw 新 tag）；**Hermes**：无 6/2 release；**Spring AI**：无 6/2 官方 release（最近 **2.0.0-M8 为 5/27**）；**skills**：Codex **6 角色插件 110 skills**；Claude API **advisor max_tokens** |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| OpenAI / Codex | [Codex for every role, tool, and workflow](https://openai.com/index/codex-for-every-role-tool-workflow/) | **2026-06-02** | 官方发布 | **6 角色插件**（销售/数据分析/投行等）+ **Sites** 托管交互应用 + **Annotations** 局部精修 |
| OpenAI / 模型 | [GPT-5.2 & GPT-5.3-Codex sunset in Codex（ChatGPT 登录）](https://community.openai.com/t/gpt-5-2-and-gpt-5-3-codex-have-been-sunset-in-codex-with-chatgpt-subscriptions/1382273) | **2026-06-02 起** | 官方政策 | ChatGPT 账号登录 Codex **不再可用** 5.2/5.3；免费档默认 **GPT-5.5**；API 路径仍可用 |
| Microsoft / Build | [Introducing MAI-Thinking-1](https://microsoft.ai/news/introducing-mai-thinking-1/) | **2026-06-02** | 官方发布 | **35B active MoE**、**256K** 上下文；**53% SWE-Bench Pro**；无蒸馏、商用授权数据 |
| Microsoft / Agent | [Microsoft Scout built on OpenClaw（The Verge Build 汇总）](https://www.theverge.com/tech/941668/microsoft-build-may-2026-live-news-updates) | **2026-06-02** | 产品发布 | **365 常驻 Autopilot**；**Project Solara** Android Agent OS；**MXC** 容器隔离 OpenClaw |
| 政策 / AI 安全 | [Trump signs AI safety order（Ideastream）](https://www.ideastream.org/2026-06-02/trump-signs-ai-safety-order-seeking-voluntary-review-of-new-models) | **2026-06-02** | 政策监管 | **自愿** 提前 ≤30 天提交前沿模型供政府网络安全测试；非强制许可 |
| Anthropic / 安全 | [Expanding Project Glasswing](https://www.anthropic.com/news/expanding-project-glasswing) | **2026-06-02** | 官方发布 | **~150** 新组织、**15+** 国家；电力/水务/医疗等 **Mythos Preview** 漏洞扫描 |
| Anthropic / API | [Claude API release notes — June 2](https://docs.anthropic.com/en/release-notes/api) | **2026-06-02** | 官方文档 | **advisor max_tokens**；**stop_reason=refusal 且无输出不计费** |
| Claude Code | [anthropics/claude-code `v2.1.160`](https://github.com/anthropics/claude-code/releases/tag/v2.1.160) | **`Published: 2026-06-02T02:10:25Z`** | 开源发布 | shell 启动文件写入确认；**`workflow`→`ultracode`**；grep 后可直接 edit |
| Claude Code | [anthropics/claude-code `v2.1.161`](https://github.com/anthropics/claude-code/releases/tag/v2.1.161) | **`Published: 2026-06-02T21:58:22Z`** | 开源发布 | OTEL resource labels；并行 tool/MCP 修复 |
| LangGraph | [langgraph==1.2.4](https://github.com/langchain-ai/langgraph/releases/tag/1.2.4) | **`Published: 2026-06-02T17:07:49Z`** | 开源发布 | `_on_started` 向后兼容；server factory 集成测试 |
| Google / Agent | [Gemini Spark hands-on（The Verge）](https://www.theverge.com/ai-artificial-intelligence/941388/gemini-spark-ai-agent-trip-planning) | **2026-06-02** | 技术媒体 | **24/7 个人 Agent** 实测：Gmail/Docs 任务 + 行程规划；隐私/成本权衡 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| Codex 知识工作 | [Codex plugins/Sites/Annotations 官方文](https://openai.com/index/codex-for-every-role-tool-workflow/) | 62 apps、110 skills、Sites URL 分享 | 非研发知识工作者/管理员 |
| Codex 模型迁移 | [Community: GPT-5.2/5.3 sunset](https://community.openai.com/t/gpt-5-2-and-gpt-5-3-codex-have-been-sunset-in-codex-with-chatgpt-subscriptions/1382273) | ChatGPT 登录 vs API key 路径 | Codex 重度用户 |
| MAI 推理 | [MAI-Thinking-1 model card](https://microsoft.ai/models/mai-thinking-1/) | Foundry 私有预览、AIME/SWE 指标 | 平台/数据科学 |
| Claude Code | [v2.1.160 release notes](https://github.com/anthropics/claude-code/releases/tag/v2.1.160) | ultracode、acceptEdits 安全 | 终端 Agent 用户 |
| Dynamic workflows | [Claude Code workflows docs](https://code.claude.com/docs/en/workflows) | **`ultracode` 触发**、research preview | 多 Agent 编排 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：6/2 是 **「白领 Agent 产品化 + 自研推理模型 + 开源 Agent 运行时双更」** 同日碰撞——OpenAI 把 Codex 推向 **Sites/插件目录**，Microsoft 用 **OpenClaw Scout** 对标 Google **Gemini Spark**，Anthropic 用 **Glasswing + Claude Code 连更** 巩固安全/终端栈。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| Codex 产品 | **Plugins + Sites + Annotations** | 内部工具从「文件输出」→「可分享 URL」；Annotations 降低全量重写 |
| 模型生命周期 | **GPT-5.2/5.3 Codex sunset** | CI 固定 model id；ChatGPT 登录与 API key **两条配额线** |
| Microsoft Agent | **Scout + Solara + MXC** | 企业 OpenClaw 需 **Execution Container** 沙箱策略 |
| Claude Code | **2.1.160/161** | 迁移 **`/effort ultracode`**；OTEL labels 做 **per-team 用量切片** |
| LangGraph | **1.2.4** | 升级前跑 **factory-graph** 集成测试 |
| OpenClaw vs 商业 | **Scout 基于 OpenClaw** | 选型：自托管 OpenClaw vs 365 托管 Scout 的 **数据驻留** |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **OpenAI Codex 6/2 官方发布** | 知识工作者 Agent 栈（插件/Sites/Annotations）一手定义 |
| 必读 | **MAI-Thinking-1 + Build Scout 汇总** | 微软「第四 lab」叙事与 OpenClaw 企业化路径 |
| 推荐 | **Claude Code v2.1.160/161** | 当日可核验 **breaking + 安全** 变更 |
| 推荐 | **Trump AI safety EO 报道** | 自愿送审框架对 frontier 发布节奏的影响 |
| 延伸 | **Gemini Spark 实测** | 对照 Codex Sites / Claude dynamic workflows 的「常驻 Agent」UX |

### 来源清单

- 检索范围：2026-06-02 00:00:00 到 2026-06-02 23:59:59（Asia/Shanghai）
- 引用域名：openai.com, community.openai.com, microsoft.ai, theverge.com, techcrunch.com, anthropic.com, docs.anthropic.com, github.com, ideastream.org
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 官方发布 | Codex for every role | 2026-06-02 | https://openai.com/index/codex-for-every-role-tool-workflow/ |
| 官方政策 | GPT-5.2/5.3 Codex sunset | 2026-06-02 | https://community.openai.com/t/gpt-5-2-and-gpt-5-3-codex-have-been-sunset-in-codex-with-chatgpt-subscriptions/1382273 |
| 官方发布 | MAI-Thinking-1 | 2026-06-02 | https://microsoft.ai/news/introducing-mai-thinking-1/ |
| 技术媒体 | Microsoft Build 汇总 | 2026-06-02 | https://www.theverge.com/tech/941668/microsoft-build-may-2026-live-news-updates |
| 政策监管 | Trump AI safety EO | 2026-06-02 | https://www.ideastream.org/2026-06-02/trump-signs-ai-safety-order-seeking-voluntary-review-of-new-models |
| 官方发布 | Expanding Project Glasswing | 2026-06-02 | https://www.anthropic.com/news/expanding-project-glasswing |
| 官方文档 | Claude API June 2 notes | 2026-06-02 | https://docs.anthropic.com/en/release-notes/api |
| 开源发布 | Claude Code v2.1.160 | 2026-06-02 | https://github.com/anthropics/claude-code/releases/tag/v2.1.160 |
| 开源发布 | Claude Code v2.1.161 | 2026-06-02 | https://github.com/anthropics/claude-code/releases/tag/v2.1.161 |
| 开源发布 | langgraph 1.2.4 | 2026-06-02 | https://github.com/langchain-ai/langgraph/releases/tag/1.2.4 |
| 技术媒体 | Gemini Spark review | 2026-06-02 | https://www.theverge.com/ai-artificial-intelligence/941388/gemini-spark-ai-agent-trip-planning |""",
}

KB_SECTIONS = {
    "2026-06-02": """## 2026-06-02

### 今日总览

**一句话结论**：`2026-06-02` 固定来源口径下，**腾讯云开发者社区** 硬对齐 **LLM 自动修 Bug 31% 天花板** 与 **Hermes Agent 桌面 v0.5.0** 解读；**掘金** 有 **Agent 新闻汇总** 与 **截图→企业级页面双 Skill** 实践；美团/阿里官方 blog、字节 techblog、百度 FEX/EFE 等 **`site:` + 当日硬对齐** 未见可引用首发长文。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 阿里 102 / 阿里云开发者 / 中间件 / 语雀；腾讯云开发者 / AlloyTeam；字节 techblog / 掘金；百度 FEX/EFE/开发者中心；美团 / 京东云 / 凹凸 / 滴滴 / 网易知乎 / 360 / 有赞 |
| 核心趋势 | **Agent 工程边界**：LLM 修 Bug **A 级修复率 ~31%** 难靠流水线突破；**Skills 落地**：截图→UIDL→DevUI 组件库 **双 Skill 串联** |
| 可直接关注 | 阅读腾讯云 **31% 天花板** 文校准 Agent 修 Bug ROI；评估 **Hermes 桌面 v0.5.0** 与 OpenClaw 选型 |
| 未发现更新 | 阿里 102/中间件/语雀、tech.meituan.com、techblog.toutiao.com、腾讯云+（非开发者社区）、京东/滴滴/有赞/360/网易知乎、百度 FEX/EFE、AlloyTeam、Tencent_TEG 公众号：本次未见 6/2 硬对齐首发长文 |

### 重要文章与更新

| 主题 | 标题 | 日期 | 来源 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| Agent / 质量 | [31%：LLM 修 Bug 的真正天花板？](https://cloud.tencent.com/developer/article/2680797) | **2026-06-02 12:02:48** | 腾讯云开发者社区 | 全链路优化后 **A 级修复率仍 ~31%**——Agent 修 Bug 需人机协同而非全自动 |
| Agent 工具 | [Hermes Agent 桌面端 v0.5.0 发布解读](https://cloud.tencent.com/developer/article/2680836) | **2026-06-02 13:17:38** | 腾讯云开发者社区 | **Hermes Slate Desk v0.5.0** UI/功能升级（社区稿，非 Nous 官方首发） |
| Agent 工程（社区） | [AI Agents 新闻日报（2026年6月）](https://juejin.cn/post/7646255632631119912) | **2026-06-02** | 掘金 | SLIM/GodeX/Cosmos3/MiniMax M3 等 **Agent 生态** 汇总（非官方原文） |
| 前端 / Skills | [从截图到企业级前端页面：2 个 Skill](https://juejin.cn/post/7646396172870008847) | **2026-06-02** | 掘金 | **image-analyze + vue-devui-practices** Skill 链：截图→UIDL→DevUI 代码 |

### 技术文档与实践

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| Agent 质量评估 | [腾讯云：LLM 修 Bug 31% 天花板](https://cloud.tencent.com/developer/article/2680797) | 评分机制、Bug 分类、任务调度极限 | Agent 平台/质效负责人 |
| Skills 实践 | [掘金：双 Skill 截图转页面](https://juejin.cn/post/7646396172870008847) | UIDL、Design Token、DevUI 组件约束 | 前端/Agent 编排 |
| Hermes 桌面 | [腾讯云：Hermes v0.5.0](https://cloud.tencent.com/developer/article/2680836) | 桌面端 Agent UX 迭代 | 自托管 Agent 用户 |

### 工程实践归纳

**总体判断**：固定来源当日增量集中在 **「Agent 能力边界量化 + Skills 串联落地」**——31% 天花板说明 **eval 驱动 + 人工复核** 仍是修 Bug Agent 标配；掘金 **双 Skill** 展示国内团队如何把 **设计稿→规范代码** 封装为可复用 Skill。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 修 Bug Agent | **A 级修复率 ~31% 平台期** | 流水线优化无法突破模型固有边界；应设 **human-in-the-loop** |
| Skills 编排 | **截图→UIDL→DevUI** 两 Skill | 复杂 UI 生成宜 **分阶段 Skill** 而非单 prompt |
| 官方 blog 空窗 | 多维度 **6/2 无硬对齐** | 大厂首发常滞后；社区稿须标注 **非官方原文** |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **腾讯云 6/2 LLM 修 Bug 天花板** | 当日固定来源 **硬时间戳** 长文，直接约束 Agent ROI 预期 |
| 推荐 | **掘金双 Skill 前端实践** | 可复制的 **Skill 拆分** 模板 |
| 延伸 | **掘金 Agent 新闻汇总** | 快速对齐 **Cosmos3/M3** 等生态语境（需对照官方） |

### 来源清单

- 检索范围：2026-06-02 00:00:00 到 2026-06-02 23:59:59（Asia/Shanghai）
- 固定来源覆盖：腾讯（腾讯云开发者社区 ✓）；字节（掘金 ✓）；其余维度已检索未见 6/2 硬对齐首发长文
- 来源清单表格：

| 公司/组织 | 来源 | 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- | --- | --- |
| 腾讯 | 腾讯云开发者社区 | 技术文章 | LLM 修 Bug 31% 天花板 | 2026-06-02 | https://cloud.tencent.com/developer/article/2680797 |
| 腾讯 | 腾讯云开发者社区 | 社区解读 | Hermes Agent 桌面 v0.5.0 | 2026-06-02 | https://cloud.tencent.com/developer/article/2680836 |
| 字节跳动 | 掘金 | 社区汇总 | AI Agents 六月新闻 | 2026-06-02 | https://juejin.cn/post/7646255632631119912 |
| 字节跳动 | 掘金 | 实践文章 | 截图到企业级页面双 Skill | 2026-06-02 | https://juejin.cn/post/7646396172870008847 |
| 美团/阿里/京东/滴滴/百度/360/有赞/网易 | 固定来源清单 | 无新增 | 无可靠新增来源 | - | - |""",
    "2026-06-03": """## 2026-06-03

### 今日总览

**一句话结论**：`2026-06-03` 固定来源口径下，**腾讯云开发者社区** 发布 **游戏安全行业峰会报名**（AI 时代游戏安全范式）；**掘金** 有 **ACTS 推理 token 优化**、**Codex 并入 ChatGPT** 等 **社区解读**；美团/阿里官方 blog、字节 techblog、百度 FEX/EFE 等 **`site:` + 当日硬对齐** 未见可引用首发长文。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 阿里 102 / 阿里云开发者 / 中间件 / 语雀；腾讯云开发者 / AlloyTeam；字节 techblog / 掘金；百度 FEX/EFE/开发者中心；美团 / 京东云 / 凹凸 / 滴滴 / 网易知乎 / 360 / 有赞 |
| 核心趋势 | **安全 + Agent**：游戏安全峰会聚焦 **AI 时代攻防**；社区传播 **MDP 控 token 推理（ACTS）** 与 **Codex 超级应用化** 讨论 |
| 可直接关注 | 游戏/安全团队关注 **6 月峰会** 议题；推理密集型 Agent 可评估 **ACTS controller** 模式 |
| 未发现更新 | 阿里 102/中间件/语雀、tech.meituan.com、techblog.toutiao.com、阿里云开发者（6/3 硬对齐）、京东/滴滴/有赞/360/网易知乎、百度 FEX/EFE、AlloyTeam、Tencent_TEG 公众号：本次未见 6/3 硬对齐首发长文 |

### 重要文章与更新

| 主题 | 标题 | 日期 | 来源 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| 安全 / 游戏 | [游戏安全行业峰会报名 — AI 时代游戏安全新范式](https://cloud.tencent.com/developer/article/2681634) | **2026-06-03 12:38:24** | 腾讯云开发者社区 | 云鼎实验室发起 **行业峰会**——AI 辅助攻防与游戏安全治理 |
| Agent 推理（社区） | [ACTS：用 MDP 建模推理过程省 token](https://juejin.cn/post/7647054707223494675) | **2026-06-03** | 掘金 | **controller agent** 驱动冻结 reasoner；**arXiv:2606.03965** 解读（非官方首发） |
| Codex 产品（社区） | [Codex 并入 ChatGPT 深度分析](https://juejin.cn/post/7646704463968747520) | **2026-06-03** | 掘金 | 转述 OpenAI **超级应用** 战略与 **500 万 WAU** 数据（非 OpenAI 官方首发） |
| AI 资讯（社区） | [AI 每日新闻精选 — 2026年6月3日](https://juejin.cn/post/7646542167926456370) | **2026-06-03** | 掘金 | 微信 AI 智能体测试、Qwen3.7-Plus 等 **媒体/社区传播** 汇总 |

### 技术文档与实践

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| 游戏安全 | [腾讯云：游戏安全峰会文](https://cloud.tencent.com/developer/article/2681634) | AI 时代游戏攻防、行业协同 | 游戏安全/后端 |
| Token 效率 | [掘金：ACTS 解读](https://juejin.cn/post/7647054707223494675) | MDP + controller、跨 reasoner 迁移 | Agent 平台研发 |
| 超级应用 | [掘金：Codex×ChatGPT 分析](https://juejin.cn/post/7646704463968747520) | 9 亿 WAU 入口、知识工作者占比 | 产品/架构 |

### 工程实践归纳

**总体判断**：固定来源当日以 **「安全行业活动 + 社区 Agent 方法论传播」** 为主——官方 team blog 仍处空窗，但腾讯云 **硬时间戳** 峰会文与掘金 **ACTS** 笔记对 **Agent 成本治理** 有直接参考值。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| ACTS 模式 | **冻结 reasoner + 外部 controller** | 75% token 预算下准确率损失 <2%——适合 **长推理 Agent** 降本 |
| Codex 战略 | 社区解读 **并入 ChatGPT** | 入口统一后需重新评估 **IDE vs 超级应用** 分工 |
| 官方 blog 空窗 | **6/3 多维度无硬对齐** | 重大发布常 **滞后 1–3 天** 才出现在 team blog |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **腾讯云 6/3 游戏安全峰会文** | 当日固定来源 **唯一硬时间戳长文** |
| 推荐 | **掘金 ACTS 笔记** | 快速理解 **MDP 控推理** 工程模式（建议对照 arXiv 原文） |
| 延伸 | **掘金 Codex 超级应用分析** | 对齐 **OpenAI 6/2–6/3 产品线** 讨论语境 |

### 来源清单

- 检索范围：2026-06-03 00:00:00 到 2026-06-03 23:59:59（Asia/Shanghai）
- 固定来源覆盖：腾讯（腾讯云开发者社区 ✓）；字节（掘金 ✓）；其余维度已检索未见 6/3 硬对齐首发长文
- 来源清单表格：

| 公司/组织 | 来源 | 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- | --- | --- |
| 腾讯 | 腾讯云开发者社区 | 活动/技术传播 | 游戏安全行业峰会 | 2026-06-03 | https://cloud.tencent.com/developer/article/2681634 |
| 字节跳动 | 掘金 | 社区解读 | ACTS 推理 token 优化 | 2026-06-03 | https://juejin.cn/post/7647054707223494675 |
| 字节跳动 | 掘金 | 社区解读 | Codex 并入 ChatGPT | 2026-06-03 | https://juejin.cn/post/7646704463968747520 |
| 字节跳动 | 掘金 | 社区汇总 | AI 每日新闻 6/3 | 2026-06-03 | https://juejin.cn/post/7646542167926456370 |
| 美团/阿里/京东/滴滴/百度/360/有赞/网易 | 固定来源清单 | 无新增 | 无可靠新增来源 | - | - |""",
}


def _split_digest(raw, default_header):
    if not raw or not raw.strip():
        return default_header.strip() + "\n", {}

    first = SECTION_DATE_RE.search(raw)
    if not first:
        return raw.strip() + "\n", {}

    header = raw[: first.start()].strip()
    if not header:
        header = default_header.strip()
    else:
        header = header.strip()

    body = raw[first.start() :]
    matches = list(SECTION_DATE_RE.finditer(body))
    sections = {}
    for i, match in enumerate(matches):
        date_key = match.group(1)
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        sections[date_key] = body[start:end].strip()
    return header + "\n", sections


def merge_sections(digest_path, sections_dict, header_lines):
    os.makedirs(os.path.dirname(digest_path), exist_ok=True)
    default_header = header_lines.strip() + "\n"

    if os.path.isfile(digest_path):
        with open(digest_path, "r", encoding="utf-8") as f:
            raw = f.read()
    else:
        raw = ""

    header, existing = _split_digest(raw, header_lines)
    if not header.strip():
        header = default_header

    for date_key, body in sections_dict.items():
        existing[date_key] = body.strip()

    ordered_dates = sorted(existing.keys(), reverse=True)
    chunks = [header.rstrip(), ""]
    for date_key in ordered_dates:
        chunks.append(existing[date_key])
        chunks.append("")

    out = "\n".join(chunks)
    if not out.endswith("\n"):
        out += "\n"

    with open(digest_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(out)

    return list(sections_dict.keys())


def update_state(state_path, dates_to_add, last_end_date):
    os.makedirs(os.path.dirname(state_path), exist_ok=True)
    state = {}
    if os.path.isfile(state_path):
        with open(state_path, "r", encoding="utf-8") as f:
            state = json.load(f)

    processed = state.get("processed_dates") or []
    if not isinstance(processed, list):
        processed = []

    merged = sorted(set(processed + list(dates_to_add)))
    state["processed_dates"] = merged
    state["last_end_date"] = last_end_date
    prev_sync = state.get("last_sync_ymd") or ""
    if not prev_sync or last_end_date > prev_sync:
        state["last_sync_ymd"] = last_end_date

    with open(state_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
        f.write("\n")


def main():
    merge_sections(AI_DIGEST, AI_SECTIONS, AI_HEADER)
    merge_sections(KB_DIGEST, KB_SECTIONS, KB_HEADER)

    end_date = "2026-06-03"
    update_state(AI_STATE, BATCH_DATES, end_date)
    update_state(KB_STATE, BATCH_DATES, end_date)

    print("AI dates:", ", ".join(BATCH_DATES))
    print("KB dates:", ", ".join(BATCH_DATES))
    print("Updated through", end_date)


if __name__ == "__main__":
    main()

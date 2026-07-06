# AI Daily News Digest

按 Asia/Shanghai 时区增量汇总 AI/人工智能相关每日资讯。

## 2026-07-05

### 今日总览

**一句话结论**：`2026-07-05` 是 **「OpenClaw 7.1-beta.2 平台大版本 + Mechanical Turk 标注平台退场 + GPT-5.6 宽发布窗口临近」**——**OpenClaw 2026.7.1-beta.2**（**Published 2026-07-05T09:10:09Z**）集中交付 **GPT-5.6 / attach / ClawRouter / 原生 App**；**Amazon Mechanical Turk** 宣布 **7/30** 起不再接受新客户；媒体汇总 **GPT-5.6 Sol/Terra/Luna** 政府审查后 **GA 窗口**（**6/26 受限预览** 相邻传播）。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | OpenClaw GitHub release；TechCrunch 7/5；GPT-5.6/Claude Science 相邻传播；专项工具链 |
| 核心趋势 | **自托管 Agent 平台化**：OpenClaw **455 PR** 级 beta 覆盖 **路由/多通道/移动端**；**人类标注供应链收缩**：MTurk **停纳新客** 与 **LLM 自标注** 讽刺闭环；**frontier 发布节奏**：GPT-5.6 **~20 伙伴预览** 后 **mid-July GA** 预期 |
| 可直接关注 | 自托管栈评估 **OpenClaw 7.1-beta.2**（**Node 22/24**）；数据团队规划 **MTurk 替代标注** 管线；跟踪 **GPT-5.6 Terra 2× 定价** 对 Agent 路由的影响 |
| 专项检索结论 | **Claude Code**：无 **7/5** 新 release（最新 **v2.1.201 为 7/3**）；**Codex**：无 **7/5** release；**OpenClaw**：**2026.7.1-beta.2**（**Published 2026-07-05**）；**Hermes**：无 **7/5** release；**Spring AI / Spring Alibaba AI**：无 **7/5** release；**Langfuse**：无 **7/5** release；**LangChain/LangGraph**：无 **7/5** release；**Code Graph**：无 **7/5** release；**skills**：OpenClaw **ClawRouter** 与 Claude Science **60+ skills**（**6/30** 相邻） |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| OpenClaw / 发布 | [openclaw 2026.7.1-beta.2](https://github.com/openclaw/openclaw/releases/tag/v2026.7.1-beta.2) | **2026-07-05** | 开源预发布 | **GPT-5.6**、**openclaw attach**、**ClawRouter**、Telegram **Codex /login**、**on-exit cron**、iOS/Android/macOS 大更新 |
| 数据 / 标注 | [Amazon MTurk stops new customers（TechCrunch）](https://techcrunch.com/2026/07/05/amazon-will-stop-accepting-new-customers-for-mechanical-turk/) | **2026-07-05** | 产业/基建 | **7/30/2026** 起停纳新客；2018 起 **SageMaker 标注** 叙事；**33–46% worker 用 LLM 完成任务**（2023 研究） |
| OpenAI / 模型 | [GPT-5.6 preview & GA window（AIToolsRecap 7/5）](https://aitoolsrecap.com/Blog/ai-news-july-5-2026) | **2026-07-05**（相邻日期/中国时间窗口传播） | 技术媒体 | **Sol 96.7% Terminal-Bench 2.1** 叙事；**Terra 2× 低于 GPT-5.5 成本**；**6/26 政府限制 ~20 伙伴** 后 **mid-July GA** 预期 |
| Anthropic / 垂直 | [Claude Science grant deadline（官方 6/30）](https://www.anthropic.com/news/claude-science-ai-workbench) | **2026-06-30**（**7/5 窗口传播**） | 官方产品 | **AI for Science** 项目申请 **至 7/15**；**$30K credits + Modal $2K** |
| 企业合规 | [Alibaba Claude Code ban（TechCrunch 7/4）](https://techcrunch.com/2026/07/04/alibaba-reportedly-bans-employees-from-using-claude-code/) | **2026-07-04**（**7/5 中国时间窗口传播**） | 产业/合规 | **7/10** 生效；改 **Qoder**；Anthropic **distillation 反滥用** 背景 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| OpenClaw 7.1-beta.2 | **GitHub release notes** | **ClawRouter**、**attach** harness、**Node 22/24** 要求 | 自托管 Gateway 运维 |
| GPT-5.6 接入 | **OpenClaw Chronicles GPT-5.6** | **Sol/Terra/Luna** catalog、Codex OAuth、App Server | 有 preview 权限的团队 |
| 标注供应链 | **TechCrunch MTurk 报道** | 停纳新客时间表、LLM 污染标注数据 | ML 数据工程 |
| Claude Science | **Anthropic 官方 Science 页** | **7/15 申请截止**、BioNeMo skills | 生命科学研发 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：7/5 是 **「OpenClaw 平台 beta 大打包 + 人类标注平台边缘化 + frontier 模型 GA 倒计时」**——工程侧 **OpenClaw 7.1-beta.2** 把 **模型路由、外部 harness、移动端、Cron** 合成一次交付；产业侧 **MTurk** 退场提示 **RLHF/评测数据** 需新供给；**GPT-5.6 Terra** 定价叙事或重塑 **Agent 默认路由**。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| OpenClaw | **2026.7.1-beta.2** | **ClawRouter** 动态模型发现 + 预算报告；**attach** 统一 Codex/Claude harness |
| 多通道 Agent | **Telegram Codex /login**、iMessage polls | 多 IM 通道应统一 **steering + final-reply recovery** |
| Cron | **on-exit** schedule | 用 **进程退出事件** 触发 Agent 比固定 cron 更贴近 CI/批任务 |
| Claude Code | 无 **7/5** release | 维持 **7/3 Manual + v2.1.201** |
| Codex/Hermes/Langfuse | 无 **7/5** release | 无变更 |
| 数据标注 | **MTurk 停纳新客** | 评测/微调 pipeline 需 **LLM-judge + 合成数据** 替代方案 |
| GPT-5.6 | **GA 窗口临近**（媒体 **7/5**） | 预备 **Terra 成本路由** 与 **Sol ultra** 质量档 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **OpenClaw 2026.7.1-beta.2 release** | 当日 **最可核验重大开源 Agent 平台** 更新 |
| 必读 | **TechCrunch：Mechanical Turk 停纳新客** | **AI 标注供应链** 拐点信号 |
| 推荐 | **AIToolsRecap 7/5 GPT-5.6 汇总** | **GA 窗口 + Terra 定价** 竞争对照 |
| 延伸 | **Claude Science 7/15 申请** | 垂直 **workflow+skills** 资助样本 |

### 来源清单

- 检索范围：2026-07-05 00:00:00 到 2026-07-05 23:59:59（Asia/Shanghai）
- 引用域名：github.com, techcrunch.com, aitoolsrecap.com, anthropic.com, openclawchronicles.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 开源发布 | openclaw 2026.7.1-beta.2 | 2026-07-05 | https://github.com/openclaw/openclaw/releases/tag/v2026.7.1-beta.2 |
| 技术媒体 | Amazon MTurk stops new customers | 2026-07-05 | https://techcrunch.com/2026/07/05/amazon-will-stop-accepting-new-customers-for-mechanical-turk/ |
| 技术媒体 | AI News July 5 2026 | 2026-07-05 | https://aitoolsrecap.com/Blog/ai-news-july-5-2026 |
| 官方产品 | Claude Science workbench | 2026-06-30（7/5 传播） | https://www.anthropic.com/news/claude-science-ai-workbench |
| 产业 | Alibaba Claude Code ban | 2026-07-04（相邻） | https://techcrunch.com/2026/07/04/alibaba-reportedly-bans-employees-from-using-claude-code/ |

## 2026-07-04

### 今日总览

**一句话结论**：`2026-07-04` 是 **「Leanstral 1.5 形式化 Agent 全面开源 + 阿里禁用 Claude Code + 版权诉讼倒逼 AI 使用披露」**——Mistral **Leanstral 1.5** 获 **The Decoder/TestingCatalog** 等 **7/4** 深度解读；**阿里巴巴** 据报 **7/10 起** 禁员工使用 **Claude Code** 改推 **Qoder**；**Midjourney** 诉 Hollywood 要求披露 **内部 generative AI** 用法。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | TechCrunch 7/4；Mistral 官方（**7/2** 相邻）；The Decoder/TestingCatalog；专项工具链 |
| 核心趋势 | **形式化 proof agent 产品化**：Lean 4 **587/672 PutnamBench** + **真实 bug** 发现；**地缘/合规工具链**：中国大厂 **Claude Code 退场** 与 Anthropic **distillation 反滥用**；**版权 discovery**：studio **内部 AI 训练/使用** 成诉讼焦点 |
| 可直接关注 | 形式化/安全团队试用 **leanstral-1-5** 免费 API；在华企业评估 **Qoder/国产 Agent** 替代 **Claude Code**；内容/法务关注 **Midjourney discovery** 对 **内部 AI 文档** 的示范效应 |
| 专项检索结论 | **Claude Code**：无 **7/4** 新 GitHub release（最近 **v2.1.201 为 7/3**）；**Codex**：无 **7/4** release；**OpenClaw**：无 **7/4** release；**Hermes**：无 **7/4** release；**Spring AI / Spring Alibaba AI**：无 **7/4** release；**Langfuse / LangChain / Code Graph**：无 **7/4** release（Code Graph **Medium 7/4** 相邻解读）；**skills**：Leanstral **proof agent** 与 Midjourney **prompt/output 披露** 争点 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| Mistral / 形式化 | [Leanstral 1.5: Proof Abundance（官方）](https://mistral.ai/news/leanstral-1-5/) | **2026-07-02**（**7/4** 媒体续传） | 官方发布 | **Apache-2.0**；**labs-leanstral-1-5** 免费 API；**119B/6B active**；**57 仓库扫出 5 bug** |
| Mistral / 形式化 | [Leanstral 1.5（The Decoder）](https://the-decoder.com/mistrals-open-source-leanstral-1-5-aces-formal-math-benchmarks-and-catches-real-bugs-in-code/) | **2026-07-04** | 技术媒体 | **miniF2F 100%**；**FATE-H 87% / FATE-X 34%**；Rust **varinteger** overflow 案例 |
| Mistral / 形式化 | [Leanstral 1.5 open model（TestingCatalog）](https://www.testingcatalog.com/mistral-releases-leanstral-1-5-open-model-for-proof-engineering/) | **2026-07-04** | 技术媒体 | **256k context**；Labs **2026-09-30 退役** 时间表；替换 **leanstral-2603** |
| 企业合规 | [Alibaba bans Claude Code（TechCrunch）](https://techcrunch.com/2026/07/04/alibaba-reportedly-bans-employees-from-using-claude-code/) | **2026-07-04** | 产业/合规 | **7/10** 起禁 **Claude Code**；改 **Qoder**；Anthropic **distillation/reseller** 反滥用背景 |
| 版权 / 诉讼 | [Midjourney vs Hollywood AI disclosure（TechCrunch）](https://techcrunch.com/2026/07/04/midjourney-wants-hollywood-studios-to-reveal-the-details-of-their-ai-usage/) | **2026-07-04** | 政策/法律 | 要求披露 **内部 storyboard/ideation AI** 与 **全部 prompts/outputs** |
| Code Graph | [Inside CodeGraph（Medium）](https://ai.plainenglish.io/inside-codegraph-how-ai-coding-agents-understand-million-line-codebases-without-reading-every-file-66b069215c00) | **2026-07-04**（相邻日期/中国时间窗口传播） | 技术媒体 | 本地 **knowledge graph** 降 token；支持 **Claude Code/Cursor/Hermes** 等 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| Lean 4 Agent | **Mistral Leanstral 1.5 官方 + TestingCatalog** | **Mistral Vibe**、`/leanstral`、Lean LSP MCP | 形式化/证明工程师 |
| 企业工具链 | **TechCrunch 阿里 Claude Code 禁令** | **Qoder** 替代、跨境 **OAuth/distillation** 风险 | 在华研发管理 |
| 版权 discovery | **Midjourney 诉讼报道** | **consumer-facing vs internal AI** 证据边界 | 法务/内容团队 |
| Code Graph | **Inside CodeGraph 文** | 预索引图谱 vs 每 session 重发现 | 大仓 Agent 架构 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：7/4 主线是 **「形式化 Agent 开源可达 + 跨境 Coding Agent 合规收紧 + 生成式 AI 使用透明化诉讼」**——Leanstral 把 **proof engineering** 拉到免费 API；阿里案例说明 **frontier 工具 + 地缘合规** 已进入 **IT 采购清单**；Midjourney 争 **internal AI** 披露，影响 **训练数据/工具链审计** 标准。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 形式化 Agent | **Leanstral 1.5** 7/4 媒体深读 | **Lean 4 + code agent env** 可接 **SafeVerify** 流水线 |
| 跨境合规 | **阿里禁 Claude Code** | 企业需 **approved tool list** + **国产 Agent IDE** 双轨 |
| 版权诉讼 | **Midjourney discovery 扩面** | 内部 **storyboard AI** 亦可能构成 **industry custom** 证据 |
| Claude Code | 无 **7/4** release | 维持 **7/3 Manual** 升级节奏 |
| Codex/OpenClaw/Hermes | 无 **7/4** release | 无变更 |
| Langfuse/LangChain/Spring | 无 **7/4** release | 跟踪 **7/3 Langfuse v3.205.0** 即可 |
| Code Graph | **Medium 7/4 解读** | 多 Agent 共用 **repo-local index** 仍是降本主线 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **Leanstral 1.5 官方 + The Decoder 7/4** | 当日 **形式化 Agent** 最完整叙事 |
| 必读 | **TechCrunch：阿里 Claude Code 禁令** | **7/10 deadline** 的企业工具链样本 |
| 推荐 | **Midjourney Hollywood discovery** | **internal vs consumer AI** 法律边界 |
| 延伸 | **Inside CodeGraph** | 大仓 Agent **context layer** 工程对照 |

### 来源清单

- 检索范围：2026-07-04 00:00:00 到 2026-07-04 23:59:59（Asia/Shanghai）
- 引用域名：mistral.ai, the-decoder.com, testingcatalog.com, techcrunch.com, ai.plainenglish.io
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 官方发布 | Leanstral 1.5 | 2026-07-02（7/4 续传） | https://mistral.ai/news/leanstral-1-5/ |
| 技术媒体 | Leanstral 1.5 The Decoder | 2026-07-04 | https://the-decoder.com/mistrals-open-source-leanstral-1-5-aces-formal-math-benchmarks-and-catches-real-bugs-in-code/ |
| 技术媒体 | Leanstral 1.5 TestingCatalog | 2026-07-04 | https://www.testingcatalog.com/mistral-releases-leanstral-1-5-open-model-for-proof-engineering/ |
| 产业 | Alibaba bans Claude Code | 2026-07-04 | https://techcrunch.com/2026/07/04/alibaba-reportedly-bans-employees-from-using-claude-code/ |
| 法律 | Midjourney Hollywood AI usage | 2026-07-04 | https://techcrunch.com/2026/07/04/midjourney-wants-hollywood-studios-to-reveal-the-details-of-their-ai-usage/ |
| 技术媒体 | Inside CodeGraph | 2026-07-04（相邻） | https://ai.plainenglish.io/inside-codegraph-how-ai-coding-agents-understand-million-line-codebases-without-reading-every-file-66b069215c00 |

## 2026-07-03

### 今日总览

**一句话结论**：`2026-07-03` 是 **「Claude Code Manual 权限语义 + Langfuse v4 会话 UI + 机器人/Agent 技能库 ASPIRE + 35B Agents-A1 开源活跃」**——**Claude Code v2.1.200/201** 连更；**Langfuse v3.205.0** 强化 trace 图与会话视图；**NVIDIA ASPIRE** 机器人技能库论文传播；**上海 AI Lab Agents-A1** 仓库持续更新；**Mistral Leanstral 1.5** 媒体续传（官方 **7/2**）。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | GitHub release；NVIDIA/Mistral/上海 AI Lab；MarkTechPost/TechCrunch；专项工具链 |
| 核心趋势 | **Coding Agent 体验细化**：CC **default→Manual**、对话框不再自动继续；**LLMOps UI 迭代**：Langfuse **v4 sessions** + **widget MCP**；**Agent 技能复利**：ASPIRE **31% zero-shot** 长任务；**Horizon scaling**：35B **Agents-A1** 对标万亿级 Agent 表现 |
| 可直接关注 | 升级 **Claude Code ≥2.1.200** 并检查 **permission mode** 配置；评估 **Langfuse v3.205.0** trace 图与 **Parquet export**；机器人/具身团队跟踪 **ASPIRE** 开源计划 |
| 专项检索结论 | **Claude Code**：**v2.1.200**（**Published 2026-07-03T16:52:33Z**）+ **v2.1.201**（**23:50:35Z**）；**Codex**：**0.143.0-alpha.35**（**Published 2026-07-03T02:33:31Z**）；**OpenClaw**：无 **7/3** 新 release（**2026.7.1-beta.1 为 7/2**）；**Hermes**：无 **7/3** release；**Spring AI / Spring Alibaba AI**：无 **7/3** release；**Langfuse**：**v3.205.0**（**Published 2026-07-03T17:20:56Z**）；**LangChain/LangGraph**：无 **7/3** release；**Code Graph**：无 **7/3** release（社区解读 **7/3~7/4** 相邻传播）；**skills**：ASPIRE **机器人 skill library** 论文主线 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| Claude Code | [Claude Code v2.1.200](https://github.com/anthropics/claude-code/releases/tag/v2.1.200) | **2026-07-03** | 开源发布 | **default→Manual** 权限模式；**AskUserQuestion** 不再自动继续；background session/daemon 多项修复 |
| Claude Code | [Claude Code v2.1.201](https://github.com/anthropics/claude-code/releases/tag/v2.1.201) | **2026-07-03** | 开源发布 | **Sonnet 5** 会话移除 mid-conversation **harness reminders** system role |
| Codex | [Codex 0.143.0-alpha.35](https://github.com/openai/codex/releases/tag/rust-v0.143.0-alpha.35) | **2026-07-03** | 开源预发布 | alpha 线常规迭代 |
| Langfuse | [Langfuse v3.205.0](https://github.com/langfuse/langfuse/releases/tag/v3.205.0) | **2026-07-03** | 开源发布 | **v4 sessions View**、filter sidebar rail、**widget MCP/API**、trace graph 抛光、**Parquet export** |
| NVIDIA / 具身 | [ASPIRE: Agentic Skills Discovery for Robotics（NVIDIA GEAR）](https://research.nvidia.com/labs/gear/aspire/) | **2026-06-29~07-03**（相邻日期/中国时间窗口传播） | 论文/研究 | **skill library** 持续学习；**LIBERO-Pro Long 31% zero-shot**；handover **20%→92%** |
| 论文 | [ASPIRE arXiv:2607.00272](https://arxiv.org/html/2607.00272v1) | **2026-07-03**（MarkTechPost 报道） | 论文原文 | 多机构 **code-as-policy** 机器人 Agent；**CaP-Agent0** 对照 |
| 开源 Agent 模型 | [InternScience/Agents-A1（GitHub）](https://github.com/InternScience/Agents-A1) | **2026-06-26~07-03**（仓库 **Last push 2026-07-03**） | 开源发布 | **35B MoE**；**45K token** 平均轨迹；**六域 multi-teacher OPD** |
| Mistral / 形式化 | [Leanstral 1.5（Mistral 官方）](https://mistral.ai/news/leanstral-1-5/) | **2026-07-02**（相邻日期/中国时间窗口传播） | 官方发布 | **587/672 PutnamBench**；**Apache-2.0**；**119B MoE / 6B active** |
| Mistral / 形式化 | [Leanstral 1.5（MarkTechPost）](https://www.marktechpost.com/2026/07/03/mistral-ai-releases-leanstral-1-5-an-apache-2-0-lean-4-code-agent-model-solving-587-of-672-putnambench-problems/) | **2026-07-03** | 技术媒体 | **miniF2F 100%**；**5 个真实仓库 bug** 发现叙事 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| Claude Code 权限 | **v2.1.200 release** | **Manual** 模式、`/config` idle timeout | 终端 Agent 日常用户 |
| Langfuse 会话 | **v3.205.0 release** | v4 sessions、widget MCP、metadata 搜索建议 | LLMOps/Agent 运维 |
| 机器人 Agent | **ASPIRE 论文 + NVIDIA 页** | multimodal traces、skill distillation | 具身/机器人研发 |
| 长程 Agent 模型 | **Agents-A1 技术报告** | horizon scaling、domain-routed OPD | Agent 训练/评测 |
| 形式化证明 | **Leanstral 1.5 官方文** | Lean 4 agent、CISPO RL、code verification | 形式化/安全关键代码 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：7/3 呈现 **「终端 Agent 权限语义清晰化 + 观测平台 UI/MCP 加厚 + 机器人/数学 Agent 技能复利」**——Claude Code 把 **Manual** 命名落地；Langfuse 向 **v4 会话与 widget** 演进；ASPIRE 与 Leanstral 分别代表 **物理世界 skill library** 与 **形式化 proof agent** 两条 Agent 深化路径。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| Claude Code | **v2.1.200 Manual + 对话框 hold** | 人机协同 Agent 应 **显式等待用户**；background session 需 **daemon 版本时间戳** 防回滚劫持 |
| Langfuse | **v3.205.0** sessions/graph/widget | 观测栈从 trace 列表 → **会话级 View + MCP widget 创建** |
| Codex | **0.143.0-alpha.35** | alpha 跟进前在 staging 验证 |
| ASPIRE | **机器人 skill library** | **validated fix → reusable skill** 模式可映射到软件 Agent **playbook** |
| Agents-A1 | **35B horizon scaling** | 长轨迹 **45K tokens** 训练 infra 比纯参数量更关键 |
| Leanstral | **Lean 4 proof agent** | 形式化验证 Agent 可 **catch real bugs**（varinteger overflow 等） |
| OpenClaw | 无 **7/3** tag | 继续跟踪 **7.1-beta.1** attach/Telegram Codex |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **Claude Code v2.1.200** | **Manual 权限 + 对话框行为** 当日最可核验 CC 变更 |
| 必读 | **Langfuse v3.205.0** | **v4 sessions + widget MCP** 工程信号 |
| 推荐 | **ASPIRE 论文** | **skill library + zero-shot 31%** 具身 Agent 样本 |
| 推荐 | **Agents-A1 GitHub/报告** | **35B vs 万亿参数** horizon scaling 一手材料 |
| 延伸 | **Leanstral 1.5** | 形式化 **proof engineering** 开源标杆 |

### 来源清单

- 检索范围：2026-07-03 00:00:00 到 2026-07-03 23:59:59（Asia/Shanghai）
- 引用域名：github.com, research.nvidia.com, arxiv.org, mistral.ai, marktechpost.com, internscience.github.io
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 开源发布 | Claude Code v2.1.200 | 2026-07-03 | https://github.com/anthropics/claude-code/releases/tag/v2.1.200 |
| 开源发布 | Claude Code v2.1.201 | 2026-07-03 | https://github.com/anthropics/claude-code/releases/tag/v2.1.201 |
| 开源发布 | Codex 0.143.0-alpha.35 | 2026-07-03 | https://github.com/openai/codex/releases/tag/rust-v0.143.0-alpha.35 |
| 开源发布 | Langfuse v3.205.0 | 2026-07-03 | https://github.com/langfuse/langfuse/releases/tag/v3.205.0 |
| 论文原文 | ASPIRE arXiv | 2026-07-03（报道） | https://arxiv.org/html/2607.00272v1 |
| 官方研究 | NVIDIA ASPIRE | 2026-06-29~07-03（相邻） | https://research.nvidia.com/labs/gear/aspire/ |
| 开源发布 | Agents-A1 | 2026-07-03（push） | https://github.com/InternScience/Agents-A1 |
| 官方发布 | Leanstral 1.5 | 2026-07-02（相邻） | https://mistral.ai/news/leanstral-1-5/ |
| 技术媒体 | Leanstral 1.5 MarkTechPost | 2026-07-03 | https://www.marktechpost.com/2026/07/03/mistral-ai-releases-leanstral-1-5-an-apache-2-0-lean-4-code-agent-model-solving-587-of-672-putnambench-problems/ |

## 2026-07-02

### 今日总览

**一句话结论**：`2026-07-02` 是 **「企业 AI 部署军备竞赛 + 芯片/基建叙事 + 平台侧冷静信号」**——Microsoft 宣布 **Frontier Company（$2.5B + 6000 人）** 对标 AWS/OpenAI/Anthropic FDE；Anthropic 与 **Samsung** 洽谈自研芯片；**Langfuse v3.203.2** 与 **OpenClaw 2026.7.1-beta.1** 同日发布；Meta 内部称 **Agent 进展慢于预期**。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | TechCrunch 7/2 产业线；GitHub release；政策/监管相邻传播；专项工具链 |
| 核心趋势 | **FDE/部署组织常态化**：云厂与模型厂竞相组建「驻场工程军团」；**定制芯片** 成为算力自主叙事；**Agent 落地** 出现「资本开支↑、产品体感未兑现」张力 |
| 可直接关注 | 评估 **Microsoft Frontier Company** 与既有 Azure/OpenAI 栈的交付边界；Java/Agent 栈跟踪 **Langfuse agent skills**；自托管 Agent 试用 **OpenClaw 7.1-beta**（GPT-5.6、`openclaw attach`） |
| 专项检索结论 | **Claude Code**：无 **7/2** 新 GitHub release；**Dynamic Workflows** 官方 GA 为 **5/28**，**7/2 技术媒体**续传 **Pro 档可 `/config` 开启**；**Codex**：无 **7/2** release；**OpenClaw**：**2026.7.1-beta.1**（**Published 2026-07-02**）— **GPT-5.6**、`attach` 外部 harness、Telegram Codex；**Hermes**：无 **7/2** release；**Spring AI / Spring Alibaba AI**：无 **7/2** release；**Langfuse**：**v3.203.2**（**Published 2026-07-02T15:35:24Z**）— **Langfuse skills**、assistant 自动重命名；**LangChain/LangGraph**：无 **7/2** release（**1.2.7** 为 **6/30** 相邻）；**Code Graph**：无 **7/2** release；**skills**：Langfuse **agent skills** 功能入库 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| Microsoft / 企业落地 | [Microsoft Frontier Company（$2.5B）](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/) | **2026-07-02** | 产业/组织 | **6000 专家** 驻场交付企业 AI；对标 **AWS $1B FDE**、OpenAI/Anthropic 合资部署实体 |
| Anthropic / 基础设施 | [Anthropic × Samsung 定制芯片洽谈（TechCrunch）](https://techcrunch.com/2026/07/02/anthropic-is-discussing-a-new-custom-chip-with-samsung/) | **2026-07-02** | 产业/基建 | 多元化算力栈叙事；与 OpenAI×Broadcom **Jalapeño** 对照 |
| Meta / Agent | [Zuckerberg：Agent 进展慢于预期（TechCrunch）](https://techcrunch.com/2026/07/02/mark-zuckerberg-tells-staff-that-ai-agents-havent-progressed-as-quickly-as-hed-hoped/) | **2026-07-02** | 产业/组织 | **$145B** AI 基建 vs **Agent Transformation** 未兑现；裁员/重组余波 |
| Meta / 产品 | [Meta Pocket vibe-coded 游戏 App（TechCrunch）](https://techcrunch.com/2026/07/02/meta-quietly-launches-vibe-coded-gaming-app-pocket/) | **2026-07-02** | 产品 | **Gizmo 收购** 团队产物；prompt 生成交互 **gizmos** feed（**6/29** 上架，**7/2** 报道） |
| 可持续 / 基建 | [Google/Amazon 可持续报告：AI 碳排预警（TechCrunch）](https://techcrunch.com/2026/07/02/a-warning-sign-about-ais-real-cost-courtesy-of-google-and-amazon/) | **2026-07-02** | 政策/ESG | Google 排放 **+25% YoY**、Amazon **+16%**；**net-zero** 与 AI 扩张张力 |
| Langfuse / 发布 | [Langfuse v3.203.2](https://github.com/langfuse/langfuse/releases/tag/v3.203.2) | **2026-07-02** | 开源发布 | **Langfuse agent skills**、对话自动重命名、trace UI/MCP 文档修复 |
| OpenClaw / 发布 | [openclaw 2026.7.1-beta.1](https://github.com/openclaw/openclaw/releases/tag/v2026.7.1-beta.1) | **2026-07-02** | 开源预发布 | **GPT-5.6** 模型族、`openclaw attach`、Telegram **Codex** 配对/steering、**on-exit cron** |
| Claude Code / 产品 | [Dynamic Workflows Pro 扩面（TechTimes）](http://www.techtimes.com/articles/319532/20260702/claude-code-dynamic-workflows-go-ga-pro-users-can-now-spawn-1000-parallel-agents.htm) | **2026-07-02** | 技术媒体 | **Pro** 可通过 `/config` 开启；官方 GA 见 **5/28** Anthropic 博文 |
| 政策 / 监管 | [出口管制 × frontier 发布（相邻传播）](https://www.techcrunch.com/2026/07/01/neocloud-together-ai-raises-800m-leaps-to-8-3b-valuation/) | **2026-06-26~07-02**（相邻日期/中国时间窗口传播） | 政策监管 | **GPT-5.6** 仍限 **~20 伙伴**；**Fable 5** 已 **7/1** 全球恢复 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| 企业部署 | **Microsoft Frontier Company 公告** | FDE vs 传统 SI；Fortune 500 既有工程师基础 | 企业 AI 交付负责人 |
| Claude Code Workflows | [Dynamic workflows 官方文档](https://code.claude.com/docs/en/workflows) | `/config`、`ultracode`、`/workflows`；**v2.1.154+** | 多 Agent 编排研发 |
| Langfuse Agent | **v3.203.2 release** | **agent skills**、MCP trace 拉取文档、v4 trace UI | LLMOps/Agent 运维 |
| OpenClaw | **2026.7.1-beta.1 release notes** | `openclaw attach`、GPT-5.6 catalog、Telegram Codex | 自托管 Gateway 用户 |
| 定制芯片 | **Anthropic×Samsung 报道** | 推理/训练芯片分工；与 **TPU/GPU** 多云策略 | 基础设施架构 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：7/2 呈现 **「部署军团 + 可观测性/agent skills 工具链 + 自托管 Agent 追新模型」**——产业侧重金买交付能力，工程侧 **Langfuse/OpenClaw** 继续把 **trace、MCP、多通道 Agent** 做厚；Meta 一线反馈提醒 **Agent ROI** 仍难兑现。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 企业 FDE | **Microsoft $2.5B Frontier Company** | 大客 AI 项目将标配 **驻场工程 + 成果对赌**；内部团队需准备 **可观测/合规** 交付包 |
| Langfuse | **v3.203.2** agent skills + MCP 文档 | 观测平台开始吸收 **Skills** 语义；与 Claude/Cursor skills 生态对齐 |
| OpenClaw | **7.1-beta.1** GPT-5.6 + attach + Telegram Codex | 自托管栈需 **快速跟进 frontier 模型 catalog**；多通道应统一 **harness 附加** 模式 |
| Claude Code | **Dynamic Workflows** Pro 扩面（媒体 **7/2**） | **千级 subagent** 编排适合审计/迁移；注意 **token 账单** 与 **ultracode** 误触 |
| Code Graph / Spring Alibaba | 无 **7/2** 信号 | 继续跟踪 **CodeGraph npm** 与 **java2ai** 文档 |
| Agent 预期管理 | **Meta town hall** 降温 | 企业应设 **Agent 里程碑** 与 **人力替代** 解耦 KPI |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **Microsoft Frontier Company** | 2026 **云厂 FDE 军备** 的标杆动作 |
| 必读 | **Langfuse v3.203.2** | **agent skills** 进入观测平台的主线信号 |
| 推荐 | **OpenClaw 2026.7.1-beta.1** | **GPT-5.6 + attach + Telegram Codex** 三合一 beta |
| 推荐 | **Meta Agent 进展慢于预期** | **高 capex / 低 Agent 体感** 的产业对照 |
| 延伸 | **Google/Amazon 可持续报告解读** | AI 数据中心 **碳排** 将进入采购/合规 checklist |

### 来源清单

- 检索范围：2026-07-02 00:00:00 到 2026-07-02 23:59:59（Asia/Shanghai）
- 引用域名：techcrunch.com, github.com, code.claude.com, techtimes.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 技术媒体 | Microsoft Frontier Company | 2026-07-02 | https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/ |
| 技术媒体 | Anthropic Samsung chip talks | 2026-07-02 | https://techcrunch.com/2026/07/02/anthropic-is-discussing-a-new-custom-chip-with-samsung/ |
| 技术媒体 | Zuckerberg on AI agents | 2026-07-02 | https://techcrunch.com/2026/07/02/mark-zuckerberg-tells-staff-that-ai-agents-havent-progressed-as-quickly-as-hed-hoped/ |
| 技术媒体 | Meta Pocket app | 2026-07-02 | https://techcrunch.com/2026/07/02/meta-quietly-launches-vibe-coded-gaming-app-pocket/ |
| 技术媒体 | Google Amazon sustainability | 2026-07-02 | https://techcrunch.com/2026/07/02/a-warning-sign-about-ais-real-cost-courtesy-of-google-and-amazon/ |
| 开源发布 | Langfuse v3.203.2 | 2026-07-02 | https://github.com/langfuse/langfuse/releases/tag/v3.203.2 |
| 开源发布 | openclaw 2026.7.1-beta.1 | 2026-07-02 | https://github.com/openclaw/openclaw/releases/tag/v2026.7.1-beta.1 |
| 技术媒体 | Claude Code Dynamic Workflows Pro | 2026-07-02 | http://www.techtimes.com/articles/319532/20260702/claude-code-dynamic-workflows-go-ga-pro-users-can-now-spawn-1000-parallel-agents.htm |
| 官方文档 | Claude Code workflows | 参考文档 | https://code.claude.com/docs/en/workflows |

## 2026-07-01

### 今日总览

**一句话结论**：`2026-07-01` 是 **「Fable 5 全球重上线 + 桌面 Agent 平台战 + LLM 可观测性/MCP 工程栈同日加码」**——Anthropic **全球恢复 Claude Fable 5**；Google **Gemini Spark 登陆 macOS**；**Claude Code v2.1.198** 与 **Hermes v0.18.0** 发布；**Langfuse v3.203.0** 带来 **MCP 可变写 + HITL** 与 trace UI 修复。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | Anthropic/OpenAI/Google 官方与文档；TechCrunch/The Verge；GitHub release；Langfuse/LangChain/Code Graph/Spring Alibaba AI 专项 |
| 核心趋势 | **监管与发布耦合**：Fable 5 **6/12 出口管制 → 7/1 全球重部署**；**桌面 Agent** 争夺（Spark vs Claude Desktop）；**Agent 可观测性 MCP 化**（Langfuse **7/1 release**） |
| 可直接关注 | 评估 **Fable 5 至 7/7** **50% 周配额**；Mac **Ultra** 试用 **Spark + custom MCP**；Java/Spring 栈评估 **Langfuse OTel + Spring AI Alibaba Graph 观测** 组合 |
| 专项检索结论 | **Claude Code**：**v2.1.198**（**Published 2026-07-01T20:45:36Z**）；**Codex**：无 7/1 新 release；**OpenClaw**：**v2026.6.11**（**2026-06-30**）；**Hermes**：**v0.18.0**（**2026-07-01**）；**Spring AI**：无 7/1 release；**Spring Alibaba AI**：无 7/1 release（最近 **v1.1.2.2** 为 **2026-03-10**）；**Langfuse**：**v3.203.0**（**Published 2026-07-01T12:35:41Z**）— MCP **mutating + HITL**、observations **metadata 过滤**；**LangChain/LangGraph**：**langgraph 1.2.7**（**2026-06-30**，相邻日期）— `DeltaChannel`/JSON roundtrip 修复；**Code Graph**：**@colbymchenry/codegraph v1.1.6**（**2026-06-30**，相邻日期）— npm **1.0 GA** 后 **`codegraph_explore` 单工具 MCP**；**skills**：Claude Code **`/dataviz`** |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| Anthropic / 模型 | [Redeploying Claude Fable 5（全球恢复）](https://www.anthropic.com/news/redeploying-fable-5) | **2026-07-01** | 官方发布 | **6/12 出口管制** 后 **Fable 5** 重登 Claude.ai/Code/Cowork；**7/7 前** Pro/Max/Team 含 **50% 周配额** |
| Anthropic / 模型 | [Introducing Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5) | **2026-06-30**（相邻日期/中国时间窗口传播） | 官方发布 | **1M context**、**adaptive thinking** 默认；Intro 价 **$2/$10** 至 **8/31** |
| Google / Agent | [Gemini Spark updates（macOS Beta）](https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-june-2026/) | **2026-07-01** | 官方产品 | 桌面 **PDF 整理**、Workspace 联动；**Tasks/Keep** 与 **Canva/Dropbox** 等 connected apps |
| Google / Agent | [Gemini Spark now on Mac（TechCrunch）](https://techcrunch.com/2026/07/01/gemini-spark-googles-agentic-assistant-is-now-available-on-mac/) | **2026-07-01** | 产品发布 | **Gemini 桌面 App** 集成 Spark；**custom MCP**；限 **US Ultra** beta |
| OpenAI / 模型 | [Previewing GPT-5.6 Sol/Terra/Luna](https://openai.com/index/previewing-gpt-5-6-sol/) | **2026-06-26**（相邻日期/中国时间窗口传播） | 官方发布 | **7/1 仍限 ~20 trusted partners** |
| 基础设施 | [Together AI $800M Series C（TechCrunch）](https://techcrunch.com/2026/07/01/neocloud-together-ai-raises-800m-leaps-to-8-3b-valuation/) | **2026-07-01** | 融资/基建 | Neocloud **$8.3B** 估值 |
| 监管 / 地缘 | [Claude Fable 5 back online（The Verge）](https://www.theverge.com/ai-artificial-intelligence/958964/anthropic-claude-fable-5-is-back) | **2026-07-01** | 政策监管 | **jailbreak 严重度框架** 与 **Glasswing** 伙伴协作 |
| Claude Code / 发布 | [Claude Code v2.1.198](https://github.com/anthropics/claude-code/releases/tag/v2.1.198) | **2026-07-01** | 开源发布 | **Claude in Chrome GA**；后台 Agent **draft PR**；**`/dataviz` skill** |
| Hermes / 发布 | [Hermes Agent v0.18.0](https://github.com/NousResearch/hermes-agent/releases) | **2026-07-01** | 开源发布 | **The Judgment Release**：P0/P1 清零；**MoA ensembles**、**Vertex Gemini** 一等 provider |
| Langfuse / 发布 | [Langfuse v3.203.0](https://github.com/langfuse/langfuse/releases/tag/v3.203.0) | **2026-07-01** | 开源发布 | **Mutating MCP + HITL**；MCP **observations metadata 过滤**；trace **dedupe** 与 **GPT-5.5** 模型价 |
| LangChain / 发布 | [langgraph 1.2.7](https://github.com/langchain-ai/langgraph/releases/tag/1.2.7) | **2026-06-30**（相邻日期/中国时间窗口传播） | 开源发布 | **`DeltaChannel` 快照**、**Overwrite JSON roundtrip** 修复 |
| Code Graph / 发布 | [@colbymchenry/codegraph v1.1.6](https://www.npmjs.com/package/@colbymchenry/codegraph) | **2026-06-30**（相邻日期/中国时间窗口传播） | 开源发布 | **1.0 GA** 后 npm 稳定线；**`codegraph_explore` 单工具 MCP** 面向 Claude Code/Cursor/Hermes |
| 运维 / OpenAI | [Subscription plan switch account bans（Community）](https://community.openai.com/t/switching-subscription-plans-can-lead-to-account-bans/1385430) | **2026-07-01** | 运维/治理 | **Pro 升降级** 误封申诉线程 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| Fable 5 重部署 | [Anthropic redeploying Fable 5](https://www.anthropic.com/news/redeploying-fable-5) | 出口管制时间线、**Glasswing/Mythos** 分层、**jailbreak 严重度框架** | 合规/平台架构 |
| Langfuse OTel | [Integrating Langfuse with Spring AI](https://langfuse.com/integrations/frameworks/spring-ai) | **OTLP `/api/public/otel`**、Basic Auth、**prompt/completion 采集 Filter** | Java/Spring AI 可观测性 |
| Langfuse MCP | [Langfuse MCP changelog（5/29）](https://langfuse.com/changelog/2026-05-29-mcp-update) | **Observations/Metrics/Scores** 进 MCP；与 **7/1 mutating MCP** 组合 | Agent 运维/调试 |
| Spring Alibaba Graph | [java2ai Graph quick-start](https://java2ai.com/docs/frameworks/graph-core/quick-start) | **StateGraph**、条件路由、**Human-in-the-Loop** | Java Agent 工作流 |
| Code Graph | [colbymchenry/codegraph README](https://github.com/colbymchenry/codegraph) | **tree-sitter + SQLite FTS5**、**impact analysis**、本地 MCP | AI 编程 Agent 集成 |
| Claude Code | [v2.1.198 release notes](https://github.com/anthropics/claude-code/releases/tag/v2.1.198) | 后台 Agent **draft PR**、**anthropicAws** gateway | 终端 Agent 用户 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：7/1 呈现 **「最强模型恢复上线 + 桌面 Agent 入口 + 可观测性/MCP 工程栈同日发布」** 三线并进——Langfuse **v3.203.0** 把 **Agent 调试/评分/HITL** 进一步 MCP 化；CodeGraph **v1.1.6** 与 Spark **custom MCP** 共同强化 **「Agent 上下文 ≠ 裸 grep」** 的产品共识。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| Langfuse 可观测性 | **v3.203.0**：**mutating MCP + HITL**、metadata 过滤、trace dedupe | 生产 Agent 应 **OTel → Langfuse** 统一 trace，MCP 只读/可写分 **allow-list** |
| LangGraph | **1.2.7** 修复 **DeltaChannel/Overwrite** | 长线程 checkpoint 场景优先升级；关注 **v3 stream abort** 子图取消（1.2.6） |
| Code Graph | **v1.1.6**（6/30）单工具 **`codegraph_explore`** | 大仓 Agent 预索引 **符号/调用边**，减少 **Read/Grep 轮次** |
| Spring Alibaba AI | 无 7/1 release；Graph + **Langfuse OTel** 已有社区集成范例 | Java Agent 用 **Graph observation starter** + Langfuse **OTLP** 做端到端 trace |
| 政府门控发布 | **Fable 5 全球恢复** vs **GPT-5.6 仍锁预览** | 生产需 **模型别名 + 降级链** |
| 桌面 Agent | **Gemini Spark** macOS beta | **Workspace-native** + **MCP/connected apps** 对标 Claude Cowork |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **Anthropic Redeploying Fable 5** | 2026 **出口管制 × frontier 发布** 一手时间线 |
| 必读 | **Langfuse v3.203.0 release** | **MCP mutating/HITL** 与 trace UI 修复的当日基准 |
| 推荐 | **Gemini Spark on Mac + connected apps** | **桌面文件权限 + 第三方 App** 的产品组合 |
| 推荐 | **Claude Code v2.1.198** | 后台 Agent **PR 自动化** 工程参考 |
| 推荐 | **CodeGraph v1.1.6 + explore MCP** | 本地代码图谱降低 Agent **工具调用/token** 的实证路径 |
| 延伸 | **langgraph 1.2.7** | 长运行 Agent **状态/channel** 稳定性补丁 |

### 来源清单

- 检索范围：2026-07-01 00:00:00 到 2026-07-01 23:59:59（Asia/Shanghai）
- 引用域名：anthropic.com, blog.google, openai.com, techcrunch.com, theverge.com, github.com, langfuse.com, npmjs.com, java2ai.com, community.openai.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 官方发布 | Redeploying Claude Fable 5 | 2026-07-01 | https://www.anthropic.com/news/redeploying-fable-5 |
| 官方发布 | Claude Sonnet 5 | 2026-06-30（相邻日期/中国时间窗口传播） | https://www.anthropic.com/news/claude-sonnet-5 |
| 官方发布 | Gemini Spark updates | 2026-07-01 | https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-june-2026/ |
| 技术媒体 | Gemini Spark on Mac | 2026-07-01 | https://techcrunch.com/2026/07/01/gemini-spark-googles-agentic-assistant-is-now-available-on-mac/ |
| 技术媒体 | Together AI Series C | 2026-07-01 | https://techcrunch.com/2026/07/01/neocloud-together-ai-raises-800m-leaps-to-8-3b-valuation/ |
| 技术媒体 | Fable 5 back（The Verge） | 2026-07-01 | https://www.theverge.com/ai-artificial-intelligence/958964/anthropic-claude-fable-5-is-back |
| 开源发布 | Claude Code v2.1.198 | 2026-07-01 | https://github.com/anthropics/claude-code/releases/tag/v2.1.198 |
| 开源发布 | Hermes Agent v0.18.0 | 2026-07-01 | https://github.com/NousResearch/hermes-agent/releases |
| 开源发布 | Langfuse v3.203.0 | 2026-07-01 | https://github.com/langfuse/langfuse/releases/tag/v3.203.0 |
| 开源发布 | langgraph 1.2.7 | 2026-06-30（相邻日期/中国时间窗口传播） | https://github.com/langchain-ai/langgraph/releases/tag/1.2.7 |
| 开源发布 | @colbymchenry/codegraph v1.1.6 | 2026-06-30（相邻日期/中国时间窗口传播） | https://www.npmjs.com/package/@colbymchenry/codegraph |
| 官方文档 | Langfuse + Spring AI OTel | 参考文档 | https://langfuse.com/integrations/frameworks/spring-ai |
| 官方发布 | GPT-5.6 preview | 2026-06-26（相邻日期/中国时间窗口传播） | https://openai.com/index/previewing-gpt-5-6-sol/ |
| 运维 | OpenAI account ban thread | 2026-07-01 | https://community.openai.com/t/switching-subscription-plans-can-lead-to-account-bans/1385430 |

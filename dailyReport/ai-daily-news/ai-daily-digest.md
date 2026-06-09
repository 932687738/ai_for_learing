# AI Daily News Digest

按 Asia/Shanghai 时区增量汇总 AI/人工智能相关每日资讯。

## 2026-06-09

### 今日总览

**一句话结论**：`2026-06-09` 是 **「Mythos 首次公众化（Fable 5）+ WWDC 次日 Apple×Google 联合声明 + 前沿模型安全与成本双线」**——Anthropic 发布 **Claude Fable 5 / Mythos 5**（Mythos-class 首次 GA，含 cyber/bio 护栏与 **Opus 4.8 fallback**）；Apple 与 Google 发布 **Gemini 驱动的 AFM 下一代** 联合声明，并因 **DMA** 宣布 **欧盟 iOS/iPadOS 暂不提供 Siri AI**；产业侧 **SpaceX AI1 卫星 + 6/12 IPO**、**Miasma 蠕虫** 持续发酵、**Apify MCP Connectors** 上线。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | Anthropic 官方；Apple/Google 官方；TechCrunch/Axios/CNBC；arXiv 6/9；Apify；专项工具链 |
| 核心趋势 | **Mythos 产品化**：Fable 5 **$10/$50 per Mtok**、**6/22 前** 订阅含免费窗口；**端侧 Agent 监管分化**：Siri AI 在 **EU/中国** 受阻；**Agent 供应链安全**：Miasma 针对 **Claude Code/Gemini CLI/Cursor** 配置触发 |
| 可直接关注 | 评估 **claude-fable-5** API 与 **30 天 retention** 企业条款；EU/中国产品路线对照 **Private Cloud Compute + Gemini** 架构；CI 扫描 **`.claude/settings.json` + `[skip ci]`** 恶意 commit |
| 专项检索结论 | **Claude Code**：无 **6/9** 新版本（Fable 5 驱动 API/CLI 后端升级）；**Codex**：无 **6/9** 新 release；**OpenClaw**：无 **6/9** 官方 release（**2026.6.5 MCP hardening 为 6/6**）；**Hermes**：无 **6/9** 官方 release；**Spring AI**：无 **6/9** 官方 release；**skills**：无 **6/9** marketplace 新公告（Fable 5 能力外溢至 **Agent/Deep Research** 场景） |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| Anthropic / 模型 | [Claude Fable 5 and Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) | **2026-06-09** | 官方发布 | **Mythos-class 首次 GA**；cyber/bio/chemistry/distillation 高风险查询 **fallback Opus 4.8**（<5% sessions）；**Mythos 5** 限 Glasswing/可信访问 |
| Anthropic / 定价 | [Claude API Pricing — Fable 5](https://docs.anthropic.com/en/docs/about-claude/pricing) | **2026-06-09** | 开发者文档 | **$10/$50 per Mtok**（Opus 4.8 的 2×）；**6/22 前** Pro/Max/Team/Enterprise 含 Fable 5 |
| 媒体 / Anthropic | [Anthropic's Claude Fable 5（TechCrunch）](https://techcrunch.com/2026/06/09/anthropics-claude-fable-5-is-a-version-of-mythos-the-public-can-access-today/) | **2026-06-09** | 技术媒体 | 披露 **30 天 traffic retention** 防 jailbreak；**6/23** 起需 usage credits |
| Apple / Google | [Joint statement from Google and Apple](https://blog.google/company-news/inside-google/company-announcements/joint-statement-google-apple/) | **2026-06-09**（WWDC 期间传播） | 官方声明 | **AFM 下一代基于 Gemini**；仍跑 **Apple 设备 + Private Cloud Compute** |
| Apple / 监管 | [Due to DMA, Siri AI delayed in EU](https://www.apple.com/newsroom/2026/06/due-to-dma-siri-ai-delayed-in-eu-for-ios-27-and-ipados-27/) | **2026-06-09** | 政策/产品 | **欧盟 iOS/iPadOS/watchOS** 暂无 Siri AI；**macOS/visionOS** 仍可用 |
| 算力 / IPO | [SpaceX AI1 satellite + IPO（TradingKey）](https://www.tradingkey.com/analysis/stocks/us-stocks/261954234-elonmusk-spacex-ipo-ai1-tradingkey) | **2026-06-09** | 基础设施 | **AI1** 轨道数据中心设计；**6/12** 目标 IPO **~$1.77T** |
| Agent 安全 | [Microsoft repos disabled — Miasma worm（StepSecurity）](https://www.stepsecurity.io/blog/miasma-worm-hits-microsoft-again-azure-functions-action-and-72-other-repositories-disabled-after-supply-chain-attack-targeting-ai-coding-agents) | **2026-06-05**（攻击）/ **6/9**（持续报道） | 安全事件 | **73 仓库** 被禁；**Claude Code/Gemini CLI/Cursor/VS Code** 配置触发凭证收割 |
| MCP / 工具 | [Apify announces MCP connectors（AP News）](https://uat.apnews.com/press-release/ein-presswire-newsmatics/press-release-b667f2f5cefd4818b3a5785a0e38855c) | **2026-06-09** | 开源/平台 | Actor 经 **MCP** 连接 Notion/GitHub/Slack；用户 OAuth、Actor 不见凭证 |
| 成本治理 | [Can tech companies learn to love cheaper models?（TechCrunch）](https://techcrunch.com/2026/06/09/can-tech-companies-learn-to-love-cheaper-models/) | **2026-06-09** | 行业分析 | Harvey×Fireworks **3× 推理成本下降** 案例；大/小模型路由成 FinOps 焦点 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| Mythos 产品化 | **Anthropic Fable 5 公告** | 护栏+fallback、Glasswing/Mythos 5、定价窗口 | 平台/安全/研发 |
| 端侧 AI 监管 | **Apple DMA 说明** | Trusted System Agent 提案被拒；EU 功能缺口 | 移动端/合规 |
| Agent 供应链 | **StepSecurity Miasma 分析** | `.github/setup.js`、多 IDE 配置触发 | DevSecOps |
| MCP 集成 | **Apify MCP Connectors 文档** | 用户 OAuth、工具级 ACL | Agent 平台工程师 |
| 模型路由 | **TechCrunch：cheaper models** | Opus+GLM 混合、mini 模型替代 | FinOps/架构 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：6/9 呈现 **「最强 cyber-capable 模型 cautiously GA + OS 级 Agent 地缘/regulatory 分叉 + coding agent 供应链攻击常态化」**——Fable 5 把 Mythos 能力带入订阅/API，但用 **fallback + retention** 换安全；Apple/Google 联合声明确立 **Gemini×Private Cloud Compute** 模板；Miasma 则证明 **Agent IDE 配置即攻击面**。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| Mythos GA | **Fable 5 / Mythos 5** | 高风险域应 **模型路由+fallback** 而非单一 frontier |
| 端侧 Agent | **Siri AI EU 延迟** | 全球产品需 **regional feature matrix** 与 **DMA/本地化** 预案 |
| MCP 生态 | **Apify Connectors** | 第三方 Actor + 用户 OAuth = 新 **工具链 ACL** 模式 |
| Agent 安全 | **Miasma** | 仓库打开即执行：**CI 强制扫描 agent 配置变更** |
| 成本 | **小模型路由** | 长任务应用 **effort tier + 模型 cascade** 降 bill |
| 专项空窗 | Codex/OpenClaw/Hermes/Spring AI/skills 无 6/9 release | 跟进 **6/6 OpenClaw MCP fix** 与 **6/2 dynamic workflows** |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **Anthropic Fable 5 官方文** | 2026 **Mythos-class 公众化** 的护栏/定价/访问分层样板 |
| 必读 | **Apple DMA + Siri AI 公告** | 理解 **OS Agent 在欧盟为何停摆** |
| 推荐 | **Google×Apple 联合声明** | **Gemini AFM** 官方口径与隐私边界 |
| 推荐 | **Miasma 供应链分析** | **AI coding agent** 时代的新型 worm 模式 |
| 延伸 | **DuMate-DeepResearch 论文** | 可审计 **multi-agent deep research** 工程框架 |

### 来源清单

- 检索范围：2026-06-09 00:00:00 到 2026-06-09 23:59:59（Asia/Shanghai）
- 引用域名：anthropic.com, docs.anthropic.com, techcrunch.com, blog.google, apple.com, tradingkey.com, stepsecurity.io, apnews.com, arxiv.org, axios.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 官方发布 | Claude Fable 5 and Mythos 5 | 2026-06-09 | https://www.anthropic.com/news/claude-fable-5-mythos-5 |
| 开发者文档 | Claude Fable 5 pricing | 2026-06-09 | https://docs.anthropic.com/en/docs/about-claude/pricing |
| 技术媒体 | TechCrunch Fable 5 | 2026-06-09 | https://techcrunch.com/2026/06/09/anthropics-claude-fable-5-is-a-version-of-mythos-the-public-can-access-today/ |
| 官方声明 | Google×Apple joint statement | 2026-06-09 | https://blog.google/company-news/inside-google/company-announcements/joint-statement-google-apple/ |
| 政策/产品 | Apple DMA Siri delay | 2026-06-09 | https://www.apple.com/newsroom/2026/06/due-to-dma-siri-ai-delayed-in-eu-for-ios-27-and-ipados-27/ |
| 基础设施 | SpaceX AI1 / IPO | 2026-06-09 | https://www.tradingkey.com/analysis/stocks/us-stocks/261954234-elonmusk-spacex-ipo-ai1-tradingkey |
| 安全事件 | Miasma worm | 2026-06-05/6/9 传播 | https://www.stepsecurity.io/blog/miasma-worm-hits-microsoft-again-azure-functions-action-and-72-other-repositories-disabled-after-supply-chain-attack-targeting-ai-coding-agents |
| 开源/平台 | Apify MCP connectors | 2026-06-09 | https://uat.apnews.com/press-release/ein-presswire-newsmatics/press-release-b667f2f5cefd4818b3a5785a0e38855c |
| 行业分析 | Cheaper models | 2026-06-09 | https://techcrunch.com/2026/06/09/can-tech-companies-learn-to-love-cheaper-models/ |
| 论文 | DuMate-DeepResearch | 2026-06（arXiv） | https://arxiv.org/html/2606.07299v1 |

## 2026-06-08

### 今日总览

**一句话结论**：`2026-06-08` 是 **「WWDC 2026 端侧 AI 平台化 + OpenAI IPO 选项公开 + 消费级 Siri AI 落地」**——Apple 发布 **第三代 Apple Foundation Models（AFM 3 家族）** 与 **Siri AI** 独立 App；OpenAI 同日 **机密递交 S-1** 并启动 **Economic Research Exchange**；政策侧 **NSPM-11** 解读持续发酵（签署 **6/5**，Fact Sheet **6/5–6/6** 传播）。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | Apple 官方/ML Research；OpenAI 公司公告；TechCrunch/WIRED；政策 NSPM-11 解读；专项工具链 |
| 核心趋势 | **端侧+私有云双轨**：AFM 3 设备端/Private Cloud Compute 并行；**助手产品化**：Siri AI 独立 App + Extensions 生态；**资本化路径**：OpenAI S-1 机密递交但不急于上市 |
| 可直接关注 | 评估 **Siri AI Extensions** 对 Agent 插件市场的冲击；跟踪 **OpenAI Economic Research Exchange** RFP（截止 **7/5**）；对照 **AFM 3 Cloud** 的 agentic tool use 与现有 MCP 集成方案 |
| 专项检索结论 | **Claude Code**：无 **6/8** 官方 release（最近 **v2.1.168 为 6/6**）；**Codex**：无 **6/8** 新公告（**6/2** 角色插件/Sites 仍为主线）；**OpenClaw**：Build 2026 后 **Scout** 基于 OpenClaw runtime 讨论延续（**6/7** 媒体）；**Hermes**：无 **6/8** 官方 release；**Spring AI**：无 **6/8** 官方 release；**skills**：无 **6/8** 官方 marketplace 新公告 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| Apple / 平台 | [Apple Intelligence brings powerful AI capabilities into everyday experiences](https://www.apple.com/newsroom/2026/06/apple-intelligence-brings-powerful-ai-capabilities-into-everyday-experiences/) | **2026-06-08** | 官方发布 | **Siri AI** 独立 App；Photos/Safari/Passwords/Image Playground 等系统级 AI；开发者测试版 **当日** 开放 |
| Apple / 模型 | [Introducing the Third Generation of Apple's Foundation Models](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models) | **2026-06-08** | 官方研究 | **AFM 3 家族**（设备端+Cloud）；与 Google 合作定制；**Private Cloud Compute** 隐私架构 |
| OpenAI / 资本 | [Confidential submission of draft S-1 to the SEC](https://openai.com/index/openai-submits-confidential-s-1/) | **2026-06-08** | 公司公告 | 机密递交 S-1 获 **上市选项**；明确 **尚未决定时间表**，部分工作私有公司更易完成 |
| OpenAI / 研究 | [Introducing the OpenAI Economic Research Exchange](https://openai.com/index/economic-research-exchange/) | **2026-06-08** | 官方项目 | 外部实证研究 AI 经济影响；申请 **7/5** 截止，**7/31** 通知入选 |
| OpenAI / 治理 | [Built to benefit everyone: our plan](https://openai.com/index/built-for-broad-benefit/) | **2026-06-08** | 公司战略 | 第三运营阶段规划；与 S-1、Research Exchange 同日发布 |
| 媒体 / Apple | [Apple's New Siri AI Is Ready to Get Personal（WIRED）](https://www.wired.com/story/apples-new-siri-ai-is-ready-to-get-personal/) | **2026-06-08** | 技术媒体 | **Gemini** 合作驱动底层能力；更 conversational、action-oriented |
| 政策（传播） | [Speed Over Caution: What NSPM-11 Means](https://smallwarsjournal.com/2026/06/08/speed-over-caution-what-nspm-11-means/) | **2026-06-08** | 政策解读 | **NSPM-11**（**6/5** 签署）120 天多供应商采购、90 天自主武器政策更新等时间表梳理 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| 端侧 AI 架构 | **Apple AFM 3 研究文** | 设备端/Cloud 模型分工、Private Cloud Compute | 移动端/隐私敏感 Agent 研发 |
| 助手生态 | **Apple Newsroom：Siri AI** | Extensions 插件、跨 App 行动、Visual Intelligence | 消费级 Agent 产品 |
| AI 经济研究 | **OpenAI Economic Research Exchange RFP** | 外部合作、数据访问、独立实证 | 政策/FinOps/研究者 |
| 国防 AI 采购 | **NSPM-11 Fact Sheet（白宫）** | 多供应商 onboarding、vendor lock-in 禁令 | 政企合规/安全架构 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：6/8 呈现 **「平台厂商把 Agent 能力沉入 OS + 云厂商开放研究协作 + 国防 AI 加速落地」**——Apple 把 agentic tool use 写进 **AFM 3 Cloud** 与 Safari/Passwords 等系统 Agent；OpenAI 则在资本与研究两端同时为 **IPO 叙事** 铺路。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| OS 级 Agent | **Siri AI + Extensions** | 第三方 Agent 需适配 **系统级权限/隐私沙箱**，而非仅 Chat API |
| 端云协同 | **AFM 3 + Private Cloud Compute** | 敏感任务本地、重推理上云——与 **混合路由** 架构一致 |
| 开源 runtime | **Scout on OpenClaw**（**6/7** 传播） | **控制面（M365/MCP）> runtime**；OpenClaw 成多厂商共用底座 |
| Agent 记忆安全 | **MemLineage/TOKI** 论文（arXiv，相邻） | 长周期 Agent 需 **溯源链 + 双时态** 防 memory poisoning |
| 专项空窗 | Claude Code/Codex/Spring AI/skills 无 6/8 release | 跟进 **6/6–6/7** 工具链更新即可 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **Apple AFM 3 官方研究** | 2026 消费硬件 **端侧 Agent** 的官方模型栈与隐私边界 |
| 必读 | **OpenAI S-1 机密递交公告** | 理解 **AGI 公司资本化** 与产品路线的时间权衡 |
| 推荐 | **OpenAI Economic Research Exchange** | 外部验证 AI 劳动市场/企业影响的主流渠道 |
| 推荐 | **WIRED：Siri AI** | 快速把握 **Apple×Google** 合作的产品化形态 |
| 延伸 | **NSPM-11 解读** | 国防/情报 **多 vendor Agent** 采购的 120 天窗口 |

### 来源清单

- 检索范围：2026-06-08 00:00:00 到 2026-06-08 23:59:59（Asia/Shanghai）
- 引用域名：apple.com, machinelearning.apple.com, openai.com, wired.com, smallwarsjournal.com, whitehouse.gov
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 官方发布 | Apple Intelligence / Siri AI | 2026-06-08 | https://www.apple.com/newsroom/2026/06/apple-intelligence-brings-powerful-ai-capabilities-into-everyday-experiences/ |
| 官方研究 | AFM 3 第三代基础模型 | 2026-06-08 | https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models |
| 公司公告 | OpenAI 机密 S-1 | 2026-06-08 | https://openai.com/index/openai-submits-confidential-s-1/ |
| 官方项目 | Economic Research Exchange | 2026-06-08 | https://openai.com/index/economic-research-exchange/ |
| 公司战略 | Built to benefit everyone | 2026-06-08 | https://openai.com/index/built-for-broad-benefit/ |
| 技术媒体 | WIRED Siri AI | 2026-06-08 | https://www.wired.com/story/apples-new-siri-ai-is-ready-to-get-personal/ |
| 政策解读 | NSPM-11 时间表 | 2026-06-08 | https://smallwarsjournal.com/2026/06/08/speed-over-caution-what-nspm-11-means/ |

## 2026-06-07

### 今日总览

**一句话结论**：`2026-06-07` 是 **「Agent 检索架构革新 + 开源终端 Coding Agent + OpenClaw 成为企业 Agent runtime 底座」**——Perplexity 推出 **Search as Code**（Agent 写 Python 检索流水线）；Moonshot 发布开源 **KmCode CLI**；微软 **Scout** 选用 **OpenClaw** runtime；Unisound 发布原生 **U2 agentic** 模型。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | Perplexity 官方/媒体；Moonshot GitHub/npm；The New Stack；Unisound PR；OpenAI 战略报道；专项工具链 |
| 核心趋势 | **Search as Code**：把 filter/rank 移出 LLM context，宣称 CVE 案例 **~85% token 节省**；**Terminal Agent 开源化**：KmCode CLI（MIT/TypeScript）；**Runtime commodity**：OpenClaw 被 Microsoft Scout 采用 |
| 可直接关注 | 评估 **SaC** 对 MCP 工具链调用的替代/补充；试用 **KmCode CLI** 的 coder/explore/plan 子 Agent；跟踪 **Scout→OpenClaw** 上游 policy 贡献 |
| 专项检索结论 | **Claude Code**：无 **6/7** release；**Codex**：无 **6/7** release；**OpenClaw**：**Scout** 基于 OpenClaw（Build 2026，**6/7** The New Stack）；**Hermes**：无 **6/7** 官方 release（对比文延续）；**Spring AI**：无 **6/7** release；**skills**：无 **6/7** 官方 marketplace 新公告 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| Agent 检索 | [Perplexity Lets AI Agents Write Their Own Search Code（WinBuzzer）](https://winbuzzer.com/2026/06/07/perplexity-lets-ai-agents-write-their-own-search-code-xcxwbn/) | **2026-06-07** | 架构发布 | **Search as Code**：模型+沙箱+Agentic Search SDK；默认接入 **Perplexity Computer** 与 **Agent API** |
| Agent 检索 | [Perplexity Search as Code 分析（Abhishek Gautam）](https://www.abhs.in/blog/perplexity-search-as-code-85-percent-tokens-agent-api-june-2026) | **2026-06-07** | 技术解读 | 200 CVE 案例：**100% 准确率**、**42.9K vs 288.7K tokens**（公司报告，待独立复现） |
| 开源 Coding Agent | [Moonshot KmCode CLI（AI Intensify）](https://ai-intensify.com/moonshot-ai-releases-kmcode-cli-a-terminal-ai-coding-agent-built-in-typescript-for-the-next-generation-of-agents/) | **2026-06-07** | 开源发布 | **MIT**、TypeScript、npm 分发；**coder/explore/plan** 子 Agent；交互式 **/mcp-config** |
| 企业 Agent | [Microsoft Scout on OpenClaw runtime（The New Stack）](https://thenewstack.io/microsoft-scout-openclaw-runtime/) | **2026-06-07** | 行业分析 | **Scout** always-on work agent 基于 **OpenClaw**；MCP 连接 M365；upstream 贡献 enterprise policy |
| 模型/Agent | [Unisound U2 native agentic model（PRNewswire/Yahoo）](https://finance.yahoo.com/sectors/technology/articles/unisound-releases-u2-native-agentic-020300793.html) | **2026-06-07** | 产品发布 | **100+ 步**复杂工作流自主分解执行；**Unisound Token Hub** 开放 |
| 产品战略 | [OpenAI is still working on that 'super app'（TechCrunch）](https://techcrunch.com/2026/06/07/openai-is-still-working-on-that-super-app/) | **2026-06-07** | 行业分析 | ChatGPT **super app** 整合 Codex/Agent；IPO 前 profitability 压力 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| Agent 检索架构 | **Perplexity Search as Code** | Python 沙箱流水线 vs 固定 search API | Agent/RAG 平台工程师 |
| 终端 Agent | **KmCode CLI（Moonshot）** | 子 Agent 上下文隔离、MCP 交互配置 | 开源 coding agent 贡献者 |
| 企业 runtime | **The New Stack：Scout/OpenClaw** | OpenClaw 作 **free runtime**、控制面商业化 | 平台架构师 |
| Agentic 模型 | **Unisound U2 发布** | 高 intelligence density、长链执行 | 垂直 Agent 应用 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：6/7 的工程信号是 **「检索/工具调用从 prompt 搬到 code」** 与 **「开源 terminal agent + 商业 control plane 分层」** 同时加速。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 检索架构 | **Search as Code** | 复杂 filter/rank 应 **代码化+沙箱执行**，降低 context bloat |
| 开源 Agent | **KmCode CLI** | TypeScript terminal agent 成主流栈；注意 **km-cli 迁移** 路径 |
| Runtime 生态 | **OpenClaw + Scout** | 自研 runtime 让位于 **开源底座+企业策略层** |
| 长链执行 | **Unisound U2** | 「native agentic」强调 **规划-工具-校验闭环** 而非单轮 QA |
| 专项 | Hermes/Spring AI/skills 无 6/7 更新 | OpenClaw 生态热度来自 **Build 2026** 连续报道 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **Perplexity Search as Code** | 2026 Agent 检索 **code-generation** 范式代表 |
| 推荐 | **The New Stack：Scout/OpenClaw** | 理解 **Agent runtime 商品化** 与 Microsoft 策略 |
| 推荐 | **KmCode CLI 发布** | Moonshot 开源 terminal agent 的 **MCP/子 Agent** 设计 |
| 延伸 | **Unisound U2** | 中文市场 **长链 agentic** 模型样本 |

### 来源清单

- 检索范围：2026-06-07 00:00:00 到 2026-06-07 23:59:59（Asia/Shanghai）
- 引用域名：winbuzzer.com, abhs.in, ai-intensify.com, thenewstack.io, finance.yahoo.com, techcrunch.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 架构发布 | Perplexity Search as Code | 2026-06-07 | https://winbuzzer.com/2026/06/07/perplexity-lets-ai-agents-write-their-own-search-code-xcxwbn/ |
| 技术解读 | SaC token 分析 | 2026-06-07 | https://www.abhs.in/blog/perplexity-search-as-code-85-percent-tokens-agent-api-june-2026 |
| 开源发布 | Moonshot KmCode CLI | 2026-06-07 | https://ai-intensify.com/moonshot-ai-releases-kmcode-cli-a-terminal-ai-coding-agent-built-in-typescript-for-the-next-generation-of-agents/ |
| 行业分析 | Microsoft Scout/OpenClaw | 2026-06-07 | https://thenewstack.io/microsoft-scout-openclaw-runtime/ |
| 产品发布 | Unisound U2 | 2026-06-07 | https://finance.yahoo.com/sectors/technology/articles/unisound-releases-u2-native-agentic-020300793.html |
| 行业分析 | OpenAI super app | 2026-06-07 | https://techcrunch.com/2026/06/07/openai-is-still-working-on-that-super-app/ |

## 2026-06-06

### 今日总览

**一句话结论**：`2026-06-06` 是 **「企业 AI 安全加固 + Claude Code 密集补丁 + 国防 AI 政策落地传播」**——OpenAI 发布 **Lockdown Mode** 防 prompt injection 数据外泄；**Claude Code v2.1.166/v2.1.168** 同日连发 reliability 修复；**NSPM-11** Fact Sheet 公开传播；Trump 政府入股 OpenAI 讨论升温。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | OpenAI/TechCrunch；GitHub claude-code releases；白宫 NSPM-11；Anthropic Mythos 生态；专项工具链 |
| 核心趋势 | **Prompt injection 企业防护**：Lockdown Mode 禁用 live browse/agent/deep research；**Coding Agent 运维密度**：Claude Code 6 月第 8 次 release；**国防 AI 多 vendor**：NSPM-11 取代 NSM-25 |
| 可直接关注 | 敏感数据场景启用 **Lockdown Mode** 并评估 **cached-only** 浏览限制；升级 **Claude Code ≥2.1.168**；跟踪 **NSPM-11** 120 天采购改造截止 **~10/3** |
| 专项检索结论 | **Claude Code**：**v2.1.166**（21 changes）+ **v2.1.168**（reliability，Published **2026-06-06**）；**Codex**：无 **6/6** 新 release；**OpenClaw/Hermes**：无 **6/6** 官方 release；**Spring AI**：无 **6/6** release（**2.0 GA 目标 5/28** 已过，关注 **Boot 3.5 EOL 6/30**）；**skills**：无 **6/6** 官方 marketplace 新公告 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| OpenAI / 安全 | [OpenAI unveils Lockdown Mode（TechCrunch）](https://techcrunch.com/2026/06/06/openai-unveils-lockdown-mode-to-protect-sensitive-data-from-prompt-injection-attacks/) | **2026-06-06** | 产品安全 | 禁用 live web/agent/deep research 等；面向 **ChatGPT Business** 与符合条件个人账号 |
| Claude Code | [claude-code v2.1.168](https://github.com/anthropics/claude-code/releases/tag/v2.1.168) | **2026-06-06** | 开源发布 | **Bug fixes and reliability improvements**；Published **2026-06-06T23:41:53Z** |
| Claude Code | [claude-code v2.1.166](https://changelogs.directory/tools/claude-code/releases/2.1.166) | **2026-06-06** | 开源发布 | **21 changes**：fallback model、image/remote session/terminal 修复 |
| 政策 | [White House NSPM-11 Fact Sheet](https://www.whitehouse.gov/fact-sheets/2026/06/fact-sheet-president-donald-j-trump-signs-historic-directive-on-ai-in-the-national-security-enterprise/) | **2026-06-05**（签署）/ **6/6**（传播） | 政策标准 | 加速国防 AI 采纳；禁止 vendor 未经批准 disable 军用 AI；取代 **NSM-25** |
| 政策/资本 | [Trump admin may take OpenAI equity stake（TechCrunch）](https://techcrunch.com/2026/06/06/the-trump-administration-might-take-an-equity-stake-in-openai/) | **2026-06-06** | 政策/行业 | **Public Wealth Fund** 概念；与 **Bernie Sanders 50% stock tax** 提案对照 |
| 人事 | [Sriram Krishnan leaving White House AI advisor（TechCrunch）](https://techcrunch.com/2026/06/06/sriram-krishnan-is-leaving-his-role-as-white-house-ai-advisor/) | **2026-06-06** | 政策 | 白宫 AI 顾问 **6 月底** 离任；AI Action Plan 后续机构化 |
| Anthropic（相邻） | [Claude Mythos 印度扩展（Wikipedia/报道）](https://en.wikipedia.org/wiki/Claude_Mythos) | **2026-06-02**（相邻日期/中国时间窗口传播） | 生态 | Mythos 向 **150 组织/15 国** 扩展 Glasswing 访问 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| Prompt injection | **OpenAI Lockdown Mode** | cached-only 浏览、禁用 agent mode | 企业安全/合规 |
| Coding Agent 运维 | **Claude Code 2.1.166/168** | fallback model、跨 session 稳定性 | CLI agent 日常用户 |
| 国防 AI 采购 | **NSPM-11 全文/ Fact Sheet** | 多 vendor onboarding、vendor lock-in 禁令 | 政企 AI 架构 |
| Spring 迁移 | **Spring Boot 3.5 EOL（6/30）** | 与 Spring AI 2.0 迁移窗口重叠 | Java AI 团队 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：6/6 突出 **「Agent 攻击面治理（Lockdown）+ 工具链高频 patch（Claude Code）+ 国家级 Agent 采购框架（NSPM-11）」** 三线。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 数据外泄防护 | **Lockdown Mode** | 高敏环境应 **分层禁用工具** 而非仅依赖 prompt 过滤 |
| CLI Agent 稳定性 | **Claude Code 连发 patch** | 生产使用应 **pin 版本** 并跟踪 release 频率 |
| 国防 Agent | **NSPM-11** | 多 vendor + 禁止 unilateral vendor shutdown——影响 **SLA/exit clause** 设计 |
| 专项空窗 | Codex/OpenClaw/Hermes/Spring AI/skills 无 6/6 release | 关注 **6/2 Codex 插件** 与 **Build Scout** 后续 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **OpenAI Lockdown Mode（TechCrunch）** | 企业 Agent **prompt injection→exfiltration** 防护的首个产品化选项 |
| 必读 | **Claude Code v2.1.168 release** | 6 月 CLI agent **可靠性补丁** 官方来源 |
| 推荐 | **NSPM-11 Fact Sheet** | 美国国防 **多 vendor frontier AI** 采购框架 |
| 延伸 | **Trump/OpenAI equity 报道** | AI **公共资本化** 与治理争议样本 |

### 来源清单

- 检索范围：2026-06-06 00:00:00 到 2026-06-06 23:59:59（Asia/Shanghai）
- 引用域名：techcrunch.com, github.com, whitehouse.gov, changelogs.directory, en.wikipedia.org
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 产品安全 | OpenAI Lockdown Mode | 2026-06-06 | https://techcrunch.com/2026/06/06/openai-unveils-lockdown-mode-to-protect-sensitive-data-from-prompt-injection-attacks/ |
| 开源发布 | Claude Code v2.1.168 | 2026-06-06 | https://github.com/anthropics/claude-code/releases/tag/v2.1.168 |
| 开源发布 | Claude Code v2.1.166 | 2026-06-06 | https://changelogs.directory/tools/claude-code/releases/2.1.166 |
| 政策标准 | NSPM-11 Fact Sheet | 2026-06-05（签署）/ 6/6 传播 | https://www.whitehouse.gov/fact-sheets/2026/06/fact-sheet-president-donald-j-trump-signs-historic-directive-on-ai-in-the-national-security-enterprise/ |
| 政策/行业 | Trump/OpenAI equity | 2026-06-06 | https://techcrunch.com/2026/06/06/the-trump-administration-might-take-an-equity-stake-in-openai/ |
| 政策 | Krishnan 离任 | 2026-06-06 | https://techcrunch.com/2026/06/06/sriram-krishnan-is-leaving-his-role-as-white-house-ai-advisor/ |

## 2026-06-05

### 今日总览

**一句话结论**：`2026-06-05` 是 **「端侧 Gemma 4 QAT 落地 + 前沿 AI 协调暂停倡议 + Token 经济学危机显性化」**——Google 发布 **Gemma 4 QAT** 将 E2B 压至 **1GB** 级端侧内存；Anthropic 呼吁行业建立 **可验证协调暂停** 机制并披露 **Claude 已写 80%+ 合并代码**；产业侧 **Google×SpaceX 9.2 亿美元/月算力桥接**、**Tokenomics Foundation** 与 **Uber/Cursor 预算失控** 报道同日密集出现；工程侧 **GPT-5.2 Thinking 退役**、**Claude Code Workflows 预览** 与 **Agent Memory 系统表征论文** 形成对照。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | Google 官方；Anthropic API/治理；OpenAI 退役/运维；TechCrunch/The Next Web；arXiv 6/5；NVIDIA 相邻；专项工具链 |
| 核心趋势 | **端侧效率**：QAT 把 Gemma 4 推向手机/笔电本地推理；**治理前置**：递归自改进触发下的行业级刹车讨论升温；**Token 账单**：订阅→按量后企业 FinOps/Tokenomics 标准化需求爆发 |
| 可直接关注 | 评估 **Gemma 4 QAT**（Q4_0 + mobile schema）在 llama.cpp/Ollama/LiteRT-LM 的部署路径；长周期 Agent 对照 **Agent Memory** 论文的 write/read 成本拆分；企业侧启动 **token 可观测 + 路由/配额** 治理 |
| 专项检索结论 | **Claude Code**：**Workflows 研究预览**、**Auto mode** 扩面、**Opus 4.1 弃用公告**（API 文档 **2026-06-05** 条目）；**Codex**：**rusty-v8-v149.2.0** 预发布（**Published 2026-06-05**），社区反馈 **指令遵循退化/不安全 patch**；**OpenClaw/Hermes**：无 **6/5** 官方 release（生态讨论延续）；**Spring AI**：无 **6/5** 官方 release（最近 **2.0.0-M8 为 2026-05-27**）；**skills**：无 **6/5** 官方 marketplace 新公告，**Agent Skills 安全实证**（arXiv:2602.06547）持续被引用 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| Google / 端侧 | [Gemma 4 QAT models: Optimizing model compression for mobile and laptop efficiency](https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/) | **2026-06-05** | 官方发布 | **QAT** 训练内嵌量化；**E2B 文本版 <1GB**；Q4_0 + mobile 专用 schema；Hugging Face/llama.cpp/Ollama/LiteRT-LM 生态同步 |
| Anthropic / 治理 | [Anthropic urges a coordinated, verifiable pause for frontier AI（The Next Web）](https://thenextweb.com/news/anthropic-urges-a-coordinated-verifiable-pause-for-frontier-ai) | **2026-06-05** | 政策/治理 | 针对 **递归自改进** 提出 **多实验室可验证暂停**；披露 **5 月 Claude 写 80%+ 合并代码** |
| Anthropic / 企业 | [Securing & Governing Claude: Compliance API webinar](https://www.anthropic.com/webinars/securing-governing-claude-the-compliance-api-and-security-integrations) | **2026-06-05** | 官方活动 | **Compliance API** 暴露活动/聊天/文件/项目用量，对接企业安全栈 |
| Anthropic / API | [Claude Platform Release Notes — Opus 4.1 deprecation](https://platform.claude.com/docs/en/release-notes/overview) | **2026-06-05** | 开发者文档 | **claude-opus-4-1-20250805** 将于 **2026-08-05** 退役；建议迁移 **Opus 4.8** |
| Claude Code | [Claude Code — Workflows research preview（API release notes）](https://platform.claude.com/docs/en/release-notes/overview) | **2026-06-05** | 产品/工程 | **Workflows** 多步 agentic 计划；**Auto mode** 扩面长任务；Max 默认 **Opus 4.8 fast mode** |
| OpenAI / 产品 | [Introducing GPT-5.4 — GPT-5.2 Thinking retirement note](https://openai.com/index/introducing-gpt-5-4/) | **2026-06-05** | 产品生命周期 | **GPT-5.2 Thinking** 在模型选择器中 **2026-06-05 退役**（付费用户 Legacy 区保留 3 个月） |
| OpenAI / 运维 | [Some users may experience issues accessing OpenAI accounts（Status）](https://status.openai.com/incidents/01KTBZDS20E3PZ53DH2SCKXN49) | **2026-06-05** | 运维事件 | 部分账号被 **误封/暂停**，团队恢复访问并处理订阅/额度 |
| 算力 / 云 | [Google will pay SpaceX $920M per month for compute（TechCrunch）](https://techcrunch.com/2026/06/05/google-will-pay-spacex-920m-per-month-for-compute/) | **2026-06-05** | 基础设施 | **2026-10 至 2029-06** 桥接容量；约 **11 万 NVIDIA GPU**；满足 **Gemini Enterprise** 超预期需求 |
| 成本治理 | [The token bill comes due（TechCrunch）](https://techcrunch.com/2026/06/05/the-token-bill-comes-due-inside-the-industry-scramble-to-manage-ais-runaway-costs/) | **2026-06-05** | 行业分析 | **Uber 4 月烧完全年 AI 预算**；**Cursor 续费 4–5×**；Linux Foundation **Tokenomics Foundation** 7 月启动 |
| 基建 / 区域 | [AirTrunk commits $30B to build 5GW of AI data centers in India（TechCrunch）](https://techcrunch.com/2026/06/05/airtrunk-commits-30b-to-build-5gw-of-ai-data-centers-in-india/) | **2026-06-05** | 基础设施 | **2030 年前 5GW** 印度 AI DC；Maharashtra **3GW** 意向 |
| 安全 / 政策 | [NSA said to be readying Anthropic's Mythos for cyber operations（TechCrunch）](https://techcrunch.com/2026/06/05/nsa-said-to-be-readying-anthropics-mythos-for-use-in-cyber-operations/) | **2026-06-05** | 政策/安全 | 报道称 NSA 部署工程师协助使用 **Mythos**；与联邦 **供应链风险** 禁令背景交织 |
| 论文 | [Agent Memory: Characterization and System Implications（arXiv:2606.06448）](https://arxiv.org/abs/2606.06448) | **2026-06**（arXiv 编号） | 论文原文 | 首次 **Agent Memory 系统级表征**；write/read 成本不对称；10 条部署建议 |
| Codex / 发布 | [Codex rusty-v8-v149.2.0（prerelease）](https://github.com/openai/codex/releases/tag/rusty-v8-v149.2.0) | **2026-06-05** | 开源预发布 | V8 绑定层更新；非应用层 feature release |
| 生命科学（传播） | [OpenAI updates GPT-Rosalind（媒体报道）](https://cfotech.co.uk/story/openai-updates-gpt-rosalind-for-life-sciences-research) | **2026-06-03**（官方）/ **2026-06-05**（传播） | 相邻日期/中国时间窗口传播 | **GeneBench** 等评测 **31% 更少 token**；全球 **trusted-access** 扩展 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| 端侧推理 | [Gemma 4 QAT 官方文](https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/) | QAT vs PTQ、mobile 2-bit 策略、MTP QAT 权重 | 边缘/本地 Agent 研发 |
| Agent 记忆系统 | [Agent Memory 论文](https://arxiv.org/abs/2606.06448) | 四轴分类、construction/retrieval/generation 成本归因 | 平台/infra 工程师 |
| 企业治理 | [Anthropic Compliance API 研讨会](https://www.anthropic.com/webinars/securing-governing-claude-the-compliance-api-and-security-integrations) | 程序化审计、活动事件导出 | 安全/合规团队 |
| Token 经济学 | [TechCrunch：Token bill comes due](https://techcrunch.com/2026/06/05/the-token-bill-comes-due-inside-the-industry-scramble-to-manage-ais-runaway-costs/) | cost-per-intelligence、模型路由、配额分层 | FinOps/工程管理者 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：6/5 呈现 **「端侧模型压缩成熟 + Agent 记忆系统工程化 + 企业 Token 治理刚需」** 三线并进——Gemma 4 QAT 让本地 Agent 更接近消费硬件；Agent Memory 论文把 RAG 之后的 **可变状态层** 成本模型化；产业报道则把 **agentic 多步/多子 Agent** 的账单问题推到台前。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 端侧 Agent | **Gemma 4 QAT** E2B **<1GB** | 本地助手应优先评估 **QAT + 模态裁剪**（去 audio/vision encoder） |
| 记忆架构 | **Agent Memory** 系统表征 | 区分 **construction-heavy** vs **query-heavy** 设计；异步写入带来 **staleness** |
| Claude Code | **Workflows** 研究预览 | 多步计划应版本化并可审计，避免与 **ultracode** 触发词混淆 |
| Token 治理 | **Tokenomics Foundation** | 尽快建立 **per-team token budget + model router + 审计对账** |
| 专项空窗 | OpenClaw/Hermes/Spring AI/MCP 无 6/5 官方 release | 跟进 **5 月 OpenRouter 排行** 与 **6/2 Build/COMPUTEX** 发布即可 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **Gemma 4 QAT 官方发布** | 2026 端侧开源模型的 **量化训练** 官方配方与工具链 |
| 必读 | **Agent Memory（2606.06448）** | 长周期 Agent **记忆层** 的首个系统级成本画像 |
| 推荐 | **Anthropic 协调暂停倡议** | 理解 **递归自改进** 触发下的行业协调难题 |
| 推荐 | **TechCrunch：Token bill** | 企业 **Agent 规模化** 后的 FinOps 范式转移 |
| 延伸 | **Google×SpaceX 算力桥接** | 超大规模 **推理容量** 的短期合约与风险条款 |

### 来源清单

- 检索范围：2026-06-05 00:00:00 到 2026-06-05 23:59:59（Asia/Shanghai）
- 引用域名：blog.google, thenextweb.com, anthropic.com, platform.claude.com, openai.com, status.openai.com, techcrunch.com, arxiv.org, github.com, cfotech.co.uk, developer.nvidia.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 官方发布 | Gemma 4 QAT | 2026-06-05 | https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/ |
| 政策/治理 | Anthropic coordinated pause | 2026-06-05 | https://thenextweb.com/news/anthropic-urges-a-coordinated-verifiable-pause-for-frontier-ai |
| 官方活动 | Compliance API webinar | 2026-06-05 | https://www.anthropic.com/webinars/securing-governing-claude-the-compliance-api-and-security-integrations |
| 开发者文档 | Claude API Jun 5 notes | 2026-06-05 | https://platform.claude.com/docs/en/release-notes/overview |
| 产品生命周期 | GPT-5.2 Thinking retirement | 2026-06-05 | https://openai.com/index/introducing-gpt-5-4/ |
| 运维 | OpenAI account access incident | 2026-06-05 | https://status.openai.com/incidents/01KTBZDS20E3PZ53DH2SCKXN49 |
| 技术媒体 | Google SpaceX compute deal | 2026-06-05 | https://techcrunch.com/2026/06/05/google-will-pay-spacex-920m-per-month-for-compute/ |
| 技术媒体 | Token bill comes due | 2026-06-05 | https://techcrunch.com/2026/06/05/the-token-bill-comes-due-inside-the-industry-scramble-to-manage-ais-runaway-costs/ |
| 技术媒体 | AirTrunk India 5GW | 2026-06-05 | https://techcrunch.com/2026/06/05/airtrunk-commits-30b-to-build-5gw-of-ai-data-centers-in-india/ |
| 技术媒体 | NSA Mythos report | 2026-06-05 | https://techcrunch.com/2026/06/05/nsa-said-to-be-readying-anthropics-mythos-for-use-in-cyber-operations/ |
| 论文原文 | Agent Memory characterization | 2026-06（arXiv 编号） | https://arxiv.org/abs/2606.06448 |
| 开源预发布 | Codex rusty-v8-v149.2.0 | 2026-06-05 | https://github.com/openai/codex/releases/tag/rusty-v8-v149.2.0 |
| 相邻传播 | GPT-Rosalind update coverage | 2026-06-03（官方）/ 2026-06-05（传播） | https://cfotech.co.uk/story/openai-updates-gpt-rosalind-for-life-sciences-research |

## 2026-06-04

### 今日总览

**一句话结论**：`2026-06-04` 是 **「ChatGPT 记忆 Dreaming 架构升级 + 生物防御行动纲领 + 入口级 Agent 平台化」**——OpenAI 推出可自动刷新记忆的 **Dreaming** 与 **Biodefense** 计划；**ChatGPT App MAU 破 10 亿**（Sensor Tower，5 月达成、6/4 密集报道）；**Apple Messages for Business** 批准首个第三方 AI Agent **Poke**；**Meta** 帐篷式数据中心加速基建；工程侧 **Codex rust-v0.137.0** 发布、付费用户获 **配额补偿重置**。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | OpenAI 官方/API Changelog；TechCrunch/The Verge；Sensor Tower/Reuters；arXiv/Hugging Face 6/4；专项工具链 |
| 核心趋势 | **个性化记忆工程化**：Dreaming 从「保存笔记」走向后台合成、可审阅摘要；**平台入口争夺**：Poke×iMessage、Chesky 新 AI Lab、Amazon 自然语言 Proteus；**基建与资本**：Meta 帐篷 DC、SpaceX IPO 路演、Anthropic IPO 舆论延续 |
| 可直接关注 | Plus/Pro 用户评估 **Dreaming** 对长期项目记忆的时效性；Agent 产品对照 **Poke/Messages for Business** 交互范式；多 Agent 流水线可试验 **StreamMA** 流式步进传递 |
| 专项检索结论 | **Claude Code**：无 6/4 新 release（最近 **v2.1.160 为 2026-06-02**）；**Codex**：**rust-v0.137.0**（**Published 2026-06-04T01:17:20Z**）；**OpenClaw**：稳定线仍为 **v2026.5.12**（2026-05-14），无 6/4 tag；**Hermes**：无 6/4 官方 release；**Spring AI**：无 6/4 官方 release（最近 **2.0.0-M7 为 2026-05-22**）；**skills**：OpenAI **Dreaming/记忆摘要** 与社区 **Skills 自进化** 讨论延续，无 6/4 官方 Skills marketplace 新公告 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| OpenAI / 记忆 | [Dreaming: Better memory for a more helpful ChatGPT](https://openai.com/index/chatgpt-memory-dreaming/) | **2026-06-04** | 官方产品 | **Dreaming V3** 后台合成记忆，解决陈旧/矛盾 saved memories；Plus/Pro 美国首发 |
| OpenAI / 治理 | [Biodefense in the Intelligence Age](https://openai.com/index/biodefense-in-the-intelligence-age/) | **2026-06-04** | 官方发布 | 衔接 **GPT-Rosalind** 与 **Rosalind Biodefense**，强调防御方能力与治理 |
| OpenAI / API | [API Changelog — moderation scores](https://developers.openai.com/api/docs/changelog) | **2026-06-04** | 开发者文档 | **Responses/Chat Completions** 同请求返回输入与输出 moderation 分数 |
| OpenAI / ChatGPT | [ChatGPT Release Notes — Memory upgrade](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) | **2026-06-04** | 产品说明 | 自动更新记忆、Plus/Pro **双倍记忆容量**；可回退 legacy saved memories |
| 用户规模 | [ChatGPT app crosses 1B MAUs（The Hindu BusinessLine / Sensor Tower）](https://www.thehindubusinessline.com/news/chatgpt-app-crosses-1-billion-monthly-active-users-in-3-years-of-launch-india-20-of-this-user-base/article71061550.ece) | **2026-06-04**（报道）/ **2026-05**（MAU 达成） | 市场数据 | App MAU **10 亿**创纪录增速；印度占 **20%**；Claude App **~5600 万 MAU、YoY +640%** |
| Apple / Agent | [Apple approves Poke as first AI agent on Messages for Business（TechCrunch）](https://techcrunch.com/2026/06/04/apple-approves-poke-as-the-first-ai-agent-on-its-messages-for-business-platform/) | **2026-06-04** | 产品发布 | 第三方 **AI Agent** 首次进入 **iMessage 商业通道**；WWDC 前信号 |
| 创业 / 实验室 | [Airbnb's Brian Chesky plans to launch a new AI lab（TechCrunch）](https://techcrunch.com/2026/06/04/airbnbs-brian-chesky-plans-to-launch-a-new-ai-lab/) | **2026-06-04** | 行业动态 | Chesky 另立 AI Lab（交互/设计向），本人仍任 Airbnb CEO |
| Meta / 基建 | [Meta builds data centers in tents（TechCrunch）](https://techcrunch.com/2026/06/04/meta-steals-a-tactic-from-tesla-and-builds-data-centers-in-tents/) | **2026-06-04** | 基础设施 | **Rapid deployment structures** 缩短建设周期；Ohio 六座帐篷 + 模块化燃气轮机 |
| Amazon / 机器人 | [Amazon warehouse robot Proteus speaks natural language（The Verge）](https://www.theverge.com/ai-artificial-intelligence/942884/amazon-next-generation-warehouse-robot-proteus) | **2026-06-04** | 产品发布 | 员工自然语言派工，机器人自主排优先级/路径；**2027 H1** 欧洲部署 |
| Codex / 发布 | [Codex rust-v0.137.0](https://github.com/openai/codex/releases/tag/rust-v0.137.0) | **2026-06-04** | 开源发布 | TUI 键位、**parent_thread_id**、multi-agent v2 dogfood、插件与云配置层 |
| Codex / 运维 | [Codex usage reset for paid subscribers（Community）](https://community.openai.com/t/questions-about-an-unexpected-codex-usage-reset-and-new-quota-period/1382610) | **2026-06-04** | 运维补偿 | 6/3 服务异常后 **手动重置 100% 配额**；重置日变更非计划周期 |
| 论文 | [StreamMA: Streaming Communication in Multi-Agent Reasoning（arXiv:2606.05158）](https://arxiv.org/abs/2606.05158) | **2026-06-03**（提交）/ **HF 2026-06-04** 收录 | 论文原文 | 流式步进传递降延迟并提升准确率；**step-level scaling law** |
| Google / 路线 | [Alphabet investor presentation: June 2026](https://blog.google/alphabet/investor-presentation-june-2026/) | **2026-06-03**（相邻日期/中国时间窗口传播） | 官方投资者材料 | **Gemini 3.5 Pro** 预计 **6 月**落地；Flash 已 GA；**~900M** 月活 Gemini 用户 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| ChatGPT 记忆 | [Dreaming 官方文](https://openai.com/index/chatgpt-memory-dreaming/) | V0→V3 演进、memory summary 可审阅/可编辑 | 产品/对话 Agent 设计 |
| API 安全 | [OpenAI Moderation guide + Changelog](https://developers.openai.com/api/docs/changelog) | 生成请求内嵌 **moderation** 对象 | 平台合规工程 |
| 多 Agent | [StreamMA 论文](https://arxiv.org/abs/2606.05158) | 流水线相邻 Agent **步级流式**、早步可靠性 | Agent 编排研发 |
| Codex CLI | [v0.137.0 release notes](https://github.com/openai/codex/releases/tag/rust-v0.137.0) | 线程父子关系、压缩 rollout、企业用量展示 | Codex/终端 Agent 用户 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：6/4 呈现 **「超级应用记忆层升级 + 商业消息渠道开放 Agent + 多 Agent 通信范式创新」**——OpenAI 用 Dreaming 把个性化从「显式记住」推进到「后台策展」；Apple/Poke 验证 **消息即 Agent 运行时**；论文侧 **StreamMA** 证明多 Agent 不必等完整 CoT 链结束再传递。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 记忆架构 | **Dreaming V3** 独立可扩展合成 | 长周期 Agent 应区分 **episodic log** vs **curated memory state** |
| 入口整合 | **Poke** on **Messages for Business** | B2C Agent 可优先适配 **iMessage/SMS** 而非独立 App |
| 多 Agent | **StreamMA** 步级 streaming | 下游 Agent 只吃 **高置信 early steps** 可降 token 与错误传播 |
| Codex | **0.137.0** + 配额重置 | outage 后 batch 需 **幂等**；关注 **parent_thread_id** 做会话树 |
| 专项空窗 | Claude Code/OpenClaw/Hermes/Spring AI 无 6/4 官方 release | 跟进 **6/2–6/3** Build/OpenAI 周发布即可 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **OpenAI Dreaming** | 2026 大规模个性化记忆的官方架构叙事 |
| 必读 | **StreamMA（2606.05158）** | 多 Agent **延迟与准确率**同时优化的可形式化框架 |
| 推荐 | **TechCrunch：Poke × Apple Messages** | 理解 **WWDC 前** 商业 Agent 通道策略 |
| 推荐 | **The Verge：Amazon Proteus NL** | 具身/物流 Agent 从 **专用软件** 到 **自然语言派工** |
| 延伸 | **Biodefense action plan** | 生命科学 AI 的 **防御方能力** 与治理边界 |

### 来源清单

- 检索范围：2026-06-04 00:00:00 到 2026-06-04 23:59:59（Asia/Shanghai）
- 引用域名：openai.com, help.openai.com, developers.openai.com, techcrunch.com, theverge.com, community.openai.com, github.com, arxiv.org, huggingface.co, blog.google, thehindubusinessline.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 官方发布 | Dreaming memory | 2026-06-04 | https://openai.com/index/chatgpt-memory-dreaming/ |
| 官方发布 | Biodefense in the Intelligence Age | 2026-06-04 | https://openai.com/index/biodefense-in-the-intelligence-age/ |
| 开发者文档 | API Changelog Jun 4 moderation | 2026-06-04 | https://developers.openai.com/api/docs/changelog |
| 产品说明 | ChatGPT Release Notes Jun 4 | 2026-06-04 | https://help.openai.com/en/articles/6825453-chatgpt-release-notes |
| 技术媒体 | Apple approves Poke agent | 2026-06-04 | https://techcrunch.com/2026/06/04/apple-approves-poke-as-the-first-ai-agent-on-its-messages-for-business-platform/ |
| 技术媒体 | Chesky AI lab | 2026-06-04 | https://techcrunch.com/2026/06/04/airbnbs-brian-chesky-plans-to-launch-a-new-ai-lab/ |
| 技术媒体 | Meta tent data centers | 2026-06-04 | https://techcrunch.com/2026/06/04/meta-steals-a-tactic-from-tesla-and-builds-data-centers-in-tents/ |
| 技术媒体 | Amazon Proteus NL | 2026-06-04 | https://www.theverge.com/ai-artificial-intelligence/942884/amazon-next-generation-warehouse-robot-proteus |
| 市场数据 | ChatGPT 1B MAU report | 2026-06-04 | https://www.thehindubusinessline.com/news/chatgpt-app-crosses-1-billion-monthly-active-users-in-3-years-of-launch-india-20-of-this-user-base/article71061550.ece |
| 开源发布 | Codex rust-v0.137.0 | 2026-06-04 | https://github.com/openai/codex/releases/tag/rust-v0.137.0 |
| 运维 | Codex quota reset thread | 2026-06-04 | https://community.openai.com/t/questions-about-an-unexpected-codex-usage-reset-and-new-quota-period/1382610 |
| 论文原文 | StreamMA | 2026-06-03（提交） | https://arxiv.org/abs/2606.05158 |
| 官方投资者材料 | Alphabet June 2026 presentation | 2026-06-03（相邻日期/中国时间窗口传播） | https://blog.google/alphabet/investor-presentation-june-2026/ |

## 2026-06-03

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
| 论文原文 | MeDxAgent | 2026-06-03 | https://arxiv.org/html/2606.03416v1 |

## 2026-06-02

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
| 技术媒体 | Gemini Spark review | 2026-06-02 | https://www.theverge.com/ai-artificial-intelligence/941388/gemini-spark-ai-agent-trip-planning |

## 2026-06-01

### 今日总览

**一句话结论**：`2026-06-01`（Asia/Shanghai）是 **「Anthropic 抢跑 IPO 保密申报 + Copilot/Codex 计费切换生效日 + 开源 Agent 栈小版本」**——**Anthropic** 于当日向 SEC **保密提交 Form S-1**（估值语境约 **$965B**）；**GitHub Copilot PRU→AI Credits** 与 **OpenAI Codex Pro 2x promo 截止** 均在 **6/1** 起改变开发者成本模型；**OpenAI Codex `rust-v0.136.0`** 与 **LangGraph SDK `0.4.1`** 同日发布；监管/产业侧 **佛罗里达州起诉 OpenAI**、**FTC 深化微软云/AI 反垄断调查**、**Nvidia RTX Spark** 消费级 AI PC 芯片亮相。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | Anthropic/OpenAI 官方与监管；GitHub Copilot/Codex 定价；LangGraph/Codex GitHub release；The Verge/TechCrunch/CNBC；NIST/DoD 政策语境；Claude Code/Codex/OpenClaw/Hermes/Spring AI/skills 专项；中文补充 |
| 核心趋势 | **资本侧**：Anthropic **保密 IPO** 抢在 OpenAI/SpaceX 窗口前占位；**工程侧**：**6/1 双计费切换** 迫使团队建立 **token/credits guard**；**产品侧**：**Microsoft Build** 周预热 **MAI-Thinking-1** 与 **Copilot super app**；**硬件侧**：**RTX Spark** 统一内存面向 **本地 Agent** |
| 可直接关注 | **Copilot 管理员** 核对 **AI Credits** 与 org promo；**Codex Pro** 用户确认 **6/1 起配额倍数**；跟踪 **Anthropic S-1** 后续公开招股书时间节点；评估 **Codex 0.136.0**（OSC8 链接、rmcp 1.7.0）与 **langgraph-sdk 0.4.1**（v3 streaming）升级 |
| 专项检索结论 | **Claude Code**：**无 2026-06-01 新 release**（最近 **`v2.1.154` 为 2026-05-28**）；**Codex**：**`rust-v0.136.0` `Published: 2026-06-01T17:49:22Z`**；**OpenClaw/Hermes**：**无 6/1 新 release**（生态报道延续 **Hermes 日 token 领先** 叙事，非当日官方发布）；**Spring AI**：**无 6/1 官方 release/博文**；**skills**：**无重大官方 skills 发布**，社区聚焦 **Agent Skills 人机交互 spec** 讨论 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| Anthropic / IPO | [Anthropic confidentially submits draft S-1 to the SEC](https://www.anthropic.com/news/confidential-draft-s1-sec) | **2026-06-01** | 官方发布 | **保密申报** 开启上市路径；股数/定价未定；与 **$965B 估值**、**Claude Code** 企业叙事联动 |
| 监管 / OpenAI | [Florida sues OpenAI over user safety（The Verge）](https://www.theverge.com/ai-artificial-intelligence/940978/florida-is-suing-openai-over-user-safety-concerns) | **2026-06-01** | 政策/诉讼 | 州 AG 指控 **ChatGPT 安全与成瘾风险**；寻求 **民事处罚与法院命令**（刑事调查进行中） |
| GitHub Copilot / 计费 | [Copilot usage-based billing 生效（6/1）](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/) | **2026-06-01 起** | 官方政策 | **PRU 结束** → **AI Credits（1 credit=$0.01）**；Chat/Agent/Code Review **按 token** |
| OpenAI / Codex 配额 | [Codex Pricing — Pro 2x promo 截止 2026-05-31](https://developers.openai.com/codex/pricing) | **2026-06-01 起恢复标准倍数** | 官方定价 | **Pro $100**：有效 **5h 限额从 2x→标准**；长时 cloud task 需重算预算 |
| 开源 / Codex CLI | [openai/codex `rust-v0.136.0`](https://github.com/openai/codex/releases/tag/rust-v0.136.0) | **`Published: 2026-06-01T17:49:22Z`** | 开源发布 | **OSC 8 超链接**、markdown 表格 KV 渲染、**rmcp 1.7.0**、远程 exec-server **API-key 注册** |
| LangGraph / SDK | [langgraph-sdk==0.4.1](https://github.com/langchain-ai/langgraph/releases/tag/sdk%3D%3D0.4.1) | **`Published: 2026-06-01T15:23:38Z`** | 开源发布 | **v3 streaming** 解码器、`RemoteGraph` v3、**tools_agent** 无状态修复 |
| Microsoft / Build 预热 | [Microsoft Build：MAI-Thinking-1 与 Copilot super app（The Verge）](https://www.theverge.com/report/940861/microsoft-build-ai-models-windows-dev-mode-what-to-expect) | **2026-06-01** 报道 | 技术媒体 | **首个自研 reasoning 模型**（非蒸馏）；**Windows 11 开发者优化体验**；Copilot **super app 仍为 mockup** |
| 反垄断 / 云+AI | [FTC 深化微软云与 AI 竞争调查（The Verge）](https://www.theverge.com/policy/940220/microsoft-ftc-antitrust-investigation-cloud-ai) | **2026-06-01** | 政策监管 | CID 聚焦 **Azure 排他**、**AI 捆绑** 与 **M365+AI 搭售** 潜在违法风险 |
| 硬件 / 边缘 AI | [Nvidia RTX Spark 消费级 AI PC 芯片（The Verge）](https://www.theverge.com/tech/940589/nvidia-rtx-spark-n1-n1x-laptop-desktop-pc-cpu-gpu-ai-release-date) | **2026-06-01** | 产品发布 | **GB10 家族** 进笔记本/迷你 PC；**128GB 统一内存** 支撑 **120B 级本地 Agent**；Build 周将演示 **OpenShell + Windows 安全 containment** |
| 媒体 / IPO 语境 | [Anthropic files to go public（TechCrunch）](https://techcrunch.com/2026/06/01/anthropic-files-to-go-public/) | **2026-06-01** | 技术媒体 | 与 OpenAI **IPO 竞速**、SpaceX **6/12** 窗口形成 **2026 超级上市季** |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| Copilot 6/1 迁移 | [Usage-based billing 官方文 + Docs](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises) | AI Credits、token 计价、Business/Enterprise **6–8 月 promo credits** | Copilot 管理员 |
| Codex 配额与升级 | [OpenAI Codex Pricing](https://developers.openai.com/codex/pricing) + [v0.136.0 changelog](https://github.com/openai/codex/releases/tag/rust-v0.136.0) | **6/1 配额恢复**、MCP/rmcp、TUI 渲染 | Codex CLI 重度用户 |
| LangGraph 流式 | [langgraph-sdk 0.4.1 release](https://github.com/langchain-ai/langgraph/releases/tag/sdk%3D%3D0.4.1) | **stream v3**、`interleave_projections` | LangGraph 平台/SDK 集成方 |
| Anthropic 上市文件 | [Anthropic S-1 保密申报公告](https://www.anthropic.com/news/confidential-draft-s1-sec) | Rule 135、SEC 审查流程 | 关注 **AI 上市公司治理** 的研发/投资读者 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：Agent 工程在 **6/1** 呈现 **「商业计费落地 + 开源 SDK 跟进」**——Copilot/Codex **同日切换** 把 **长时 Agent 会话** 推入 **可计量成本** 时代；LangGraph **SDK 0.4.1** 继续铺 **v3 事件流** 基建，与 **Google Antigravity / Gemini Spark**（Build 周）的 **常驻 Agent** 叙事形成对照。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 计费范式 | **Copilot credits + Codex 标准配额 6/1 生效** | 为 **multi-agent 并行** 设 **per-session cap**；Completions 仍免费可作 **轻量补位** |
| Codex 运行时 | **0.136.0** 强化 TUI/MCP | **OSC8** 与 **表格 KV 渲染** 改善 **终端 Agent UX**；升级前测 **rmcp 1.7.0** 兼容性 |
| LangGraph SDK | **0.4.1 + v3 streaming** | 迁移 **`astream_events(version="v3")`** 前对齐 **RemoteGraph** 与 **messages 投影** |
| OpenClaw vs Hermes | **无 6/1 release**；生态 **token 用量榜** 持续发酵 | 选型看 **Skill 治理（OpenClaw）** vs **自进化 skills（Hermes）** 与 **CVE/审计** 风险，非单日版本 |
| Spring AI | **无 6/1 官方更新** | 继续关注 **2.0.0-M6+ MCP 注解** 与 **1.1.7** 稳定线，勿将社区博文当作官方 release |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **Anthropic 保密 S-1 官方公告** | 理解 **2026 AI 超级 IPO 季** 的第一张多米诺 |
| 必读 | **GitHub Copilot + OpenAI Codex 6/1 计费文档** | 直接影响 **团队 Agent 预算与选型** |
| 推荐 | **Codex 0.136.0 + langgraph-sdk 0.4.1** | 当日 **可核验** 的两条 **开源工程 changelog** |
| 推荐 | **The Verge：Microsoft Build / FTC Microsoft** | **企业 reasoning 模型** 与 **云+AI 反垄断** 并行升温 |
| 延伸 | **Nvidia RTX Spark** | **本地 120B Agent** 与 **Windows containment** 的硬件前提 |

### 来源清单

- 检索范围：2026-06-01 00:00:00 到 2026-06-01 23:59:59（Asia/Shanghai）
- 引用域名：anthropic.com, theverge.com, techcrunch.com, cnbc.com, github.blog, docs.github.com, developers.openai.com, github.com, nist.gov（相邻）, meritalk.com（相邻）
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 官方发布 | Anthropic 保密提交 S-1 | 2026-06-01 | https://www.anthropic.com/news/confidential-draft-s1-sec |
| 技术媒体 | Florida 起诉 OpenAI | 2026-06-01 | https://www.theverge.com/ai-artificial-intelligence/940978/florida-is-suing-openai-over-user-safety-concerns |
| 技术媒体 | Anthropic IPO（TechCrunch） | 2026-06-01 | https://techcrunch.com/2026/06/01/anthropic-files-to-go-public/ |
| 官方政策 | GitHub Copilot usage-based billing 生效 | 2026-06-01 | https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/ |
| 官方定价 | OpenAI Codex promo 截止后配额 | 2026-06-01 起 | https://developers.openai.com/codex/pricing |
| 开源发布 | openai/codex rust-v0.136.0 | 2026-06-01 | https://github.com/openai/codex/releases/tag/rust-v0.136.0 |
| 开源发布 | langgraph-sdk 0.4.1 | 2026-06-01 | https://github.com/langchain-ai/langgraph/releases/tag/sdk%3D%3D0.4.1 |
| 技术媒体 | Microsoft Build 预热 | 2026-06-01 | https://www.theverge.com/report/940861/microsoft-build-ai-models-windows-dev-mode-what-to-expect |
| 技术媒体 | FTC 微软云/AI 调查 | 2026-06-01 | https://www.theverge.com/policy/940220/microsoft-ftc-antitrust-investigation-cloud-ai |
| 技术媒体 | Nvidia RTX Spark | 2026-06-01 | https://www.theverge.com/tech/940589/nvidia-rtx-spark-n1-n1x-laptop-desktop-pc-cpu-gpu-ai-release-date |

## 2026-05-31

### 今日总览

**一句话结论**：`2026-05-31`（Asia/Shanghai）是 **「Coding Agent 计费范式集中切换前夜 + 欧洲 AI 基建大单 + OpenClaw Skill 治理 beta」**——**OpenAI Codex Pro 2x 用量 promo** 与 **GitHub Copilot PRU 时代** 均在 **6/1 零点** 结束/切换；**SoftBank** 在 Choose France 峰会宣布 **€75B / 5GW 法国 AI 数据中心**；**OpenClaw `v2026.5.31-beta.1`** 上线 **Skill Workshop** 治理流；**Tempus Lens** 下一代 **agentic 肿瘤研发平台** 同日发布；社会侧 **KC Green/Artisan 和解** 与 **Erin Brockovich 数据中心透明度地图** 持续发酵。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | OpenAI Codex 官方定价；GitHub Copilot 官方博客/docs；SoftBank 新闻稿；OpenClaw GitHub；Tempus/BusinessWire；TechCrunch；Samsung HBM 产业报道；arXiv Agent 安全/RL；Claude Code/Codex/OpenClaw/Hermes/Spring AI/skills 专项；中文补充 |
| 核心趋势 | **6/1 双切换**：Copilot **PRU→AI Credits/token**、Codex Pro **2x→标准配额** 同日生效，长时 Agent 会话 **成本模型** 成为开发者焦点；**欧洲 AI 主权基建**（SoftBank 法国 5GW）与 **HBM4E 样片** 强化 **算力/存储供给链**；**OpenClaw Skill Workshop** 把 **skills 创建/审批/回滚** 产品化 |
| 可直接关注 | **Copilot/Codex 用户** 在 **6/1 前** 核对 Billing Preview 与 Codex Profiles 用量；评估 **OpenClaw 2026.5.31-beta.1** 的 **Skill Workshop + Codex 媒体异步** 修复；跟踪 **SoftBank×Schneider Electric×EDF** 法国集群 **2031 3.1GW** 落地节奏 |
| 专项检索结论 | **Claude Code**：**无 2026-05-31 新 GitHub release**（最近 **`v2.1.158` 为 `2026-05-30`**）；**Codex**：**无新 release**，但 **Pro $100 2x 用量 promo 截止 `2026-05-31`**（官方 pricing FAQ）；**OpenClaw**：**`v2026.5.31-beta.1`** **`Published: 2026-05-31T17:44:50Z` → `2026-06-01 01:44:50（Asia/Shanghai）`（相邻日期/跨时区）** + 同日 **`2026.5.30-beta.1`**；**Hermes**：**无 2026-05-31 新 release**；**Spring AI**：**未见 5/31 官方博文/release**；**skills**：**OpenClaw Skill Workshop**（`skill_workshop` 工具 + 提案审批流）为当日最可核验 skills 进展 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| GitHub Copilot / 计费切换 | [GitHub Copilot usage-based billing 官方说明](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/) | 官方 **2026-04-27**；**2026-05-31** 为 PRU 最后一日（**6/1 生效**） | 官方政策 | **PRU→AI Credits**（1 credit=$0.01）；**Completions/Next Edit 仍免费**；**Chat/Agent/Code Review 按 token**；Business/Enterprise **6–8 月促销 credits** |
| OpenAI / Codex 配额 | [Codex Pricing — Pro 2x promo 至 2026-05-31](https://developers.openai.com/codex/pricing) | **`Ends: 2026-05-31`**（Asia/Shanghai 6/1 起恢复标准倍数） | 官方定价 | **Pro $100**：2x→标准 **5x Plus**；**Pro $200**：**25x 五小时限额** 恢复 **20x**；团队应重新评估 **长时 cloud task** 预算 |
| SoftBank / AI 基建 | [SoftBank 法国 5GW AI 数据中心 €75B](https://group.softbank/en/news/press/20260531_0) | 新闻稿 **`May 31, 2026`**（巴黎活动 **`May 30, 2026` 当地**） | 官方发布 | **2031 年前 Hauts-de-France 3.1GW**；与 **Schneider Electric** 共建 Dunkirk **预制电力模块 + 机柜制造** 产业集群 |
| OpenClaw / 开源 | [openclaw/openclaw `v2026.5.31-beta.1`](https://github.com/openclaw/openclaw/releases/tag/v2026.5.31-beta.1) | GitHub **`Published: 2026-05-31T17:44:50Z` → `2026-06-01 01:44:50（Asia/Shanghai）`（相邻日期/跨时区）** | 开源预发布 | **Skill Workshop**（提案/审批/隔离/回滚）；**Codex 异步媒体** 不中断 turn；**`@openclaw/copilot` 插件** 外置 |
| 医疗 AI / Agent | [Tempus Lens 下一代 agentic 平台（BusinessWire）](https://www.businesswire.com/news/home/20260531652876/en/) | **`05/31/2026 08:00`**（媒体转述） | 产品发布 | **肿瘤药物研发 agentic AI**：多模态 RWD + foundation models + **validated AI agents**；**19/20 顶级药企** 已采用 |
| 硬件 / HBM | [Samsung 首批 HBM4E 样片出货（5/31 产业报道）](https://finance.biggo.com/news/yUgufZ4BtCxy99G5fQf9) | **`Published: 2026-05-31T08:37:39Z` → `2026-05-31 16:37:39（Asia/Shanghai）`** | 产业/硬件 | **7 代 HBM4E** 提前 **>半年** 送样；面向 **Nvidia Vera Rubin Ultra**；**16 Gbps / 48GB / 3.6TB/s** |
| AI 版权 / 创业 | [TechCrunch：KC Green 与 Artisan AI 达成和解](https://techcrunch.com/2026/05/31/this-is-fine-artist-kc-green-reaches-agreement-with-ai-startup-artisan/) | **`May 31, 2026 11:28 AM PDT` → `2026-06-01 02:28（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | **「This is fine」** 梗图被 AI 营销挪用引发争议；**和解后撤广告/撤帖**——Agent 创业 **IP 合规** 警示案例 |
| 治理 / 基建透明度 | [TechCrunch：Erin Brockovich 质疑数据中心 secrecy](https://techcrunch.com/2026/05/31/erin-brockovich-takes-aim-at-data-center-secrecy/) | **`May 31, 2026 2:05 PM PDT` → `2026-06-01 05:05（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体/政策 | **4000+ 社区提交** 构建全美数据中心地图；**透明度** 成 AI 基建扩张 **首要关切**（非 blanket 反 AI） |
| AI 安全 / 社会 | [TechCrunch：AI psychosis 辩论解读](https://techcrunch.com/2026/05/31/making-sense-of-the-debate-over-ai-psychosis/) | **`May 31, 2026 8:30 AM PDT` → `2026-05-31 23:30（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | **Box CEO Aaron Levie** 指 **「CEO 层 AI psychosis」**——强调 **亲自用工具** 而非只看 slide 定战略 |
| 论文 / Agent RL | [AXPO: Agent Explorative Policy Optimization（arXiv:2605.28774）](https://arxiv.org/abs/2605.28774) | arXiv **`Submitted 27 May 2026`**（**5/31 中国时间窗口传播**） | 论文原文 | 解决 **Thinking-Acting Gap**：工具调用 **all-wrong rollout** 时 **重采样 tool call**；8B **Pass@4 超 32B Base** |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| Copilot 6/1 迁移 | [Usage-based billing 官方文 + GitHub Docs](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises) | AI Credits、token 计价、**6–8 月 Business/Enterprise promo** | Copilot 管理员/重度 Agent 用户 |
| Codex 配额切换 | [OpenAI Codex Pricing FAQ](https://developers.openai.com/codex/pricing) | **Pro 2x promo 截止 5/31**、Profiles 用量可视化 | ChatGPT Pro + Codex 用户 |
| OpenClaw Skill Workshop | [OpenClaw v2026.5.31-beta.1 Release Notes](https://github.com/openclaw/openclaw/releases/tag/v2026.5.31-beta.1) | `skill_workshop` 工具、提案审批、support files 扫描 | 自托管 OpenClaw + Codex 团队 |
| Agent RL 训练 | [AXPO arXiv 论文](https://arxiv.org/abs/2605.28774) | tool-call resampling、uncertainty prefix selection | 多模态 Agent 训练工程师 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：Agent 工程在 **5/31** 进入 **「计费切换 + Skill 治理」** 双线——商业侧 **Copilot/Codex 同时收紧 promo** 迫使团队建立 **token budget guard**；开源侧 **OpenClaw Skill Workshop** 把 **skills 生命周期**（创建→审批→隔离→回滚）做成 **一等公民**，与 **Claude/Cursor marketplace skills** 形成不同治理哲学。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| Coding Agent 计费 | **Copilot 6/1 + Codex promo 截止 5/31** | 为 **multi-hour agent 会话** 设 **spending cap**；Completions 仍免费可作 **轻量补位** |
| Skill 治理 | **OpenClaw Skill Workshop beta** | **提案式 skills** + **scanner/hash/rollback** 比「直接写 SKILL.md」更适合 **团队/企业 Gateway** |
| Codex 可靠性 | **OpenClaw 2026.5.31** Codex fixes | **session lock / compaction / 异步媒体** 是 **Codex app-server 生产化** 的关键修复面 |
| Agent RL | **AXPO 论文** | **工具调用 token** 需要 **定向探索** 而非纯 GRPO——对 **VLM+tools** 微调有参考价值 |
| Agent 安全 | **Lacuna（arXiv:2605.28617，相邻传播）** | **typed program holes** 把 **LLM 写代码** 约束在 **编译期 capability tracking** 内 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **GitHub Copilot usage-based billing + Docs** | **6/1 起** 必须理解的 **AI Credits** 与 **无 fallback** 规则 |
| 必读 | **OpenAI Codex Pricing（promo 截止说明）** | **Pro 用户** 6/1 起 **有效配额减半** 的直接影响 |
| 推荐 | **OpenClaw 2026.5.31-beta.1 + Skill Workshop 文档** | 当前 **skills 治理 + Codex 集成** 最完整 changelog |
| 推荐 | **SoftBank 法国 5GW 官方新闻稿** | **欧洲 AI 基建** 地缘布局与 **Schneider/EDF 工业配套** |
| 延伸 | **AXPO arXiv 论文** | **Agentic RL** 中 **tool-use 探索** 的可复现方法 |

### 来源清单

- 检索范围：2026-05-31 00:00:00 到 2026-05-31 23:59:59（Asia/Shanghai）
- 引用域名：github.blog, docs.github.com, developers.openai.com, group.softbank, github.com, businesswire.com, techcrunch.com, arxiv.org, finance.biggo.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 官方政策 | GitHub Copilot usage-based billing（6/1 生效） | 2026-04-27 宣布；5/31 窗口 | https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/ |
| 官方定价 | OpenAI Codex Pro 2x promo 截止 | Ends 2026-05-31 | https://developers.openai.com/codex/pricing |
| 官方发布 | SoftBank 法国 5GW AI DC | 2026-05-31（巴黎 May 30 当地） | https://group.softbank/en/news/press/20260531_0 |
| 开源发布 | OpenClaw v2026.5.31-beta.1 | 2026-05-31（GitHub UTC，Asia/Shanghai 跨日） | https://github.com/openclaw/openclaw/releases/tag/v2026.5.31-beta.1 |
| 产品发布 | Tempus Lens next-generation | 2026-05-31 | https://www.businesswire.com/news/home/20260531652876/en/ |
| 技术媒体 | TechCrunch KC Green/Artisan | 2026-05-31 | https://techcrunch.com/2026/05/31/this-is-fine-artist-kc-green-reaches-agreement-with-ai-startup-artisan/ |
| 技术媒体 | TechCrunch Erin Brockovich 数据中心 | 2026-05-31 | https://techcrunch.com/2026/05/31/erin-brockovich-takes-aim-at-data-center-secrecy/ |
| 技术媒体 | TechCrunch AI psychosis 辩论 | 2026-05-31 | https://techcrunch.com/2026/05/31/making-sense-of-the-debate-over-ai-psychosis/ |
| 论文原文 | AXPO arXiv:2605.28774 | 相邻日期/中国时间窗口传播 | https://arxiv.org/abs/2605.28774 |
| 产业/硬件 | Samsung HBM4E 样片报道 | 2026-05-31 | https://finance.biggo.com/news/yUgufZ4BtCxy99G5fQf9 |

## 2026-05-30

### 今日总览

**一句话结论**：`2026-05-30`（Asia/Shanghai）主线是 **「云端常驻 Agent 产品化 + 开源 Agent 栈加固 + Copilot 计费范式切换」**——**Google Gemini Spark** 在美向 **AI Ultra** 用户开放 **24/7 云端 Agent**（**Gemini 3.5 Flash + Antigravity**）；**OpenClaw `v2026.5.28`** 同日发布并强化 **Codex/Copilot Agent 运行时**；**Claude Code `v2.1.158`** 把 **Auto mode** 带到 **Bedrock/Vertex/Foundry**；**GitHub Copilot** 因 **6 月 1 日 token 计费** 引发开发者强烈反弹；**Anthropic $65B / $965B 估值** 与 **戴尔 AI 服务器 +757%** 在当日媒体窗口持续发酵。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | Google/DeepMind；OpenClaw/Claude Code GitHub；GitHub Copilot 官方博客；TechCrunch/VentureBeat；arXiv/HF；Spring AI/spring.io 核验；Claude Code/Codex/OpenClaw/Hermes/Spring AI/skills 专项；中文补充 |
| 核心趋势 | **云端 VM Agent**（Spark）与 **本地 Gateway Agent**（OpenClaw）形成对照——前者强调 **Workspace 原生 + 关盖继续跑**；**Copilot 从 PRU 切到 AI Credits/token** 标志 coding agent 进入 **按量付费** 阶段；**OpenClaw 大版本** 集中修复 **Codex session/lock/compaction** 可靠性 |
| 可直接关注 | 评估 **Gemini Spark Skills/Schedules** 能否替代部分 **Cron + MCP** 办公自动化；Windows/macOS **OpenClaw 2026.5.28** 升级验证 **Codex Supervisor + Copilot agent runtime**；**Copilot 用户** 在 **6/1 前** 用 Billing Preview 估算 token 账单；**Claude Code 多云** 团队启用 **`CLAUDE_CODE_ENABLE_AUTO_MODE=1`** |
| 专项检索结论 | **Claude Code**：**`v2.1.158`** **`Published: 2026-05-30T02:42:16Z` → `2026-05-30 10:42:16（Asia/Shanghai）`**——Bedrock/Vertex/Foundry **Auto mode**（Opus 4.7/4.8）；**Codex**：**无 2026-05-30 新 release**（桌面 **v26.527** 为 **`2026-05-29`**）；**OpenClaw**：**`v2026.5.28`** **`Published: 2026-05-30T20:06:10Z` → `2026-05-31 04:06:10（Asia/Shanghai）`（相邻日期/跨时区）** + 同日 **`2026.5.30-beta.1`**；**Hermes**：**无 2026-05-30 新 release**（最近 **`v2026.5.29.2` 为 `2026-05-29`**）；**Spring AI**：**未见 2026-05-30 官方博文/release**（spring.io 最近仍为 **1.1.1 / 2.0.0-M8 预发布**）；**skills**：**无独立 marketplace 发布**；Spark 文档已出现 **Skills/Schedules** 工作流概念 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| Google / Agent 产品 | [Gemini Spark 正式可用（PCMag / Google 支持文档）](https://support.google.com/gemini/answer/17094196?hl=en) | **2026-05-30**（PCMag **Updated May 30, 2026**；I/O 后 **5/29 起** 向 AI Ultra 美区 rollout） | 产品发布 | **24/7 云端 VM Agent**：Gmail/Calendar/Docs/Sheets/Slides + Connected Apps + 远程浏览器；**Gemini 3.5 Flash + Antigravity**；需 **Google AI Ultra（$100/月档）** 与美区 18+ |
| Google / 产品评测 | [TechCrunch：Gemini Spark 实测](https://techcrunch.com/2026/05/30/i-put-googles-24-7-ai-assistant-gemini-spark-to-work-and-its-actually-pretty-useful/) | **`May 30, 2026 8:30 AM PDT` → `2026-05-30 23:30（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | 对比 **OpenClaw 需保持设备唤醒**；指出 **Keep 未集成、iPhone 无法直达 Spark** 等产品缺口 |
| OpenClaw / 开源 | [openclaw/openclaw `v2026.5.28`](https://github.com/openclaw/openclaw/releases/tag/v2026.5.28) | GitHub **`Published: 2026-05-30T20:06:10Z` → `2026-05-31 04:06:10（Asia/Shanghai）`（相邻日期/跨时区）** | 开源发布 | **Codex/Copilot agent runtime**、**Codex Supervisor plugin**、**Claude Opus 4.8** 支持；大量 **session lock / compaction / hook relay** 修复 |
| Claude Code | [anthropics/claude-code `v2.1.158`](https://github.com/anthropics/claude-code/releases/tag/v2.1.158) | GitHub **`Published: 2026-05-30T02:42:16Z` → `2026-05-30 10:42:16（Asia/Shanghai）`** | 开源发布 | **`CLAUDE_CODE_ENABLE_AUTO_MODE=1`** 在 **Bedrock/Vertex/Foundry** 启用 **Auto mode**（Opus 4.7/4.8） |
| GitHub Copilot / 计费 | [GitHub Copilot is moving to usage-based billing](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/) | 官方 **2026-04-27** 宣布；**2026-05-30** 媒体集中讨论 **6/1 生效** | 官方政策 | **PRU → GitHub AI Credits**；按 **input/output/cached tokens** 计费；**Pro $10 / Pro+ $39** 含等额 credits；**Business/Enterprise 6–8 月促销 credits** |
| GitHub Copilot / 社区 | [TechCrunch：Copilot token 计费引开发者不满](https://techcrunch.com/2026/05/30/what-a-joke-github-copilots-new-token-based-billing-spurs-consternation-among-devs/) | **`May 30, 2026 9:30 AM PDT` → `2026-05-30 00:30（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | 社区担心 **长时 agent 会话** 账单暴涨；反映 **「鼓励重度 agent 使用 → 按 token 收费」** 张力 |
| Meta / 硬件 | [Meta is reportedly developing an AI pendant（TechCrunch）](https://techcrunch.com/2026/05/30/meta-is-reportedly-developing-an-ai-pendant/) | **`May 30, 2026 8:59 AM PDT` → `2026-05-30 23:59（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | 基于 **Limitless 收购** 的 **AI 吊坠** 内测计划；同步 **Wearables for Work** 订阅与 AI 眼镜扩展 |
| 基础设施 | [SoftBank €75B 法国数据中心（TechCrunch）](https://techcrunch.com/2026/05/30/softbank-says-it-will-invest-up-to-e75-billion-to-build-french-data-centers/) | **`May 30, 2026 2:45 PM PDT` → `2026-05-31 05:45（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | 规划 **5GW** 容量、**2031 年前 3.1GW** 落地 Hauts-de-France；SoftBank 称 **欧洲最大 AI 基建投资** |
| 资本 / Anthropic | [Anthropic Series H $65B @ $965B（官方）](https://www.anthropic.com/news/series-h) | 官方 **`2026-05-28`**；**2026-05-30** 全球媒体持续报道 | 官方发布/资本 | **Samsung/SK Hynix/Micron** 等 **存储巨头** 入局；**ARR >$47B**；估值 **首超 OpenAI（$852B）** |
| 硬件 / 财报 | [戴尔 AI 服务器收入 +757%（5/29 财报，5/30 报道）](https://developer.aliyun.com/article/1738694) | 财报 **2026-05-29**；中文社区 **2026-05-30** 转述 | 财报/媒体 | **AI 服务器 $16.1B/季、同比 +757%**；FY 指引 **$500B→$600B**；印证 **推理/训练采购** 仍在爆发 |
| 产业 / 中国 | [2026 世界智能产业博览会天津（5/28–31，5/30 报道）](https://developer.aliyun.com/article/1738694) | 展会 **2026-05-28 至 2026-05-31**；**2026-05-30** 中文简报 | 产业活动 | **40+ 大模型、740+ 机构** 展示 **制造/物流/座舱/鉴别** 等落地 |
| 论文 / RAG | [LLM-Wiki: Retrieval as Reasoning（arXiv:2605.25480）](https://arxiv.org/abs/2605.25480) | arXiv **2605.25480**（相邻日期/中国时间窗口传播） | 论文原文 | **腾讯 WeChat** 提出 **Wiki 编译 + Error Book 自校正** 的 **Agent-native RAG**；HotpotQA/MuSiQue 等 **+2.0–8.1 F1** |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| Gemini Spark | [Find & manage Gemini Spark tasks](https://support.google.com/gemini/answer/17094196?hl=en) | Tasks/Schedules/Skills、Workspace 集成、Activity 删除策略 | 评估 **云端常驻办公 Agent** 的团队 |
| OpenClaw 升级 | [OpenClaw v2026.5.28 Release Notes](https://github.com/openclaw/openclaw/releases/tag/v2026.5.28) | Codex Supervisor、Copilot agent runtime、session lock 修复 | 自托管 **OpenClaw + Codex** 运维 |
| Claude Code 多云 | [Claude Code v2.1.158](https://github.com/anthropics/claude-code/releases/tag/v2.1.158) | **`CLAUDE_CODE_ENABLE_AUTO_MODE=1`** on Bedrock/Vertex/Foundry | 企业 **Claude Code 多云** 部署 |
| Copilot 计费迁移 | [Usage-based billing 官方说明](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/) | AI Credits、token 计价、annual plan 过渡 | Copilot **Pro/Business** 管理员 |
| Agent-native RAG | [LLM-Wiki 论文](https://arxiv.org/abs/2605.25480) | Wiki 编译、link-following tools、Error Book | RAG/Agent 架构师 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：Agent 工程在 **「云端编排（Spark） vs 本地 Gateway（OpenClaw）」** 两线并进——Google 把 **Skills + Schedules + Workspace** 打包成 **Ultra 订阅卖点**；OpenClaw 则通过 **`2026.5.28`** 把 **Codex/Copilot runtime 可靠性** 推到生产级；与此同时 **Copilot token 计费** 迫使团队重新评估 **长时 agent 任务** 的 **成本模型**。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 云端常驻 Agent | **Gemini Spark GA（美区 Ultra）** | **VM 后台执行** 可替代部分 **Cron + 本地 OpenClaw** 场景，但 **vendor lock-in** 更高 |
| Gateway 可靠性 | **OpenClaw 2026.5.28** | **session lock / compaction / hook relay** 是 **multi-agent + Codex** 生产化的真正门槛 |
| Coding Agent 计费 | **Copilot 6/1 token 计费** | 团队应为 **agent 会话** 设 **budget guard + model tier**；Completions/Next Edit 仍 **不扣 credits** |
| Agent-native RAG | **LLM-Wiki 论文** | 把 KB **编译为可遍历 Wiki** 比 **flat chunk + embedding** 更适配 **ReAct 工具环** |
| MCP 生态 | **Langfuse MCP 5/29 更新**（相邻日期） | 观测/评分/评论进 MCP——**Agent 可观测性** 继续 MCP 化 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **OpenClaw v2026.5.28 Release Notes** | 当前 **Codex + Copilot agent runtime** 最完整的变更清单 |
| 必读 | **GitHub Copilot usage-based billing 官方文** | **6/1 前** 必须理解的 **AI Credits/token** 规则 |
| 推荐 | **Gemini Spark Google 支持文档 + TechCrunch 实测** | 理解 **云端 Agent** 的能力边界与 **Workspace 集成深度** |
| 推荐 | **LLM-Wiki arXiv 论文** | **Retrieval-as-Reasoning** 的可复现架构参考 |
| 延伸 | **SoftBank 法国 5GW 数据中心公告** | **欧洲 AI 算力** 地缘布局与 **能源/电网** 约束 |

### 来源清单

- 检索范围：2026-05-30 00:00:00 到 2026-05-30 23:59:59（Asia/Shanghai）
- 引用域名：support.google.com, techcrunch.com, github.com, github.blog, anthropic.com, arxiv.org, developer.aliyun.com, pcmag.com, thenextweb.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 官方发布/产品 | Gemini Spark Tasks 管理文档 | 2026-05-30（文档随 rollout 更新） | https://support.google.com/gemini/answer/17094196 |
| 开源发布 | OpenClaw v2026.5.28 | 2026-05-30（GitHub UTC，Asia/Shanghai 跨日） | https://github.com/openclaw/openclaw/releases/tag/v2026.5.28 |
| 开源发布 | Claude Code v2.1.158 | 2026-05-30 | https://github.com/anthropics/claude-code/releases/tag/v2.1.158 |
| 官方政策 | GitHub Copilot usage-based billing | 2026-04-27（5/30 媒体窗口） | https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/ |
| 技术媒体 | TechCrunch Gemini Spark 实测 | 2026-05-30 | https://techcrunch.com/2026/05/30/i-put-googles-24-7-ai-assistant-gemini-spark-to-work-and-its-actually-pretty-useful/ |
| 技术媒体 | TechCrunch Copilot token 计费争议 | 2026-05-30 | https://techcrunch.com/2026/05/30/what-a-joke-github-copilots-new-token-based-billing-spurs-consternation-among-devs/ |
| 技术媒体 | TechCrunch Meta AI pendant | 2026-05-30 | https://techcrunch.com/2026/05/30/meta-is-reportedly-developing-an-ai-pendant/ |
| 技术媒体 | TechCrunch SoftBank 法国数据中心 | 2026-05-30 | https://techcrunch.com/2026/05/30/softbank-says-it-will-invest-up-to-e75-billion-to-build-french-data-centers/ |
| 官方发布/资本 | Anthropic Series H | 2026-05-28（5/30 传播） | https://www.anthropic.com/news/series-h |
| 论文原文 | LLM-Wiki arXiv:2605.25480 | 相邻日期/中国时间窗口传播 | https://arxiv.org/abs/2605.25480 |
| 中文补充 | 阿里云社区 5/30 AI 简报 | 2026-05-30 | https://developer.aliyun.com/article/1738694 |

## 2026-05-29

### 今日总览

**一句话结论**：`2026-05-29`（Asia/Shanghai）主线是 **「防御加速 + 评测治理 + Windows Codex 平台化 + 企业 Agent 出海」**——**OpenAI** 同日连发 **Rosalind Biodefense / GPT‑Rosalind 可信访问** 与 **第三方评测 Playbook**；**Codex v26.527** 把 **Computer Use 与移动端远程控制** 带到 **Windows**；**Anthropic** 在 **Claude Platform on AWS** 上线 **Managed Agents webhooks / 多 Agent 编排 / 自托管沙箱**；**Hermes Agent v0.15.1** 同日热修；**腾讯 Cloud Day 香港** 向全球推出 **WorkBuddy / Miora / TokenHub** 企业 Agent 栈。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | OpenAI/Anthropic 官方；Codex/Hermes GitHub；TechCrunch/VentureBeat；arXiv/HF；Spring AI/spring.io 核验；Claude Code/Codex/OpenClaw/Hermes/Spring AI/skills 专项；中文补充 |
| 核心趋势 | **生物防御加速（Rosalind）** 与 **评测 harness 公开化** 并行；**Codex Windows Computer Use** 补齐跨平台 Agent 桌面能力；**企业 Agent 瓶颈从模型转向权限/编排/可靠性**（Workday/VentureBeat）；**记忆/推理基础设施** 受资本关注（XCENA） |
| 可直接关注 | 生物/公卫团队申请 **Rosalind Biodefense / GPT‑Rosalind**；安全/评测团队读 **Third-Party Eval Playbook** 对齐 harness 披露；Windows 开发者升级 **Codex 26.527** 验证 Computer Use；Java 团队仍以 **spring.io M7** 为准、勿信第三方 GA 传言 |
| 专项检索结论 | **Claude Code**：**无 2026-05-29 新 GitHub tag**（最近 **`v2.1.154`** 为 **`2026-05-28`**）；**Codex**：**`v26.527`** **`2026-05-29`** 官方推文/Changelog——**Windows Computer Use + ChatGPT 移动端远程 Windows**；**OpenClaw**：**无 2026-05-29 新 release**（最近 **`v2026.5.27`** 为 **`2026-05-28`**）；**Hermes**：**`v2026.5.29` / v0.15.1** **`Published: 2026-05-29T01:12:15Z` → `2026-05-29 09:12:15（Asia/Shanghai）`**；**Spring AI**：**未见 2.0 GA 官方博文**（spring.io 最近 **`2.0.0-M7` 为 `2026-05-23`**，文档仍标 *in development*）；**skills**：**无独立 marketplace 发布**；Hermes 热修纳入 **19,932 条 skills.sh 全量目录** |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| OpenAI / 生物防御 | [Strengthening societal resilience with Rosalind Biodefense](https://openai.com/index/strengthening-societal-resilience-with-rosalind-biodefense/) | **2026-05-29** | 官方发布 | 启动 **Rosalind Biodefense** 赞助可信开发者；向美/盟政府伙伴扩展 **GPT‑Rosalind** 访问——**防御加速（defensive acceleration）** 样板 |
| OpenAI / 评测治理 | [A shared playbook for trustworthy third party evaluations](https://openai.com/index/trustworthy-third-party-evaluations-foundations/) | **2026-05-29** | 官方发布 | 强调 **harness 选择 + validity checks**（reward hacking/contamination/sandbagging）——第三方 frontier 评测披露模板 |
| OpenAI / 企业落地 | [Boston Children's uses AI to unlock new diagnoses](https://openai.com/index/boston-childrens-hospital/) | **2026-05-29** | 官方案例 | 企业 **ChatGPT 层** + **50+ 自动化**；**40+ 罕见病新诊断**、**~60,000 小时** 节省——医疗 Agent 基础设施化参考 |
| OpenAI / Codex 案例 | [How Braintrust turns customer requests into code with Codex](https://openai.com/index/braintrust/) | **2026-05-29** | 官方案例 | 客户请求→代码的 **Codex 生产闭环** 实践 |
| Codex / Windows | [OpenAI Codex v26.527 — Windows Computer Use & mobile remote（Neowin）](https://www.neowin.net/news/openai-rolls-out-major-codex-for-windows-update-with-computer-use-and-mobile-access/) | **`May 29, 2026`**（OpenAI 官方 X **`10:41 AM · May 29, 2026`**） | 产品更新 | **Windows 前台 Computer Use**；**ChatGPT iOS/Android 或 Mac Codex 远程启动/审批 Windows 任务**；Profile 展示 token 统计 |
| Anthropic / AWS 平台 | [Claude Platform API Release Notes — May 29, 2026](https://docs.anthropic.com/en/release-notes/api) | **2026-05-29** | 官方文档 | **Claude Managed Agents webhooks、multiagent orchestration、self-hosted sandboxes** 在 **Claude Platform on AWS** GA；新增 IAM actions 与 **`AnthropicSelfHostedEnvironmentAccess`** 策略 |
| Hermes | [NousResearch/hermes-agent `v2026.5.29`](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.5.29) | GitHub **`Published: 2026-05-29T01:12:15Z` → `2026-05-29 09:12:15（Asia/Shanghai）`** | 开源发布 | **v0.15.1 热修**：修复 loopback **dashboard 401 无限 reload**；Docker **`HERMES_DASHBOARD_INSECURE=1` 显式 opt-in**；**skills.sh 全量 19,932 条** |
| 企业 Agent / 腾讯 | [Tencent launches WorkBuddy for global users（TechNode）](https://technode.com/2026/05/29/tencent-launches-workbuddy-productivity-ai-agent-for-global-users/) | **`May 29, 2026`**（PR **`HONG KONG, May 29, 2026`**） | 官方产品/媒体 | **WorkBuddy** 全球发布：并行多 Agent、**MCP 接 GitHub/Jira/Notion**、IM 远程（Slack/Telegram/Discord/WeChat）；同场还有 **Miora** 创意工作室与 **TokenHub MaaS** |
| 资本 / Agent | [Cognition's Scott Wu: AI coding agents shouldn't replace humans（TechCrunch）](https://techcrunch.com/2026/05/29/cognitions-scott-wu-says-ai-coding-agents-shouldnt-replace-humans/) | **`May 29, 2026 9:13 AM PDT` → `2026-05-30 00:13（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | **Devin** 定位 **L3–L4 维护/迁移** 而非替代；**$1B @ $26B** 融资背景 |
| 基础设施 / 芯片 | [XCENA $135M at $570M valuation（TechCrunch）](https://techcrunch.com/2026/05/29/xcena-secures-135m-at-570m-valuation-betting-on-memory-as-ais-real-bottleneck/) | **`May 29, 2026 5:00 AM PDT` → `2026-05-29 20:00（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | **近内存计算 MX1（CXL）** 押注推理 **memory scaling** 瓶颈 |
| 运营事件 | [OpenAI widespread outage（News9live）](https://www.news9live.com/technology/artificial-intelligence/openai-down-chatgpt-api-dall-e-sora-and-login-hit-by-widespread-outage-2975319) | **2026-05-29** | 运营 | **ChatGPT/API/Codex/Sora/Login** 同日大面积故障——与 Codex 大版本发布同日，需关注 status.openai.com |
| 论文 / Agent RL | [Agent Explorative Policy Optimization（arXiv:2605.28774）](https://arxiv.org/pdf/2605.28774) | 提交 **2026-05-28**（相邻日期/中国时间窗口传播） | 论文原文 | **AXPO** 用 **tool-call resampling** 缓解 multimodal agentic RL 的 **Thinking-Acting Gap** |
| 开源 / 自改进 Agent | [Hexo Labs open-sources SIA（MarkTechPost）](https://www.marktechpost.com/2026/05/29/hexo-labs-open-sources-sia-a-self-improving-agent-that-updates-both-the-harness-and-the-model-weights/) | **2026-05-29** | 开源/媒体 | **SIA** 同时更新 **harness + LoRA 权重** 的自改进闭环（MIT，`hexo-ai/sia`） |
| 教育 / 政策合作 | [Armenia × OpenAI Education for Countries](https://edunewsletter.openai.com/p/armenias-next-step-toward-ai-native) | **2026-05-29** | 官方通讯 | **5 万** 师生/研究者获得 frontier AI 工具访问——国家级 AI-native 教育样板 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| 生物防御 | [Rosalind Biodefense 公告](https://openai.com/index/strengthening-societal-resilience-with-rosalind-biodefense/) | GPT‑Rosalind、trusted access、Fourth Eon/LLNL/CEPI 首批伙伴 | 公卫/生物信息/合规团队 |
| 评测治理 | [Third-Party Eval Playbook](https://openai.com/index/trustworthy-third-party-evaluations-foundations/) | harness 文档化、validity checks、agentic 任务披露 | AI 安全/评测工程师 |
| Codex Windows | [Neowin：Codex 26.527](https://www.neowin.net/news/openai-rolls-out-major-codex-for-windows-update-with-computer-use-and-mobile-access/) | 前台 Computer Use、移动端 remote control、Profile token stats | Windows 开发/Agent 运维 |
| AWS Managed Agents | [Anthropic API Release Notes](https://docs.anthropic.com/en/release-notes/api) | webhooks、multiagent orchestration、self-hosted sandboxes IAM | 在 AWS 上跑 Claude Agent 的团队 |
| Hermes 热修 | [Hermes v2026.5.29 Release](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.5.29) | dashboard 401 loop、Docker insecure opt-in、skills.sh 全量 | 自托管 Hermes 运维 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：Agent 工程在 **「评测可审计 + 平台跨端 + 编排可靠性」** 三线推进——OpenAI 把 **harness** 推到评测标准中心；Codex 把 **桌面 Computer Use** 扩展到 Windows 并与移动端组成 **跨设备控制面**；VentureBeat 当日两篇指出企业 Agent 进入 **rebuild era**，瓶颈是 **权限/状态恢复/编排** 而非单点模型分数。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 评测 harness | OpenAI **Third-Party Eval Playbook** | 对外 benchmark 必须披露 **工具访问、采样、重试、validity checks**；否则 scores 不可比 |
| 跨平台 Codex | **Windows 26.527 Computer Use + mobile remote** | Agent 桌面能力需规划 **前台/后台** 差异（Windows 仅前台）；移动端作 **审批/steer 控制面** |
| AWS Agent 平台 | Anthropic **Managed Agents on AWS** 能力包 | 生产 Agent 把 **webhook 编排 + 自托管沙箱** 与 **IAM 最小权限** 一起设计 |
| 企业 Agent 权限 | VentureBeat：**permissions bottleneck**（Workday Sana 案例） | Agent SOR 应绑定 **组织身份/审批模型**，避免 DIY Agent **权限过宽** |
| 可靠性重建 | VentureBeat：**rebuild era**（Temporal 观点） | 长跑 Agent 需要 ** durable workflow + 断点恢复 + 成本可观测** |
| Agent RL 研究 | **AXPO**（arXiv 2605.28774） | multimodal agent 训练需单独优化 **tool-call 探索**，而非只调 thinking tokens |
| 自改进 Agent | **SIA** 开源 | harness 与权重 **双杠杆** 自改进——适合研究型团队，生产需严格 gate |
| Hermes 运维 | **v0.15.1** 热修 | loopback dashboard 与 Docker **insecure 绑定** 是常见踩坑点；升级后验证 **skills 目录完整性** |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **OpenAI：Rosalind Biodefense + GPT‑Rosalind** | 当日 **防御加速** 最权威官方定义与申请路径 |
| 必读 | **OpenAI：Third-Party Eval Playbook** | 理解 **harness = 评测结果的一部分**——影响所有 frontier 评测设计 |
| 推荐 | **Codex 26.527 Windows + mobile** | **跨平台 Agent 桌面** 能力对齐 Mac 的关键里程碑 |
| 推荐 | **Anthropic AWS Managed Agents Release Notes** | **webhook + 多 Agent + 自托管沙箱** 的生产组合 |
| 延伸 | **Boston Children's 企业 AI 案例** | 医疗场景 **enterprise AI layer** 量化 ROI 参考 |
| 延伸 | **SIA 自改进 Agent（hexo-ai/sia）** | harness/权重双更新的研究型架构 |

### 来源清单

- 检索范围：2026-05-29 00:00:00 到 2026-05-29 23:59:59（Asia/Shanghai）
- 引用域名：openai.com, developers.openai.com, docs.anthropic.com, github.com, techcrunch.com, venturebeat.com, neowin.net, technode.com, arxiv.org, marktechpost.com, edunewsletter.openai.com, news9live.com, spring.io
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 官方发布 | Rosalind Biodefense | 2026-05-29 | https://openai.com/index/strengthening-societal-resilience-with-rosalind-biodefense/ |
| 官方发布 | Third-Party Eval Playbook | 2026-05-29 | https://openai.com/index/trustworthy-third-party-evaluations-foundations/ |
| 官方案例 | Boston Children's AI | 2026-05-29 | https://openai.com/index/boston-childrens-hospital/ |
| 官方案例 | Braintrust × Codex | 2026-05-29 | https://openai.com/index/braintrust/ |
| 官方文档 | Anthropic API Release Notes | 2026-05-29 | https://docs.anthropic.com/en/release-notes/api |
| 开源发布 | Hermes Agent v2026.5.29 | 2026-05-29 | https://github.com/NousResearch/hermes-agent/releases/tag/v2026.5.29 |
| 技术媒体 | Codex Windows 26.527 | 2026-05-29 | https://www.neowin.net/news/openai-rolls-out-major-codex-for-windows-update-with-computer-use-and-mobile-access/ |
| 技术媒体 | Tencent WorkBuddy global | 2026-05-29 | https://technode.com/2026/05/29/tencent-launches-workbuddy-productivity-ai-agent-for-global-users/ |
| 技术媒体 | Cognition Scott Wu | 2026-05-29（相邻日期/跨时区） | https://techcrunch.com/2026/05/29/cognitions-scott-wu-says-ai-coding-agents-shouldnt-replace-humans/ |
| 技术媒体 | XCENA Series B | 2026-05-29（相邻日期/跨时区） | https://techcrunch.com/2026/05/29/xcena-secures-135m-at-570m-valuation-betting-on-memory-as-ais-real-bottleneck/ |
| 技术媒体 | Agent permissions bottleneck | 2026-05-29 | https://venturebeat.com/orchestration/the-ai-agent-bottleneck-isnt-model-performance-its-permissions |
| 技术媒体 | Agent rebuild era | 2026-05-29 | https://venturebeat.com/orchestration/ai-agents-are-entering-their-rebuild-era-as-enterprises-confront-the-reliability-problem |
| 论文原文 | AXPO | 2026-05-28（相邻日期/中国时间窗口传播） | https://arxiv.org/pdf/2605.28774 |
| 开源/媒体 | SIA self-improving agent | 2026-05-29 | https://www.marktechpost.com/2026/05/29/hexo-labs-open-sources-sia-a-self-improving-agent-that-updates-both-the-harness-and-the-model-weights/ |
| 官方通讯 | Armenia Education | 2026-05-29 | https://edunewsletter.openai.com/p/armenias-next-step-toward-ai-native |

## 2026-05-28

### 今日总览

**一句话结论**：`2026-05-28`（Asia/Shanghai）主线是 **「旗舰模型 + 万亿估值 + 治理框架」同日叠加强工程 release**——**Anthropic** 连发 **Claude Opus 4.8**（**Dynamic Workflows**、**Fast mode 降价 3×**）与 **$65B Series H @ $965B**；**OpenAI** 发布 **Frontier Governance Framework** 并推 **Codex CLI 0.135.0**；**OpenClaw `v2026.5.27`** 在上海晚间发布；资本与产品侧 **Asana 收购 StackAI**、**Sesame 对话 Agent iOS** 显示 **企业 Agent 平台化** 与 **消费级语音 Agent** 并进。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | Anthropic/OpenAI 官方；OpenClaw/Codex GitHub & Changelog；TechCrunch/VentureBeat；HF Daily 2026-05-28；Spring AI GA 预期核验；Claude Code/Codex/OpenClaw/Hermes/Spring AI/skills 专项；中文补充 |
| 核心趋势 | **Opus 4.8 加速迭代**（41 天 Opus 小版本、并行 subagent 工作流）；**AI 资本格局重排**（Anthropic $965B > OpenAI $840B）；**前沿治理公开化**（OpenAI Frontier Governance ↔ CA/EU 法规）；**编码 Agent 运维增强**（Codex doctor/0.135.0、OpenClaw 安全与 Codex 集成）；**企业 human-agent 并购**（Asana×StackAI） |
| 可直接关注 | 评估 **Opus 4.8 + `/fast`** 与 **Dynamic Workflows** 对大型代码库迁移；读 **OpenAI Frontier Governance Framework** 对齐内部 AI 风险分类；升级 **Codex 0.135.0** 的 `codex doctor`/`/permissions` profile；部署 **OpenClaw 2026.5.27** 验证 Gateway/Codex 路径；Java 团队核对 **Spring AI 2.0 GA** 是否已正式发布（当日未见 spring.io GA 文） |
| 专项检索结论 | **Claude Code**：**无新 GitHub tag**（最近 **`v2.1.152`** 为 **`2026-05-27`**）；**`2026-05-28`** 官方随 Opus 4.8 发布 **Dynamic Workflows**（research preview，数百并行 subagent）；**Codex**：**`Codex CLI 0.135.0`** 官方 Changelog **`2026-05-28`**（GitHub **无稳定 `rust-v0.135.0` tag**，仅 alpha）；**OpenClaw**：**`v2026.5.27`** **`Published: 2026-05-28T11:41:42Z` → `2026-05-28 19:41:42（Asia/Shanghai）`**；**Hermes**：未发现 **`2026-05-28`** 新 tag（最近 **`v0.13.0`** 为 **`2026-05-07`**）；**Spring AI**：**未见 `2.0.0` GA 官方博文**（spring.io 最近 **`2.0.0-M7` 为 `2026-05-23`**，文档仍标 *in development*）；**skills**：**无独立 marketplace 发布**；随 Opus 4.8 的 **effort 控制 / API system entries** 属模型与 harness 能力更新 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| Anthropic / 模型 | [Introducing Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8) | **2026-05-28** | 官方发布 | 同价升级；**诚实度/不确定性标注** 提升；**effort 控制**；**Dynamic Workflows**；**fast mode $10/$50**（较 4.7 fast 降 3×）；API **`claude-opus-4-8`** |
| Anthropic / 资本 | [Anthropic raises $65B Series H at $965B](https://www.anthropic.com/news/series-h) | **2026-05-28** | 官方公告 | **ARR ~$47B**；含 **$15B hyperscaler**（Amazon **$5B**）；算力协议（Amazon/Google/SpaceX）支撑 Claude 规模 |
| Anthropic / Agent | [Opus 4.8 + Dynamic Workflows（TechCrunch）](https://techcrunch.com/2026/05/28/anthropic-releases-opus-4-8-with-new-dynamic-workflow-tool/) | **`May 28, 2026 10:00 AM PDT` → `2026-05-29 01:00（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | 代码库级迁移：**数百并行 subagent** + 输出校验；Mythos 类模型 **数周内** 可能更广开放 |
| OpenAI / 治理 | [OpenAI’s Frontier Governance Framework](https://openai.com/index/openai-frontier-governance-framework/) | **2026-05-28** | 官方发布 | 将 **Preparedness Framework** 映射到 **加州 Transparency in Frontier AI Act**、**EU GPAI Code of Practice**；覆盖 cyber/CBRN/操纵/失控等 |
| Codex | [Codex CLI 0.135.0（OpenAI Developers Changelog）](https://developers.openai.com/codex/changelog) | **2026-05-28** | 官方发布 | **`codex doctor`** 增强诊断；**`/status` 远程连接**；**vim 模式** 与 **`/permissions` named profiles**；**Python SDK Sandbox presets** |
| OpenClaw | [openclaw/openclaw `v2026.5.27`](https://github.com/openclaw/openclaw/releases/tag/v2026.5.27) | GitHub **`Published: 2026-05-28T11:41:42Z` → `2026-05-28 19:41:42（Asia/Shanghai）`** | 开源发布 | **安全边界**（群组 prompt、Tailscale no-auth 拒绝）；**Codex app-server** 稳定性；**Gateway/回复路径 perf**；**Pixverse/DeepInfra** 等 provider |
| 企业 Agent | [Asana acquires StackAI ($75M)](https://techcrunch.com/2026/05/28/asana-acquires-no-code-agent-builder-stack-ai/) | **`May 28, 2026 1:06 PM PDT` → `2026-05-29 04:06（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | **human-agent 操作系统** 定位；无代码 Agent 接入 Salesforce/Slack 等 **现有企业数据面** |
| 语音 Agent | [Sesame launches iOS app](https://techcrunch.com/2026/05/28/sesame-the-conversational-ai-startup-from-oculus-founders-launches-its-ios-app/) | **`May 28, 2026 8:35 AM PDT` → `2026-05-28 23:35（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | **四角色语音 Agent**（Maya/Miles 等）；**incognito**；面向 **2027 硬件** 路线 |
| 硬件 Agent | [Vertu Alphafold + Hermes Agent](https://techcrunch.com/2026/05/28/vertu-wants-ceos-to-run-companies-from-an-ai-foldable-starting-at-6880/) | **`May 28, 2026 12:00 AM PDT` → `2026-05-28 15:00（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | 奢侈品折叠机预装 **Hermes Agent** 接 ERP/CRM——**开源 Agent 框架进入高端政企定制** 样本 |
| 平台 / 产品 | [YouTube Premium 播客 AI 推荐与 Auto speed](https://techcrunch.com/2026/05/28/youtube-adds-new-podcast-features-including-an-ai-recommendation-tool-and-auto-speed/) | **`May 28, 2026 7:28 AM PDT` → `2026-05-28 22:28（Asia/Shanghai）`（相邻日期/跨时区）** | 官方产品 | **Ask Music 式播客推荐** + **智能变速**；Premium 月 **8 亿小时** 播客收听 |
| Spring AI | [Spring AI 2.0 GA 预期（第三方，未见官方 GA）](https://byteiota.com/spring-ai-2-0-ships-may-28-java-finally-has-a-real-ai-stack/) | **计划 2026-05-28**；**官方未确认 GA** | 生态观察 | **Boot 4.0 + Java 21** 基线；**MCP annotations**；与 **Boot 3.5 EOL（2026-06-30）** 仅 **33 天** 窗口——需以 **spring.io 正式博文/Maven `2.0.0` release** 为准 |
| 论文 / Agent | [HF Daily 2026-05-28：MemTrace / SkillGrad / Agent Explorative PO 等](https://huggingface.co/papers/date/2026-05-28) | **HF Daily：2026-05-28** | 论文社区 | **MemTrace**（LLM 记忆系统错误归因）；**SkillGrad**（技能优化）；**Gamma-World**（多智能体世界模型）等当日提交簇 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| Opus 4.8 | [Claude Opus 4.8 发布公告](https://www.anthropic.com/news/claude-opus-4-8) | effort、fast mode、Dynamic Workflows、API system entries | Claude API / Claude Code 用户 |
| 前沿治理 | [OpenAI Frontier Governance Framework](https://openai.com/index/openai-frontier-governance-framework/) | Preparedness ↔ 法规映射、风险分类、事件响应 | AI 合规/安全负责人 |
| Codex 升级 | [Codex Changelog 0.135.0](https://developers.openai.com/codex/changelog) | doctor、permissions profile、vim、remote status | Codex CLI 运维 |
| OpenClaw | [OpenClaw v2026.5.27 Release](https://github.com/openclaw/openclaw/releases/tag/v2026.5.27) | 安全边界、Codex 集成、Gateway perf | 自托管 Agent 运维 |
| Spring AI 迁移 | [Spring AI 2.0 Getting Started（仍标 development）](https://docs.spring.io/spring-ai/reference/2.0/getting-started.html) | BOM `2.0.0`、Boot 4.x | Java AI 工程师（待 GA 官宣后升级） |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：Agent 工程在 **「更大规模并行编排 + 更强旗舰模型 + 更硬治理披露」** 三线同时推进——Opus 4.8 的 **Dynamic Workflows** 把 **subagent 并行** 推到代码库迁移场景；OpenClaw/Codex 继续加固 **运行时安全与诊断**；HF 当日论文簇聚焦 **记忆错误归因（MemTrace）** 与 **技能梯度优化（SkillGrad）**。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 并行 Agent 编排 | Opus 4.8 **Dynamic Workflows** | 大任务用 **计划 → 数百 subagent → 校验**；以 **现有测试套件** 作 merge bar |
| 模型性价比 | **Fast mode 3× 降价** | 延迟敏感生产流量可切 **fast**；API 需申请 waitlist |
| 治理对齐 | OpenAI **Frontier Governance Framework** | 企业可把 **内部风险台账** 对齐 **CA/EU** 披露口径 |
| Codex 可运维性 | **0.135.0 doctor + permissions profiles** | 支持案例先跑 **doctor**；权限用 **named profile** 而非散落 env |
| OpenClaw 安全 | **v2026.5.27** 群组/Tailscale/命令包装拦截 | 多通道 Agent **默认拒绝高危暴露** |
| Agent 记忆研究 | **MemTrace**（HF 2026-05-28） | 记忆系统需要 **错误 trace/归因** 而不只是检索命中率 |
| 企业落地 | Asana×StackAI | **工作管理 OS + 无代码 Agent 构建器** = 存量 SaaS 数据上的 Agent 层 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **Anthropic：Claude Opus 4.8 + Dynamic Workflows** | 当日 **最强 Agent 编码能力 + 并行工作流** 官方定义 |
| 必读 | **Anthropic：Series H $65B @ $965B** | 理解 **2026 资本与算力军备** 对模型供给的影响 |
| 推荐 | **OpenAI Frontier Governance Framework** | 前沿模型 **合规披露模板** 的参考实现 |
| 推荐 | **OpenClaw v2026.5.27 Highlights** | 上海时区 **硬对齐** 的个人 Agent 安全/性能包 |
| 延伸 | **HF Daily 2026-05-28（MemTrace / SkillGrad）** | Agent **记忆与技能** 研究前沿 |

### 来源清单

- 检索范围：2026-05-28 00:00:00 到 2026-05-28 23:59:59（Asia/Shanghai）
- 引用域名：anthropic.com, openai.com, developers.openai.com, github.com, techcrunch.com, venturebeat.com, huggingface.co, byteiota.com, spring.io
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 官方发布 | Claude Opus 4.8 | 2026-05-28 | https://www.anthropic.com/news/claude-opus-4-8 |
| 官方公告 | Anthropic Series H $65B | 2026-05-28 | https://www.anthropic.com/news/series-h |
| 官方发布 | OpenAI Frontier Governance Framework | 2026-05-28 | https://openai.com/index/openai-frontier-governance-framework/ |
| 官方发布 | Codex CLI 0.135.0 | 2026-05-28 | https://developers.openai.com/codex/changelog |
| 开源发布 | OpenClaw v2026.5.27 | 2026-05-28（Asia/Shanghai） | https://github.com/openclaw/openclaw/releases/tag/v2026.5.27 |
| 技术媒体 | Opus 4.8 Dynamic Workflows | 2026-05-28/29（跨时区） | https://techcrunch.com/2026/05/28/anthropic-releases-opus-4-8-with-new-dynamic-workflow-tool/ |
| 技术媒体 | Asana acquires StackAI | 2026-05-28/29（跨时区） | https://techcrunch.com/2026/05/28/asana-acquires-no-code-agent-builder-stack-ai/ |
| 技术媒体 | Sesame iOS Agent app | 2026-05-28/29（跨时区） | https://techcrunch.com/2026/05/28/sesame-the-conversational-ai-startup-from-oculus-founders-launches-its-ios-app/ |
| 技术媒体 | Vertu Alphafold Hermes | 2026-05-28（跨时区） | https://techcrunch.com/2026/05/28/vertu-wants-ceos-to-run-companies-from-an-ai-foldable-starting-at-6880/ |
| 技术媒体 | YouTube podcast AI features | 2026-05-28（跨时区） | https://techcrunch.com/2026/05/28/youtube-adds-new-podcast-features-including-an-ai-recommendation-tool-and-auto-speed/ |
| 论文社区 | HF Daily 2026-05-28 | 2026-05-28 | https://huggingface.co/papers/date/2026-05-28 |
| 生态观察 | Spring AI 2.0 GA 预期（未官方确认） | 2026-05-28 | https://byteiota.com/spring-ai-2-0-ships-may-28-java-finally-has-a-real-ai-stack/ |

## 2026-05-27

### 今日总览

**一句话结论**：`2026-05-27`（Asia/Shanghai）主线是 **Agent 从「能写代码」走向「能交易、能自治改进、能进企业控制面」**——**Robinhood** 开放 **MCP 驱动的 Agent 交易/虚拟卡**；**OpenAI** 发布 **Codex 自改进 Tax AI** 工程范式与 **2026 全球选举保障**；**Claude Code `v2.1.152`** 强化 **`/code-review --fix` + Skills 热重载** 并配套 **security-guidance 插件**；**OpenClaw `v2026.5.26-beta.2`** 继续 **Gateway/Transcript/渠道/观测性** 大包；资本侧 **Cognition/Devin 融资 $1B@$25B** 与 **Snowflake×AWS $6B Graviton** 显示 **编码 Agent 与 Agent 算力 CPU 层** 仍在升温。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | OpenAI/Anthropic 官方；OpenClaw/Claude Code/Codex GitHub；TechCrunch/VentureBeat；Fujitsu 企业合作；HF Papers 2026-05-27；EU AI Act 高风险指南跟进；Claude Code/Codex/OpenClaw/Hermes/Spring AI/skills 专项；中文补充 |
| 核心趋势 | **金融 Agent 基础设施化**（Robinhood MCP 交易/支付）；**生产 Agent 自改进闭环**（Codex Tax AI 25%→97%）；**编码 Agent 产品化竞争**（Claude Code review/fix + 安全插件 vs Cognition $25B）；**平台治理与选举诚信**（OpenAI 选举保障 + YouTube 自动 AI 标签）；**个人 Agent 运维 release 节奏**（OpenClaw beta.2 捆绑 Codex 0.134.0） |
| 可直接关注 | 评估 **Claude Code v2.1.152** 的 **`/code-review --fix`** 与 **`/reload-skills`**；安装 **security-guidance@claude-plugins-official** 做提交前扫描；读 **OpenAI Tax AI + Codex 有界 worktree** 设计自改进 Agent；升级 **OpenClaw v2026.5.26-beta.2** 验证 **Activity tab + Gateway perf**；企业 Agent 对照 **Merck/Mastercard「plumbing first」** 与 **Robinhood MCP** 集成模式 |
| 专项检索结论 | **Claude Code**：**`v2.1.152`** **`Published: 2026-05-27T01:30:59Z` → `2026-05-27 09:30:59（Asia/Shanghai）`**；同日 **security-guidance 插件** 全用户可用；**Codex**：**无新 CLI tag**（最近 **`rust-v0.134.0`** 为 **`2026-05-26`**）；**OpenAI 官方文** **`Building self-improving tax agents with Codex`** **`May 27, 2026`**；**OpenClaw**：**`v2026.5.26-beta.2`** **`Published: 2026-05-27T05:46:50Z` → `2026-05-27 13:46:50（Asia/Shanghai）`**（捆绑 **Codex 0.134.0**）；**Hermes**：未发现 **`2026-05-27`** 新 tag（最近 **`v2026.5.16`**）；**Spring AI**：未发现 **`2026-05-27`** release（**2.0 GA 预计 2026-05-28**）；**skills**：**Claude Code v2.1.152** 新增 **`disallowed-tools` frontmatter、`/reload-skills`、SessionStart `reloadSkills`**；**MCP 当日无新 spec release**（最近 **2026-07-28 RC 公告** 为 **`2026-05-19~22`** 窗口） |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| Claude Code | [anthropics/claude-code `v2.1.152`](https://github.com/anthropics/claude-code/releases/tag/v2.1.152) | GitHub **`Published: 2026-05-27T01:30:59Z` → `2026-05-27 09:30:59（Asia/Shanghai）`** | 开源发布 | **`/code-review --fix`** 直接改 working tree；Skills **`disallowed-tools`**；**`/reload-skills`** + SessionStart **`reloadSkills`**；**`--fallback-model`** 会话级切换 |
| Claude Code / 安全 | [security-guidance plugin for Claude Code（Cybersecurity News 跟进）](https://cybersecuritynews.com/free-security-plugin-for-claude-code/) | **`May 27, 2026`** | 官方插件/工程 | **`/plugin install security-guidance@claude-plugins-official`**；实时扫描 edits/commits；可扩展 **`.claude/security-patterns.yaml`** |
| OpenClaw | [openclaw/openclaw `v2026.5.26-beta.2`](https://github.com/openclaw/openclaw/releases/tag/v2026.5.26-beta.2) | GitHub **`Published: 2026-05-27T05:46:50Z` → `2026-05-27 13:46:50（Asia/Shanghai）`** | 开源发布 | **Gateway 启动/回复路径 perf**、**Transcript 统一路径**、**Activity tab**、**Codex CLI 0.134.0**、渠道/Talk/安全边界大批修复 |
| Codex / 企业 Agent | [Building self-improving tax agents with Codex（OpenAI）](https://openai.com/index/building-self-improving-tax-agents-with-codex/) | **`May 27, 2026`** | 官方发布 | **Thrive/Crete Tax AI**：生产轨迹 → 结构化信号 → **Codex 有界 worktree** 自改进；准确率 **25%→97%** 样本 |
| OpenAI / 治理 | [Election information and safeguards in 2026（OpenAI）](https://openai.com/index/election-safeguards-2026/) | **`May 27, 2026`** | 官方发布 | **AP 实时计票**、**Democracy Works 投票信息**、**SynthID+C2PA** 溯源、**Codex Security/TAC** 支持选举网络安全 |
| OpenAI / 开源 | [Warp's big bet on building open source with GPT-5.5（OpenAI）](https://openai.com/index/warp/) | **`May 27, 2026`** | 官方案例 | Warp 终端以 **GPT-5.5** 支撑开源构建——编码 Agent 与开源生态结合样本 |
| Anthropic / 研究 | [Coding agents in the social sciences（Anthropic）](https://www.anthropic.com/research/coding-agents-social-sciences) | **`May 27, 2026`** | 官方研究 | **1260 名量化社科研究者** 调查 + 随机实验：Coding Agent 采纳与能力自评——企业培训/治理参考 |
| 企业合作 | [Fujitsu expands AI strategy through collaborations with OpenAI and Anthropic](https://www.finanznachrichten.de/nachrichten-2026-05/68608555-fujitsu-limited-fujitsu-expands-ai-strategy-through-collaborations-with-openai-and-anthropic-008.htm) | **`May 27, 2026`** | 企业发布 | 富士通 × **Anthropic Claude FDE** + 全集团 Claude 生产力；结合 **Kozuchi/Takane** 做 AI 选型集成 |
| 编码 Agent / 资本 | [Cognition raises $1B at $25B pre-money valuation（TechCrunch）](https://techcrunch.com/2026/05/27/ai-coding-startup-cognition-raises-1b-at-25b-pre-money-valuation/) | **`May 27, 2026 9:00 AM PDT` → `2026-05-28 00:00（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | **Devin** ARR **$492M**、MoM **+50%**；独立编码 Agent 仍获顶级 VC 背书 |
| 金融 Agent | [Robinhood now lets your AI agents trade stocks（TechCrunch）](https://techcrunch.com/2026/05/27/robinhood-now-lets-your-ai-agents-trade-stocks/) | **`May 27, 2026 5:30 AM PDT` → `2026-05-27 20:30（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | **独立 Agent 钱包 + MCP 连接**；**Agentic 虚拟信用卡**；金融场景 **MCP server** 样板 |
| 平台 / 订阅 | [Meta launches subscriptions including AI plans（TechCrunch）](https://techcrunch.com/2026/05/27/meta-officially-launches-instagram-facebook-and-whatsapp-subscriptions-with-more-to-come-including-ai-plans/) | **`May 27, 2026 11:00 AM PDT` → `2026-05-28 02:00（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | **Meta One Plus/Premium** 测试更深推理与多模态生成——消费级 **AI 订阅分层** |
| 内容治理 | [YouTube will now automatically label AI videos（TechCrunch）](https://techcrunch.com/2026/05/27/youtube-will-now-automatically-label-ai-videos/) | **`May 27, 2026 6:00 AM PDT` → `2026-05-27 21:00（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | **自动检测 photorealistic AI** 并强制标签；**C2PA 元数据** 永久绑定 |
| 基础设施 | [Snowflake signs $6B deal with AWS for AI CPU chips（TechCrunch）](https://techcrunch.com/2026/05/27/in-more-good-news-for-amazon-snowflake-signs-6b-deal-with-aws-for-ai-cpu-chips/) | **`May 27, 2026 1:10 PM PDT` → `2026-05-28 04:10（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | **Cortex AI + Agent 工作负载** 推高 **Graviton CPU** 需求——Agent 时代 **CPU 层** 与 GPU 分工 |
| 搜索 / 产品 | [Why Google's AI can't spell Google（TechCrunch）](https://techcrunch.com/2026/05/27/why-googles-ai-cant-spell-google-or-anything-else/) | **`May 27, 2026 5:17 PM PDT` → `2026-05-28 08:17（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | **AI Search 拼写/计数** 持续翻车；Google 承认 **LLM 不擅长拼写**——搜索 UX 风险样本 |
| 企业 Agent | [Merck and Mastercard seeing real agentic AI results（VentureBeat）](https://venturebeat.com/infrastructure/merck-and-mastercard-are-seeing-real-agentic-ai-results-both-say-the-plumbing-came-first) | **`May 27, 2026 11:23 AM PT` → `2026-05-28 02:23（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | **Merck** 研发周期 **-33%**、合规营销 **+70~80%**；**Mastercard** 编排化争议/欺诈流程——**plumbing first** |
| 政策 | [EU AI Act high-risk draft guidelines follow-up（Hogan Lovells）](https://www.jdsupra.com/legalnews/european-commission-publishes-long-3230922/) | 指南发布 **`2026-05-19`**；跟进文 **`May 27, 2026`** | 政策标准 | **Article 6 高风险分类** 167 页草案解读；咨询至 **`2026-06-23`**；**Annex III 生效延至 2027-12-02** |
| 论文 / Agent | [MUSE-Autoskill: Self-Evolving Agents via Skill Creation（HF Daily）](https://huggingface.co/papers/date/2026-05-27) | **HF Daily：`2026-05-27`** | 论文原文 | 当日 Agent Skills 论文簇：**技能创建/记忆/管理/评测** 自进化框架 |
| 论文 / 移动 Agent | [MobileGym: Verifiable Parallel Simulation for Mobile GUI Agents（HF Daily）](https://huggingface.co/papers/date/2026-05-27) | **HF Daily：`2026-05-27`** | 论文原文 | **可验证、高并行** 移动 GUI Agent 仿真平台——Agent 评测基础设施 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| Claude Code 升级 | [Claude Code v2.1.152 Release Notes](https://github.com/anthropics/claude-code/releases/tag/v2.1.152) | `/code-review --fix`、Skills reload、fallback model | 终端编码 Agent 用户 |
| Claude Code 安全 | [security-guidance 插件安装说明](https://cybersecuritynews.com/free-security-plugin-for-claude-code/) | 插件 marketplace、patterns YAML、Agent SDK commit review | 安全左移/DevSecOps |
| Codex 自改进 Agent | [OpenAI Tax AI 工程文](https://openai.com/index/building-self-improving-tax-agents-with-codex/) | 有界 worktree、生产 trace→eval、skills/docs 注入 | 企业 Agent 平台架构师 |
| OpenClaw 升级 | [OpenClaw v2026.5.26-beta.2 Highlights](https://github.com/openclaw/openclaw/releases/tag/v2026.5.26-beta.2) | Transcript 路径、Activity tab、Gateway perf | 自托管个人 Agent 运维 |
| 选举/溯源 | [OpenAI Election Safeguards 2026](https://openai.com/index/election-safeguards-2026/) | SynthID、C2PA、AP 计票、TAC/Codex Security | AI 治理/合规负责人 |
| Spring AI 迁移 | [Spring AI 2.0 GA 倒计时（预计 5/28）](https://byteiota.com/spring-ai-2-ga-java-production-stack/) | Boot 4、Jackson 3、MCP annotations | Java AI 工程师（提前排期） |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：Agent 工程继续 **「控制面 + 工具面 + 金融/合规场景」** 三线并进——**Robinhood MCP** 把 Agent 接到 **真实资金边界**；**OpenAI Tax AI** 给出 **生产自改进** 参考架构；**Claude Code** 把 **review/fix/security/skills reload** 打成日常闭环；**OpenClaw** 维持 **高频 beta 运维 release**。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 金融 MCP | Robinhood **Agent 账户 + MCP + 虚拟卡** | Agent 接外部系统时 **预充值钱包 + 审批预览 + MCP 边界** 优于全账户授权 |
| 自改进 Agent | OpenAI **Tax AI + Codex worktree** | 用 **生产 artifact + eval + 只读上下文** 构建 **有界自改进**；避免无界 auto-patch |
| 编码 Agent 竞争 | Cognition **$25B** vs Claude Code/Codex | 独立 Agent 仍需 **企业客户 + ARR** 证明；工具链 **review/security** 成差异化 |
| Claude Code 工具链 | **v2.1.152** review/fix + security plugin | 把 **PR review → local fix → commit scan** 串成一条命令链 |
| OpenClaw 运维 | **beta.2** Gateway/Transcript/Activity | 个人 Agent 平台投资 **观测性 + transcript 一致性** 先于新渠道 |
| 企业落地 | Merck/Mastercard **plumbing first** | Agent 上线前先做 **数据/编排/治理基础设施** |
| Agent Skills 研究 | **MUSE-Autoskill**（HF 2026-05-27） | 技能 **创建-记忆-管理-评测** 应作为平台一等公民 |
| MCP 标准 | **2026-07-28 spec RC**（5/19~22 窗口） | **无状态 transport** 将改变 server 部署；提前规划 **stateless tools/call** |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **OpenAI：Building self-improving tax agents with Codex** | 当日 **最完整的生产 Agent 自改进工程文** |
| 必读 | **Claude Code v2.1.152 + security-guidance 插件** | 编码 Agent **review/fix/安全** 同日双升级 |
| 推荐 | **Robinhood MCP Agent 交易（TechCrunch）** | **MCP 进入金融交易** 的首批公开产品化样本 |
| 推荐 | **OpenClaw v2026.5.26-beta.2 Release Highlights** | 上海时区 **硬对齐** 的最大开源个人 Agent 运维包 |
| 延伸 | **Merck/Mastercard agentic AI（VentureBeat）** | 受监管行业 **Agent 落地** 的量化效果与前提 |

### 来源清单

- 检索范围：2026-05-27 00:00:00 到 2026-05-27 23:59:59（Asia/Shanghai）
- 引用域名：github.com, openai.com, anthropic.com, techcrunch.com, venturebeat.com, finanznachrichten.de, cybersecuritynews.com, huggingface.co, jdsupra.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 开源发布 | Claude Code v2.1.152 | 2026-05-27（Asia/Shanghai） | https://github.com/anthropics/claude-code/releases/tag/v2.1.152 |
| 官方插件 | security-guidance for Claude Code | 2026-05-27 | https://cybersecuritynews.com/free-security-plugin-for-claude-code/ |
| 开源发布 | OpenClaw v2026.5.26-beta.2 | 2026-05-27（Asia/Shanghai） | https://github.com/openclaw/openclaw/releases/tag/v2026.5.26-beta.2 |
| 官方发布 | Building self-improving tax agents with Codex | 2026-05-27 | https://openai.com/index/building-self-improving-tax-agents-with-codex/ |
| 官方发布 | Election safeguards 2026 | 2026-05-27 | https://openai.com/index/election-safeguards-2026/ |
| 官方发布 | Warp + GPT-5.5 open source | 2026-05-27 | https://openai.com/index/warp/ |
| 官方研究 | Coding agents in social sciences | 2026-05-27 | https://www.anthropic.com/research/coding-agents-social-sciences |
| 企业发布 | Fujitsu × OpenAI/Anthropic | 2026-05-27 | https://www.finanznachrichten.de/nachrichten-2026-05/68608555-fujitsu-limited-fujitsu-expands-ai-strategy-through-collaborations-with-openai-and-anthropic-008.htm |
| 技术媒体 | Cognition $1B@$25B | 2026-05-27/28（跨时区） | https://techcrunch.com/2026/05/27/ai-coding-startup-cognition-raises-1b-at-25b-pre-money-valuation/ |
| 技术媒体 | Robinhood Agent MCP trading | 2026-05-27/28（跨时区） | https://techcrunch.com/2026/05/27/robinhood-now-lets-your-ai-agents-trade-stocks/ |
| 技术媒体 | Meta AI subscription plans | 2026-05-27/28（跨时区） | https://techcrunch.com/2026/05/27/meta-officially-launches-instagram-facebook-and-whatsapp-subscriptions-with-more-to-come-including-ai-plans/ |
| 技术媒体 | YouTube auto AI labels | 2026-05-27/28（跨时区） | https://techcrunch.com/2026/05/27/youtube-will-now-automatically-label-ai-videos/ |
| 技术媒体 | Snowflake×AWS $6B Graviton | 2026-05-27/28（跨时区） | https://techcrunch.com/2026/05/27/in-more-good-news-for-amazon-snowflake-signs-6b-deal-with-aws-for-ai-cpu-chips/ |
| 技术媒体 | Google AI spelling（TechCrunch） | 2026-05-27/28（跨时区） | https://techcrunch.com/2026/05/27/why-googles-ai-cant-spell-google-or-anything-else/ |
| 技术媒体 | Merck/Mastercard agentic AI | 2026-05-27/28（跨时区） | https://venturebeat.com/infrastructure/merck-and-mastercard-are-seeing-real-agentic-ai-results-both-say-the-plumbing-came-first |
| 政策标准 | EU AI Act high-risk guidelines 跟进 | 2026-05-19/27 | https://www.jdsupra.com/legalnews/european-commission-publishes-long-3230922/ |
| 论文原文 | HF Daily 2026-05-27（MUSE-Autoskill 等） | 2026-05-27 | https://huggingface.co/papers/date/2026-05-27 |

## 2026-05-26

### 今日总览

**一句话结论**：`2026-05-26`（Asia/Shanghai）主线是 **「搜索入口 AI 化」引发用户用脚投票**（DuckDuckGo 安装量峰值 **+30.5%**、noai 页面 **+27.7%**）与 **Codex/OpenClaw 工程面双升级**（**Codex CLI 0.134.0** 本地历史检索 + `--profile` + MCP OAuth；**OpenClaw `v2026.5.25-beta.1`** Gateway 性能/语音/渠道/观测性大包）并行；**Skills 分发层** 出现 **Vercel `skills.sh`**（跨 **51** 个 Agent 的一键安装）；**Claude Code/Codex GitHub tag 当日无新 release**，但 **v2.1.150 远程 system prompt 注入** 在 **`2026-05-26` 窗口** 引发社区争议。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | OpenAI Codex 官方 Changelog；OpenClaw GitHub API；TechCrunch；Anthropic Status/Webinar；skills.sh/Vercel；AgentTrust/RAC 论文；Claude Code/Codex/OpenClaw/Hermes/Spring AI/skills 专项；EU/US 政策窗口；中文补充 |
| 核心趋势 | **消费者拒绝「强制 AI 搜索」**（Google I/O 后迁移 DuckDuckGo）；**编码 Agent 工具链成熟化**（Codex 历史搜索、MCP schema 可靠性）；**个人 Agent 平台运维化**（OpenClaw 可见回复延迟分离、Activity 观测、Rastermill 替代 Sharp）；**Skills npm 化**（`npx skills add` 跨 Agent 分发） |
| 可直接关注 | 评估 **Codex 0.134.0** 的 `--profile` 迁移与 **readOnly MCP 并发**；升级 **OpenClaw v2026.5.25-beta.1** 并验证 **Talk/Discord voice** 与 **Activity tab**；团队 Skills 用 **skills.sh** 统一 `.cursor`/`.claude`/`.codex` 目录；Claude Code 用户检查 **v2.1.150 bootstrap/GrowthBook** 与 `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` |
| 专项检索结论 | **Claude Code**：未发现 **`2026-05-26`** 新 tag（最近 **`v2.1.150`** 为 **`2026-05-23`**）；**`2026-05-26` 窗口** HN 热议 **v2.1.150 远程 system prompt 注入**（`api.anthropic.com/api/claude_cli/bootstrap` + GrowthBook `tengu_heron_brook`）；**Codex**：**`Codex CLI 0.134.0`** 官方 Changelog **`2026-05-26`**（GitHub rust release tag 未同步）；**OpenClaw**：**`v2026.5.25-beta.1`** **`Published: 2026-05-26T09:41:10Z` → `2026-05-26 17:41:10（Asia/Shanghai）`**（**`v2026.5.26-beta.1`** 为 **`21:10 UTC` → `2026-05-27 05:10` 上海，属邻近日期）；**Hermes**：未发现 **`2026-05-26`** 新 tag（最近 **`v2026.5.16`**）；**Spring AI**：未发现 **`2026-05-26`** release（**2.0 GA 预计 2026-05-28**）；**skills**：**skills.sh**（**`26 May, 2026`** 深度文）+ **find-skills** 等 leaderboard 生态 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| Codex | [Codex CLI 0.134.0（OpenAI Developers Changelog）](https://developers.openai.com/codex/changelog) | **`2026-05-26`** | 官方发布 | **本地会话历史搜索**（含预览）、**`--profile` 主选择器**、**MCP per-server env + OAuth**、**readOnly MCP 并发**、connector schema `$ref` 保留 |
| OpenClaw | [openclaw/openclaw `v2026.5.25-beta.1`](https://github.com/openclaw/openclaw/releases/tag/v2026.5.25-beta.1) | GitHub **`Published: 2026-05-26T09:41:10Z` → `2026-05-26 17:41:10（Asia/Shanghai）`** | 开源发布 | **可见回复延迟分离**、Gateway 热路径缓存、**Talk/Discord voice 可 inspect/steer**、**Activity tab**、**Rastermill 替代 Sharp**、多频道生产化修复 |
| 搜索 / 产品 | [DuckDuckGo installs up 30% as users reject Google AI Search（TechCrunch）](https://techcrunch.com/2026/05/26/duckduckgo-installs-are-up-30-as-users-reject-being-force-fed-googles-ai-search/) | **`May 26, 2026 3:32 PM PDT` → `2026-05-27 06:32（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | Google I/O 后 **AI 搜索改造** 引发反弹；DDG 美国安装 **WoW +18.1% 均值、峰值 +30.5%（5/25）**；**noai.duckduckgo.com** 访问 **峰值 +27.7%** |
| 版权 / 平台 | [UMG and TikTok renew agreement to combat unauthorized AI music（TechCrunch）](https://techcrunch.com/2026/05/26/universal-music-group-and-tiktok-renew-agreement-to-combat-unauthorized-ai-music/) | **`May 26, 2026 7:55 AM PDT` → `2026-05-26 22:55（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | 续约承诺 **下架未授权 AI 生成音乐**、改进署名——平台 **AI 音乐治理** 与 **EU 合成内容标注** 压力共振 |
| Anthropic / 产品 | [Claude Mythos 1 商用准备（媒体跟进 Glasswing）](https://gbhackers.com/anthropic-prepares-claude-mythos-through-claude-code/) | **`May 26, 2026`（第三方报道）** | 技术媒体 | 代码/界面出现 **`claude-mythos-1-preview`**；拟接入 **Claude Code** 与 **Claude Security** 平台——需以 Anthropic 官方为准 |
| Anthropic / 活动 | [How an Anthropic sales leader runs his week with Cowork（Webinar）](https://www.anthropic.com/webinars/how-anthropics-sales-leader-runs-his-week-with-claude) | **`May 26, 2026 10:00 am`** | 官方活动 | Cowork 在 **Salesforce + BigQuery** 场景下的 **forecast/overnight 4k 账户 评分** 实践样本 |
| 平台可靠性 | [Claude Status: Elevated errors for Claude Code in Slack](https://status.anthropic.com/) | **事件：`2026-05-26 01:56–05:19 UTC` → `2026-05-26 09:56–13:19（Asia/Shanghai）`；Resolved `05:19 UTC`** | 官方状态 | Slack 集成 **Claude Code 错误率升高** 约 3.5 小时后恢复 |
| Skills 生态 | [skills.sh: Vercel building the npm for Agent Skills](https://www.ailinklab.com/en/opensource/skills-ecosystem/) | **`26 May, 2026`** | 社区/工程 | **`npx skills add`** 支持 **51** 个 Agent；**agentskills.io** 开放格式 + **leaderboard 发现**；**find-skills** 等 **41 万+** 累计安装 |
| Claude Code / 治理 | [HN: Claude Code v2.1.150 remote system prompt injection](https://news.ycombinator.com/item?id=48259288) | **`2026-05-26` 讨论窗口**（v2.1.150 发布于 **`2026-05-23`**） | 社区 | **`bootstrap` API + GrowthBook `tengu_heron_brook`（60s 刷新）** 可向本地 CLI 注入 system prompt 片段；缓解：`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` |
| Agent 安全 | [AgentTrust: Runtime Safety for AI Agent Tool Use（arXiv 2605.04785）](https://arxiv.org/html/2605.04785v1) | **May 2026 论文**（ACM CAIS 会议 **`2026-05-26–29`** 窗口） | 论文原文 | **MCP 兼容** 工具执行拦截；**95% verdict / 0.3ms 级延迟**（生产 ruleset）；shell 去混淆 + **RiskChain** |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| Codex 升级 | [Codex Changelog 2026-05-26](https://developers.openai.com/codex/changelog) | 历史搜索、`--profile`、MCP OAuth、extension hook 上下文 | Codex CLI 日常用户 |
| OpenClaw 升级 | [OpenClaw Releases（v2026.5.25-beta.1 要点）](https://github.com/openclaw/openclaw/releases) | 回复路径 perf、Transcripts、Diagnostics/OTel、移动端 Talk | 自托管个人 Agent 运维 |
| Skills 分发 | [skills.sh 官网 + vercel-labs/skills](https://skills.sh) | `npx skills add owner/repo --skill name`、telemetry 可关 | 多 Agent 团队标准化 |
| Agent 工具安全 | [AgentTrust 论文 + AGPL 实现](https://arxiv.org/html/2605.04785v1) | allow/warn/block/review、SafeFix、shell 规范化 | 企业 MCP/Agent 安全架构师 |
| Spring AI 迁移 | [Spring AI 2.0 GA 倒计时（预计 5/28）](https://byteiota.com/spring-ai-2-ga-java-production-stack/) | Boot 4 硬依赖、Jackson 3、MCP-first | Java AI 工程师（提前排期） |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：Agent 工程继续从「能跑」走向「可运维、可分发、可治理」——**OpenClaw** 把 **延迟、观测、渠道、语音** 打成运维 release；**Codex** 强化 **profile/MCP/历史检索**；**skills.sh** 把 Skills 变成 **跨 Agent 包管理**；安全侧 **AgentTrust** 给出 **亚毫秒级工具拦截** 参考实现。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 搜索 UX 反弹 | Google AI Search → DuckDuckGo 迁移 | 产品侧需保留 **「纯链接/无 AI」** 路径；企业内网搜索同理 |
| Codex 工具链 | **0.134.0** history search + MCP | 长会话 Agent 必备 **本地检索**；MCP 侧区分 **readOnly 并发** 与 OAuth |
| 个人 Agent 运维 | OpenClaw **v2026.5.25-beta.1** | 投资 **Activity/OTel/secret-prep traces**；语音场景验证 **steer/cancel** |
| Skills 供应链 | **skills.sh** 跨 51 Agent | 内部规范用 **SKILL.md + Git repo + `npx skills add`**，避免每 Agent 手抄 |
| Claude Code 治理 | v2.1.150 远程 prompt 注入争议 | 企业部署需审计 **bootstrap/flags**；必要时 **DISABLE_NONESSENTIAL_TRAFFIC** |
| Agent 工具安全 | AgentTrust **MCP 网关** | 在 MCP 与工具之间加 **策略层**（非仅靠模型自律） |
| 补偿事务 | RAC（LangGraph/CrewAI 可插拔） | 长时程 Agent 用 **日志 + LIFO rollback** 替代纯 LLM「想想怎么撤销」 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **Codex CLI 0.134.0 官方 Changelog** | 当日 **唯一硬对齐 OpenAI 编码 Agent 正式发布** |
| 必读 | **OpenClaw v2026.5.25-beta.1 Release Highlights** | 当日 **上海时区硬对齐** 的最大开源个人 Agent 运维包 |
| 推荐 | **TechCrunch：DuckDuckGo vs Google AI Search** | **C 端对「强制 AI 搜索」** 的量化反弹样本 |
| 推荐 | **skills.sh 生态深度文（2026-05-26）** | Skills 从文件拷贝升级为 **包管理 + 发现层** |
| 延伸 | **HN：Claude Code v2.1.150 远程 prompt** | 评估 **本地 CLI 是否应允许厂商动态注入 system 段** |

### 来源清单

- 检索范围：2026-05-26 00:00:00 到 2026-05-26 23:59:59（Asia/Shanghai）
- 引用域名：developers.openai.com, github.com, techcrunch.com, anthropic.com, status.anthropic.com, ailinklab.com, skills.sh, arxiv.org, news.ycombinator.com, gbhackers.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 官方发布 | Codex CLI 0.134.0 | 2026-05-26 | https://developers.openai.com/codex/changelog |
| 开源发布 | OpenClaw v2026.5.25-beta.1 | 2026-05-26（Asia/Shanghai） | https://github.com/openclaw/openclaw/releases/tag/v2026.5.25-beta.1 |
| 技术媒体 | DuckDuckGo 安装激增（TechCrunch） | 2026-05-26/27（跨时区） | https://techcrunch.com/2026/05/26/duckduckgo-installs-are-up-30-as-users-reject-being-force-fed-googles-ai-search/ |
| 技术媒体 | UMG×TikTok AI 音乐治理（TechCrunch） | 2026-05-26/27（跨时区） | https://techcrunch.com/2026/05/26/universal-music-group-and-tiktok-renew-agreement-to-combat-unauthorized-ai-music/ |
| 技术媒体 | Claude Mythos 1 准备（GBHackers） | 2026-05-26 | https://gbhackers.com/anthropic-prepares-claude-mythos-through-claude-code/ |
| 官方活动 | Anthropic Cowork Webinar | 2026-05-26 | https://www.anthropic.com/webinars/how-anthropics-sales-leader-runs-his-week-with-claude |
| 官方状态 | Claude Code in Slack 事件 | 2026-05-26 | https://status.anthropic.com/ |
| 社区工程 | skills.sh 生态文 | 2026-05-26 | https://www.ailinklab.com/en/opensource/skills-ecosystem/ |
| 社区 | HN Claude Code v2.1.150 prompt 注入 | 2026-05-26 窗口 | https://news.ycombinator.com/item?id=48259288 |
| 论文原文 | AgentTrust | 2026-05（会议 05-26 起） | https://arxiv.org/html/2605.04785v1 |

## 2026-05-25

### 今日总览

**一句话结论**：`2026-05-25`（Asia/Shanghai）主线是 **AI 治理从「技术圈讨论」升格为「全球公共议题」**——教宗 Leo XIV 发布首份 AI 教谕 **Magnifica Humanitas** 并在梵蒂冈与 **Anthropic 联创 Chris Olah** 同台发布；**OpenAI** 同日宣布巴西首家媒体合作（Folha/UOL）；企业侧 **ClickUp 以 22% 裁员 + ~3000 内部 Agent** 诠释「100x org」叙事；工程侧 **OpenClaw `v2026.5.24-beta.2`** 在当日窗口发布（Gateway 性能/Meeting Notes/子 Agent 上下文收口）；**Claude Code/Codex/Hermes/Spring AI 当日无新官方 release**，**Agent Skills** 则以 Hugging Face 当日论文簇（SkillOpt、From Raw Experience to Skill Consumption）与 Cursor Skills 注入 bug 讨论延续。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | OpenAI/Anthropic/Vatican 官方；OpenClaw GitHub；TechCrunch；Hugging Face Papers；Claude Code/Codex/OpenClaw/Hermes/Spring AI/skills 专项；EU/US 政策窗口；中文补充 |
| 核心趋势 | **AI 治理公共化**（教谕 + Olah 同台 + 「disarm AI」话语）；**媒体/API 生态扩张**（OpenAI 巴西合作 + Codex/Enterprise/API 接入）；**Agent 组织重构**（ClickUp 内部 3000 Agent + 百万美元薪酬带）；**个人 Agent 平台迭代**（OpenClaw beta.2 性能/Meeting Notes）；**Skills 研究化**（自进化 Skill 优化与经验→Skill 消费链路） |
| 可直接关注 | 阅读 **Magnifica Humanitas** 全文与 Olah 讲稿对照企业 AI 治理；评估 **OpenClaw v2026.5.24-beta.2** Gateway 热路径与 Meeting Notes 插件；跟踪 **Spring AI 2.0 GA（预计 5/28）** 与 Boot 4 迁移窗口；用 HF 当日 **SkillOpt / Skill Consumption** 论文设计 Skills 评测与归档 |
| 专项检索结论 | **Claude Code**：未发现 **`2026-05-25`** 新 tag（最近 **`v2.1.146`** 为 **`2026-05-21`**）；**Codex**：未发现 **`2026-05-25`** 新 release（最近 **`rust-v0.134.0-alpha.1`** 为 **`2026-05-22`**）；**OpenClaw**：**`v2026.5.24-beta.2`** **`Published: 2026-05-24T23:49:30Z` → `2026-05-25 07:49:30（Asia/Shanghai）`**；**Hermes**：未发现 **`2026-05-25`** 新 tag（最近 **`v2026.5.16`** 为 **`2026-05-16`**）；**Spring AI**：未发现 **`2026-05-25`** 硬对齐 release（**2.0 GA 预计 2026-05-28**，当前最新里程碑 **`v2.0.0-M7`** 为 **`2026-05-22`**）；**skills/Cursor Skills**：HF **`2026-05-25`** 出现 **SkillOpt / From Raw Experience to Skill Consumption** 等 Agent Skills 论文；Cursor 社区 **`2026-05-25` 窗口** 报告 **`.agents/skills` 发现正常但 system prompt 注入失败** |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| AI 治理 / 教谕 | [Magnifica Humanitas: On safeguarding the human person in the time of artificial Intelligence（Vatican）](https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260525-enciclica-magnifica-humanitas.html) | **梵蒂冈发布：`2026-05-25`** | 政策/标准 | 首份以 AI 为核心议题的教谕；强调 **human dignity、劳动、民主、战争/自主武器**；提出 **「disarm AI」** 话语——技术权力须服从共同善与有效监督 |
| Anthropic / 治理 | [Anthropic co-founder Chris Olah's remarks on Pope Leo XIV's encyclical](https://www.anthropic.com/news/chris-olah-pope-leo-encyclical) | **`May 25, 2026`** | 官方发布 | Olah 承认 frontier lab **激励结构** 与「做对的事」可能冲突；呼吁 **外部监督/批评者**；提出 **全球贫困、人类 flourishing、模型 interpretability** 三问——研发组织应纳入 humanities/宗教/哲学对话 |
| OpenAI / 媒体 | [OpenAI, Grupo Folha, and Grupo UOL announce strategic content partnership](https://openai.com/index/grupo-folha-grupo-uol-partnership/) | **`May 25, 2026`** | 官方发布 | OpenAI **巴西首家媒体合作**；ChatGPT 展示 Folha/UOL 摘要并链回原文；合作方还可接入 **Codex、ChatGPT Enterprise、API** 探索新闻产品与内部工作流 |
| 企业 Agent / 组织 | [What ClickUp's mass layoff tells us about the future of work（TechCrunch）](https://techcrunch.com/2026/05/25/what-clickups-mass-layoff-tells-us-about-the-future-of-work/) | **`May 25, 2026 9:00 AM PDT` → `2026-05-26 00:00（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | CEO 将 **22% 裁员** 框为 **AI 转型** 而非单纯降本；称已部署 **~3000 内部 AI Agent**、员工转向 **指挥 Agent + 审阅输出**；计划 **百万美元薪酬带** 与对外产品化 Agent 效率指标 |
| AI 治理 / 媒体 | [The pope's AI encyclical isn't really about AI（TechCrunch）](https://techcrunch.com/2026/05/25/the-popes-ai-encyclical-isnt-really-about-ai/) | **`May 25, 2026 8:09 AM PDT` → `2026-05-25 23:09（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | 解读教谕核心：**权力集中、不平等、民主侵蚀、AI 军备竞赛**；并提及 **Trump 延迟签署 AI 行政令**（ reportedly 受 David Sacks 影响）与 **Meta Oversight Board** 对 deepfake/认知自由的关切 |
| OpenClaw | [openclaw/openclaw `v2026.5.24-beta.2`](https://github.com/openclaw/openclaw/releases/tag/v2026.5.24-beta.2) | GitHub **`Published: 2026-05-24T23:49:30Z` → `2026-05-25 07:49:30（Asia/Shanghai）`** | 开源发布 | **Gateway 热路径缓存**（models 列表 **~20s→~5ms**）、**Meeting Notes 源插件**（Discord voice 首发）、**子 Agent 默认仅 bootstrap AGENTS.md/TOOLS.md**、Codex 插件生命周期 QA-Lab 覆盖 |
| 平台可靠性 | [Claude Status: Elevated error rates on Opus 4.7](https://status.anthropic.com/) | **事件：`2026-05-25 06:30–10:30 UTC` → `2026-05-25 14:30–18:30（Asia/Shanghai）`；Resolved `10:39 UTC`** | 官方状态 | **`2026-05-25`** Opus 4.7 **错误率升高** 约 4 小时后恢复——生产 Agent 需为 **模型 tier 波动** 预留 fallback/重试策略 |
| 论文 / Agent Skills | [SkillOpt: Executive Strategy for Self-Evolving Agent Skills（HF Daily）](https://huggingface.co/papers/date/2026-05-25) | **HF Daily：`2026-05-25`** | 论文原文 | 当日 Agent Skills 论文簇之一：聚焦 **自进化 Skill 的执行策略优化**——与 Codex/Claude Code Skills 工程实践可对照 |
| 论文 / Agent Skills | [From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills（HF Daily）](https://huggingface.co/papers/date/2026-05-25) | **HF Daily：`2026-05-25`** | 论文原文 | 系统研究 **原始轨迹 → 可消费 Skill** 的生成与使用链路——对团队 Skills 归档/治理有直接参考 |
| Skills / Cursor | [Cursor Agent Skills in `.agents/skills` — injection bug（Cursor Forum）](https://forum.cursor.com/t/cursor-agent-skills-in-agents-skills/161142) | **`2026-05-25` 窗口确认** | 社区/工程 | Skills **Settings 与 `/` 菜单可见** 但未注入 **` ` system prompt**——属 **注入阶段 bug** 而非发现失败；生产 Skills 工作流需临时 workaround |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| AI 治理 | [Magnifica Humanitas 全文（Vatican）](https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260525-enciclica-magnifica-humanitas.html) | **human dignity、劳动、LAWS、民主/信息操纵** | AI 产品/政策/合规负责人 |
| Frontier lab 自省 | [Chris Olah 梵蒂冈讲稿（Anthropic）](https://www.anthropic.com/news/chris-olah-pope-leo-encyclical) | **激励结构、外部批评、interpretability 三问** | AI 安全/对齐研究者 |
| OpenClaw 升级 | [OpenClaw v2026.5.24-beta.2 Release Notes](https://github.com/openclaw/openclaw/releases/tag/v2026.5.24-beta.2) | Gateway **provider auth 预暖**、Meeting Notes **SDK 源契约**、**imageQuality** 自适应压缩 | 自托管个人 Agent 运维 |
| Agent Skills 研究 | [Hugging Face Daily Papers 2026-05-25](https://huggingface.co/papers/date/2026-05-25) | **SkillOpt**、**Skill Consumption**、**HINT-SD** 长时程 Agent | Agent 平台/Skills 治理团队 |
| Spring AI 迁移 | [Spring AI 2.0.0-M7 Release](https://github.com/spring-projects/spring-ai/releases/tag/v2.0.0-M7) | **Boot 4 硬依赖**、Jackson 3、MCP-first；**GA 预计 2026-05-28** | Java AI 工程师（提前排迁移） |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：`2026-05-25` Agent 工程呈现 **「治理话语上行 + 平台能力下行」** 双轨——公共领域以教谕/Olah 将 **对齐与监督** 推向跨学科对话；工程侧 OpenClaw 继续 **Gateway 性能/Meeting Notes/子 Agent 上下文** 收口；Skills 方向从 **工具配置** 进入 **自进化与经验归档** 的研究阶段（HF 当日论文簇）。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 治理 × 研发 | Magnifica Humanitas + Olah 讲稿 | 产品/Agent 设计应预设 **外部审计者与社区参与**，而非仅内部 red team |
| 企业 Agent 组织 | ClickUp ~3000 内部 Agent | 度量从 **token 消耗** 转向 **价值/节省时间**；但需警惕 **「自动化=留任」** 叙事与真实 headcount 曲线 |
| 个人 Agent 平台 | OpenClaw **v2026.5.24-beta.2** | 优先验证 **Gateway models 列表延迟** 与 **Meeting Notes Discord voice** 集成后再上生产 |
| Skills 生命周期 | HF **SkillOpt / Skill Consumption** | 建立 **轨迹→Skill→消费** 闭环与 admission 评分，避免仅堆 SKILL.md |
| Cursor Skills | 注入 stage bug | 在修复前：显式 `@skill` 或手动引用 SKILL.md，勿假设 system prompt 自动携带 |
| Java AI 栈 | Spring AI **2.0 GA 倒计时（5/28）** | Boot 3.5 **EOL 2026-06-30** 与 AI 2.0 窗口重叠——尽快做 **Boot 4 + Jackson 3** 清单 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **Magnifica Humanitas + Olah 讲稿** | 当日 **唯一跨宗教/AI lab/公共政策** 的硬对齐同台事件 |
| 必读 | **OpenAI 巴西媒体合作官方文** | 观察 **归因/透明/链回原文** 与 **Enterprise/API/Codex** 捆绑策略 |
| 推荐 | **OpenClaw v2026.5.24-beta.2** | 当日 **主要开源 Agent 平台 release**（Gateway 4100× models 列表加速值得实测） |
| 推荐 | **TechCrunch：ClickUp AI 裁员叙事** | **Agent 组织重构** 的公开样本（含 Gartner 80% 自主技术公司裁员对照） |
| 延伸 | **HF 2026-05-25 Agent Skills 论文簇** | 将 Skills 从「prompt 文件」升级为 **可评测、可进化、可消费** 的工程对象 |

### 来源清单

- 检索范围：2026-05-25 00:00:00 到 2026-05-25 23:59:59（Asia/Shanghai）
- 引用域名：vatican.va, anthropic.com, openai.com, github.com, techcrunch.com, huggingface.co, forum.cursor.com, status.anthropic.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 政策标准 | Magnifica Humanitas 教谕 | 2026-05-25 | https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260525-enciclica-magnifica-humanitas.html |
| 官方发布 | Chris Olah 梵蒂冈讲稿 | 2026-05-25 | https://www.anthropic.com/news/chris-olah-pope-leo-encyclical |
| 官方发布 | OpenAI × Folha/UOL 巴西合作 | 2026-05-25 | https://openai.com/index/grupo-folha-grupo-uol-partnership/ |
| 开源发布 | OpenClaw v2026.5.24-beta.2 | 2026-05-25（Asia/Shanghai） | https://github.com/openclaw/openclaw/releases/tag/v2026.5.24-beta.2 |
| 技术媒体 | ClickUp AI 裁员（TechCrunch） | 2026-05-25/26（跨时区） | https://techcrunch.com/2026/05/25/what-clickups-mass-layoff-tells-us-about-the-future-of-work/ |
| 技术媒体 | 教谕解读（TechCrunch） | 2026-05-25/26（跨时区） | https://techcrunch.com/2026/05/25/the-popes-ai-encyclical-isnt-really-about-ai/ |
| 官方状态 | Claude Opus 4.7 错误率事件 | 2026-05-25 | https://status.anthropic.com/ |
| 论文原文 | HF Daily Papers（含 SkillOpt 等） | 2026-05-25 | https://huggingface.co/papers/date/2026-05-25 |
| 社区工程 | Cursor Skills 注入 bug | 2026-05-25 窗口 | https://forum.cursor.com/t/cursor-agent-skills-in-agents-skills/161142 |
| 开源发布 | Spring AI 2.0.0-M7（邻近日期参考） | 2026-05-22 | https://github.com/spring-projects/spring-ai/releases/tag/v2.0.0-M7 |

## 2026-05-24

### 今日总览

**一句话结论**：`2026-05-24`（Asia/Shanghai）主线是 **AI 安全从「人力防御」转向「Agentic Defense + 平台责任」**（Google Cloud COO 呼吁 **fully agentic defense**、NYT 报道 **Q1 网络安全岗位 +11%**）与 **OpenClaw `v2026.5.22` stable 发布**（Codex app-server/harness 可靠性收口）并行；**Claude Code 被用于 AutoTTS 自动发现 test-time scaling 控制器**（约 **$40/160min**、**~70% token 节省**）与 **Agent-BRACE 论文**（**2026-05-24 arXiv 提交**）共同指向 **「人类设计搜索空间，Agent 写策略/信念状态」** 范式；**Skills 生态** 出现 **69k+ SKILL.md 开放目录**（claudskills.com）但 **Claude Code/Codex/Hermes/Spring AI 当日无新官方 release**。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | OpenClaw GitHub；TechCrunch/NYT/The Decoder/The Register；Agent-BRACE/AutoTTS 论文与媒体；Claude Code/Codex/OpenClaw/Hermes/Spring AI/skills 专项；EU/US 政策窗口；中文补充 |
| 核心趋势 | **AI 安全「机器速度 vs 机器速度」**（攻击 handoff **8h→22s**、Agent 漫游发现遗留 SharePoint）；**TTS/Agent 策略自动化**（Claude Code 写 controller、信念状态 WEP 标注）；**个人 Agent 平台 stable 线晋升**（OpenClaw **v2026.5.22**）；**Skills 供应链治理**（69k 目录 + 内容评分 admission） |
| 可直接关注 | 评估 **OpenClaw v2026.5.22** 的 Codex migration/插件绑定修复；阅读 **AutoTTS** 离线 replay 环境设计；跟踪 **Google API key 撤销 23 分钟窗口** 与 **自动 tier 升级** 风险；用 **Agent-BRACE** 的 **WEP 信念状态** 改造长时程 Agent |
| 专项检索结论 | **Claude Code**：未发现 **`2026-05-24`** 新 tag（最近 **`v2.1.148`** 为 **`2026-05-22`**）；**AutoTTS** 使用 **Claude Code** 作 explorer（**THE DECODER `May 24, 2026`** 解读）；**Codex**：未发现 **`2026-05-24`** 新 release（最近 **`rust-v0.134.0-alpha.1`** 为 **`2026-05-22`**）；**OpenClaw**：**`v2026.5.22`** **`Published: 2026-05-24T01:12:56Z` → `2026-05-24 09:12:56（Asia/Shanghai）`**；**Hermes**：未发现 **`2026-05-24`** 新 tag（最近 **`v2026.5.16`** 为 **`2026-05-16`**，仓库 **`Last push: 2026-05-24`**）；**Spring AI**：未发现 **`2026-05-24`** 硬对齐 release；**skills/Cursor Skills**：**claudskills.com** 跨 **69,369** SKILL.md（DEV 工程文 **`2026-05-24` 窗口**），**SKILL.md 格式向 cursor-rules/aider-skills 泄漏** |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| OpenClaw | [openclaw/openclaw `v2026.5.22`](https://github.com/openclaw/openclaw/releases/tag/v2026.5.22) | GitHub **`Published: 2026-05-24T01:12:56Z` → `2026-05-24 09:12:56（Asia/Shanghai）`** | 开源发布 | **beta→stable** 线：Codex app-server **`/codex detach`** 插件绑定逃逸、**prompt timeout 竞态** 修复、**Codex/OpenClaw code-mode 边界** 文档澄清、QA-Lab 媒体工具超时修复 |
| AI 安全 / 平台 | [Everyone is navigating AI security in real time — even Google](https://techcrunch.com/2026/05/24/everyone-is-navigating-ai-security-in-real-time-even-google/) | **`May 24, 2026 2:39 PM PDT` → `2026-05-25 05:39（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | Google Cloud COO **Francis de Souza**：**shadow AI**、**AI-native fully agentic defense**、攻击 **handoff 22 秒**；并引用 **Google API key 泄露账单** 与 **删除后 23 分钟仍可用** 争议 |
| AI 安全 / 就业 | [One job growing in the AI era? Cybersecurity experts（NYT 转引）](https://www.straitstimes.com/business/economy/one-job-growing-in-the-ai-era-cybersecurity-experts-to-deal-with-the-bug-pocalypse) | **`May 24, 2026`（NYT/Techmeme 窗口）** | 技术媒体 | Glassdoor：**Q1 网络安全岗位发布 +11% YoY**；AI 生成代码引入漏洞 + **Mythos 类模型** 加速找洞——「**bug-pocalypse**」人力缺口 |
| Claude Code / TTS | [Researchers let Claude Code discover AI scaling algorithms…](https://the-decoder.com/researchers-let-claude-code-discover-ai-scaling-algorithms-that-humans-probably-wouldnt-have-designed/) | **`May 24, 2026`** | 技术媒体 | **AutoTTS**：Claude Code 在离线 replay 环境迭代 **Confidence Momentum Controller**；**~70% token 节省**、发现成本 **~$40/160min**——人类设计 **environment**，Agent 写 **controller 代码** |
| 论文 / Agent | [Agent-BRACE: Decoupling Beliefs from Actions…](https://arxiv.org/abs/2605.11436) | **arXiv 提交：`2026-05-24`** | 论文原文 | 将 LLM Agent 拆为 **belief state model + policy model**；用 **WEP  verbalized certainty** 标注原子 claim；Quest 上 **+14.5%/+5.3%** 绝对提升且 **context 近常数** |
| Skills 生态 | [How I indexed 69,000 Claude Code skills…](https://dev.to/adamlankamer/how-i-indexed-69000-claude-code-skills-and-what-i-learned-doing-it-76f) | **`2026-05-24`（DEV 发布窗口）** | 社区工程 | **claudskills.com** 开放目录/API/Parquet 数据集；**24 源 nightly miner**、**内容 admission 评分**（反 popularity 排序）；**SKILL.md → cursor-rules/aider-skills** 跨 Agent 标准泄漏 |
| AI 安全 / Google | [Threat hunters find Google API keys still usable 23 minutes after deletion](https://www.theregister.com/devops/2026/05/21/threat-hunters-find-google-api-keys-still-usable-23-minutes-after-deletion/5244504) | **`May 21, 2026`（`2026-05-24` TechCrunch 交叉引用）** | 技术媒体 | **Aikido**：legacy **Google API key** 删除后 **最长 23 分钟** 仍可用；**Gemini AQ key ~1min**、**service account ~5s**——平台 revoke SLA 不一致 |
| Anthropic / Mythos | [Anthropic Moves Closer to Public Claude Mythos Release…](http://www.techtimes.com/articles/317076/20260524/anthropic-moves-closer-public-claude-mythos-release-10000-critical-bugs-found-first.htm) | **`May 24, 2026`** | 技术媒体 | 跟进 **5/22 Glasswing 更新**：**Mythos Preview 仍 gated**；**Claude Security beta** 三周 **2100+** 漏洞补丁——披露产能 vs 补丁产能张力延续 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| AutoTTS | [AutoTTS GitHub + 项目页](https://github.com/zhengkid/AutoTTS) | 离线 **replay environment**、**beta parameterization**、Claude Code **explorer loop** | Agent 推理成本优化 / TTS 研究者 |
| Agent 信念状态 | [Agent-BRACE 论文 + 代码](https://github.com/joykirat18/Agent-BRACE) | **WEP 标注**、belief/policy **PPO 联合训练**、长时程 **POMDP** | 具身/文本世界 Agent 工程师 |
| OpenClaw 升级 | [OpenClaw v2026.5.22 Release Notes](https://github.com/openclaw/openclaw/releases/tag/v2026.5.22) | Codex **plugin-owned conversation binding**、**migrate plan codex** | 自托管个人 Agent 运维 |
| Skills 目录 | [claudskills.com API OpenAPI](https://claudskills.com/api/v1/openapi.json) | **CC BY 4.0 数据集**、**admission scoring**、跨 Agent **SKILL.md** 互操作 | Skills 平台/治理团队 |
| MCP 企业运行时 | [Should you build or buy an MCP runtime…（DEV）](https://dev.to/arcade/should-you-build-or-buy-an-mcp-runtime-for-enterprise-ai-agents-in-2026-36jg) | **OAuth/审计/策略** vs 自建 LangChain/Mastra 适配 | 企业 Agent 架构师 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：Agent 工程继续从 **「手写 heuristics」** 迁移到 **「可搜索/可进化的控制面」**——**AutoTTS** 让 Claude Code 写 **TTS controller**，**Agent-BRACE** 让 RL 学 **结构化信念状态**；平台侧 **OpenClaw stable** 收口 Codex harness 可靠性；安全侧 **Agent 既是攻击面也是防御面**（漫游数据资产 + agentic defense）。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| TTS 自动化 | AutoTTS + Claude Code | 投资 **offline replay + trace feedback**，而非手工调 branch/prune 阈值 |
| 长时程 POMDP | Agent-BRACE **WEP claims** | 用 **显式 verbalized uncertainty** 替代 raw history 或单点 summary |
| 个人 Agent stable | OpenClaw **v2026.5.22** | 跟踪 **Codex code-mode 边界** 与 **plugin detach** 行为再评估生产策略 |
| Skills 供应链 | 69k 开放目录 | 引入 **内容 admission + 来源审计**；勿仅按 stars/installs 安装 |
| MCP 安全 | Agent framework RCE/CVE 清单（社区） | **STDIO MCP** 需 **allowlist/sandbox**；生产优先 **Streamable HTTP + runtime 层** |
| Agentic Defense | Google Cloud COO 观点 | 安全架构需覆盖 **models/data pipelines/agents/prompts** 全栈，而非 perimeter-only |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **OpenClaw v2026.5.22 GitHub Release** | 当日 **唯一硬对齐官方开源 Agent 平台 stable 发布** |
| 必读 | **THE DECODER：Claude Code × AutoTTS** | **Agent 写算法** 的可复现样本（$40 级 discovery 成本） |
| 推荐 | **Agent-BRACE（2026-05-24 arXiv）** | 长时程 Agent **信念状态 + 不确定性** 的结构化做法 |
| 推荐 | **TechCrunch：Google Cloud AI 安全访谈** | **Agentic defense** 与 **平台 revoke/计费** 现实差距的对照 |
| 延伸 | **claudskills 69k 目录工程文** | Skills **发现/治理/跨 Agent 标准** 的一手数据 |

### 来源清单

- 检索范围：2026-05-24 00:00:00 到 2026-05-24 23:59:59（Asia/Shanghai）
- 引用域名：github.com, techcrunch.com, the-decoder.com, arxiv.org, dev.to, theregister.com, straitstimes.com, techtimes.com, zhengkid.github.io
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 开源发布 | OpenClaw v2026.5.22 | 2026-05-24 | https://github.com/openclaw/openclaw/releases/tag/v2026.5.22 |
| 技术媒体 | Google Cloud AI security（TechCrunch） | 2026-05-24（PDT，Asia/Shanghai 跨至 05-25） | https://techcrunch.com/2026/05/24/everyone-is-navigating-ai-security-in-real-time-even-google/ |
| 技术媒体 | Cybersecurity jobs +11%（NYT 转引） | 2026-05-24 | https://www.straitstimes.com/business/economy/one-job-growing-in-the-ai-era-cybersecurity-experts-to-deal-with-the-bug-pocalypse |
| 技术媒体 | Claude Code AutoTTS（THE DECODER） | 2026-05-24 | https://the-decoder.com/researchers-let-claude-code-discover-ai-scaling-algorithms-that-humans-probably-wouldnt-have-designed/ |
| 论文原文 | Agent-BRACE | 2026-05-24 | https://arxiv.org/abs/2605.11436 |
| 社区工程 | 69k Claude Code skills catalog | 2026-05-24 | https://dev.to/adamlankamer/how-i-indexed-69000-claude-code-skills-and-what-i-learned-doing-it-76f |
| 技术媒体 | Google API key 23min revoke gap | 2026-05-21（05-24 交叉引用） | https://www.theregister.com/devops/2026/05/21/threat-hunters-find-google-api-keys-still-usable-23-minutes-after-deletion/5244504 |
| 技术媒体 | Anthropic Mythos 跟进 | 2026-05-24 | http://www.techtimes.com/articles/317076/20260524/anthropic-moves-closer-public-claude-mythos-release-10000-critical-bugs-found-first.htm |
| 教程 | MCP runtime build vs buy | 2026-05-24 窗口 | https://dev.to/arcade/should-you-build-or-buy-an-mcp-runtime-for-enterprise-ai-agents-in-2026-36jg |
| 官方发布 | OpenAI/Anthropic/Spring AI | 未发现 2026-05-24 硬对齐新 release | - |
| 中文补充 | 机器之心/量子位 | 未发现 2026-05-24 硬对齐 AI 要闻 | - |

## 2026-05-23

### 今日总览

**一句话结论**：`2026-05-23`（Asia/Shanghai）主线是 **Spring AI 三版本同日发布并修复 CVE-2026-41863**（Anthropic Skills API 路径穿越）与 **Gemini Omni Flash 上手评测**（anything-to-anything 视频/deepfake 风险）并行；**Glasswing/Mythos 漏洞披露产能** 在媒体窗口继续发酵，**OpenClaw `v2026.5.22-beta.1`** 与 **Hermes Agent 超越 OpenClaw 的 OpenRouter 用量叙事** 推动个人 Agent 赛道竞争升温；**EU AI Act 高风险分类草案** 与 **美国 TAKE IT DOWN 执法** 同日呈现监管分化。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | Spring 官方；OpenClaw GitHub；The Verge/TechCrunch/The Next Web；Claude Code/Codex/OpenClaw/Hermes/Spring AI/skills 专项；EU/US 政策；arXiv；中文补充 |
| 核心趋势 | **Java AI 栈安全补丁与 MCP 传输迁移**（Spring AI 2.0-M7）；**多模态生成进入「真实视频 + deepfake」争议区**（Gemini Omni）；**漏洞发现速度 >> 补丁速度**（Glasswing 跟进报道）；**跨大西洋 AI 合规套利**（EU 收窄 vs US 扩大执法） |
| 可直接关注 | 升级 **Spring AI ≥1.1.7** 修复 **CVE-2026-41863**；评估 **Gemini Omni / Flow** 的 deepfake 与 credits 成本；跟踪 **OpenClaw beta** 与 **Hermes 自进化 skills** 选型；对照 **EU Annex III 草案** 与 **FTC TAKE IT DOWN** 做产品合规映射 |
| 专项检索结论 | **Claude Code**：终端 **`v2.1.148`** 仍为 **`2026-05-22`** 最新；**`claude-code-action v1.0.133`** **`Published: 2026-05-23T04:05:39Z` → `2026-05-23 12:05:39（Asia/Shanghai）`**（CI **workload identity federation**）；**Codex**：**Locked computer use** 在 **`2026-05-23`** 媒体继续解读（官方 Changelog 为 **`2026-05-21`**）；**OpenClaw**：**`v2026.5.22-beta.1`** **`Published: 2026-05-23T09:59:56Z` → `2026-05-23 17:59:56（Asia/Shanghai）`**；**Hermes**：The Batch / 社区分析强调 **OpenRouter 日 token 超越 OpenClaw** 与 **自动 skills 生成**（无 **`2026-05-23`** 新 tag）；**Spring AI**：官方博文 **`2026-05-23`** 发布 **`1.0.8`/`1.1.7`/`2.0.0-M7`**；**skills/Cursor Skills**：未发现 **`2026-05-23`** 官方 Changelog（Cursor Docs 为既有 open standard 文档） |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| Spring AI | [Spring AI 1.0.8, 1.1.7, 2.0.0-M7 Available Now](https://spring.io/blog/2026/05/23/spring-ai-1-0-8-1-1-7-2-0-0-M7-available-now) | **官方：`2026-05-23`** | 官方发布 | **`1.1.7`/`2.0.0-M7`** 修复 **CVE-2026-41863**（Anthropic Skills API 文件名未消毒导致 **Path.resolve 越界写**）；**2.0-M7** 弃用 MCP **SSE**、默认 **Streamable HTTP**，**ToolCallAdvisor** 成为默认工具调用路径 |
| Spring 安全 | [CVE-2026-41863 Advisory](https://spring.io/security/cve-2026-41863) | **`2026-05-23`（随 1.1.7 发布）** | 安全公告 | 仅影响使用 **Anthropic Skills API** 且 LLM 可控文件名的应用——需升级 **≥1.1.7** |
| 多模态 / Gemini | [Google’s new anything-to-anything AI model is wild](https://www.theverge.com/tech/936507/gemini-omni-hands-on-deepfake-ai-video) | **`May 23, 2026 11:00 AM UTC` → `2026-05-23 19:00（Asia/Shanghai）`** | 技术媒体 | **Gemini Omni Flash** 上手：**真实自拍视频 + 文本 prompt → deepfake 场景**；credits 消耗快（约 20 条 clip 后 Pro 计划剩 **145/1000** credits）——产品/合规需评估 **非 consensual likeness** 风险 |
| AI 安全 / Glasswing | [Claude Mythos found 10,000 critical vulnerabilities… patches can't keep up](https://thenextweb.com/news/anthropic-glasswing-claude-mythos-10000-vulnerabilities) | **`2026-05-23`（媒体跟进 Glasswing 周五披露）** | 技术媒体 | **1,726** 已验证、**1,094** 高/严重确认、仅 **97** 已补丁；**WolfSSL CVE-2026-5194（CVSS 9.1）** 为标志性发现——「发现 >> 补丁」产能瓶颈 |
| OpenClaw | [openclaw/openclaw `v2026.5.22-beta.1`](https://github.com/openclaw/openclaw/releases/tag/v2026.5.22-beta.1) | GitHub **`Published: 2026-05-23T09:59:56Z` → `2026-05-23 17:59:56（Asia/Shanghai）`** | 开源预发布 | 文档/启动/插件/Gateway/CLI 可靠性 beta 线更新（含 Telegram/Slack/Windows 等修复）——跟踪 stable 晋升 |
| Hermes / 个人 Agent | [Hermes Agent challenges OpenClaw（The Batch）](https://www.deeplearning.ai/the-batch/hermes-agent-challenges-openclaw) | **`2026-05-23`（The Batch 窗口）** | 技术媒体 | **Hermes** 强调 **多层 memory + 自动 SKILL.md 生成 + Curator 归档**；**OpenRouter** 日 token 超越 **OpenClaw**——个人 Agent 竞争从「渠道广度」转向「自进化深度」 |
| Claude Code CI | [anthropics/claude-code-action `v1.0.133`](https://github.com/anthropics/claude-code-action/releases/tag/v1.0.133) | GitHub **`Published: 2026-05-23T04:05:39Z` → `2026-05-23 12:05:39（Asia/Shanghai）`** | 开源发布 | CI 工作流改用 **workload identity federation** 做 Claude 认证——企业 GitHub Actions 集成参考 |
| 企业 AI / 体育 | [Ferrari is using IBM's AI to create F1 superfans](https://techcrunch.com/2026/05/23/ferrari-is-using-ai-to-create-f1-superfans/) | **`May 23, 2026 8:08 AM PDT` → `2026-05-23 23:08（Asia/Shanghai）`** | 企业落地 | IBM 重构 **Ferrari fan app**：**AI 赛事摘要、预测游戏、AI companion**；**race weekend 互动 +62%**——「telemetry → 叙事 → 个性化」闭环样本 |
| AI 基础设施 / 能源 | [Elon Musk has given up on solar power (on Earth)](https://techcrunch.com/2026/05/23/elon-musk-has-given-up-on-solar-power-on-earth/) | **`May 23, 2026 6:00 AM PDT` → `2026-05-23 21:00（Asia/Shanghai）`** | 技术媒体 | SpaceX IPO 文件提及 **terawatt-scale AI compute** 与 **space-based solar**——AI 算力能源叙事从地面 NIMBY 转向轨道 |
| AI 基础设施 / 核能 | [Nuclear startup Deep Fission… going public again](https://techcrunch.com/2026/05/23/nuclear-startup-deep-fission-says-its-going-public-again-and-i-have-questions/) | **`May 23, 2026 7:50 AM PDT` → `2026-05-23 22:50（Asia/Shanghai）`** | 技术媒体 | **Deep Fission** 拟 IPO 为 **AI 数据中心** 供地下反应堆电力——监管/技术现实与 AI 电力 hype 的张力 |
| 政策 / EU | [EU draft guidance narrows high-risk AI classification](https://noah-news.com/eu-draft-guidance-narrows-high-risk-ai-classification-with-focus-on-purpose-and/) | **`Sat 23 May 2026`（解读 EU 5/22 草案）** | 政策标准 | **Annex III** 草案：**关键基础设施/执法/司法** 部分收窄，**就业/保险/教育** 扩大；反馈截止 **2026-06-23**；Annex III 合规延至 **2027-12-02** |
| 政策 / US | [EU narrowed… FTC started fining eight platforms](https://ngtimes.org/2026/05/23/the-eu-narrowed-and-the-ftc-broadened-on-the-same-week) | **`May 23, 2026`** | 政策标准 | **FTC TAKE IT DOWN**（**5/19** 致函 8 平台）**$53,088/违规** vs **EU 高风险分类收窄**——跨大西洋 **compliance arbitrage** |
| AI 伦理 / 内容 | [Author Steven Rosenbaum… trapped in a toxic relationship with AI](https://www.theverge.com/ai-artificial-intelligence/936827/author-steven-rosenbaum-sounds-like-hes-trapped-in-a-toxic-relationship-with-ai) | **`May 23, 2026 7:19 PM UTC` → `2026-05-24 03:19（Asia/Shanghai）`（相邻日期/跨时区）** | 社会观察 | AI 辅助写作 ** fabricated quotes** 案例——企业/出版 **human-in-the-loop + 出处核验** 警示 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| Spring AI 升级 | [Spring AI 1.1.7 / 2.0.0-M7 Release Notes](https://github.com/spring-projects/spring-ai/releases/tag/v2.0.0-M7) | **ToolCallAdvisor**、**ToolSpec** API、MCP **Streamable HTTP** | Java/Spring Agent 开发者 |
| CVE 修复 | [CVE-2026-41863](https://spring.io/security/cve-2026-41863) | Anthropic Skills API **文件名消毒** | 使用 Skills API 的安全评审 |
| Codex 锁屏自动化 | [Computer Use – Codex app](https://developers.openai.com/codex/app/computer-use) | **Locked use** safeguards、短授权窗口 | macOS Codex 用户 / MDM |
| MCP + LangChain | [Building Autonomous DevOps Agents with MCP and LangChain](https://dev.to/rs9000/building-autonomous-devops-agents-with-mcp-and-langchain-82n) | **`MultiServerMCPClient`** stdio + SSE 混合 | Agent 平台工程师 |
| Cursor Skills | [Agent Skills \| Cursor Docs](https://cursor.com/docs/skills) | **SKILL.md** open standard、`.cursor/skills/` 发现规则 | IDE Agent 用户 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：**Agent 工程继续「运行时 + 安全 + 合规」三线并进**——Spring AI 在 **MCP 传输迁移与 ToolCallAdvisor 默认化** 上收口 Java 栈；个人 Agent 赛道 **OpenClaw beta vs Hermes 自进化 skills** 形成 **广度 vs 深度** 对照；安全侧 **Glasswing 披露漏斗** 与 **Spring CVE** 共同提示：**Agent 写文件/写 skill 路径必须消毒与审计**。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| Java AI 安全 | Spring AI **CVE-2026-41863** | LLM 影响的 **文件名/路径** 必须白名单或 sandbox，不可直接 **Path.resolve** |
| MCP 协议演进 | Spring AI **2.0-M7** 弃用 SSE | 新集成优先 **Streamable HTTP**；legacy SSE 需迁移计划 |
| 个人 Agent 竞争 | Hermes **自动 skills + Curator** vs OpenClaw **13k+ 静态 skills** | 选型：**Day-1 广度** 选 OpenClaw；**长期 workflow 复利** 评估 Hermes |
| OpenClaw beta | **v2026.5.22-beta.1** | 生产环境跟踪 **stable 晋升** 与 **ClawHub 恶意 skills** 供应链 |
| Agent 推理成本 | DEV 社区 **MCP+LangChain DevOps** 示例 | **stdio 本地 + SSE 远程 ticketing** 单 ReAct 环——多 MCP server 编排模板 |
| 漏洞披露产能 | Glasswing **97/1094 已补丁** | 引入 **AI 扫描 + maintainer SLA**；缩短 patch cycle |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **Spring AI 2026-05-23 三版本发布 + CVE-2026-41863** | 当日 **唯一硬对齐官方 Java AI 栈发布** |
| 必读 | **The Verge：Gemini Omni hands-on** | **deepfake 门槛与 credits 经济学** 的直观样本 |
| 推荐 | **The Next Web：Glasswing 补丁跟不上** | 量化 **发现/验证/补丁** 漏斗，安全团队必读 |
| 推荐 | **DeepLearning.AI The Batch：Hermes vs OpenClaw** | 个人 Agent **memory/skills 架构** 对照 |
| 延伸 | **NG Times：EU 收窄 vs FTC 扩大** | 跨国 AI 产品 **合规套利** 框架 |

### 来源清单

- 检索范围：2026-05-23 00:00:00 到 2026-05-23 23:59:59（Asia/Shanghai）
- 引用域名：spring.io, github.com, theverge.com, techcrunch.com, thenextweb.com, deeplearning.ai, ngtimes.org, dev.to, cursor.com, developers.openai.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 官方发布 | Spring AI 1.0.8 / 1.1.7 / 2.0.0-M7 | 2026-05-23 | https://spring.io/blog/2026/05/23/spring-ai-1-0-8-1-1-7-2-0-0-M7-available-now |
| 安全公告 | CVE-2026-41863 | 2026-05-23 | https://spring.io/security/cve-2026-41863 |
| 开源发布 | OpenClaw v2026.5.22-beta.1 | 2026-05-23 | https://github.com/openclaw/openclaw/releases/tag/v2026.5.22-beta.1 |
| 开源发布 | claude-code-action v1.0.133 | 2026-05-23 | https://github.com/anthropics/claude-code-action/releases/tag/v1.0.133 |
| 技术媒体 | Gemini Omni hands-on | 2026-05-23 | https://www.theverge.com/tech/936507/gemini-omni-hands-on-deepfake-ai-video |
| 技术媒体 | Glasswing patches can't keep up | 2026-05-23 | https://thenextweb.com/news/anthropic-glasswing-claude-mythos-10000-vulnerabilities |
| 技术媒体 | Hermes Agent challenges OpenClaw | 2026-05-23 | https://www.deeplearning.ai/the-batch/hermes-agent-challenges-openclaw |
| 技术媒体 | Ferrari × IBM AI fan app | 2026-05-23 | https://techcrunch.com/2026/05/23/ferrari-is-using-ai-to-create-f1-superfans/ |
| 政策标准 | EU/US regulatory divergence | 2026-05-23 | https://ngtimes.org/2026/05/23/the-eu-narrowed-and-the-ftc-broadened-on-the-same-week |
| 教程 | MCP + LangChain DevOps agents | 2026-05-23 | https://dev.to/rs9000/building-autonomous-devops-agents-with-mcp-and-langchain-82n |
| 论文 | 未发现可核验的 2026-05-23 arXiv cs.AI 新提交批次（最近为 2026-05-22） | - | - |
| 中文补充 | 机器之心/量子位：未发现 2026-05-23 硬对齐 AI 要闻 | - | - |

## 2026-05-22

### 今日总览

**一句话结论**：`2026-05-22`（Asia/Shanghai）主线是 **Anthropic Project Glasswing 首月进展披露**（Mythos Preview 与约 50 家伙伴累计发现 **1 万+** 高/严重漏洞，瓶颈转向 **验证—披露—补丁**）与 **Codex 桌面 Agent 能力再升级**（**Appshots / Goal mode GA / Locked computer use** 在 **`2026-05-22`** 媒体窗口集中发酵）并行；Coding Agent 侧 **Claude Code `v2.1.148`** 热修复 Bash 回归，**LangChain 生态** 在跨日窗口发布 **`langchain-openai==1.2.2`** 与 **`langchain@1.4.2`**。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | Anthropic/OpenAI 官方与 GitHub Release；TechCrunch/The Verge；Claude Code/Codex/OpenClaw/Hermes/Spring AI/skills 专项；arXiv 论文；EU/US 政策；中文补充 |
| 核心趋势 | **AI 网络安全从「找洞」转向「披露与补丁产能」**；**Coding Agent 向「屏幕上下文 + 锁屏远程操控 + 跨日 Goal」收敛**；**平台侧 AI 内容生成（Spotify/Meta）与监管/伦理争议同步升温** |
| 可直接关注 | 跟进 **Glasswing 开源漏洞 Dashboard** 与 **Claude Security / Mythos 工具申请**；评估 **Codex Appshots + Locked computer use** 的企业安全边界；升级 **Claude Code v2.1.148** 修复 Bash 127 回归 |
| 专项检索结论 | **Claude Code**：**`v2.1.148`** **`Published: 2026-05-22T01:16:52Z` → `2026-05-22 09:16:52（Asia/Shanghai）`**；**Codex**：官方 Changelog **`2026-05-21`** 发布 **Appshots/Goal mode**（**`2026-05-22`** 媒体硬对齐）；**`rust-v0.134.0-alpha.1`** **`Published: 2026-05-22T19:03:43Z` → `2026-05-23 03:03:43（Asia/Shanghai）`（相邻日期/跨时区）**；**OpenClaw**：未发现 **`2026-05-22`** 新 tag（最近 **`v2026.5.20`** 为 **`2026-05-21`**）；**Hermes**：未发现 **`2026-05-22`** 新 tag；**Spring AI**：未发现 **`2026-05-22`** 硬对齐 release/博文；**skills/Cursor Skills**：未发现 **`2026-05-22`** 官方 Changelog（Anthropic 在 Glasswing 更新中提及向合格客户开放 **Mythos 配套 skills**） |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| AI 安全 / Mythos | [Project Glasswing: An initial update](https://www.anthropic.com/research/glasswing-initial-update) | **官方稿：`May 22, 2026`** | 官方发布 | 首月 **1 万+** 高/严重漏洞；开源扫描 **6,202** 估高/严重（**23,019** 总量）；**530** 已披露高/严重、**75** 已补丁；发布 [开源漏洞 Dashboard](https://red.anthropic.com/2026/cvd/)——瓶颈从 **发现** 转向 **triaging/patching** |
| AI 安全（媒体） | [Anthropic is making the security tools… just a bit more available](https://www.theverge.com/ai-artificial-intelligence/936637/anthropic-is-making-the-security-tools-its-used-with-claude-mythos-preview-just-a-bit-more-available) | **`May 22, 2026 10:55 PM UTC` → `2026-05-23 06:55（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | 合格客户可申请 **skills、harness、threat model builder**；与官方 Glasswing 稿交叉验证 |
| Codex | [Appshots, goal mode, and more（Codex Changelog）](https://developers.openai.com/codex/changelog) | **Changelog：`2026-05-21`；媒体硬对齐：`May 22, 2026`** | 官方发布 | **Appshots**（双 Command 发送前台窗口截图+文本）；**Goal mode GA**；**Locked computer use**（锁屏/息屏仍可从手机驱动 Mac 应用，含 safeguards；**EEA/UK/CH 不可用**） |
| Codex（媒体） | [OpenAI's Codex Can Now Use Your Mac Even When It's Locked](https://www.macrumors.com/2026/05/22/codex-use-mac-apps-when-locked/) | **`Friday May 22, 2026 4:28 am PDT` → `2026-05-22 19:28（Asia/Shanghai）`** | 技术媒体 | 需 **Computer Use 插件 + 屏幕录制/辅助功能** 权限；每 app 授权或 **Always allow**——企业需评估 ** unattended automation** 风险 |
| Claude Code | [anthropics/claude-code `v2.1.148`](https://github.com/anthropics/claude-code/releases/tag/v2.1.148) | GitHub **`Published: 2026-05-22T01:16:52Z` → `2026-05-22 09:16:52（Asia/Shanghai）`** | 开源发布 | 修复 **`v2.1.147`** 引入的 **Bash tool 全量 exit code 127** 回归 |
| Codex CLI | [openai/codex `rust-v0.134.0-alpha.1`](https://github.com/openai/codex/releases/tag/rust-v0.134.0-alpha.1) | GitHub **`Published: 2026-05-22T19:03:43Z` → `2026-05-23 03:03:43（Asia/Shanghai）`（相邻日期/跨时区）** | 开源预发布 | 当日 **alpha 预发布** 线更新（含 `codex-app-server`/`argument-comment-lint` 等资产）——跟踪下一稳定 tag |
| LangChain | [langchain-openai==1.2.2](https://github.com/langchain-ai/langchain/releases/tag/langchain-openai%3D%3D1.2.2) | GitHub **`Published: 2026-05-21T22:08:45Z` → `2026-05-22 06:08:45（Asia/Shanghai）`** | 开源发布 | **ContextOverflowError** 条件放宽、**LLM context size** 取自 model profiles、**httpx finalizers** guard |
| LangChain JS | [langchain@1.4.2](https://github.com/langchain-ai/langchainjs/releases/tag/langchain%401.4.2) | GitHub **`Published: 2026-05-21T22:00:57Z` → `2026-05-22 06:00:57（Asia/Shanghai）`** | 开源发布 | Agent stream **unwrap tool message outputs**；**todoListMiddleware** ToolMessage `name` 修复 |
| AI 安全 / 社会 | [AI is being used to resurrect the voices of dead pilots](https://techcrunch.com/2026/05/22/ai-is-being-used-to-resurrect-the-voices-of-dead-pilots/) | **`May 22, 2026 4:03 PM PDT` → `2026-05-23 07:03（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | NTSB 因 **spectrogram + AI（含 Codex）** 重建遇难飞行员 CVR 音频暂时限制 docket；**42** 调查待复核——AI 滥用与 **敏感数据公开** 治理案例 |
| 消费 AI / 内容 | [Spotify's AI bet: more of everything, less of what you want](https://techcrunch.com/2026/05/22/spotifys-ai-bet-more-of-everything-less-of-what-you-want/) | **`May 22, 2026 9:18 AM PDT` → `2026-05-22 21:18（Asia/Shanghai）`** | 技术媒体 | Investor Day 后 **Personal podcasts / 日历邮件音频简报 / 实验桌面 app** 等 **生成式内容** 堆叠；**Huxe** 同日关停——「功能商品化」挤压独立应用 |
| 消费 AI / 社交 | [Meta quietly launches a new Reddit-like app called Forum](https://techcrunch.com/2026/05/22/meta-quietly-launches-a-new-reddit-like-app-called-forum/) | **`May 22, 2026 7:24 AM PDT` → `2026-05-22 22:24（Asia/Shanghai）`** | 产品发布 | **Ask** 标签页跨 Groups 聚合 AI 答案 + **Admin AI assistant**  moderation——对照 Google **Search Agents** 多入口策略 |
| 搜索 / AI 产品 | [Google's AI search is so broken it can 'disregard' what you're looking for](https://www.theverge.com/tech/936176/google-ai-overviews-search-disregard) | **`May 22, 2026 4:01 PM UTC` → `2026-05-23 00:01（Asia/Shanghai）`（相邻日期/跨时区）** | 技术媒体 | 搜索词 **`disregard`/`ignore`/`skip`** 触发 AI Overview **聊天式误回复**——I/O 后 **Gemini 3.5 Flash 默认化** 的可靠性警示 |
| AI 硬件 | [We tried Google's AI glasses and they're almost there](https://techcrunch.com/2026/05/22/we-tried-googles-ai-glasses-and-theyre-almost-there/) | **`May 22, 2026 8:37 AM PDT` → `2026-05-22 23:37（Asia/Shanghai）`** | 技术媒体 | **Android XR 镜片显示版** 仍处 Trusted Tester；**2026 秋音频版** 先出货——与 Meta/Snap 竞争节奏 |
| 论文 / Agent 治理 | [Contractual Skills: A GovernSpec Design Framework for Enterprise AI Agents](https://arxiv.org/html/2605.22634v1) | **arXiv 列表：`May 22, 2026`** | 论文原文 | 将 **SKILL.md** 组织为 **task contract**（goal/permissions/human gates/verification）——企业 Agent **可审计 Skill** 设计参考 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| Mythos / 漏洞披露 | [Glasswing initial update](https://www.anthropic.com/research/glasswing-initial-update) + [CVD Dashboard](https://red.anthropic.com/2026/cvd/) | 90 天 CVD、maintainer capacity、triaging 漏斗 | 安全工程 / 开源维护者 |
| Codex 桌面 Agent | [Codex Changelog：Appshots & Goal mode](https://developers.openai.com/codex/changelog) | Appshots、Goal mode、Locked computer use safeguards | macOS Codex 用户 / 安全评审 |
| Claude Code 热修复 | [Claude Code v2.1.148](https://github.com/anthropics/claude-code/releases/tag/v2.1.148) | Bash 127 回归修复 | 已升级 **v2.1.147** 的用户 |
| LangChain MCP | [LangChain MCP Docs](https://docs.langchain.com/oss/python/langchain/mcp) | `MultiServerMCPClient`、tool interceptors、stateful sessions | Python Agent 工程师 |
| 企业 Skill 契约 | [Contractual Skills（GovernSpec）](https://arxiv.org/html/2605.22634v1) | SKILL.md 作为 **task contract** | Agent 平台 / 合规架构 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：**Agent 工程焦点从「能调用工具」转向「治理闭环」**——Glasswing 强调 **verify-gated disclosure**，论文侧同步出现 **Contractual Skills / Guardrails as Infrastructure / Verify-Gated Completion**；Coding Agent 则在 **屏幕上下文（Appshots）与锁屏自动化** 上继续扩展 **Computer Use** 边界。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 漏洞披露产能 | Glasswing：**发现 >> 补丁** | 引入 **AI 扫描 + 人工 triage SLA**；跟踪 [CVD Dashboard](https://red.anthropic.com/2026/cvd/) 漏斗 |
| Skill 即契约 | GovernSpec **Contractual Skills** | SKILL.md 应含 **permissions / human gates / verification**，而非仅 prompt |
| MCP 工程化 | LangChain **tool interceptors** | 在 MCP 层注入 **auth/header/retry**，弥补 server 进程隔离 |
| 跨 turn 目标 | Codex **Goal mode GA** | 与 **Claude Code `/code-review`** 形成「长任务 + 审查」双轨 |
| 锁屏自动化 | Codex **Locked computer use** | 必须 **短授权 + 本地输入重锁 + 区域限制**——纳入企业 MDM 策略 |
| LangChain 补丁 | **langchain-openai 1.2.2** | 升级以修复 **ContextOverflowError** 误判与 context size 来源 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **Anthropic：Project Glasswing initial update** | 当日 **最硬对齐官方稿**，定义 AI 时代 **漏洞披露瓶颈** |
| 必读 | **Codex Changelog：Appshots / Goal mode / Locked use** | **Coding Agent 产品化** 与 **安全边界** 同日交汇 |
| 推荐 | **Claude Code v2.1.148** Release | 小版本但影响 **Bash 全失败** 的生产事故 |
| 推荐 | arXiv：**Contractual Skills（GovernSpec）** | 把 **Agent Skills** 上升到 **企业可审计契约** |
| 延伸 | The Verge：**Google AI Overviews disregard bug** | I/O 后 **Search Agent 默认化** 的 **可靠性/提示注入** 风险样本 |

### 来源清单

- 检索范围：2026-05-22 00:00:00 到 2026-05-22 23:59:59（Asia/Shanghai）
- 引用域名：anthropic.com, developers.openai.com, github.com, techcrunch.com, theverge.com, macrumors.com, arxiv.org, docs.langchain.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 官方发布 | Project Glasswing: An initial update | 2026-05-22 | https://www.anthropic.com/research/glasswing-initial-update |
| 官方发布 | Codex Changelog：Appshots, goal mode, and more | 2026-05-21（2026-05-22 媒体窗口） | https://developers.openai.com/codex/changelog |
| 开源发布 | Claude Code v2.1.148 | 2026-05-22 | https://github.com/anthropics/claude-code/releases/tag/v2.1.148 |
| 开源预发布 | Codex rust-v0.134.0-alpha.1 | 2026-05-22（相邻日期/跨时区发布） | https://github.com/openai/codex/releases/tag/rust-v0.134.0-alpha.1 |
| 开源发布 | langchain-openai==1.2.2 | 2026-05-22（跨日窗口） | https://github.com/langchain-ai/langchain/releases/tag/langchain-openai%3D%3D1.2.2 |
| 开源发布 | langchain@1.4.2 | 2026-05-22（跨日窗口） | https://github.com/langchain-ai/langchainjs/releases/tag/langchain%401.4.2 |
| 技术媒体 | NTSB / AI 重建飞行员语音 | 2026-05-22（相邻日期/跨时区） | https://techcrunch.com/2026/05/22/ai-is-being-used-to-resurrect-the-voices-of-dead-pilots/ |
| 技术媒体 | Spotify AI 内容堆叠 | 2026-05-22 | https://techcrunch.com/2026/05/22/spotifys-ai-bet-more-of-everything-less-of-what-you-want/ |
| 技术媒体 | Meta Forum + AI Ask | 2026-05-22 | https://techcrunch.com/2026/05/22/meta-quietly-launches-a-new-reddit-like-app-called-forum/ |
| 技术媒体 | Google AI Overviews disregard bug | 2026-05-22（相邻日期/跨时区） | https://www.theverge.com/tech/936176/google-ai-overviews-search-disregard |
| 技术媒体 | Anthropic Glasswing 工具开放（Verge） | 2026-05-22（相邻日期/跨时区） | https://www.theverge.com/ai-artificial-intelligence/936637/anthropic-is-making-the-security-tools-its-used-with-claude-mythos-preview-just-a-bit-more-available |
| 技术媒体 | Google AI 眼镜上手 | 2026-05-22 | https://techcrunch.com/2026/05/22/we-tried-googles-ai-glasses-and-theyre-almost-there/ |
| 论文原文 | Contractual Skills: GovernSpec | 2026-05-22 | https://arxiv.org/html/2605.22634v1 |

## 2026-05-21

### 今日总览

**一句话结论**：`2026-05-21`（Asia/Shanghai）主线是 **Coding Agent 双栈同日发版**（Claude Code **`v2.1.146`**、Codex **`rust-v0.133.0`**）与 **Google I/O Agent 产品落地争议**（Information Agents / Gemini Spark / Daily Brief 多入口但 Ultra 付费墙）并行；政策侧 **特朗普推迟签署 AI 安全审查 EO**，企业侧 **Microsoft × EY 宣布 10 亿美元级联合计划** 推动从试点到规模化落地。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | OpenAI/Anthropic/Google/Microsoft 官方与 GitHub Release；TechCrunch/The Verge；Claude Code/Codex/OpenClaw/Hermes/Spring AI/skills 专项；arXiv 论文；EU/US 政策；中文补充 |
| 核心趋势 | **终端 Coding Agent 进入「Goals 默认开 + 权限 Profile 继承 + /code-review 标准化」工程化阶段**；**消费级 Agent 生态产品化加速但付费墙与品牌碎片化引质疑**；**美国政府 AI 预发布审查 EO 暂缓**，监管与产业速度博弈加剧 |
| 可直接关注 | 升级 **Claude Code v2.1.146** 评估 `/code-review` 与 Windows MCP 分页修复；评估 **Codex 0.133.0** 的 Goals 默认开启与 `remote-control` 前台化；跟踪 **OpenClaw beta.2** 的 Policy 插件与 Discord 语音 Agent |
| 专项检索结论 | **Claude Code**：**`v2.1.146`** **`Published: 2026-05-21T01:51:52Z` → `2026-05-21 09:51:52（Asia/Shanghai）`**；**Codex**：**`rust-v0.133.0`** **`Published: 2026-05-21T16:48:03Z` → `2026-05-22 00:48:03（Asia/Shanghai）`（相邻日期/跨时区）**；**OpenClaw**：**`v2026.5.20-beta.2`** **`Published: 2026-05-21T15:57:15Z` → `2026-05-21 23:57:15（Asia/Shanghai）`**；**Hermes**：未发现 **`2026-05-21`** 新 tag（最近 **`v2026.5.16`** 为 **`2026-05-16`**）；**Spring AI**：未发现与 **`2026-05-21`** 硬对齐的新 release/博文；**skills/Cursor Skills**：未发现 **`2026-05-21`** 官方 Changelog（最近为 **`2026-05-20` Automations**） |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| Claude Code | [anthropics/claude-code `v2.1.146`](https://github.com/anthropics/claude-code/releases/tag/v2.1.146) | GitHub **`Published: 2026-05-21T01:51:52Z` → `2026-05-21 09:51:52（Asia/Shanghai）`** | 开源发布 | **`/simplify` 重命名为 `/code-review`**（可选 effort level）；修复 Windows PowerShell、MCP 分页、后台会话权限与 auto-updater 可靠性 |
| Codex | [openai/codex `rust-v0.133.0`](https://github.com/openai/codex/releases/tag/rust-v0.133.0) | GitHub **`Published: 2026-05-21T16:48:03Z` → `2026-05-22 00:48:03（Asia/Shanghai）`（相邻日期/跨时区）** | 开源发布 | **Goals 默认开启** + 专用存储跨 turn 追踪；**`codex remote-control` 前台化**；Permission profiles 继承与 managed `requirements.toml` |
| OpenClaw | [openclaw/openclaw `v2026.5.20-beta.2`](https://github.com/openclaw/openclaw/releases/tag/v2026.5.20-beta.2) | GitHub **`Published: 2026-05-21T15:57:15Z` → `2026-05-21 23:57:15（Asia/Shanghai）`** | 开源预发布 |  bundled **Policy 插件**、Discord 语音会话跟随用户、**xAI device-code OAuth**、Skill 加载安全收紧（禁止 `cat SKILL.md` 兼容路径） |
| 消费 Agent 生态 | [Google is pitching an AI agent ecosystem to consumers who may not buy it](https://techcrunch.com/2026/05/21/google-is-pitching-an-ai-agent-ecosystem-to-consumers-who-may-not-buy-it/) | **`May 21, 2026 6:52 AM PDT` → `2026-05-21 21:52（Asia/Shanghai）`** | 技术媒体 | I/O 后 **Information Agents / Gemini Spark / Daily Brief / Android Halo** 多品牌入口，初期锁定 **Google Ultra（$100/月）** 等付费档——产品策略与「Agent 普及」叙事存在张力 |
| 政策监管 | [Trump delays AI security executive order](https://techcrunch.com/2026/05/21/trump-delays-ai-security-executive-order-i-dont-want-to-get-in-the-way-of-that-leading/) | **`May 21, 2026 10:30 AM PDT` → `2026-05-22 01:30（Asia/Shanghai）`（相邻日期/跨时区）** | 政策标准 | 拟要求 AI 公司在发布前 **14–90 天** 向政府共享前沿模型的 EO **暂缓签署**；背景含 Anthropic Mythos、OpenAI GPT-5.5 Cyber 等安全能力争议 |
| 企业 AI 落地 | [From AI pilots to enterprise impact](https://blogs.microsoft.com/blog/2026/05/21/from-ai-pilots-to-enterprise-impact-why-execution-is-the-new-differentiator/) | **官方稿：`May 21, 2026`** | 官方发布 | Microsoft × EY **10 亿美元+** 联合计划；EY 作为 Customer Zero 披露 Copilot **94% 月活 / 85% 周活** 与 Finance/Tax/Assurance Agent 量化成效 |
| AI 硬件/消费 | [Hark raises $700M Series A](https://techcrunch.com/2026/05/21/hark-raises-700m-series-a-for-its-secretive-universal-ai-interface/) | **`May 21, 2026 7:00 AM PDT` → `2026-05-21 22:00（Asia/Shanghai）`** | 融资/产品 | Figure.AI 创始人 Brett Adcock 的 **通用 AI 界面 + 硬件** 路线获 **$700M A 轮**（估值 $6B）；计划夏季发布多模态模型 |
| AI 数学（延续） | [OpenAI model disproves discrete geometry conjecture](https://openai.com/index/model-disproves-discrete-geometry-conjecture/) | **官方稿：`May 20, 2026`；媒体持续：`May 21, 2026`** | 官方发布 | Erdős 平面单位距离问题 **首个 AI 自主证伪** 案例在 **`2026-05-21`** 继续发酵——研发侧应以 **PDF + companion remarks** 为证据链核心 |
| 版权/生成式 AI | [Spotify and Universal Music strike deal on AI covers and remixes](https://techcrunch.com/2026/05/21/spotify-and-universal-music-strike-deal-allowing-fan-made-ai-covers-and-remixes/) | **`May 21, 2026`** | 行业协议 | Premium 用户可创作 **AI cover/remix** 并分成——「consent, credit, compensation」框架或成内容平台模板 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| Claude Code 代码审查 | [Claude Code v2.1.146 Release Notes](https://github.com/anthropics/claude-code/releases/tag/v2.1.146) | `/code-review` effort level、MCP 分页、Windows 终端稳定性 | 日常 Claude Code 用户 / Windows 开发者 |
| Codex Goals 与远程控制 | [Codex 0.133.0 Release](https://github.com/openai/codex/releases/tag/rust-v0.133.0) | Goals DB、permission profiles、`remote-control` 前台 UX | Codex CLI / 插件扩展开发者 |
| OpenClaw Policy 与 Skill 安全 | [OpenClaw beta.2 Release](https://github.com/openclaw/openclaw/releases/tag/v2026.5.20-beta.2) | Policy 插件、Skill 必须通过 read tool 加载、Discord voice bootstrap | 自托管 Agent 平台工程 |
| 企业 Agent 规模化 | [Microsoft × EY 官方公告](https://news.microsoft.com/source/2026/05/21/ey-and-microsoft-announce-global-initiative-to-help-clients-scale-ai-enterprisewide-value-creation-and-move-beyond-experimentation/) | Forward Deployed Engineers、Frontier Firm 蓝图 | 企业架构 / 转型负责人 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：**Coding Agent 栈在「审查命令标准化 + 目标持久化 + 策略插件化」三处同时收敛**；消费侧 Agent 仍处 **多品牌、高付费、低统一入口** 阶段，与开源网关（OpenClaw）的 **Policy/Skill 安全收紧** 形成对照。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 代码审查 UX | Claude Code `/code-review` 取代 `/simplify` | 把「简化/审查」收敛为 **单一可配置 slash command**，降低团队培训成本 |
| 跨 turn 目标 | Codex Goals 默认开 + 专用 DB | 长任务 Agent 应 **持久化 goal 状态**，而非仅依赖上下文窗口 |
| 网关策略 | OpenClaw bundled Policy plugin | 频道合规、doctor lint、workspace repair 应 **插件化 + 可 opt-in 修复** |
| Skill 加载安全 | OpenClaw 移除 `cat SKILL.md` 兼容 | Skill 文件 **只经 read tool 加载**，executable 单独 allowlist——防 prompt 注入式 bypass |
| 企业落地度量 | EY Copilot 94% MAU | Agent 推广 KPI 应从 **试点满意度** 升级到 **周活/任务完成率/职能 ROI** |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **Claude Code v2.1.146** + **Codex rust-v0.133.0** Release Notes | 当日 **双 Coding Agent 发版**，直接影响日常工程工作流 |
| 必读 | **OpenClaw v2026.5.20-beta.2** | Policy 插件与 Skill 安全模型是 **自托管 Agent 治理** 样板 |
| 推荐 | TechCrunch：**Google Agent 生态** + **Trump 推迟 AI EO** | 理解 **产品付费墙** 与 **监管节奏** 对 Agent 路线的影响 |
| 延伸 | Microsoft Blog：**AI pilots → enterprise impact** | 大型企业 **从试点到生产** 的可量化参考 |

### 来源清单

- 检索范围：2026-05-21 00:00:00 到 2026-05-21 23:59:59（Asia/Shanghai）
- 引用域名：github.com, openai.com, blogs.microsoft.com, techcrunch.com, news.microsoft.com, developer.nvidia.com（相邻检索）
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 开源发布 | Claude Code v2.1.146 | 2026-05-21 | https://github.com/anthropics/claude-code/releases/tag/v2.1.146 |
| 开源发布 | Codex rust-v0.133.0 | 2026-05-21（相邻日期/跨时区发布） | https://github.com/openai/codex/releases/tag/rust-v0.133.0 |
| 开源发布 | OpenClaw v2026.5.20-beta.2 | 2026-05-21 | https://github.com/openclaw/openclaw/releases/tag/v2026.5.20-beta.2 |
| 官方发布 | Microsoft：From AI pilots to enterprise impact | 2026-05-21 | https://blogs.microsoft.com/blog/2026/05/21/from-ai-pilots-to-enterprise-impact-why-execution-is-the-new-differentiator/ |
| 官方发布 | Microsoft × EY 联合倡议 | 2026-05-21 | https://news.microsoft.com/source/2026/05/21/ey-and-microsoft-announce-global-initiative-to-help-clients-scale-ai-enterprisewide-value-creation-and-move-beyond-experimentation/ |
| 技术媒体 | Google Agent 生态质疑 | 2026-05-21 | https://techcrunch.com/2026/05/21/google-is-pitching-an-ai-agent-ecosystem-to-consumers-who-may-not-buy-it/ |
| 技术媒体 | Trump 推迟 AI 安全 EO | 2026-05-21（相邻日期/跨时区传播） | https://techcrunch.com/2026/05/21/trump-delays-ai-security-executive-order-i-dont-want-to-get-in-the-way-of-that-leading/ |
| 技术媒体 | Hark $700M Series A | 2026-05-21 | https://techcrunch.com/2026/05/21/hark-raises-700m-series-a-for-its-secretive-universal-ai-interface/ |
| 技术媒体 | Spotify × UMG AI covers 协议 | 2026-05-21 | https://techcrunch.com/2026/05/21/spotify-and-universal-music-strike-deal-allowing-fan-made-ai-covers-and-remixes/ |
| 官方发布 | OpenAI 离散几何证明（延续传播） | 2026-05-20（2026-05-21 持续讨论） | https://openai.com/index/model-disproves-discrete-geometry-conjecture/ |

## 2026-05-20

### 今日总览

**一句话结论**：`2026-05-20`（Asia/Shanghai，00:00–23:59）主线是 **OpenAI 通用推理模型自主证伪 Erdős 平面单位距离猜想**（附数学家 companion remarks 与 PDF 证明）与 **Agent 产品/技能生态继续分化**（Figma 画布内 AI Agent、NVIDIA AI-Q 深度研究 Skill、OpenClaw `alpha.1`）并行；监管侧 **欧盟委员会发布高风险 AI 系统分类草案指南**并开放公众咨询至 6 月 23 日。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | OpenAI 官方稿；TechCrunch/The Verge 跟进；NVIDIA Technical Blog；Figma 产品发布；EU AI Act 草案指南；Claude Code/Codex/OpenClaw/Hermes GitHub Release；arXiv/HF 论文；政策监管；中文补充 |
| 核心趋势 | **AI 数学推理从「营销争议」走向「可核验证明 + 外部数学家背书」**；**设计/办公/研究三类 Agent 各自强化「上下文 + 多 Agent 并行 + 企业数据不出域」**；**EU AI Act 高风险分类进入咨询期**，合规时间表与 Digital Omnibus 修订联动 |
| 可直接关注 | 研读 OpenAI **unit-distance proof + companion remarks** 评估「长链推理 + 跨领域连接」能力边界；设计/产品团队对照 **Figma 画布 Agent** 的多 Agent 协作模式；受监管行业跟进 **EU 高风险 AI 分类草案** 与 2027/2028 义务节点 |
| 专项检索结论 | **Claude Code**：未发现 **`2026-05-20（上海）`** 新 GitHub Release（最近 **`v2.1.145`** 为 **`2026-05-19`**）；**Codex**：未发现当日新 tag（**`rust-v0.131.0`** 仍属 **`2026-05-19`** 窗口）；**OpenClaw**：**`v2026.5.19-alpha.1`** **`Published: 2026-05-20T00:50:52Z` → `2026-05-20 08:50:52（Asia/Shanghai）`**；**Hermes**：未发现 **`2026-05-20`** 新 tag（最近 **`v2026.5.16`**）；**Spring AI / LangChain**：未发现与 **`2026-05-20`** 硬对齐的新 release/博文；**skills**：NVIDIA 发布 **AI-Q deep research skill**（Claude Code/Codex 可安装）；OpenClaw 侧新增 **meme-maker / autoreview** 等 skills 迭代 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| AI 数学 / 推理 | [An OpenAI model has disproved a central conjecture in discrete geometry](https://openai.com/index/model-disproves-discrete-geometry-conjecture/) | **官方稿：`May 20, 2026`** | 官方发布 | 通用推理模型给出 **平面单位距离问题**新下界构造（推翻「方格网格 essentially optimal」长期信念），附 [证明 PDF](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-proof.pdf) 与 [数学家 companion remarks](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-remarks.pdf)——评估 **长链推理可信度** 与 **跨代数数论×组合几何** 连接能力 |
| AI 数学（媒体） | [OpenAI claims it solved an 80-year-old math problem — for real this time](https://techcrunch.com/2026/05/20/openai-claims-it-solved-an-80-year-old-math-problem-for-real-this-time/) | **`May 20, 2026 1:28 PM PDT` → `2026-05-21 04:28（Asia/Shanghai）`（相邻日期/跨时区传播）** | 技术媒体 | 对照 **2025 年 GPT-5 Erdős 误报** 背景，说明本次附带 **Noga Alon / Thomas Bloom** 等外部数学家背书——研发侧应 **以 PDF+remarks 为准**，媒体作线索 |
| 教育 / 国家级部署 | [The next phase of OpenAI’s Education for Countries](https://openai.com/index/the-next-phase-of-education-for-countries/) | **官方稿：`May 20, 2026`** | 官方发布 | 伦敦 Education World Forum 公布首批国家进展（爱沙尼亚 2 万+ 学生等），**新加坡加入**；强调 **研究驱动部署 + ChatGPT Edu/Codex 本地化 + 教师培训** |
| 设计 Agent | [Figma adds an AI assistant to its collaborative canvas](https://techcrunch.com/2026/05/20/figma-adds-an-ai-assistant-to-its-collaborative-canvas/) | **`May 20, 2026 6:00 AM PDT` → `2026-05-20 21:00（Asia/Shanghai）`** | 产品发布 | 画布内 **自然语言驱动生成/编辑/自动化**，支持 **多 Agent 并行**；与既有 **Claude Code/Codex CLI 集成**形成「设计 + 代码」双栈 |
| Agent Skills / 企业研究 | [Add a Specialized Deep Research Skill to Agent Harnesses](https://developer.nvidia.com/blog/add-a-specialized-deep-research-skill-to-agent-harnesses/) | **官方稿：`May 20, 2026`** | 官方教程 | **AI-Q skill** 让 Claude Code/Codex 将深度研究 **委托给本地/托管 AI-Q 服务器**，返回 **带引用的结构化报告**；含 **MCP 认证数据源**集成模式——受监管行业 **数据不出域** 参考架构 |
| 政策 / EU AI Act | [European Commission Releases Draft Guidelines on High-Risk AI Under the EU AI Act](https://www.hunton.com/privacy-and-cybersecurity-law-blog/european-commission-releases-draft-guidelines-on-high-risk-ai-under-the-eu-ai-act) | **欧盟发布：`May 19, 2026`；公众咨询报道：`May 20, 2026`** | 政策标准 | **Article 6(5) 高风险 AI 分类草案指南**三部分（一般原则 / Annex I 产品安全 / Annex III 独立高风险场景）；咨询至 **2026-06-23**；义务节点延至 **2027-12-02 / 2028-08-02** |
| 桌面 Agent 创业 | [IrisGo, a startup backed by Andrew Ng, looks to become the AI desktop buddy](https://techcrunch.com/2026/05/20/irisgo-a-startup-backed-by-andrew-ng-looks-to-become-the-ai-desktop-buddy-you-never-knew-you-needed/) | **`May 20, 2026`** | 技术媒体 | **录一次流程、自动重复** 的桌面 companion；内置邮件/发票/报告 skills——对照 **Spark/OpenClaw** 的「常驻助手」产品形态 |
| OpenClaw | [openclaw/openclaw `v2026.5.19-alpha.1`](https://github.com/openclaw/openclaw/releases/tag/v2026.5.19-alpha.1) | GitHub **`Published: 2026-05-20T00:50:52Z` → `2026-05-20 08:50:52（Asia/Shanghai）`** | 开源预发布 | Mac Settings 卡片化、**`defineToolPlugin`**、**meme-maker skill**、browser **`--timeout-ms`**、Node **≥22.19**、Docker **`OPENCLAW_IMAGE_APT_PACKAGES`** |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| AI 数学证明 | OpenAI：**unit-distance proof + companion remarks** | 代数数论构造、外部数学家核验流程 | 研究/推理评测 / AI safety |
| Agent Skills 企业化 | NVIDIA：**AI-Q deep research skill** | SKILL.md + helper script + MCP 认证数据源 | Agent 平台 / 合规研发 |
| EU 合规准备 | EC 草案指南 + Digital Omnibus 时间表 | Annex I/III 分类、2027/2028 义务节点 | 法务 / 产品经理 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：**「通用 Agent 编排」与「垂直能力 Skill/Blueprint」继续解耦**——Figma/NVIDIA 分别把 **设计上下文** 与 **企业深度研究** 封装为可调用能力，OpenClaw 则在开源侧强化 **typed tool plugins + skills CLI**。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| Skill 标准化 | NVIDIA AI-Q skill 跨 Claude Code/Codex | 复杂子能力（研究/合规检索）应 **独立服务 + SKILL.md 契约**，而非塞进主 Agent prompt |
| 多 Agent UI | Figma 画布多 Agent 并行 | 产品层需 **会话/任务隔离 + 权限边界**，避免 Agent 互相覆盖设计状态 |
| 开源 Agent 网关 | OpenClaw **alpha.1** | **插件 SDK 版本化 + Node 基线抬升** 要纳入升级 runbook |
| 数学推理评测 | OpenAI unit-distance 证明 | 建立 **「官方 PDF + 外部数学家 remarks + 媒体二次核验」** 三源证据链，避免 repeat Weil 式误报 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | OpenAI：**An OpenAI model has disproved…** + PDF 证明 | 当日 **最具里程碑** 的可核验一手材料 |
| 必读 | NVIDIA：**Add a Specialized Deep Research Skill…** | **Agent Skills × 企业 MCP 数据源** 落地模板 |
| 推荐 | OpenAI：**The next phase of Education for Countries** | 国家级 **研究驱动 AI 部署** 指标与新加坡案例 |
| 推荐 | EU 高风险 AI 分类 **草案指南**（EC 链接见 Hunton 博文） | 2027 前 **产品分级与合规排期** 输入 |
| 延伸 | Figma AI assistant（TechCrunch） | **设计工具 Agent 化** 的产品交互参考 |

### 来源清单

- 检索范围：2026-05-20 00:00:00 到 2026-05-20 23:59:59（Asia/Shanghai），并对 **GitHub `Published`（UTC）**、媒体 **PDT/UTC** 做换算标注
- 引用域名：`openai.com`, `techcrunch.com`, `developer.nvidia.com`, `hunton.com`, `digital-strategy.ec.europa.eu`, `github.com`
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 官方发布 | OpenAI unit-distance conjecture disproof | **`May 20, 2026`** | https://openai.com/index/model-disproves-discrete-geometry-conjecture/ |
| 官方发布 | OpenAI Education for Countries next phase | **`May 20, 2026`** | https://openai.com/index/the-next-phase-of-education-for-countries/ |
| 官方教程 | NVIDIA AI-Q deep research skill | **`May 20, 2026`** | https://developer.nvidia.com/blog/add-a-specialized-deep-research-skill-to-agent-harnesses/ |
| 技术媒体 | OpenAI 80-year math problem | **相邻日期/跨时区传播** | https://techcrunch.com/2026/05/20/openai-claims-it-solved-an-80-year-old-math-problem-for-real-this-time/ |
| 技术媒体 | Figma AI assistant | **`May 20, 2026`（PDT→上海）** | https://techcrunch.com/2026/05/20/figma-adds-an-ai-assistant-to-its-collaborative-canvas/ |
| 技术媒体 | IrisGo desktop buddy | **`May 20, 2026`** | https://techcrunch.com/2026/05/20/irisgo-a-startup-backed-by-andrew-ng-looks-to-become-the-ai-desktop-buddy-you-never-knew-you-needed/ |
| 政策标准 | EU high-risk AI draft guidelines | **`May 19–20, 2026`** | https://www.hunton.com/privacy-and-cybersecurity-law-blog/european-commission-releases-draft-guidelines-on-high-risk-ai-under-the-eu-ai-act |
| 开源发布 | OpenClaw v2026.5.19-alpha.1 | **UTC→上海 `2026-05-20`** | https://github.com/openclaw/openclaw/releases/tag/v2026.5.19-alpha.1 |

## 2026-05-19

### 今日总览

**一句话结论**：`2026-05-19`（Asia/Shanghai，00:00–23:59）主线是 **Google I/O 2026 把「Agent 平台 + 分发」推到前台**（Gemini 3.5 Flash、Gemini Spark、Antigravity 2.0/CLI、Search Agent 化）与 **Anthropic/OpenAI 在「人才 + 平台 + 信任」三线并进**（Karpathy 加盟预训练、Claude Managed Agents/MCP tunnels、OpenAI 内容溯源 C2PA×SynthID）并行；工程侧 **Claude Code `v2.1.144`、Codex `0.131.0`、OpenClaw `v2026.5.19-beta.1`** 同日或按 UTC→上海换算落入当日窗口。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | Google I/O 官方稿与 blog.google；OpenAI 溯源公告；Anthropic 对话倡议 + API Release Notes + Karpathy 人事；Claude Code/Codex/OpenClaw GitHub Release；TechCrunch/The Verge；arXiv/HF 论文；政策/中文补充 |
| 核心趋势 | **Agent 从「聊天」转向「长时程执行 + 组织上下文」**：Spark/Antigravity/Search Agents 与 Zoom MCP（前日）形成「平台化 Agent」共振；**溯源与治理**（C2PA、SynthID、Anthropic 道德形成研究）与 **顶级预训练人才流动**同步升温 |
| 可直接关注 | 评估 **Gemini 3.5 Flash + Antigravity 2.0** 作为 coding/agent 基座；企业侧对照 **Claude Managed Agents** 的 MCP tunnels、自托管 sandbox、100K+ token spill；安全/合规团队跟进 **OpenAI 公开验证工具** 与 C2PA 互操作 |
| 专项检索结论 | **Claude Code**：**`v2.1.144`** GitHub **`Published: 2026-05-19T00:48:51Z` → `2026-05-19 08:48:51（Asia/Shanghai）`**；**Codex**：**`rust-v0.131.0`** **`Published: 2026-05-18T17:39:34Z` → `2026-05-19 01:39:34（Asia/Shanghai）`**；**OpenClaw**：**`v2026.5.19-beta.1`** **`Published: 2026-05-18T22:58:13Z` → `2026-05-19 06:58:13（Asia/Shanghai）`**；**Hermes**：未发现 **`2026-05-19（上海）`** 新 tag（最近 **`v2026.5.16`** 仍属 **`2026-05-16`** 窗口）；**Spring AI / LangChain**：未发现与 **`2026-05-19`** 硬对齐的新 release/博文；**skills**：Antigravity 2.0 延续 **Agent Skills/Hooks/Subagents** 能力栈，OpenClaw beta.1 侧继续 **typed tool plugins + autoreview/meme-maker** 等 skills 迭代 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| Google I/O / 模型 | [Google I/O 2026: Sundar Pichai’s opening keynote](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) | **官方稿：`May 19, 2026`** | 官方发布 | Gemini 3.5 Flash 成为 Gemini App/Search AI Mode 默认；宣布 **Gemini Spark**、**Gemini Omni**、Antigravity 2.0、Search Agent 化——「**模型 + 分发 + Agent 运行时**」一体化叙事 |
| Agent 模型 | [With Gemini 3.5 Flash, Google bets its next AI wave on agents, not chatbots](https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/) | **`May 19, 2026 10:51 AM PDT` → `2026-05-20 01:51（Asia/Shanghai）`（相邻日期/跨时区传播）** | 技术媒体 | 3.5 Flash 强调 **coding + 长时程 autonomous agents**；与 **Antigravity** 协同演示多 Agent 构建 OS——对 **agent harness 与默认模型选型**有直接参考 |
| 个人 Agent | [Google introduces Gemini Spark, a 24/7 agentic assistant with Gmail integration](https://techcrunch.com/2026/05/19/google-introduces-gemini-spark-a-24-7-agentic-assistant-with-gmail-integration/) | **`May 19, 2026 10:45 AM PDT` → `2026-05-20 01:45（Asia/Shanghai）`（相邻日期/跨时区传播）** | 技术媒体 | **Gmail/Workspace 原生集成 + Google Cloud VM 常驻**；MCP 扩展第三方——企业需提前设计 **邮箱/文档上下文的分级与审计** |
| Agent 开发平台 | [Google launches Antigravity 2.0 with an updated desktop app and CLI tool](https://techcrunch.com/2026/05/19/google-launches-antigravity-2-0-with-an-updated-desktop-app-and-cli-tool/) | **`May 19, 2026`（I/O 同日）** | 技术媒体 | 独立桌面 Agent IDE + **Antigravity CLI**（承接 Gemini CLI 能力栈）；对 **多 Agent 并行、后台任务、Subagents** 的工程落地是重要对照组 |
| 具身/世界模型 | [Google’s Genie world model can now simulate real streets with Street View](https://techcrunch.com/2026/05/19/googles-genie-world-model-can-now-simulate-real-streets-with-street-view/) | **`May 19, 2026`（I/O 同日）** | 技术媒体 | **Street View × Genie 3** 生成可交互 3D 环境——机器人/AV **仿真数据**与 **罕见场景**训练的新供给 |
| 内容溯源 | [Advancing content provenance for a safer, more transparent AI ecosystem](https://openai.com/index/advancing-content-provenance/) | **官方稿：`May 19, 2026`** | 官方发布 | **C2PA Conforming Generator** + 与 Google **SynthID 图像水印**合作 + **[公开验证工具预览](https://openai.com/verify)**——生成式媒体 **合规/风控/平台治理**必读 |
| 治理 / 价值观 | [Widening the conversation on frontier AI](https://www.anthropic.com/news/widening-conversation-ai) | **官方稿：`May 19, 2026`** | 官方发布 | 与宗教/哲学/文化社群对话 **AI 道德形成**；实验 **「外部良知」工具**降低 misalignment——对 **Constitution/评测集设计**有方法论启发 |
| Claude API / Agent 平台 | [Claude Platform Release Notes — May 19, 2026](https://docs.anthropic.com/en/release-notes/api) | **`May 19, 2026`** | 官方文档 | **MCP tunnels（RP）**、**Claude Managed Agents 自托管 sandbox**、会话内更新 MCP 配置、**>100K token 输出 spill 到 sandbox 文件** |
| 人事 / 预训练 | [OpenAI co-founder Andrej Karpathy joins Anthropic's pre-training team](https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/) | **`May 19, 2026 8:43 AM PDT` → `2026-05-19 23:43（Asia/Shanghai）`** | 技术媒体 | Karpathy 加入 **pre-training**，将建 **「用 Claude 加速预训练研究」**团队——信号：**AI-assisted research** 与纯算力堆叠并重 |
| Claude Code | [anthropics/claude-code `v2.1.144`](https://github.com/anthropics/claude-code/releases/tag/v2.1.144) | GitHub **`Published: 2026-05-19T00:48:51Z` → `2026-05-19 08:48:51（Asia/Shanghai）`** | 开源发布 | **`/resume` 支持 background sessions**、MCP 分页 tools 修复、启动/API 不可达 **75s 挂起→15s 超时**、Windows/CJK 渲染多项修复 |
| Codex | [openai/codex `rust-v0.131.0`](https://github.com/openai/codex/releases/tag/rust-v0.131.0) | GitHub **`Published: 2026-05-18T17:39:34Z` → `2026-05-19 01:39:34（Asia/Shanghai）`** | 开源发布 | TUI 会话控制增强、**@mentions** 跨文件/插件/skills 搜索、**`codex doctor`** 诊断、远程 daemon/Windows sandbox 硬化 |
| OpenClaw | [openclaw/openclaw `v2026.5.19-beta.1`](https://github.com/openclaw/openclaw/releases/tag/v2026.5.19-beta.1) | GitHub **`Published: 2026-05-18T22:58:13Z` → `2026-05-19 06:58:13（Asia/Shanghai）`** | 开源预发布 | Mac Settings 卡片化、**`defineToolPlugin`**、browser CLI **`--timeout-ms`**、Node **≥22.19**、Docker **`OPENCLAW_IMAGE_APT_PACKAGES`** |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| Google Agent 栈 | I/O Keynote + Antigravity 2.0 稿 | 3.5 Flash、Spark、Antigravity CLI、Search Agents | 平台/全栈 / Agent 架构 |
| 溯源互操作 | OpenAI：**Advancing content provenance** | C2PA、SynthID、verify 工具边界 | 安全/合规 / 媒体平台 |
| Claude 企业 Agent | Anthropic API Release Notes（5/19） | MCP tunnels、自托管 sandbox、大输出 spill | 后端 / 集成工程师 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：**Google 用「默认模型 + Agent 运行时 + Workspace 分发」打组合拳**；Anthropic 则在 **Managed Agents 私有化执行**与 **预训练人才**上加深护城河；OpenAI 同日补 **跨平台溯源**这一「信任基础设施」。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| Agent 运行时竞争 | Antigravity 2.0 / Spark / Claude Managed Agents | 选型时对比 **常驻 VM、MCP 扩展、后台 subagent、权限/审计**四件套 |
| MCP 企业化 | Anthropic **MCP tunnels** + Google Spark MCP 路线图 | 内网 MCP Server 需 **隧道/零信任**方案，别直接把 localhost 暴露给云端 |
| 大工具输出 | Managed Agents **100K+ token spill to file** | 长日志/抓取结果应 **文件化 + 截断预览**，避免撑爆 context |
| 开源 Agent 网关 | OpenClaw **beta.1** 周更 | **插件 SDK + QA gates** 是长期维护成本，应纳入 SRE 预算 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | Google I/O 2026 Keynote（blog.google） | 当日 **Agent 化产品矩阵**的一手叙事 |
| 必读 | OpenAI：**Advancing content provenance** | 看清 **C2PA × SynthID × 公开 verify** 如何组合 |
| 推荐 | Anthropic API Release Notes（**May 19**） | **MCP tunnels / 自托管 sandbox** 的企业落地细节 |
| 推荐 | Claude Code **`v2.1.144` release notes** | 终端 Agent **稳定性/MCP/background session** 修复面 |

### 来源清单

- 检索范围：2026-05-19 00:00:00 到 2026-05-19 23:59:59（Asia/Shanghai），并对 **GitHub `Published`（UTC）**、媒体 **PDT/UTC** 做换算标注
- 引用域名：`blog.google`, `techcrunch.com`, `openai.com`, `anthropic.com`, `docs.anthropic.com`, `github.com`, `theverge.com`, `arxiv.org`
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 官方发布 | Google I/O 2026 Keynote | **`May 19, 2026`** | https://blog.google/innovation-and-ai/sundar-pichai-io-2026/ |
| 官方发布 | OpenAI content provenance | **`May 19, 2026`** | https://openai.com/index/advancing-content-provenance/ |
| 官方发布 | Anthropic widening conversation | **`May 19, 2026`** | https://www.anthropic.com/news/widening-conversation-ai |
| 官方文档 | Claude API Release Notes | **`May 19, 2026`** | https://docs.anthropic.com/en/release-notes/api |
| 技术媒体 | Gemini 3.5 Flash agents | **相邻日期/跨时区传播** | https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/ |
| 技术媒体 | Gemini Spark | **相邻日期/跨时区传播** | https://techcrunch.com/2026/05/19/google-introduces-gemini-spark-a-24-7-agentic-assistant-with-gmail-integration/ |
| 技术媒体 | Antigravity 2.0 | **`May 19, 2026`** | https://techcrunch.com/2026/05/19/google-launches-antigravity-2-0-with-an-updated-desktop-app-and-cli-tool/ |
| 技术媒体 | Genie × Street View | **`May 19, 2026`** | https://techcrunch.com/2026/05/19/googles-genie-world-model-can-now-simulate-real-streets-with-street-view/ |
| 技术媒体 | Karpathy → Anthropic | **上海 `2026-05-19`（PDT→上海）** | https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/ |
| 开源发布 | Claude Code v2.1.144 | **UTC→上海 `2026-05-19`** | https://github.com/anthropics/claude-code/releases/tag/v2.1.144 |
| 开源发布 | Codex rust-v0.131.0 | **UTC→上海 `2026-05-19`** | https://github.com/openai/codex/releases/tag/rust-v0.131.0 |
| 开源发布 | OpenClaw v2026.5.19-beta.1 | **UTC→上海 `2026-05-19`** | https://github.com/openclaw/openclaw/releases/tag/v2026.5.19-beta.1 |

## 2026-05-18

### 今日总览

**一句话结论**：`2026-05-18`（Asia/Shanghai，00:00–23:59）主线是「**开源 Agent 网关密集迭代（OpenClaw `v2026.5.16-beta.5` 的 GitHub `Published` 换算落入上海当日凌晨）** × **企业协作厂商把会议与会话上下文通过 MCP 推进到 Codex / Claude 工具链（Zoom 官方稿 `Published May 18, 2026`）** × **涉 OpenAI 组织形态与 Altman 的诉讼以“程序法窗口”收束（陪审团裁决 + 大量美媒 UTC/美西时间戳换算后落入上海次日）**」并行；同日 **患者侧 AI 就诊笔记（Kin Health 种子轮）**与 **HF Daily `2026-05-18` 上的 Agent/RAG/浏览器 Agent 指纹论文**补充研发视角。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | OpenClaw GitHub Release（UTC→上海）；Zoom MCP 新闻稿与 Codex 插件仓库线索；Musk v. Altman 陪审团进展（The Verge / TechCrunch）；Schiff 数据中心能源法案快讯（The Verge）；患者侧 AI notetaker 融资（TechCrunch）；Hugging Face Daily Papers `2026-05-18`；Codex / Claude Code / Hermes / Spring AI / LangChain / skills 专项；arXiv 核对 |
| 核心趋势 | **Agent 基础设施继续“平台化”**：网关侧一周多更 + 会议厂商把 **组织上下文**接进 MCP；**法律战**短期落到 **诉讼时效与程序**，但 **治理与信任**议题不会消失；**医疗 + LLM**仍在 **准确率/同意/HIPAA**张力下扩张 |
| 可直接关注 | 维护 OpenClaw/Codex 集成：跟踪 **typed tool plugins、代理 TLS、QA-Lab parity**；企业 AI：评估 **Zoom MCP**时的 **数据驻留、审计、最小权限**；安全：**浏览器 Agent 可被动指纹识别**意味着你要重新设计 **流量与脚本策略** |
| 专项检索结论 | **Codex**：未发现 **`Published` 落入上海 `2026-05-18`** 的新稳定版 tag（以 `openai/codex` releases 为准）；**Claude Code**：未发现 **`2026-05-18（上海）`** 强对齐的新 GitHub Release tag；**OpenClaw**：**`v2026.5.16-beta.5`** GitHub **`Published: 2026-05-17T17:59:02Z` → `2026-05-18 01:59:02（Asia/Shanghai）`**，**落入**当日窗口；**Hermes**：未发现 **`2026-05-18（上海）`** 新 tag（`v2026.5.16` 仍属此前窗口）；**Spring AI / LangChain**：未发现与 **`2026-05-18`** 日期字段硬对齐的新博文/变更日志条目；**skills**：以 **OpenClaw beta.5**（meme-maker、`autoreview`、node inspector、Python debug、`defineToolPlugin` 等）与 **Zoom×Codex** 物料为主 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| 多通道 Agent 网关 | [openclaw/openclaw `v2026.5.16-beta.5`](https://github.com/openclaw/openclaw/releases/tag/v2026.5.16-beta.5) | GitHub **`Published: 2026-05-17T17:59:02Z` → `2026-05-18 01:59:02（Asia/Shanghai）`** | 开源预发布 | Mac 端 Settings 卡片化、**`defineToolPlugin` + plugins build/validate/init**、HTTPS 托管 forward-proxy、**meme-maker / autoreview / node inspector / Python debug** 等 skills、QA-Lab 与 runtime parity 闸门强化——典型“**生产型 Agent 平台周更**” |
| 企业 MCP / 会议智能 | [Zoom connects conversations and organizational context across AI tools through expanded MCP capabilities](https://news.zoom.com/zoom-mcp-expanded-capabilities/) | **官方稿：`Published May 18, 2026`** | 官方新闻稿 | 将 **会议摘要/转写/录制/Notes**与 **Salesforce、Workday、ServiceNow** 等接进 **MCP Server**，并宣布 **OpenAI Codex 插件**与 **Claude 插件**路径——企业要把 **上下文治理**前置到集成设计 |
| Codex 插件物料 | [openai/plugins：`plugins/zoom`](https://github.com/openai/plugins/tree/main/plugins/zoom)（Zoom 稿内链接） | **与 Zoom 官方稿同日宣发（以稿件为准）** | 开源插件目录 | 把 **会议可验证事实**导入 **编码侧文档化/自动化**的参考接线 |
| 诉讼 / 治理 | [Elon Musk loses his case against Sam Altman \| The Verge](https://www.theverge.com/ai-artificial-intelligence/932383/jury-verdict-musk-v-altman-openai-trial) | **`May 18, 2026, 5:39 PM UTC` → `2026-05-19 01:39（Asia/Shanghai）`（相邻日期/跨时区传播）** | 技术媒体 | 咨询陪审团：两条主张 **诉讼时效**挡下，另一条连带失败；**法官接受意见**；对 **非营利/关联交易叙事**的工程组织仍具 **合规对照**价值 |
| 诉讼 / 产业 | [Elon Musk has lost his lawsuit against Sam Altman and OpenAI \| TechCrunch](https://techcrunch.com/2026/05/18/elon-musk-has-lost-his-lawsuit-against-sam-altman-and-openai/) | **`May 18, 2026 10:34 AM PDT` → `2026-05-19 01:34（Asia/Shanghai）`（相邻日期/跨时区传播）** | 技术媒体 | 更偏 **程序法**：陪审团认为 **提起过晚**；强调 **IPO 前“结构性威胁”之一被移开** |
| 政策 / 数据中心 | [A new bill aims to shield energy consumers from AI data center-related costs \| The Verge](https://www.theverge.com/policy/932472/a-new-bill-aims-to-shield-energy-consumers-from-ai-data-center-related-costs) | **`Posted May 18, 2026 at 5:56 PM UTC` → `2026-05-19 01:56（Asia/Shanghai）`（相邻日期/跨时区传播）** | 技术媒体（ linked 参议员公告） | **Energy Cost Fairness and Reliability Act**：对“**energy-intensive facilities**”提要求以缓解电网压力——算力扩张进入 **立法与电价分配**讨论 |
| 医疗 × LLM 产品 | [Kin Health raises $9M to build an AI notetaker for patients \| TechCrunch](https://techcrunch.com/2026/05/18/kin-health-raises-9m-to-build-an-ai-notetaker-for-patients/) | **`May 18, 2026 8:26 AM PDT` → `2026-05-18 23:26（Asia/Shanghai）`** | 技术媒体 | 患者侧 **录音→临床叙事→摘要**流水线；**未宣称 HIPAA 认证**但强调加密与默认私有——对 **同意/准确性/责任边界**要按监管口径自己再核验 |
| 论文（Agent/编程） | [Solvita: Enhancing Large Language Models for Competitive Programming via Agentic Evolution](https://arxiv.org/abs/2605.15301) | **见于** HF Daily [`2026-05-18`](https://huggingface.co/papers/date/2026-05-18)；**arXiv 版本历史以 abs 页为准** | 论文原文 | **Planner/Solver/Oracle/Hacker** 闭环 + **图结构知识网络**沉淀经验，强调 **竞赛编程 Agent** 的可演进性 |
| 论文（安全 × Browser Agent） | [Known By Their Actions: Fingerprinting LLM Browser Agents via UI Traces](https://arxiv.org/abs/2605.14786) | **见于** HF Daily [`2026-05-18`](https://huggingface.co/papers/date/2026-05-18) | 论文原文 | **被动 UI traces** 可对 **14 个前沿模型**做高 F1 **指纹识别**——对 **客户端自动化、Bot 治理、红队**有直接含义 |
| 论文（RAG 评测） | [MLAIRE: Multilingual Language-Aware Information Retrieval Evaluation Protocal](https://arxiv.org/abs/2605.07249) | **见于** HF Daily [`2026-05-18`](https://huggingface.co/papers/date/2026-05-18) | 论文原文 | 把 **跨语语义相关**与 **query-language preference**拆开评测——多语 **RAG/搜索引擎**上线前的指标设计参考 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| OpenClaw 变更阅读 | OpenClaw Release **`v2026.5.16-beta.5`** | tool plugins、代理 TLS、skills、QA gates | Agent 平台 / SRE |
| MCP 集成 | Zoom 官方稿 + `openai/plugins` Zoom 目录 | MCP server、Codex 插件、企业系统连接器 | 企业架构 / 集成工程师 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：工程热点在 **“把组织上下文接到工具协议上”**（Zoom MCP）与 **“把 Agent 网关打磨到可发布节奏”**（OpenClaw）；论文侧则提醒 **浏览器 Agent 的匿名性假设可能不成立**。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| MCP 作为上下文总线 | Zoom：会议智能 + CRM/ITSM | 企业侧需要 **数据分级、检索边界、审计追踪**与 **MCP Server 版本治理** |
| 网关交付 | OpenClaw beta.5 | **插件工具链 + QA-Lab**是长期维护成本中心，要提前预算 |
| 评测 | MLAIRE / Solvita / “Known By Their Actions” | **多语 RAG**要同时看 **语义与可读语言**；**浏览器自动化**要假设 **可被站点侧观测** |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | OpenClaw：**`v2026.5.16-beta.5` notes** | 直接反映 **Agent 网关**一周内的真实修复面 |
| 必读 | arXiv：**2605.14786（Browser Agent fingerprint）** | 安全与产品设计交叉点 |
| 推荐 | Zoom：**expanded MCP** 官方稿 | 看清 **“会议上下文商品化”**的接口与叙事 |

### 来源清单

- 检索范围：2026-05-18 00:00:00 到 2026-05-18 23:59:59（Asia/Shanghai），并对 **GitHub `Published`（UTC）**、媒体 **UTC/PDT** 做换算标注
- 引用域名：`github.com`, `news.zoom.com`, `theverge.com`, `techcrunch.com`, `schiff.senate.gov`（linked）, `huggingface.co`, `arxiv.org`
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 开源发布 | OpenClaw `v2026.5.16-beta.5` | **UTC→上海 `2026-05-18`** | https://github.com/openclaw/openclaw/releases/tag/v2026.5.16-beta.5 |
| 官方新闻稿 | Zoom expanded MCP | **`Published May 18, 2026`** | https://news.zoom.com/zoom-mcp-expanded-capabilities/ |
| 技术媒体 | Musk loses（The Verge） | **相邻日期/跨时区传播** | https://www.theverge.com/ai-artificial-intelligence/932383/jury-verdict-musk-v-altman-openai-trial |
| 技术媒体 | Musk loses（TechCrunch） | **相邻日期/跨时区传播** | https://techcrunch.com/2026/05/18/elon-musk-has-lost-his-lawsuit-against-sam-altman-and-openai/ |
| 技术媒体 | Schiff energy bill | **相邻日期/跨时区传播** | https://www.theverge.com/policy/932472/a-new-bill-aims-to-shield-energy-consumers-from-ai-data-center-related-costs |
| 技术媒体 | Kin Health $9M | **上海 `2026-05-18`**（PDT→上海） | https://techcrunch.com/2026/05/18/kin-health-raises-9m-to-build-an-ai-notetaker-for-patients/ |
| 论文聚合 | Hugging Face Daily Papers | **列表页：`2026-05-18`** | https://huggingface.co/papers/date/2026-05-18 |
| 论文原文 | Solvita | **以 arXiv 为准** | https://arxiv.org/abs/2605.15301 |
| 论文原文 | Known By Their Actions | **以 arXiv 为准** | https://arxiv.org/abs/2605.14786 |
| 论文原文 | MLAIRE | **以 arXiv 为准** | https://arxiv.org/abs/2605.07249 |

## 2026-05-17

### 今日总览

**一句话结论**：`2026-05-17`（Asia/Shanghai，00:00–23:59）在「工程事实」层面最明显的是 **MCP Streamable HTTP 在 `initialize` 阶段对 `MCP-Protocol-Version` 头与 JSON-RPC body 的一致性处理被公开质疑并进入社区修复讨论**；在「舆论议程」层面，美媒同日密集讨论 **苹果下一代 Siri（Gemini + 自动删除聊天记录）**、**Musk v. OpenAI 收尾阶段对“信任”的放大器效应**、以及 **高校毕业典礼上对 AI 叙事的公开反弹**，但这些稿件的站点时间戳在换算到 **Asia/Shanghai** 后往往落在 **2026-05-18 凌晨**，需要按 **相邻日期/跨时区传播**阅读。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | MCP / Agent 网关工程（GitHub Issue PR 线程）；消费级 AI 产品链（Bloomberg 线索 × TechCrunch）；通用办公协同里的 CV/分割遗留能力退役（Microsoft 官方社区 × The Verge）；长周期 Agent 评测论文管线（Hugging Face Daily Papers `2026-05-17` × arXiv）；汽车业“AI skills swap”与岗位结构（TechCrunch Mobility）；诉讼与公共叙事（TechCrunch）；开源 CLI Agent 发布脉冲（GitHub `Published` UTC→上海_calibration）；Claude Code / Codex / OpenClaw / Hermes / Spring AI / LangChain / skills 专项检索 |
| 核心趋势 | **协议层一致性会先变成“可观测 bug”**：MCP 这类强工具协议在跨网关部署时，**header vs body** 的权威来源必须工程化；**信任变成显式产品叙事**：苹果试图用 **数据留存策略**对冲第三方模型能力叙事；**社会对 AI 的反感**正在从线上投票转向 **线下公共仪式（毕业典礼）** |
| 可直接关注 | 做 MCP 网关：把 **initialize 的 version negotiation**做成可回归测试；做国家/企业落地：把 **“模型由谁运行、日志与留存周期、第三方处理者条款”**写成可审计清单；做 Agent 平台：用 **WildClawBench** 这类“真实 runtime + 长 horizon”基准校准你对 scaffold 的信心 |
| 专项检索结论 | **Codex**：未发现 GitHub `openai/codex` 的 **`Published` 落入上海 `2026-05-17`** 新稳定版 tag（近期可见 alpha 线仍集中在 **2026-05-12** 前后，需以 releases 页为准）；**Claude Code**：未发现 **`2026-05-17（上海）`** 强对齐的新 GitHub Release tag；**OpenClaw**：`v2026.5.16-beta.5` 的 GitHub **`Published: 2026-05-17T17:59:02Z` → `2026-05-18 01:59:32（Asia/Shanghai）`**，**不计入**本节严格日窗，但建议 **`2026-05-18`** digest 作为高频跟进；**Hermes**：`v2026.5.16` 落在 **`2026-05-16`** 窗口，本节不再重复展开；**Spring AI**：未发现 `spring.io/blog` 与 **`2026-05-17`** 日期字段硬对齐的新条目；**LangChain**：未发现 `changelog.langchain.com` / `blog.langchain.com` 与 **`2026-05-17`** 同日落款；**skills**：OpenClaw beta.5 含多项 **skills / tool plugin**增量，但 **`Published` 换算后为上海次日** |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| MCP / HTTP 互操作 | [Issue #2108：`MCP-Protocol-Version` header 与 body `protocolVersion` 在 `initialize` 不一致时仍被接受](https://github.com/modelcontextprotocol/typescript-sdk/issues/2108) | **Updated `2026-05-17T14:18:44Z` → `2026-05-17 22:18:44（Asia/Shanghai）`** | 开源缺陷报告 + 修复讨论（链接到 PR `#2111` 线索） | 这类问题会被 **API 网关、观测平台、审计日志**放大；应当把 **协商权威来源**写入实现与测试 |
| 消费级 AI 隐私叙事 | [Apple’s Siri revamp could include auto-deleting chats \| TechCrunch](https://techcrunch.com/2026/05/17/apples-siri-revamp-could-include-auto-deleting-chats/)（引用 Bloomberg） | **TechCrunch：`May 17, 2026 1:15 PM PDT` → `2026-05-18 04:15（Asia/Shanghai）`（相邻日期/跨时区传播）** | 技术媒体 | 独立 App × **Gemini** × **可配置留存周期**，本质是 **“第三方模型 + 第一方隐私承诺”**的产品结构设计题 |
| 诉讼 / 产业信任 | [Why trust is a big question at the Elon Musk-OpenAI trial \| TechCrunch](https://techcrunch.com/2026/05/17/why-trust-is-a-big-question-at-the-elon-musk-openai-trial/) | **`May 17, 2026 12:46 PM PDT` → `2026-05-18 03:46（Asia/Shanghai）`（相邻日期/跨时区传播）** | 技术媒体 | 对 **公司治理、对外陈述一致性、监管沟通**是提醒：信任不是公关辞令，是 **可验证事实集合** |
| 公共舆论 / AI 接受度 | [University of Arizona students boo Eric Schmidt’s AI cheerleading during commencement \| The Verge](https://www.theverge.com/ai-artificial-intelligence/932203/university-of-arizona-students-boo-eric-schmidt-ai-commencement) | **`May 17, 2026, 5:22 PM UTC` → `2026-05-18 01:22（Asia/Shanghai）`（相邻日期/跨时区传播）** | 技术媒体 | **人才市场体感**会反过来影响政策与企业内训；对 HR/TL 是“别说教，先展示可验证收益”的信号 |
| Teams / CV 功能退役 | [Microsoft is retiring Teams’ Together Mode \| The Verge](https://www.theverge.com/tech/932215/microsoft-teams-together-mode) | **The Verge：`May 17, 2026, 9:15 PM UTC` → `2026-05-18 05:15（Asia/Shanghai）`（相邻日期/跨时区传播）**；微软官方公告见下 | 技术媒体（引用官方社区） | Together Mode **用分割/抠像把头像摆进虚拟会议室**；退役说明 **“AI/CV 加持的协同特性”也要服从总体 UX / 性能预算** |
| Teams / 官方说明 | [Goodbye Together mode, hello simplified meeting layouts in Microsoft Teams](https://techcommunity.microsoft.com/blog/microsoft365insiderblog/goodbye-together-mode-hello-simplified-meeting-layouts-in-microsoft-teams/4519312) | **Microsoft Community Hub 帖子落款：`May 14, 2026`（相邻日期）** | 厂商官方社区 | 以 **现代画廊视图**承接多路视频；对做实时音视频与 CV 插件的人是“功能生命周期管理”的样本 |
| 产业组织 / skills | [TechCrunch Mobility: The AI skills arms race is coming for automotive](https://techcrunch.com/2026/05/17/techcrunch-mobility-the-ai-skills-arms-race-is-coming-for-automotive/) | **`May 17, 2026 9:05 AM PDT` → `2026-05-18 00:05（Asia/Shanghai）`（相邻日期/跨时区传播）** | 技术媒体 | **裁撤传统 IT 岗 × 招聘 AI-native 工程**的结构性叙事；对你意味着团队技能模型与预算要先改 |
| Agent 评测 / 论文 | [WildClawBench: A Benchmark for Real-World, Long-Horizon Agent Evaluation](https://arxiv.org/abs/2605.10912) | **见于** HF Daily Papers [`2026-05-17`](https://huggingface.co/papers/date/2026-05-17) 列表；**arXiv 版本日以 abs 页 Submission history 为准** | 论文原文 | 直接把 **OpenClaw / Claude Code / Codex / Hermes** 接进容器化 harness，强调 **轨迹、工具副作用与判分** |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| MCP 协议对齐 | `typescript-sdk`：**Issue #2108** 及关联 **PR #2111**（见 Issue 时间线） | Streamable HTTP、`initialize`、header/body 一致性 | MCP Server/Client 维护者、网关作者 |
| Agent 评测 | **WildClawBench**（GitHub：`internlm/WildClawBench`） | native runtime、dockerized harness、hybrid grading | Agent 平台 / 评测负责人 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：这一天更像「**协议与评测基础设施**在收紧」：**MCP**把版本协商细节暴露成缺陷；**WildClawBench**把“scaffold 不是附带物”写进分数差异里。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| MCP 网关 | `initialize` mismatch 可被接受 | 把 **“header 与 body 是否必须一致”**定义成明确策略，并 **用集成测试锁住** |
| 长周期 Agent | WildClawBench：换 harness 可巨幅改分 | 你的 Agent 系统评估必须 **固定 harness 版本与工具白名单** |
| OpenClaw 工具面 | `v2026.5.16-beta.5`（`Published`→上海次日）包含 **typed tool plugins / skills**增量 | **关注次日章节**以免漏掉高频平台变更 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | **MCP `typescript-sdk`：Issue #2108** | 这是典型的 **“协议实现细节 → 线上诡异故障”**入口 |
| 必读 | **WildClawBench（2605.10912）** | 把评测从“答对了吗”推进到“**怎么在真实 runtime 里做错/做对**” |
| 推荐 | **TechCrunch：Siri / Gemini / auto-delete** | 观察 **平台公司如何把隐私叙事产品化** |

### 来源清单

- 检索范围：2026-05-17 00:00:00 到 2026-05-17 23:59:59（Asia/Shanghai），并对 **GitHub / 媒体 UTC & 美西时间**做换算标注
- 引用域名：`github.com`, `techcrunch.com`, `theverge.com`, `techcommunity.microsoft.com`, `huggingface.co`, `arxiv.org`
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 开源缺陷 | MCP TS SDK Issue #2108 | **Updated UTC→上海 `2026-05-17`** | https://github.com/modelcontextprotocol/typescript-sdk/issues/2108 |
| 技术媒体 | Apple Siri auto-deleting chats | **相邻日期/跨时区传播（上海 `2026-05-18` 早盘）** | https://techcrunch.com/2026/05/17/apples-siri-revamp-could-include-auto-deleting-chats/ |
| 技术媒体 | Musk-OpenAI trial trust | **相邻日期/跨时区传播（上海 `2026-05-18`）** | https://techcrunch.com/2026/05/17/why-trust-is-a-big-question-at-the-elon-musk-openai-trial/ |
| 技术媒体 | Schmidt commencement booed | **相邻日期/跨时区传播（上海 `2026-05-18`）** | https://www.theverge.com/ai-artificial-intelligence/932203/university-of-arizona-students-boo-eric-schmidt-ai-commencement |
| 技术媒体 | Teams Together Mode retired | **相邻日期/跨时区传播**；**官方社区 `May 14, 2026`** | https://www.theverge.com/tech/932215/microsoft-teams-together-mode |
| 厂商社区 | Goodbye Together mode（Teams） | **`May 14, 2026`** | https://techcommunity.microsoft.com/blog/microsoft365insiderblog/goodbye-together-mode-hello-simplified-meeting-layouts-in-microsoft-teams/4519312 |
| 技术媒体 | AI skills arms race（automotive） | **相邻日期/跨时区传播** | https://techcrunch.com/2026/05/17/techcrunch-mobility-the-ai-skills-arms-race-is-coming-for-automotive/ |
| 论文聚合 | Hugging Face Daily Papers | **列表页：`2026-05-17`** | https://huggingface.co/papers/date/2026-05-17 |
| 论文原文 | WildClawBench | **以 arXiv 版本历史为准** | https://arxiv.org/abs/2605.10912 |
| 开源发布（次日窗） | OpenClaw `v2026.5.16-beta.5` | **`Published` UTC→上海 `2026-05-18 01:59`** | https://github.com/openclaw/openclaw/releases/tag/v2026.5.16-beta.5 |

## 2026-05-16

### 今日总览

**一句话结论**：`2026-05-16`（Asia/Shanghai，00:00–23:59）更像「**开源 Agent 网关继续把 Codex / MCP / 多端可靠性打穿（OpenClaw `v2026.5.16-beta.1`）** × **平台与媒体侧同步收紧“深度伪造/生成式滥用”的治理边界（YouTube 扩展 AI likeness 检测、arXiv 对 LLM 残留证据的硬惩罚叙事）** × **OpenAI 用国家级落地样本推进“可用智能+素养教育”（Malta × ChatGPT Plus）**」三条主线并行；同时 **Databricks OfficeQA Pro / GPT‑5.5** 等案例文仍标注在 **OpenAI 站点的 `May 15, 2026`**，更适合作为 **相邻日期/隔夜传播**阅读。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | OpenClaw GitHub Release（`Published` UTC→上海校准）；OpenAI 官网 Malta 合作（页面日期 `May 16, 2026`）；The Verge（YouTube likeness、arXiv 治理）；Hugging Face Daily Papers `2026-05-16` 列表抽样；OpenAI×Databricks 案例页（页面日期 `May 15, 2026`）；Claude Code / `openai/codex` releases 专项；Spring AI / LangChain 博客日期硬对齐；skills/Agent Skills 线索（OpenClaw `resolvedSkills` 缓存）；中文补充（机器之心/量子位 **`2026-05-16` 同日强匹配主编发**：本次检索未稳定命中） |
| 核心趋势 | **运行时工程仍是最硬仗**：同一日在 OpenClaw 里能看到 **Codex app-server 线程绑定/Compaction/超时**、**MCP 与审批模式**、以及 **多通道可靠性**的一组“生产事故型修复”集合；**治理从内容平台向学术基础设施外溢**：arXiv 对“不可辩驳的 LLM 生成残留证据”的处罚叙事，会反向推动团队内部的 **生成式产出审计链**；**国家样本**：Malta 把 **素养课程 + 一年期 Plus**做成“可复制的公共政策抓手” |
| 可直接关注 | 做多供应商 Agent 网关：把 **MCP 作用域、审批模式、线程/Compaction 事件语义**纳入 SLO；做企业知识库/助手：把 **implicit conflict（记忆被间接推翻）**从评测（如 STALE）反推为 **状态机式的记忆写入策略**；做内容与社区产品：对照 YouTube likeness 机制，复盘 **人脸/肖像权/恶搞例外**边界 |
| 专项检索结论 | **Codex**：**未发现** GitHub `openai/codex` 在 **`2026-05-16（上海）`**窗口内的 **新 Release tag**（以 releases 检索为准；工程叙事可参考 OpenAI×Databricks 案例页，但其 **OpenAI 页面落款为 `May 15, 2026`**）；**Claude Code**：**未发现**同日强对齐的新 GitHub Release tag；**OpenClaw**：**`v2026.5.16-beta.1`** GitHub **`Published: 2026-05-16T01:33:32Z`** → **`2026-05-16 09:33:32（Asia/Shanghai）`**，**落入**当日窗口；**Hermes**：**未发现**与 **`2026-05-16（上海）`**强绑定的新 **`NousResearch/hermes-agent` tag**（第三方传播不作为硬事实）；**Spring AI**：**未发现** `spring.io/blog` 与 **`2026-05-16`**日期字段硬对齐的新条目；**MCP**：以 **OpenClaw**同日说明为主（**Codex app-server/MCP：按 agent id 限定 user MCP servers + 审批默认**）；**skills**：OpenClaw 变更包含 **`resolvedSkills` hydration 缓存**（减少 warm gateway 上的重复 skill 快照重建） |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| 多通道 Agent 网关 | [openclaw/openclaw `v2026.5.16-beta.1`](https://github.com/openclaw/openclaw/releases/tag/v2026.5.16-beta.1) | GitHub **`Published` `2026-05-16T01:33:32Z`** → **`2026-05-16 09:33:32（Asia/Shanghai）`** | 开源预发布 | 同一天同时覆盖 **SuperGrok OAuth 免 `XAI_API_KEY`**、`cron run --wait`、`resolvedSkills` 缓存、**Codex 线程/Compaction/idle watchdog**、**MCP 作用域与审批默认**、以及大量 **Telegram/Discord/Matrix/WebChat**可靠性修复——是典型的“**Agent 平台周更**”样本 |
| 公共政策 × 产品落地 | [OpenAI and Malta partner to bring ChatGPT Plus to all citizens](https://openai.com/index/malta-chatgpt-plus-partnership/) | **2026-05-16**（OpenAI 页面落款 **May 16, 2026**） | 官方公告 | 将 **University of Malta 课程**与 **一年期 ChatGPT Plus**绑定，强调 **AI literacy + 可用工具**；对企业/政府客户这是 **OpenAI for Countries** playbook 的公开对照案例 |
| 平台安全 / 深度伪造 | [YouTube is expanding its AI deepfake detection tool to all adult users](https://www.theverge.com/news/931884/youtube-likeness-detection-ai-deepfake-expansion-all-adults) | **2026-05-15，10:25 PM UTC** → **`2026-05-16 06:25（Asia/Shanghai）`** | 技术媒体（引用 Google/YouTube 官方线程） | 将 **likeness detection**从创作者/特定职业人群扩到 **18+ 普通账号**；工程上要关注 **误报/自拍照数据落盘/撤回与删除**条款与区域合规差异 |
| 学术基础设施 / 治理 | [ArXiv will ban researchers who upload papers full of AI slop](https://www.theverge.com/science/931766/arxiv-ai-slop-ban-researchers) | **2026-05-15，8:38 PM UTC** → **`2026-05-16 04:38（Asia/Shanghai）`** | 技术媒体（引用 arXiv 相关干系人叙述） | 对“**不可辩驳的 LLM 生成残留**（幻觉引用、meta-comment）”讨论 **1 年封禁 + 后续需同行评审发表后再投 arXiv**；研发侧要升级为 **文档流水线审计**（不仅是“禁止粘贴”） |
| 论文原文（评测） | [STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?](https://arxiv.org/abs/2605.06527) | **见于** HF Daily [`2026-05-16`](https://huggingface.co/papers/date/2026-05-16) 列表；**arXiv 具体版本日以 Submission history 为准** | 论文原文 | 把“**implicit conflict**（新证据间接推翻旧记忆）”做成 **长上下文探测评测**，并提出 **CUPMem**式“写入侧状态裁决”方向；适合做 **Memory/RAG**架构评审对标 |
| 企业 Agent 评测叙事（相邻日期） | [Databricks brings GPT‑5.5 to enterprise agent workflows](https://openai.com/index/databricks/) | OpenAI 页面落款 **`May 15, 2026`**（**相邻日期/隔夜阅读**） | 官方案例文 | **OfficeQA Pro**：强调扫描 PDF/老旧文档解析错误如何在 Agent 工作流里级联放大；**46% 误差下降 / 首次 >50%**等数字以原文为准，适合做 **文档 Agent harness**对照阅读 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| OpenClaw 运维与排障 | OpenClaw：`v2026.5.16-beta.1` Release notes（见上） | Codex app-server 线程、Compaction 成功事件、usage 统计一致性、网关重启追踪 | Agent 平台 / SRE |
| 记忆系统评测 | arXiv：**STALE（2605.06527）** | implicit conflict、三维探测（State Resolution / Premise Resistance / Policy Adaptation） | ML 平台 / 记忆工程 |
| 平台治理对照 | The Verge：**YouTube likeness**（见上） + **arXiv slop ban**（见上） | 端到端的“检测/申诉/删除”与学术基础设施规则 | Trust & Safety / 研究运营 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：工程侧的高信噪增量依然集中在 **“把外部模型与工具运行时绑紧并把失败面收口”**（OpenClaw 同日 release 的体量和类别就是证据）；论文侧则继续补 **Agent Memory**评测拼图（STALE 这类 **implicit invalidation**）。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| Codex 一体化 | OpenClaw：线程绑定、Compaction 成功事件、idle watchdog | 外层网关与内层 native loop **事件语义要对齐**，否则会出现“假失败/卡住直到超时” |
| MCP 工程化 | OpenClaw：按 agent id 限定 user MCP + 审批默认 | **工具面扩大**时先把 **作用域与审批默认**写进配置契约，而不是只靠提示词 |
| 记忆失效模式 | STALE：implicit conflict | 记忆的难点不仅是检索，而是 **信念传播与撤销**；需要 **写入侧状态结构**而不只是向量召回 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | OpenClaw：**`v2026.5.16-beta.1` notes** | 一周内想理解“Agent 网关”应修哪些类 bug，这是高质量样本 |
| 必读 | arXiv：**STALE（2605.06527）** | 直戳“**记忆会过期但不说破**”的工程痛点 |
| 推荐 | OpenAI：**Malta partnership** | 看 **国家尺度**如何设计“素养 + 访问”捆绑产品 |
| 延伸 | OpenAI：**Databricks / OfficeQA Pro**（`May 15, 2026`） | 企业文档 Agent 的 **解析错误级联**是很好的风险清单 |

### 来源清单

- 检索范围：2026-05-16 00:00:00 到 2026-05-16 23:59:59（Asia/Shanghai），并对 **GitHub `Published`（UTC）**与 **媒体 UTC 时间**做换算校准
- 引用域名：`github.com`, `openai.com`, `theverge.com`, `huggingface.co`, `arxiv.org`
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 开源发布 | OpenClaw `v2026.5.16-beta.1` | **`Published` UTC → 上海 `2026-05-16`** | https://github.com/openclaw/openclaw/releases/tag/v2026.5.16-beta.1 |
| 官方公告 | OpenAI × Malta：ChatGPT Plus | **`2026-05-16`（OpenAI 页面日期）** | https://openai.com/index/malta-chatgpt-plus-partnership/ |
| 技术媒体 | YouTube expands AI likeness detection | **UTC → 落入上海 `2026-05-16` 早盘** | https://www.theverge.com/news/931884/youtube-likeness-detection-ai-deepfake-expansion-all-adults |
| 技术媒体 | arXiv ban narrative（AI slop） | **UTC → 落入上海 `2026-05-16` 凌晨** | https://www.theverge.com/science/931766/arxiv-ai-slop-ban-researchers |
| 论文聚合 | Hugging Face Daily Papers | **列表页：`2026-05-16`** | https://huggingface.co/papers/date/2026-05-16 |
| 论文原文 | STALE | **以 arXiv Submission history 为准** | https://arxiv.org/abs/2605.06527 |
| 官方案例文 | Databricks × GPT‑5.5 / OfficeQA Pro | **`May 15, 2026`（相邻日期）** | https://openai.com/index/databricks/ |

## 2026-05-15

### 今日总览

**一句话结论**：`2026-05-15`（Asia/Shanghai，00:00–23:59）更像「**平台把 Agent 的个性化记忆与模型阵容治理收口（Copilot Memory 用户偏好 × Grok Code Fast 1 下线）** × **开源侧把 OpenAI 回合交给 Codex app-server 接管（OpenClaw 官方博文 + 巨型 beta 发布）** × **产业/监管侧讨论“GEO/操纵生成式答案也算垃圾内容”与“大厂组织全力押注单一 agentic 平台”**」三条主线并行。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | GitHub 官方 changelog（Copilot Memory、Grok 模型退役）；OpenClaw 官方博客 + GitHub `Published` 时间戳（UTC→上海）；OpenAI `codex` Release；Anthropic PwC 官宣（页面日期字段校准）；The Verge（OpenClaw×OpenAI、OpenAI 组织调整、Google spam policy）；Hugging Face Daily Papers `2026-05-15`；Spring AI / LangChain 博客日期硬对齐；Claude Code / Hermes GitHub releases 专项；skills/Cursor 专项；中文补充（机器之心等未见同日强匹配主编发） |
| 核心趋势 | **记忆与偏好跨仓复用**：Copilot Memory 从「仓库级」扩到「用户级」偏好，直接影响多代理一致性与合规审计设计；**模型生命周期治理**：GitHub 侧明确退役 Grok Code Fast 1 并给替代模型建议；**运行时边界重划**：OpenClaw 将 `openai/gpt-*` 默认回合交给 Codex app-server，减少工具重复与会话泄漏；**搜索生态反 GEO**：Google 明确把「操纵生成式 AI 回答」纳入 spam 语义 |
| 可直接关注 | 企业侧：把 **user-level memory**当成「可导出、可删除、可隔离租户」的合规对象，而不是聊天增值功能；平台侧：**模型退役**会打断自动化流水线，需在 CI/IDE policy 做 **pin + fallback**；Agent 工程：**harness 切换可显著改评测**（WildClawBench 结论与 OpenClaw/Codex 路线形成互文） |
| 专项检索结论 | **Codex**：`rust-v0.131.0-alpha.18` 的 GitHub **`Published`** 为 **`2026-05-14T21:41:33Z`** → **`2026-05-15 05:41:33（Asia/Shanghai）`**，**落入**本日窗口；**Claude Code**：**未发现**与 **`2026-05-15（上海）`** 强对齐的新 GitHub Release tag（以 releases 页检索为准）；**OpenClaw**：`v2026.5.14-beta.1` 的 **`Published`** 为 **`2026-05-14T21:31:13Z`** → **`2026-05-15 05:31:13（Asia/Shanghai）`**，**落入**本日窗口；同日官方博文说明 **`openai/gpt-*` 默认走 Codex app-server**；**Hermes**：**未发现**同日 Hermes Agent **新 tag**；见 **第三方报道**对 OpenRouter 日推理排行的解读（需与官方/第三方 API 统计交叉核验）；**Spring AI**：**未发现** `spring.io/blog` 上与 **`2026-05-15`** 日期字段明确对齐的新条目；**MCP**：未检索到「规范级」单一重磅条款式发布；以 SDK/inspector 仓库活跃度与集成叙事为主；**skills**：OpenClaw 发布说明维护者侧 **`codex-review` skill**（偏工程化治理/评审闭环）；**Cursor Agent Skills**：**未发现**与 **`2026-05-15`** 强绑定的独立技能平台发布（仍以文档与邻近版本节奏为主） |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| Copilot / 记忆 | [Copilot Memory supports user preferences for Pro, Pro+ users](https://github.blog/changelog/2026-05-15-copilot-memory-supports-user-preferences-for-pro-pro-users/) | **2026-05-15**（changelog  slug **`2026-05-15`**) | 官方 changelog | 早期体验：把 **提交风格 / PR 结构 / 沟通语气**等做成 **跨仓库、跨代理**可用的用户级偏好；工程上要同步考虑 **记忆最小化、可撤回、与组织策略/审计日志**的对齐 |
| Copilot / 模型治理 | [Grok Code Fast 1 deprecated](https://github.blog/changelog/2026-05-15-grok-code-fast-1-deprecated/) | **2026-05-15**（GitHub：**today, May 15, 2026**） | 官方 changelog | 明确 **退役日 + 建议替代**（GPT-5 mini / Claude Haiku 4.5）；对企业意味着 **模型白名单、提示词/评测基准、成本曲线**要随政策变化做例行巡检 |
| 企业落地 / 合作伙伴 | [PwC is deploying Claude to build technology, execute deals, and reinvent enterprise functions for clients](https://www.anthropic.com/news/pwc-expanded-partnership) | **2026-05-14**（Anthropic 页面落款；**与上海窗相邻/隔夜传播**） | 官方公告 | 组织级叙述聚焦 **Claude Code + Cowork** rollout、**30k** 培训认证、**Office of the CFO** 新事业群；更像「专业服务业如何把 agentic build/deal execution/职能再造打成产品」的样本，需结合客户行业合规再拆解 |
| 多通道 Agent / Codex 集成 | OpenClaw：[OpenAI Models in OpenClaw, Done Right](https://openclaw.ai/blog/openai-models-in-openclaw-done-right) + The Verge：[OpenClaw now works better with OpenAI models and Codex](https://www.theverge.com/ai-artificial-intelligence/931078/openclaw-now-works-better-with-openai-models-and-codex) | Verge：**Posted May 15, 2026 at 12:29 AM UTC**（**落入上海 `2026-05-15` 08:29**）；OpenClaw 博文未展示独立「日历发布时间戳」（以正文表述为准） | 官方博客 + 技术媒体 | 关键工程信息：`openai/gpt-*` **默认**切到 **Codex app-server**；外层 OpenClaw 继续握 **channels/memory/cron/tools**；内层 **native thread/tool search/visible reply 工具化**——这是「两层 agent 平台」的清晰边界练习 |
| 开源发布 / Codex CLI | [openai/codex `rust-v0.131.0-alpha.18`](https://github.com/openai/codex/releases/tag/rust-v0.131.0-alpha.18) | GitHub **`Published`** **`2026-05-14T21:41:33Z`** → **`2026-05-15 05:41:33（Asia/Shanghai）`** | 开源预发布 | 以 **UTC 发布时间换算**落入上海日历日窗口；适合作为 **`2026-05-15`** 批次的「二进制/代理/打包」增量追踪点 |
| 开源发布 / OpenClaw | [openclaw/openclaw `v2026.5.14-beta.1`](https://github.com/openclaw/openclaw/releases/tag/v2026.5.14-beta.1) | GitHub **`Published`** **`2026-05-14T21:31:13Z`** → **`2026-05-15 05:31:13（Asia/Shanghai）`** | 开源预发布 | 变更面极大：**Codex app-server 迁移/会话绑定**、**依赖与供应链治理（npm advisory gating）**、多通道 **status reaction**、以及与 **review skills / 贡献者分流 skills**相关的维护者工具链 |
| 组织与产品战略（媒体报道） | [OpenAI keeps shuffling its executives in bid to win AI agent battle](https://www.theverge.com/ai-artificial-intelligence/931544/openai-keeps-shuffling-its-executives-in-bid-to-win-ai-agent-battle) | **May 15, 2026, 6:21 PM UTC** → **上海 `2026-05-16` 02:21**（**相邻日期/跨区域传播**；以稿件日期落款为准） | 技术媒体 | 引用备忘录口径：**单一 agentic 平台**、**合并 ChatGPT 与 Codex 体验**；组织研究价值高，但实施细节仍需 **OpenAI 官方后续产品与工程发布**印证 |
| 搜索生态 / 治理 | [Google updates its spam rules to include attempts to ‘manipulate’ AI](https://www.theverge.com/tech/931416/google-ai-search-spam-policy) | **May 15, 2026, 4:42 PM UTC** → **上海 `2026-05-16` 00:42**（**相邻日期**；The Verge 引用 [Google spam policies](https://developers.google.com/search/docs/essentials/spam-policies)） | 技术媒体 + 政策文档入口 | 「**操纵生成式回答**」被明确纳入 spam 语义，和 **GEO / recommendation poisoning**讨论直接相关；内容侧与安全侧要做 **威胁建模：对手盘会如何注入“权威记忆”** |
| 论文社区聚合 | [Hugging Face Daily Papers（May 15, 2026）](https://huggingface.co/papers/date/2026-05-15) | **2026-05-15**（HF 列表页日期） | 论文社区聚合 | 适合做当日「**Agent / 记忆 / 长程评测**」的阅读索引；单篇是否首发请以 arXiv **Submission history**为准 |
| 论文原文（示例核验） | [WildClawBench（arXiv:2605.10912）](https://arxiv.org/abs/2605.10912) | **见于** HF Daily **`2026-05-15`** 列表；**arXiv 页面以 Submission history 为准** | 论文原文 | **原生运行时 + 长程 + 真实工具**的 Agent benchmark 叙事；核心方法信号：**同模型切换 harness 可带来大幅分数差**，直接支持你在架构评审里主张「**评测要绑定运行时**」 |
| 产业排名（第三方报道） | TechTimes：[Nous Research's Hermes Agent…（OpenRouter 日推理排行叙事）](http://www.techtimes.com/articles/316694/20260515/nous-researchs-hermes-agent-dethrones-openclaw-worlds-most-used-open-source-ai-agent.htm) | 页面标识 **`20260515`**；**非 Hermes GitHub release** | **第三方报道，补充核验** | 只适合当「市场叙事/传播事件」线索；**token 规模、排行口径、统计窗口**必须回到 **OpenRouter / 项目方**一手材料复核 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| Copilot Memory 治理 | GitHub Docs：[About GitHub Copilot Memory](https://docs.github.com/copilot/concepts/agents/copilot-memory) + [个人 Memory 设置](https://github.com/settings/copilot/memory) | 用户记忆的最小化、审阅与删除路径 | 企业安全 / DevEx |
| OpenClaw × Codex 边界 | OpenClaw：**OpenAI Models in OpenClaw, Done Right**（见上） | app-server 负责 native loop；OpenClaw 负责通道与产品层策略 | 多模型 Agent 平台架构师 |
| 反 GEO / 内容合规 | Google：**Search spam policies**（见 The Verge 引用链） | 操纵生成式结果亦可构成违规 | 增长 / SEO / Trust & Safety |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：工程发布主战场在 **「Copilot 记忆与模型阵容」**与 **「OpenClaw/Codex 运行时融合」**；论文侧 **HF 日更列表高密度**，但需 **逐篇用 arXiv 时间戳**剔除“旧稿新上榜”。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 记忆从仓库到用户 | Copilot Memory：user-level preferences | 多仓协作团队要避免「个人偏好」与「组织编码规范」冲突：需要 **precedence 规则** |
| harness 与评测绑定 | WildClawBench + OpenClaw release | **benchmark 结论迁移到生产**时，至少锁定：**CLI 版本、工具白名单、超时、重试、权限** |
| 模型退役 | Grok Code Fast 1 deprecated | 把「模型名」从配置与评测里 **参数化**，避免 CI 突然红一片 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | OpenClaw：**OpenAI Models in OpenClaw, Done Right** | 把「谁来跑 tool loop」讲清楚，是做多供应商 Agent 平台的通用参照 |
| 必读 | GitHub：**Copilot Memory user preferences** changelog | 直接影响交付一致性与代码评审风格，且牵动隐私治理 |
| 推荐 | arXiv：**WildClawBench（2605.10912）** | 用数据提醒：**换 harness ≈ 换系统**，别用单一分数拍板 |
| 延伸 | The Verge：**Google spam policy / GEO** | 把「内容操纵」与「模型输出操纵」串到同一张风险地图上 |

### 来源清单

- 检索范围：2026-05-15 00:00:00 到 2026-05-15 23:59:59（Asia/Shanghai），并对 **GitHub `Published`（UTC）**与 **媒体 UTC 时间**做换算校准
- 引用域名：`github.blog`, `github.com`, `anthropic.com`, `openclaw.ai`, `theverge.com`, `developers.google.com`, `huggingface.co`, `arxiv.org`, `techtimes.com`
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 官方 changelog | Copilot Memory user preferences | **2026-05-15** | https://github.blog/changelog/2026-05-15-copilot-memory-supports-user-preferences-for-pro-pro-users/ |
| 官方 changelog | Grok Code Fast 1 deprecated | **2026-05-15** | https://github.blog/changelog/2026-05-15-grok-code-fast-1-deprecated/ |
| 官方公告 | Anthropic × PwC expanded partnership | **2026-05-14（页面日期；相邻窗阅读）** | https://www.anthropic.com/news/pwc-expanded-partnership |
| 官方博客 | OpenAI Models in OpenClaw, Done Right | 正文未给独立日历戳（以表述为准） | https://openclaw.ai/blog/openai-models-in-openclaw-done-right |
| 技术媒体 | OpenClaw × OpenAI / Codex（The Verge） | Posted **2026-05-15 00:29 UTC** → 上海 **08:29** | https://www.theverge.com/ai-artificial-intelligence/931078/openclaw-now-works-better-with-openai-models-and-codex |
| 技术媒体 | OpenAI executive shuffle / agent memo（The Verge） | **2026-05-15 18:21 UTC**（**上海日历相邻**） | https://www.theverge.com/ai-artificial-intelligence/931544/openai-keeps-shuffling-its-executives-in-bid-to-win-ai-agent-battle |
| 技术媒体 | Google spam policy & AI manipulation（The Verge） | **2026-05-15 16:42 UTC**（**上海日历相邻**） | https://www.theverge.com/tech/931416/google-ai-search-spam-policy |
| 开源发布 | Codex `rust-v0.131.0-alpha.18` | **`Published` UTC → 上海 `2026-05-15` 早盘** | https://github.com/openai/codex/releases/tag/rust-v0.131.0-alpha.18 |
| 开源发布 | OpenClaw `v2026.5.14-beta.1` | **`Published` UTC → 上海 `2026-05-15` 早盘** | https://github.com/openclaw/openclaw/releases/tag/v2026.5.14-beta.1 |
| 论文聚合 | Hugging Face Daily Papers | **2026-05-15** | https://huggingface.co/papers/date/2026-05-15 |
| 论文原文 | WildClawBench | **见 HF 列表；arXiv 以 submission 为准** | https://arxiv.org/abs/2605.10912 |
| 第三方报道 | Hermes/OpenRouter 叙事（TechTimes） | **20260515 页面标识** | http://www.techtimes.com/articles/316694/20260515/nous-researchs-hermes-agent-dethrones-openclaw-worlds-most-used-open-source-ai-agent.htm |

## 2026-05-14

### 今日总览

**一句话结论**：同日主线更像「**云上团队 Agent（GitHub Copilot app + Workspace/Codex 移动协同）× 平台安全与向善部署（ChatGPT safety summaries × Gates×Anthropic 公益合作）**，再叠加 **`Interrupt`** 第二天的产业议程与国内媒体侧的 **竞品 CLI/组织策略**叙事。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | OpenAI / Gates Foundation / Anthropic 官网；GitHub changelog（Copilot app / Auto / Usage API）；Anthropic Claude Code、`openclaw` release；LangChain Interrupt 会务材料；The Verge 产业报道；arxiv/huggingface Papers 抽样；skills/Agent Skills 专项；中文补充检索（机器之心未发现同日硬匹配） |
| 核心趋势 | **协作入口**：GitHub-native Copilot desktop app（技术预览）把「从 GitHub 工件出发的云会话」做实；OpenAI「**随时随地连到正在跑的 Codex**」把移动端变成长任务 steering 面板；**安全与公共利益**：ChatGPT「**safety summaries**」对齐跨会话风险识别；Anthropic × Gates **`$200M/4yr`** 承诺把模型能力导向全球健康/教育与农业公共服务品 |
| 可直接关注 | GitHub：`Copilot app`/`cloud agent`/usage API 同日三连发，企业要优先核对 **预览开关、CLI policy、配额与密钥面**；OpenAI：**Codex 移动协同**背后是 **中继层与令牌/会话审批**的工程与治理议题；Anthropic × Gates：**公共 benchmark/数据集**/连接器组合的路线，适合做对「向善部署」指标体系的对照阅读 |
| 专项检索结论 | **Codex（GitHub `openai/codex` Release）**：`rust-v0.131.0-alpha.18` 的 `Published` 为 **`2026-05-14T21:41:33Z`**，折算 Asia/Shanghai 为 **`2026-05-15 05:41:33`**，**不属于**本日 **`2026-05-14 00:00–23:59（上海）`** 窗口，建议归入 **`2026-05-15`** 批次；**Claude Code**：`v2.1.141` 的 `Published` 为 **`2026-05-13T23:19:16Z`** → **`2026-05-14 07:19:16（上海）`**，**落入**当日窗口（偏工程体验/权限与企业身份联邦）；**OpenClaw**：`v2026.5.12-beta.6` 的 `Published` 为 **`2026-05-13T21:00:40Z`** → **`2026-05-14 05:00:40（上海）`**，**落入**当日窗口（含 Copilot Gemini 看图路由等修复）；`v2026.5.14-beta.1` 的 `Published` 为 **`2026-05-14T21:31:13Z`** → **`2026-05-15 05:31:13（上海）`**，**不属于**当日窗口；**Hermes**：**未发现**同日新 release tag；**Spring AI**：**未发现** `spring.io/blog` 上与 `2026-05-14` **日期字段明确对齐**的新发布条目；**MCP**：未检索到与原技能「规范级主线仓库」同日**可单列**的重大规范发布（以生态发布节奏与实现对齐 PR 为主）；**skills**：GitHub Copilot app changelog 写明可把 **skills/prompts 固化成可重复工作流**（更接近「组织能力资产化」，而非单一标准文本变更） |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| 安全 / ChatGPT | [Helping ChatGPT better recognize context in sensitive conversations](https://openai.com/index/chatgpt-recognize-context-in-sensitive-conversations/) | **2026-05-14**（OpenAI index 落款 **May 14, 2026**） | 官方安全说明 | 「跨消息/跨会话」风险识别引入 **narrow safety summaries**：对「自杀自伤 / 伤人意念」场景的 **意图随时间演化**更可审计；给企业做 **内容安全与工作场所辅导**的对话类产品提供「边界条件」范式（仍须结合法务与本地化流程） |
| 产品 / Codex | [Work with Codex from anywhere](https://openai.com/index/work-with-codex-from-anywhere/) | **2026-05-14**（OpenAI index 落款 **May 14, 2026**） | 产品发布 | Codex **进入 ChatGPT 移动端预览**：手机侧跨线程 steering、命令审批、截图/终端/测试回填；同日强调 **Remote SSH GA**、**Hooks GA**、**Programmatic tokens（Business/Enterprise）** 与本地环境 HIPAA 场景的边界说明——本质是 **长时间运行 Agent 的移动控制面 + 令牌治理** |
| 公益 × 模型商用 | [Making AI work for more people（Gates Foundation）](https://www.gatesfoundation.org/ideas/media-center/press-releases/2026/05/ai-anthropic-partnership) ; [Anthropic forms $200 million partnership with the Gates Foundation](https://www.anthropic.com/news/gates-foundation-partnership) | **2026-05-14**（双方稿件落款 **May 14, 2026**） | 官方公告 / 公益合作 | **4 年 2 亿美金**量级承诺（grant + credits + tech support）：把连接器、benchmark、数据集等 **公共品**投进全球健康（疫苗/疟疾 TB 建模伙伴 IDM/IHME 叙述）、教育与农业小额农户场景——对学习 **「有益部署 Beneficial deployments」指标体系**的团队是高信噪上下文 |
| Copilot / 桌面 Agent | [GitHub Copilot app is now available in technical preview](https://github.blog/changelog/2026-05-14-github-copilot-app-is-now-available-in-technical-preview/) | **2026-05-14**（changelog **`2026-05-14-…`** 条目） | 官方 changelog | 从 **Issue/PR/会话**拉起隔离会话分支；集成终端/浏览器验证；可把 **skills/prompts**整理成例行工作流；并提到 **Agent Merge** 收口 review comments / checks——对平台工程团队是「**GitHub 原生 agentic IDE**」的新入口 |
| Copilot Cloud | [Copilot cloud agent supports auto model selection](https://github.blog/changelog/2026-05-14-copilot-cloud-agent-supports-auto-model-selection/) | **2026-05-14**（changelog **`2026-05-14-…`** 条目） | 官方 changelog | Auto 选型把「系统健康 × 可用模型集合」收口成运行时策略——研发侧可把其当作 **运行时路由/兜底**的一层，但要注意组织策略与会话可追溯性 |
| Copilot Metrics | [Team-level Copilot usage metrics now available via API](https://github.blog/changelog/2026-05-14-team-level-copilot-usage-metrics-now-available-via-api/) | **2026-05-14**（changelog **`2026-05-14-…`** 条目） | 官方 changelog | user↔teams 映射进入 **使用量 API**，可把「团队维度成本与采用率」接进内部 FinOps/License 工作台 |
| 开发者工具 CLI | Claude Code [`v2.1.141`](https://github.com/anthropics/claude-code/releases/tag/v2.1.141)（`Published` **`2026-05-13T23:19:16Z`**） | **2026-05-13（UTC）/ 相邻落入上海：`2026-05-14 07:19:16`** | 开源发布 | Hooks 扩展 `terminalSequence`、插件 HTTPS 克隆开关、`ANTHROPIC_WORKSPACE_ID` workload identity federation、长思考 spinner 变暖提示、`/feedback`收录近 24h/7 天会话等——偏 **人机协同与政企身份**硬需求 |
| 多通道 Agent 运行时 | OpenClaw [`v2026.5.12-beta.6`](https://github.com/openclaw/openclaw/releases/tag/v2026.5.12-beta.6)（`Published` **`2026-05-13T21:00:40Z`**） | **2026-05-13（UTC）/ 相邻落入上海：`2026-05-14 05:00:40`** | 开源 prerelease | 网关协议：**要求 v4 客户端**，流式 `deltaText/replace` 帧明示；并为 **Gemini image** 走 OAuth→Copilot API token 交换等修复——说明 **模型能力扩展**常与 **令牌交换与网关协议版本**耦合 |
| 竞品 / 开发者工具（媒体报道） | [xAI launches an “early beta” of its agentic CLI for Grok](https://www.theverge.com/ai-artificial-intelligence/930802/xai-launches-an-early-beta-of-its-agentic-cli-for-grok)（Posted **`May 14, 2026 7:38 PM UTC`**） | 2026-05-13（UTC 发布时间）→ **落入上海 `2026-05-15` 日历日凌晨**（但 **The Verge 页面日期落款为 May 14, 2026**） | 技术媒体 | 以 **`SuperGrok Heavy`** 订阅门槛推出的 **编码 CLI Beta**叙事；适合做「市场空间/定价」对照，工程技术细节仍需 **回溯 xAI 官方发布材料** |
| 组织策略（媒体报道） | [Microsoft starts canceling Claude Code licenses](https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad)（**`May 14, 2026, 7:00 PM UTC`**） | 同上行（ UTC 发布时间跨上海日历日边界；**落款 May 14, 2026**） | 技术媒体 | 观察 **大厂内部 toolchain 收敛**：Experiences + Devices 线转向 **Copilot CLI**的内部叙事与财年节点（报道引用内部 memo）；对评估「组织级 Agent IDE 选型」的人有 **路线图外生冲击**参考价值 |
| 产业议程 | [Interrupt 2026 Agenda / FAQ](https://interrupt.langchain.com/event-agenda)（会期含 **`2026-05-14` Day 2**） | **2026-05-14**（旧金山 **Day 2**；与本 Skill 的上海日历窗口存在 **时区换算相邻**阅读） | 社区会议 | LangChain **`Interrupt`** 进入 Day 2：偏 **产品与治理议程**风向标；工程质量结论仍需 **`2026-05-14` 同日官方材料**逐项对齐 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| ChatGPT × 公共安全叙事 | OpenAI：**Helping ChatGPT better recognize context…**（见上链接） | safety summaries：跨会话narrow scope、限时保留、对齐专家输入 | Trust & Safety / PM |
| Workspace / Codex Enterprise | OpenAI：**Work with Codex from anywhere** + [Hooks 文档入口](https://developers.openai.com/codex/hooks)（文内引用） | 移动 relay、REMOTE SSH、Hooks GA、程序化 token | DevEx / 平台安全架构师 |
| GitHub Copilot App | GitHub：**GitHub Copilot app documentation**（见 changelog 文末 `gh.io` 导流链接聚合） | 会话隔离、terminal/browser 验证、PR 闭环 | 习惯 GitHub-centric 的研发团队 |
| 受益部署指标体系 | Gates Foundation：**AI–Anthropic partnership**（见上） + Anthropic：**Beneficial deployments**叙述 | 「公共数据集 / benchmark / 连接器」组合的落地描述 | NGO Tech / Applied ML 负责人 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：工程发布面 **GitHub Copilot app + cloud agent Auto routing**补齐「从哪里启动 session / 如何把长任务跑着」的云入口；开源侧 Claude Code/OpenClaw 继续堆 **网关协议、令牌交换与 IDE/通道体验**。**LangGraph 版本级旗舰发布**同日未检索到与上海窗口强绑定的一手「单一大盘」条目，更多注意力在 **Interrupt 会议议程**与 **多端 Agent 控制权**产品上。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 会话隔离与工作流封装 | Copilot desktop app：`Issue/PR/会话`起手 + `skills/prompts`沉淀 | 「组织知识」不要停留在 prompt 草稿，要能 **映射到可追溯 session 模板**并与 PR 门禁打通 |
| 长任务人机协同 | ChatGPT Mobile ↔ Codex relay：移动端审批/改向 | 「长任务」的工程关键是 **checkpoint + interruptibility + 稽核链路**，不是再大一点的上下文窗口 |
| 网关协议耦合 | OpenClaw：v4-only + 显式帧 | 多端 SDK **必须对齐协议版本演进**，否则会退化成「本地拼装 diff」, 失真且难排障 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | Gates Foundation：**Making AI work for more people** | 「公共品 + benchmark + country-led」组合拳的一手措辞，便于对齐你司 CSR/向善 AI 报告的引用口径 |
| 必读 | Anthropic：**Gates partnership** | Anthropic Beneficial deployments 视角与「连接器/eval datasets」的工程落点并排阅读 |
| 推荐 | GitHub Copilot：**app technical preview** changelog | 「GitHub-native agentic IDE」的路线级描述，直接关系到团队是否把工作流搬进 GitHub 会话容器 |
| 推荐 | OpenAI：**Helping ChatGPT… sensitive conversations** | safety summaries「窄用途、短时、仅存安全相关 factual notes」的工程与伦理写法可借鉴 |
| 延伸 | Verge：**Grok CLI early beta / Microsoft & Claude Code** | 适合做竞争态势阅读；关键技术结论请 **回到厂商原文**核验 |

### 来源清单

- 检索范围：2026-05-14 00:00:00 到 2026-05-14 23:59:59（Asia/Shanghai），并对照 UTC `Published` 时间校准「跨日时区边界」条目
- 引用域名：`openai.com`, `gatesfoundation.org`, `anthropic.com`, `github.blog`, `github.com`, `interrupt.langchain.com`, `langchain.com`, `theverge.com`
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 官方发布 | Helping ChatGPT better recognize context in sensitive conversations | **2026-05-14**（OpenAI：**May 14, 2026**） | https://openai.com/index/chatgpt-recognize-context-in-sensitive-conversations/ |
| 官方发布 | Work with Codex from anywhere | **2026-05-14**（OpenAI：**May 14, 2026**） | https://openai.com/index/work-with-codex-from-anywhere/ |
| 官方公告 | Making AI work for more people（Gates Foundation） | **2026-05-14**（稿件：**May 14, 2026**） | https://www.gatesfoundation.org/ideas/media-center/press-releases/2026/05/ai-anthropic-partnership |
| 官方公告 | Anthropic forms $200 million partnership with the Gates Foundation | **2026-05-14**（稿件：**May 14, 2026**） | https://www.anthropic.com/news/gates-foundation-partnership |
| 官方 changelog | GitHub Copilot app technical preview | **2026-05-14** | https://github.blog/changelog/2026-05-14-github-copilot-app-is-now-available-in-technical-preview/ |
| 官方 changelog | Copilot cloud agent auto model selection | **2026-05-14** | https://github.blog/changelog/2026-05-14-copilot-cloud-agent-supports-auto-model-selection/ |
| 官方 changelog | Team Copilot usage metrics API | **2026-05-14** | https://github.blog/changelog/2026-05-14-team-level-copilot-usage-metrics-now-available-via-api/ |
| 开源发布 | Claude Code v2.1.141（UTC `Published` **`2026-05-13T23:19:16Z`**） | **落入上海 `2026-05-14` 相邻窗口** | https://github.com/anthropics/claude-code/releases/tag/v2.1.141 |
| 开源发布 | OpenClaw v2026.5.12-beta.6（UTC `Published` **`2026-05-13T21:00:40Z`**） | **落入上海 `2026-05-14` 相邻窗口** | https://github.com/openclaw/openclaw/releases/tag/v2026.5.12-beta.6 |
| 会务材料 | Interrupt 2026 Agenda（日程含 **`2026-05-14` Day 2；与 Asia/Shanghai 存在跨日时区相邻**） | 会议日（旧金山） | https://interrupt.langchain.com/event-agenda |
| 技术媒体 | xAI Grok CLI early beta | **Posted May 14, 2026 7:38 PM UTC**（The Verge 日期落款 May 14, 2026） | https://www.theverge.com/ai-artificial-intelligence/930802/xai-launches-an-early-beta-of-its-agentic-cli-for-grok |
| 技术媒体 | Microsoft starts canceling Claude Code licenses | **May 14, 2026, 7:00 PM UTC**（The Verge 日期落款 May 14, 2026） | https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad |

## 2026-05-13

### 今日总览

**一句话结论**：`2026-05-13`（Asia/Shanghai 全日窗口）更像「**企业/小商户把 Agent 接进业务系统** + **平台方把云 Agent 编排 API 化** + **IDE 侧把多仓云环境做成可治理资产**」，同日还有 **Interrupt 会前日（工作坊）** 与 **英国 AISI 网络安全评测进展** 这类“治理与红队叙事”抬升风险讨论水位。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | Anthropic / GitHub 官方；Cursor changelog；LangChain Interrupt（会议窗口）；The Verge / AISI / Microsoft 安全博客摘要核验；Copilot Agent Tasks API；Claude Code / Codex / OpenClaw / Hermes / Spring AI / MCP 专项检索；中文补充（量子位 Create2026 速览、掘金 AI 速递） |
| 核心趋势 | **SMB 连接器套餐**：Anthropic 推出 Claude for Small Business（连接器 + 工作流 +技能）；**Codex/云 Agent 自动化入口**：GitHub 公布 Copilot cloud agent 的 Agent tasks REST API（public preview）；**Cursor**：云 Agent **多仓环境 + Dockerfile 机密 + 分层缓存 + 环境治理**；**安全评测舆论场**：AISI / MDASH / Mythos & GPT-5.5 叙事同日升温 |
| 可直接关注 | 把小企业“台账/发票/合同/营销”这类高风险动作做成 **人机同权的审批流**（官方强调人在回路）；把 **云 Agent** 接进 **内部开发者门户/批量化迁移流水线** 需要 API 与凭证治理；把 **环境定义（Dockerfile）** 当供应链面管（机密、缓存、回滚） |
| 专项检索结论 | **Codex**：**未发现** GitHub Release 页明确落在 **`2026-05-13`（Asia/Shanghai）** 的新 tag（相邻仍可见 `rust-v0.131.0-alpha.8` 等更接近 `2026-05-12` 的节奏）；**Claude Code**：**未发现**当日新 GitHub Release tag；**OpenClaw**：检索到 **`v2026.5.12-beta.5`** 的 GitHub `Published` 时间为 **`2026-05-13T18:06:44Z`**，换算 Asia/Shanghai 为 **`2026-05-14 02:06:44`**，**不属于**本日 `00:00–23:59（上海）` 窗口，**建议并入 `2026-05-14` 批次**再写入“发布类”结论；**Hermes**：**未发现**当日新 release；**Spring AI**：**未发现**当日官方博客/Release 线显著落点；**MCP**：**未发现**可核验的“规范级/主线仓库”在当日的单一高置信重大发布（以社区议题与相邻合并为主）；**skills / Agent Skills**：当日更偏 **产品工程化**（Cursor 环境治理与多仓）与小企业 **预置技能包**，而非标准文本突变 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| 产品 / 中小企业落地 | [Introducing Claude for Small Business](https://www.anthropic.com/news/claude-for-small-business) | 2026-05-13 | 官方公告 | 把连接器与“可运行工作流/技能”打包进 Claude Cowork，强调权限继承与人在回路；对做 **B2B 集成** 的团队是“连接器 + 审批 + 审计”样板 |
| 开发者平台 / 云 Agent | [Start Copilot cloud agent tasks via the REST API](https://github.blog/changelog/2026-05-13-start-copilot-cloud-agent-tasks-via-the-rest-api/) | 2026-05-13 | 官方 changelog | Business/Enterprise 可用 REST **启动 cloud agent 任务**并跟踪进度；适合做跨仓批量改造、门户一键建库、周期发布自动化（前提是治理好 token/密钥与代码变更授权） |
| IDE / 云 Agent 基础设施 | [Cursor Changelog（May 13, 2026）](https://cursor.com/changelog/05-13-26) | 2026-05-13 | 产品更新 | **多仓环境**、Dockerfile **build secrets**、分层缓存（命中缓存构建更快）、环境版本回滚/审计/出站与密钥隔离；把“像笔记本一样的 Agent 运行环境”工程化 |
| Agent 社区 | [Introducing Interrupt: The AI Agent Conference by LangChain](https://blog.langchain.com/introducing-interrupt-langchain-conference)（会议窗口落入当日：5/13 工作坊日） | 2026-05-13（会议日程） | 社区活动 | 以 Interrupt（`2026-05-13`–`2026-05-14`，旧金山）观察 **Agent 产品/治理** 议程风向；当日为会前工作坊与社交环节（以官网/博文披露的日程为准） |
| 安全评测 / 监管叙事 | [AI cybersecurity updates for MDASH, Mythos, and GPT-5.5](https://www.theverge.com/ai-artificial-intelligence/930236/ai-cybersecurity-updates-for-mdash-mythos-and-gpt-5-5) | 2026-05-13 | 技术媒体 | 汇总 AISI 对 **Claude Mythos Preview** 与 **GPT-5.5** 的网络安全测试进展，并关联 Microsoft **MDASH** 与 Patch Tuesday 发现；适合做威胁建模与安全基准的对照阅读 |
| 产业 / 国内活动 | [Create2026 百度 AI 开发者大会速览（量子位）](https://www.qbitai.com/2026/05/416762.html) | 2026-05-13 | 中文媒体 | 便于快速抓取国内同日活动叙事（**DAA**、DuMate、秒哒、智能云基础设施等）；关键数字与能力边界建议再查官方材料 |
| 隐私 / 产品 | [Mark Zuckerberg announces ‘completely private’ encrypted Meta AI chat](https://www.theverge.com/tech/929791/meta-ai-incognito-chats) | 2026-05-13 | 技术媒体 | “会话结束即消失、服务器不可读”的隐私叙事会与 **企业日志/合规** 需求冲突；做端云架构时要分清营销承诺与可验证威胁模型 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| Copilot 自动化集成 | [Agent tasks REST API 文档](https://docs.github.com/rest/agent-tasks/agent-tasks?apiVersion=2026-03-10#start-a-task) | 任务启停、鉴权（PAT/OAuth）、进度查询 | 平台工程 / DevEx |
| 云 Agent 环境 | [Cloud agent development environments（Cursor Docs）](https://cursor.com/docs/cloud-agent/setup) | Dockerfile、机密、缓存、审计 | 需要给团队开“可控沙箱”的研发负责人 |
| Claude SMB 集成 | [Claude for Small Business 解决方案页](https://claude.com/solutions/small-business) | 连接器、工作流目录、信任与安全说明 | 做 SaaS 集成与权限模型的 PM/架构师 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：工程侧的“硬更新”集中在 **托管云 Agent 的任务 API**（GitHub）与 **IDE 云环境治理**（Cursor）；**LangGraph/LangChain 本体**未检索到与 `2026-05-13` 强绑定的单一旗舰发布，更多热度来自 **Interrupt** 线下议程。另：OpenClaw 的相邻 release 时间戳落在 **上海日历日的次日**，见上表“跨日时区边界”。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 编排自动化 | Copilot cloud agent REST 任务 API | 用 **API + PR** 闭合“需求→环境→变更”的链路；要把 **凭证、仓库范围、评审门槛** 设计成平台能力，而不是脚本私货 |
| 环境与供应链 | Cursor：build secrets / 分层缓存 / 环境级 egress | 多仓 Agent 会把“镜像构建依赖”放大成供应链面；**机密只进 build、不进运行态**是可复制模式 |
| 跨日时区边界 | OpenClaw：Release 时间戳 vs 业务日切 | 全球化项目要以 **业务时区（本 Skill：Asia/Shanghai）** 定义“某天发过什么”，避免把 UTC 午夜附近的发布写错日 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | [Claude for Small Business（Anthropic）](https://www.anthropic.com/news/claude-for-small-business) | 一手定义连接方式、工作流边界与信任叙述 |
| 必读 | [Copilot Agent tasks API（GitHub Blog）](https://github.blog/changelog/2026-05-13-start-copilot-cloud-agent-tasks-via-the-rest-api/) | 云 Agent “可编程入口”会直接改变内部自动化拓扑 |
| 推荐 | [AISI：How fast is autonomous AI cyber capability advancing?](https://www.aisi.gov.uk/blog/how-fast-is-autonomous-ai-cyber-capability-advancing) | 把模型评测与国家安全叙事的“速度感”对齐到可引用来源 |
| 延伸 | [量子位：Create2026 速览](https://www.qbitai.com/2026/05/416762.html) | 国内产业语料与时间线抓型；关键结论需二次核验 |

### 来源清单

- 检索范围：2026-05-13 00:00:00 到 2026-05-13 23:59:59（Asia/Shanghai）
- 引用域名：anthropic.com, claude.com, github.blog, docs.github.com, github.com, cursor.com, blog.langchain.com, theverge.com, aisi.gov.uk, microsoft.com, qbitai.com, deepmind.google, juejin.cn, techcrunch.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 官方发布 | Introducing Claude for Small Business | 2026-05-13 | https://www.anthropic.com/news/claude-for-small-business |
| 官方 changelog | Start Copilot cloud agent tasks via the REST API | 2026-05-13 | https://github.blog/changelog/2026-05-13-start-copilot-cloud-agent-tasks-via-the-rest-api/ |
| 产品更新 | Cursor（May 13, 2026 changelog） | 2026-05-13 | https://cursor.com/changelog/05-13-26 |
| 社区活动 | Introducing Interrupt（会议介绍；日程含 2026-05-13） | 相邻信息：会议窗口 | https://blog.langchain.com/introducing-interrupt-langchain-conference |
| 技术媒体 | AI cybersecurity updates（The Verge） | 2026-05-13 | https://www.theverge.com/ai-artificial-intelligence/930236/ai-cybersecurity-updates-for-mdash-mythos-and-gpt-5-5 |
| 技术媒体 | Meta AI incognito chats（The Verge） | 2026-05-13 | https://www.theverge.com/tech/929791/meta-ai-incognito-chats |
| 技术媒体 | Anthropic is launching Claude for Small Business（The Verge） | 2026-05-13 | https://www.theverge.com/ai-artificial-intelligence/929727/anthropic-is-launching-claude-for-small-business |
| 中文补充 | Create2026 百度 AI 开发者大会速览（量子位） | 2026-05-13 | https://www.qbitai.com/2026/05/416762.html |
| 中文补充 | 衍辉 AI 速递 5.13（掘金；条目多为转载核验线索） | 2026-05-13 | https://juejin.cn/post/7639128832419250217 |

## 2026-05-12

### 今日总览

**一句话结论**：本日同时出现 **交互层（指针/系统 UI）**、**平台商业化（Copilot 用量与套餐）** 与 **工程底座（Codex alpha、MCP 参考实现、开源 Agent 运行时）** 三条线叠加——更像“产品入口改造 + 企业付费模型落地 + Agent 工具链持续打补丁”的组合拳，而不是单一模型发布日。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | OpenAI / Google DeepMind / GitHub 官方与 changelog；Codex / OpenClaw；MCP servers；The Verge（政策与产业）；LangChain / Spring AI / Hermes / Claude Code / Cursor Skills 专项检索；中文补充（掘金） |
| 核心趋势 | **UI 入口前移**：DeepMind 公布 AI 指针原则并推进 Gemini in Chrome / Googlebook「Magic Pointer」；**Copilot 用量经济实锤**：个人套餐引入 flex、发布 Max，并开放 4 月用量报告；**开源工程继续增量**：Codex `0.131.0-alpha.7`、OpenClaw `beta.5`（上海时区落入当日窗口）、MCP everything-server 合并 Zod v4 升级 PR |
| 可直接关注 | 指针交互对「少写 prompt、 pixels → 实体」的产品隐喻；企业侧 Copilot **base + flex** 的预算模型；MCP 参考服务器与 SDK 版本联动的 schema 栈升级 |
| 专项检索结论 | **Codex**：`rust-v0.131.0-alpha.7`，GitHub `Published` `2026-05-12T01:58:34Z`（Asia/Shanghai 当日）；**Claude Code**：**未发现** GitHub Release 页面明确落在 `2026-05-12` 的新 tag（最近相邻为 `v2.1.139` **2026-05-11**）；**OpenClaw**：`v2026.5.10-beta.5`，`Published` `2026-05-11T16:38:39Z` → **落入 `2026-05-12 00:38` Asia/Shanghai**；**Hermes**：**未发现**当日新 release（最近仍为 `v2026.5.7` **2026-05-07**）；**Spring AI**：**未发现**当日 release（最近相邻仍为 **2026-05-08** milestone/patch）；**skills / Agent Skills**：**未发现**可核验的规范级当日大发布（以文档与社区迁移内容为主） |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| 研究与竞赛 | [What Parameter Golf taught us](https://openai.com/index/what-parameter-golf-taught-us/) | 2026-05-12 | 官方研究 | OpenAI 复盘 Parameter Golf：海量提交、**编码 agent 广泛参与**带来实验加速，也带来审核/归因/抄榜噪声；并提到 **Codex triage bot** 在大流量下的用法，对“人机混合评审流水线”有直接启发 |
| 交互与多模态产品 | [Shaping the future of AI interaction by reimagining the mouse pointer](https://deepmind.google/blog/ai-pointer/) | 2026-05-12 | 官方研究 / 产品路线 | 提出指针交互四原则，并把实验 demo 放进 AI Studio；同步宣布在 **Chrome** 与 **Googlebook** 上推进更“无打断”的 pointing+语音交互，适合做端侧/桌面 Agent 产品的人机界面参考 |
| 开发者平台 / AI 编程商业化 | [GitHub Copilot individual plans: flex allotments, new Max plan](https://github.blog/news-insights/company-news/github-copilot-individual-plans-introducing-flex-allotments-in-pro-and-pro-and-a-new-max-plan/) | 2026-05-12 | 官方公告 | **Pro / Pro+ / Max** 的 **base credits + flex allotment** 结构，配合 **6 月 1 日**用量计费切换；付费计划下 **completions / next edit suggestions 仍不限** |
| 开发者工具链 | [Codex `0.131.0-alpha.7`](https://github.com/openai/codex/releases/tag/rust-v0.131.0-alpha.7) | 2026-05-12（`Published` UTC 对应上海当日） | 开源 prerelease | 延续多平台资产与分发矩阵；与同日 Parameter Golf 文章形成“产品体验 ↔ 开源 CLI”对照阅读 |
| 开源 Agent 运行时 | [OpenClaw `v2026.5.10-beta.5`](https://github.com/openclaw/openclaw/releases/tag/v2026.5.10-beta.5) | 2026-05-12（Asia/Shanghai；`Published` `2026-05-11T16:38:39Z`） | 开源 prerelease | Fly Machines 环境识别、Fal 图片编辑路由、**`session.agentToAgent.maxPingPongTurns` 上限提升到 20**、Slack unfurl、**`/context map`**、Codex app-server 超时客户端回收、pnpm 11 等——偏“平台化运营+可靠性补丁” |
| MCP 工程 | [servers#4136：upgrade everything-server to zod v4, latest MCP sdk](https://github.com/modelcontextprotocol/servers/pull/4136) | 2026-05-12（Merged `2026-05-12T14:15:10Z`） | 开源合并 | 参考实现升级 **Zod v4** 与 **`@modelcontextprotocol/sdk` `1.29.0`**，展示 **v3→v4** API 迁移样例；自述 **不改变 MCP tool schema 行为** |
| AI 政策与授权 | [Human Consent Standard for AI licensing（RSL Media）](https://www.theverge.com/ai-artificial-intelligence/928534/rsl-media-human-consent-standard) | 2026-05-12 | 技术媒体 / 产业标准 | 把“机器人协议信号”扩展到 **肖像/角色/作品本体**；六月 registry 预期上线——对训练数据合规、爬虫策略与安全红线有前置影响 |
| Copilot 产品体验 | [Copilot code review: comment experience improvements](https://github.blog/changelog/2026-05-12-copilot-code-review-comment-experience-improvements/) | 2026-05-12 | 官方 changelog | PR 场景：**severity** + **分组 comment**，降低大 PR 噪声；依赖新 PR 体验开关 |
| Copilot 迁移配套 | [April reports for usage-based billing](https://github.blog/changelog/2026-05-12-april-reports-are-now-available-to-prepare-for-usage-based-billing/) | 2026-05-12 | 官方 changelog | 4 月用量→credits 的“预演报表”，帮助个人与企业在 **6/1** 前估预算（文档提示有统计口径边界） |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| 竞赛运营与 agent | [Parameter Golf 复盘](https://openai.com/index/what-parameter-golf-taught-us/) | 低比特训练、量化、评测策略边界、agent 辅助提交流程 | ML 平台 / DevRel / 研究团队 |
| MCP schema 栈 | [PR #4136 描述与 diff 导向阅读](https://github.com/modelcontextprotocol/servers/pull/4136) | Zod v4：`z.url()`、`z.looseObject()`、SDK 版本对齐 | MCP server 维护者 |
| Copilot 计费 | [Usage-based billing 文档入口（GitHub Docs）](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-individuals) | base/flex、仪表盘读数 | 需要给研发部做预算模型的人 |
| 指针交互原型 | [AI Pointer demos（AI Studio）](https://aistudio.google.com/)（文内链接） | pointing+语音、上下文绑定 | 端侧产品 / 交互设计 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：**未发现** LangChain 官方博客在 `2026-05-12` 的新发长文；同日工程注意力更多在 **IDE/浏览器入口**、**GitHub Copilot 计费与 code review 交互**、以及 **MCP 参考实现依赖升级** 上。LangChain 侧的 **Interrupt 会议**处于 **2026-05-13`–`05-14**（**相邻日期**）窗口，可作为 community 热度背景。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| MCP 实现面 | everything-server 合并 Zod v4 升级 | 给“协议不变、实现库升级”的场景一套可抄的迁移路径；注意 **SDK 小版本**与 schema 库联动 |
| Agent 运行态 | OpenClaw 继续堆多通道与沙箱策略细粒度开关 | 多 Agent ping‑pong、消息跨上下文权限，本质是 ** blast radius 控制**，企业自建 agent 也要 Product+Security 同桌设参 |
| 交互层 | DeepMind AI Pointer | 把“选区即 prompt”推到 UI 预设里，减少长提示与粘贴摩擦 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | [Parameter Golf 复盘](https://openai.com/index/what-parameter-golf-taught-us/) | 一手总结 agent 时代开放式技术竞技的治理难题 |
| 必读 | [DeepMind：AI pointer](https://deepmind.google/blog/ai-pointer/) | 看懂 Google 如何把多模态理解嵌进最基础的指针交互 |
| 推荐 | [Copilot 个人套餐与 flex](https://github.blog/news-insights/company-news/github-copilot-individual-plans-introducing-flex-allotments-in-pro-and-pro-and-a-new-max-plan/) | 直接决定团队 IDE agent 用量规划 |
| 推荐 | [The Verge：Human Consent Standard](https://www.theverge.com/ai-artificial-intelligence/928534/rsl-media-human-consent-standard) | 训练/爬虫/真人素材授权的新信号，需和法务一起读 |
| 延伸（相邻） | [Introducing Interrupt（LangChain 会议预热）](https://blog.langchain.com/introducing-interrupt-langchain-conference) | Agent 社区议程风向标（会议日：2026-05-13 起） |

### 来源清单

- 检索范围：2026-05-12 00:00:00 到 2026-05-12 23:59:59（Asia/Shanghai）
- 引用域名：openai.com, deepmind.google, aistudio.google.com, github.com, github.blog, theverge.com, rslmedia.org, juejin.cn, blog.langchain.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 官方发布 | What Parameter Golf taught us | 2026-05-12 | https://openai.com/index/what-parameter-golf-taught-us/ |
| 官方发布 | Reimagining the mouse pointer（AI pointer） | 2026-05-12 | https://deepmind.google/blog/ai-pointer/ |
| 官方发布 | GitHub Copilot individual plans（flex / Max） | 2026-05-12 | https://github.blog/news-insights/company-news/github-copilot-individual-plans-introducing-flex-allotments-in-pro-and-pro-and-a-new-max-plan/ |
| 官方 changelog | April reports for usage-based billing | 2026-05-12 | https://github.blog/changelog/2026-05-12-april-reports-are-now-available-to-prepare-for-usage-based-billing/ |
| 官方 changelog | Copilot code review comment experience improvements | 2026-05-12 | https://github.blog/changelog/2026-05-12-copilot-code-review-comment-experience-improvements/ |
| 开源发布 | OpenAI Codex `0.131.0-alpha.7` | 2026-05-12（Asia/Shanghai） | https://github.com/openai/codex/releases/tag/rust-v0.131.0-alpha.7 |
| 开源发布 | OpenClaw `v2026.5.10-beta.5` | 2026-05-12（Asia/Shanghai；UTC 相邻） | https://github.com/openclaw/openclaw/releases/tag/v2026.5.10-beta.5 |
| 开源合并 | MCP servers PR #4136（Zod v4） | 2026-05-12 | https://github.com/modelcontextprotocol/servers/pull/4136 |
| 技术媒体 | Human Consent Standard（RSL Media） | 2026-05-12 | https://www.theverge.com/ai-artificial-intelligence/928534/rsl-media-human-consent-standard |
| 中文补充 | 掘金：ChatGPT 更新节奏与趋势（社区稿） | 2026-05-12 | https://juejin.cn/post/7638839672550785062 |
| 社区预热（相邻日期） | Introducing Interrupt（LangChain conference） | 发布日未在抓取正文顶部展示；会议为 2026-05-13`–`05-14（相邻日期） | https://blog.langchain.com/introducing-interrupt-langchain-conference |

## 2026-05-11

### 今日总览

**一句话结论**：本日 AI 主线从单点模型发布转向 **Agent 工具链持续发版 + 企业部署服务化 + Agent 治理平台化**，其中 Codex 与 OpenClaw 的开源 release 最具工程可复现价值。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | OpenAI / Anthropic / GitHub / Codex / Claude Code / OpenClaw / Hermes / Spring AI / LangGraph / RAG / MCP / arXiv / Hugging Face / VentureBeat / IAPP / 量子位 |
| 核心趋势 | **Coding agent 继续高频迭代**：Codex alpha 与 OpenClaw beta 同日可核验；**企业 AI 进入交付公司化阶段**：OpenAI Deployment Company 线索显示模型厂商开始前置咨询和工程交付；**Agent 平台治理成为竞争点**：memory、eval、orchestration 与合规可观测被打包进平台能力 |
| 可直接关注 | Codex `0.131.0-alpha.6` 的多平台资产与 sigstore；OpenClaw `maxPingPongTurns`、跨上下文消息权限、`/context map`；OpenAI / Anthropic 企业交付模式对自建 Agent 平台边界的影响 |
| 专项检索结论 | **Codex**：GitHub `rust-v0.131.0-alpha.6` Published `2026-05-11T11:48:21Z`；**Claude Code**：未核验到官方 GitHub Release 页面明确标注 `2026-05-11` 的重要功能发布，第三方索引提到 `v2.1.138` internal fixes，未列为重大事件；**OpenClaw**：`v2026.5.10-beta.4` 在目标窗口可核验；**Hermes**：未发现当日新 release，最近仍为 `v2026.5.7`；**Spring AI**：未发现当日 release，最近相邻为 2026-05-08 的 `1.1.6` / `2.0.0-M6`；**skills**：未发现当日规范级新发布，OpenAI / Cursor / Claude skills 文档仍作为背景资料 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| AI 编程 / Codex | [OpenAI Codex `0.131.0-alpha.6`](https://github.com/openai/codex/releases/tag/rust-v0.131.0-alpha.6) | 2026-05-11 | 开源 prerelease | 覆盖 Codex CLI、app-server、responses proxy、Windows sandbox setup、npm 包和 sigstore 资产，适合验证跨平台分发与供应链签名流程 |
| 开源 Agent 运行时 | [OpenClaw `v2026.5.10-beta.4`](https://github.com/openclaw/openclaw/releases/tag/v2026.5.10-beta.4) | 2026-05-11 | 开源 prerelease | 增强 agent-to-agent 长链路、跨上下文消息权限、Slack 展开控制、Fly Machines 环境检测、`/context map`，可作为自托管 Agent 运行时治理参考 |
| 企业 AI 落地 | [OpenAI launches the OpenAI Deployment Company](https://www.techmeme.com/260511/p22) | 2026-05-11 | 企业 AI / 媒体聚合 | OpenAI 以部署公司承接企业 AI 系统建设，说明模型厂商正在从 API 供应商向前置交付和工作流重构延伸 |
| Agent 平台治理（相邻） | [Anthropic wants to own your agent's memory, evals, and orchestration](https://venturebeat.com/orchestration/anthropic-wants-to-own-your-agents-memory-evals-and-orchestration-and-that-should-make-enterprises-nervous/) | 2026-05-08（相邻日期） | 技术媒体 / 架构分析 | 把 Agent memory、evaluation、multi-agent orchestration 的平台化与厂商锁定风险讲清楚，适合企业评估自建 vs 托管 Agent 控制面 |
| Java AI（相邻） | [Spring AI `2.0.0-M6`](https://github.com/spring-projects/spring-ai/releases/tag/v2.0.0-M6) | 2026-05-08（相邻日期） | 开源 milestone | OpenAI 类层次重构、provider options 不可变化、模块移除等变化提醒 Java 企业栈关注 API 兼容与值对象不可变设计 |
| 政策监管（相邻） | [EU agrees to amend AI Act, clarifies overlap with machinery rules](https://iapp.org/news/a/eu-agrees-to-amend-ai-act-clarifies-overlap-with-machinery-rules) | 2026-05-07（相邻日期） | 政策监管 | 高风险 AI 合规期限、工业 AI 适用边界和 nudifier 禁令变化，会影响欧盟市场 AI 产品路线图与治理排期 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| Codex 发布工程 | [Codex `0.131.0-alpha.6` Release](https://github.com/openai/codex/releases/tag/rust-v0.131.0-alpha.6) | 多平台二进制、npm 包、sigstore、Windows sandbox setup | DevEx / 供应链安全 |
| Agent 运行时治理 | [OpenClaw `v2026.5.10-beta.4`](https://github.com/openclaw/openclaw/releases/tag/v2026.5.10-beta.4) | 消息权限、上下文地图、Slack 配置、local model service | Agent 平台 / 自托管团队 |
| Workspace Agent 背景 | [Introducing workspace agents in ChatGPT](https://openai.com/index/introducing-workspace-agents-in-chatgpt/) | 组织共享 Agent、审批、Slack、Compliance API、prompt injection safeguard | 企业 AI 平台 / 治理团队 |
| Java Agent 生态 | [Spring AI `2.0.0-M6`](https://github.com/spring-projects/spring-ai/releases/tag/v2.0.0-M6) | breaking changes、provider options 不可变、MCP SDK 演进 | Java / Spring AI 团队 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：当日未发现 LangChain / LangGraph / LlamaIndex / MCP 官方在 `2026-05-11` 的重大新 release；工程焦点落在 coding agent 本体、Agent 运行时治理和企业交付模式。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| Coding agent | Codex alpha 继续提供完整多平台资产矩阵 | 内部试用 alpha 通道时要把 **版本固定、资产校验、回滚策略**纳入流水线，而不是只看功能点 |
| Agent runtime | OpenClaw 放大跨 Agent 消息链路、上下文可视化和 provider local service | 长会话 Agent 的治理重点是 **上下文可解释、权限可控、运行时可迁移** |
| 托管 Agent 平台 | OpenAI / Anthropic 都在把企业流程、memory、eval、orchestration 前移到平台层 | 企业要先定义哪些能力必须由自己掌控，避免业务规则、评测标准和记忆数据被单一厂商绑定 |
| Java AI | Spring AI 相邻版本强调不可变 options 与接口重构 | 企业 Java 栈要把 AI provider 配置当成稳定契约管理，避免应用层堆 if/else 适配各供应商 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | [OpenClaw `v2026.5.10-beta.4`](https://github.com/openclaw/openclaw/releases/tag/v2026.5.10-beta.4) | 最能观察自托管 Agent runtime 在权限、上下文、消息平台和本地模型服务上的演进 |
| 必读 | [Codex `0.131.0-alpha.6`](https://github.com/openai/codex/releases/tag/rust-v0.131.0-alpha.6) | 适合检查 Codex 的跨平台构建、资产命名和供应链签名方式 |
| 推荐 | [VentureBeat：Anthropic agent memory/evals/orchestration](https://venturebeat.com/orchestration/anthropic-wants-to-own-your-agents-memory-evals-and-orchestration-and-that-should-make-enterprises-nervous/) | 帮助判断托管 Agent 平台与自建 LangGraph / CrewAI / RAG memory 的边界 |
| 延伸 | [IAPP：EU AI Act amendments](https://iapp.org/news/a/eu-agrees-to-amend-ai-act-clarifies-overlap-with-machinery-rules) | 合规期限和工业 AI 边界变化会直接影响产品出海排期 |

### 来源清单

- 检索范围：2026-05-11 00:00:00 到 2026-05-11 23:59:59（Asia/Shanghai）
- 引用域名：github.com, openai.com, techmeme.com, venturebeat.com, iapp.org, spring-projects/spring-ai
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 开源发布 | OpenAI Codex `0.131.0-alpha.6` | 2026-05-11 | https://github.com/openai/codex/releases/tag/rust-v0.131.0-alpha.6 |
| 开源发布 | OpenClaw `v2026.5.10-beta.4` | 2026-05-11 | https://github.com/openclaw/openclaw/releases/tag/v2026.5.10-beta.4 |
| 媒体聚合 / 企业 AI | OpenAI Deployment Company | 2026-05-11 | https://www.techmeme.com/260511/p22 |
| 官方产品背景 | Introducing workspace agents in ChatGPT | 2026-04-22（相邻背景） | https://openai.com/index/introducing-workspace-agents-in-chatgpt/ |
| 技术媒体 | Anthropic agent memory/evals/orchestration analysis | 2026-05-08（相邻日期） | https://venturebeat.com/orchestration/anthropic-wants-to-own-your-agents-memory-evals-and-orchestration-and-that-should-make-enterprises-nervous/ |
| 开源发布 | Spring AI `2.0.0-M6` | 2026-05-08（相邻日期） | https://github.com/spring-projects/spring-ai/releases/tag/v2.0.0-M6 |
| 政策监管 | EU AI Act amendments | 2026-05-07（相邻日期） | https://iapp.org/news/a/eu-agrees-to-amend-ai-act-clarifies-overlap-with-machinery-rules |

## 2026-05-10

### 今日总览

**一句话结论**：当日 **GitHub 官方 changelog 未见 05-10 条目**，coding agent 以 **前一日密集发版后的消化期**为主；舆论场则集中讨论 **Anthropic 对「Claude 曾试图勒索工程师」根因的再叙事**，以及 **Anthropic–xAI（Colossus 1）算力转租**的商业解读。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | OpenAI / Anthropic / Google DeepMind / GitHub changelog；Codex / Claude Code / OpenClaw / Hermes / Spring AI；LangChain；arXiv；TechCrunch / The Verge；量子位 |
| 核心趋势 | **对齐叙事外溢**：媒体把 Anthropic 官方「Teaching Claude why」研究，与历史 **blackmail** 事件重新并置讨论；**算力金融化**：「前沿实验室 × neocloud」转租模式进入资本市场话语 |
| 可直接关注 | 读 **Anthropic 研究原文**再对照媒体报道的裁剪；评估 **多供应商算力合同**对 Agent 产品路线图的约束 |
| 专项检索结论 | **Codex / Claude Code / OpenClaw**：GitHub `Published` **未见 2026-05-10** 新 tag（最近仍为 **2026-05-09** 前后版本）；**Hermes**：**未发现**当日新 Release（最近仍为 **2026-05-07** `v2026.5.7`）；**Spring AI**：**未发现** `spring.io/blog` 当日发文；**Agent Skills**：**未发现** Marketplace 级当日大发布 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| 对齐与安全（媒体） | [Anthropic says ‘evil’ portrayals of AI were responsible for Claude’s blackmail attempts](https://techcrunch.com/2026/05/10/anthropic-says-evil-portrayals-of-ai-were-responsible-for-claudes-blackmail-attempts/) | 2026-05-10 | 技术媒体 | 把「虚构叙事 → 行为分布」问题拉回公众讨论；**应以 Anthropic 研究原文为准** |
| 对齐与安全（官方，相邻） | [Teaching Claude why](https://www.anthropic.com/research/teaching-claude-why) | **2026-05-08**（相邻日期；TC 文内引用） | 研究博文 | 「说理 + 宪法文本 + 多样化环境」组合训练，对 **agentic misalignment** 评估集设计有直接启发 |
| 产业与算力（媒体） | [We’re feeling cynical about xAI’s big deal with Anthropic](https://techcrunch.com/2026/05/10/were-feeling-cynical-about-xais-big-deal-with-anthropic/) | 2026-05-10 | 评论/播客衍生 | 解释 **Colossus 1 转租 / neocloud** 叙事与 IPO 窗口期激励；需与 [Anthropic 官方合作稿](https://www.anthropic.com/news/higher-limits-spacex)（**2026-05-06**，相邻）交叉阅读 |
| 中文产业（展会窗口） | [太初元碁携龙虾一体机亮相北京科博会](https://www.qbitai.com/2026/05/415027.html) | **2026-05-09**（稿件；**相邻日期/中国时间窗口传播**：科博会 **5/8–5/10**） | 中文媒体 | **OpenClaw 国产化一体机 + Skills 预装** 的政企私有化叙事，可对照当日 **OpenClaw beta** 工程变更 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| 对齐训练 | [Teaching Claude why](https://www.anthropic.com/research/teaching-claude-why) | 示范 vs 说理、constitutional docs、OOD 行为 | 安全 / 对齐工程师 |
| Agent 威胁建模 | 量子位「龙虾一体机」+ 既有 OpenClaw 安全讨论 | 私有化部署、预装 Skills、并发规格 | 平台架构 / 安全架构 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：当日 **未发现** LangChain / LangGraph **带 2026-05-10 日期**的官方博客更新；工程注意力更多在 **个人 Agent 运行时（OpenClaw 前一日大版本）** 的跟进与 **媒体侧对齐叙事**。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 开源 Agent 运行时 | 05-09 发布 `v2026.5.9-beta.1` 后，社区进入 issue/回滚观察期 | 大版本后优先验证 **Docker/tini、Node 22.16+ floor、日志脱敏** |
| 对齐 eval | Anthropic 称 Haiku 4.5 后在测试场景 **0% blackmail**（见 TC 引述） | 把「越界行为」拆成 **可复现 scenario + 版本矩阵** 做回归 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读（相邻） | [Teaching Claude why](https://www.anthropic.com/research/teaching-claude-why) | 一手方法论，避免只读媒体二手摘要 |
| 推荐 | [TC：evil portrayals 报道](https://techcrunch.com/2026/05/10/anthropic-says-evil-portrayals-of-ai-were-responsible-for-claudes-blackmail-attempts/) | 快速了解公众叙事如何折叠技术结论 |
| 延伸 | [TC：xAI–Anthropic 交易评论](https://techcrunch.com/2026/05/10/were-feeling-cynical-about-xais-big-deal-with-anthropic/) | 理解算力转租与资本市场叙事的张力 |

### 来源清单

- 检索范围：2026-05-10 00:00:00 到 2026-05-10 23:59:59（Asia/Shanghai）
- 引用域名：techcrunch.com, anthropic.com, qbitai.com, github.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 技术媒体 | Anthropic says ‘evil’ portrayals… | 2026-05-10 | https://techcrunch.com/2026/05/10/anthropic-says-evil-portrayals-of-ai-were-responsible-for-claudes-blackmail-attempts/ |
| 技术媒体 | We’re feeling cynical about xAI’s big deal… | 2026-05-10 | https://techcrunch.com/2026/05/10/were-feeling-cynical-about-xais-big-deal-with-anthropic/ |
| 研究（相邻） | Teaching Claude why | 2026-05-08 | https://www.anthropic.com/research/teaching-claude-why |
| 官方新闻（相邻） | Higher usage limits… SpaceX | 2026-05-06 | https://www.anthropic.com/news/higher-limits-spacex |
| 中文媒体（相邻/窗口） | 太初元碁携龙虾一体机亮相北京科博会 | 2026-05-09；科博会 5/8–5/10 | https://www.qbitai.com/2026/05/415027.html |

## 2026-05-09

### 今日总览

**一句话结论**：**coding agent 三线同日迭代**（Codex **alpha**、Claude Code **补丁**、OpenClaw **巨型 beta**），叠加 **国产基础模型与语音多模态** 的高密度发布，形成「工具链 + 模型供给侧」同频共振。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | OpenAI Codex releases；Anthropic Claude Code releases；OpenClaw releases；Hermes / Spring AI / LangChain / MCP / arXiv；量子位 |
| 核心趋势 | **Agent 运行时工程化**：日志脱敏、模型目录动态发现、Discord 语音实时模式、Bedrock `serviceTier` 等把「能跑」推向「能运维」；**国产模型性价比叙事**再强化 |
| 可直接关注 | OpenClaw **Node 22.16+** 与 **tini** 变更对部署流水线的影响；Codex **0.131.0-alpha.1** 与上游 lockfile 联动 |
| 专项检索结论 | **Codex**：[`rust-v0.131.0-alpha.1`](https://github.com/openai/codex/releases/tag/rust-v0.131.0-alpha.1) **Published 2026-05-09T00:30:24Z**；**Claude Code**：[`v2.1.137`](https://github.com/anthropics/claude-code/releases/tag/v2.1.137) **2026-05-09T00:11:04Z**（Windows 插件激活修复）；**OpenClaw**：[`v2026.5.9-beta.1`](https://github.com/openclaw/openclaw/releases/tag/v2026.5.9-beta.1) **2026-05-09T13:32:02Z**（**Prerelease**）；**Hermes**：当日 **无** 新 GitHub Release（最近 **2026-05-07**）；**Spring AI**：**未发现**当日官方博客；**skills**：OpenClaw 对 **Windows 插件 skills 目录 junction** 等工程修复，偏 **实现层** |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| 开源 coding agent | [OpenAI Codex `0.131.0-alpha.1`（Prerelease）](https://github.com/openai/codex/releases/tag/rust-v0.131.0-alpha.1) | 2026-05-09 | 开源 pre-release | 跟进 **alpha** 与 stable 通道差异；校验 CI 产物与 **sigstore** 资产 |
| 开源 coding agent | [Claude Code `v2.1.137`](https://github.com/anthropics/claude-code/releases/tag/v2.1.137) | 2026-05-09 | 开源 patch | **VS Code 扩展在 Windows 上无法激活** 一类「环境耦合 bug」对团队桌面标准化敏感 |
| 开源 personal agent | [OpenClaw `v2026.5.9-beta.1`（Prerelease）](https://github.com/openclaw/openclaw/releases/tag/v2026.5.9-beta.1) | 2026-05-09 | 开源 pre-release | 覆盖 **模型目录运行时拉取**、**日志脱敏**、**Discord 实时语音模式**、**Bedrock serviceTier**、**Node 22.16+ floor** 等一长串运维向变更 |
| 基础模型 | [百度发布文心 5.1：搜索能力登顶国内…](https://www.qbitai.com/2026/05/414496.html) | 2026-05-09 | 中文媒体 / 产业 | 「多维弹性预训练 → **约 6% 预训练成本**」叙事，适合与 **官方技术博客** 交叉验证 |
| 语音多模态 | [阶跃最新语音模型位列 Artificial Analysis 评测榜中国第一](https://www.qbitai.com/2026/05/415023.html) | 2026-05-09 | 中文媒体 / 产品 | **Speech Arena** 盲测 Elo 机制对 **TTS 选型**有参考意义 |
| 具身智能 | [空间智能的“具身化”跃迁，高德 ABot 体系模型夺冠 AGIBot 全球挑战赛](https://www.qbitai.com/2026/05/414826.html) | 2026-05-09 | 中文媒体 / 竞赛 | **世界模型 + 物理一致性** 指标（Visual Quality / Action Following）对机器人数据管线有启发 |
| 政策（相邻） | [两项 AI 政策发布…](https://www.qbitai.com/2026/05/415019.html) | **2026-05-08**（正文「5 月 8 日」；量子位 **2026-05-09** 传播） | 中文媒体 / 政策解读 | 「算电协同 + 智能体规范应用」双文件的行业化解读 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| OpenClaw 运维 | [OpenClaw `v2026.5.9-beta.1` Release Notes](https://github.com/openclaw/openclaw/releases/tag/v2026.5.9-beta.1) | `tini`、HTTP 日志脱敏、网关重启 RPC、`serviceTier` | 自托管 Agent 平台工程 |
| Codex 发布工程 | [Codex `rust-v0.131.0-alpha.1`](https://github.com/openai/codex/releases/tag/rust-v0.131.0-alpha.1) | alpha 二进制矩阵、npm pack | 想在 alpha 通道验证新特性的团队 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：**未发现** LangChain 官方博客在 **2026-05-09** 的更新；同日工程热点主要由 **OpenClaw 大 beta** 与 **国产模型/语音** 牵引。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| Agent 平台 | OpenClaw：统一 **provider/model identity** 注入 system prompt | 减少「模型自称与实际路由不一致」导致的调试成本 |
| 模型路由 | OpenClaw：Google / Gemini **retired id 归一化** 到 `gemini-3.1-pro-preview` | 线上配置漂移时，用 **canonical id** 做迁移层 |
| RAG / 工具 | OpenClaw：`oc-path` 插件、`openclaw path` 访问 workspace 文本 | 最小权限读取敏感 workspace 文件 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 必读 | [OpenClaw `v2026.5.9-beta.1` Release Notes](https://github.com/openclaw/openclaw/releases/tag/v2026.5.9-beta.1) | 单版本集中观察 **多通道（Discord/Telegram/Feishu）+ 语音 + Codex harness** 的耦合方式 |
| 推荐 | [Claude Code `v2.1.137`](https://github.com/anthropics/claude-code/releases/tag/v2.1.137) | Windows 开发者可立刻核对扩展激活回归 |
| 延伸 | [文心 5.1 量子位报道](https://www.qbitai.com/2026/05/414496.html) | 快速获取国内模型发布叙事与指标口径 |

### 来源清单

- 检索范围：2026-05-09 00:00:00 到 2026-05-09 23:59:59（Asia/Shanghai）
- 引用域名：github.com, openai.com（Codex 仓库）, qbitai.com, anthropics.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 开源发布 | Codex `0.131.0-alpha.1` | 2026-05-09 | https://github.com/openai/codex/releases/tag/rust-v0.131.0-alpha.1 |
| 开源发布 | Claude Code `v2.1.137` | 2026-05-09 | https://github.com/anthropics/claude-code/releases/tag/v2.1.137 |
| 开源发布 | OpenClaw `v2026.5.9-beta.1` | 2026-05-09 | https://github.com/openclaw/openclaw/releases/tag/v2026.5.9-beta.1 |
| 中文媒体 | 百度发布文心 5.1 | 2026-05-09 | https://www.qbitai.com/2026/05/414496.html |
| 中文媒体 | 阶跃 StepAudio 2.5 TTS | 2026-05-09 | https://www.qbitai.com/2026/05/415023.html |
| 中文媒体 | 高德 ABot AGIBot 夺冠 | 2026-05-09 | https://www.qbitai.com/2026/05/414826.html |
| 中文媒体（相邻） | 两项 AI 政策发布（解读稿） | 2026-05-08 / 2026-05-09 传播 | https://www.qbitai.com/2026/05/415019.html |
| 开源发布（相邻） | Hermes Agent `v2026.5.7` | 2026-05-07 | https://github.com/NousResearch/hermes-agent/releases/tag/v2026.5.7 |

## 2026-05-08

### 今日总览

**一句话结论**：本日主轴是「 coding agent 企业治理可被产品化」「供应链与证书轮转进入硬截止日」「对齐训练方法论公开升级」，同时大厂个人 Agent 叙事与开源 Agent 爆款形成明显竞品压力。


| 维度     | 本日结论                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 检索范围   | OpenAI / Anthropic 官方；Google Cloud Gemini；GitHub Copilot & 平台changelog；coding agent（Codex/Claude Code/OpenClaw/Hermes）；MCP/registry；可信媒体（CNBC）；政策相邻（EU 云）；论文相邻（arXiv）；中文量子位相邻                                                                                                                                                                                                                                                                                                                                                                                   |
| 核心趋势   | OpenAI 将 macOS 证书生效日与《Running Codex safely》长篇实践同日公开；Anthropic 以「Teaching Claude why」解释 agentic 对齐训练；Gemini Flash-Lite 进入企业 Agent 平台 GA（官方日期为前一自然日）；GitHub Copilot cloud agent 的工程化指标与密钥管理同日增强                                                                                                                                                                                                                                                                                                                                                                   |
| 可直接关注  | 证书与客户端强制更新窗口；Codex sandbox/approval/OTel 与公司治理模版；对齐训练中「说理」优于单纯示范；Copilot Usage API 细粒度与安全供应链                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 专项检索结论 | **Codex**：当日官方工程文《Running Codex safely at OpenAI》；稳定版 `[0.129.0](https://github.com/openai/codex/releases/tag/rust-v0.129.0)` **发布日为 2026-05-07**，作相邻日期摘录；**Claude Code**：当日 **未发现** GitHub Release；搜索结果中较近版本为 `**v2.1.129`（2026-05-06）**，请以仓库 [Releases](https://github.com/anthropics/claude-code/releases) 页面为准。**OpenClaw**：最近 **2026-05-07** 的 `v2026.5.7`，当日无新 tag；**Hermes**：当日 **未发现** 新的 GitHub Release（未检索到 `**v2026.5.8`** 等新 tag）；**Spring AI**：未发现 **2026-05-08** 官方 release；**Agent Skills**：未发现 **当日** Marketplace/规范级大发布，`SKILL.md` 体系仍为既有文档主战场 |


### 重要事件与发布


| 主题       | 标题                                                                                                                                                                            | 日期                                 | 类型         | 研发/学习价值                                                                                                          |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------- |
| 供应链安全    | [OpenAI：Our response to the Axios developer tool compromise](https://openai.com/index/axios-developer-tool-compromise/)                                                       | 生效 **2026-05-08**（公告更新 2026-04-10） | 安全公告       | 明确 **GitHub Actions 漂浮标签风险**、`minimumReleaseAge` 缺失教训；列出旧证书下线后最早仍受影响的 macOS 应用版本阈值，可作发布与 SBOM 流程对照               |
| AI 编程治理  | [OpenAI：Running Codex safely at OpenAI](https://openai.com/index/running-codex-safely/)                                                                                       | 2026-05-08                         | 实践博客       | Sandbox + approval + **auto_review**、网络代理白/黑名单、`rules`、**OpenTelemetry** 导出与合规平台联动，可当企业落地 coding agent **控制面清单** |
| 对齐与安全研究  | [Anthropic：Teaching Claude why](https://www.anthropic.com/research/teaching-claude-why)                                                                                       | 2026-05-08                         | 研究博文       | 「示范不如说理」：**difficult advice**、constitutional document、OOD 泛化与 RL **持续性**一并讨论，适合做安全训练数据与 eval 设计的阅读材料             |
| 云与模型 GA  | [Google Cloud：Gemini 3.1 Flash-Lite is now generally available…](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-flash-lite-is-now-generally-available) | 2026-05-07（**相邻日期**，官方文首日期）        | 产品 GA      | JetBrains/Gladly 等点名 **超低时延 Agent** 管线；给出成本与延迟工程叙述，可作「边缘分类器 + Agent 编排」选型参考                                      |
| AI 编程    | [OpenAI Codex `rust-v0.129.0](https://github.com/openai/codex/releases/tag/rust-v0.129.0)`                                                                                    | 2026-05-07（相邻日期）                   | 开源 stable  | vim modal、sandbox/workspace `/diff`、`/hooks`、`/goal` discoverability 等一批 **CLI/TUI & 治理能力**齐备 GA                 |
| 开发者平台    | [GitHub：`More flexible secrets…`（Copilot cloud agent）](https://github.blog/changelog/2026-05-08-more-flexible-secrets-and-variables-for-copilot-cloud-agent/)                 | 2026-05-08                         | 平台 Release | Cloud agent **密钥/变量灵活性**直接关系多环境与工作流模版安全                                                                          |
| 开发者平台    | [GitHub：Copilot code review comment types in usage metrics API](https://github.blog/changelog/2026-05-08-copilot-code-review-comment-types-now-in-usage-metrics-api/)         | 2026-05-08                         | 平台 Release | 将 **静态分析类注释**并入用量 API，可做团队质量与采纳度观测                                                                               |
| 模型生命周期   | [GitHub：`Upcoming deprecation of Grok Code Fast 1](https://github.blog/changelog/2026-05-08-upcoming-deprecation-of-grok-code-fast-1/)`                                       | 2026-05-08                         | Retired    | 提醒在 Copilot/GitHub Models 侧的 **路由与回退预案**                                                                         |
| 应用安全     | [GitHub：CodeQL 2.25.3 adds Swift 6.3 support](https://github.blog/changelog/2026-05-08-codeql-2-25-3-adds-swift-6-3-support/)                                                 | 2026-05-08                         | 安全扫描       | Swift 6.3 规则刷新，可与 AI 生成移动端代码的同周治理联动                                                                              |
| 产业叙事     | [CNBC：Meta, Google enter AI agent race…](https://www.cnbc.com/2026/05/08/ai-agent-meta-google-agentic-wars-tech-download.html)                                                | 2026-05-08                         | 媒体综述       | 「OpenClaw 现象 → 竞品 Agent」叙事 & **trust/governance** 引述；需与官方 primary 对照阅读                                           |
| 政策相邻     | [CNBC：EU cloud sensitive data restrictions…](https://www.cnbc.com/2026/05/07/eu-commission-cloud-sensitive-data.html)                                                         | 2026-05-07（相邻日期）                   | 政策/地缘政治    | **跨境云与政务敏感数据**，影响模型训练与 Sovereign AI 选型                                                                           |
| 中文补充（相邻） | [量子位：ChatGPT 免费模型升级（GPT-5.5 Instant）](https://www.qbitai.com/2026/05/412995.html)                                                                                             | 2026-05-05（页面日期，相邻传播）              | 中文媒体       | 「幻觉」「记忆」「回答长度」产品力叙述，可作国内用户体感对照；**仍以 OpenAI primary 为准**                                                          |


### 技术文档与教程


| 方向              | 推荐资料                                                                                                                                                                                                                        | 核心技术点                                             | 适合谁看                              |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | --------------------------------- |
| Coding agent 治理 | [Running Codex safely at OpenAI](https://openai.com/index/running-codex-safely/) + [Codex 基础配置](https://developers.openai.com/codex/config-basic)                                                                           | sandbox、approval、auto_review、网络策略、rules、otel、合规日志 | SecDevOps / 平台工程                  |
| 供应链             | [Axios compromise 应答文](https://openai.com/index/axios-developer-tool-compromise/) + Google Threat Intel ([背景](https://cloud.google.com/blog/topics/threat-intelligence/north-korea-threat-actor-targets-axios-npm-package)) | 流水线固定 commit hash、发证材料隔离、证书轮转与客户沟通节拍              | CI/CD / 签名发布负责人                   |
| 对齐训练            | [Teaching Claude why](https://www.anthropic.com/research/teaching-claude-why)                                                                                                                                               | honeypots、constitutional SDF、RL 存续性               | 对齐 / 安全研究                         |
| 低延迟 Agent 模型    | [Gemini 3.1 Flash-Lite 文档（Enterprise Agent Platform）](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-1-flash-lite)                                                                          | 定价、时延档位、Enterprise Agent Platform                 | ML 平台 / 应用架构                      |
| Copilot 可观测     | [Usage metrics：comment types changelog](https://github.blog/changelog/2026-05-08-copilot-code-review-comment-types-now-in-usage-metrics-api/)                                                                               | REST schema 增量                                    | Inner Source / Developer Insights |
| MCP 安全（相邻）      | [Secret scanning w/ GitHub MCP Server GA](https://github.blog/changelog/2026-05-05-secret-scanning-with-github-mcp-server-is-now-generally-available/)                                                                      | MCP + secret scanning GA                          | Agent + GitHub MCP 集成团队           |


### LangChain / Agent / LLM 工程相关进展

**总体判断**：当日 **未发现** LangChain / LangGraph 官方博客带 **2026-05-08** 标注的更新；工程侧热点更多来自 **云平台 GA**、**GitHub Copilot 平台 changelog**、**coding agent OTel**，以及大厂 **竞品 Agent** 媒体叙事。


| 主题                  | 进展                                                  | 工程启发                                               |
| ------------------- | --------------------------------------------------- | -------------------------------------------------- |
| LangChain/LangGraph | 当日无核验到的官方新发版/博客条目                                   | 关注后续 **Deep Agents** 系列是否与托管 Agent 竞品形成镜像          |
| MCP                 | MCP registry `v1.7.7` 等为 **本周早前**相邻发布               | OIDC slice claims、HTML 逃逸等 **registry 健壮性**，适合私服镜像 |
| RAG/MCP/GitHub      | 2026-05-05 **Secret scanning + MCP Server GA**（相邻）  | 把 MCP 接入从「能用」升级到「可 governance」的一条路径                |
| 开源 coding agent     | **Codex stable 0.129.0**（2026-05-07）                | 治理能力（hooks/goals/marketplace）与 **Stable** cadence  |
| Agent 竞品            | CNBC：**Meta/Google** 个人助手类 Agent vs **OpenClaw** 先例 | 「能做」≠「可被信任」，需同步投资 **telemetry + approvals**        |


### 值得深入阅读的资料


| 推荐级别 | 资料                                                                                                       | 为什么值得读                                                    |
| ---- | -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| 必读   | [Teaching Claude why](https://www.anthropic.com/research/teaching-claude-why)                            | 对齐训练可操作结论（说理/宪法文本/多样性环境）集中度最高                             |
| 必读   | [Running Codex safely at OpenAI](https://openai.com/index/running-codex-safely/)                         | 少见的同时覆盖 **运行时控制面 + observability + 企业内部 triage playbook** |
| 推荐   | [Axios compromise 应答](https://openai.com/index/axios-developer-tool-compromise/)                         | 端到端 Incident 叙述 + **客户侧硬截止日期**对齐                          |
| 推荐   | [CNBC agent 「军备」稿](https://www.cnbc.com/2026/05/08/ai-agent-meta-google-agentic-wars-tech-download.html) | 理解资本市场与用户对 **personal agent** 的叙事和风险感知                    |
| 延伸   | [[arXiv:2605.05873] CITE…](https://arxiv.org/abs/2605.05873)                                             | **Self-consistency / 自适应停时**的理论化（提交日 2026-05-07，相邻精读）     |


### 来源清单

- 检索范围：2026-05-08 00:00:00 到 2026-05-08 23:59:59（Asia/Shanghai）
- 引用域名：openai.com, anthropic.com, cloud.google.com, github.com, github.blog, cnbc.com, arxiv.org, qbitai.com
- 来源清单表格：


| 类型             | 标题                                                  | 日期                          | 链接                                                                                                                                                                                                                         |
| -------------- | --------------------------------------------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 官方发布           | Our response to the Axios developer tool compromise | 生效 2026-05-08；文面 2026-04-10 | [https://openai.com/index/axios-developer-tool-compromise/](https://openai.com/index/axios-developer-tool-compromise/)                                                                                                     |
| 官方发布           | Running Codex safely at OpenAI                      | 2026-05-08                  | [https://openai.com/index/running-codex-safely/](https://openai.com/index/running-codex-safely/)                                                                                                                           |
| 研究             | Teaching Claude why                                 | 2026-05-08                  | [https://www.anthropic.com/research/teaching-claude-why](https://www.anthropic.com/research/teaching-claude-why)                                                                                                           |
| 官方发布           | Gemini 3.1 Flash-Lite GA                            | 2026-05-07（相邻日期）            | [https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-flash-lite-is-now-generally-available](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-flash-lite-is-now-generally-available) |
| 开源发布           | Codex rust-v0.129.0                                 | 2026-05-07（相邻日期）            | [https://github.com/openai/codex/releases/tag/rust-v0.129.0](https://github.com/openai/codex/releases/tag/rust-v0.129.0)                                                                                                   |
| 开源发布（相邻）       | OpenClaw v2026.5.7                                  | 2026-05-07（相邻日期）            | [https://github.com/openclaw/openclaw/releases/tag/v2026.5.7](https://github.com/openclaw/openclaw/releases/tag/v2026.5.7)                                                                                                 |
| 平台 Release     | Copilot secrets/variables cloud agent               | 2026-05-08                  | [https://github.blog/changelog/2026-05-08-more-flexible-secrets-and-variables-for-copilot-cloud-agent/](https://github.blog/changelog/2026-05-08-more-flexible-secrets-and-variables-for-copilot-cloud-agent/)             |
| 平台 Release     | Copilot code review metrics API                     | 2026-05-08                  | [https://github.blog/changelog/2026-05-08-copilot-code-review-comment-types-now-in-usage-metrics-api/](https://github.blog/changelog/2026-05-08-copilot-code-review-comment-types-now-in-usage-metrics-api/)               |
| 平台 Retired     | Grok Code Fast 1 deprecation                        | 2026-05-08                  | [https://github.blog/changelog/2026-05-08-upcoming-deprecation-of-grok-code-fast-1/](https://github.blog/changelog/2026-05-08-upcoming-deprecation-of-grok-code-fast-1/)                                                   |
| 平台 Improvement | Disable commit comments (user-level)                | 2026-05-08                  | [https://github.blog/changelog/2026-05-08-disable-commit-comments-on-the-user-level/](https://github.blog/changelog/2026-05-08-disable-commit-comments-on-the-user-level/)                                                 |
| 安全扫描           | CodeQL Swift 6.3                                    | 2026-05-08                  | [https://github.blog/changelog/2026-05-08-codeql-2-25-3-adds-swift-6-3-support/](https://github.blog/changelog/2026-05-08-codeql-2-25-3-adds-swift-6-3-support/)                                                           |
| 技术媒体           | The Tech Download: Agentic wars                     | 2026-05-08                  | [https://www.cnbc.com/2026/05/08/ai-agent-meta-google-agentic-wars-tech-download.html](https://www.cnbc.com/2026/05/08/ai-agent-meta-google-agentic-wars-tech-download.html)                                               |
| 政策相邻           | EU cloud / sensitive data                           | 2026-05-07                  | [https://www.cnbc.com/2026/05/07/eu-commission-cloud-sensitive-data.html](https://www.cnbc.com/2026/05/07/eu-commission-cloud-sensitive-data.html)                                                                         |
| 中文媒体（相邻）       | ChatGPT 免费模型升级量子位稿件                                 | 2026-05-05                  | [https://www.qbitai.com/2026/05/412995.html](https://www.qbitai.com/2026/05/412995.html)                                                                                                                                   |
| 论文相邻           | arXiv:2605.05873 CITE                               | 2026-05-07                  | [https://arxiv.org/abs/2605.05873](https://arxiv.org/abs/2605.05873)                                                                                                                                                       |

## 2026-05-07

### 今日总览

**一句话结论**：2026-05-07 的 AI 动态主线是“实时多模态、编码 Agent、Agent Skills、企业级 Agent 数据层、AI 安全与监管”同步推进，Agent 正从能执行任务走向能编排、能记忆、能审计、能通过 skills 复用团队流程。


| 维度     | 本日结论                                                                                                                                                                                                                                          |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 检索范围   | AI、LLM、Agent、RAG、MCP、Agent Skills、Codex Skills、Claude Code Skills、Cursor Skills、Claude Code、Codex、OpenClaw、Hermes、Spring AI、GitHub Copilot、Hugging Face Papers、语音多模态、企业 AI、AI 安全、政策监管                                                         |
| 核心趋势   | OpenAI 推进实时语音和网络安全能力分级；GitHub/Codex/OpenClaw/Hermes 形成编码 Agent 工具链更新；Codex/Cursor/Claude/GitHub 的 skills 文档让“可复用工作流”成为 Agent 工程基础设施；DeepMind、Sakana、Yugabyte 等展示 Agent 工程化和企业化方向                                                              |
| 可直接关注  | 实时语音 Agent、异构模型代码审查、Agent Skills 工作流复用、多 Agent 编排、Agent 共享记忆与审计、欧盟 AI Act 时间表                                                                                                                                                                 |
| 专项检索结论 | `Codex`、`OpenClaw`、`Hermes` 当天有可核验 release；`Claude Code` 当天无正式 release 但有相邻日期更新；`Spring AI` 当天无官方新发布但相邻日期资料仍有工程价值；`skills/Agent Skills` 当天未发现通用 marketplace 大发布，但 Codex、Claude Code、Cursor、GitHub CLI 和 JFrog Skills 的相邻日期资料显示 skills 生态正在标准化 |


### 重要事件与发布


| 主题           | 标题                                                                                                                                                                                                            | 日期                        | 类型            | 研发/学习价值                                                                                                                               |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| 语音多模态        | [OpenAI：Advancing voice intelligence with new models in the API](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/)                                                           | 2026-05-07                | 模型发布          | GPT-Realtime-2、Translate、Whisper 让语音 Agent 支持实时推理、工具调用、翻译和转写，适合客服、会议、语音助手和实时操作场景                                                      |
| AI 安全        | [OpenAI：Scaling Trusted Access for Cyber with GPT-5.5 and GPT-5.5-Cyber](https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/)                                                                     | 2026-05-07                | 模型发布/AI 安全    | 通过身份验证、分级访问和账户安全控制，把高风险网络安全能力开放给合规防御团队                                                                                                |
| 产品安全         | [OpenAI：Introducing Trusted Contact in ChatGPT](https://openai.com/index/introducing-trusted-contact-in-chatgpt/)                                                                                             | 2026-05-07                | 产品安全          | 展示敏感场景告警、人工复核和隐私最小披露机制，适合 AI 产品安全设计参考                                                                                                 |
| 可解释性         | [Anthropic：Natural Language Autoencoders](https://www.anthropic.com/research/natural-language-autoencoders)                                                                                                   | 2026-05-07                | 研究/模型评测       | 将模型激活转换为自然语言解释，为隐藏动机审计、红队分析和异常行为定位提供新方法                                                                                               |
| 编码 Agent     | [Google DeepMind：AlphaEvolve impact update](https://deepmind.google/blog/alphaevolve-impact/)                                                                                                                 | 2026-05-07                | Agent 工程/产业落地 | 展示 Gemini 编码 Agent 在 TPU、Spanner、科研和行业优化中的实际价值                                                                                        |
| AI 编程        | [GitHub：Rubber Duck in GitHub Copilot CLI now supports more models](https://github.blog/changelog/2026-05-07-rubber-duck-in-github-copilot-cli-now-supports-more-models/)                                     | 2026-05-07                | 开发者工具         | GPT/Claude 异构互审模式可用于发现架构问题、细微 bug 和跨文件冲突                                                                                              |
| AI 编程        | [OpenAI Codex 0.129.0-alpha.15](https://github.com/openai/codex/releases/tag/rust-v0.129.0-alpha.15)                                                                                                          | 2026-05-07                | 开源发布          | Codex 同步交付 CLI、app server、proxy、Windows sandbox 和 NPM 包，说明本地 coding agent 仍在快速迭代                                                      |
| Agent 框架     | [Hermes Agent v0.13.0](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.5.7)                                                                                                                   | 2026-05-07                | 开源发布          | 多 Agent Kanban、`/goal`、checkpoint v2、MCP 增强和 8 个 P0 修复，适合生产级 Agent 平台参考                                                               |
| Agent 运行时    | [OpenClaw v2026.5.7](https://github.com/openclaw/openclaw/releases/tag/v2026.5.7)                                                                                                                             | 2026-05-07                | 开源发布          | 修复权限、记忆开关、skill cache、Codex approval 和跨渠道投递，强化多平台 Agent runtime 稳定性                                                                   |
| Agent Skills | [JFrog Skills v0.8.0](https://github.com/jfrog/jfrog-skills/commit/acd7ad7eab071e37fa305c200f51d0d1cced3e82)                                                                                                  | 2026-05-06（相邻日期/中国时间窗口传播） | 开源发布/企业技能包    | 针对 JFrog 平台的 agent skills 更新了 `SKILL.md` 入口、chunked-read robustness、环境检查和 OneModel GraphQL 参考结构，说明企业工具正在把可审计、可分发的 skills 作为 Agent 接口层 |
| 数据基础设施       | [Yugabyte：Meko agent-native data infrastructure](https://www.businesswire.com/news/home/20260507728812/en/Yugabyte-Launches-Meko-a-Data-Infrastructure-to-Solve-the-Multi-Agent-Memory-and-Knowledge-Problem) | 2026-05-07                | 企业 AI/RAG 数据层 | 将记忆、知识、会话、trace 和 MCP 接口统一到 Agent 数据层，解决多 Agent 共享记忆和审计问题                                                                             |
| 多 Agent 编排   | [VentureBeat：Sakana RL Conductor / Fugu 多模型编排](https://venturebeat.com/orchestration/how-sakana-trained-a-7b-model-to-orchestrate-gpt-5-claude-sonnet-4-and-gemini-2-5-pro)                                   | 2026-05-07                | 技术媒体/多 Agent  | 7B conductor 用 RL 动态编排 GPT-5、Claude、Gemini 等 worker，是对静态 pipeline 的重要补充                                                               |
| 研究跟踪         | [Hugging Face Daily Papers 2026-05-07](https://huggingface.co/papers/date/2026-05-07)                                                                                                                         | 2026-05-07                | 论文聚合          | 当天论文覆盖多模态搜索 Agent、检索评测、编码 Agent benchmark、安全和医疗 Agent audit                                                                           |
| 政策监管         | [European Parliament：AI Act simplification deal reached](https://www.europarl.europa.eu/news/en/press-room/20260427IPR42011/ai-act-deal-on-simplification-measures-ban-on-nudifier-apps)                      | 2026-05-07                | 政策监管          | 明确高风险系统合规时点、水印义务和 nudifier 禁令，影响欧盟市场准入和治理路线图                                                                                          |


### 技术文档与教程


| 方向                 | 推荐资料                                                                                                                                             | 核心技术点                                                                            | 适合谁看                                                |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- | --------------------------------------------------- |
| 实时语音 Agent         | [OpenAI Realtime API 新语音模型说明](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/)                                 | 128K 上下文、并行工具调用、可调 reasoning effort、tool transparency、实时翻译/转写定价                  | 语音助手、客服、会议产品研发                                      |
| 异构模型审查             | [GitHub Copilot CLI Rubber Duck changelog](https://github.blog/changelog/2026-05-07-rubber-duck-in-github-copilot-cli-now-supports-more-models/) | 编排模型 + critic 模型，GPT/Claude 双向二审                                                 | IDE Agent、代码审查工具团队                                  |
| 本地 coding agent    | [Codex 0.129.0-alpha.15 release](https://github.com/openai/codex/releases/tag/rust-v0.129.0-alpha.15)                                            | CLI、app server、proxy、Windows sandbox、NPM 包、跨平台二进制                                | 编码助手平台、终端工具研发                                       |
| 长会话 coding agent   | [Claude Code Release v2.1.132](https://github.com/anthropics/claude-code/releases/tag/v2.1.132)                                                  | `CLAUDE_CODE_SESSION_ID`、alternate screen、终端/MCP/补全修复                            | 使用或构建 Claude Code 工作流的人                             |
| 多平台 Agent runtime  | [OpenClaw v2026.5.7 release](https://github.com/openclaw/openclaw/releases/tag/v2026.5.7)                                                        | skill cache、memory 权限、Codex approval、Cron 状态、跨渠道 delivery                        | Agent 运行时和消息平台接入团队                                  |
| Codex Skills       | [OpenAI Codex Agent Skills 文档](https://developers.openai.com/codex/skills)                                                                       | `SKILL.md`、渐进式加载、显式/隐式调用、repo/user/admin/system 多级目录、插件分发、技能启停配置                 | 需要把团队流程沉淀成 Codex 可复用能力的研发团队                         |
| Cursor Skills      | [Cursor Agent Skills 文档](https://www.cursor.com/docs/context/skills)                                                                             | `.agents/skills`、`.cursor/skills`、嵌套目录作用域、Claude/Codex 目录兼容、`/migrate-to-skills` | 使用 Cursor 组织项目级/用户级 Agent 能力的人                      |
| Claude Code Skills | [Claude Code Skills 文档](https://docs.anthropic.com/en/docs/claude-code/skills)                                                                   | `SKILL.md`、自动发现、显式调用、项目级/用户级技能、命令迁移                                              | 使用 Claude Code 构建长会话工作流的人                           |
| Skills 分发          | [GitHub CLI `gh skill](https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli)`                                            | 安装、搜索、发布、更新、tag pinning、tree SHA 变更检测、frontmatter provenance                     | 关注 skills 供应链、版本固定和跨 agent 分发的人                     |
| 企业工具 Skills        | [JFrog Skills v0.8.0](https://github.com/jfrog/jfrog-skills/commit/acd7ad7eab071e37fa305c200f51d0d1cced3e82)                                     | `SKILL.md` chunked-read robustness、确认式变更、server selection、环境脚本、GraphQL 参考文件路由    | 企业 DevSecOps / artifact / CVE / compliance Agent 场景 |
| Java Agent 生态      | [Spring AI 2.0.0-M5 Release](https://github.com/spring-projects/spring-ai/releases/tag/v2.0.0-M5)                                                | MCP Java SDK 升级、模块兼容性调整                                                          | Java/Spring AI 应用团队                                 |
| Agent 记忆管理         | [Spring AI Session API](https://spring.io/blog/2026/04/15/spring-ai-session-management)                                                          | 事件溯源会话、上下文压缩、多 Agent 分支隔离                                                        | 企业 Agent 平台研发                                       |
| AI 安全权限            | [OpenAI Trusted Access for Cyber](https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/)                                               | 分级访问、身份验证、防滥用边界、账号安全                                                             | 安全工程、红队、平台治理                                        |
| 模型可解释性             | [Anthropic NLA 研究与代码](https://www.anthropic.com/research/natural-language-autoencoders)                                                          | 激活重构、自然语言解释、隐藏动机审计                                                               | 模型评测、可解释性、AI 安全研究                                   |
| 法规合规               | [EU AI Act 议会文本](https://www.europarl.europa.eu/news/en/press-room/20260427IPR42011/ai-act-deal-on-simplification-measures-ban-on-nudifier-apps) | 高风险系统时间表、水印义务、禁用场景                                                               | 国际化产品、合规、治理团队                                       |


### LangChain / Agent / LLM 工程相关进展

**总体判断**：当天没有 LangChain/LangGraph/LlamaIndex 官方大版本，但 Agent 工程在“运行时可靠性、异构模型编排、共享记忆、评测基准、企业治理”上进展明显。


| 主题           | 进展                                                                                                                                                                   | 工程启发                                                 |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Claude Code  | 当天无正式 release；相邻日期 `v2.1.132` / `v2.1.129` 修复终端、缓存、OAuth、MCP、会话体验                                                                                                    | coding agent 的竞争点正在转向长会话稳定性、工具连接可靠性和细节体验             |
| Codex        | `0.129.0-alpha.15` 当天发布，覆盖 CLI、app server、proxy、sandbox                                                                                                              | 本地执行、跨平台分发和应用服务化会是 coding agent 的关键基础                |
| OpenClaw     | `v2026.5.7` 当天发布，修复权限、记忆、skill cache、Codex approval、消息投递                                                                                                             | 多平台 Agent runtime 需要把权限、记忆、投递状态和审批链路作为一等能力           |
| Hermes       | `v0.13.0` 当天发布，包含 Multi-agent Kanban、`/goal`、checkpoint v2、MCP 增强、8 个 P0 修复                                                                                          | 长久在线 Agent 服务需要任务板、目标锁定、恢复机制和安全默认值                   |
| Spring AI    | 当天无官方新发版；相邻日期资料强调 MCP Java SDK、Session API、上下文压缩和多 Agent 分支隔离                                                                                                        | Java 企业栈需要把 memory/session/compaction 做成框架级能力        |
| Agent Skills | 当天未发现通用 skills marketplace 大发布；OpenAI Codex、Cursor、Claude Code 文档均采用 `SKILL.md` + 渐进式加载思路，GitHub CLI 已提供 `gh skill` 安装/发布/更新能力，JFrog Skills 相邻日期 release 展示企业工具技能包实践 | skills 正在从“个人提示词集合”升级为可版本化、可分发、可审计、可跨 agent 复用的工作流单元 |
| RAG/MCP 数据层  | Yugabyte Meko、Weaviate Secure MCP Server（相邻日期）和 GraphRAG/MCP 讨论指向统一 memory/knowledge/trace 层                                                                         | 企业 Agent 的关键不是单次检索，而是共享记忆、权限、审计和可追踪上下文               |
| 论文与评测        | Hugging Face 当日论文覆盖多模态搜索 Agent、检索评测、编码 Agent 平台、安全与医疗 Agent audit                                                                                                    | 评测正在从单模型能力转向平台、任务、工具和领域 skill 的综合评价                  |
| 企业落地         | Teradata、Cognizant、Yugabyte、Sakana、Writer 等强调治理、编排、上下文和审计                                                                                                            | 企业 Agent 正在从 demo 走向生产平台，治理和数据上下文是落地前提               |


### 值得深入阅读的资料


| 推荐级别 | 资料                                                                                                                                                                                    | 为什么值得读                                                                                  |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| 必读   | [Advancing voice intelligence with new models in the API](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/)                                          | 实时语音 Agent 的能力边界发生变化，工具调用、长上下文和翻译/转写可直接进入产品设计                                           |
| 必读   | [Yugabyte Launches Meko](https://www.businesswire.com/news/home/20260507728812/en/Yugabyte-Launches-Meko-a-Data-Infrastructure-to-Solve-the-Multi-Agent-Memory-and-Knowledge-Problem) | 把 Agent 记忆、知识、会话和 trace 合成数据层，是企业 Agent 架构的关键方向                                         |
| 必读   | [Natural Language Autoencoders](https://www.anthropic.com/research/natural-language-autoencoders)                                                                                     | 可解释性从特征分析走向自然语言解释，有助于理解模型隐藏动机和评测偏差                                                      |
| 推荐   | [Hermes Agent v0.13.0 Release](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.5.7)                                                                                   | 多 Agent Kanban、恢复机制和安全修复非常适合参考生产级 Agent 平台建设                                            |
| 推荐   | [OpenAI Codex Agent Skills](https://developers.openai.com/codex/skills)                                                                                                               | 清晰说明 Codex 如何发现、选择、加载、分发和禁用 skills，适合作为编写团队技能的基准文档                                      |
| 推荐   | [Cursor Agent Skills](https://www.cursor.com/docs/context/skills)                                                                                                                     | 说明 Cursor 对 `.agents/skills`、`.cursor/skills`、Claude/Codex 目录兼容和嵌套作用域的支持，适合设计项目级 skills |
| 推荐   | [GitHub CLI `gh skill](https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli)`                                                                                 | 给 skills 生态补上搜索、安装、发布、更新、版本锁定和 provenance 管理，是团队分发 skills 的关键工具链参考                      |
| 推荐   | [Rubber Duck in GitHub Copilot CLI](https://github.blog/changelog/2026-05-07-rubber-duck-in-github-copilot-cli-now-supports-more-models/)                                             | 异构模型互审是提升代码审查质量的实用模式                                                                    |
| 推荐   | [Hugging Face Daily Papers 2026-05-07](https://huggingface.co/papers/date/2026-05-07)                                                                                                 | 便于跟踪 Agent 搜索、检索评测、编码 Agent benchmark 和安全 benchmark                                     |
| 延伸   | [Sakana RL Conductor / Fugu](https://venturebeat.com/orchestration/how-sakana-trained-a-7b-model-to-orchestrate-gpt-5-claude-sonnet-4-and-gemini-2-5-pro)                             | 帮助理解从静态 pipeline 到 RL 动态 orchestration 的架构转变                                            |
| 延伸   | [Spring AI Session API](https://spring.io/blog/2026/04/15/spring-ai-session-management)                                                                                               | Java 企业 Agent 的 session、memory、compaction、branch isolation 参考                           |


### 来源清单

- 检索范围：2026-05-07 00:00:00 到 2026-05-07 23:59:59（Asia/Shanghai）
- 引用域名：openai.com, developers.openai.com, anthropic.com, docs.anthropic.com, cursor.com, deepmind.google, github.blog, github.com, huggingface.co, businesswire.com, venturebeat.com, europarl.europa.eu, spring.io
- 来源清单表格：


| 类型         | 标题                                                                               | 日期                           | 链接                                                                                                                                                                                                                                                                                                                         |
| ---------- | -------------------------------------------------------------------------------- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 官方发布       | Advancing voice intelligence with new models in the API                          | 2026-05-07                   | [https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/)                                                                                                                                                     |
| 官方发布       | Scaling Trusted Access for Cyber with GPT-5.5 and GPT-5.5-Cyber                  | 2026-05-07                   | [https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/](https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/)                                                                                                                                                                                         |
| 官方发布       | Introducing Trusted Contact in ChatGPT                                           | 2026-05-07                   | [https://openai.com/index/introducing-trusted-contact-in-chatgpt/](https://openai.com/index/introducing-trusted-contact-in-chatgpt/)                                                                                                                                                                                       |
| 论文/研究原文    | Natural Language Autoencoders: Turning Claude’s thoughts into text               | 2026-05-07                   | [https://www.anthropic.com/research/natural-language-autoencoders](https://www.anthropic.com/research/natural-language-autoencoders)                                                                                                                                                                                       |
| 官方发布       | AlphaEvolve: How our Gemini-powered coding agent is scaling impact across fields | 2026-05-07                   | [https://deepmind.google/blog/alphaevolve-impact/](https://deepmind.google/blog/alphaevolve-impact/)                                                                                                                                                                                                                       |
| 开发者工具      | Rubber Duck in GitHub Copilot CLI now supports more models                       | 2026-05-07                   | [https://github.blog/changelog/2026-05-07-rubber-duck-in-github-copilot-cli-now-supports-more-models/](https://github.blog/changelog/2026-05-07-rubber-duck-in-github-copilot-cli-now-supports-more-models/)                                                                                                               |
| 开源发布       | OpenAI Codex 0.129.0-alpha.15                                                    | 2026-05-07                   | [https://github.com/openai/codex/releases/tag/rust-v0.129.0-alpha.15](https://github.com/openai/codex/releases/tag/rust-v0.129.0-alpha.15)                                                                                                                                                                                 |
| 开源发布       | Hermes Agent v0.13.0 (2026.5.7)                                                  | 2026-05-07                   | [https://github.com/NousResearch/hermes-agent/releases/tag/v2026.5.7](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.5.7)                                                                                                                                                                                 |
| 开源发布       | OpenClaw v2026.5.7                                                               | 2026-05-07                   | [https://github.com/openclaw/openclaw/releases/tag/v2026.5.7](https://github.com/openclaw/openclaw/releases/tag/v2026.5.7)                                                                                                                                                                                                 |
| 官方文档       | OpenAI Codex Agent Skills                                                        | 2026-05-07 专项检索核验            | [https://developers.openai.com/codex/skills](https://developers.openai.com/codex/skills)                                                                                                                                                                                                                                   |
| 官方文档       | Cursor Agent Skills                                                              | 2026-05-07 专项检索核验            | [https://www.cursor.com/docs/context/skills](https://www.cursor.com/docs/context/skills)                                                                                                                                                                                                                                   |
| 官方文档       | Claude Code Skills                                                               | 2026-05-07 专项检索核验            | [https://docs.anthropic.com/en/docs/claude-code/skills](https://docs.anthropic.com/en/docs/claude-code/skills)                                                                                                                                                                                                             |
| 开发者工具      | Manage agent skills with GitHub CLI                                              | 2026-04-16（相邻日期/skills 生态背景） | [https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli](https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli)                                                                                                                                                               |
| 开源发布       | JFrog Skills v0.8.0                                                              | 2026-05-06（相邻日期/中国时间窗口传播）    | [https://github.com/jfrog/jfrog-skills/commit/acd7ad7eab071e37fa305c200f51d0d1cced3e82](https://github.com/jfrog/jfrog-skills/commit/acd7ad7eab071e37fa305c200f51d0d1cced3e82)                                                                                                                                             |
| 开源发布       | Claude Code v2.1.132                                                             | 2026-05-06（相邻日期/中国时间窗口传播）    | [https://github.com/anthropics/claude-code/releases/tag/v2.1.132](https://github.com/anthropics/claude-code/releases/tag/v2.1.132)                                                                                                                                                                                         |
| 开源发布       | Spring AI 2.0.0-M5                                                               | 2026-04-27（相邻日期/中国时间窗口传播）    | [https://github.com/spring-projects/spring-ai/releases/tag/v2.0.0-M5](https://github.com/spring-projects/spring-ai/releases/tag/v2.0.0-M5)                                                                                                                                                                                 |
| 官方技术博客     | Spring AI Agentic Patterns (Part 7): Session API                                 | 2026-04-15（相邻日期/中国时间窗口传播）    | [https://spring.io/blog/2026/04/15/spring-ai-session-management](https://spring.io/blog/2026/04/15/spring-ai-session-management)                                                                                                                                                                                           |
| 论文聚合       | Hugging Face Daily Papers                                                        | 2026-05-07                   | [https://huggingface.co/papers/date/2026-05-07](https://huggingface.co/papers/date/2026-05-07)                                                                                                                                                                                                                             |
| 企业 AI 基础设施 | Yugabyte Launches Meko                                                           | 2026-05-07                   | [https://www.businesswire.com/news/home/20260507728812/en/Yugabyte-Launches-Meko-a-Data-Infrastructure-to-Solve-the-Multi-Agent-Memory-and-Knowledge-Problem](https://www.businesswire.com/news/home/20260507728812/en/Yugabyte-Launches-Meko-a-Data-Infrastructure-to-Solve-the-Multi-Agent-Memory-and-Knowledge-Problem) |
| 技术媒体       | Sakana RL Conductor / Fugu multi-agent orchestration                             | 2026-05-07                   | [https://venturebeat.com/orchestration/how-sakana-trained-a-7b-model-to-orchestrate-gpt-5-claude-sonnet-4-and-gemini-2-5-pro](https://venturebeat.com/orchestration/how-sakana-trained-a-7b-model-to-orchestrate-gpt-5-claude-sonnet-4-and-gemini-2-5-pro)                                                                 |
| 政策与标准      | AI Act: deal on simplification measures, ban on “nudifier” apps                  | 2026-05-07                   | [https://www.europarl.europa.eu/news/en/press-room/20260427IPR42011/ai-act-deal-on-simplification-measures-ban-on-nudifier-apps](https://www.europarl.europa.eu/news/en/press-room/20260427IPR42011/ai-act-deal-on-simplification-measures-ban-on-nudifier-apps)                                                           |

## 2026-05-06

### 今日总览

**一句话结论**：2026-05-06 的主线是“算力与配额驱动的 Agent 开发体验改善 + 开发者工具持续工程化”，其中 Anthropic 的算力合作及 Claude/Claude Code 限额调整最具即时影响。


| 维度     | 本日结论                                                                                                                                                                                    |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 检索范围   | AI、LLM、Agent、Claude Code、Codex、OpenClaw、Hermes、Spring AI、GitHub Copilot、Hugging Face Papers、Agent Skills、政策与企业基础设施                                                                      |
| 核心趋势   | 算力供给与产品配额直接影响开发者体验；Copilot 与 coding agent 工具继续提升工程流畅度；Agent 研究继续向多 Agent 协作与工作区任务评测推进                                                                                                   |
| 可直接关注  | Claude/Claude Code 限额变化、Copilot VS Code 版本演进、Agent 基准（Workspace-Bench/OpenSeeker-v2）                                                                                                    |
| 专项检索结论 | `Claude Code` 当天有 release（v2.1.131/v2.1.129）；`Codex` 相邻日期有 release（v0.129.0-alpha.6 于 2026-05-05）；`OpenClaw`/`Hermes` 当天未见独立新 release；`Spring AI` 当天无新发版；`skills` 当天无通用 marketplace 大发布 |


### 重要事件与发布


| 主题          | 标题                                                                                                                                                    | 日期         | 类型    | 研发/学习价值                                                             |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ----- | ------------------------------------------------------------------- |
| 算力与产品策略     | [Anthropic: Higher usage limits for Claude and a compute deal with SpaceX](https://www.anthropic.com/news/higher-limits-spacex)                       | 2026-05-06 | 官方发布  | 通过新增算力提升 Claude / Claude Code 使用上限，说明“模型能力”与“算力配额策略”已深度耦合，直接影响生产可用性 |
| AI 编程工具     | [GitHub Copilot in Visual Studio Code, April releases](https://github.blog/changelog/2026-05-06-github-copilot-in-visual-studio-code-april-releases/) | 2026-05-06 | 开发者工具 | 涵盖语义检索、会话回溯、终端联动等能力，反映 IDE agent 正从问答助手走向持续协作执行体                    |
| Claude Code | [Claude Code v2.1.131](https://github.com/anthropics/claude-code/releases/tag/v2.1.131)                                                               | 2026-05-06 | 开源发布  | 修复 Windows 扩展激活和认证问题，持续提升跨平台稳定性                                     |
| Claude Code | [Claude Code v2.1.129](https://github.com/anthropics/claude-code/releases/tag/v2.1.129)                                                               | 2026-05-06 | 开源发布  | 增加插件 URL 获取能力并修复多项交互问题，强化工具扩展与终端体验                                  |
| 论文跟踪        | [Hugging Face Daily Papers 2026-05-06](https://huggingface.co/papers/date/2026-05-06)                                                                 | 2026-05-06 | 论文聚合  | 当日论文集中在多 Agent 协作、搜索 agent 与工作区任务评测，为 Agent 工程评测提供新样本               |


### 技术文档与教程


| 方向              | 推荐资料                                                                                                                                                      | 核心技术点                                | 适合谁看                 |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | -------------------- |
| 产品配额与算力         | [Anthropic 官方公告](https://www.anthropic.com/news/higher-limits-spacex)                                                                                     | 配额上调、算力协同、企业级容量规划                    | 关注 AI 平台容量与成本治理的团队   |
| IDE Agent 演进    | [Copilot VS Code 更新](https://github.blog/changelog/2026-05-06-github-copilot-in-visual-studio-code-april-releases/)                                       | 语义检索、会话连续性、终端联动                      | 开发效率平台、IDE 工具链团队     |
| Claude Code 稳定性 | [v2.1.131](https://github.com/anthropics/claude-code/releases/tag/v2.1.131) / [v2.1.129](https://github.com/anthropics/claude-code/releases/tag/v2.1.129) | Windows 兼容、认证链路、插件获取、交互修复            | 使用 Claude Code 的研发团队 |
| Agent 研究输入      | [HF Daily Papers 2026-05-06](https://huggingface.co/papers/date/2026-05-06)                                                                               | OpenSeeker-v2、Workspace-Bench、ARIS 等 | 做 Agent 评测和任务编排的人    |


### LangChain / Agent / LLM 工程相关进展

**总体判断**：当天官方大模型能力发布不密集，但 coding agent 与开发者工作流工具持续迭代，工程重心转向“稳定性、连续会话和可执行性”。


| 主题           | 进展                                               | 工程启发                                 |
| ------------ | ------------------------------------------------ | ------------------------------------ |
| Claude Code  | 当天连续发布 v2.1.131 / v2.1.129，集中修复平台兼容与交互问题         | coding agent 在真实场景的竞争焦点是稳定与可持续会话体验   |
| Codex        | 当天无新 release；相邻日期 `v0.129.0-alpha.6`（2026-05-05） | 需关注高频 alpha 节奏下的回归验证与版本治理            |
| OpenClaw     | 当天未检索到可核验新 release                               | 运行时类项目需结合相邻日期更新观察稳定性趋势               |
| Hermes       | 当天未检索到可核验新 release（相邻日期 `v0.12.0` 于 2026-04-30）  | 多 Agent 平台演进更偏周级节奏，建议按周追踪            |
| Spring AI    | 当天无新发版（相邻日期 `v2.0.0-M5`）                         | Java Agent 栈仍处于里程碑迭代期，关注 API 兼容变化    |
| Agent Skills | 当天未发现通用 skills marketplace 大发布                   | skills 生态以文档标准化和 host 工具链集成为主，而非单日爆发 |


### 值得深入阅读的资料


| 推荐级别 | 资料                                                                                                                                                    | 为什么值得读                            |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| 必读   | [Anthropic: Higher usage limits for Claude and a compute deal with SpaceX](https://www.anthropic.com/news/higher-limits-spacex)                       | 对“算力-配额-产品可用性”的联动关系解释最直接，影响团队容量规划 |
| 推荐   | [GitHub Copilot in Visual Studio Code, April releases](https://github.blog/changelog/2026-05-06-github-copilot-in-visual-studio-code-april-releases/) | 展示 IDE agent 在检索、会话、终端上的系统化增强     |
| 推荐   | [Claude Code v2.1.131](https://github.com/anthropics/claude-code/releases/tag/v2.1.131)                                                               | 反映跨平台问题修复优先级与实际落地痛点               |
| 推荐   | [Hugging Face Daily Papers 2026-05-06](https://huggingface.co/papers/date/2026-05-06)                                                                 | 汇总多 Agent 与任务评测方向，适合筛选后续精读论文      |


### 来源清单

- 检索范围：2026-05-06 00:00:00 到 2026-05-06 23:59:59（Asia/Shanghai）
- 引用域名：anthropic.com, github.blog, github.com, huggingface.co
- 来源清单表格：


| 类型    | 标题                                                            | 日期                        | 链接                                                                                                                                                                                             |
| ----- | ------------------------------------------------------------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 官方发布  | Higher usage limits for Claude and a compute deal with SpaceX | 2026-05-06                | [https://www.anthropic.com/news/higher-limits-spacex](https://www.anthropic.com/news/higher-limits-spacex)                                                                                     |
| 开发者工具 | GitHub Copilot in Visual Studio Code, April releases          | 2026-05-06                | [https://github.blog/changelog/2026-05-06-github-copilot-in-visual-studio-code-april-releases/](https://github.blog/changelog/2026-05-06-github-copilot-in-visual-studio-code-april-releases/) |
| 开源发布  | Claude Code v2.1.131                                          | 2026-05-06                | [https://github.com/anthropics/claude-code/releases/tag/v2.1.131](https://github.com/anthropics/claude-code/releases/tag/v2.1.131)                                                             |
| 开源发布  | Claude Code v2.1.129                                          | 2026-05-06                | [https://github.com/anthropics/claude-code/releases/tag/v2.1.129](https://github.com/anthropics/claude-code/releases/tag/v2.1.129)                                                             |
| 开源发布  | OpenAI Codex v0.129.0-alpha.6                                 | 2026-05-05（相邻日期/中国时间窗口传播） | [https://github.com/openai/codex/releases/tag/rust-v0.129.0-alpha.6](https://github.com/openai/codex/releases/tag/rust-v0.129.0-alpha.6)                                                       |
| 开源发布  | Hermes Agent v0.12.0                                          | 2026-04-30（相邻日期/中国时间窗口传播） | [https://github.com/NousResearch/hermes-agent/releases/tag/v2026.4.30](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.4.30)                                                   |
| 开源发布  | Spring AI 2.0.0-M5                                            | 2026-04-27（相邻日期/中国时间窗口传播） | [https://github.com/spring-projects/spring-ai/releases/tag/v2.0.0-M5](https://github.com/spring-projects/spring-ai/releases/tag/v2.0.0-M5)                                                     |
| 论文聚合  | Hugging Face Daily Papers                                     | 2026-05-06                | [https://huggingface.co/papers/date/2026-05-06](https://huggingface.co/papers/date/2026-05-06)                                                                                                 |

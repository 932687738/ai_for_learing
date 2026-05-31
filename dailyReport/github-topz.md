# GitHub 快照（Stars Search API + Trending）

本文件由 `tools/update_github_topz.py` 生成，两块内容独立编排：

- **模块一**：`tools/github_topz/stars_merge.py` → GitHub REST `/search/repositories` 全局 Star 前十名，并按既有规则与本节历史 Markdown 表格合并（列结构与原 `github-topz.md` 一致）。
- **模块二**：`tools/github_topz/trending_fetch.py` → 抓取 Trending 「今日 / 本周 / 本月」页面 HTML，`article.Box-row` 解析后与中文简介渲染。
- **标记列**：各表相对**本次运行前**已保存的 `github-topz.md` 中对应表格出现过的 `owner/repo` 做差集；首次出现标 **新增**；再次运行会先清空上一轮「新增」后仅标记新一轮新增（详见 `.cursor/rules/dual-digest-on-pull.mdc`）。

---
## 全局 Star Search API（与文件历史合并）

- 数据源：[`dual-digest-on-pull`](../.cursor/rules/dual-digest-on-pull.mdc) 工作流程下配套的 GitHub Search API：`sort=stars` **全局前十名**（`/search/repositories`）。与本节历史行合并时：**已出现的仓库更新 Stars**，新仓库按 Star **降序** 参与整表排序。
- **仓库简介**列：数据源为 GitHub `description`，**写入时为中文简述**——常见仓库内置固定中文提要；其余在渲染时尽力通过公开翻译接口转写，失败则回退英文摘录。表格中若为中文且无新的英文数据源，会直接沿用原有中文单元格。
- **与 Trending 区别**：本节为全局累计 Star 排序快照；文末 Trending 为 GitHub「今日 / 本周 / 本月热度」榜单，数据源与口径均不同。
- **标记**列：相对**本次拉取前**磁盘上 `github-topz.md` 中本节表格已存在的 `owner/repo`，不存在的行标为 **新增**；下次拉取会重新计算并清空上一次的「新增」（仅保留新一轮相对上一轮新增）。

**最近一次更新时间**（Asia/Shanghai）： 2026-05-31 13:10:02

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 508372 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 471552 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 445659 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 437978 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 389242 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 375712 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 355763 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 351050 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 347824 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 300455 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
| 11 | `awesome-selfhosted/awesome-selfhosted` | 295209 | 可自行部署的各类自由软件网络服务与 Web 应用清单。 | https://github.com/awesome-selfhosted/awesome-selfhosted |  |
| 12 | `practical-tutorials/project-based-learning` | 266609 | 基于项目的教程精选列表 | https://github.com/practical-tutorials/project-based-learning |  |
| 13 | `facebook/react` | 245279 | 用于构建 Web 与原生用户界面的 React 视图库（含多端生态）。 | https://github.com/facebook/react |  |

---
## Trending 页面快照（HTML 抓取）

**说明**：与上方「全局 Star Search」数据源不同；本段按 GitHub trending 页的 **daily / weekly / monthly** 各拉一页并解析。**若前端改版导致选择器失效，需更新解析逻辑。**

- **标记**列：三个 `since` 子表**各自独立**对照本次拉取前文件中该小节表格已出现的 `owner/repo`；新出现的行标 **新增**。下次拉取会先清空上一轮「新增」再重算（只保留相对**上一版文件**的新仓库）。

### 今日 trending（since=daily）

**页面**： `https://github.com/trending?since=daily`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `microsoft/markitdown` | 132830 | 9089 | Python | 2,470 stars today | 用于将文件和Office文档转换为Markdown的Python工具。 | https://github.com/microsoft/markitdown | 新增 |
| 2 | `harry0703/MoneyPrinterTurbo` | 72291 | 10363 | Python | 2,768 stars today | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. | https://github.com/harry0703/MoneyPrinterTurbo | 新增 |
| 3 | `anthropics/claude-code` | 128474 | 20953 | Python | 592 stars today | Claude Code是一个代理编码工具，它位于您的终端中，了解您的代码库，并通过执行日常任务、解释复杂代码和处理git工作流程（所有这些都通过自然语言命令）来帮助您更快地进行编码。 | https://github.com/anthropics/claude-code | 新增 |
| 4 | `cursor/plugins` | 1489 | 120 | TypeScript | 205 stars today | 光标插件规范和官方插件 | https://github.com/cursor/plugins | 新增 |
| 5 | `revfactory/harness` | 4321 | 629 | HTML | 55 stars today | 一种元技能，用于设计特定领域的座席团队，定义专业座席，并生成他们使用的技能。 | https://github.com/revfactory/harness | 新增 |
| 6 | `EveryInc/compound-engineering-plugin` | 18455 | 1393 | TypeScript | 349 stars today | Claude Code、Codex、Cursor等的官方复合工程插件 | https://github.com/EveryInc/compound-engineering-plugin | 新增 |
| 7 | `affaan-m/ECC` | 199466 | 30623 | JavaScript | 908 stars today | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC | 新增 |
| 8 | `OpenBMB/VoxCPM` | 22880 | 2676 | Python | 779 stars today | VoxCPM2 ：用于多语言语音生成、创意语音设计和真实克隆的无标记TTS | https://github.com/OpenBMB/VoxCPM | 新增 |
| 9 | `galilai-group/stable-worldmodel` | 1487 | 168 | Python | 318 stars today | 可重现的世界模型研究和评估平台 | https://github.com/galilai-group/stable-worldmodel | 新增 |
| 10 | `Crosstalk-Solutions/project-nomad` | 27396 | 2688 | TypeScript | 469 stars today | Project N.O.M.A.D是一款独立的离线生存计算机，配备了关键工具、知识和人工智能，可随时随地让您随时了解情况并获得授权。 | https://github.com/Crosstalk-Solutions/project-nomad | 新增 |
| 11 | `run-llama/liteparse` | 7988 | 472 | Rust | 925 stars today | 快速、实用、开源的文档解析器 | https://github.com/run-llama/liteparse | 新增 |
| 12 | `chen08209/FlClash` | 40418 | 2530 | Dart | 187 stars today | 基于ClashMeta的多平台代理客户端，简单易用，开源且无广告。 | https://github.com/chen08209/FlClash | 新增 |
| 13 | `FareedKhan-dev/train-llm-from-scratch` | 2365 | 379 | Jupyter Notebook | 327 stars today | 从下载数据到生成文本，这是培训LLM的简单方法。 | https://github.com/FareedKhan-dev/train-llm-from-scratch | 新增 |
| 14 | `ruvnet/RuView` | 69019 | 9206 | Rust | 655 stars today | π RuView将商用WiFi信号转化为实时空间智能、生命体征监测和存在检测--所有这些都无需一个像素的视频。 | https://github.com/ruvnet/RuView | 新增 |
| 15 | `DataTalksClub/data-engineering-zoomcamp` | 41807 | 8288 | Jupyter Notebook | 274 stars today | Data Engineering Zoomcamp是一门为期9周的关于构建生产就绪数据管道的免费课程。下一个队列将于2026年1月开始。在此处加入课程 👇🏼 | https://github.com/DataTalksClub/data-engineering-zoomcamp | 新增 |
| 16 | `OpenMOSS/MOSS-TTS` | 2671 | 239 | Python | 62 stars today | MOSS ‑ TTS家族是来自MOSI.AI和OpenMOSS团队的开源语音和声音生成模型家族。它专为高保真、高表现力和复杂的现实世界场景而设计，涵盖稳定的长篇语音、多扬声器对话、语音/字符设计…… | https://github.com/OpenMOSS/MOSS-TTS | 新增 |
| 17 | `dreammis/social-auto-upload` | 11861 | 2097 | Python | 73 stars today | 自动化上传视频到社交媒体：抖音、小红书、视频号、tiktok、youtube、bilibili | https://github.com/dreammis/social-auto-upload | 新增 |
| 18 | `anthropics/skills` | 144259 | 16998 | Python | 454 stars today | 座席技能的公共存储库 | https://github.com/anthropics/skills | 新增 |
| 19 | `codecrafters-io/build-your-own-x` | 508372 | 48249 | Markdown | 817 stars today | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `harry0703/MoneyPrinterTurbo` | 72293 | 10363 | Python | 13,948 stars this week | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. | https://github.com/harry0703/MoneyPrinterTurbo | 新增 |
| 2 | `Lum1104/Understand-Anything` | 46204 | 3735 | TypeScript | 25,612 stars this week | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Lum1104/Understand-Anything | 新增 |
| 3 | `rohitg00/ai-engineering-from-scratch` | 25266 | 4093 | Python | 12,082 stars this week | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch | 新增 |
| 4 | `anthropics/knowledge-work-plugins` | 18278 | 2146 | Python | 5,538 stars this week | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins | 新增 |
| 5 | `colbymchenry/codegraph` | 34536 | 2110 | TypeScript | 15,909 stars this week | Claude Code、Codex、Gemini、Cursor、OpenCode、AntiGravity、Kiro和Hermes Agent的预索引代码知识图—代币更少，工具调用更少， 100%本地化 | https://github.com/colbymchenry/codegraph | 新增 |
| 6 | `hardikpandya/stop-slop` | 7474 | 524 | — | 3,543 stars this week | 从散文中删除AI TELLS的技能文件 | https://github.com/hardikpandya/stop-slop | 新增 |
| 7 | `mukul975/Anthropic-Cybersecurity-Skills` | 12645 | 1468 | Python | 5,417 stars this week | 人工智能代理的754种结构化网络安全技能·映射到5个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND和NIST AI RMF · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20多个平台· 26个安全数据…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills | 新增 |
| 8 | `Leonxlnx/taste-skill` | 29253 | 2162 | Shell | 10,202 stars this week | 品味技能-让您的人工智能有良好的品味。阻止人工智能产生无聊的通用斜坡 | https://github.com/Leonxlnx/taste-skill | 新增 |
| 9 | `microsoft/markitdown` | 132831 | 9089 | Python | 6,652 stars this week | 用于将文件和Office文档转换为Markdown的Python工具。 | https://github.com/microsoft/markitdown | 新增 |
| 10 | `anthropics/claude-plugins-official` | 28837 | 3067 | Python | 2,771 stars this week | 由Anthropic管理的高质量Claude Code插件的官方目录。 | https://github.com/anthropics/claude-plugins-official | 新增 |
| 11 | `affaan-m/ECC` | 199466 | 30623 | JavaScript | 10,802 stars this week | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC | 新增 |
| 12 | `cursor/plugins` | 1489 | 120 | TypeScript | 738 stars this week | 光标插件规范和官方插件 | https://github.com/cursor/plugins | 新增 |
| 13 | `microsoft/agent-governance-toolkit` | 3480 | 498 | Python | 1,553 stars this week | AI代理治理工具包—针对自主AI代理的策略实施、零信任身份、执行沙盒和可靠性工程。涵盖10/10 OWASP Agentic Top 10。 | https://github.com/microsoft/agent-governance-toolkit | 新增 |
| 14 | `dograh-hq/dograh` | 3888 | 782 | Python | 1,236 stars this week | 开源语音AI平台。Vapi和Retell的自托管替代品。在PREM上， BYOK跨语音到语音或LLM/STT/TTS ，具有可视化工作流程构建器、MCP本机和电话支持。 | https://github.com/dograh-hq/dograh | 新增 |
| 15 | `revfactory/harness` | 4321 | 629 | HTML | 626 stars this week | 一种元技能，用于设计特定领域的座席团队，定义专业座席，并生成他们使用的技能。 | https://github.com/revfactory/harness | 新增 |
| 16 | `ogulcancelik/herdr` | 3245 | 212 | Rust | 923 stars this week | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr | 新增 |
| 17 | `can1357/oh-my-pi` | 8817 | 705 | TypeScript | 1,963 stars this week | 终端的AI编码代理—哈希锚定编辑、优化工具线束、LSP、Python、浏览器、子代理等 | https://github.com/can1357/oh-my-pi | 新增 |
| 18 | `p-e-w/heretic` | 22540 | 2391 | Python | 1,248 stars this week | 语言模型的全自动审查删除 | https://github.com/p-e-w/heretic | 新增 |
| 19 | `Chachamaru127/claude-code-harness` | 2302 | 227 | Shell | 1,034 stars this week | Claude Code Dedicated Development Harness -通过自主计划→工作→审核周期实现高质量发展 | https://github.com/Chachamaru127/claude-code-harness | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `colbymchenry/codegraph` | 34536 | 2110 | TypeScript | 33,455 stars this month | Claude Code、Codex、Gemini、Cursor、OpenCode、AntiGravity、Kiro和Hermes Agent的预索引代码知识图—代币更少，工具调用更少， 100%本地化 | https://github.com/colbymchenry/codegraph | 新增 |
| 2 | `anthropics/financial-services` | 28905 | 4049 | Python | 21,134 stars this month | — | https://github.com/anthropics/financial-services | 新增 |
| 3 | `CloakHQ/CloakBrowser` | 22682 | 1805 | Python | 21,160 stars this month | Stealth Chromium可通过每次机器人检测测试。插入式剧作家更换源级指纹补丁，通过30/30测试 | https://github.com/CloakHQ/CloakBrowser | 新增 |
| 4 | `Lum1104/Understand-Anything` | 46204 | 3735 | TypeScript | 36,047 stars this month | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Lum1104/Understand-Anything | 新增 |
| 5 | `rohitg00/agentmemory` | 19982 | 1648 | TypeScript | 17,789 stars this month | # 1基于真实世界基准的AI编码代理持久内存 | https://github.com/rohitg00/agentmemory | 新增 |
| 6 | `Imbad0202/academic-research-skills` | 24634 | 2037 | Python | 20,575 stars this month | Claude Code的学术研究技能：研究→撰写→评审→修订→最终确定 | https://github.com/Imbad0202/academic-research-skills | 新增 |
| 7 | `mattpocock/skills` | 112448 | 9871 | Shell | 71,266 stars this month | 真正工程师的技能。直接来自我的.claude目录。 | https://github.com/mattpocock/skills | 新增 |
| 8 | `rohitg00/ai-engineering-from-scratch` | 25266 | 4093 | Python | 19,463 stars this month | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch | 新增 |
| 9 | `decolua/9router` | 15279 | 2288 | JavaScript | 11,936 stars this month | 无限免费AI编码。通过40多家供应商将Claude Code、Codex、Cursor、Cline、Copilot、Antigravity连接到免费的Claude/GPT/Gemini。自动回退， RTK -40%代币，从未达到限制。 | https://github.com/decolua/9router | 新增 |
| 10 | `yikart/AiToEarn` | 17133 | 2734 | TypeScript | 8,137 stars this month | 让我们使用人工智能来赚取收入！ | https://github.com/yikart/AiToEarn | 新增 |
| 11 | `ruvnet/ruflo` | 56717 | 6459 | TypeScript | 23,037 stars this month | 🌊 Claude的领先代理编排平台。部署智能多智能体群，协调自主工作流程，构建对话式人工智能系统。具有企业级架构、自学群体智能、RAG集成和本地Claude Code/… | https://github.com/ruvnet/ruflo | 新增 |
| 12 | `bytedance/UI-TARS-desktop` | 35770 | 3600 | TypeScript | 6,319 stars this month | 开源多模态人工智能代理堆栈：连接尖端人工智能模型和代理基础设施 | https://github.com/bytedance/UI-TARS-desktop | 新增 |
| 13 | `AIDC-AI/Pixelle-Video` | 20600 | 2891 | Python | 13,102 stars this month | 🚀 AI 全自动短视频引擎 · AI Fully Automated Short Video Engine | https://github.com/AIDC-AI/Pixelle-Video | 新增 |
| 14 | `multica-ai/andrej-karpathy-skills` | 162705 | 16665 | — | 65,076 stars this month | 一个用于改进Claude Code行为的CLAUDE.md文件，源自Andrej Karpathy对LLM编码陷阱的观察。 | https://github.com/multica-ai/andrej-karpathy-skills | 新增 |
| 15 | `soxoj/maigret` | 31104 | 2225 | Python | 11,299 stars this month | 通过用户名从3000多个网站🕵️‍♂️收集个人档案 | https://github.com/soxoj/maigret | 新增 |
| 16 | `TauricResearch/TradingAgents` | 81057 | 15754 | Python | 26,772 stars this month | TradingAgent ：多代理LLM金融交易框架 | https://github.com/TauricResearch/TradingAgents | 新增 |
| 17 | `LearningCircuit/local-deep-research` | 8221 | 706 | Python | 3,835 stars this month | SimpleQA约95% （例如3090上的Qwen3.6-27B ）。支持所有本地和云LLM （ llama.cpp、Ollama、Google等）。10多个搜索引擎- arXiv、PubMed、您的私人文档。本地和加密的一切。 | https://github.com/LearningCircuit/local-deep-research | 新增 |
| 18 | `1jehuang/jcode` | 6766 | 754 | Rust | 5,765 stars this month | 编码代理线束 | https://github.com/1jehuang/jcode | 新增 |


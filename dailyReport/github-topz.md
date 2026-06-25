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

**最近一次更新时间**（Asia/Shanghai）： 2026-06-25 10:29:55

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 519309 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 478563 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 450461 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 444057 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 390752 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 380319 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 358196 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 354732 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 353865 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 304690 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
| 11 | `awesome-selfhosted/awesome-selfhosted` | 297987 | 可自行部署的各类自由软件网络服务与 Web 应用清单。 | https://github.com/awesome-selfhosted/awesome-selfhosted |  |
| 12 | `996icu/996.ICU` | 276267 | 倡议关注「996」工作制、计数星标与交流的开发社区仓库（含网络迷因用语）。 | https://github.com/996icu/996.ICU |  |
| 13 | `practical-tutorials/project-based-learning` | 267810 | 基于项目的教程精选列表 | https://github.com/practical-tutorials/project-based-learning |  |
| 14 | `facebook/react` | 245279 | 用于构建 Web 与原生用户界面的 React 视图库（含多端生态）。 | https://github.com/facebook/react |  |

---
## Trending 页面快照（HTML 抓取）

**说明**：与上方「全局 Star Search」数据源不同；本段按 GitHub trending 页的 **daily / weekly / monthly** 各拉一页并解析。**若前端改版导致选择器失效，需更新解析逻辑。**

- **标记**列：三个 `since` 子表**各自独立**对照本次拉取前文件中该小节表格已出现的 `owner/repo`；新出现的行标 **新增**。下次拉取会先清空上一轮「新增」再重算（只保留相对**上一版文件**的新仓库）。

### 今日 trending（since=daily）

**页面**： `https://github.com/trending?since=daily`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `calesthio/OpenMontage` | 19673 | 2225 | Python | 3,719 stars today | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 2 | `ZhuLinsen/daily_stock_analysis` | 48630 | 43014 | Python | 1,468 stars today | LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。 LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs. | https://github.com/ZhuLinsen/daily_stock_analysis |  |
| 3 | `apple/container` | 42314 | 1244 | Swift | 1,838 stars today | 用于在Mac上使用轻量级虚拟机创建和运行Linux容器的工具。它是用Swift编写的，并针对Apple芯片进行了优化。 | https://github.com/apple/container | 新增 |
| 4 | `interviewstreet/hiring-agent` | 2257 | 601 | Python | 203 stars today | 用于评估和评分简历的AI代理。 | https://github.com/interviewstreet/hiring-agent | 新增 |
| 5 | `JCodesMore/ai-website-cloner-template` | 19401 | 2892 | TypeScript | 692 stars today | 使用AI编码代理，只需一个命令即可克隆任何网站 | https://github.com/JCodesMore/ai-website-cloner-template |  |
| 6 | `revfactory/harness` | 7771 | 1058 | HTML | 277 stars today | 一种元技能，用于设计特定领域的座席团队，定义专业座席，并生成他们使用的技能。 | https://github.com/revfactory/harness |  |
| 7 | `flutter/flutter` | 177369 | 30545 | Dart | 73 stars today | Flutter可以轻松快速地为移动设备及其他设备构建漂亮的应用程序 | https://github.com/flutter/flutter | 新增 |
| 8 | `andreknieriem/headunit-revived` | 1436 | 112 | Kotlin | 41 stars today | 用于显示Android Auto的Headunit应用程序 | https://github.com/andreknieriem/headunit-revived | 新增 |
| 9 | `stablyai/orca` | 6856 | 495 | TypeScript | 331 stars today | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca | 新增 |
| 10 | `google-labs-code/design.md` | 17427 | 1569 | TypeScript | 619 stars today | 用于向编码代理描述视觉标识的格式规范。DESIGN.md为代理提供了对设计系统的持久、结构化的理解。 | https://github.com/google-labs-code/design.md | 新增 |
| 11 | `Flowseal/zapret-discord-youtube` | 30031 | 2342 | Batchfile | 61 stars today | — | https://github.com/Flowseal/zapret-discord-youtube | 新增 |
| 12 | `kunchenguid/no-mistakes` | 2219 | 149 | Go | 110 stars today | git push no-mistakes | https://github.com/kunchenguid/no-mistakes | 新增 |
| 13 | `NousResearch/hermes-agent` | 202138 | 36123 | Python | 1,178 stars today | 与您一起成长的客服代表 | https://github.com/NousResearch/hermes-agent |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `calesthio/OpenMontage` | 19674 | 2225 | Python | 12,948 stars this week | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 2 | `DeusData/codebase-memory-mcp` | 14169 | 1045 | C | 9,589 stars this week | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 3 | `google-research/timesfm` | 25460 | 2422 | Python | 3,915 stars this week | TimesFM （时间序列基础模型）是由Google Research开发的用于时间序列预测的预训练时间序列基础模型。 | https://github.com/google-research/timesfm |  |
| 4 | `n0-computer/iroh` | 10701 | 489 | Rust | 1,196 stars this week | IP地址中断，改为拨号键。Rust中的模块化网络堆栈。 | https://github.com/n0-computer/iroh |  |
| 5 | `koala73/worldmonitor` | 59603 | 9321 | TypeScript | 2,899 stars this week | 实时全球智能仪表板。在统一的态势感知界面中进行人工智能驱动的新闻聚合、地缘政治监控和基础设施跟踪 | https://github.com/koala73/worldmonitor |  |
| 6 | `asgeirtj/system_prompts_leaks` | 45770 | 7516 | JavaScript | 2,662 stars this week | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT 5.5 Thinking ， GPT 5.5 Instant ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 7 | `Panniantong/Agent-Reach` | 39861 | 3162 | Python | 6,752 stars this week | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 8 | `penpot/penpot` | 53519 | 3445 | Clojure | 3,593 stars this week | Penpot ：用于设计和代码协作的开源设计工具 | https://github.com/penpot/penpot |  |
| 9 | `withastro/flue` | 6625 | 371 | TypeScript | 1,415 stars this week | 沙盒代理框架。 | https://github.com/withastro/flue |  |
| 10 | `jamiepine/voicebox` | 33888 | 4079 | TypeScript | 3,583 stars this week | 开源AI语音工作室。克隆、命令、创建。 | https://github.com/jamiepine/voicebox |  |
| 11 | `iptv-org/iptv` | 128321 | 7066 | TypeScript | 3,543 stars this week | 收集来自世界各地的公开IPTV频道 | https://github.com/iptv-org/iptv |  |
| 12 | `OpenCut-app/OpenCut` | 59565 | 6472 | TypeScript | 3,550 stars this week | 开源CapCut替代方案 | https://github.com/OpenCut-app/OpenCut |  |
| 13 | `stablyai/orca` | 6856 | 495 | TypeScript | 1,397 stars this week | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 14 | `makeplane/plane` | 52897 | 4716 | TypeScript | 1,871 stars this week | 🔥🔥🔥 开源JIRA、Linear、Monday和ClickUp替代方案。Plane是一个现代化的项目管理平台，用于管理任务、冲刺、文档和分类。 | https://github.com/makeplane/plane |  |
| 15 | `Kong/insomnia` | 39674 | 2347 | TypeScript | 1,167 stars this week | GraphQL、REST、WebSockets、SSE和gRPC的开源、跨平台API客户端。使用云、本地和Git存储。 | https://github.com/Kong/insomnia |  |
| 16 | `Stirling-Tools/Stirling-PDF` | 84081 | 7318 | Java | 2,793 stars this week | GitHub上排名第一的PDF应用程序，可让您在任何地方的任何设备上编辑PDF | https://github.com/Stirling-Tools/Stirling-PDF |  |
| 17 | `ZhuLinsen/daily_stock_analysis` | 48630 | 43014 | Python | 5,185 stars this week | LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。 LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs. | https://github.com/ZhuLinsen/daily_stock_analysis | 新增 |
| 18 | `NVIDIA/SkillSpector` | 10382 | 828 | Python | 2,980 stars this week | 人工智能代理技能的安全扫描仪。检测漏洞、恶意模式和安全风险。 | https://github.com/NVIDIA/SkillSpector |  |
| 19 | `microsoft/presidio` | 9603 | 1161 | Python | 888 stars this week | 一个开源框架，用于检测、编辑、屏蔽和匿名处理文本、图像和结构化数据中的敏感数据(PII)。支持NLP、模式匹配和可定制管道。 | https://github.com/microsoft/presidio | 新增 |
| 20 | `mukul975/Anthropic-Cybersecurity-Skills` | 20613 | 2393 | Python | 4,304 stars this week | 人工智能代理的817种结构化网络安全技能·映射到6个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF和MITRE F3 （打击欺诈） · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20 + p…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `harry0703/MoneyPrinterTurbo` | 92268 | 13316 | Python | 35,076 stars this month | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. | https://github.com/harry0703/MoneyPrinterTurbo | 新增 |
| 2 | `apple/container` | 42316 | 1244 | Swift | 15,056 stars this month | 用于在Mac上使用轻量级虚拟机创建和运行Linux容器的工具。它是用Swift编写的，并针对Apple芯片进行了优化。 | https://github.com/apple/container | 新增 |
| 3 | `DeusData/codebase-memory-mcp` | 14169 | 1045 | C | 11,171 stars this month | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp | 新增 |
| 4 | `mvanhorn/last30days-skill` | 46434 | 3849 | Python | 20,137 stars this month | 人工智能代理技能，研究Reddit、X、YouTube、HN、Polymarket和网络上的任何主题，然后合成基础摘要 | https://github.com/mvanhorn/last30days-skill | 新增 |
| 5 | `microsoft/markitdown` | 158788 | 11099 | Python | 34,276 stars this month | 用于将文件和Office文档转换为Markdown的Python工具。 | https://github.com/microsoft/markitdown | 新增 |
| 6 | `iptv-org/iptv` | 128321 | 7066 | TypeScript | 12,109 stars this month | 收集来自世界各地的公开IPTV频道 | https://github.com/iptv-org/iptv | 新增 |
| 7 | `Panniantong/Agent-Reach` | 39862 | 3162 | Python | 19,348 stars this month | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach | 新增 |
| 8 | `microsoft/Webwright` | 5608 | 355 | Python | 5,553 stars this month | 一个简单的SWE风格的浏览器代理框架，可在长时间的Web任务上实现SOTA结果。 | https://github.com/microsoft/Webwright | 新增 |
| 9 | `esengine/DeepSeek-Reasonix` | 24432 | 1487 | Go | 18,341 stars this month | 为您的终端提供DeepSeek原生AI编码代理。围绕前缀缓存稳定性而设计—保持运行。 | https://github.com/esengine/DeepSeek-Reasonix | 新增 |
| 10 | `Egonex-AI/Understand-Anything` | 67517 | 5595 | TypeScript | 43,940 stars this month | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Egonex-AI/Understand-Anything | 新增 |
| 11 | `Leonxlnx/taste-skill` | 50366 | 3482 | JavaScript | 31,423 stars this month | 品味技能-让您的人工智能有良好的品味。阻止人工智能产生无聊的通用斜坡 | https://github.com/Leonxlnx/taste-skill | 新增 |
| 12 | `calesthio/OpenMontage` | 19675 | 2225 | Python | 13,960 stars this month | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage | 新增 |
| 13 | `colbymchenry/codegraph` | 54221 | 3322 | TypeScript | 33,428 stars this month | 预索引的代码知识图，在代码更改时自动同步，适用于Claude Code、Codex、Gemini、Cursor、OpenCode、AntiGravity、Kiro和Hermes Agent —代币更少，工具调用更少， 100%本地 | https://github.com/colbymchenry/codegraph | 新增 |
| 14 | `lfnovo/open-notebook` | 33152 | 3738 | TypeScript | 9,484 stars this month | 笔记本LM的开源实现，具有更大的灵活性和功能 | https://github.com/lfnovo/open-notebook | 新增 |
| 15 | `phuryn/pm-skills` | 20912 | 2125 | — | 9,390 stars this month | PM Skills Marketplace ： 100多种代理技能、命令和插件—从发现到战略、执行、发布和增长。 | https://github.com/phuryn/pm-skills | 新增 |
| 16 | `hardikpandya/stop-slop` | 12220 | 849 | — | 8,335 stars this month | 从散文中删除AI TELLS的技能文件 | https://github.com/hardikpandya/stop-slop | 新增 |
| 17 | `tashfeenahmed/freellmapi` | 12126 | 1871 | TypeScript | 7,377 stars this month | OpenAI兼容代理，将16个LLM提供商的免费层（约17亿个代币/月）堆叠在一个/v1端点后面—加上任何自定义OpenAI兼容端点。智能路由、自动故障转移、加密密钥。仅限个人实验。 | https://github.com/tashfeenahmed/freellmapi | 新增 |
| 18 | `can1357/oh-my-pi` | 14512 | 1269 | TypeScript | 7,664 stars this month | 终端的AI编码代理—哈希锚定编辑、优化工具线束、LSP、Python、浏览器、子代理等 | https://github.com/can1357/oh-my-pi | 新增 |
| 19 | `mukul975/Anthropic-Cybersecurity-Skills` | 20614 | 2393 | Python | 12,570 stars this month | 人工智能代理的817种结构化网络安全技能·映射到6个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF和MITRE F3 （打击欺诈） · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20 + p…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills | 新增 |
| 20 | `openai/plugins` | 3501 | 412 | JavaScript | 2,262 stars this month | OpenAI插件 | https://github.com/openai/plugins | 新增 |
| 21 | `ogulcancelik/herdr` | 7156 | 436 | Rust | 4,800 stars this month | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr | 新增 |
| 22 | `run-llama/liteparse` | 10971 | 718 | Rust | 5,736 stars this month | 快速、实用、开源的文档解析器 | https://github.com/run-llama/liteparse | 新增 |
| 23 | `supermemoryai/supermemory` | 27443 | 2381 | TypeScript | 4,815 stars this month | 内存和上下文引擎+应用程序，速度极快，可扩展，可以在本地完全运行。人工智能时代的内存API。 | https://github.com/supermemoryai/supermemory | 新增 |


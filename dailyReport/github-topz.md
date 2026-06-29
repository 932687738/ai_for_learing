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

**最近一次更新时间**（Asia/Shanghai）： 2026-06-29 08:58:31

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 520594 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 479645 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 450691 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 444780 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 390916 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 380874 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 358549 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 355308 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 354425 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 305310 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
| 11 | `awesome-selfhosted/awesome-selfhosted` | 301670 | 可自行部署的各类自由软件网络服务与 Web 应用清单。 | https://github.com/awesome-selfhosted/awesome-selfhosted |  |
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
| 1 | `simplex-chat/simplex-chat` | 15008 | 865 | Haskell | 1,180 stars today | SimpleX -第一个没有任何类型用户标识符的消息传递网络-设计为100 ％私有！ iOS ， Android和桌面应用程序📱！ | https://github.com/simplex-chat/simplex-chat |  |
| 2 | `ripienaar/free-for-dev` | 125231 | 13167 | HTML | 495 stars today | 具有devops和infradev感兴趣的免费层的SaaS、PaaS和IaaS产品列表 | https://github.com/ripienaar/free-for-dev |  |
| 3 | `commaai/openpilot` | 62386 | 11095 | Python | 266 stars today | openpilot是一个机器人操作系统。目前，它升级了300多辆支持车辆的驾驶员辅助系统。 | https://github.com/commaai/openpilot |  |
| 4 | `xbtlin/ai-berkshire` | 5298 | 720 | Python | 1,445 stars today | AI 时代的伯克希尔：基于 Claude Code / Codex 的价值投资研究框架。巴菲特·芒格·段永平·李录四大师方法论 + 多Agent并行研究。· AI-era Berkshire: a value investing research framework built for Claude Code / Codex. 4 masters' methodologies + multi-agent adversarial analysis. | https://github.com/xbtlin/ai-berkshire |  |
| 5 | `Robbyant/lingbot-map` | 8227 | 803 | Python | 372 stars today | 用于从流数据重建场景的前馈3D基础模型 | https://github.com/Robbyant/lingbot-map |  |
| 6 | `DeusData/codebase-memory-mcp` | 19656 | 1424 | C | 2,190 stars today | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 7 | `cupy/cupy` | 11517 | 1069 | Python | 174 stars today | 适用于GPU的NumPy和SciPy | https://github.com/cupy/cupy |  |
| 8 | `altic-dev/FluidVoice` | 3730 | 238 | Swift | 365 stars today | FluidVoice -最快的macOS离线听写应用程序-语音到文本完全本地。一个⭐带我们走很长的路:)) | https://github.com/altic-dev/FluidVoice |  |
| 9 | `opendatalab/MinerU` | 71592 | 6014 | Python | 380 stars today | 将复杂的文档（如PDF和Office文档）转换为适用于Agent工作流程的LLM就绪markdown/JSON。 | https://github.com/opendatalab/MinerU |  |
| 10 | `HKUDS/Vibe-Trading` | 14314 | 2631 | Python | 492 stars today | “Vibe-Trading ：您的个人交易代理” | https://github.com/HKUDS/Vibe-Trading |  |
| 11 | `ByteByteGoHq/system-design-101` | 84455 | 9350 | — | 250 stars today | 使用视觉效果和简单术语解释复杂系统。帮助您准备系统设计面试。 | https://github.com/ByteByteGoHq/system-design-101 |  |
| 12 | `usestrix/strix` | 26733 | 2984 | Python | 122 stars today | 开源人工智能黑客可查找并修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 13 | `browser-use/video-use` | 11048 | 1524 | Python | 196 stars today | 使用编码代理编辑视频 | https://github.com/browser-use/video-use |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `calesthio/OpenMontage` | 26952 | 2987 | Python | 18,703 stars this week | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 2 | `DeusData/codebase-memory-mcp` | 19657 | 1425 | C | 8,926 stars this week | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 3 | `kunchenguid/no-mistakes` | 4064 | 227 | Go | 2,449 stars this week | git push no-mistakes | https://github.com/kunchenguid/no-mistakes |  |
| 4 | `palmier-io/palmier-pro` | 9303 | 657 | Swift | 5,034 stars this week | 专为人工智能打造的macOS视频编辑器 | https://github.com/palmier-io/palmier-pro |  |
| 5 | `google-labs-code/design.md` | 22836 | 1816 | TypeScript | 6,728 stars this week | 用于向编码代理描述视觉标识的格式规范。DESIGN.md为代理提供了对设计系统的持久、结构化的理解。 | https://github.com/google-labs-code/design.md |  |
| 6 | `JCodesMore/ai-website-cloner-template` | 22819 | 3259 | TypeScript | 5,317 stars this week | 使用AI编码代理，只需一个命令即可克隆任何网站 | https://github.com/JCodesMore/ai-website-cloner-template |  |
| 7 | `simplex-chat/simplex-chat` | 15009 | 865 | Haskell | 3,218 stars this week | SimpleX -第一个没有任何类型用户标识符的消息传递网络-设计为100 ％私有！ iOS ， Android和桌面应用程序📱！ | https://github.com/simplex-chat/simplex-chat |  |
| 8 | `interviewstreet/hiring-agent` | 3172 | 702 | Python | 1,973 stars this week | 用于评估和评分简历的AI代理。 | https://github.com/interviewstreet/hiring-agent |  |
| 9 | `ZhuLinsen/daily_stock_analysis` | 51122 | 44433 | Python | 7,045 stars this week | LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。 LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs. | https://github.com/ZhuLinsen/daily_stock_analysis |  |
| 10 | `stablyai/orca` | 8616 | 601 | TypeScript | 2,769 stars this week | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 11 | `Panniantong/Agent-Reach` | 44474 | 3538 | Python | 7,692 stars this week | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 12 | `mukul975/Anthropic-Cybersecurity-Skills` | 22660 | 2583 | Python | 5,212 stars this week | 817 structured cybersecurity skills for AI agents · Mapped to 6 frameworks: MITRE ATT&amp;CK, NIST CSF 2.0, MITRE ATLAS, D3FEND, NIST AI RMF &amp; MITRE F3 (Fight Fraud) · agentskills.io standard · Works with Claude Code, GitHub Copilot, Codex CLI, Cursor, Gemini CLI &amp; 20+ p… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills |  |
| 13 | `penpot/penpot` | 54397 | 3532 | Clojure | 2,429 stars this week | Penpot: The open-source design tool for design and code collaboration | https://github.com/penpot/penpot |  |
| 14 | `BuilderIO/agent-native` | 2888 | 287 | TypeScript | 1,540 stars this week | A framework for building agent-native applications. | https://github.com/BuilderIO/agent-native |  |
| 15 | `jamiepine/voicebox` | 35438 | 4256 | TypeScript | 3,883 stars this week | The open-source AI voice studio. Clone, dictate, create. | https://github.com/jamiepine/voicebox |  |
| 16 | `aws/agent-toolkit-for-aws` | 1542 | 131 | Python | 600 stars this week | Official, AWS-supported MCP servers, skills, and plugins to help AI agents build on AWS | https://github.com/aws/agent-toolkit-for-aws |  |
| 17 | `alibaba/page-agent` | 20473 | 1763 | TypeScript | 1,778 stars this week | JavaScript in-page GUI agent. Control web interfaces with natural language. | https://github.com/alibaba/page-agent |  |
| 18 | `Stirling-Tools/Stirling-PDF` | 84953 | 7379 | Java | 3,079 stars this week | #1 PDF Application on GitHub that lets you edit PDFs on any device anywhere | https://github.com/Stirling-Tools/Stirling-PDF |  |
| 19 | `koala73/worldmonitor` | 60703 | 9463 | TypeScript | 2,845 stars this week | Real-time global intelligence dashboard. AI-powered news aggregation, geopolitical monitoring, and infrastructure tracking in a unified situational awareness interface | https://github.com/koala73/worldmonitor |  |
| 20 | `NanmiCoder/MediaCrawler` | 54024 | 11037 | Python | 2,472 stars this week | 小红书笔记 · 评论爬虫、抖音视频 · 评论爬虫、快手视频 · 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖子 ｜ 百度贴吧评论回复爬虫 · 知乎问答文章｜评论爬虫 | https://github.com/NanmiCoder/MediaCrawler |  |
| 21 | `topoteretes/cognee` | 24898 | 2309 | Python | 6,064 stars this week | Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory across sessions with a self-hosted knowledge graph engine. | https://github.com/topoteretes/cognee |  |
| 22 | `bytedance/deer-flow` | 75244 | 10156 | Python | 2,976 stars this week | An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours. | https://github.com/bytedance/deer-flow |  |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `apple/container` | 44313 | 1314 | Swift | 17,676 stars this month | A tool for creating and running Linux containers using lightweight virtual machines on a Mac. It is written in Swift, and optimized for Apple silicon. | https://github.com/apple/container |  |
| 2 | `DeusData/codebase-memory-mcp` | 19657 | 1425 | C | 16,051 stars this month | High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies. | https://github.com/DeusData/codebase-memory-mcp |  |
| 3 | `calesthio/OpenMontage` | 26952 | 2988 | Python | 22,408 stars this month | World's first open-source, agentic video production system. 12 pipelines, 52 tools, 500+ agent skills. Turn your AI coding assistant into a full video production studio. | https://github.com/calesthio/OpenMontage |  |
| 4 | `Panniantong/Agent-Reach` | 44474 | 3538 | Python | 23,835 stars this month | Give your AI agent eyes to see the entire internet. Read &amp; search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees. | https://github.com/Panniantong/Agent-Reach |  |
| 5 | `mvanhorn/last30days-skill` | 47432 | 3937 | Python | 20,899 stars this month | AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary | https://github.com/mvanhorn/last30days-skill |  |
| 6 | `iptv-org/iptv` | 129073 | 7128 | TypeScript | 12,819 stars this month | Collection of publicly available IPTV channels from all over the world | https://github.com/iptv-org/iptv |  |
| 7 | `harry0703/MoneyPrinterTurbo` | 93906 | 13617 | Python | 29,272 stars this month | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. | https://github.com/harry0703/MoneyPrinterTurbo |  |
| 8 | `lfnovo/open-notebook` | 33786 | 3786 | TypeScript | 10,048 stars this month | An Open Source implementation of Notebook LM with more flexibility and features | https://github.com/lfnovo/open-notebook |  |
| 9 | `phuryn/pm-skills` | 21530 | 2181 | — | 9,864 stars this month | PM Skills Marketplace: 100+ agentic skills, commands, and plugins — from discovery to strategy, execution, launch, and growth. | https://github.com/phuryn/pm-skills |  |
| 10 | `Leonxlnx/taste-skill` | 52576 | 3630 | JavaScript | 27,093 stars this month | Taste-Skill - gives your AI good taste. stops the AI from generating boring, generic slop | https://github.com/Leonxlnx/taste-skill |  |
| 11 | `microsoft/markitdown` | 160625 | 11288 | Python | 34,072 stars this month | Python tool for converting files and office documents to Markdown. | https://github.com/microsoft/markitdown |  |
| 12 | `openai/plugins` | 3713 | 433 | JavaScript | 2,436 stars this month | OpenAI Plugins | https://github.com/openai/plugins |  |
| 13 | `tashfeenahmed/freellmapi` | 13803 | 2055 | TypeScript | 7,784 stars this month | OpenAI-compatible proxy that stacks the free tiers of 16 LLM providers (~1.7B tokens/month) behind one /v1 endpoint — plus any custom OpenAI-compatible endpoint. Smart routing, automatic failover, encrypted keys. Personal experimentation only. | https://github.com/tashfeenahmed/freellmapi |  |
| 14 | `can1357/oh-my-pi` | 15008 | 1334 | TypeScript | 6,959 stars this month | ⌥ AI Coding agent for the terminal — hash-anchored edits, optimized tool harness, LSP, Python, browser, subagents, and more | https://github.com/can1357/oh-my-pi |  |
| 15 | `mukul975/Anthropic-Cybersecurity-Skills` | 22660 | 2583 | Python | 11,207 stars this month | 817 structured cybersecurity skills for AI agents · Mapped to 6 frameworks: MITRE ATT&amp;CK, NIST CSF 2.0, MITRE ATLAS, D3FEND, NIST AI RMF &amp; MITRE F3 (Fight Fraud) · agentskills.io standard · Works with Claude Code, GitHub Copilot, Codex CLI, Cursor, Gemini CLI &amp; 20+ p… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills |  |
| 16 | `ogulcancelik/herdr` | 7954 | 490 | Rust | 5,186 stars this month | agent multiplexer that lives in your terminal. | https://github.com/ogulcancelik/herdr |  |
| 17 | `asgeirtj/system_prompts_leaks` | 46870 | 7669 | JavaScript | 6,089 stars this month | Extracted system prompts from Anthropic - Claude Fable 5, Opus 4.8, Claude Code, Claude Design. OpenAI - ChatGPT 5.5 Thinking, GPT 5.5 Instant, Codex. Google - Gemini 3.5 Flash, 3.1 Pro, Antigravity. xAI - Grok, Cursor, Copilot, VS Code, Perplexity, and more. Updated regularly. | https://github.com/asgeirtj/system_prompts_leaks |  |
| 18 | `stablyai/orca` | 8616 | 601 | TypeScript | 4,966 stars this month | Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription. Available on desktop and mobile. | https://github.com/stablyai/orca |  |
| 19 | `supermemoryai/supermemory` | 27869 | 2404 | TypeScript | 5,193 stars this month | Memory and context engine + app that is extremely fast, scalable, and can be run fully locally. The Memory API for the AI era. | https://github.com/supermemoryai/supermemory |  |
| 20 | `simplex-chat/simplex-chat` | 15010 | 865 | Haskell | 3,395 stars this month | SimpleX - the first messaging network operating without user identifiers of any kind - 100% private by design! iOS, Android and desktop apps 📱! | https://github.com/simplex-chat/simplex-chat |  |
| 21 | `Open-LLM-VTuber/Open-LLM-VTuber` | 12028 | 1404 | Python | 4,172 stars this month | Talk to any LLM with hands-free voice interaction, voice interruption, and Live2D taking face running locally across platforms | https://github.com/Open-LLM-VTuber/Open-LLM-VTuber |  |


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

**最近一次更新时间**（Asia/Shanghai）： 2026-07-02 09:31:30

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 521514 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 480616 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 450768 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 445801 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 391097 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 381341 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 358852 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 355733 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 354776 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 305855 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `msitarzewski/agency-agents` | 123492 | 20097 | Shell | 2,114 stars today | 一个完整的人工智能机构，触手可及--从前端向导到Reddit社区忍者，从奇思妙想的注入者到现实检查者。每位客服代表都是具有个性、流程和经过验证的交付成果的专家。 | https://github.com/msitarzewski/agency-agents |  |
| 2 | `usestrix/strix` | 29767 | 3225 | Python | 1,211 stars today | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 3 | `HKUDS/Vibe-Trading` | 16567 | 2810 | Python | 694 stars today | “Vibe-Trading ：您的个人交易代理” | https://github.com/HKUDS/Vibe-Trading |  |
| 4 | `hasaneyldrm/exercises-dataset` | 8444 | 953 | HTML | 2,470 stars today | 包含433项健身练习的综合数据集。每个条目包括名称、类别、目标肌肉群、设备、说明、缩略图和动画视频。 | https://github.com/hasaneyldrm/exercises-dataset |  |
| 5 | `facebook/astryx` | 2666 | 137 | TypeScript | 708 stars today | 完全可定制和代理就绪的开源设计系统 | https://github.com/facebook/astryx |  |
| 6 | `diegosouzapw/OmniRoute` | 9555 | 1469 | TypeScript | 1,010 stars today | 永不停止编码。免费AI网关：一个端点， 231多家提供商（ 50多家免费） ，将Claude Code、Codex、Cursor、Cline和Copilot连接到免费的Claude/GPT/Gemini。RTK + Caveman堆叠压缩可节省15-95%的代币、智能自动回退、MCP/A2A、多模式API、桌面/PWA。 | https://github.com/diegosouzapw/OmniRoute |  |
| 7 | `allenai/olmocr` | 18280 | 1505 | Python | 334 stars today | 用于线性化LLM数据集/培训的PDF的工具包 | https://github.com/allenai/olmocr |  |
| 8 | `logto-io/logto` | 13277 | 906 | TypeScript | 113 stars today | SaaS和AI应用程序🧑‍🚀的身份验证和授权基础设施，基于OIDC和OAuth 2.1 ，具有多租户、SSO和RBAC。 | https://github.com/logto-io/logto |  |
| 9 | `togatoga/karukan` | 583 | 35 | Rust | 42 stars today | Linux、macOS、神经假名-汉字转换引擎的日语输入法系统 | https://github.com/togatoga/karukan |  |
| 10 | `Mebus/cupp` | 6250 | 2065 | Python | 184 stars today | 通用用户密码分析器（ CUPP ） | https://github.com/Mebus/cupp |  |
| 11 | `Unclecheng-li/VulnClaw` | 1582 | 218 | Python | 132 stars today | 基于 AI Agent + MCP 工具链 + 渗透 Skill 编排， 配合大语言模型， 自然语言输入 → 自动完成「信息收集 → 漏洞发现 → 漏洞利用 → 报告生成」全流程。 | https://github.com/Unclecheng-li/VulnClaw |  |
| 12 | `microsoft/AI-For-Beginners` | 50471 | 10256 | Jupyter Notebook | 1,096 stars today | 12周， 24课，全民人工智能！ | https://github.com/microsoft/AI-For-Beginners |  |
| 13 | `refactoringhq/tolaria` | 18025 | 1223 | TypeScript | 150 stars today | 用于管理降价知识库的桌面应用程序 | https://github.com/refactoringhq/tolaria |  |
| 14 | `ogulcancelik/herdr` | 9618 | 566 | Rust | 609 stars today | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 15 | `0xNyk/council-of-high-intelligence` | 2641 | 245 | Shell | 161 stars today | 18个人工智能角色在多个法学硕士提供商中精心策划您最艰难的决策。亚里士多德（ Aristotle ）、费曼（ Feynman ）、卡尼曼（ Kahneman ）、托瓦兹（ Torvalds ）等--具有真正模型多样性的结构化多轮一个命令：/council | https://github.com/0xNyk/council-of-high-intelligence |  |
| 16 | `altic-dev/FluidVoice` | 5503 | 332 | Swift | 572 stars today | 具有设备上STT和定制训练AI增强模型的最快且唯一的macOS听写应用程序- Local Wispr Flow替代方案。一个⭐需要我们走很长的路:)) Windows、iOS和Linux即将推出。 | https://github.com/altic-dev/FluidVoice |  |
| 17 | `CoreBunch/Instatic` | 2018 | 167 | TypeScript | 508 stars today | Instatic是一款现代化的自托管可视化CMS ，只需1分钟即可运行 | https://github.com/CoreBunch/Instatic |  |
| 18 | `TencentCloud/CubeSandbox` | 6806 | 569 | Rust | 79 stars today | 适用于人工智能代理的即时、并发、安全和轻量级沙盒。 | https://github.com/TencentCloud/CubeSandbox |  |
| 19 | `browser-use/video-use` | 13236 | 1658 | Python | 693 stars today | 使用编码代理编辑视频 | https://github.com/browser-use/video-use |  |
| 20 | `yikart/AiToEarn` | 22561 | 3405 | TypeScript | 116 stars today | 让我们使用人工智能来赚取收入！ | https://github.com/yikart/AiToEarn |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `xbtlin/ai-berkshire` | 8136 | 1032 | Python | 6,758 stars this week | AI 时代的伯克希尔：基于 Claude Code / Codex 的价值投资研究框架。巴菲特·芒格·段永平·李录四大师方法论 + 多Agent并行研究。· AI-era Berkshire: a value investing research framework built for Claude Code / Codex. 4 masters' methodologies + multi-agent adversarial analysis. | https://github.com/xbtlin/ai-berkshire |  |
| 2 | `simplex-chat/simplex-chat` | 17555 | 1023 | Haskell | 6,289 stars this week | SimpleX -第一个没有任何类型用户标识符的消息传递网络-设计为100 ％私有！ iOS ， Android和桌面应用程序📱！ | https://github.com/simplex-chat/simplex-chat |  |
| 3 | `calesthio/OpenMontage` | 30910 | 3507 | Python | 12,624 stars this week | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 4 | `google-labs-code/design.md` | 24043 | 1883 | TypeScript | 7,186 stars this week | 用于向编码代理描述视觉标识的格式规范。DESIGN.md为代理提供了对设计系统的持久、结构化的理解。 | https://github.com/google-labs-code/design.md |  |
| 5 | `DeusData/codebase-memory-mcp` | 23835 | 1752 | C | 9,697 stars this week | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 6 | `kunchenguid/no-mistakes` | 4745 | 271 | Go | 2,887 stars this week | git push no-mistakes | https://github.com/kunchenguid/no-mistakes |  |
| 7 | `JCodesMore/ai-website-cloner-template` | 24447 | 3461 | TypeScript | 5,359 stars this week | 使用AI编码代理，只需一个命令即可克隆任何网站 | https://github.com/JCodesMore/ai-website-cloner-template |  |
| 8 | `Robbyant/lingbot-map` | 9231 | 892 | Python | 1,823 stars this week | 用于从流数据重建场景的前馈3D基础模型 | https://github.com/Robbyant/lingbot-map |  |
| 9 | `ripienaar/free-for-dev` | 127620 | 13332 | HTML | 4,268 stars this week | 具有devops和infradev感兴趣的免费层的SaaS、PaaS和IaaS产品列表 | https://github.com/ripienaar/free-for-dev |  |
| 10 | `stablyai/orca` | 10307 | 692 | TypeScript | 3,537 stars this week | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 11 | `topoteretes/cognee` | 26396 | 2443 | Python | 5,171 stars this week | Cognee是面向智能体的开源AI内存平台。使用自托管知识图表引擎，为您的人工智能代理提供跨会话的持久长期记忆。 | https://github.com/topoteretes/cognee |  |
| 12 | `Panniantong/Agent-Reach` | 48369 | 3848 | Python | 8,791 stars this week | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 13 | `interviewstreet/hiring-agent` | 4165 | 822 | Python | 2,185 stars this week | 用于评估和评分简历的AI代理。 | https://github.com/interviewstreet/hiring-agent |  |
| 14 | `alibaba/page-agent` | 20937 | 1786 | TypeScript | 1,450 stars this week | JavaScript页面内GUI代理。使用自然语言控制Web界面。 | https://github.com/alibaba/page-agent |  |
| 15 | `NanmiCoder/MediaCrawler` | 54821 | 11131 | Python | 2,575 stars this week | 小红书笔记 · 评论爬虫、抖音视频 · 评论爬虫、快手视频 · 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖子 ｜ 百度贴吧评论回复爬虫 · 知乎问答文章｜评论爬虫 | https://github.com/NanmiCoder/MediaCrawler |  |
| 16 | `ZhuLinsen/daily_stock_analysis` | 53086 | 46008 | Python | 4,994 stars this week | LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。 LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs. | https://github.com/ZhuLinsen/daily_stock_analysis |  |
| 17 | `jamiepine/voicebox` | 36733 | 4420 | TypeScript | 2,960 stars this week | 开源AI语音工作室。克隆、命令、创建。 | https://github.com/jamiepine/voicebox |  |
| 18 | `mukul975/Anthropic-Cybersecurity-Skills` | 23790 | 2700 | Python | 3,367 stars this week | 人工智能代理的817种结构化网络安全技能·映射到6个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF和MITRE F3 （打击欺诈） · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20 + p…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills |  |
| 19 | `aws/agent-toolkit-for-aws` | 1683 | 138 | Python | 693 stars this week | AWS支持的官方MCP服务器、技能和插件，以帮助AI代理在AWS上构建 | https://github.com/aws/agent-toolkit-for-aws |  |
| 20 | `BuilderIO/agent-native` | 3310 | 317 | TypeScript | 1,277 stars this week | 用于构建代理本机应用程序的框架。 | https://github.com/BuilderIO/agent-native |  |
| 21 | `usestrix/strix` | 29769 | 3225 | Python | 2,804 stars this week | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `apple/container` | 45651 | 1356 | Swift | 19,052 stars this month | 用于在Mac上使用轻量级虚拟机创建和运行Linux容器的工具。它是用Swift编写的，并针对Apple芯片进行了优化。 | https://github.com/apple/container |  |
| 2 | `DeusData/codebase-memory-mcp` | 23835 | 1752 | C | 20,690 stars this month | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 3 | `calesthio/OpenMontage` | 30910 | 3507 | Python | 26,509 stars this month | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 4 | `Panniantong/Agent-Reach` | 48369 | 3848 | Python | 27,497 stars this month | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 5 | `mvanhorn/last30days-skill` | 48256 | 3991 | Python | 21,484 stars this month | 人工智能代理技能，研究Reddit、X、YouTube、HN、Polymarket和网络上的任何主题，然后合成基础摘要 | https://github.com/mvanhorn/last30days-skill |  |
| 6 | `iptv-org/iptv` | 129833 | 7195 | TypeScript | 13,422 stars this month | 收集来自世界各地的公开IPTV频道 | https://github.com/iptv-org/iptv |  |
| 7 | `phuryn/pm-skills` | 22052 | 2222 | — | 10,309 stars this month | PM Skills Marketplace ： 100多种代理技能、命令和插件—从发现到战略、执行、发布和增长。 | https://github.com/phuryn/pm-skills |  |
| 8 | `lfnovo/open-notebook` | 34358 | 3830 | TypeScript | 10,482 stars this month | 笔记本LM的开源实现，具有更大的灵活性和功能 | https://github.com/lfnovo/open-notebook |  |
| 9 | `asgeirtj/system_prompts_leaks` | 47671 | 7778 | JavaScript | 6,665 stars this month | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT 5.5 Thinking ， GPT 5.5 Instant ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 10 | `openai/plugins` | 3888 | 455 | JavaScript | 2,564 stars this month | OpenAI插件 | https://github.com/openai/plugins |  |
| 11 | `Leonxlnx/taste-skill` | 54467 | 3741 | JavaScript | 23,990 stars this month | 品味技能-让您的人工智能有良好的品味。阻止人工智能产生无聊的通用斜坡 | https://github.com/Leonxlnx/taste-skill |  |
| 12 | `harry0703/MoneyPrinterTurbo` | 94964 | 13791 | Python | 19,037 stars this month | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. | https://github.com/harry0703/MoneyPrinterTurbo |  |
| 13 | `ogulcancelik/herdr` | 9618 | 566 | Rust | 5,827 stars this month | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 14 | `stablyai/orca` | 10307 | 692 | TypeScript | 6,221 stars this month | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 15 | `t8y2/dbx` | 8066 | 691 | Rust | 5,289 stars this month | 15MB, lightweight, cross-platform database client. Supports MySQL, PostgreSQL, SQLite, Redis, MongoDB, DuckDB, ClickHouse, SQL Server and more.15MB，轻量级跨平台数据库客户端、数据库管理工具。支持 MySQL、PostgreSQL、SQLite、Redis、MongoDB、DuckDB、ClickHouse、SQL Server 等。 | https://github.com/t8y2/dbx |  |
| 16 | `OpenCut-app/OpenCut` | 61125 | 6591 | TypeScript | 8,963 stars this month | 开源CapCut替代方案 | https://github.com/OpenCut-app/OpenCut |  |
| 17 | `mukul975/Anthropic-Cybersecurity-Skills` | 23790 | 2700 | Python | 10,648 stars this month | 人工智能代理的817种结构化网络安全技能·映射到6个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF和MITRE F3 （打击欺诈） · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20 + p…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills |  |
| 18 | `roboflow/supervision` | 46163 | 4094 | Python | 6,459 stars this month | 我们为您编写可重复使用的计算机视觉工具。 💜 | https://github.com/roboflow/supervision |  |
| 19 | `tashfeenahmed/freellmapi` | 14576 | 2139 | TypeScript | 7,637 stars this month | OpenAI兼容代理，将16个LLM提供商的免费层（约17亿个代币/月）堆叠在一个/v1端点后面—加上任何自定义OpenAI兼容端点。智能路由、自动故障转移、加密密钥。仅限个人实验。 | https://github.com/tashfeenahmed/freellmapi |  |
| 20 | `n0-computer/iroh` | 10969 | 507 | Rust | 2,314 stars this month | IP地址中断，改为拨号键。将QUIC + NAT遍历添加到您的应用程序的库。 | https://github.com/n0-computer/iroh |  |


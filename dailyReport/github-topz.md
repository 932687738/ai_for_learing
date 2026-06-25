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

**最近一次更新时间**（Asia/Shanghai）： 2026-06-26 07:42:06

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 519672 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 478804 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 450523 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 444242 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 390799 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 380456 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 358290 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 354866 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 353952 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 304821 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `google-labs-code/design.md` | 19109 | 1643 | TypeScript | 1,407 stars today | 用于向编码代理描述视觉标识的格式规范。DESIGN.md为代理提供了对设计系统的持久、结构化的理解。 | https://github.com/google-labs-code/design.md |  |
| 2 | `calesthio/OpenMontage` | 22007 | 2470 | Python | 3,553 stars today | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 3 | `xbtlin/ai-berkshire` | 1817 | 295 | Python | 201 stars today | AI 时代的伯克希尔：基于 Claude Code 的价值投资研究框架。巴菲特·芒格·段永平·李录四大师方法论 + 多Agent并行研究。· AI-era Berkshire: a value investing research framework built on Claude Code. 4 masters' methodologies + multi-agent adversarial analysis. | https://github.com/xbtlin/ai-berkshire | 新增 |
| 4 | `mauriceboe/TREK` | 6610 | 604 | TypeScript | 112 stars today | 自托管行程/行程规划工具，提供实时协作、互动地图、PWA支持、SSO、预算、装箱单等功能。 | https://github.com/mauriceboe/TREK | 新增 |
| 5 | `apple/container` | 43184 | 1266 | Swift | 1,366 stars today | 用于在Mac上使用轻量级虚拟机创建和运行Linux容器的工具。它是用Swift编写的，并针对Apple芯片进行了优化。 | https://github.com/apple/container |  |
| 6 | `JCodesMore/ai-website-cloner-template` | 20387 | 3005 | TypeScript | 1,021 stars today | 使用AI编码代理，只需一个命令即可克隆任何网站 | https://github.com/JCodesMore/ai-website-cloner-template |  |
| 7 | `every-app/open-seo` | 2492 | 295 | TypeScript | 57 stars today | Semrush和Ahrefs的开源替代品 | https://github.com/every-app/open-seo | 新增 |
| 8 | `garrytan/gstack` | 115769 | 17164 | TypeScript | 836 stars today | 使用Garry Tan确切的Claude Code设置： 23个自以为是的工具，分别担任首席执行官、设计师、工程经理、发布经理、文档工程师和QA | https://github.com/garrytan/gstack | 新增 |
| 9 | `aws/agent-toolkit-for-aws` | 1120 | 114 | Python | 15 stars today | AWS支持的官方MCP服务器、技能和插件，以帮助AI代理在AWS上构建 | https://github.com/aws/agent-toolkit-for-aws | 新增 |
| 10 | `mukul975/Anthropic-Cybersecurity-Skills` | 21198 | 2445 | Python | 600 stars today | 人工智能代理的817种结构化网络安全技能·映射到6个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF和MITRE F3 （打击欺诈） · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20 + p…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills | 新增 |
| 11 | `alibaba/page-agent` | 19787 | 1705 | TypeScript | 196 stars today | JavaScript页面内GUI代理。使用自然语言控制Web界面。 | https://github.com/alibaba/page-agent | 新增 |
| 12 | `IceWhaleTech/CasaOS` | 34792 | 1991 | Go | 202 stars today | CasaOS -一个简单、易用、优雅的开源个人云系统。 | https://github.com/IceWhaleTech/CasaOS | 新增 |
| 13 | `opendatalab/MinerU` | 69529 | 5881 | Python | 524 stars today | 将复杂的文档（如PDF和Office文档）转换为适用于Agent工作流程的LLM就绪markdown/JSON。 | https://github.com/opendatalab/MinerU | 新增 |
| 14 | `Free-TV/IPTV` | 18191 | 2677 | Python | 141 stars today | 免费电视频道的M3U播放列表 | https://github.com/Free-TV/IPTV | 新增 |
| 15 | `shanraisshan/claude-code-best-practice` | 60500 | 6060 | HTML | 450 stars today | 从氛围编码到代理工程-实践使克劳德完美 | https://github.com/shanraisshan/claude-code-best-practice | 新增 |
| 16 | `NanmiCoder/MediaCrawler` | 52731 | 10920 | Python | 347 stars today | 小红书笔记 · 评论爬虫、抖音视频 · 评论爬虫、快手视频 · 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖子 ｜ 百度贴吧评论回复爬虫 · 知乎问答文章｜评论爬虫 | https://github.com/NanmiCoder/MediaCrawler | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `calesthio/OpenMontage` | 22007 | 2470 | Python | 12,948 stars this week | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 2 | `DeusData/codebase-memory-mcp` | 14746 | 1086 | C | 9,589 stars this week | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 3 | `google-research/timesfm` | 25564 | 2429 | Python | 3,915 stars this week | TimesFM （时间序列基础模型）是由Google Research开发的用于时间序列预测的预训练时间序列基础模型。 | https://github.com/google-research/timesfm |  |
| 4 | `koala73/worldmonitor` | 59805 | 9343 | TypeScript | 2,899 stars this week | 实时全球智能仪表板。在统一的态势感知界面中进行人工智能驱动的新闻聚合、地缘政治监控和基础设施跟踪 | https://github.com/koala73/worldmonitor |  |
| 5 | `penpot/penpot` | 53679 | 3459 | Clojure | 3,593 stars this week | Penpot ：用于设计和代码协作的开源设计工具 | https://github.com/penpot/penpot |  |
| 6 | `jamiepine/voicebox` | 34194 | 4114 | TypeScript | 3,583 stars this week | 开源AI语音工作室。克隆、命令、创建。 | https://github.com/jamiepine/voicebox |  |
| 7 | `asgeirtj/system_prompts_leaks` | 46046 | 7547 | JavaScript | 2,662 stars this week | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT 5.5 Thinking ， GPT 5.5 Instant ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 8 | `Panniantong/Agent-Reach` | 41167 | 3255 | Python | 6,752 stars this week | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 9 | `ZhuLinsen/daily_stock_analysis` | 49479 | 43443 | Python | 5,185 stars this week | LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。 LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs. | https://github.com/ZhuLinsen/daily_stock_analysis |  |
| 10 | `OpenCut-app/OpenCut` | 59780 | 6492 | TypeScript | 3,550 stars this week | 开源CapCut替代方案 | https://github.com/OpenCut-app/OpenCut |  |
| 11 | `withastro/flue` | 6700 | 372 | TypeScript | 1,415 stars this week | 沙盒代理框架。 | https://github.com/withastro/flue |  |
| 12 | `mukul975/Anthropic-Cybersecurity-Skills` | 21198 | 2445 | Python | 4,304 stars this week | 人工智能代理的817种结构化网络安全技能·映射到6个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF和MITRE F3 （打击欺诈） · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20 + p…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills |  |
| 13 | `Stirling-Tools/Stirling-PDF` | 84362 | 7349 | Java | 2,793 stars this week | GitHub上排名第一的PDF应用程序，可让您在任何地方的任何设备上编辑PDF | https://github.com/Stirling-Tools/Stirling-PDF |  |
| 14 | `interviewstreet/hiring-agent` | 2733 | 654 | Python | 902 stars this week | 用于评估和评分简历的AI代理。 | https://github.com/interviewstreet/hiring-agent | 新增 |
| 15 | `stablyai/orca` | 7406 | 530 | TypeScript | 1,397 stars this week | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 16 | `n0-computer/iroh` | 10765 | 492 | Rust | 1,196 stars this week | IP地址中断，改为拨号键。Rust中的模块化网络堆栈。 | https://github.com/n0-computer/iroh |  |
| 17 | `Kong/insomnia` | 39722 | 2346 | TypeScript | 1,167 stars this week | GraphQL、REST、WebSockets、SSE和gRPC的开源、跨平台API客户端。使用云、本地和Git存储。 | https://github.com/Kong/insomnia |  |
| 18 | `makeplane/plane` | 53078 | 4736 | TypeScript | 1,871 stars this week | 🔥🔥🔥 开源JIRA、Linear、Monday和ClickUp替代方案。Plane是一个现代化的项目管理平台，用于管理任务、冲刺、文档和分类。 | https://github.com/makeplane/plane |  |
| 19 | `bytedance/deer-flow` | 74705 | 10074 | Python | 3,068 stars this week | 研究、编码和创建的开源远程SuperAgent线束。借助沙箱、内存、工具、技能、子代理和消息网关，它可以处理可能需要几分钟到几小时的不同级别的任务。 | https://github.com/bytedance/deer-flow | 新增 |
| 20 | `mattpocock/skills` | 146273 | 12650 | Shell | 11,581 stars this week | 真正工程师的技能。直接来自我的.claude目录。 | https://github.com/mattpocock/skills | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `harry0703/MoneyPrinterTurbo` | 92586 | 13362 | Python | 35,076 stars this month | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. | https://github.com/harry0703/MoneyPrinterTurbo |  |
| 2 | `apple/container` | 43184 | 1266 | Swift | 15,056 stars this month | 用于在Mac上使用轻量级虚拟机创建和运行Linux容器的工具。它是用Swift编写的，并针对Apple芯片进行了优化。 | https://github.com/apple/container |  |
| 3 | `DeusData/codebase-memory-mcp` | 14746 | 1086 | C | 11,171 stars this month | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 4 | `calesthio/OpenMontage` | 22007 | 2470 | Python | 13,960 stars this month | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 5 | `mvanhorn/last30days-skill` | 46714 | 3873 | Python | 20,137 stars this month | 人工智能代理技能，研究Reddit、X、YouTube、HN、Polymarket和网络上的任何主题，然后合成基础摘要 | https://github.com/mvanhorn/last30days-skill |  |
| 6 | `Panniantong/Agent-Reach` | 41167 | 3255 | Python | 19,348 stars this month | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 7 | `iptv-org/iptv` | 128490 | 7082 | TypeScript | 12,109 stars this month | 收集来自世界各地的公开IPTV频道 | https://github.com/iptv-org/iptv |  |
| 8 | `microsoft/markitdown` | 159150 | 11133 | Python | 34,276 stars this month | 用于将文件和Office文档转换为Markdown的Python工具。 | https://github.com/microsoft/markitdown |  |
| 9 | `lfnovo/open-notebook` | 33336 | 3746 | TypeScript | 9,484 stars this month | 笔记本LM的开源实现，具有更大的灵活性和功能 | https://github.com/lfnovo/open-notebook |  |
| 10 | `phuryn/pm-skills` | 21063 | 2136 | — | 9,390 stars this month | PM Skills Marketplace ： 100多种代理技能、命令和插件—从发现到战略、执行、发布和增长。 | https://github.com/phuryn/pm-skills |  |
| 11 | `Leonxlnx/taste-skill` | 50963 | 3508 | JavaScript | 31,423 stars this month | 品味技能-让您的人工智能有良好的品味。阻止人工智能产生无聊的通用斜坡 | https://github.com/Leonxlnx/taste-skill |  |
| 12 | `esengine/DeepSeek-Reasonix` | 24673 | 1495 | Go | 18,341 stars this month | 为您的终端提供DeepSeek原生AI编码代理。围绕前缀缓存稳定性而设计—保持运行。 | https://github.com/esengine/DeepSeek-Reasonix |  |
| 13 | `Egonex-AI/Understand-Anything` | 67942 | 5624 | TypeScript | 43,940 stars this month | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Egonex-AI/Understand-Anything |  |
| 14 | `colbymchenry/codegraph` | 54569 | 3349 | TypeScript | 33,428 stars this month | 预索引的代码知识图，在代码更改时自动同步，适用于Claude Code、Codex、Gemini、Cursor、OpenCode、AntiGravity、Kiro和Hermes Agent —代币更少，工具调用更少， 100%本地 | https://github.com/colbymchenry/codegraph |  |
| 15 | `openai/plugins` | 3552 | 415 | JavaScript | 2,262 stars this month | OpenAI插件 | https://github.com/openai/plugins |  |
| 16 | `tashfeenahmed/freellmapi` | 12691 | 1931 | TypeScript | 7,377 stars this month | OpenAI兼容代理，将16个LLM提供商的免费层（约17亿个代币/月）堆叠在一个/v1端点后面—加上任何自定义OpenAI兼容端点。智能路由、自动故障转移、加密密钥。仅限个人实验。 | https://github.com/tashfeenahmed/freellmapi |  |
| 17 | `mukul975/Anthropic-Cybersecurity-Skills` | 21198 | 2445 | Python | 12,570 stars this month | 人工智能代理的817种结构化网络安全技能·映射到6个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF和MITRE F3 （打击欺诈） · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20 + p…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills |  |
| 18 | `hardikpandya/stop-slop` | 12443 | 863 | — | 8,335 stars this month | 从散文中删除AI TELLS的技能文件 | https://github.com/hardikpandya/stop-slop |  |
| 19 | `can1357/oh-my-pi` | 14637 | 1282 | TypeScript | 7,664 stars this month | 终端的AI编码代理—哈希锚定编辑、优化工具线束、LSP、Python、浏览器、子代理等 | https://github.com/can1357/oh-my-pi |  |
| 20 | `run-llama/liteparse` | 11060 | 727 | Rust | 5,736 stars this month | 快速、实用、开源的文档解析器 | https://github.com/run-llama/liteparse |  |
| 21 | `ogulcancelik/herdr` | 7328 | 450 | Rust | 4,800 stars this month | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 22 | `supermemoryai/supermemory` | 27540 | 2386 | TypeScript | 4,815 stars this month | 内存和上下文引擎+应用程序，速度极快，可扩展，可以在本地完全运行。人工智能时代的内存API。 | https://github.com/supermemoryai/supermemory |  |


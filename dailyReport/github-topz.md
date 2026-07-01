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

**最近一次更新时间**（Asia/Shanghai）： 2026-07-01 09:18:28

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 521151 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 480248 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 450677 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 445384 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 391041 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 381178 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 358731 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 355598 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 354673 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 305661 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `hasaneyldrm/exercises-dataset` | 6660 | 801 | HTML | 1,343 stars today | 包含433项健身练习的综合数据集。每个条目包括名称、类别、目标肌肉群、设备、说明、缩略图和动画视频。 | https://github.com/hasaneyldrm/exercises-dataset | 新增 |
| 2 | `usestrix/strix` | 28132 | 3125 | Python | 515 stars today | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix | 新增 |
| 3 | `msitarzewski/agency-agents` | 120917 | 19751 | Shell | 1,791 stars today | 一个完整的人工智能机构，触手可及--从前端向导到Reddit社区忍者，从奇思妙想的注入者到现实检查者。每位客服代表都是具有个性、流程和经过验证的交付成果的专家。 | https://github.com/msitarzewski/agency-agents |  |
| 4 | `altic-dev/FluidVoice` | 4932 | 301 | Swift | 588 stars today | 具有设备上STT和定制训练AI增强模型的最快且唯一的macOS听写应用程序- Local Wispr Flow替代方案。一个⭐需要我们走很长的路:)) Windows、iOS和Linux即将推出。 | https://github.com/altic-dev/FluidVoice |  |
| 5 | `diegosouzapw/OmniRoute` | 8536 | 1393 | TypeScript | 387 stars today | 永不停止编码。免费AI网关：一个端点， 231多家提供商（ 50多家免费） ，将Claude Code、Codex、Cursor、Cline和Copilot连接到免费的Claude/GPT/Gemini。RTK + Caveman堆叠压缩可节省15-95%的代币、智能自动回退、MCP/A2A、多模式API、桌面/PWA。 | https://github.com/diegosouzapw/OmniRoute | 新增 |
| 6 | `browser-use/video-use` | 12602 | 1607 | Python | 721 stars today | 使用编码代理编辑视频 | https://github.com/browser-use/video-use |  |
| 7 | `xbtlin/ai-berkshire` | 7498 | 954 | Python | 969 stars today | AI 时代的伯克希尔：基于 Claude Code / Codex 的价值投资研究框架。巴菲特·芒格·段永平·李录四大师方法论 + 多Agent并行研究。· AI-era Berkshire: a value investing research framework built for Claude Code / Codex. 4 masters' methodologies + multi-agent adversarial analysis. | https://github.com/xbtlin/ai-berkshire |  |
| 8 | `Mebus/cupp` | 6105 | 2048 | Python | 32 stars today | 通用用户密码分析器（ CUPP ） | https://github.com/Mebus/cupp | 新增 |
| 9 | `ripienaar/free-for-dev` | 127325 | 13307 | HTML | 742 stars today | 具有devops和infradev感兴趣的免费层的SaaS、PaaS和IaaS产品列表 | https://github.com/ripienaar/free-for-dev |  |
| 10 | `google/agents-cli` | 4199 | 454 | Python | 445 stars today | CLI和技能可将任何编码助手转变为在Google Cloud上创建、评估和部署AI代理的专家。 | https://github.com/google/agents-cli | 新增 |
| 11 | `roboflow/supervision` | 45913 | 4074 | Python | 309 stars today | 我们为您编写可重复使用的计算机视觉工具。 💜 | https://github.com/roboflow/supervision | 新增 |
| 12 | `ogulcancelik/herdr` | 9022 | 543 | Rust | 486 stars today | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr | 新增 |
| 13 | `simplex-chat/simplex-chat` | 17336 | 1008 | Haskell | 1,235 stars today | SimpleX -第一个没有任何类型用户标识符的消息传递网络-设计为100 ％私有！ iOS ， Android和桌面应用程序📱！ | https://github.com/simplex-chat/simplex-chat |  |
| 14 | `CoreBunch/Instatic` | 1533 | 138 | TypeScript | 351 stars today | Instatic是一款现代化的自托管可视化CMS ，只需1分钟即可运行 | https://github.com/CoreBunch/Instatic | 新增 |
| 15 | `microsoft/AI-For-Beginners` | 49375 | 10163 | Jupyter Notebook | 252 stars today | 12周， 24课，全民人工智能！ | https://github.com/microsoft/AI-For-Beginners | 新增 |
| 16 | `facebook/astryx` | 1788 | 96 | TypeScript | 364 stars today | 完全可定制和代理就绪的开源设计系统 | https://github.com/facebook/astryx | 新增 |
| 17 | `HKUDS/Vibe-Trading` | 15796 | 2736 | Python | 721 stars today | “Vibe-Trading ：您的个人交易代理” | https://github.com/HKUDS/Vibe-Trading |  |
| 18 | `obra/superpowers` | 242514 | 21521 | Shell | 890 stars today | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers | 新增 |
| 19 | `Robbyant/lingbot-map` | 8871 | 859 | Python | 189 stars today | 用于从流数据重建场景的前馈3D基础模型 | https://github.com/Robbyant/lingbot-map | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `calesthio/OpenMontage` | 29902 | 3373 | Python | 15,353 stars this week | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 2 | `simplex-chat/simplex-chat` | 17336 | 1008 | Haskell | 5,995 stars this week | SimpleX -第一个没有任何类型用户标识符的消息传递网络-设计为100 ％私有！ iOS ， Android和桌面应用程序📱！ | https://github.com/simplex-chat/simplex-chat |  |
| 3 | `google-labs-code/design.md` | 23717 | 1870 | TypeScript | 7,524 stars this week | 用于向编码代理描述视觉标识的格式规范。DESIGN.md为代理提供了对设计系统的持久、结构化的理解。 | https://github.com/google-labs-code/design.md |  |
| 4 | `DeusData/codebase-memory-mcp` | 22868 | 1661 | C | 10,031 stars this week | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 5 | `kunchenguid/no-mistakes` | 4535 | 258 | Go | 2,783 stars this week | git push no-mistakes | https://github.com/kunchenguid/no-mistakes |  |
| 6 | `JCodesMore/ai-website-cloner-template` | 23978 | 3407 | TypeScript | 5,624 stars this week | 使用AI编码代理，只需一个命令即可克隆任何网站 | https://github.com/JCodesMore/ai-website-cloner-template |  |
| 7 | `mauriceboe/TREK` | 8592 | 719 | TypeScript | 2,744 stars this week | 自托管行程/行程规划工具，提供实时协作、互动地图、PWA支持、SSO、预算、装箱单等功能。 | https://github.com/mauriceboe/TREK | 新增 |
| 8 | `ZhuLinsen/daily_stock_analysis` | 52492 | 45523 | Python | 5,806 stars this week | LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。 LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs. | https://github.com/ZhuLinsen/daily_stock_analysis |  |
| 9 | `stablyai/orca` | 9689 | 660 | TypeScript | 3,311 stars this week | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 10 | `alibaba/page-agent` | 20794 | 1780 | TypeScript | 1,591 stars this week | JavaScript页面内GUI代理。使用自然语言控制Web界面。 | https://github.com/alibaba/page-agent |  |
| 11 | `topoteretes/cognee` | 26113 | 2402 | Python | 6,417 stars this week | Cognee是面向智能体的开源AI内存平台。使用自托管知识图表引擎，为您的人工智能代理提供跨会话的持久长期记忆。 | https://github.com/topoteretes/cognee |  |
| 12 | `Robbyant/lingbot-map` | 8871 | 859 | Python | 1,388 stars this week | 用于从流数据重建场景的前馈3D基础模型 | https://github.com/Robbyant/lingbot-map | 新增 |
| 13 | `interviewstreet/hiring-agent` | 3996 | 788 | Python | 2,266 stars this week | 用于评估和评分简历的AI代理。 | https://github.com/interviewstreet/hiring-agent |  |
| 14 | `Panniantong/Agent-Reach` | 47085 | 3729 | Python | 8,398 stars this week | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 15 | `jamiepine/voicebox` | 36308 | 4347 | TypeScript | 3,336 stars this week | 开源AI语音工作室。克隆、命令、创建。 | https://github.com/jamiepine/voicebox |  |
| 16 | `mukul975/Anthropic-Cybersecurity-Skills` | 23472 | 2668 | Python | 4,109 stars this week | 人工智能代理的817种结构化网络安全技能·映射到6个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF和MITRE F3 （打击欺诈） · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20 + p…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills |  |
| 17 | `aws/agent-toolkit-for-aws` | 1651 | 137 | Python | 684 stars this week | AWS支持的官方MCP服务器、技能和插件，以帮助AI代理在AWS上构建 | https://github.com/aws/agent-toolkit-for-aws |  |
| 18 | `NanmiCoder/MediaCrawler` | 54507 | 11100 | Python | 2,683 stars this week | 小红书笔记 · 评论爬虫、抖音视频 · 评论爬虫、快手视频 · 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖子 ｜ 百度贴吧评论回复爬虫 · 知乎问答文章｜评论爬虫 | https://github.com/NanmiCoder/MediaCrawler |  |
| 19 | `BuilderIO/agent-native` | 3203 | 309 | TypeScript | 1,370 stars this week | 用于构建代理本机应用程序的框架。 | https://github.com/BuilderIO/agent-native |  |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `apple/container` | 45360 | 1342 | Swift | 18,624 stars this month | 用于在Mac上使用轻量级虚拟机创建和运行Linux容器的工具。它是用Swift编写的，并针对Apple芯片进行了优化。 | https://github.com/apple/container |  |
| 2 | `DeusData/codebase-memory-mcp` | 22868 | 1661 | C | 19,612 stars this month | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 3 | `calesthio/OpenMontage` | 29902 | 3373 | Python | 25,466 stars this month | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 4 | `Panniantong/Agent-Reach` | 47086 | 3729 | Python | 26,239 stars this month | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 5 | `mvanhorn/last30days-skill` | 47927 | 3961 | Python | 21,268 stars this month | 人工智能代理技能，研究Reddit、X、YouTube、HN、Polymarket和网络上的任何主题，然后合成基础摘要 | https://github.com/mvanhorn/last30days-skill |  |
| 6 | `iptv-org/iptv` | 129590 | 7179 | TypeScript | 13,223 stars this month | 收集来自世界各地的公开IPTV频道 | https://github.com/iptv-org/iptv |  |
| 7 | `phuryn/pm-skills` | 21896 | 2206 | — | 10,208 stars this month | PM Skills Marketplace ： 100多种代理技能、命令和插件—从发现到战略、执行、发布和增长。 | https://github.com/phuryn/pm-skills |  |
| 8 | `lfnovo/open-notebook` | 34138 | 3806 | TypeScript | 10,333 stars this month | 笔记本LM的开源实现，具有更大的灵活性和功能 | https://github.com/lfnovo/open-notebook |  |
| 9 | `harry0703/MoneyPrinterTurbo` | 94507 | 13733 | Python | 21,864 stars this month | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. | https://github.com/harry0703/MoneyPrinterTurbo |  |
| 10 | `openai/plugins` | 3826 | 444 | JavaScript | 2,528 stars this month | OpenAI插件 | https://github.com/openai/plugins |  |
| 11 | `asgeirtj/system_prompts_leaks` | 47402 | 7736 | JavaScript | 6,472 stars this month | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT 5.5 Thinking ， GPT 5.5 Instant ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 12 | `Leonxlnx/taste-skill` | 53874 | 3712 | JavaScript | 24,412 stars this month | 品味技能-让您的人工智能有良好的品味。阻止人工智能产生无聊的通用斜坡 | https://github.com/Leonxlnx/taste-skill |  |
| 13 | `alibaba/zvec` | 12641 | 754 | C++ | 2,930 stars this month | 轻量级、快如闪电的进程内矢量数据库 | https://github.com/alibaba/zvec | 新增 |
| 14 | `stablyai/orca` | 9689 | 660 | TypeScript | 5,752 stars this month | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 15 | `ogulcancelik/herdr` | 9023 | 543 | Rust | 5,502 stars this month | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 16 | `mukul975/Anthropic-Cybersecurity-Skills` | 23472 | 2668 | Python | 10,688 stars this month | 人工智能代理的817种结构化网络安全技能·映射到6个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF和MITRE F3 （打击欺诈） · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20 + p…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills |  |
| 17 | `kenn-io/agentsview` | 3457 | 273 | Go | 2,301 stars this month | 编码代理的本地首次会话搜索、分析、见解和令牌使用统计信息，支持Claude Code、Codex和其他20多个代理。 | https://github.com/kenn-io/agentsview | 新增 |
| 18 | `tashfeenahmed/freellmapi` | 14255 | 2099 | TypeScript | 7,626 stars this month | OpenAI兼容代理，将16个LLM提供商的免费层（约17亿个代币/月）堆叠在一个/v1端点后面—加上任何自定义OpenAI兼容端点。智能路由、自动故障转移、加密密钥。仅限个人实验。 | https://github.com/tashfeenahmed/freellmapi |  |
| 19 | `OpenCut-app/OpenCut` | 60732 | 6569 | TypeScript | 8,695 stars this month | 开源CapCut替代方案 | https://github.com/OpenCut-app/OpenCut | 新增 |
| 20 | `can1357/oh-my-pi` | 15336 | 1357 | TypeScript | 6,466 stars this month | 终端的AI编码代理—哈希锚定编辑、优化工具线束、LSP、Python、浏览器、子代理等 | https://github.com/can1357/oh-my-pi |  |


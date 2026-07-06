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

**最近一次更新时间**（Asia/Shanghai）： 2026-07-06 09:14:51

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 522448 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 481522 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 451069 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 446904 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 391335 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 381840 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 359412 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 356264 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 355163 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 306316 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
| 11 | `awesome-selfhosted/awesome-selfhosted` | 301670 | 可自行部署的各类自由软件网络服务与 Web 应用清单。 | https://github.com/awesome-selfhosted/awesome-selfhosted |  |
| 12 | `996icu/996.ICU` | 276361 | 倡议关注「996」工作制、计数星标与交流的开发社区仓库（含网络迷因用语）。 | https://github.com/996icu/996.ICU |  |
| 13 | `practical-tutorials/project-based-learning` | 272207 | 基于项目的教程精选列表 | https://github.com/practical-tutorials/project-based-learning |  |
| 14 | `obra/superpowers` | 246876 | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers | 新增 |
| 15 | `facebook/react` | 245279 | 用于构建 Web 与原生用户界面的 React 视图库（含多端生态）。 | https://github.com/facebook/react |  |
| 16 | `torvalds/linux` | 238531 | Linux内核源树 | https://github.com/torvalds/linux | 新增 |

---
## Trending 页面快照（HTML 抓取）

**说明**：与上方「全局 Star Search」数据源不同；本段按 GitHub trending 页的 **daily / weekly / monthly** 各拉一页并解析。**若前端改版导致选择器失效，需更新解析逻辑。**

- **标记**列：三个 `since` 子表**各自独立**对照本次拉取前文件中该小节表格已出现的 `owner/repo`；新出现的行标 **新增**。下次拉取会先清空上一轮「新增」再重算（只保留相对**上一版文件**的新仓库）。

### 今日 trending（since=daily）

**页面**： `https://github.com/trending?since=daily`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `Zackriya-Solutions/meetily` | 17032 | 1803 | Rust | 1,409 stars today | 隐私第一，基于Rust构建的人工智能会议助手，具有4倍的Parakeet/Whisper实时转录、扬声器日记和Ollama摘要。100%本地处理。无需云。Meetily （ Meetly Ai - https://meetily.ai ）是首屈一指的自托管、开源Ai会议...... | https://github.com/Zackriya-Solutions/meetily |  |
| 2 | `openai/codex-plugin-cc` | 25476 | 1539 | JavaScript | 1,532 stars today | 使用Claude Code的Codex来查看代码或委派任务。 | https://github.com/openai/codex-plugin-cc |  |
| 3 | `asgeirtj/system_prompts_leaks` | 49970 | 8180 | JavaScript | 981 stars today | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT 5.5 Thinking ， GPT 5.5 Instant ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 4 | `Leonxlnx/taste-skill` | 57505 | 3936 | JavaScript | 863 stars today | 品味技能-让您的人工智能有良好的品味。阻止人工智能产生无聊的通用斜坡 | https://github.com/Leonxlnx/taste-skill | 新增 |
| 5 | `alirezarezvani/claude-skills` | 20574 | 2794 | Python | 392 stars today | 337 Claude Code技能和代理技能和插件（ 30多个代理、70多个自定义命令、330多个技能、可定制的参考文献、脚本） ，适用于Claude Code、Codex、Gemini CLI、Cursor和其他8个编码代理—工程、营销、产品、合规、C级咨询、研究…… | https://github.com/alirezarezvani/claude-skills |  |
| 6 | `rommapp/romm` | 10544 | 505 | Python | 410 stars today | 一个美丽、强大、自托管的ROM管理器和播放器。 | https://github.com/rommapp/romm |  |
| 7 | `ogulcancelik/herdr` | 12076 | 702 | Rust | 651 stars today | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 8 | `alibaba/page-agent` | 23895 | 2061 | TypeScript | 805 stars today | JavaScript页面内GUI代理。使用自然语言控制Web界面。 | https://github.com/alibaba/page-agent |  |
| 9 | `harvard-edge/cs249r_book` | 26851 | 3193 | Python | 329 stars today | 机器学习系统 | https://github.com/harvard-edge/cs249r_book |  |
| 10 | `usestrix/strix` | 37133 | 3766 | Python | 1,114 stars today | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 11 | `hesreallyhim/awesome-claude-code` | 48367 | 4232 | Python | 148 stars today | 来自Anthropic PBC不可阻挡团队的编码伙伴无可争议的冠军Claude Code ，为最优秀的代理人精心挑选了最优秀的资源。顶级技能的精彩展示，双手灵巧的代理，闪烁的状态线， t… | https://github.com/hesreallyhim/awesome-claude-code | 新增 |
| 12 | `coreyhaines31/marketingskills` | 36437 | 5896 | JavaScript | 145 stars today | Claude Code和人工智能代理的营销技能。CRO、文案撰写、搜索引擎优化、分析和增长工程。 | https://github.com/coreyhaines31/marketingskills | 新增 |
| 13 | `JuliusBrussee/caveman` | 84874 | 4719 | JavaScript | 1,052 stars today | 🪨 为什么在很少令牌欺骗时使用许多令牌— Claude Code技能通过像穴居人一样说话来削减65 ％的令牌 | https://github.com/JuliusBrussee/caveman |  |
| 14 | `CoplayDev/unity-mcp` | 11929 | 1278 | C# | 414 stars today | Unity MCP充当AI助手和Unity Editor之间的桥梁。为您的LLM工具提供在Unity中管理资源、控制场景、编辑脚本和自动化任务的工具。 | https://github.com/CoplayDev/unity-mcp |  |
| 15 | `facebook/astryx` | 5893 | 374 | TypeScript | 522 stars today | 完全可定制和代理就绪的开源设计系统 | https://github.com/facebook/astryx | 新增 |
| 16 | `immich-app/immich` | 106122 | 6057 | TypeScript | 470 stars today | 高性能自托管照片和视频管理解决方案。 | https://github.com/immich-app/immich |  |
| 17 | `ruvnet/RuView` | 76724 | 10284 | Rust | 161 stars today | π RuView将商用WiFi信号转化为实时空间智能、生命体征监测和存在检测--所有这些都无需一个像素的视频。 | https://github.com/ruvnet/RuView | 新增 |
| 18 | `gastownhall/gastown` | 16388 | 1519 | Go | 51 stars today | Gas Town -多代理工作区经理 | https://github.com/gastownhall/gastown | 新增 |
| 19 | `dotnet/skills` | 4043 | 302 | C# | 246 stars today | 用于使用.NET和C #协助AI编码代理的技能的存储库 | https://github.com/dotnet/skills |  |
| 20 | `OthmanAdi/planning-with-files` | 24716 | 2106 | Python | 66 stars today | 为AI编码代理和长期运行的代理任务提供基于文件的持久规划。在上下文丢失和/或清除后仍可使用的防崩溃扣分计划，以及磁盘上的确定性完成门和多Agent共享状态。手工风格。适用于Claude Code、Codex CLI、Cursor…… | https://github.com/OthmanAdi/planning-with-files | 新增 |
| 21 | `steipete/CodexBar` | 16226 | 1351 | Swift | 153 stars today | 显示OpenAI Codex和Claude Code的使用统计信息，无需登录。 | https://github.com/steipete/CodexBar | 新增 |
| 22 | `anthropics/claude-code` | 136301 | 21906 | Python | 156 stars today | Claude Code是一个代理编码工具，它位于您的终端中，了解您的代码库，并通过执行日常任务、解释复杂代码和处理git工作流程（所有这些都通过自然语言命令）来帮助您更快地进行编码。 | https://github.com/anthropics/claude-code | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `usestrix/strix` | 37134 | 3766 | Python | 10,338 stars this week | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 2 | `xbtlin/ai-berkshire` | 10318 | 1312 | Python | 5,038 stars this week | AI 时代的伯克希尔：基于 Claude Code / Codex 的价值投资研究框架。巴菲特·芒格·段永平·李录四大师方法论 + 多Agent并行研究。· AI-era Berkshire: a value investing research framework built for Claude Code / Codex. 4 masters' methodologies + multi-agent adversarial analysis. | https://github.com/xbtlin/ai-berkshire |  |
| 3 | `diegosouzapw/OmniRoute` | 11877 | 1722 | TypeScript | 4,411 stars this week | 永不停止编码。免费AI网关：一个端点， 231多家提供商（ 50多家免费） ，将Claude Code、Codex、Cursor、Cline和Copilot连接到免费的Claude/GPT/Gemini。RTK + Caveman堆叠压缩可节省15-95%的代币、智能自动回退、MCP/A2A、多模式API、桌面/PWA。 | https://github.com/diegosouzapw/OmniRoute |  |
| 4 | `simplex-chat/simplex-chat` | 17923 | 1055 | Haskell | 3,572 stars this week | SimpleX -第一个没有任何类型用户标识符的消息传递网络-设计为100 ％私有！ iOS ， Android和桌面应用程序📱！ | https://github.com/simplex-chat/simplex-chat |  |
| 5 | `Robbyant/lingbot-map` | 9896 | 982 | Python | 1,875 stars this week | 用于从流数据重建场景的前馈3D基础模型 | https://github.com/Robbyant/lingbot-map |  |
| 6 | `ogulcancelik/herdr` | 12076 | 702 | Rust | 3,937 stars this week | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 7 | `logto-io/logto` | 13826 | 947 | TypeScript | 1,575 stars this week | SaaS和AI应用程序🧑‍🚀的身份验证和授权基础设施，基于OIDC和OAuth 2.1 ，具有多租户、SSO和RBAC。 | https://github.com/logto-io/logto |  |
| 8 | `Zackriya-Solutions/meetily` | 17032 | 1803 | Rust | 2,972 stars this week | 隐私第一，基于Rust构建的人工智能会议助手，具有4倍的Parakeet/Whisper实时转录、扬声器日记和Ollama摘要。100%本地处理。无需云。Meetily （ Meetly Ai - https://meetily.ai ）是首屈一指的自托管、开源Ai会议...... | https://github.com/Zackriya-Solutions/meetily | 新增 |
| 9 | `browser-use/video-use` | 15033 | 1777 | Python | 4,288 stars this week | 使用编码代理编辑视频 | https://github.com/browser-use/video-use |  |
| 10 | `alibaba/page-agent` | 23895 | 2061 | TypeScript | 3,151 stars this week | JavaScript页面内GUI代理。使用自然语言控制Web界面。 | https://github.com/alibaba/page-agent |  |
| 11 | `Starmel/OpenSuperWhisper` | 1808 | 150 | Swift | 532 stars this week | macOS听写应用 | https://github.com/Starmel/OpenSuperWhisper |  |
| 12 | `msitarzewski/agency-agents` | 127517 | 20709 | Shell | 10,637 stars this week | 一个完整的人工智能机构，触手可及--从前端向导到Reddit社区忍者，从奇思妙想的注入者到现实检查者。每位客服代表都是具有个性、流程和经过验证的交付成果的专家。 | https://github.com/msitarzewski/agency-agents |  |
| 13 | `apache/maven` | 5286 | 2905 | Java | 173 stars this week | Apache Maven核心 | https://github.com/apache/maven |  |
| 14 | `openai/codex-plugin-cc` | 25477 | 1539 | JavaScript | 3,405 stars this week | 使用Claude Code的Codex来查看代码或委派任务。 | https://github.com/openai/codex-plugin-cc |  |
| 15 | `DeusData/codebase-memory-mcp` | 26728 | 1984 | C | 7,945 stars this week | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 16 | `stablyai/orca` | 12375 | 836 | TypeScript | 3,783 stars this week | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 17 | `calesthio/OpenMontage` | 33667 | 3860 | Python | 7,353 stars this week | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 18 | `JCodesMore/ai-website-cloner-template` | 25844 | 3636 | TypeScript | 3,246 stars this week | 使用AI编码代理，只需一个命令即可克隆任何网站 | https://github.com/JCodesMore/ai-website-cloner-template |  |
| 19 | `ZhuLinsen/daily_stock_analysis` | 54707 | 47360 | Python | 3,806 stars this week | LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。 LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs. | https://github.com/ZhuLinsen/daily_stock_analysis |  |
| 20 | `allenai/olmocr` | 18794 | 1541 | Python | 1,212 stars this week | 用于线性化LLM数据集/培训的PDF的工具包 | https://github.com/allenai/olmocr |  |
| 21 | `topoteretes/cognee` | 27122 | 2525 | Python | 2,699 stars this week | Cognee是面向智能体的开源AI内存平台。使用自托管知识图表引擎，为您的人工智能代理提供跨会话的持久长期记忆。 | https://github.com/topoteretes/cognee |  |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `apple/container` | 46635 | 1397 | Swift | 19,954 stars this month | 用于在Mac上使用轻量级虚拟机创建和运行Linux容器的工具。它是用Swift编写的，并针对Apple芯片进行了优化。 | https://github.com/apple/container |  |
| 2 | `DeusData/codebase-memory-mcp` | 26728 | 1984 | C | 23,591 stars this month | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 3 | `calesthio/OpenMontage` | 33667 | 3860 | Python | 29,179 stars this month | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 4 | `Panniantong/Agent-Reach` | 51298 | 4119 | Python | 30,017 stars this month | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 5 | `mvanhorn/last30days-skill` | 49167 | 4078 | Python | 21,367 stars this month | 人工智能代理技能，研究Reddit、X、YouTube、HN、Polymarket和网络上的任何主题，然后合成基础摘要 | https://github.com/mvanhorn/last30days-skill |  |
| 6 | `iptv-org/iptv` | 130575 | 7261 | TypeScript | 14,048 stars this month | 收集来自世界各地的公开IPTV频道 | https://github.com/iptv-org/iptv |  |
| 7 | `interviewstreet/hiring-agent` | 4836 | 917 | Python | 3,975 stars this month | 用于评估和评分简历的AI代理。 | https://github.com/interviewstreet/hiring-agent |  |
| 8 | `phuryn/pm-skills` | 22621 | 2274 | — | 10,731 stars this month | PM Skills Marketplace ： 100多种代理技能、命令和插件—从发现到战略、执行、发布和增长。 | https://github.com/phuryn/pm-skills |  |
| 9 | `asgeirtj/system_prompts_leaks` | 49971 | 8180 | JavaScript | 8,311 stars this month | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT 5.5 Thinking ， GPT 5.5 Instant ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 10 | `ogulcancelik/herdr` | 12076 | 702 | Rust | 7,360 stars this month | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 11 | `stablyai/orca` | 12375 | 836 | TypeScript | 8,064 stars this month | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 12 | `usestrix/strix` | 37134 | 3766 | Python | 10,932 stars this month | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 13 | `kenn-io/agentsview` | 3747 | 291 | Go | 2,486 stars this month | 编码代理的本地首次会话搜索、分析、见解和令牌使用统计信息，支持Claude Code、Codex和其他20多个代理。 | https://github.com/kenn-io/agentsview | 新增 |
| 14 | `n0-computer/iroh` | 11130 | 515 | Rust | 2,466 stars this month | IP地址中断，改为拨号键。将QUIC + NAT遍历添加到您的应用程序的库。 | https://github.com/n0-computer/iroh |  |
| 15 | `roboflow/supervision` | 46803 | 4172 | Python | 6,888 stars this month | 我们为您编写可重复使用的计算机视觉工具。 💜 | https://github.com/roboflow/supervision |  |
| 16 | `openai/plugins` | 4075 | 470 | JavaScript | 2,651 stars this month | OpenAI插件 | https://github.com/openai/plugins |  |
| 17 | `t8y2/dbx` | 8714 | 737 | Rust | 4,861 stars this month | 20MB, lightweight, cross-platform database client. Supports MySQL, PostgreSQL, SQLite, Redis, MongoDB, DuckDB, ClickHouse, SQL Server and more.20MB，轻量级跨平台数据库客户端、数据库管理工具。支持 MySQL、PostgreSQL、SQLite、Redis、MongoDB、DuckDB、ClickHouse、SQL Server 等。 | https://github.com/t8y2/dbx |  |
| 18 | `lfnovo/open-notebook` | 34959 | 3884 | TypeScript | 9,499 stars this month | 笔记本LM的开源实现，具有更大的灵活性和功能 | https://github.com/lfnovo/open-notebook |  |
| 19 | `mukul975/Anthropic-Cybersecurity-Skills` | 24626 | 2805 | Python | 10,363 stars this month | 人工智能代理的817种结构化网络安全技能·映射到6个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF和MITRE F3 （打击欺诈） · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20 + p…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills |  |
| 20 | `every-app/open-seo` | 4100 | 458 | TypeScript | 1,924 stars this month | Semrush和Ahrefs的开源替代品 | https://github.com/every-app/open-seo | 新增 |


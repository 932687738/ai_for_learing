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

**最近一次更新时间**（Asia/Shanghai）： 2026-07-05 08:46:49

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 522448 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 481522 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 451069 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 446610 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 391275 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 381728 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 359281 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 356126 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 355077 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 306316 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `openai/codex-plugin-cc` | 24423 | 1484 | JavaScript | 718 stars today | 使用Claude Code的Codex来查看代码或委派任务。 | https://github.com/openai/codex-plugin-cc |  |
| 2 | `JuliusBrussee/caveman` | 83972 | 4677 | JavaScript | 1,089 stars today | 🪨 为什么在很少令牌欺骗时使用许多令牌— Claude Code技能通过像穴居人一样说话来削减65 ％的令牌 | https://github.com/JuliusBrussee/caveman |  |
| 3 | `alibaba/page-agent` | 23111 | 2008 | TypeScript | 742 stars today | JavaScript页面内GUI代理。使用自然语言控制Web界面。 | https://github.com/alibaba/page-agent | 新增 |
| 4 | `usestrix/strix` | 36042 | 3654 | Python | 1,904 stars today | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 5 | `ChromeDevTools/chrome-devtools-mcp` | 45775 | 2980 | TypeScript | 304 stars today | 适用于编码代理的Chrome开发者工具 | https://github.com/ChromeDevTools/chrome-devtools-mcp |  |
| 6 | `Zackriya-Solutions/meetily` | 15274 | 1671 | Rust | 718 stars today | 隐私第一，基于Rust构建的人工智能会议助手，具有4倍的Parakeet/Whisper实时转录、扬声器日记和Ollama摘要。100%本地处理。无需云。Meetily （ Meetly Ai - https://meetily.ai ）是首屈一指的自托管、开源Ai会议...... | https://github.com/Zackriya-Solutions/meetily | 新增 |
| 7 | `asgeirtj/system_prompts_leaks` | 48919 | 7982 | JavaScript | 471 stars today | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT 5.5 Thinking ， GPT 5.5 Instant ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks | 新增 |
| 8 | `harvard-edge/cs249r_book` | 26563 | 3164 | Python | 443 stars today | 机器学习系统 | https://github.com/harvard-edge/cs249r_book |  |
| 9 | `rommapp/romm` | 10208 | 493 | Python | 398 stars today | 一个美丽、强大、自托管的ROM管理器和播放器。 | https://github.com/rommapp/romm | 新增 |
| 10 | `ogulcancelik/herdr` | 11439 | 669 | Rust | 707 stars today | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr | 新增 |
| 11 | `dotnet/skills` | 3805 | 289 | C# | 59 stars today | 用于使用.NET和C #协助AI编码代理的技能的存储库 | https://github.com/dotnet/skills | 新增 |
| 12 | `agentskills/agentskills` | 22336 | 1411 | Python | 351 stars today | 客服代表技能的规范和文档 | https://github.com/agentskills/agentskills |  |
| 13 | `immich-app/immich` | 105629 | 6029 | TypeScript | 201 stars today | 高性能自托管照片和视频管理解决方案。 | https://github.com/immich-app/immich | 新增 |
| 14 | `chthollyphile/folia-major` | 987 | 63 | TypeScript | 175 stars today | 专注于绚丽的歌词动画效果的本地音乐/navidrome/第三方网易云播放器 | https://github.com/chthollyphile/folia-major | 新增 |
| 15 | `mattpocock/skills` | 156557 | 13471 | Shell | 973 stars today | 真正工程师的技能。直接来自我的.claude目录。 | https://github.com/mattpocock/skills | 新增 |
| 16 | `CoplayDev/unity-mcp` | 11597 | 1262 | C# | 69 stars today | Unity MCP充当AI助手和Unity Editor之间的桥梁。为您的LLM工具提供在Unity中管理资源、控制场景、编辑脚本和自动化任务的工具。 | https://github.com/CoplayDev/unity-mcp | 新增 |
| 17 | `alirezarezvani/claude-skills` | 20156 | 2759 | Python | 136 stars today | 337 Claude Code技能和代理技能和插件（ 30多个代理、70多个自定义命令、330多个技能、可定制的参考文献、脚本） ，适用于Claude Code、Codex、Gemini CLI、Cursor和其他8个编码代理—工程、营销、产品、合规、C级咨询、研究…… | https://github.com/alirezarezvani/claude-skills | 新增 |
| 18 | `crynta/terax-ai` | 8056 | 861 | TypeScript | 62 stars today | 轻量级（ 7MB ）终端优先的人工智能原生开发工作区 | https://github.com/crynta/terax-ai | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `usestrix/strix` | 36043 | 3654 | Python | 9,362 stars this week | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix | 新增 |
| 2 | `xbtlin/ai-berkshire` | 9664 | 1227 | Python | 5,984 stars this week | AI 时代的伯克希尔：基于 Claude Code / Codex 的价值投资研究框架。巴菲特·芒格·段永平·李录四大师方法论 + 多Agent并行研究。· AI-era Berkshire: a value investing research framework built for Claude Code / Codex. 4 masters' methodologies + multi-agent adversarial analysis. | https://github.com/xbtlin/ai-berkshire | 新增 |
| 3 | `simplex-chat/simplex-chat` | 17847 | 1047 | Haskell | 4,630 stars this week | SimpleX -第一个没有任何类型用户标识符的消息传递网络-设计为100 ％私有！ iOS ， Android和桌面应用程序📱！ | https://github.com/simplex-chat/simplex-chat | 新增 |
| 4 | `Robbyant/lingbot-map` | 9733 | 962 | Python | 2,065 stars this week | 用于从流数据重建场景的前馈3D基础模型 | https://github.com/Robbyant/lingbot-map | 新增 |
| 5 | `diegosouzapw/OmniRoute` | 11309 | 1637 | TypeScript | 4,133 stars this week | 永不停止编码。免费AI网关：一个端点， 231多家提供商（ 50多家免费） ，将Claude Code、Codex、Cursor、Cline和Copilot连接到免费的Claude/GPT/Gemini。RTK + Caveman堆叠压缩可节省15-95%的代币、智能自动回退、MCP/A2A、多模式API、桌面/PWA。 | https://github.com/diegosouzapw/OmniRoute | 新增 |
| 6 | `DeusData/codebase-memory-mcp` | 26176 | 1938 | C | 9,517 stars this week | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp | 新增 |
| 7 | `ogulcancelik/herdr` | 11439 | 669 | Rust | 3,506 stars this week | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr | 新增 |
| 8 | `logto-io/logto` | 13728 | 942 | TypeScript | 1,488 stars this week | SaaS和AI应用程序🧑‍🚀的身份验证和授权基础设施，基于OIDC和OAuth 2.1 ，具有多租户、SSO和RBAC。 | https://github.com/logto-io/logto | 新增 |
| 9 | `Starmel/OpenSuperWhisper` | 1713 | 146 | Swift | 499 stars this week | macOS听写应用 | https://github.com/Starmel/OpenSuperWhisper | 新增 |
| 10 | `browser-use/video-use` | 14688 | 1750 | Python | 4,174 stars this week | 使用编码代理编辑视频 | https://github.com/browser-use/video-use | 新增 |
| 11 | `msitarzewski/agency-agents` | 127037 | 20615 | Shell | 10,976 stars this week | 一个完整的人工智能机构，触手可及--从前端向导到Reddit社区忍者，从奇思妙想的注入者到现实检查者。每位客服代表都是具有个性、流程和经过验证的交付成果的专家。 | https://github.com/msitarzewski/agency-agents | 新增 |
| 12 | `calesthio/OpenMontage` | 33114 | 3797 | Python | 8,447 stars this week | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage | 新增 |
| 13 | `JCodesMore/ai-website-cloner-template` | 25556 | 3598 | TypeScript | 3,730 stars this week | 使用AI编码代理，只需一个命令即可克隆任何网站 | https://github.com/JCodesMore/ai-website-cloner-template | 新增 |
| 14 | `stablyai/orca` | 12028 | 806 | TypeScript | 3,790 stars this week | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca | 新增 |
| 15 | `openai/codex-plugin-cc` | 24423 | 1484 | JavaScript | 1,974 stars this week | 使用Claude Code的Codex来查看代码或委派任务。 | https://github.com/openai/codex-plugin-cc | 新增 |
| 16 | `topoteretes/cognee` | 26974 | 2509 | Python | 3,388 stars this week | Cognee是面向智能体的开源AI内存平台。使用自托管知识图表引擎，为您的人工智能代理提供跨会话的持久长期记忆。 | https://github.com/topoteretes/cognee | 新增 |
| 17 | `interviewstreet/hiring-agent` | 4692 | 903 | Python | 1,647 stars this week | 用于评估和评分简历的AI代理。 | https://github.com/interviewstreet/hiring-agent | 新增 |
| 18 | `allenai/olmocr` | 18706 | 1536 | Python | 1,229 stars this week | 用于线性化LLM数据集/培训的PDF的工具包 | https://github.com/allenai/olmocr | 新增 |
| 19 | `apache/maven` | 5269 | 2905 | Java | 157 stars this week | Apache Maven核心 | https://github.com/apache/maven | 新增 |
| 20 | `craft-ai-agents/craft-agents-oss` | 6707 | 920 | TypeScript | 341 stars this week | — | https://github.com/craft-ai-agents/craft-agents-oss | 新增 |
| 21 | `ZhuLinsen/daily_stock_analysis` | 54272 | 46990 | Python | 3,842 stars this week | LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。 LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs. | https://github.com/ZhuLinsen/daily_stock_analysis | 新增 |
| 22 | `alibaba/page-agent` | 23111 | 2008 | TypeScript | 2,484 stars this week | JavaScript页面内GUI代理。使用自然语言控制Web界面。 | https://github.com/alibaba/page-agent | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `apple/container` | 46439 | 1382 | Swift | 19,762 stars this month | 用于在Mac上使用轻量级虚拟机创建和运行Linux容器的工具。它是用Swift编写的，并针对Apple芯片进行了优化。 | https://github.com/apple/container |  |
| 2 | `DeusData/codebase-memory-mcp` | 26176 | 1938 | C | 23,024 stars this month | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 3 | `calesthio/OpenMontage` | 33114 | 3797 | Python | 28,653 stars this month | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 4 | `Panniantong/Agent-Reach` | 50627 | 4042 | Python | 29,397 stars this month | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 5 | `mvanhorn/last30days-skill` | 48938 | 4048 | Python | 21,849 stars this month | 人工智能代理技能，研究Reddit、X、YouTube、HN、Polymarket和网络上的任何主题，然后合成基础摘要 | https://github.com/mvanhorn/last30days-skill |  |
| 6 | `iptv-org/iptv` | 130411 | 7246 | TypeScript | 13,918 stars this month | 收集来自世界各地的公开IPTV频道 | https://github.com/iptv-org/iptv |  |
| 7 | `simplex-chat/simplex-chat` | 17847 | 1047 | Haskell | 6,724 stars this month | SimpleX -第一个没有任何类型用户标识符的消息传递网络-设计为100 ％私有！ iOS ， Android和桌面应用程序📱！ | https://github.com/simplex-chat/simplex-chat | 新增 |
| 8 | `interviewstreet/hiring-agent` | 4692 | 903 | Python | 3,861 stars this month | 用于评估和评分简历的AI代理。 | https://github.com/interviewstreet/hiring-agent | 新增 |
| 9 | `phuryn/pm-skills` | 22494 | 2258 | — | 10,626 stars this month | PM Skills Marketplace ： 100多种代理技能、命令和插件—从发现到战略、执行、发布和增长。 | https://github.com/phuryn/pm-skills |  |
| 10 | `asgeirtj/system_prompts_leaks` | 48919 | 7982 | JavaScript | 7,399 stars this month | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT 5.5 Thinking ， GPT 5.5 Instant ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 11 | `ogulcancelik/herdr` | 11439 | 669 | Rust | 6,930 stars this month | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 12 | `stablyai/orca` | 12028 | 806 | TypeScript | 7,802 stars this month | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 13 | `n0-computer/iroh` | 11088 | 514 | Rust | 2,434 stars this month | IP地址中断，改为拨号键。将QUIC + NAT遍历添加到您的应用程序的库。 | https://github.com/n0-computer/iroh |  |
| 14 | `usestrix/strix` | 36044 | 3655 | Python | 9,853 stars this month | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix | 新增 |
| 15 | `roboflow/supervision` | 46675 | 4151 | Python | 6,762 stars this month | 我们为您编写可重复使用的计算机视觉工具。 💜 | https://github.com/roboflow/supervision |  |
| 16 | `openai/plugins` | 4028 | 466 | JavaScript | 2,652 stars this month | OpenAI插件 | https://github.com/openai/plugins |  |
| 17 | `t8y2/dbx` | 8584 | 730 | Rust | 4,933 stars this month | 15MB, lightweight, cross-platform database client. Supports MySQL, PostgreSQL, SQLite, Redis, MongoDB, DuckDB, ClickHouse, SQL Server and more.15MB，轻量级跨平台数据库客户端、数据库管理工具。支持 MySQL、PostgreSQL、SQLite、Redis、MongoDB、DuckDB、ClickHouse、SQL Server 等。 | https://github.com/t8y2/dbx |  |
| 18 | `lfnovo/open-notebook` | 34821 | 3871 | TypeScript | 10,499 stars this month | 笔记本LM的开源实现，具有更大的灵活性和功能 | https://github.com/lfnovo/open-notebook |  |
| 19 | `Leonxlnx/taste-skill` | 56490 | 3867 | JavaScript | 23,500 stars this month | 品味技能-让您的人工智能有良好的品味。阻止人工智能产生无聊的通用斜坡 | https://github.com/Leonxlnx/taste-skill |  |
| 20 | `mukul975/Anthropic-Cybersecurity-Skills` | 24401 | 2778 | Python | 10,382 stars this month | 人工智能代理的817种结构化网络安全技能·映射到6个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF和MITRE F3 （打击欺诈） · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20 + p…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills | 新增 |


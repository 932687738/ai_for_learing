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

**最近一次更新时间**（Asia/Shanghai）： 2026-07-10 09:09:20

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 523833 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 483447 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 451391 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 448388 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 391538 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 382357 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 359952 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 356884 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 355652 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 307245 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
| 11 | `awesome-selfhosted/awesome-selfhosted` | 303934 | 可自行部署的各类自由软件网络服务与 Web 应用清单。 | https://github.com/awesome-selfhosted/awesome-selfhosted |  |
| 12 | `996icu/996.ICU` | 276361 | 倡议关注「996」工作制、计数星标与交流的开发社区仓库（含网络迷因用语）。 | https://github.com/996icu/996.ICU |  |
| 13 | `practical-tutorials/project-based-learning` | 272563 | 基于项目的教程精选列表 | https://github.com/practical-tutorials/project-based-learning |  |
| 14 | `obra/superpowers` | 246876 | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers |  |
| 15 | `react/react` | 246311 | 用于Web和本机用户界面的库。 | https://github.com/react/react |  |
| 16 | `facebook/react` | 245279 | 用于构建 Web 与原生用户界面的 React 视图库（含多端生态）。 | https://github.com/facebook/react |  |
| 17 | `torvalds/linux` | 238531 | Linux内核源树 | https://github.com/torvalds/linux |  |
| 18 | `vuejs/vue` | 209989 | 这是Vue 2的存储库。如需了解VUE 3 ，请访问https://github.com/vuejs/core | https://github.com/vuejs/vue |  |
| 19 | `n8n-io/n8n` | 195721 | 具有原生AI功能的公平代码工作流程自动化平台。将视觉构建与自定义代码、自托管或云、400多个集成相结合。 | https://github.com/n8n-io/n8n |  |
| 20 | `microsoft/vscode` | 187216 | Visual Studio Code | https://github.com/microsoft/vscode |  |

---
## Trending 页面快照（HTML 抓取）

**说明**：与上方「全局 Star Search」数据源不同；本段按 GitHub trending 页的 **daily / weekly / monthly** 各拉一页并解析。**若前端改版导致选择器失效，需更新解析逻辑。**

- **标记**列：三个 `since` 子表**各自独立**对照本次拉取前文件中该小节表格已出现的 `owner/repo`；新出现的行标 **新增**。下次拉取会先清空上一轮「新增」再重算（只保留相对**上一版文件**的新仓库）。

### 今日 trending（since=daily）

**页面**： `https://github.com/trending?since=daily`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `MadsLorentzen/ai-job-search` | 19029 | 5502 | TypeScript | 3,716 stars today | 基于Claude Code构建的人工智能工作申请框架。分叉，填写您的个人资料，让Claude评估工作，定制简历，写求职信，并为面试做好准备。 | https://github.com/MadsLorentzen/ai-job-search |  |
| 2 | `SmartlyDressedGames/U3-SDK` | 2033 | 258 | C# | 524 stars today | Unturned的源代码，这是一款免费的开放世界僵尸生存沙盒游戏。 | https://github.com/SmartlyDressedGames/U3-SDK |  |
| 3 | `addyosmani/agent-skills` | 75877 | 8163 | JavaScript | 2,554 stars today | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 4 | `VoltAgent/awesome-design-md` | 99697 | 11574 | — | 1,391 stars today | 由流行品牌设计系统进行的DESIGN.md文件分析的集合。将一个放入您的项目中，让编码代理生成匹配的UI。 | https://github.com/VoltAgent/awesome-design-md |  |
| 5 | `iOfficeAI/OfficeCLI` | 13438 | 915 | C# | 1,929 stars today | OfficeCLI是第一个也是最好的Office套件，专为AI代理读取、编辑和自动化Word、Excel和PowerPoint文件而构建。免费、开源、单一二进制文件，无需安装Office。 | https://github.com/iOfficeAI/OfficeCLI |  |
| 6 | `wonderwhy-er/DesktopCommanderMCP` | 6576 | 781 | TypeScript | 185 stars today | 这是Claude的MCP服务器，具有终端控制、文件系统搜索和diff文件编辑功能 | https://github.com/wonderwhy-er/DesktopCommanderMCP |  |
| 7 | `anthropics/claude-cookbooks` | 47161 | 5555 | Jupyter Notebook | 194 stars today | 一系列笔记本/食谱，展示了一些有趣而有效的使用Claude的方法。 | https://github.com/anthropics/claude-cookbooks |  |
| 8 | `vxcontrol/pentagi` | 19406 | 2621 | Go | 535 stars today | 完全自主的AI Agents系统，能够执行复杂的渗透测试任务 | https://github.com/vxcontrol/pentagi |  |
| 9 | `unclecode/crawl4ai` | 71826 | 7378 | Python | 215 stars today | 🚀🤖 Crawl4AI ：开源LLM友好的网络爬虫和爬虫。不要害羞，在这里加入： https://discord.gg/jP8KfhDhyN | https://github.com/unclecode/crawl4ai |  |
| 10 | `imthenachoman/How-To-Secure-A-Linux-Server` | 29089 | 1938 | — | 243 stars today | 不断发展的Linux服务器安全操作指南。 | https://github.com/imthenachoman/How-To-Secure-A-Linux-Server |  |
| 11 | `huxingyi/autoremesher` | 2370 | 172 | C++ | 403 stars today | 自动四边形重新网格化工具 | https://github.com/huxingyi/autoremesher |  |
| 12 | `bradautomates/claude-video` | 6707 | 770 | Python | 718 stars today | 让Claude能够观看任何视频。/观看下载、提取帧、转录，并将所有内容交给Claude。 | https://github.com/bradautomates/claude-video |  |
| 13 | `prisma/prisma` | 46904 | 2329 | TypeScript | 376 stars today | 适用于Node.js和TypeScript的下一代ORM · PostgreSQL、MySQL、MariaDB、SQL Server、SQLite、MongoDB和CockroachDB | https://github.com/prisma/prisma |  |
| 14 | `kyutai-labs/pocket-tts` | 6984 | 702 | Python | 235 stars today | 适合计划工作站（和口袋）的TTS | https://github.com/kyutai-labs/pocket-tts |  |
| 15 | `asgeirtj/system_prompts_leaks` | 55159 | 9012 | JavaScript | 1,125 stars today | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT 5.5 Thinking ， GPT 5.5 Instant ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `MadsLorentzen/ai-job-search` | 19030 | 5502 | TypeScript | 13,847 stars this week | 基于Claude Code构建的人工智能工作申请框架。分叉，填写您的个人资料，让Claude评估工作，定制简历，写求职信，并为面试做好准备。 | https://github.com/MadsLorentzen/ai-job-search |  |
| 2 | `Zackriya-Solutions/meetily` | 22206 | 2231 | Rust | 8,885 stars this week | 隐私第一，基于Rust构建的人工智能会议助手，具有4倍的Parakeet/Whisper实时转录、扬声器日记和Ollama摘要。100%本地处理。无需云。Meetily （ Meetly Ai - https://meetily.ai ）是首屈一指的自托管、开源Ai会议...... | https://github.com/Zackriya-Solutions/meetily |  |
| 3 | `usestrix/strix` | 39624 | 4059 | Python | 8,370 stars this week | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 4 | `facebook/astryx` | 7474 | 518 | TypeScript | 4,087 stars this week | 完全可定制和代理就绪的开源设计系统 | https://github.com/facebook/astryx |  |
| 5 | `asgeirtj/system_prompts_leaks` | 55159 | 9012 | JavaScript | 7,149 stars this week | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT 5.5 Thinking ， GPT 5.5 Instant ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 6 | `openai/codex-plugin-cc` | 27166 | 1665 | JavaScript | 4,792 stars this week | 使用Claude Code的Codex来查看代码或委派任务。 | https://github.com/openai/codex-plugin-cc |  |
| 7 | `ogulcancelik/herdr` | 14824 | 870 | Rust | 4,756 stars this week | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 8 | `alibaba/page-agent` | 25520 | 2238 | TypeScript | 4,459 stars this week | JavaScript页面内GUI代理。使用自然语言控制Web界面。 | https://github.com/alibaba/page-agent |  |
| 9 | `diegosouzapw/OmniRoute` | 14323 | 2120 | TypeScript | 4,119 stars this week | 永不停止编码。免费AI网关：一个端点， 231多家提供商（ 50多家免费） ，将Claude Code、Codex、Cursor、Cline和Copilot连接到免费的Claude/GPT/Gemini。RTK + Caveman堆叠压缩可节省15-95%的代币、智能自动回退、MCP/A2A、多模式API、桌面/PWA。 | https://github.com/diegosouzapw/OmniRoute |  |
| 10 | `bradautomates/claude-video` | 6707 | 770 | Python | 3,630 stars this week | 让Claude能够观看任何视频。/观看下载、提取帧、转录，并将所有内容交给Claude。 | https://github.com/bradautomates/claude-video |  |
| 11 | `TencentCloud/CubeSandbox` | 9339 | 800 | Rust | 2,284 stars this week | 适用于人工智能代理的即时、并发、安全和轻量级沙盒。 | https://github.com/TencentCloud/CubeSandbox |  |
| 12 | `dotnet/skills` | 4491 | 330 | C# | 886 stars this week | 用于使用.NET和C #协助AI编码代理的技能的存储库 | https://github.com/dotnet/skills |  |
| 13 | `stablyai/orca` | 15083 | 1051 | TypeScript | 4,111 stars this week | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 14 | `huggingface/speech-to-speech` | 5838 | 724 | Python | 788 stars this week | 使用开源模型构建本地语音代理 | https://github.com/huggingface/speech-to-speech |  |
| 15 | `harvard-edge/cs249r_book` | 27247 | 3271 | Python | 1,969 stars this week | 机器学习系统 | https://github.com/harvard-edge/cs249r_book |  |
| 16 | `xbtlin/ai-berkshire` | 12347 | 1653 | Python | 3,757 stars this week | AI 时代的伯克希尔：基于 Claude Code / Codex 的价值投资研究框架。巴菲特·芒格·段永平·李录四大师方法论 + 多Agent并行研究。· AI-era Berkshire: a value investing research framework built for Claude Code / Codex. 4 masters' methodologies + multi-agent adversarial analysis. | https://github.com/xbtlin/ai-berkshire |  |
| 17 | `ruvnet/RuView` | 79675 | 10719 | Rust | 3,537 stars this week | π RuView将商用WiFi信号转化为实时空间智能、生命体征监测和存在检测--所有这些都无需一个像素的视频。 | https://github.com/ruvnet/RuView |  |
| 18 | `saadeghi/daisyui` | 41531 | 1649 | Svelte | 261 stars this week | 🌼 🌼 🌼 🌼 🌼 最受欢迎、免费和开源的Tailwind CSS组件库 | https://github.com/saadeghi/daisyui |  |
| 19 | `immich-app/immich` | 107101 | 6147 | TypeScript | 2,194 stars this week | 高性能自托管照片和视频管理解决方案。 | https://github.com/immich-app/immich |  |
| 20 | `steipete/CodexBar` | 17364 | 1416 | Swift | 1,679 stars this week | 显示OpenAI Codex和Claude Code的使用统计信息，无需登录。 | https://github.com/steipete/CodexBar |  |
| 21 | `browser-use/video-use` | 16268 | 1913 | Python | 2,645 stars this week | 使用编码代理编辑视频 | https://github.com/browser-use/video-use |  |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `DeusData/codebase-memory-mcp` | 29167 | 2202 | C | 26,040 stars this month | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 2 | `calesthio/OpenMontage` | 36167 | 4230 | Python | 31,648 stars this month | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 3 | `Panniantong/Agent-Reach` | 53880 | 4349 | Python | 28,801 stars this month | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 4 | `NVIDIA/SkillSpector` | 12624 | 1043 | Python | 10,971 stars this month | 人工智能代理技能的安全扫描仪。检测漏洞、恶意模式和安全风险。 | https://github.com/NVIDIA/SkillSpector |  |
| 5 | `asgeirtj/system_prompts_leaks` | 55159 | 9012 | JavaScript | 13,616 stars this month | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT 5.5 Thinking ， GPT 5.5 Instant ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 6 | `MadsLorentzen/ai-job-search` | 19030 | 5502 | TypeScript | 14,585 stars this month | 基于Claude Code构建的人工智能工作申请框架。分叉，填写您的个人资料，让Claude评估工作，定制简历，写求职信，并为面试做好准备。 | https://github.com/MadsLorentzen/ai-job-search |  |
| 7 | `apple/container` | 47310 | 1471 | Swift | 20,582 stars this month | 用于在Mac上使用轻量级虚拟机创建和运行Linux容器的工具。它是用Swift编写的，并针对Apple芯片进行了优化。 | https://github.com/apple/container |  |
| 8 | `iptv-org/iptv` | 131781 | 7371 | TypeScript | 14,536 stars this month | 收集来自世界各地的公开IPTV频道 | https://github.com/iptv-org/iptv |  |
| 9 | `ogulcancelik/herdr` | 14824 | 870 | Rust | 9,607 stars this month | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 10 | `simplex-chat/simplex-chat` | 18226 | 1108 | Haskell | 7,111 stars this month | SimpleX -第一个没有任何类型用户标识符的消息传递网络-设计为100 ％私有！ iOS ， Android和桌面应用程序📱！ | https://github.com/simplex-chat/simplex-chat |  |
| 11 | `usestrix/strix` | 39624 | 4059 | Python | 13,697 stars this month | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 12 | `alibaba/zvec` | 14651 | 906 | C++ | 4,912 stars this month | 轻量级、快如闪电的进程内矢量数据库 | https://github.com/alibaba/zvec |  |
| 13 | `stablyai/orca` | 15083 | 1051 | TypeScript | 10,439 stars this month | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 14 | `Zackriya-Solutions/meetily` | 22206 | 2231 | Rust | 9,534 stars this month | 隐私第一，基于Rust构建的人工智能会议助手，具有4倍的Parakeet/Whisper实时转录、扬声器日记和Ollama摘要。100%本地处理。无需云。Meetily （ Meetly Ai - https://meetily.ai ）是首屈一指的自托管、开源Ai会议...... | https://github.com/Zackriya-Solutions/meetily |  |
| 15 | `interviewstreet/hiring-agent` | 5322 | 1003 | Python | 4,239 stars this month | 用于评估和评分简历的AI代理。 | https://github.com/interviewstreet/hiring-agent |  |
| 16 | `alibaba/page-agent` | 25520 | 2238 | TypeScript | 7,146 stars this month | JavaScript页面内GUI代理。使用自然语言控制Web界面。 | https://github.com/alibaba/page-agent |  |
| 17 | `n0-computer/iroh` | 11302 | 559 | Rust | 2,617 stars this month | IP地址中断，改为拨号键。将QUIC + NAT遍历添加到您的应用程序的库。 | https://github.com/n0-computer/iroh |  |
| 18 | `diegosouzapw/OmniRoute` | 14323 | 2120 | TypeScript | 8,325 stars this month | 永不停止编码。免费AI网关：一个端点， 231多家提供商（ 50多家免费） ，将Claude Code、Codex、Cursor、Cline和Copilot连接到免费的Claude/GPT/Gemini。RTK + Caveman堆叠压缩可节省15-95%的代币、智能自动回退、MCP/A2A、多模式API、桌面/PWA。 | https://github.com/diegosouzapw/OmniRoute |  |
| 19 | `phuryn/pm-skills` | 23242 | 2358 | — | 10,042 stars this month | PM Skills Marketplace ： 100多种代理技能、命令和插件—从发现到战略、执行、发布和增长。 | https://github.com/phuryn/pm-skills |  |
| 20 | `mauriceboe/TREK` | 9749 | 843 | TypeScript | 4,177 stars this month | 自托管行程/行程规划工具，提供实时协作、互动地图、PWA支持、SSO、预算、装箱单等功能。 | https://github.com/mauriceboe/TREK |  |
| 21 | `ZhuLinsen/daily_stock_analysis` | 56232 | 48389 | Python | 14,989 stars this month | LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。 LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs. | https://github.com/ZhuLinsen/daily_stock_analysis |  |
| 22 | `JCodesMore/ai-website-cloner-template` | 27197 | 3870 | TypeScript | 10,636 stars this month | 使用AI编码代理，只需一个命令即可克隆任何网站 | https://github.com/JCodesMore/ai-website-cloner-template |  |
| 23 | `t8y2/dbx` | 9460 | 841 | Rust | 4,945 stars this month | 20MB, lightweight, cross-platform database client. Supports MySQL, PostgreSQL, SQLite, Redis, MongoDB, DuckDB, ClickHouse, SQL Server and more.20MB，轻量级跨平台数据库客户端、数据库管理工具。支持 MySQL、PostgreSQL、SQLite、Redis、MongoDB、DuckDB、ClickHouse、SQL Server 等。 | https://github.com/t8y2/dbx |  |


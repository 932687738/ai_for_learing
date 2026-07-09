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

**最近一次更新时间**（Asia/Shanghai）： 2026-07-09 09:12:58

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 523318 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 483148 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 451253 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 448090 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 391486 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 382104 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 359618 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 356605 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 355406 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 307049 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
| 11 | `awesome-selfhosted/awesome-selfhosted` | 303934 | 可自行部署的各类自由软件网络服务与 Web 应用清单。 | https://github.com/awesome-selfhosted/awesome-selfhosted |  |
| 12 | `996icu/996.ICU` | 276361 | 倡议关注「996」工作制、计数星标与交流的开发社区仓库（含网络迷因用语）。 | https://github.com/996icu/996.ICU |  |
| 13 | `practical-tutorials/project-based-learning` | 272563 | 基于项目的教程精选列表 | https://github.com/practical-tutorials/project-based-learning |  |
| 14 | `obra/superpowers` | 246876 | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers |  |
| 15 | `react/react` | 246311 | 用于Web和本机用户界面的库。 | https://github.com/react/react | 新增 |
| 16 | `facebook/react` | 245279 | 用于构建 Web 与原生用户界面的 React 视图库（含多端生态）。 | https://github.com/facebook/react |  |
| 17 | `torvalds/linux` | 238531 | Linux内核源树 | https://github.com/torvalds/linux |  |
| 18 | `vuejs/vue` | 209989 | 这是Vue 2的存储库。如需了解VUE 3 ，请访问https://github.com/vuejs/core | https://github.com/vuejs/vue | 新增 |
| 19 | `n8n-io/n8n` | 195721 | 具有原生AI功能的公平代码工作流程自动化平台。将视觉构建与自定义代码、自托管或云、400多个集成相结合。 | https://github.com/n8n-io/n8n | 新增 |
| 20 | `microsoft/vscode` | 187216 | Visual Studio Code | https://github.com/microsoft/vscode | 新增 |

---
## Trending 页面快照（HTML 抓取）

**说明**：与上方「全局 Star Search」数据源不同；本段按 GitHub trending 页的 **daily / weekly / monthly** 各拉一页并解析。**若前端改版导致选择器失效，需更新解析逻辑。**

- **标记**列：三个 `since` 子表**各自独立**对照本次拉取前文件中该小节表格已出现的 `owner/repo`；新出现的行标 **新增**。下次拉取会先清空上一轮「新增」再重算（只保留相对**上一版文件**的新仓库）。

### 今日 trending（since=daily）

**页面**： `https://github.com/trending?since=daily`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `addyosmani/agent-skills` | 74105 | 7992 | JavaScript | 1,297 stars today | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 2 | `ruvnet/RuView` | 79148 | 10648 | Rust | 799 stars today | π RuView将商用WiFi信号转化为实时空间智能、生命体征监测和存在检测--所有这些都无需一个像素的视频。 | https://github.com/ruvnet/RuView |  |
| 3 | `TencentCloud/TencentDB-Agent-Memory` | 7654 | 708 | TypeScript | 318 stars today | TencentDB Agent Memory通过4层渐进式管道为AI Agent提供完全本地化的长期内存，无外部API依赖。 | https://github.com/TencentCloud/TencentDB-Agent-Memory | 新增 |
| 4 | `prisma/prisma` | 46557 | 2280 | TypeScript | 46 stars today | 适用于Node.js和TypeScript的下一代ORM · PostgreSQL、MySQL、MariaDB、SQL Server、SQLite、MongoDB和CockroachDB | https://github.com/prisma/prisma | 新增 |
| 5 | `mvanhorn/last30days-skill` | 50757 | 4237 | Python | 352 stars today | 人工智能代理技能，研究Reddit、X、YouTube、HN、Polymarket和网络上的任何主题，然后合成基础摘要 | https://github.com/mvanhorn/last30days-skill | 新增 |
| 6 | `argoproj/argo-cd` | 23434 | 7425 | Go | 29 stars today | Kubernetes的声明式持续部署 | https://github.com/argoproj/argo-cd | 新增 |
| 7 | `iOfficeAI/OfficeCLI` | 11856 | 806 | C# | 1,717 stars today | OfficeCLI是第一个也是最好的Office套件，专为AI代理读取、编辑和自动化Word、Excel和PowerPoint文件而构建。免费、开源、单一二进制文件，无需安装Office。 | https://github.com/iOfficeAI/OfficeCLI |  |
| 8 | `asgeirtj/system_prompts_leaks` | 54209 | 8825 | JavaScript | 1,218 stars today | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT 5.5 Thinking ， GPT 5.5 Instant ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 9 | `obra/superpowers` | 249823 | 22166 | Shell | 1,116 stars today | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers | 新增 |
| 10 | `alibaba/zvec` | 14412 | 888 | C++ | 395 stars today | 轻量级、快如闪电的进程内矢量数据库 | https://github.com/alibaba/zvec | 新增 |
| 11 | `Diolinux/PhotoGIMP` | 15038 | 595 | CSS | 1,125 stars today | 适用于Photoshop用户的GIMP 3 +修补程序 | https://github.com/Diolinux/PhotoGIMP | 新增 |
| 12 | `wonderwhy-er/DesktopCommanderMCP` | 6379 | 749 | TypeScript | 28 stars today | 这是Claude的MCP服务器，具有终端控制、文件系统搜索和diff文件编辑功能 | https://github.com/wonderwhy-er/DesktopCommanderMCP | 新增 |
| 13 | `huxingyi/autoremesher` | 2017 | 153 | C++ | 296 stars today | 自动四边形重新网格化工具 | https://github.com/huxingyi/autoremesher | 新增 |
| 14 | `bradautomates/claude-video` | 6061 | 722 | Python | 951 stars today | 让Claude能够观看任何视频。/观看下载、提取帧、转录，并将所有内容交给Claude。 | https://github.com/bradautomates/claude-video |  |
| 15 | `TencentCloud/CubeSandbox` | 8933 | 737 | Rust | 564 stars today | 适用于人工智能代理的即时、并发、安全和轻量级沙盒。 | https://github.com/TencentCloud/CubeSandbox |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `Zackriya-Solutions/meetily` | 21657 | 2162 | Rust | 8,366 stars this week | 隐私第一，基于Rust构建的人工智能会议助手，具有4倍的Parakeet/Whisper实时转录、扬声器日记和Ollama摘要。100%本地处理。无需云。Meetily （ Meetly Ai - https://meetily.ai ）是首屈一指的自托管、开源Ai会议...... | https://github.com/Zackriya-Solutions/meetily |  |
| 2 | `usestrix/strix` | 39074 | 3967 | Python | 10,274 stars this week | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 3 | `facebook/astryx` | 7180 | 471 | TypeScript | 4,943 stars this week | 完全可定制和代理就绪的开源设计系统 | https://github.com/facebook/astryx | 新增 |
| 4 | `openai/codex-plugin-cc` | 26920 | 1622 | JavaScript | 4,890 stars this week | 使用Claude Code的Codex来查看代码或委派任务。 | https://github.com/openai/codex-plugin-cc |  |
| 5 | `alibaba/page-agent` | 25219 | 2163 | TypeScript | 4,295 stars this week | JavaScript页面内GUI代理。使用自然语言控制Web界面。 | https://github.com/alibaba/page-agent |  |
| 6 | `ogulcancelik/herdr` | 14393 | 825 | Rust | 4,754 stars this week | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 7 | `diegosouzapw/OmniRoute` | 13775 | 2005 | TypeScript | 4,424 stars this week | 永不停止编码。免费AI网关：一个端点， 231多家提供商（ 50多家免费） ，将Claude Code、Codex、Cursor、Cline和Copilot连接到免费的Claude/GPT/Gemini。RTK + Caveman堆叠压缩可节省15-95%的代币、智能自动回退、MCP/A2A、多模式API、桌面/PWA。 | https://github.com/diegosouzapw/OmniRoute |  |
| 8 | `asgeirtj/system_prompts_leaks` | 54209 | 8825 | JavaScript | 6,182 stars this week | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT 5.5 Thinking ， GPT 5.5 Instant ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 9 | `TencentCloud/CubeSandbox` | 8933 | 737 | Rust | 2,106 stars this week | 适用于人工智能代理的即时、并发、安全和轻量级沙盒。 | https://github.com/TencentCloud/CubeSandbox |  |
| 10 | `huggingface/speech-to-speech` | 5710 | 687 | Python | 736 stars this week | 使用开源模型构建本地语音代理 | https://github.com/huggingface/speech-to-speech |  |
| 11 | `dotnet/skills` | 4429 | 328 | C# | 840 stars this week | 用于使用.NET和C #协助AI编码代理的技能的存储库 | https://github.com/dotnet/skills |  |
| 12 | `bradautomates/claude-video` | 6061 | 722 | Python | 2,903 stars this week | 让Claude能够观看任何视频。/观看下载、提取帧、转录，并将所有内容交给Claude。 | https://github.com/bradautomates/claude-video | 新增 |
| 13 | `hasaneyldrm/exercises-dataset` | 11052 | 1248 | HTML | 3,028 stars this week | 1,324个运动健身数据集—动画GIF、180 × 180缩略图、肌肉群和设备数据，以及6种语言的分步说明。LogPress应用程序背后的运动数据层。 | https://github.com/hasaneyldrm/exercises-dataset |  |
| 14 | `immich-app/immich` | 106935 | 6131 | TypeScript | 2,099 stars this week | 高性能自托管照片和视频管理解决方案。 | https://github.com/immich-app/immich |  |
| 15 | `altic-dev/FluidVoice` | 6894 | 430 | Swift | 1,563 stars this week | 具有设备上STT和定制训练的人工智能增强模型的最快且唯一的macOS听写应用程序。本地Wispr Flow替代方案。⭐帮助大量:) Windows和iOS等待名单打开。Linux即将推出。 | https://github.com/altic-dev/FluidVoice |  |
| 16 | `JuliusBrussee/caveman` | 86832 | 4859 | JavaScript | 8,080 stars this week | 🪨 为什么在很少令牌欺骗时使用许多令牌— Claude Code技能通过像穴居人一样说话来削减65 ％的令牌 | https://github.com/JuliusBrussee/caveman |  |
| 17 | `msitarzewski/agency-agents` | 129318 | 21020 | Shell | 7,364 stars this week | 一个完整的人工智能机构，触手可及--从前端向导到Reddit社区忍者，从奇思妙想的注入者到现实检查者。每位客服代表都是具有个性、流程和经过验证的交付成果的专家。 | https://github.com/msitarzewski/agency-agents |  |
| 18 | `xbtlin/ai-berkshire` | 12031 | 1577 | Python | 3,960 stars this week | AI 时代的伯克希尔：基于 Claude Code / Codex 的价值投资研究框架。巴菲特·芒格·段永平·李录四大师方法论 + 多Agent并行研究。· AI-era Berkshire: a value investing research framework built for Claude Code / Codex. 4 masters' methodologies + multi-agent adversarial analysis. | https://github.com/xbtlin/ai-berkshire |  |
| 19 | `stablyai/orca` | 14228 | 960 | TypeScript | 3,953 stars this week | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 20 | `ChromeDevTools/chrome-devtools-mcp` | 46389 | 3025 | TypeScript | 1,547 stars this week | 适用于编码代理的Chrome开发者工具 | https://github.com/ChromeDevTools/chrome-devtools-mcp |  |
| 21 | `alirezarezvani/claude-skills` | 21708 | 2903 | Python | 2,068 stars this week | 345 Claude Code技能和代理技能和插件（ 30多个代理、70多个自定义命令、330多个技能、可定制的参考、脚本） ，适用于Claude Code、Codex、Gemini CLI、Cursor和其他8个编码代理—工程、营销、产品、合规、C级咨询、研究…… | https://github.com/alirezarezvani/claude-skills | 新增 |
| 22 | `browser-use/video-use` | 16071 | 1858 | Python | 3,054 stars this week | 使用编码代理编辑视频 | https://github.com/browser-use/video-use |  |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `DeusData/codebase-memory-mcp` | 28621 | 2130 | C | 25,432 stars this month | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 2 | `apple/container` | 47160 | 1428 | Swift | 20,483 stars this month | 用于在Mac上使用轻量级虚拟机创建和运行Linux容器的工具。它是用Swift编写的，并针对Apple芯片进行了优化。 | https://github.com/apple/container |  |
| 3 | `calesthio/OpenMontage` | 35663 | 4129 | Python | 31,078 stars this month | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 4 | `NVIDIA/SkillSpector` | 12502 | 1028 | Python | 11,135 stars this month | 人工智能代理技能的安全扫描仪。检测漏洞、恶意模式和安全风险。 | https://github.com/NVIDIA/SkillSpector |  |
| 5 | `Panniantong/Agent-Reach` | 53256 | 4267 | Python | 29,819 stars this month | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 6 | `asgeirtj/system_prompts_leaks` | 54209 | 8825 | JavaScript | 12,446 stars this month | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT 5.5 Thinking ， GPT 5.5 Instant ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 7 | `iptv-org/iptv` | 131278 | 7310 | TypeScript | 14,144 stars this month | 收集来自世界各地的公开IPTV频道 | https://github.com/iptv-org/iptv |  |
| 8 | `simplex-chat/simplex-chat` | 18150 | 1075 | Haskell | 7,042 stars this month | SimpleX -第一个没有任何类型用户标识符的消息传递网络-设计为100 ％私有！ iOS ， Android和桌面应用程序📱！ | https://github.com/simplex-chat/simplex-chat |  |
| 9 | `ogulcancelik/herdr` | 14393 | 825 | Rust | 9,114 stars this month | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 10 | `usestrix/strix` | 39074 | 3967 | Python | 13,169 stars this month | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 11 | `alibaba/zvec` | 14413 | 888 | C++ | 4,505 stars this month | 轻量级、快如闪电的进程内矢量数据库 | https://github.com/alibaba/zvec |  |
| 12 | `interviewstreet/hiring-agent` | 5207 | 960 | Python | 4,145 stars this month | 用于评估和评分简历的AI代理。 | https://github.com/interviewstreet/hiring-agent |  |
| 13 | `stablyai/orca` | 14228 | 960 | TypeScript | 9,594 stars this month | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 14 | `Zackriya-Solutions/meetily` | 21658 | 2162 | Rust | 8,898 stars this month | 隐私第一，基于Rust构建的人工智能会议助手，具有4倍的Parakeet/Whisper实时转录、扬声器日记和Ollama摘要。100%本地处理。无需云。Meetily （ Meetly Ai - https://meetily.ai ）是首屈一指的自托管、开源Ai会议...... | https://github.com/Zackriya-Solutions/meetily |  |
| 15 | `phuryn/pm-skills` | 23059 | 2316 | — | 10,758 stars this month | PM Skills Marketplace ： 100多种代理技能、命令和插件—从发现到战略、执行、发布和增长。 | https://github.com/phuryn/pm-skills |  |
| 16 | `alibaba/page-agent` | 25219 | 2163 | TypeScript | 6,860 stars this month | JavaScript页面内GUI代理。使用自然语言控制Web界面。 | https://github.com/alibaba/page-agent |  |
| 17 | `n0-computer/iroh` | 11247 | 522 | Rust | 2,584 stars this month | IP地址中断，改为拨号键。将QUIC + NAT遍历添加到您的应用程序的库。 | https://github.com/n0-computer/iroh |  |
| 18 | `diegosouzapw/OmniRoute` | 13776 | 2005 | TypeScript | 7,718 stars this month | 永不停止编码。免费AI网关：一个端点， 231多家提供商（ 50多家免费） ，将Claude Code、Codex、Cursor、Cline和Copilot连接到免费的Claude/GPT/Gemini。RTK + Caveman堆叠压缩可节省15-95%的代币、智能自动回退、MCP/A2A、多模式API、桌面/PWA。 | https://github.com/diegosouzapw/OmniRoute | 新增 |
| 19 | `ZhuLinsen/daily_stock_analysis` | 55902 | 48185 | Python | 14,822 stars this month | LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。 LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs. | https://github.com/ZhuLinsen/daily_stock_analysis |  |
| 20 | `t8y2/dbx` | 9284 | 793 | Rust | 5,013 stars this month | 20MB, lightweight, cross-platform database client. Supports MySQL, PostgreSQL, SQLite, Redis, MongoDB, DuckDB, ClickHouse, SQL Server and more.20MB，轻量级跨平台数据库客户端、数据库管理工具。支持 MySQL、PostgreSQL、SQLite、Redis、MongoDB、DuckDB、ClickHouse、SQL Server 等。 | https://github.com/t8y2/dbx |  |
| 21 | `mauriceboe/TREK` | 9610 | 794 | TypeScript | 4,067 stars this month | 自托管行程/行程规划工具，提供实时协作、互动地图、PWA支持、SSO、预算、装箱单等功能。 | https://github.com/mauriceboe/TREK | 新增 |
| 22 | `JCodesMore/ai-website-cloner-template` | 26812 | 3799 | TypeScript | 10,241 stars this month | 使用AI编码代理，只需一个命令即可克隆任何网站 | https://github.com/JCodesMore/ai-website-cloner-template | 新增 |


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

**最近一次更新时间**（Asia/Shanghai）： 2026-07-14 09:10:46

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 524878 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 484643 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 451717 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 449741 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 392020 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 382837 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 8 | `nilbuild/developer-roadmap` | 360770 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 9 | `donnemartin/system-design-primer` | 357457 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 10 | `jwasham/coding-interview-university` | 356125 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 11 | `vinta/awesome-python` | 307966 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
| 12 | `awesome-selfhosted/awesome-selfhosted` | 303934 | 可自行部署的各类自由软件网络服务与 Web 应用清单。 | https://github.com/awesome-selfhosted/awesome-selfhosted |  |
| 13 | `996icu/996.ICU` | 276361 | 倡议关注「996」工作制、计数星标与交流的开发社区仓库（含网络迷因用语）。 | https://github.com/996icu/996.ICU |  |
| 14 | `practical-tutorials/project-based-learning` | 272563 | 基于项目的教程精选列表 | https://github.com/practical-tutorials/project-based-learning |  |
| 15 | `obra/superpowers` | 246876 | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers |  |
| 16 | `react/react` | 246311 | 用于Web和本机用户界面的库。 | https://github.com/react/react |  |
| 17 | `facebook/react` | 245279 | 用于构建 Web 与原生用户界面的 React 视图库（含多端生态）。 | https://github.com/facebook/react |  |
| 18 | `torvalds/linux` | 238531 | Linux内核源树 | https://github.com/torvalds/linux |  |
| 19 | `vuejs/vue` | 209989 | 这是Vue 2的存储库。如需了解VUE 3 ，请访问https://github.com/vuejs/core | https://github.com/vuejs/vue |  |
| 20 | `n8n-io/n8n` | 195721 | 具有原生AI功能的公平代码工作流程自动化平台。将视觉构建与自定义代码、自托管或云、400多个集成相结合。 | https://github.com/n8n-io/n8n |  |
| 21 | `microsoft/vscode` | 187216 | Visual Studio Code | https://github.com/microsoft/vscode |  |

---
## Trending 页面快照（HTML 抓取）

**说明**：与上方「全局 Star Search」数据源不同；本段按 GitHub trending 页的 **daily / weekly / monthly** 各拉一页并解析。**若前端改版导致选择器失效，需更新解析逻辑。**

- **标记**列：三个 `since` 子表**各自独立**对照本次拉取前文件中该小节表格已出现的 `owner/repo`；新出现的行标 **新增**。下次拉取会先清空上一轮「新增」再重算（只保留相对**上一版文件**的新仓库）。

### 今日 trending（since=daily）

**页面**： `https://github.com/trending?since=daily`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `OpenCut-app/OpenCut` | 66373 | 6989 | TypeScript | 1,229 stars today | 开源CapCut替代方案 | https://github.com/OpenCut-app/OpenCut | 新增 |
| 2 | `HKUDS/Vibe-Trading` | 21755 | 3755 | Python | 1,153 stars today | “Vibe-Trading ：您的个人交易代理” | https://github.com/HKUDS/Vibe-Trading |  |
| 3 | `moeru-ai/airi` | 41875 | 4194 | TypeScript | 78 stars today | 💖🧸 自我托管，你拥有的Grok Companion ，一个包含外府灵魂的容器，将它们带入我们的世界的网络生活，希望达到Neuro-sama的高度。能够实时语音聊天、Minecraft、Factorio播放。支持Web/macOS/Windows。 | https://github.com/moeru-ai/airi | 新增 |
| 4 | `Shubhamsaboo/awesome-llm-apps` | 119620 | 17739 | Python | 996 stars today | 100多个AI Agent和RAG应用程序，您可以实际运行—克隆、自定义、发货。 | https://github.com/Shubhamsaboo/awesome-llm-apps |  |
| 5 | `Nutlope/hallmark` | 5153 | 271 | CSS | 794 stars today | Claude Code、Cursor和Codex的防AI倾斜设计技能。 | https://github.com/Nutlope/hallmark |  |
| 6 | `Raphire/Win11Debloat` | 50873 | 2049 | PowerShell | 118 stars today | 一个简单、轻量级的PowerShell脚本，允许您删除预安装的应用程序、禁用遥测以及执行各种其他更改来整理和自定义Windows体验。Win11Debloat适用于Windows 10和Windows 11。 | https://github.com/Raphire/Win11Debloat | 新增 |
| 7 | `Graphify-Labs/graphify` | 84731 | 8344 | Python | 1,095 stars today | AI编码助理技能（ Claude Code、Codex、OpenCode、Cursor、Gemini CLI等）。将任何代码、SQL架构、R脚本、shell脚本、文档、论文、图像或视频文件夹转换为可查询的知识图。一个图形中的应用代码+数据库架构+基础设施。 | https://github.com/Graphify-Labs/graphify | 新增 |
| 8 | `hasaneyldrm/exercises-dataset` | 12624 | 1482 | HTML | 451 stars today | 1,324个运动健身数据集—动画GIF、180 × 180缩略图、肌肉群和设备数据，以及6种语言的分步说明。LogPress应用程序背后的运动数据层。 | https://github.com/hasaneyldrm/exercises-dataset | 新增 |
| 9 | `github/spec-kit` | 120594 | 10694 | Python | 543 stars today | 帮助您开始规格驱动开发💫的工具包 | https://github.com/github/spec-kit | 新增 |
| 10 | `coreyhaines31/marketingskills` | 38571 | 6162 | JavaScript | 299 stars today | Claude Code和人工智能代理的营销技能。CRO、文案撰写、搜索引擎优化、分析和增长工程。 | https://github.com/coreyhaines31/marketingskills | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `wonderwhy-er/DesktopCommanderMCP` | 8182 | 997 | TypeScript | 1,939 stars this week | 这是Claude的MCP服务器，具有终端控制、文件系统搜索和diff文件编辑功能 | https://github.com/wonderwhy-er/DesktopCommanderMCP |  |
| 2 | `abseil/abseil-cpp` | 17965 | 3217 | C++ | 621 stars this week | Abseil通用库（ C + + ） | https://github.com/abseil/abseil-cpp |  |
| 3 | `Zackriya-Solutions/meetily` | 24189 | 2533 | Rust | 5,392 stars this week | 隐私第一，基于Rust构建的人工智能会议助手，具有4倍的Parakeet/Whisper实时转录、扬声器日记和Ollama摘要。100%本地处理。无需云。Meetily （ Meetly Ai - https://meetily.ai ）是首屈一指的自托管、开源Ai会议...... | https://github.com/Zackriya-Solutions/meetily |  |
| 4 | `TencentCloud/CubeSandbox` | 9992 | 982 | Rust | 2,367 stars this week | 适用于人工智能代理的即时、并发、安全和轻量级沙盒。 | https://github.com/TencentCloud/CubeSandbox |  |
| 5 | `openai/codex-plugin-cc` | 28405 | 1867 | JavaScript | 2,265 stars this week | 使用Claude Code的Codex来查看代码或委派任务。 | https://github.com/openai/codex-plugin-cc |  |
| 6 | `ogulcancelik/herdr` | 16139 | 1092 | Rust | 3,449 stars this week | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 7 | `iOfficeAI/OfficeCLI` | 16128 | 1091 | C# | 7,596 stars this week | OfficeCLI是第一个也是最好的Office套件，专为AI代理读取、编辑和自动化Word、Excel和PowerPoint文件而构建。免费、开源、单一二进制文件，无需安装Office。 | https://github.com/iOfficeAI/OfficeCLI |  |
| 8 | `diegosouzapw/OmniRoute` | 16875 | 2553 | TypeScript | 4,345 stars this week | 永不停止编码。免费AI网关：一个端点， 231多家提供商（ 50多家免费） ，将Claude Code、Codex、Cursor、Cline和Copilot连接到免费的Claude/GPT/Gemini。RTK + Caveman堆叠压缩可节省15-95%的代币、智能自动回退、MCP/A2A、多模式API、桌面/PWA。 | https://github.com/diegosouzapw/OmniRoute |  |
| 9 | `asgeirtj/system_prompts_leaks` | 57305 | 9478 | JavaScript | 6,284 stars this week | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT GPT-5.6、Codex GPT-5.6、GPT-5.5。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 10 | `bradautomates/claude-video` | 8141 | 896 | Python | 4,128 stars this week | 让Claude能够观看任何视频。/观看下载、提取帧、转录，并将所有内容交给Claude。 | https://github.com/bradautomates/claude-video |  |
| 11 | `stablyai/orca` | 18294 | 1445 | TypeScript | 5,263 stars this week | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 12 | `tt-a1i/archify` | 4219 | 391 | JavaScript | 1,333 stars this week | 任何代理技能：使用暗/亮主题切换和PNG/JPEG/WebP/SVG导出生成漂亮的架构图 | https://github.com/tt-a1i/archify |  |
| 13 | `facebook/astryx` | 8701 | 727 | TypeScript | 2,255 stars this week | 完全可定制和代理就绪的开源设计系统 | https://github.com/facebook/astryx |  |
| 14 | `usestrix/strix` | 41212 | 4339 | Python | 3,403 stars this week | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 15 | `alibaba/page-agent` | 26445 | 2424 | TypeScript | 1,950 stars this week | JavaScript页面内GUI代理。使用自然语言控制Web界面。 | https://github.com/alibaba/page-agent |  |
| 16 | `ruvnet/RuView` | 80481 | 10835 | Rust | 3,403 stars this week | π RuView将商用WiFi信号转化为实时空间智能、生命体征监测和存在检测--所有这些都无需一个像素的视频。 | https://github.com/ruvnet/RuView |  |
| 17 | `vxcontrol/pentagi` | 20409 | 2705 | Go | 2,199 stars this week | 完全自主的AI Agents系统，能够执行复杂的渗透测试任务 | https://github.com/vxcontrol/pentagi |  |
| 18 | `argoproj/argo-cd` | 23675 | 7613 | Go | 342 stars this week | Kubernetes的声明式持续部署 | https://github.com/argoproj/argo-cd | 新增 |
| 19 | `pbakaus/impeccable` | 46358 | 2804 | JavaScript | 2,450 stars this week | 让您的人工智能更好地进行设计的设计语言。 | https://github.com/pbakaus/impeccable |  |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `calesthio/OpenMontage` | 38036 | 4595 | Python | 33,392 stars this month | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 2 | `DeusData/codebase-memory-mcp` | 31120 | 2483 | C | 27,660 stars this month | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 3 | `GoogleCloudPlatform/knowledge-catalog` | 6885 | 563 | HTML | 6,484 stars this month | Google Cloud知识目录工具和示例 | https://github.com/GoogleCloudPlatform/knowledge-catalog | 新增 |
| 4 | `asgeirtj/system_prompts_leaks` | 57305 | 9478 | JavaScript | 15,390 stars this month | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT GPT-5.6、Codex GPT-5.6、GPT-5.5。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 5 | `Panniantong/Agent-Reach` | 55781 | 4605 | Python | 28,900 stars this month | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 6 | `catchorg/Catch2` | 21289 | 3447 | C++ | 887 stars this month | 用于单元测试、TDD和BDD的现代C + +原生测试框架-使用C + +14、C + +17及更高版本（ C + +11支持v2.x分支， C + +03支持Catch1.x分支） | https://github.com/catchorg/Catch2 | 新增 |
| 7 | `usestrix/strix` | 41212 | 4339 | Python | 15,337 stars this month | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 8 | `kunchenguid/no-mistakes` | 6121 | 545 | Go | 4,819 stars this month | git push no-mistakes | https://github.com/kunchenguid/no-mistakes |  |
| 9 | `ogulcancelik/herdr` | 16139 | 1092 | Rust | 10,569 stars this month | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 10 | `stablyai/orca` | 18294 | 1445 | TypeScript | 13,222 stars this month | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 11 | `Zackriya-Solutions/meetily` | 24190 | 2533 | Rust | 11,340 stars this month | 隐私第一，基于Rust构建的人工智能会议助手，具有4倍的Parakeet/Whisper实时转录、扬声器日记和Ollama摘要。100%本地处理。无需云。Meetily （ Meetly Ai - https://meetily.ai ）是首屈一指的自托管、开源Ai会议...... | https://github.com/Zackriya-Solutions/meetily |  |
| 12 | `interviewstreet/hiring-agent` | 5761 | 1143 | Python | 4,624 stars this month | 用于评估和评分简历的AI代理。 | https://github.com/interviewstreet/hiring-agent |  |
| 13 | `diegosouzapw/OmniRoute` | 16875 | 2553 | TypeScript | 10,603 stars this month | 永不停止编码。免费AI网关：一个端点， 231多家提供商（ 50多家免费） ，将Claude Code、Codex、Cursor、Cline和Copilot连接到免费的Claude/GPT/Gemini。RTK + Caveman堆叠压缩可节省15-95%的代币、智能自动回退、MCP/A2A、多模式API、桌面/PWA。 | https://github.com/diegosouzapw/OmniRoute |  |
| 14 | `alibaba/page-agent` | 26445 | 2424 | TypeScript | 8,001 stars this month | JavaScript页面内GUI代理。使用自然语言控制Web界面。 | https://github.com/alibaba/page-agent |  |
| 15 | `simplex-chat/simplex-chat` | 18577 | 1251 | Haskell | 7,461 stars this month | SimpleX -第一个没有任何类型用户标识符的消息传递网络-设计为100 ％私有！ iOS ， Android和桌面应用程序📱！ | https://github.com/simplex-chat/simplex-chat |  |
| 16 | `n0-computer/iroh` | 11665 | 681 | Rust | 2,981 stars this month | IP地址中断，改为拨号键。将QUIC + NAT遍历添加到您的应用程序的库。 | https://github.com/n0-computer/iroh |  |
| 17 | `gabime/spdlog` | 29196 | 5328 | C++ | 322 stars this month | 快速C + +日志记录库。 | https://github.com/gabime/spdlog |  |
| 18 | `iptv-org/iptv` | 132815 | 7576 | TypeScript | 14,736 stars this month | 收集来自世界各地的公开IPTV频道 | https://github.com/iptv-org/iptv |  |
| 19 | `ocornut/imgui` | 74599 | 12005 | C++ | 875 stars this month | 尊敬的ImGui ：无臃肿的C + +图形用户界面，依赖关系最少 | https://github.com/ocornut/imgui |  |
| 20 | `topoteretes/cognee` | 27778 | 2751 | Python | 10,013 stars this month | Cognee是面向智能体的开源AI内存平台。使用自托管知识图表引擎，为您的人工智能代理提供跨会话的持久长期记忆。 | https://github.com/topoteretes/cognee |  |


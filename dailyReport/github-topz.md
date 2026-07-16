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

**最近一次更新时间**（Asia/Shanghai）： 2026-07-16 09:16:46

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 525615 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 485381 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 451995 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 450477 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 392206 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 383046 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 361123 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 9 | `donnemartin/system-design-primer` | 357742 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 10 | `jwasham/coding-interview-university` | 356306 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 11 | `vinta/awesome-python` | 308369 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `OpenCut-app/OpenCut` | 71779 | 7354 | TypeScript | 1,664 stars today | 开源CapCut替代方案 | https://github.com/OpenCut-app/OpenCut |  |
| 2 | `Nutlope/hallmark` | 8544 | 442 | CSS | 1,277 stars today | Claude Code、Cursor和Codex的防AI倾斜设计技能。 | https://github.com/Nutlope/hallmark |  |
| 3 | `mattpocock/skills` | 172298 | 14795 | Shell | 2,130 stars today | 真正工程师的技能。直接来自我的.claude目录。 | https://github.com/mattpocock/skills |  |
| 4 | `moeru-ai/airi` | 42507 | 4252 | TypeScript | 110 stars today | 💖🧸 自我托管，你拥有的Grok Companion ，一个包含外府灵魂的容器，将它们带入我们的世界的网络生活，希望达到Neuro-sama的高度。能够实时语音聊天、Minecraft、Factorio播放。支持Web/macOS/Windows。 | https://github.com/moeru-ai/airi |  |
| 5 | `Dicklesworthstone/destructive_command_guard` | 4767 | 178 | Rust | 471 stars today | 破坏性命令防护(dcg)用于阻止代理执行危险的git和shell命令。 | https://github.com/Dicklesworthstone/destructive_command_guard |  |
| 6 | `HKUDS/Vibe-Trading` | 23709 | 4038 | Python | 915 stars today | “Vibe-Trading ：您的个人交易代理” | https://github.com/HKUDS/Vibe-Trading |  |
| 7 | `openinterpreter/openinterpreter` | 65491 | 5654 | Rust | 299 stars today | 低成本车型的编码代理 | https://github.com/openinterpreter/openinterpreter |  |
| 8 | `HKUDS/DeepTutor` | 26271 | 3565 | Python | 172 stars today | DeepTutor ：终身个性化辅导。https://deeptutor.info/。 | https://github.com/HKUDS/DeepTutor |  |
| 9 | `HenryNdubuaku/maths-cs-ai-compendium` | 5903 | 742 | TypeScript | 725 stars today | 成为一名破解的人工智能/机器学习研究工程师 | https://github.com/HenryNdubuaku/maths-cs-ai-compendium |  |
| 10 | `Shubhamsaboo/awesome-llm-apps` | 121921 | 17994 | Python | 1,236 stars today | 100多个AI Agent和RAG应用程序，您可以实际运行—克隆、自定义、发货。 | https://github.com/Shubhamsaboo/awesome-llm-apps |  |
| 11 | `coreyhaines31/marketingskills` | 39769 | 6316 | JavaScript | 340 stars today | Claude Code和人工智能代理的营销技能。CRO、文案撰写、搜索引擎优化、分析和增长工程。 | https://github.com/coreyhaines31/marketingskills |  |
| 12 | `YimMenu/YimMenuV2` | 1426 | 355 | C++ | 38 stars today | 《侠盗猎车手5 ：强化版》实验菜单 | https://github.com/YimMenu/YimMenuV2 |  |
| 13 | `hasaneyldrm/exercises-dataset` | 14382 | 1726 | HTML | 949 stars today | 1,324个运动健身数据集—动画GIF、180 × 180缩略图、肌肉群和设备数据，以及6种语言的分步说明。LogPress应用程序背后的运动数据层。 | https://github.com/hasaneyldrm/exercises-dataset |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `wonderwhy-er/DesktopCommanderMCP` | 8337 | 1007 | TypeScript | 2,055 stars this week | 这是Claude的MCP服务器，具有终端控制、文件系统搜索和diff文件编辑功能 | https://github.com/wonderwhy-er/DesktopCommanderMCP |  |
| 2 | `google-labs-code/stitch-skills` | 7447 | 977 | TypeScript | 992 stars this week | 专为与Stitch MCP服务器配合使用而设计的代理技能库。每项技能都遵循Agent Skills开放标准，与Antigravity、Gemini CLI、Claude Code、Cursor等编码代理兼容。 | https://github.com/google-labs-code/stitch-skills |  |
| 3 | `abseil/abseil-cpp` | 18002 | 3224 | C++ | 648 stars this week | Abseil通用库（ C + + ） | https://github.com/abseil/abseil-cpp |  |
| 4 | `iOfficeAI/OfficeCLI` | 17768 | 1177 | C# | 6,374 stars this week | OfficeCLI是第一个也是最好的Office套件，专为AI代理读取、编辑和自动化Word、Excel和PowerPoint文件而构建。免费、开源、单一二进制文件，无需安装Office。 | https://github.com/iOfficeAI/OfficeCLI |  |
| 5 | `stablyai/orca` | 19909 | 1553 | TypeScript | 5,777 stars this week | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 6 | `chriskohlhoff/asio` | 6183 | 1511 | C++ | 247 stars this week | Asio C + +库 | https://github.com/chriskohlhoff/asio |  |
| 7 | `HKUDS/Vibe-Trading` | 23709 | 4038 | Python | 4,802 stars this week | “Vibe-Trading ：您的个人交易代理” | https://github.com/HKUDS/Vibe-Trading |  |
| 8 | `Nutlope/hallmark` | 8545 | 442 | CSS | 3,551 stars this week | Claude Code、Cursor和Codex的防AI倾斜设计技能。 | https://github.com/Nutlope/hallmark |  |
| 9 | `oven-sh/bun` | 94783 | 4977 | Rust | 1,291 stars this week | 令人难以置信的快速JavaScript运行时、捆绑程序、测试运行程序和包管理器–所有功能于一身 | https://github.com/oven-sh/bun |  |
| 10 | `tt-a1i/archify` | 5148 | 436 | JavaScript | 1,840 stars this week | 任何代理技能：使用暗/亮主题切换和PNG/JPEG/WebP/SVG导出生成漂亮的架构图 | https://github.com/tt-a1i/archify |  |
| 11 | `openai/codex-plugin-cc` | 28828 | 1895 | JavaScript | 1,998 stars this week | 使用Claude Code的Codex来查看代码或委派任务。 | https://github.com/openai/codex-plugin-cc |  |
| 12 | `diegosouzapw/OmniRoute` | 17752 | 2648 | TypeScript | 4,149 stars this week | 永不停止编码。免费AI网关：一个端点， 231多家提供商（ 50多家免费） ，将Claude Code、Codex、Cursor、Cline和Copilot连接到免费的Claude/GPT/Gemini。RTK + Caveman堆叠压缩可节省15-95%的代币、智能自动回退、MCP/A2A、多模式API、桌面/PWA。 | https://github.com/diegosouzapw/OmniRoute |  |
| 13 | `ogulcancelik/herdr` | 16844 | 1140 | Rust | 2,636 stars this week | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 14 | `TencentCloud/CubeSandbox` | 10296 | 997 | Rust | 1,545 stars this week | 适用于人工智能代理的即时、并发、安全和轻量级沙盒。 | https://github.com/TencentCloud/CubeSandbox |  |
| 15 | `Shubhamsaboo/awesome-llm-apps` | 121921 | 17994 | Python | 4,902 stars this week | 100多个AI Agent和RAG应用程序，您可以实际运行—克隆、自定义、发货。 | https://github.com/Shubhamsaboo/awesome-llm-apps |  |
| 16 | `pbakaus/impeccable` | 47055 | 2826 | JavaScript | 2,428 stars this week | 让您的人工智能更好地进行设计的设计语言。 | https://github.com/pbakaus/impeccable |  |
| 17 | `OpenCut-app/OpenCut` | 71782 | 7354 | TypeScript | 8,702 stars this week | 开源CapCut替代方案 | https://github.com/OpenCut-app/OpenCut |  |
| 18 | `davila7/claude-code-templates` | 29559 | 3243 | Python | 1,052 stars this week | 用于配置和监控Claude Code的CLI工具 | https://github.com/davila7/claude-code-templates |  |
| 19 | `anthropics/claude-cookbooks` | 48964 | 5802 | Jupyter Notebook | 2,252 stars this week | 一系列笔记本/食谱，展示了一些有趣而有效的使用Claude的方法。 | https://github.com/anthropics/claude-cookbooks |  |
| 20 | `Zackriya-Solutions/meetily` | 24977 | 2611 | Rust | 3,499 stars this week | 隐私第一，基于Rust构建的人工智能会议助手，具有4倍的Parakeet/Whisper实时转录、扬声器日记和Ollama摘要。100%本地处理。无需云。Meetily （ Meetly Ai - https://meetily.ai ）是首屈一指的自托管、开源Ai会议...... | https://github.com/Zackriya-Solutions/meetily |  |
| 21 | `actions/checkout` | 8514 | 2722 | TypeScript | 181 stars this week | 签出仓库的操作 | https://github.com/actions/checkout |  |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `calesthio/OpenMontage` | 38950 | 4715 | Python | 34,298 stars this month | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 2 | `DeusData/codebase-memory-mcp` | 31866 | 2543 | C | 28,343 stars this month | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 3 | `catchorg/Catch2` | 21299 | 3449 | C++ | 908 stars this month | 用于单元测试、TDD和BDD的现代C + +原生测试框架-使用C + +14、C + +17及更高版本（ C + +11支持v2.x分支， C + +03支持Catch1.x分支） | https://github.com/catchorg/Catch2 |  |
| 4 | `asgeirtj/system_prompts_leaks` | 58114 | 9606 | JavaScript | 15,928 stars this month | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT GPT-5.6、Codex GPT-5.6、GPT-5.5。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 5 | `kunchenguid/no-mistakes` | 6311 | 557 | Go | 4,964 stars this month | git push no-mistakes | https://github.com/kunchenguid/no-mistakes |  |
| 6 | `usestrix/strix` | 41865 | 4398 | Python | 15,974 stars this month | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 7 | `Panniantong/Agent-Reach` | 56807 | 4671 | Python | 27,531 stars this month | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 8 | `stablyai/orca` | 19910 | 1553 | TypeScript | 14,890 stars this month | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 9 | `ogulcancelik/herdr` | 16844 | 1140 | Rust | 11,079 stars this month | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 10 | `Zackriya-Solutions/meetily` | 24977 | 2611 | Rust | 12,267 stars this month | 隐私第一，基于Rust构建的人工智能会议助手，具有4倍的Parakeet/Whisper实时转录、扬声器日记和Ollama摘要。100%本地处理。无需云。Meetily （ Meetly Ai - https://meetily.ai ）是首屈一指的自托管、开源Ai会议...... | https://github.com/Zackriya-Solutions/meetily |  |
| 11 | `diegosouzapw/OmniRoute` | 17752 | 2648 | TypeScript | 11,484 stars this month | 永不停止编码。免费AI网关：一个端点， 231多家提供商（ 50多家免费） ，将Claude Code、Codex、Cursor、Cline和Copilot连接到免费的Claude/GPT/Gemini。RTK + Caveman堆叠压缩可节省15-95%的代币、智能自动回退、MCP/A2A、多模式API、桌面/PWA。 | https://github.com/diegosouzapw/OmniRoute |  |
| 12 | `gabime/spdlog` | 29233 | 5330 | C++ | 357 stars this month | 快速C + +日志记录库。 | https://github.com/gabime/spdlog |  |
| 13 | `alibaba/page-agent` | 26756 | 2460 | TypeScript | 8,322 stars this month | JavaScript页面内GUI代理。使用自然语言控制Web界面。 | https://github.com/alibaba/page-agent |  |
| 14 | `GoogleCloudPlatform/knowledge-catalog` | 7133 | 582 | HTML | 5,364 stars this month | Google Cloud知识目录工具和示例 | https://github.com/GoogleCloudPlatform/knowledge-catalog |  |
| 15 | `interviewstreet/hiring-agent` | 5930 | 1172 | Python | 4,793 stars this month | 用于评估和评分简历的AI代理。 | https://github.com/interviewstreet/hiring-agent |  |
| 16 | `simplex-chat/simplex-chat` | 18680 | 1264 | Haskell | 7,565 stars this month | SimpleX -第一个没有任何类型用户标识符的消息传递网络-设计为100 ％私有！ iOS ， Android和桌面应用程序📱！ | https://github.com/simplex-chat/simplex-chat |  |
| 17 | `ocornut/imgui` | 74705 | 12012 | C++ | 954 stars this month | 尊敬的ImGui ：无臃肿的C + +图形用户界面，依赖关系最少 | https://github.com/ocornut/imgui |  |
| 18 | `wonderwhy-er/DesktopCommanderMCP` | 8337 | 1007 | TypeScript | 2,199 stars this month | 这是Claude的MCP服务器，具有终端控制、文件系统搜索和diff文件编辑功能 | https://github.com/wonderwhy-er/DesktopCommanderMCP |  |
| 19 | `n0-computer/iroh` | 11747 | 695 | Rust | 3,068 stars this month | IP地址中断，改为拨号键。将QUIC + NAT遍历添加到您的应用程序的库。 | https://github.com/n0-computer/iroh |  |
| 20 | `OpenCut-app/OpenCut` | 71782 | 7354 | TypeScript | 14,882 stars this month | 开源CapCut替代方案 | https://github.com/OpenCut-app/OpenCut |  |


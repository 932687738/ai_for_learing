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

**最近一次更新时间**（Asia/Shanghai）： 2026-07-18 08:09:22

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 527323 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 486134 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 451971 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 451003 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 392339 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 383292 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 361360 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 9 | `donnemartin/system-design-primer` | 357998 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 10 | `jwasham/coding-interview-university` | 356482 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 11 | `vinta/awesome-python` | 308747 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `codecrafters-io/build-your-own-x` | 527323 | 49903 | Markdown | 1,068 stars today | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `PostHog/posthog` | 36179 | 3010 | Python | 438 stars today | 🦔 PostHog是构建自动驾驶产品的领先平台。我们的开发人员工具–人工智能可观察性、分析、会话重播、标记、实验、错误跟踪、日志等–捕获代理诊断问题、发现机会和发布所需的所有上下文…… | https://github.com/PostHog/posthog |  |
| 3 | `HenryNdubuaku/maths-cs-ai-compendium` | 6603 | 810 | TypeScript | 200 stars today | 成为一名破解的人工智能/机器学习研究工程师 | https://github.com/HenryNdubuaku/maths-cs-ai-compendium | 新增 |
| 4 | `Nutlope/hallmark` | 11993 | 601 | CSS | 1,485 stars today | Claude Code、Cursor和Codex的防AI倾斜设计技能。 | https://github.com/Nutlope/hallmark |  |
| 5 | `github/copilot-sdk` | 9790 | 1330 | Java | 233 stars today | 用于将GitHub Copilot Agent集成到应用和服务中的多平台SDK | https://github.com/github/copilot-sdk |  |
| 6 | `anthropics/cwc-workshops` | 1579 | 489 | TypeScript | 45 stars today | — | https://github.com/anthropics/cwc-workshops | 新增 |
| 7 | `PrismML-Eng/Bonsai-demo` | 1706 | 167 | Shell | 278 stars today | 盆栽演示 | https://github.com/PrismML-Eng/Bonsai-demo |  |
| 8 | `protocolbuffers/protobuf` | 71537 | 16192 | C++ | 11 stars today | 协议缓冲区- Google的数据交换格式 | https://github.com/protocolbuffers/protobuf | 新增 |
| 9 | `tirth8205/code-review-graph` | 19733 | 2106 | Python | 74 stars today | MCP和CLI的本地优先代码智能图。构建代码库的持久映射，以便AI编码工具仅读取重要内容，并对审阅和大型重构工作流进行基准上下文缩减。 | https://github.com/tirth8205/code-review-graph | 新增 |
| 10 | `docusealco/docuseal` | 17831 | 1769 | Ruby | 91 stars today | 开源DocuSign替代方案。创建、填写和签署数字文档 ✍️ | https://github.com/docusealco/docuseal | 新增 |
| 11 | `openinterpreter/openinterpreter` | 66350 | 5706 | Rust | 431 stars today | Kimi K3等开放模型的编码代理 | https://github.com/openinterpreter/openinterpreter |  |
| 12 | `RyanCodrai/turbovec` | 13293 | 1179 | Python | 280 stars today | 基于TurboQuant构建的矢量索引，用Rust和Python绑定编写 | https://github.com/RyanCodrai/turbovec | 新增 |
| 13 | `HKUDS/DeepTutor` | 27345 | 3644 | Python | 531 stars today | DeepTutor ：终身个性化辅导。https://deeptutor.info/。 | https://github.com/HKUDS/DeepTutor |  |
| 14 | `OpenCut-app/OpenCut` | 74841 | 7545 | TypeScript | 1,074 stars today | 开源CapCut替代方案 | https://github.com/OpenCut-app/OpenCut |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `Nutlope/hallmark` | 11993 | 601 | CSS | 8,075 stars this week | Claude Code、Cursor和Codex的防AI倾斜设计技能。 | https://github.com/Nutlope/hallmark |  |
| 2 | `abseil/abseil-cpp` | 17959 | 3138 | C++ | 608 stars this week | Abseil通用库（ C + + ） | https://github.com/abseil/abseil-cpp |  |
| 3 | `google-labs-code/stitch-skills` | 7612 | 893 | TypeScript | 1,076 stars this week | 专为与Stitch MCP服务器配合使用而设计的代理技能库。每项技能都遵循Agent Skills开放标准，与Antigravity、Gemini CLI、Claude Code、Cursor等编码代理兼容。 | https://github.com/google-labs-code/stitch-skills |  |
| 4 | `HKUDS/Vibe-Trading` | 24620 | 4075 | Python | 5,616 stars this week | “Vibe-Trading ：您的个人交易代理” | https://github.com/HKUDS/Vibe-Trading |  |
| 5 | `wonderwhy-er/DesktopCommanderMCP` | 8450 | 934 | TypeScript | 1,657 stars this week | 这是Claude的MCP服务器，具有终端控制、文件系统搜索和diff文件编辑功能 | https://github.com/wonderwhy-er/DesktopCommanderMCP |  |
| 6 | `OpenCut-app/OpenCut` | 74841 | 7545 | TypeScript | 12,718 stars this week | 开源CapCut替代方案 | https://github.com/OpenCut-app/OpenCut |  |
| 7 | `stablyai/orca` | 21138 | 1532 | TypeScript | 5,409 stars this week | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 8 | `Shubhamsaboo/awesome-llm-apps` | 123596 | 18215 | Python | 6,252 stars this week | 100多个AI Agent和RAG应用程序，您可以实际运行—克隆、自定义、发货。 | https://github.com/Shubhamsaboo/awesome-llm-apps |  |
| 9 | `oven-sh/bun` | 94801 | 4884 | Rust | 1,212 stars this week | 令人难以置信的快速JavaScript运行时、捆绑程序、测试运行程序和包管理器–所有功能于一身 | https://github.com/oven-sh/bun |  |
| 10 | `iOfficeAI/OfficeCLI` | 18823 | 1261 | C# | 4,611 stars this week | OfficeCLI是第一个也是最好的Office套件，专为AI代理读取、编辑和自动化Word、Excel和PowerPoint文件而构建。免费、开源、单一二进制文件，无需安装Office。 | https://github.com/iOfficeAI/OfficeCLI |  |
| 11 | `davila7/claude-code-templates` | 29681 | 3155 | Python | 1,084 stars this week | 用于配置和监控Claude Code的CLI工具 | https://github.com/davila7/claude-code-templates |  |
| 12 | `openai/codex-plugin-cc` | 29097 | 1843 | JavaScript | 1,801 stars this week | 使用Claude Code的Codex来查看代码或委派任务。 | https://github.com/openai/codex-plugin-cc |  |
| 13 | `HKUDS/DeepTutor` | 27345 | 3644 | Python | 1,801 stars this week | DeepTutor ：终身个性化辅导。https://deeptutor.info/。 | https://github.com/HKUDS/DeepTutor |  |
| 14 | `pbakaus/impeccable` | 47638 | 2759 | JavaScript | 2,331 stars this week | 让您的人工智能更好地进行设计的设计语言。 | https://github.com/pbakaus/impeccable |  |
| 15 | `kangarooking/cangjie-skill` | 3495 | 505 | Python | 1,158 stars this week | 把书、长视频、播客等高价值内容蒸馏成可执行的 Agent Skills | https://github.com/kangarooking/cangjie-skill |  |
| 16 | `diegosouzapw/OmniRoute` | 18378 | 2633 | TypeScript | 3,605 stars this week | 永不停止编码。免费AI网关：一个端点， 231多家提供商（ 50多家免费） ，将Claude Code、Codex、Cursor、Cline和Copilot连接到免费的Claude/GPT/Gemini。RTK + Caveman堆叠压缩可节省15-95%的代币、智能自动回退、MCP/A2A、多模式API、桌面/PWA。 | https://github.com/diegosouzapw/OmniRoute |  |
| 17 | `ogulcancelik/herdr` | 17642 | 1113 | Rust | 2,512 stars this week | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 18 | `actions/checkout` | 8484 | 2601 | TypeScript | 159 stars this week | 签出仓库的操作 | https://github.com/actions/checkout |  |
| 19 | `vercel-labs/native` | 6495 | 263 | Zig | 854 stars this week | 用于构建本机桌面应用的工具包 | https://github.com/vercel-labs/native | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `calesthio/OpenMontage` | 39516 | 4677 | Python | 34,748 stars this month | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 2 | `DeusData/codebase-memory-mcp` | 32429 | 2478 | C | 28,151 stars this month | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 3 | `asgeirtj/system_prompts_leaks` | 58638 | 9579 | JavaScript | 15,885 stars this month | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT GPT-5.6、Codex GPT-5.6、GPT-5.5。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 4 | `kunchenguid/no-mistakes` | 6415 | 477 | Go | 5,063 stars this month | git push no-mistakes | https://github.com/kunchenguid/no-mistakes |  |
| 5 | `usestrix/strix` | 42258 | 4359 | Python | 16,488 stars this month | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 6 | `stablyai/orca` | 21138 | 1532 | TypeScript | 16,048 stars this month | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 7 | `ogulcancelik/herdr` | 17642 | 1113 | Rust | 11,568 stars this month | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 8 | `Zackriya-Solutions/meetily` | 25286 | 2533 | Rust | 12,699 stars this month | 隐私第一，基于Rust构建的人工智能会议助手，具有4倍的Parakeet/Whisper实时转录、扬声器日记和Ollama摘要。100%本地处理。无需云。Meetily （ Meetly Ai - https://meetily.ai ）是首屈一指的自托管、开源Ai会议...... | https://github.com/Zackriya-Solutions/meetily |  |
| 9 | `diegosouzapw/OmniRoute` | 18379 | 2633 | TypeScript | 12,026 stars this month | 永不停止编码。免费AI网关：一个端点， 231多家提供商（ 50多家免费） ，将Claude Code、Codex、Cursor、Cline和Copilot连接到免费的Claude/GPT/Gemini。RTK + Caveman堆叠压缩可节省15-95%的代币、智能自动回退、MCP/A2A、多模式API、桌面/PWA。 | https://github.com/diegosouzapw/OmniRoute |  |
| 10 | `alibaba/page-agent` | 26914 | 2357 | TypeScript | 8,521 stars this month | JavaScript页面内GUI代理。使用自然语言控制Web界面。 | https://github.com/alibaba/page-agent |  |
| 11 | `Panniantong/Agent-Reach` | 57492 | 4603 | Python | 25,126 stars this month | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 12 | `interviewstreet/hiring-agent` | 6010 | 1076 | Python | 4,955 stars this month | 用于评估和评分简历的AI代理。 | https://github.com/interviewstreet/hiring-agent |  |
| 13 | `ocornut/imgui` | 74735 | 11915 | C++ | 1,007 stars this month | 尊敬的ImGui ：无臃肿的C + +图形用户界面，依赖关系最少 | https://github.com/ocornut/imgui |  |
| 14 | `simplex-chat/simplex-chat` | 18671 | 1172 | Haskell | 7,662 stars this month | SimpleX -第一个没有任何类型用户标识符的消息传递网络-设计为100 ％私有！ iOS ， Android和桌面应用程序📱！ | https://github.com/simplex-chat/simplex-chat |  |
| 15 | `BuilderIO/agent-native` | 3753 | 362 | TypeScript | 3,209 stars this month | 用于构建代理本机应用程序的框架。 | https://github.com/BuilderIO/agent-native | 新增 |
| 16 | `gabime/spdlog` | 29165 | 5248 | C++ | 391 stars this month | 快速C + +日志记录库。 | https://github.com/gabime/spdlog |  |
| 17 | `OpenCut-app/OpenCut` | 74841 | 7545 | TypeScript | 18,999 stars this month | 开源CapCut替代方案 | https://github.com/OpenCut-app/OpenCut |  |
| 18 | `iOfficeAI/OfficeCLI` | 18823 | 1261 | C# | 11,556 stars this month | OfficeCLI是第一个也是最好的Office套件，专为AI代理读取、编辑和自动化Word、Excel和PowerPoint文件而构建。免费、开源、单一二进制文件，无需安装Office。 | https://github.com/iOfficeAI/OfficeCLI |  |
| 19 | `wonderwhy-er/DesktopCommanderMCP` | 8450 | 934 | TypeScript | 2,389 stars this month | 这是Claude的MCP服务器，具有终端控制、文件系统搜索和diff文件编辑功能 | https://github.com/wonderwhy-er/DesktopCommanderMCP |  |


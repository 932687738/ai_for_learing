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

**最近一次更新时间**（Asia/Shanghai）： 2026-08-07 09:41:07

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 536887 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 493128 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 454766 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 453612 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 393890 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 385393 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 363806 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 362051 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 10 | `jwasham/coding-interview-university` | 358033 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 11 | `vinta/awesome-python` | 312584 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `TencentCloud/TencentDB-Agent-Memory` | 16438 | 1479 | TypeScript | 1,057 stars today | TencentDB Agent Memory是AI Agent的团队级内存中心—将对话、文档和代码转换为四个可重用的内存资产（ Chat Memory、Skill、LLM-Wiki、Code-Graph ） ，这些资产在代理和框架之间进行管理、共享和配备。 | https://github.com/TencentCloud/TencentDB-Agent-Memory |  |
| 2 | `addyosmani/agent-skills` | 82966 | 8896 | JavaScript | 593 stars today | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 3 | `cloudflare/computer` | 4833 | 242 | TypeScript | 2,802 stars today | 为您的代理提供一台电脑 👾 | https://github.com/cloudflare/computer |  |
| 4 | `mattpocock/skills` | 207100 | 17887 | Shell | 1,873 stars today | 真正工程师的技能。直接来自我的.agents目录。 | https://github.com/mattpocock/skills | 新增 |
| 5 | `goauthentik/authentik` | 23135 | 1774 | Python | 138 stars today | 您需要的身份验证胶水。 | https://github.com/goauthentik/authentik | 新增 |
| 6 | `huangruiteng/loopx` | 2884 | 218 | Python | 847 stars today | 适用于长期运行的AI代理团队的轻量级循环工程状态内核。跨Codex、Claude Code和其他编码代理的Agent-Loop不可知，具有持久目标、配额感知自动唤醒、可执行待办事项、证据日志和可验证的交接。 | https://github.com/huangruiteng/loopx |  |
| 7 | `google/guava` | 51642 | 11164 | Java | 13 stars today | 适用于Java的Google核心库 | https://github.com/google/guava | 新增 |
| 8 | `TapXWorld/ChinaTextbook` | 77127 | 17419 | Roff | 134 stars today | 所有小初高、大学PDF教材。 | https://github.com/TapXWorld/ChinaTextbook | 新增 |
| 9 | `Significant-Gravitas/AutoGPT` | 186020 | 46056 | Python | 37 stars today | AutoGPT的愿景是为每个人提供可访问的人工智能，供其使用并以此为基础。我们的使命是提供工具，让您专注于重要的事情。 | https://github.com/Significant-Gravitas/AutoGPT | 新增 |
| 10 | `tirth8205/code-review-graph` | 29036 | 2685 | Python | 237 stars today | MCP和CLI的本地优先代码智能图。构建代码库的持久映射，以便AI编码工具仅读取重要内容，并对审阅和大型重构工作流进行基准上下文缩减。 | https://github.com/tirth8205/code-review-graph | 新增 |
| 11 | `esengine/DeepSeek-Reasonix` | 32439 | 2099 | Go | 888 stars today | 为您的终端提供DeepSeek原生AI编码代理。围绕前缀缓存稳定性而设计—保持运行。 | https://github.com/esengine/DeepSeek-Reasonix |  |
| 12 | `obra/superpowers` | 268114 | 23964 | Shell | 858 stars today | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers |  |
| 13 | `firecrawl/pdf-inspector` | 12475 | 839 | Rust | 1,190 stars today | 用于PDF检查、分类和文本提取的快速Rust库。智能检测扫描的PDF和基于文本的PDF ，以实现智能路由决策。 | https://github.com/firecrawl/pdf-inspector |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `zhaoxuya520/reverse-skill` | 19864 | 2715 | PowerShell | 10,091 stars this week | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工… | https://github.com/zhaoxuya520/reverse-skill |  |
| 2 | `microsoft/AI-For-Beginners` | 62713 | 12185 | Jupyter Notebook | 9,164 stars this week | 12周， 24课，全民人工智能！ | https://github.com/microsoft/AI-For-Beginners |  |
| 3 | `TencentCloud/TencentDB-Agent-Memory` | 16438 | 1479 | TypeScript | 6,444 stars this week | TencentDB Agent Memory是AI Agent的团队级内存中心—将对话、文档和代码转换为四个可重用的内存资产（ Chat Memory、Skill、LLM-Wiki、Code-Graph ） ，这些资产在代理和框架之间进行管理、共享和配备。 | https://github.com/TencentCloud/TencentDB-Agent-Memory |  |
| 4 | `lyogavin/airllm` | 29643 | 3166 | Jupyter Notebook | 5,222 stars this week | 使用单个4GB GPU的AirLLM 70B推理 | https://github.com/lyogavin/airllm |  |
| 5 | `virgiliojr94/book-to-skill` | 17655 | 1888 | Python | 3,903 stars this week | 将任何技术书籍PDF转化为Claude Code技能—随时准备在您工作时进行学习、参考和使用。 | https://github.com/virgiliojr94/book-to-skill |  |
| 6 | `block/buzz` | 24275 | 2780 | Rust | 5,903 stars this week | 蜂巢思维沟通平台 | https://github.com/block/buzz |  |
| 7 | `esengine/DeepSeek-Reasonix` | 32439 | 2099 | Go | 4,203 stars this week | 为您的终端提供DeepSeek原生AI编码代理。围绕前缀缓存稳定性而设计—保持运行。 | https://github.com/esengine/DeepSeek-Reasonix |  |
| 8 | `different-ai/openwork` | 21290 | 2085 | TypeScript | 2,939 stars this week | Claude Cowork的开源替代品（由opencode提供支持） | https://github.com/different-ai/openwork |  |
| 9 | `agavra/tuicr` | 2495 | 189 | Rust | 741 stars this week | 使用vim键绑定的代码审查TUI | https://github.com/agavra/tuicr | 新增 |
| 10 | `ayghri/i-have-adhd` | 17778 | 1022 | Python | 3,628 stars this week | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 11 | `deepfakes/faceswap` | 57311 | 13502 | Python | 618 stars this week | 适用于所有人的Deepfakes软件 | https://github.com/deepfakes/faceswap | 新增 |
| 12 | `DataExpert-io/data-engineer-handbook` | 43264 | 8899 | Jupyter Notebook | 716 stars this week | 这是一个存储库，其中包含您想要了解的有关数据工程的所有内容的链接 | https://github.com/DataExpert-io/data-engineer-handbook |  |
| 13 | `antirez/ds4` | 20807 | 1858 | C | 1,319 stars this week | 适用于Metal、CUDA和ROCm的DeepSeek 4 Flash和PRO本地推理引擎 | https://github.com/antirez/ds4 | 新增 |
| 14 | `embabel/embabel-agent` | 3992 | 398 | Kotlin | 154 stars this week | JVM的代理框架。发音Em-BAY-bel/”b” l/ | https://github.com/embabel/embabel-agent | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `permissionlesstech/bitchat` | 34667 | 5531 | Swift | 8,701 stars this month | 蓝牙网状聊天， IRC共鸣 | https://github.com/permissionlesstech/bitchat |  |
| 2 | `diegosouzapw/OmniRoute` | 41734 | 5532 | TypeScript | 29,383 stars this month | 永不停止编码。免费MIT AI网关：一个端点， 290多个提供商（ 90多个免费） ， 500多个型号— Kimi ， Claude ， GPT ， OpenAI ， Gemini ， GLM ， DeepSeek ， MiniMax。适用于Claude Code、Codex、Cursor、OpenCode、Cline和Copilot。配额感知自动回退， RTK +穴居人压缩保存…… | https://github.com/diegosouzapw/OmniRoute |  |
| 3 | `stablyai/orca` | 38993 | 2750 | TypeScript | 26,353 stars this month | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面、移动和VPS上使用。 | https://github.com/stablyai/orca |  |
| 4 | `emilkowalski/skills` | 26394 | 1427 | — | 21,162 stars this month | 设计师和工程师的技能。 | https://github.com/emilkowalski/skills |  |
| 5 | `koala73/worldmonitor` | 79416 | 11872 | TypeScript | 18,274 stars this month | 实时全球智能仪表板。在统一的态势感知界面中进行人工智能驱动的新闻聚合、地缘政治监控和基础设施跟踪 | https://github.com/koala73/worldmonitor |  |
| 6 | `Nutlope/hallmark` | 22316 | 1134 | CSS | 18,764 stars this month | Claude Code、Cursor和Codex的防AI倾斜设计技能。 | https://github.com/Nutlope/hallmark |  |
| 7 | `tt-a1i/archify` | 9868 | 774 | HTML | 7,074 stars this month | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify |  |
| 8 | `huggingface/speech-to-speech` | 11437 | 1421 | Python | 6,090 stars this month | 使用开源模型构建本地语音代理 | https://github.com/huggingface/speech-to-speech |  |
| 9 | `1jehuang/jcode` | 16225 | 1822 | Rust | 8,110 stars this month | RAM效率最高的线束 | https://github.com/1jehuang/jcode |  |
| 10 | `iOfficeAI/OfficeCLI` | 26193 | 1761 | C# | 17,847 stars this month | OfficeCLI是第一个也是最好的Office套件，专为AI代理读取、编辑和自动化Word、Excel和PowerPoint文件而构建。免费、开源、单一二进制文件，无需安装Office。 | https://github.com/iOfficeAI/OfficeCLI |  |
| 11 | `wonderwhy-er/DesktopCommanderMCP` | 9233 | 1116 | TypeScript | 3,118 stars this month | 这是Claude的MCP服务器，具有终端控制、文件系统搜索和diff文件编辑功能 | https://github.com/wonderwhy-er/DesktopCommanderMCP |  |
| 12 | `HKUDS/DeepTutor` | 32758 | 4276 | Python | 7,645 stars this month | DeepTutor ：终身个性化辅导。https://deeptutor.info/。 | https://github.com/HKUDS/DeepTutor |  |
| 13 | `MadsLorentzen/ai-job-search` | 30525 | 10383 | TypeScript | 23,601 stars this month | 在您的机器上运行的作业搜索。基于Claude Code构建的人工智能求职框架：评估帖子、定制简历、撰写求职信、准备面试。分叉并拥有它。 | https://github.com/MadsLorentzen/ai-job-search |  |
| 14 | `Shubhamsaboo/awesome-llm-apps` | 131108 | 19330 | Python | 14,892 stars this month | 100多个人工智能代理、代理技能和RAG应用程序-免费开源。 | https://github.com/Shubhamsaboo/awesome-llm-apps |  |
| 15 | `OpenCut-app/OpenCut` | 81322 | 8060 | TypeScript | 20,061 stars this month | 开源CapCut替代方案 | https://github.com/OpenCut-app/OpenCut |  |
| 16 | `microsoft/AI-For-Beginners` | 62714 | 12185 | Jupyter Notebook | 10,946 stars this month | 12周， 24课，全民人工智能！ | https://github.com/microsoft/AI-For-Beginners | 新增 |
| 17 | `pbakaus/impeccable` | 56319 | 3426 | JavaScript | 12,655 stars this month | 让您的人工智能更好地进行设计的设计语言。 | https://github.com/pbakaus/impeccable |  |
| 18 | `pingdotgg/t3code` | 17030 | 3831 | TypeScript | 3,746 stars this month | — | https://github.com/pingdotgg/t3code |  |
| 19 | `every-app/open-seo` | 10749 | 1235 | TypeScript | 6,602 stars this month | Semrush和Ahrefs的开源替代品 | https://github.com/every-app/open-seo |  |
| 20 | `zhaoxuya520/reverse-skill` | 19865 | 2715 | PowerShell | 12,319 stars this month | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工… | https://github.com/zhaoxuya520/reverse-skill | 新增 |
| 21 | `HKUDS/Vibe-Trading` | 30065 | 4842 | Python | 12,134 stars this month | “Vibe-Trading ：您的个人交易代理” | https://github.com/HKUDS/Vibe-Trading |  |
| 22 | `bradautomates/claude-video` | 14288 | 1374 | Python | 10,428 stars this month | 让Claude能够观看任何视频。/观看下载、提取帧、转录，并将所有内容交给Claude。 | https://github.com/bradautomates/claude-video |  |
| 23 | `tirth8205/code-review-graph` | 29036 | 2685 | Python | 9,787 stars this month | MCP和CLI的本地优先代码智能图。构建代码库的持久映射，以便AI编码工具仅读取重要内容，并对审阅和大型重构工作流进行基准上下文缩减。 | https://github.com/tirth8205/code-review-graph |  |


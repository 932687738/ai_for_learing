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

**最近一次更新时间**（Asia/Shanghai）： 2026-08-12 10:23:15

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 538848 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 494653 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 455520 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 453833 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 394176 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 385976 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 364182 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 363241 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 10 | `jwasham/coding-interview-university` | 358410 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 11 | `vinta/awesome-python` | 313470 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `msitarzewski/agency-agents` | 143356 | 23285 | Shell | 958 stars today | 一个完整的人工智能机构，触手可及--从前端向导到Reddit社区忍者，从奇思妙想的注入者到现实检查者。每位客服代表都是具有个性、流程和经过验证的交付成果的专家。 | https://github.com/msitarzewski/agency-agents |  |
| 2 | `semantica-agi/semantica` | 4948 | 533 | Python | 893 stars today | 上下文和负责任的人工智能系统的图形原生基础设施 | https://github.com/semantica-agi/semantica |  |
| 3 | `nvm-sh/nvm` | 94495 | 10354 | Shell | 22 stars today | 节点版本管理器-兼容POSIX的bash脚本，用于管理多个活动的node.js版本 | https://github.com/nvm-sh/nvm | 新增 |
| 4 | `addyosmani/agent-skills` | 86256 | 9267 | JavaScript | 578 stars today | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 5 | `ZhuLinsen/daily_stock_analysis` | 62180 | 52452 | Python | 243 stars today | LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。 LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs. | https://github.com/ZhuLinsen/daily_stock_analysis | 新增 |
| 6 | `vitali87/code-graph-rag` | 3857 | 564 | Python | 341 stars today | 您的monorepo的终极抹布。利用人工智能和知识图谱的力量查询、理解和编辑多语言代码库 | https://github.com/vitali87/code-graph-rag |  |
| 7 | `anthropics/skills` | 168172 | 20036 | Python | 485 stars today | 座席技能的公共存储库 | https://github.com/anthropics/skills | 新增 |
| 8 | `3b1b/manim` | 90214 | 7485 | Python | 197 stars today | 解释性数学视频的动画引擎 | https://github.com/3b1b/manim | 新增 |
| 9 | `HKUDS/DeepTutor` | 34784 | 4424 | Python | 812 stars today | DeepTutor ：终身个性化辅导。https://deeptutor.info/。 | https://github.com/HKUDS/DeepTutor | 新增 |
| 10 | `stablyai/orca` | 42864 | 2983 | TypeScript | 875 stars today | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面、移动和VPS上使用。 | https://github.com/stablyai/orca | 新增 |
| 11 | `paperclipai/paperclip` | 77206 | 14256 | TypeScript | 748 stars today | 每个人都使用的开源应用程序来管理工作中的代理 | https://github.com/paperclipai/paperclip |  |
| 12 | `huggingface/transformers` | 163830 | 34204 | Python | 80 stars today | 🤗 Transformers ：用于推理和训练的文本、视觉、音频和多模态模型中最先进的机器学习模型的模型定义框架。 | https://github.com/huggingface/transformers | 新增 |
| 13 | `harveyai/harvey-labs` | 1095 | 197 | Python | 28 stars today | 旨在评估和改进客服代表支持法律工作的能力的基准。 | https://github.com/harveyai/harvey-labs | 新增 |
| 14 | `jaywcjlove/awesome-mac` | 110513 | 8419 | Swift | 298 stars today | 该项目致力于收集高质量的macOS软件，并按不同类别进行系统整理，以便于搜索和使用。 | https://github.com/jaywcjlove/awesome-mac | 新增 |
| 15 | `calesthio/OpenMontage` | 47388 | 5906 | Python | 458 stars today | 全球首个开源代理视频制作系统。12个制作管道、100多个工具、700多个代理技能和生产知识文件。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage | 新增 |
| 16 | `practical-tutorials/project-based-learning` | 278495 | 35781 | Python | 401 stars today | 基于项目的教程精选列表 | https://github.com/practical-tutorials/project-based-learning | 新增 |
| 17 | `PrimeIntellect-ai/prime-agent` | 14163 | 1461 | TypeScript | 1,138 stars today | 自我改进的RLM代理，用于编码工作流程和长期运行的自主任务。 | https://github.com/PrimeIntellect-ai/prime-agent |  |


### 本周 trending（since=weekly）

> Trending HTML 抓取或解析失败： `<urlopen error [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。>`。**since**=`weekly`。


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `diegosouzapw/OmniRoute` | 45964 | 6174 | TypeScript | 30,582 stars this month | 永不停止编码。免费MIT AI网关：一个端点， 290多个提供商（ 90多个免费） ， 500多个型号— Kimi ， Claude ， GPT ， OpenAI ， Gemini ， GLM ， DeepSeek ， MiniMax。适用于Claude Code、Codex、Cursor、OpenCode、Cline和Copilot。配额感知自动回退， RTK +穴居人压缩保存…… | https://github.com/diegosouzapw/OmniRoute |  |
| 2 | `koala73/worldmonitor` | 80841 | 12082 | TypeScript | 19,348 stars this month | 实时全球智能仪表板。在统一的态势感知界面中进行人工智能驱动的新闻聚合、地缘政治监控和基础设施跟踪 | https://github.com/koala73/worldmonitor |  |
| 3 | `Nutlope/hallmark` | 24079 | 1217 | CSS | 20,034 stars this month | Claude Code、Cursor和Codex的防AI倾斜设计技能。 | https://github.com/Nutlope/hallmark |  |
| 4 | `1jehuang/jcode` | 17210 | 1935 | Rust | 8,917 stars this month | RAM效率最高的线束 | https://github.com/1jehuang/jcode |  |
| 5 | `zhaoxuya520/reverse-skill` | 23989 | 3260 | PowerShell | 15,942 stars this month | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工… | https://github.com/zhaoxuya520/reverse-skill |  |
| 6 | `HKUDS/DeepTutor` | 34784 | 4424 | Python | 9,113 stars this month | DeepTutor ：终身个性化辅导。https://deeptutor.info/。 | https://github.com/HKUDS/DeepTutor |  |
| 7 | `stablyai/orca` | 42867 | 2983 | TypeScript | 26,440 stars this month | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面、移动和VPS上使用。 | https://github.com/stablyai/orca |  |
| 8 | `pingdotgg/t3code` | 18283 | 4153 | TypeScript | 4,753 stars this month | — | https://github.com/pingdotgg/t3code |  |
| 9 | `TencentCloud/TencentDB-Agent-Memory` | 19924 | 1798 | TypeScript | 11,445 stars this month | TencentDB Agent Memory是AI Agent的团队级内存中心—将对话、文档和代码转换为四个可重用的内存资产（ Chat Memory、Skill、LLM-Wiki、Code-Graph ） ，这些资产在代理和框架之间进行管理、共享和配备。 | https://github.com/TencentCloud/TencentDB-Agent-Memory |  |
| 10 | `mattpocock/skills` | 213908 | 18463 | Shell | 49,161 stars this month | 真正工程师的技能。直接来自我的.agents目录。 | https://github.com/mattpocock/skills |  |
| 11 | `every-app/open-seo` | 11371 | 1314 | TypeScript | 7,123 stars this month | Semrush和Ahrefs的开源替代品 | https://github.com/every-app/open-seo |  |
| 12 | `tt-a1i/archify` | 11456 | 871 | HTML | 7,913 stars this month | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify |  |
| 13 | `earendil-works/pi` | 87717 | 10901 | TypeScript | 18,096 stars this month | AI agent toolkit ：统一LLM API、agent loop、TUI、coding agent CLI | https://github.com/earendil-works/pi |  |
| 14 | `kangarooking/cangjie-skill` | 7285 | 902 | Python | 4,833 stars this month | 把书、长视频、播客等高价值内容蒸馏成可执行的 Agent Skills | https://github.com/kangarooking/cangjie-skill |  |
| 15 | `virgiliojr94/book-to-skill` | 20538 | 2174 | Python | 11,976 stars this month | 将任何技术书籍PDF转化为Claude Code技能—随时准备在您工作时进行学习、参考和使用。 | https://github.com/virgiliojr94/book-to-skill |  |
| 16 | `tirth8205/code-review-graph` | 29825 | 2729 | Python | 10,514 stars this month | MCP和CLI的本地优先代码智能图。构建代码库的持久映射，以便AI编码工具仅读取重要内容，并对审阅和大型重构工作流进行基准上下文缩减。 | https://github.com/tirth8205/code-review-graph |  |
| 17 | `huggingface/speech-to-speech` | 12276 | 1500 | Python | 6,181 stars this month | 使用开源模型构建本地语音代理 | https://github.com/huggingface/speech-to-speech |  |
| 18 | `agegr/pi-web` | 4021 | 560 | TypeScript | 2,913 stars this month | Pi编码代理的Web UI | https://github.com/agegr/pi-web |  |
| 19 | `OpenCut-app/OpenCut` | 82419 | 8141 | TypeScript | 20,621 stars this month | 开源CapCut替代方案 | https://github.com/OpenCut-app/OpenCut |  |
| 20 | `MoonshotAI/kimi-code` | 6385 | 1016 | TypeScript | 3,345 stars this month | Kimi Code CLI —新一代代理的起点 | https://github.com/MoonshotAI/kimi-code |  |
| 21 | `iOfficeAI/OfficeCLI` | 27754 | 1878 | C# | 12,907 stars this month | OfficeCLI是第一个也是最好的Office套件，专为AI代理读取、编辑和自动化Word、Excel和PowerPoint文件而构建。免费、开源、单一二进制文件，无需安装Office。 | https://github.com/iOfficeAI/OfficeCLI | 新增 |


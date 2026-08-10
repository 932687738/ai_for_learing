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

**最近一次更新时间**（Asia/Shanghai）： 2026-08-10 09:34:54

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 538132 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 494058 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 455227 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 453707 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 394041 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 385707 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 364020 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 362716 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 10 | `jwasham/coding-interview-university` | 358281 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 11 | `vinta/awesome-python` | 313100 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `PrimeIntellect-ai/prime-agent` | 11194 | 1155 | TypeScript | 2,356 stars today | 自我改进的RLM代理，用于编码工作流程和长期运行的自主任务。 | https://github.com/PrimeIntellect-ai/prime-agent | 新增 |
| 2 | `vitali87/code-graph-rag` | 3012 | 520 | Python | 96 stars today | 您的monorepo的终极抹布。利用人工智能和知识图谱的力量查询、理解和编辑多语言代码库 | https://github.com/vitali87/code-graph-rag | 新增 |
| 3 | `msitarzewski/agency-agents` | 140724 | 22984 | Shell | 858 stars today | 一个完整的人工智能机构，触手可及--从前端向导到Reddit社区忍者，从奇思妙想的注入者到现实检查者。每位客服代表都是具有个性、流程和经过验证的交付成果的专家。 | https://github.com/msitarzewski/agency-agents | 新增 |
| 4 | `pranshuparmar/witr` | 20695 | 726 | Go | 210 stars today | 为什么会出现这种情况？将任何进程、端口、容器或文件追溯到启动它的原因- CLI + TUI。 | https://github.com/pranshuparmar/witr | 新增 |
| 5 | `google-deepmind/weathernext` | 7098 | 938 | Python | 86 stars today | — | https://github.com/google-deepmind/weathernext | 新增 |
| 6 | `addyosmani/agent-skills` | 85159 | 9162 | JavaScript | 680 stars today | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 7 | `ZhuLinsen/daily_stock_analysis` | 61218 | 52003 | Python | 306 stars today | LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。 LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs. | https://github.com/ZhuLinsen/daily_stock_analysis | 新增 |
| 8 | `goauthentik/authentik` | 24286 | 1858 | Python | 310 stars today | 您需要的身份验证胶水。 | https://github.com/goauthentik/authentik |  |
| 9 | `google/skills` | 17249 | 1393 | Python | 528 stars today | Google产品和技术的代理技能 | https://github.com/google/skills | 新增 |
| 10 | `Comfy-Org/ComfyUI` | 125555 | 14845 | Python | 365 stars today | 最强大、模块化的扩散模型GUI、API和后端，具有图形/节点界面。 | https://github.com/Comfy-Org/ComfyUI | 新增 |
| 11 | `harveyai/harvey-labs` | 836 | 177 | Python | 47 stars today | 旨在评估和改进客服代表支持法律工作的能力的基准。 | https://github.com/harveyai/harvey-labs | 新增 |
| 12 | `pingdotgg/t3code` | 17669 | 4012 | TypeScript | 163 stars today | — | https://github.com/pingdotgg/t3code | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `firecrawl/pdf-inspector` | 13884 | 950 | Rust | 8,641 stars this week | 用于PDF检查、分类和文本提取的快速Rust库。智能检测扫描的PDF和基于文本的PDF ，以实现智能路由决策。 | https://github.com/firecrawl/pdf-inspector | 新增 |
| 2 | `zhaoxuya520/reverse-skill` | 22535 | 3070 | PowerShell | 9,784 stars this week | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工… | https://github.com/zhaoxuya520/reverse-skill |  |
| 3 | `TencentCloud/TencentDB-Agent-Memory` | 18784 | 1694 | TypeScript | 8,003 stars this week | TencentDB Agent Memory是AI Agent的团队级内存中心—将对话、文档和代码转换为四个可重用的内存资产（ Chat Memory、Skill、LLM-Wiki、Code-Graph ） ，这些资产在代理和框架之间进行管理、共享和配备。 | https://github.com/TencentCloud/TencentDB-Agent-Memory |  |
| 4 | `lyogavin/airllm` | 30378 | 3235 | Jupyter Notebook | 5,129 stars this week | 使用单个4GB GPU的AirLLM 70B推理 | https://github.com/lyogavin/airllm |  |
| 5 | `esengine/DeepSeek-Reasonix` | 33464 | 2164 | Go | 4,709 stars this week | 为您的终端提供DeepSeek原生AI编码代理。围绕前缀缓存稳定性而设计—保持运行。 | https://github.com/esengine/DeepSeek-Reasonix |  |
| 6 | `microsoft/AI-For-Beginners` | 64044 | 12393 | Jupyter Notebook | 5,514 stars this week | 12周， 24课，全民人工智能！ | https://github.com/microsoft/AI-For-Beginners |  |
| 7 | `usekaneo/kaneo` | 7911 | 630 | TypeScript | 1,952 stars this week | 你需要的一🎯切。没有什么你不需要的。开源项目管理适合您，而不是对您不利。 | https://github.com/usekaneo/kaneo | 新增 |
| 8 | `virgiliojr94/book-to-skill` | 19453 | 2079 | Python | 4,121 stars this week | 将任何技术书籍PDF转化为Claude Code技能—随时准备在您工作时进行学习、参考和使用。 | https://github.com/virgiliojr94/book-to-skill |  |
| 9 | `google/skills` | 17249 | 1393 | Python | 1,626 stars this week | Google产品和技术的代理技能 | https://github.com/google/skills | 新增 |
| 10 | `unclebob/swarm-forge` | 2055 | 218 | Clojure | 562 stars this week | 用于协调多个AI代理的简单工具。 | https://github.com/unclebob/swarm-forge | 新增 |
| 11 | `iv-org/invidious` | 22546 | 2515 | Crystal | 778 stars this week | Invidious是YouTube的替代前端 | https://github.com/iv-org/invidious | 新增 |
| 12 | `goauthentik/authentik` | 24286 | 1858 | Python | 1,579 stars this week | 您需要的身份验证胶水。 | https://github.com/goauthentik/authentik | 新增 |
| 13 | `Comfy-Org/ComfyUI` | 125557 | 14845 | Python | 2,018 stars this week | 最强大、模块化的扩散模型GUI、API和后端，具有图形/节点界面。 | https://github.com/Comfy-Org/ComfyUI | 新增 |
| 14 | `drawdb-io/drawdb` | 38640 | 3160 | JavaScript | 331 stars this week | 免费、简单、直观的在线数据库图编辑器和SQL生成器。 | https://github.com/drawdb-io/drawdb | 新增 |
| 15 | `vitali87/code-graph-rag` | 3012 | 520 | Python | 236 stars this week | 您的monorepo的终极抹布。利用人工智能和知识图谱的力量查询、理解和编辑多语言代码库 | https://github.com/vitali87/code-graph-rag | 新增 |
| 16 | `livekit/agents` | 12830 | 3527 | Python | 1,138 stars this week | 构建实时语音AI代理的框架 🤖🎙️📹 | https://github.com/livekit/agents | 新增 |
| 17 | `embabel/embabel-agent` | 4059 | 401 | Kotlin | 195 stars this week | JVM的代理框架。发音Em-BAY-bel/”b” l/ | https://github.com/embabel/embabel-agent |  |
| 18 | `donnemartin/system-design-primer` | 362716 | 57750 | Python | 2,724 stars this week | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `diegosouzapw/OmniRoute` | 44301 | 5956 | TypeScript | 30,114 stars this month | 永不停止编码。免费MIT AI网关：一个端点， 290多个提供商（ 90多个免费） ， 500多个型号— Kimi ， Claude ， GPT ， OpenAI ， Gemini ， GLM ， DeepSeek ， MiniMax。适用于Claude Code、Codex、Cursor、OpenCode、Cline和Copilot。配额感知自动回退， RTK +穴居人压缩保存…… | https://github.com/diegosouzapw/OmniRoute |  |
| 2 | `Nutlope/hallmark` | 23044 | 1179 | CSS | 19,383 stars this month | Claude Code、Cursor和Codex的防AI倾斜设计技能。 | https://github.com/Nutlope/hallmark |  |
| 3 | `koala73/worldmonitor` | 80206 | 11985 | TypeScript | 18,846 stars this month | 实时全球智能仪表板。在统一的态势感知界面中进行人工智能驱动的新闻聚合、地缘政治监控和基础设施跟踪 | https://github.com/koala73/worldmonitor |  |
| 4 | `1jehuang/jcode` | 16635 | 1876 | Rust | 8,441 stars this month | RAM效率最高的线束 | https://github.com/1jehuang/jcode |  |
| 5 | `stablyai/orca` | 40855 | 2865 | TypeScript | 26,197 stars this month | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面、移动和VPS上使用。 | https://github.com/stablyai/orca |  |
| 6 | `pingdotgg/t3code` | 17669 | 4012 | TypeScript | 4,164 stars this month | — | https://github.com/pingdotgg/t3code |  |
| 7 | `HKUDS/DeepTutor` | 33379 | 4316 | Python | 8,060 stars this month | DeepTutor ：终身个性化辅导。https://deeptutor.info/。 | https://github.com/HKUDS/DeepTutor |  |
| 8 | `zhaoxuya520/reverse-skill` | 22535 | 3070 | PowerShell | 14,667 stars this month | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工… | https://github.com/zhaoxuya520/reverse-skill |  |
| 9 | `microsoft/AI-For-Beginners` | 64044 | 12393 | Jupyter Notebook | 12,125 stars this month | 12周， 24课，全民人工智能！ | https://github.com/microsoft/AI-For-Beginners |  |
| 10 | `OpenCut-app/OpenCut` | 81916 | 8102 | TypeScript | 20,310 stars this month | 开源CapCut替代方案 | https://github.com/OpenCut-app/OpenCut |  |
| 11 | `every-app/open-seo` | 11116 | 1280 | TypeScript | 6,888 stars this month | Semrush和Ahrefs的开源替代品 | https://github.com/every-app/open-seo |  |
| 12 | `mattpocock/skills` | 211184 | 18259 | Shell | 49,380 stars this month | 真正工程师的技能。直接来自我的.agents目录。 | https://github.com/mattpocock/skills | 新增 |
| 13 | `tt-a1i/archify` | 10935 | 843 | HTML | 7,736 stars this month | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify |  |
| 14 | `TencentCloud/TencentDB-Agent-Memory` | 18784 | 1694 | TypeScript | 10,707 stars this month | TencentDB Agent Memory是AI Agent的团队级内存中心—将对话、文档和代码转换为四个可重用的内存资产（ Chat Memory、Skill、LLM-Wiki、Code-Graph ） ，这些资产在代理和框架之间进行管理、共享和配备。 | https://github.com/TencentCloud/TencentDB-Agent-Memory | 新增 |
| 15 | `Shubhamsaboo/awesome-llm-apps` | 131769 | 19408 | Python | 15,170 stars this month | 100多个人工智能代理、代理技能和RAG应用程序-免费开源。 | https://github.com/Shubhamsaboo/awesome-llm-apps |  |
| 16 | `earendil-works/pi` | 86033 | 10691 | TypeScript | 17,130 stars this month | AI agent toolkit ：统一LLM API、agent loop、TUI、coding agent CLI | https://github.com/earendil-works/pi | 新增 |
| 17 | `tirth8205/code-review-graph` | 29580 | 2710 | Python | 10,341 stars this month | MCP和CLI的本地优先代码智能图。构建代码库的持久映射，以便AI编码工具仅读取重要内容，并对审阅和大型重构工作流进行基准上下文缩减。 | https://github.com/tirth8205/code-review-graph |  |
| 18 | `virgiliojr94/book-to-skill` | 19453 | 2079 | Python | 10,969 stars this month | 将任何技术书籍PDF转化为Claude Code技能—随时准备在您工作时进行学习、参考和使用。 | https://github.com/virgiliojr94/book-to-skill | 新增 |
| 19 | `huggingface/speech-to-speech` | 11892 | 1463 | Python | 6,184 stars this month | 使用开源模型构建本地语音代理 | https://github.com/huggingface/speech-to-speech |  |
| 20 | `iOfficeAI/OfficeCLI` | 27102 | 1841 | C# | 14,276 stars this month | OfficeCLI是第一个也是最好的Office套件，专为AI代理读取、编辑和自动化Word、Excel和PowerPoint文件而构建。免费、开源、单一二进制文件，无需安装Office。 | https://github.com/iOfficeAI/OfficeCLI |  |
| 21 | `agegr/pi-web` | 3860 | 535 | TypeScript | 2,781 stars this month | Pi编码代理的Web UI | https://github.com/agegr/pi-web | 新增 |
| 22 | `bradautomates/claude-video` | 14764 | 1413 | Python | 8,376 stars this month | 让Claude能够观看任何视频。/观看下载、提取帧、转录，并将所有内容交给Claude。 | https://github.com/bradautomates/claude-video |  |


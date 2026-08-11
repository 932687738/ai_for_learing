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

**最近一次更新时间**（Asia/Shanghai）： 2026-08-11 09:31:07

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 538440 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 494343 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 455369 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 453764 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 394105 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 385827 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 364100 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 363000 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 10 | `jwasham/coding-interview-university` | 358350 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 11 | `vinta/awesome-python` | 313270 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `semantica-agi/semantica` | 4130 | 482 | Python | 970 stars today | 上下文和负责任的人工智能系统的图形原生基础设施 | https://github.com/semantica-agi/semantica | 新增 |
| 2 | `msitarzewski/agency-agents` | 141852 | 23136 | Shell | 1,349 stars today | 一个完整的人工智能机构，触手可及--从前端向导到Reddit社区忍者，从奇思妙想的注入者到现实检查者。每位客服代表都是具有个性、流程和经过验证的交付成果的专家。 | https://github.com/msitarzewski/agency-agents |  |
| 3 | `NanmiCoder/MediaCrawler` | 61059 | 12012 | Python | 259 stars today | 小红书笔记 · 评论爬虫、抖音视频 · 评论爬虫、快手视频 · 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖子 ｜ 百度贴吧评论回复爬虫 · 知乎问答文章｜评论爬虫 | https://github.com/NanmiCoder/MediaCrawler | 新增 |
| 4 | `addyosmani/agent-skills` | 85756 | 9229 | JavaScript | 659 stars today | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 5 | `paperclipai/paperclip` | 76516 | 14210 | TypeScript | 198 stars today | 每个人都使用的开源应用程序来管理工作中的代理 | https://github.com/paperclipai/paperclip | 新增 |
| 6 | `PrimeIntellect-ai/prime-agent` | 13100 | 1332 | TypeScript | 2,642 stars today | 自我改进的RLM代理，用于编码工作流程和长期运行的自主任务。 | https://github.com/PrimeIntellect-ai/prime-agent |  |
| 7 | `LadybirdBrowser/ladybird` | 65262 | 3120 | C++ | 56 stars today | 真正独立的网络浏览器 | https://github.com/LadybirdBrowser/ladybird | 新增 |
| 8 | `ruvnet/RuView` | 89375 | 11893 | Rust | 154 stars today | π RuView将商用WiFi信号转化为实时空间智能、生命体征监测和存在检测--所有这些都无需一个像素的视频。 | https://github.com/ruvnet/RuView | 新增 |
| 9 | `danielmiessler/LifeOS` | 17932 | 2366 | TypeScript | 315 stars today | ⛰️一般爬山AI线束，可帮助您在生活和工作中从当前状态转变为理想状态。 | https://github.com/danielmiessler/LifeOS | 新增 |
| 10 | `firecrawl/firecrawl` | 165098 | 9287 | TypeScript | 835 stars today | 用于大规模搜索、抓取和与Web交互的上下文API。 🔥 | https://github.com/firecrawl/firecrawl | 新增 |
| 11 | `TauricResearch/TradingAgents` | 97237 | 18735 | Python | 177 stars today | TradingAgent ：多代理LLM金融交易框架 | https://github.com/TauricResearch/TradingAgents | 新增 |
| 12 | `google-deepmind/weathernext` | 7359 | 954 | Python | 325 stars today | — | https://github.com/google-deepmind/weathernext |  |
| 13 | `vitali87/code-graph-rag` | 3543 | 548 | Python | 682 stars today | 您的monorepo的终极抹布。利用人工智能和知识图谱的力量查询、理解和编辑多语言代码库 | https://github.com/vitali87/code-graph-rag |  |
| 14 | `pingdotgg/t3code` | 18036 | 4077 | TypeScript | 389 stars today | — | https://github.com/pingdotgg/t3code |  |
| 15 | `Comfy-Org/ComfyUI` | 126339 | 14902 | Python | 922 stars today | 最强大、模块化的扩散模型GUI、API和后端，具有图形/节点界面。 | https://github.com/Comfy-Org/ComfyUI |  |
| 16 | `opa334/Dopamine` | 6037 | 6193 | C | 111 stars today | 多巴胺是适用于iOS 15至26 （ .0.1 ）的半无绳越狱 | https://github.com/opa334/Dopamine | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `huangruiteng/loopx` | 3961 | 316 | Python | 2,947 stars this week | 适用于长期运行的AI代理团队的轻量级循环工程状态内核。跨Codex、Claude Code和其他编码代理的Agent-Loop不可知，具有持久目标、配额感知自动唤醒、可执行待办事项、证据日志和可验证的交接。 | https://github.com/huangruiteng/loopx | 新增 |
| 2 | `firecrawl/pdf-inspector` | 14391 | 988 | Rust | 7,143 stars this week | 用于PDF检查、分类和文本提取的快速Rust库。智能检测扫描的PDF和基于文本的PDF ，以实现智能路由决策。 | https://github.com/firecrawl/pdf-inspector |  |
| 3 | `TencentCloud/TencentDB-Agent-Memory` | 19423 | 1747 | TypeScript | 7,555 stars this week | TencentDB Agent Memory是AI Agent的团队级内存中心—将对话、文档和代码转换为四个可重用的内存资产（ Chat Memory、Skill、LLM-Wiki、Code-Graph ） ，这些资产在代理和框架之间进行管理、共享和配备。 | https://github.com/TencentCloud/TencentDB-Agent-Memory |  |
| 4 | `zhaoxuya520/reverse-skill` | 23368 | 3170 | PowerShell | 8,182 stars this week | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工… | https://github.com/zhaoxuya520/reverse-skill |  |
| 5 | `esengine/DeepSeek-Reasonix` | 33730 | 2194 | Go | 4,109 stars this week | 为您的终端提供DeepSeek原生AI编码代理。围绕前缀缓存稳定性而设计—保持运行。 | https://github.com/esengine/DeepSeek-Reasonix |  |
| 6 | `lyogavin/airllm` | 30585 | 3257 | Jupyter Notebook | 4,042 stars this week | 使用单个4GB GPU的AirLLM 70B推理 | https://github.com/lyogavin/airllm |  |
| 7 | `semantica-agi/semantica` | 4131 | 482 | Python | 2,009 stars this week | 上下文和负责任的人工智能系统的图形原生基础设施 | https://github.com/semantica-agi/semantica | 新增 |
| 8 | `google/skills` | 17612 | 1406 | Python | 2,159 stars this week | Google产品和技术的代理技能 | https://github.com/google/skills |  |
| 9 | `virgiliojr94/book-to-skill` | 20034 | 2140 | Python | 4,113 stars this week | 将任何技术书籍PDF转化为Claude Code技能—随时准备在您工作时进行学习、参考和使用。 | https://github.com/virgiliojr94/book-to-skill |  |
| 10 | `unclebob/swarm-forge` | 2120 | 221 | Clojure | 627 stars this week | 用于协调多个AI代理的简单工具。 | https://github.com/unclebob/swarm-forge |  |
| 11 | `drawdb-io/drawdb` | 38762 | 3164 | JavaScript | 503 stars this week | 免费、简单、直观的在线数据库图编辑器和SQL生成器。 | https://github.com/drawdb-io/drawdb |  |
| 12 | `usekaneo/kaneo` | 8060 | 640 | TypeScript | 1,396 stars this week | 你需要的一🎯切。没有什么你不需要的。开源项目管理适合您，而不是对您不利。 | https://github.com/usekaneo/kaneo |  |
| 13 | `microsoft/AI-For-Beginners` | 64431 | 12468 | Jupyter Notebook | 4,028 stars this week | 12周， 24课，全民人工智能！ | https://github.com/microsoft/AI-For-Beginners |  |
| 14 | `Comfy-Org/ComfyUI` | 126339 | 14902 | Python | 2,842 stars this week | 最强大、模块化的扩散模型GUI、API和后端，具有图形/节点界面。 | https://github.com/Comfy-Org/ComfyUI |  |
| 15 | `vitali87/code-graph-rag` | 3543 | 548 | Python | 920 stars this week | 您的monorepo的终极抹布。利用人工智能和知识图谱的力量查询、理解和编辑多语言代码库 | https://github.com/vitali87/code-graph-rag |  |
| 16 | `goauthentik/authentik` | 24516 | 1873 | Python | 1,912 stars this week | 您需要的身份验证胶水。 | https://github.com/goauthentik/authentik |  |
| 17 | `DataExpert-io/data-engineer-handbook` | 43604 | 9093 | Jupyter Notebook | 781 stars this week | 这是一个存储库，其中包含您想要了解的有关数据工程的所有内容的链接 | https://github.com/DataExpert-io/data-engineer-handbook | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `diegosouzapw/OmniRoute` | 45209 | 6064 | TypeScript | 30,445 stars this month | 永不停止编码。免费MIT AI网关：一个端点， 290多个提供商（ 90多个免费） ， 500多个型号— Kimi ， Claude ， GPT ， OpenAI ， Gemini ， GLM ， DeepSeek ， MiniMax。适用于Claude Code、Codex、Cursor、OpenCode、Cline和Copilot。配额感知自动回退， RTK +穴居人压缩保存…… | https://github.com/diegosouzapw/OmniRoute |  |
| 2 | `Nutlope/hallmark` | 23523 | 1199 | CSS | 19,841 stars this month | Claude Code、Cursor和Codex的防AI倾斜设计技能。 | https://github.com/Nutlope/hallmark |  |
| 3 | `koala73/worldmonitor` | 80519 | 12027 | TypeScript | 19,125 stars this month | 实时全球智能仪表板。在统一的态势感知界面中进行人工智能驱动的新闻聚合、地缘政治监控和基础设施跟踪 | https://github.com/koala73/worldmonitor |  |
| 4 | `1jehuang/jcode` | 16887 | 1901 | Rust | 8,576 stars this month | RAM效率最高的线束 | https://github.com/1jehuang/jcode |  |
| 5 | `stablyai/orca` | 41796 | 2921 | TypeScript | 26,074 stars this month | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面、移动和VPS上使用。 | https://github.com/stablyai/orca |  |
| 6 | `zhaoxuya520/reverse-skill` | 23368 | 3170 | PowerShell | 15,571 stars this month | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工… | https://github.com/zhaoxuya520/reverse-skill |  |
| 7 | `pingdotgg/t3code` | 18036 | 4077 | TypeScript | 4,506 stars this month | — | https://github.com/pingdotgg/t3code |  |
| 8 | `HKUDS/DeepTutor` | 33926 | 4363 | Python | 8,346 stars this month | DeepTutor ：终身个性化辅导。https://deeptutor.info/。 | https://github.com/HKUDS/DeepTutor |  |
| 9 | `every-app/open-seo` | 11242 | 1299 | TypeScript | 7,031 stars this month | Semrush和Ahrefs的开源替代品 | https://github.com/every-app/open-seo |  |
| 10 | `mattpocock/skills` | 212601 | 18371 | Shell | 49,125 stars this month | 真正工程师的技能。直接来自我的.agents目录。 | https://github.com/mattpocock/skills |  |
| 11 | `TencentCloud/TencentDB-Agent-Memory` | 19423 | 1747 | TypeScript | 11,255 stars this month | TencentDB Agent Memory是AI Agent的团队级内存中心—将对话、文档和代码转换为四个可重用的内存资产（ Chat Memory、Skill、LLM-Wiki、Code-Graph ） ，这些资产在代理和框架之间进行管理、共享和配备。 | https://github.com/TencentCloud/TencentDB-Agent-Memory |  |
| 12 | `kangarooking/cangjie-skill` | 7001 | 879 | Python | 4,632 stars this month | 把书、长视频、播客等高价值内容蒸馏成可执行的 Agent Skills | https://github.com/kangarooking/cangjie-skill | 新增 |
| 13 | `tt-a1i/archify` | 11203 | 858 | HTML | 7,900 stars this month | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify |  |
| 14 | `earendil-works/pi` | 86698 | 10777 | TypeScript | 17,394 stars this month | AI agent toolkit ：统一LLM API、agent loop、TUI、coding agent CLI | https://github.com/earendil-works/pi |  |
| 15 | `OpenCut-app/OpenCut` | 82113 | 8113 | TypeScript | 20,412 stars this month | 开源CapCut替代方案 | https://github.com/OpenCut-app/OpenCut |  |
| 16 | `tirth8205/code-review-graph` | 29715 | 2720 | Python | 10,435 stars this month | MCP和CLI的本地优先代码智能图。构建代码库的持久映射，以便AI编码工具仅读取重要内容，并对审阅和大型重构工作流进行基准上下文缩减。 | https://github.com/tirth8205/code-review-graph |  |
| 17 | `virgiliojr94/book-to-skill` | 20034 | 2140 | Python | 11,470 stars this month | 将任何技术书籍PDF转化为Claude Code技能—随时准备在您工作时进行学习、参考和使用。 | https://github.com/virgiliojr94/book-to-skill |  |
| 18 | `Shubhamsaboo/awesome-llm-apps` | 131982 | 19432 | Python | 15,049 stars this month | 100多个人工智能代理、代理技能和RAG应用程序-免费开源。 | https://github.com/Shubhamsaboo/awesome-llm-apps |  |
| 19 | `huggingface/speech-to-speech` | 12025 | 1475 | Python | 6,179 stars this month | 使用开源模型构建本地语音代理 | https://github.com/huggingface/speech-to-speech |  |
| 20 | `agegr/pi-web` | 3942 | 545 | TypeScript | 2,848 stars this month | Pi编码代理的Web UI | https://github.com/agegr/pi-web |  |
| 21 | `MoonshotAI/kimi-code` | 6301 | 990 | TypeScript | 3,269 stars this month | Kimi Code CLI —新一代代理的起点 | https://github.com/MoonshotAI/kimi-code | 新增 |


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

**最近一次更新时间**（Asia/Shanghai）： 2026-08-21 10:17:15

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 541628 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 498281 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 467279 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 454374 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 394874 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 386925 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `donnemartin/system-design-primer` | 365128 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 8 | `nilbuild/developer-roadmap` | 365022 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 9 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 10 | `jwasham/coding-interview-university` | 359362 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 11 | `vinta/awesome-python` | 315168 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `modular/modular` | 28004 | 3001 | Mojo | 268 stars today | 模块化平台（包括MAX和Mojo ） | https://github.com/modular/modular | 新增 |
| 2 | `mattpocock/skills` | 226709 | 19439 | Shell | 2,192 stars today | 真正工程师的技能。直接来自我的.agents目录。 | https://github.com/mattpocock/skills |  |
| 3 | `AprilNEA/OpenLogi` | 11956 | 325 | Rust | 1,545 stars today | ⚡️用Rust编写的Logitech Options +的本地本地优先替代方案🦀—在HID + +上重新映射按钮、DPI和SmartShift。无帐户，无遥测。 | https://github.com/AprilNEA/OpenLogi | 新增 |
| 4 | `obra/superpowers` | 274987 | 24611 | Shell | 727 stars today | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers |  |
| 5 | `cursor/plugins` | 4107 | 341 | TypeScript | 449 stars today | 光标插件规范和官方插件 | https://github.com/cursor/plugins | 新增 |
| 6 | `santifer/career-ops` | 66749 | 12825 | JavaScript | 816 stars today | 开源人工智能工作搜索：扫描工作门户网站，使用结构化A-F评分标准将房源评估为1.0-5.0分，定制您的简历，跟踪应用程序—在您的人工智能编码CLI （ Claude Code、Codex、OpenCode、Antigravity…… ）中本地运行 | https://github.com/santifer/career-ops |  |
| 7 | `akitaonrails/ai-memory` | 3651 | 280 | Rust | 332 stars today | 针对座席编码CLI的长期记忆解决方案，以及促进不同座席供应商之间切换的解决方案 | https://github.com/akitaonrails/ai-memory | 新增 |
| 8 | `harry0703/MoneyPrinterTurbo` | 113035 | 17128 | Python | 2,761 stars today | 利用 AI 大模型和自动化工作流，根据主题或关键词一键生成高清短视频。Generate HD short videos from a topic or keyword with an automated AI workflow. | https://github.com/harry0703/MoneyPrinterTurbo |  |
| 9 | `agent-substrate/substrate` | 1414 | 253 | Go | 22 stars today | Agent Substrate ：核心系统 | https://github.com/agent-substrate/substrate | 新增 |
| 10 | `chaitanyagiri/munder-difflin` | 3142 | 351 | TypeScript | 507 stars today | 局部多药剂线束 | https://github.com/chaitanyagiri/munder-difflin |  |
| 11 | `PostHog/posthog` | 38022 | 3218 | Python | 60 stars today | 🦔 PostHog是构建自动驾驶产品的领先平台。我们的开发人员工具–人工智能可观察性、分析、会话重播、标记、实验、错误跟踪、日志等–捕获代理诊断问题、发现机会和发布所需的所有上下文…… | https://github.com/PostHog/posthog | 新增 |
| 12 | `mahlernim/google-timeline-visualizer` | 1634 | 177 | Kotlin | 657 stars today | 使用您的Google位置历史记录（时间轴）数据可视化您的旅行年份 | https://github.com/mahlernim/google-timeline-visualizer | 新增 |
| 13 | `volcengine/OpenViking` | 31063 | 2397 | Python | 950 stars today | 人工智能代理的自我进化上下文数据库。统一座席记忆、知识抹布和技能。 | https://github.com/volcengine/OpenViking |  |
| 14 | `JuliusBrussee/caveman` | 99674 | 5771 | Go | 258 stars today | 🪨 为什么在很少令牌欺骗时使用许多令牌— Claude Code技能通过像穴居人一样说话来削减65 ％的令牌 | https://github.com/JuliusBrussee/caveman | 新增 |
| 15 | `makeplane/plane` | 56534 | 5398 | TypeScript | 98 stars today | 🔥🔥🔥 开源JIRA、Linear、Monday和ClickUp替代方案。Plane是一个现代化的项目管理平台，用于管理任务、冲刺、文档和分类。 | https://github.com/makeplane/plane | 新增 |
| 16 | `Tencent/AI-Infra-Guard` | 5006 | 485 | Python | 50 stars today | 一个全栈AI红色团队平台，通过代理扫描、技能扫描、MCP扫描、AI Infra扫描和LLM越狱评估来保护AI生态系统。 | https://github.com/Tencent/AI-Infra-Guard | 新增 |
| 17 | `RyanCodrai/turbovec` | 15968 | 1388 | Rust | 230 stars today | 基于TurboQuant构建的矢量索引，用Rust和Python绑定编写 | https://github.com/RyanCodrai/turbovec | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `cathrynlavery/diagram-design` | 24360 | 1475 | HTML | 11,325 stars this week | Claude Code、Codex和Pi的38种编辑图类型。独立的HTML + SVG。没有阴影，没有美人鱼粪便。 | https://github.com/cathrynlavery/diagram-design |  |
| 2 | `volcengine/OpenViking` | 31063 | 2397 | Python | 2,444 stars this week | 人工智能代理的自我进化上下文数据库。统一座席记忆、知识抹布和技能。 | https://github.com/volcengine/OpenViking |  |
| 3 | `basecamp/omarchy` | 27064 | 2774 | Shell | 2,395 stars this week | 漂亮、现代且自以为是的Linux | https://github.com/basecamp/omarchy |  |
| 4 | `cactus-compute/needle` | 8142 | 524 | Python | 3,409 stars this week | 14MB基础型号，适用于微型设备；手机、可穿戴设备、智能家居和机器人。 | https://github.com/cactus-compute/needle |  |
| 5 | `semantica-agi/semantica` | 9848 | 1052 | Python | 3,674 stars this week | 上下文和负责任的人工智能系统的图形原生基础设施 | https://github.com/semantica-agi/semantica |  |
| 6 | `NVIDIA-NeMo/Switchyard` | 1978 | 178 | Rust | 932 stars this week | Switchyard允许LLM应用程序跨模型和提供商路由流量，同时保留原生OpenAI和人工API兼容性，从而实现灵活的模型选择、基准测试和成本/性能优化。 | https://github.com/NVIDIA-NeMo/Switchyard | 新增 |
| 7 | `modular/modular` | 28005 | 3001 | Mojo | 744 stars this week | 模块化平台（包括MAX和Mojo ） | https://github.com/modular/modular | 新增 |
| 8 | `harry0703/MoneyPrinterTurbo` | 113036 | 17128 | Python | 9,712 stars this week | 利用 AI 大模型和自动化工作流，根据主题或关键词一键生成高清短视频。Generate HD short videos from a topic or keyword with an automated AI workflow. | https://github.com/harry0703/MoneyPrinterTurbo |  |
| 9 | `public-apis/public-apis` | 467279 | 51540 | Python | 11,259 stars this week | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 10 | `megadose/holehe` | 13837 | 1801 | Python | 1,632 stars this week | holehe允许您检查邮件是否在Twitter、Instagram等不同网站上使用，并将检索具有忘记密码功能的网站上的信息。 | https://github.com/megadose/holehe |  |
| 11 | `AprilNEA/OpenLogi` | 11957 | 325 | Rust | 2,674 stars this week | ⚡️用Rust编写的Logitech Options +的本地本地优先替代方案🦀—在HID + +上重新映射按钮、DPI和SmartShift。无帐户，无遥测。 | https://github.com/AprilNEA/OpenLogi | 新增 |
| 12 | `lightningpixel/modly` | 7040 | 671 | TypeScript | 1,855 stars this week | 使用本地AI从图像或提示生成3D模型的桌面应用程序—完全在您的GPU上运行 | https://github.com/lightningpixel/modly |  |
| 13 | `macro-inc/macro` | 3872 | 370 | Rust | 1,456 stars this week | 宏是团队的统一工作区：电子邮件、聊天、文档、任务、座席、呼叫和CRM — @ —通过共享AI内存链接在一起。 | https://github.com/macro-inc/macro |  |
| 14 | `unslothai/unsloth` | 74111 | 6696 | Python | 3,300 stars this week | 运行和训练LLM和扩散模型的本地UI ，包括Qwen3.8、Kimi K3、MiniMax-H3、Gemma 4、DeepSeek-V4、FLUX等。 | https://github.com/unslothai/unsloth |  |
| 15 | `akitaonrails/ai-memory` | 3651 | 280 | Rust | 1,952 stars this week | 针对座席编码CLI的长期记忆解决方案，以及促进不同座席供应商之间切换的解决方案 | https://github.com/akitaonrails/ai-memory | 新增 |
| 16 | `jundot/omlx` | 20120 | 1710 | Python | 1,388 stars this week | LLM推理服务器，具有Apple Silicon的连续批处理和SSD缓存—通过macOS菜单栏进行管理 | https://github.com/jundot/omlx |  |
| 17 | `AlexsJones/llmfit` | 33292 | 2063 | Rust | 1,842 stars this week | 数以百计的模型和提供商。只需一个命令，即可查找硬件上运行的内容。 | https://github.com/AlexsJones/llmfit |  |
| 18 | `CodebuffAI/freebuff` | 10288 | 1130 | TypeScript | 1,133 stars this week | 自由编码代理 | https://github.com/CodebuffAI/freebuff |  |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `block/buzz` | 28928 | 3641 | Rust | 28,701 stars this month | 蜂巢思维沟通平台 | https://github.com/block/buzz |  |
| 2 | `permissionlesstech/bitchat` | 35713 | 5670 | Swift | 9,710 stars this month | 蓝牙网状聊天， IRC共鸣 | https://github.com/permissionlesstech/bitchat |  |
| 3 | `ayghri/i-have-adhd` | 22685 | 1451 | Python | 18,443 stars this month | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 4 | `citrolabs/ego-lite` | 12271 | 645 | JavaScript | 11,627 stars this month | 人工智能代理运行浏览器自动化的最快浏览器，旨在与您的人工智能代理（如Codex或Claude Code ）共享您登录的浏览器状态，而不会打扰您。零成本，零配置。 | https://github.com/citrolabs/ego-lite | 新增 |
| 5 | `TencentCloud/TencentDB-Agent-Memory` | 23492 | 2167 | TypeScript | 14,407 stars this month | TencentDB Agent Memory是AI Agent的团队级内存中心—将对话、文档和代码转换为四个可重用的内存资产（ Chat Memory、Skill、LLM-Wiki、Code-Graph ） ，这些资产在代理和框架之间进行管理、共享和配备。 | https://github.com/TencentCloud/TencentDB-Agent-Memory |  |
| 6 | `diegosouzapw/OmniRoute` | 52012 | 7095 | TypeScript | 31,270 stars this month | 永不停止编码。免费MIT AI网关：一个端点， 340个提供商（ 90多个免费） ， 1200多个型号— Kimi ， Claude ， GPT ， Gemini ， GLM ， DeepSeek ， MiniMax。适用于Claude Code、Codex、Cursor、OpenCode、Cline和Copilot。配额感知自动回退， RTK +穴居人压缩节省15-95% …… | https://github.com/diegosouzapw/OmniRoute |  |
| 7 | `zhaoxuya520/reverse-skill` | 27037 | 3686 | PowerShell | 18,662 stars this month | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工… | https://github.com/zhaoxuya520/reverse-skill |  |
| 8 | `bojieli/ai-agent-book` | 40338 | 4439 | Python | 31,345 stars this month | 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码 | https://github.com/bojieli/ai-agent-book | 新增 |
| 9 | `pingdotgg/t3code` | 19786 | 4633 | TypeScript | 5,646 stars this month | — | https://github.com/pingdotgg/t3code |  |
| 10 | `microsoft/AI-For-Beginners` | 65932 | 12772 | Jupyter Notebook | 13,592 stars this month | 12周， 24课，全民人工智能！ | https://github.com/microsoft/AI-For-Beginners |  |
| 11 | `virgiliojr94/book-to-skill` | 23429 | 2477 | Python | 14,598 stars this month | 将任何技术书籍PDF转化为Claude Code技能—随时准备在您工作时进行学习、参考和使用。 | https://github.com/virgiliojr94/book-to-skill |  |
| 12 | `mattpocock/skills` | 226713 | 19439 | Shell | 47,717 stars this month | 真正工程师的技能。直接来自我的.agents目录。 | https://github.com/mattpocock/skills |  |
| 13 | `1jehuang/jcode` | 18112 | 2032 | Rust | 8,972 stars this month | RAM效率最高的线束 | https://github.com/1jehuang/jcode |  |
| 14 | `basecamp/omarchy` | 27064 | 2774 | Shell | 3,095 stars this month | 漂亮、现代且自以为是的Linux | https://github.com/basecamp/omarchy |  |
| 15 | `earendil-works/pi` | 94464 | 11697 | TypeScript | 21,507 stars this month | AI agent toolkit ：统一LLM API、agent loop、TUI、coding agent CLI | https://github.com/earendil-works/pi |  |
| 16 | `koala73/worldmonitor` | 83508 | 12450 | TypeScript | 21,742 stars this month | 实时全球智能仪表板。在统一的态势感知界面中进行人工智能驱动的新闻聚合、地缘政治监控和基础设施跟踪 | https://github.com/koala73/worldmonitor |  |
| 17 | `cactus-compute/needle` | 8142 | 524 | Python | 4,829 stars this month | 14MB基础型号，适用于微型设备；手机、可穿戴设备、智能家居和机器人。 | https://github.com/cactus-compute/needle |  |
| 18 | `megadose/holehe` | 13837 | 1801 | Python | 2,109 stars this month | holehe允许您检查邮件是否在Twitter、Instagram等不同网站上使用，并将检索具有忘记密码功能的网站上的信息。 | https://github.com/megadose/holehe |  |
| 19 | `HKUDS/DeepTutor` | 36673 | 4613 | Python | 8,578 stars this month | DeepTutor ：终身个性化辅导。https://deeptutor.info/。 | https://github.com/HKUDS/DeepTutor |  |
| 20 | `different-ai/openwork` | 22817 | 2259 | TypeScript | 6,006 stars this month | Claude Cowork的开源替代品（由opencode提供支持） | https://github.com/different-ai/openwork |  |
| 21 | `lyogavin/airllm` | 31946 | 3381 | Jupyter Notebook | 8,160 stars this month | 使用单个4GB GPU的AirLLM 70B推理 | https://github.com/lyogavin/airllm |  |
| 22 | `every-app/open-seo` | 12882 | 1471 | TypeScript | 7,395 stars this month | Semrush和Ahrefs的开源替代品 | https://github.com/every-app/open-seo |  |


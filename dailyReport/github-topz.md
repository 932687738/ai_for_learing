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

**最近一次更新时间**（Asia/Shanghai）： 2026-08-18 09:47:57

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 540557 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 497015 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 463253 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 454213 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 394638 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 386565 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 364752 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 364471 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 10 | `jwasham/coding-interview-university` | 359071 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 11 | `vinta/awesome-python` | 314514 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `harry0703/MoneyPrinterTurbo` | 106154 | 16129 | Python | 1,189 stars today | 利用 AI 大模型和自动化工作流，根据主题或关键词一键生成高清短视频。Generate HD short videos from a topic or keyword with an automated AI workflow. | https://github.com/harry0703/MoneyPrinterTurbo | 新增 |
| 2 | `usestrix/strix` | 54237 | 5803 | Python | 598 stars today | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix | 新增 |
| 3 | `nautechsystems/nautilus_trader` | 25952 | 3372 | Rust | 120 stars today | 具有确定性事件驱动架构的生产级Rust原生交易引擎 | https://github.com/nautechsystems/nautilus_trader | 新增 |
| 4 | `akitaonrails/ai-memory` | 2105 | 197 | Rust | 207 stars today | 针对座席编码CLI的长期记忆解决方案，以及促进不同座席供应商之间切换的解决方案 | https://github.com/akitaonrails/ai-memory | 新增 |
| 5 | `mukul975/Anthropic-Cybersecurity-Skills` | 28466 | 3450 | Python | 198 stars today | 人工智能代理的817种结构化网络安全技能·映射到6个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF和MITRE F3 （打击欺诈） · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20 + p…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills | 新增 |
| 6 | `AlexsJones/llmfit` | 32315 | 2002 | Rust | 198 stars today | 数以百计的模型和提供商。只需一个命令，即可查找硬件上运行的内容。 | https://github.com/AlexsJones/llmfit | 新增 |
| 7 | `santifer/career-ops` | 64704 | 12653 | JavaScript | 218 stars today | 开源人工智能工作搜索：扫描工作门户网站，使用结构化A-F评分标准将房源评估为1.0-5.0分，定制您的简历，跟踪应用程序—在您的人工智能编码CLI （ Claude Code、Codex、OpenCode、Antigravity…… ）中本地运行 | https://github.com/santifer/career-ops | 新增 |
| 8 | `jundot/omlx` | 19009 | 1645 | Python | 78 stars today | LLM推理服务器，具有Apple Silicon的连续批处理和SSD缓存—通过macOS菜单栏进行管理 | https://github.com/jundot/omlx | 新增 |
| 9 | `immich-app/immich` | 111189 | 6578 | TypeScript | 175 stars today | 高性能自托管照片和视频管理解决方案。 | https://github.com/immich-app/immich | 新增 |
| 10 | `cordiverse/cordis` | 5627 | 299 | TypeScript | 957 stars today | 时空可组合性元框架 | https://github.com/cordiverse/cordis |  |
| 11 | `agalwood/Motrix` | 53113 | 4930 | TypeScript | 344 stars today | 功能齐全的下载管理器。 | https://github.com/agalwood/Motrix | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `cathrynlavery/diagram-design` | 20749 | 1275 | HTML | 16,260 stars this week | Claude Code的27种编辑图类型。独立的HTML + SVG。没有阴影，没有美人鱼的污点。 | https://github.com/cathrynlavery/diagram-design |  |
| 2 | `semantica-agi/semantica` | 8608 | 885 | Python | 4,746 stars this week | 上下文和负责任的人工智能系统的图形原生基础设施 | https://github.com/semantica-agi/semantica |  |
| 3 | `cactus-compute/needle` | 7152 | 460 | Python | 3,627 stars this week | 14MB基础型号，适用于微型设备；手机、可穿戴设备、智能家居和机器人。 | https://github.com/cactus-compute/needle |  |
| 4 | `megadose/holehe` | 13452 | 1774 | Python | 1,416 stars this week | holehe允许您检查邮件是否在Twitter、Instagram等不同网站上使用，并将检索具有忘记密码功能的网站上的信息。 | https://github.com/megadose/holehe |  |
| 5 | `PrimeIntellect-ai/prime-agent` | 16938 | 1818 | TypeScript | 4,328 stars this week | 自我改进的RLM代理，用于编码工作流程和长期运行的自主任务。 | https://github.com/PrimeIntellect-ai/prime-agent |  |
| 6 | `macro-inc/macro` | 3562 | 358 | Rust | 2,724 stars this week | 宏是团队的统一工作区：电子邮件、聊天、文档、任务、座席、呼叫和CRM — @ —通过共享AI内存链接在一起。 | https://github.com/macro-inc/macro |  |
| 7 | `vitali87/code-graph-rag` | 4547 | 610 | Python | 1,135 stars this week | 您的monorepo的终极抹布。利用人工智能和知识图谱的力量查询、理解和编辑多语言代码库 | https://github.com/vitali87/code-graph-rag |  |
| 8 | `unslothai/unsloth` | 73247 | 6602 | Python | 3,329 stars this week | 运行和训练LLM和扩散模型的本地UI ，包括Qwen3.8、Kimi K3、MiniMax-H3、Gemma 4、DeepSeek-V4、FLUX等。 | https://github.com/unslothai/unsloth |  |
| 9 | `3b1b/manim` | 91504 | 7560 | Python | 1,724 stars this week | 解释性数学视频的动画引擎 | https://github.com/3b1b/manim |  |
| 10 | `basecamp/omarchy` | 26015 | 2649 | Shell | 1,477 stars this week | 漂亮、现代且自以为是的Linux | https://github.com/basecamp/omarchy |  |
| 11 | `addyosmani/agent-skills` | 88064 | 9440 | JavaScript | 2,575 stars this week | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 12 | `lightningpixel/modly` | 6386 | 635 | TypeScript | 1,338 stars this week | 使用本地AI从图像或提示生成3D模型的桌面应用程序—完全在您的GPU上运行 | https://github.com/lightningpixel/modly | 新增 |
| 13 | `TencentCloud/TencentDB-Agent-Memory` | 22642 | 2063 | TypeScript | 3,389 stars this week | TencentDB Agent Memory是AI Agent的团队级内存中心—将对话、文档和代码转换为四个可重用的内存资产（ Chat Memory、Skill、LLM-Wiki、Code-Graph ） ，这些资产在代理和框架之间进行管理、共享和配备。 | https://github.com/TencentCloud/TencentDB-Agent-Memory |  |
| 14 | `anthropics/skills` | 170027 | 20239 | Python | 2,714 stars this week | 座席技能的公共存储库 | https://github.com/anthropics/skills | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `ayghri/i-have-adhd` | 21514 | 1367 | Python | 20,926 stars this month | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd | 新增 |
| 2 | `bojieli/ai-agent-book` | 38547 | 4249 | Python | 37,085 stars this month | 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码 | https://github.com/bojieli/ai-agent-book |  |
| 3 | `diegosouzapw/OmniRoute` | 49859 | 6791 | TypeScript | 31,675 stars this month | 永不停止编码。免费MIT AI网关：一个端点， 340个提供商（ 90多个免费） ， 1200多个型号— Kimi ， Claude ， GPT ， Gemini ， GLM ， DeepSeek ， MiniMax。适用于Claude Code、Codex、Cursor、OpenCode、Cline和Copilot。配额感知自动回退， RTK +穴居人压缩节省15-95% …… | https://github.com/diegosouzapw/OmniRoute |  |
| 4 | `koala73/worldmonitor` | 82687 | 12341 | TypeScript | 21,062 stars this month | 实时全球智能仪表板。在统一的态势感知界面中进行人工智能驱动的新闻聚合、地缘政治监控和基础设施跟踪 | https://github.com/koala73/worldmonitor |  |
| 5 | `TencentCloud/TencentDB-Agent-Memory` | 22642 | 2063 | TypeScript | 13,625 stars this month | TencentDB Agent Memory是AI Agent的团队级内存中心—将对话、文档和代码转换为四个可重用的内存资产（ Chat Memory、Skill、LLM-Wiki、Code-Graph ） ，这些资产在代理和框架之间进行管理、共享和配备。 | https://github.com/TencentCloud/TencentDB-Agent-Memory |  |
| 6 | `1jehuang/jcode` | 17859 | 2002 | Rust | 9,578 stars this month | RAM效率最高的线束 | https://github.com/1jehuang/jcode |  |
| 7 | `zhaoxuya520/reverse-skill` | 26033 | 3527 | PowerShell | 17,807 stars this month | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工… | https://github.com/zhaoxuya520/reverse-skill |  |
| 8 | `pingdotgg/t3code` | 19109 | 4434 | TypeScript | 5,096 stars this month | — | https://github.com/pingdotgg/t3code |  |
| 9 | `microsoft/AI-For-Beginners` | 65208 | 12660 | Jupyter Notebook | 12,969 stars this month | 12周， 24课，全民人工智能！ | https://github.com/microsoft/AI-For-Beginners | 新增 |
| 10 | `earendil-works/pi` | 92407 | 11447 | TypeScript | 20,481 stars this month | AI agent toolkit ：统一LLM API、agent loop、TUI、coding agent CLI | https://github.com/earendil-works/pi |  |
| 11 | `virgiliojr94/book-to-skill` | 22569 | 2379 | Python | 13,818 stars this month | 将任何技术书籍PDF转化为Claude Code技能—随时准备在您工作时进行学习、参考和使用。 | https://github.com/virgiliojr94/book-to-skill |  |
| 12 | `mattpocock/skills` | 220393 | 18992 | Shell | 45,839 stars this month | 真正工程师的技能。直接来自我的.agents目录。 | https://github.com/mattpocock/skills |  |
| 13 | `stablyai/orca` | 47467 | 3292 | TypeScript | 26,504 stars this month | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面、移动和VPS上使用。 | https://github.com/stablyai/orca |  |
| 14 | `every-app/open-seo` | 12403 | 1416 | TypeScript | 8,017 stars this month | Semrush和Ahrefs的开源替代品 | https://github.com/every-app/open-seo |  |
| 15 | `HKUDS/DeepTutor` | 36146 | 4550 | Python | 9,118 stars this month | DeepTutor ：终身个性化辅导。https://deeptutor.info/。 | https://github.com/HKUDS/DeepTutor |  |
| 16 | `agegr/pi-web` | 4614 | 634 | TypeScript | 3,349 stars this month | Pi编码代理的Web UI | https://github.com/agegr/pi-web |  |
| 17 | `tirth8205/code-review-graph` | 30448 | 2779 | Python | 10,960 stars this month | MCP和CLI的本地优先代码智能图。构建代码库的持久映射，以便AI编码工具仅读取重要内容，并对审阅和大型重构工作流进行基准上下文缩减。 | https://github.com/tirth8205/code-review-graph |  |
| 18 | `lyogavin/airllm` | 31477 | 3342 | Jupyter Notebook | 8,585 stars this month | 使用单个4GB GPU的AirLLM 70B推理 | https://github.com/lyogavin/airllm |  |
| 19 | `Nutlope/hallmark` | 25569 | 1303 | CSS | 14,015 stars this month | Claude Code、Cursor和Codex的防AI倾斜设计技能。 | https://github.com/Nutlope/hallmark |  |
| 20 | `megadose/holehe` | 13452 | 1774 | Python | 1,717 stars this month | holehe允许您检查邮件是否在Twitter、Instagram等不同网站上使用，并将检索具有忘记密码功能的网站上的信息。 | https://github.com/megadose/holehe |  |
| 21 | `different-ai/openwork` | 22568 | 2230 | TypeScript | 5,799 stars this month | Claude Cowork的开源替代品（由opencode提供支持） | https://github.com/different-ai/openwork |  |
| 22 | `opengeos/GeoLibre` | 6324 | 634 | TypeScript | 4,545 stars this month | 一个轻量级的云原生GIS平台，用于可视化、探索和分析地理空间数据。它在Web浏览器、桌面、移动设备和Jupyter笔记本中运行。 | https://github.com/opengeos/GeoLibre | 新增 |


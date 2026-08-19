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

**最近一次更新时间**（Asia/Shanghai）： 2026-08-19 09:30:05

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 540911 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 497446 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 464598 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 454282 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 394710 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 386680 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 364869 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 364694 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 10 | `jwasham/coding-interview-university` | 359157 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 11 | `vinta/awesome-python` | 314713 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `harry0703/MoneyPrinterTurbo` | 108586 | 16484 | Python | 2,304 stars today | 利用 AI 大模型和自动化工作流，根据主题或关键词一键生成高清短视频。Generate HD short videos from a topic or keyword with an automated AI workflow. | https://github.com/harry0703/MoneyPrinterTurbo |  |
| 2 | `chaitanyagiri/munder-difflin` | 2051 | 242 | TypeScript | 306 stars today | 局部多药剂线束 | https://github.com/chaitanyagiri/munder-difflin | 新增 |
| 3 | `akitaonrails/ai-memory` | 2741 | 236 | Rust | 648 stars today | 针对座席编码CLI的长期记忆解决方案，以及促进不同座席供应商之间切换的解决方案 | https://github.com/akitaonrails/ai-memory |  |
| 4 | `volcengine/OpenViking` | 29407 | 2307 | Python | 213 stars today | 人工智能代理的自我进化上下文数据库。统一座席记忆、知识抹布和技能。 | https://github.com/volcengine/OpenViking | 新增 |
| 5 | `mukul975/Anthropic-Cybersecurity-Skills` | 29220 | 3497 | Python | 730 stars today | 人工智能代理的817种结构化网络安全技能·映射到6个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF和MITRE F3 （打击欺诈） · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20 + p…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills |  |
| 6 | `public-apis/public-apis` | 464598 | 51322 | Python | 1,005 stars today | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis | 新增 |
| 7 | `basecamp/omarchy` | 26442 | 2690 | Shell | 356 stars today | 漂亮、现代且自以为是的Linux | https://github.com/basecamp/omarchy | 新增 |
| 8 | `agalwood/Motrix` | 53691 | 4951 | TypeScript | 609 stars today | 功能齐全的下载管理器。 | https://github.com/agalwood/Motrix |  |
| 9 | `NawfalMotii79/PLFM_RADAR` | 24318 | 5592 | PLSQL | 192 stars today | 开源、低成本的10.5 GHz PLFM相控阵雷达系统 | https://github.com/NawfalMotii79/PLFM_RADAR | 新增 |
| 10 | `jundot/omlx` | 19416 | 1670 | Python | 370 stars today | LLM推理服务器，具有Apple Silicon的连续批处理和SSD缓存—通过macOS菜单栏进行管理 | https://github.com/jundot/omlx |  |
| 11 | `genlayerlabs/genlayer-project-boilerplate` | 15960 | 802 | TypeScript | 535 stars today | — | https://github.com/genlayerlabs/genlayer-project-boilerplate | 新增 |
| 12 | `OpenCut-app/OpenCut` | 84796 | 8354 | TypeScript | 192 stars today | 开源CapCut替代方案 | https://github.com/OpenCut-app/OpenCut | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `cathrynlavery/diagram-design` | 21863 | 1338 | HTML | 15,812 stars this week | Claude Code的27种编辑图类型。独立的HTML + SVG。没有阴影，没有美人鱼的污点。 | https://github.com/cathrynlavery/diagram-design |  |
| 2 | `semantica-agi/semantica` | 9021 | 931 | Python | 4,304 stars this week | 上下文和负责任的人工智能系统的图形原生基础设施 | https://github.com/semantica-agi/semantica |  |
| 3 | `cactus-compute/needle` | 7516 | 482 | Python | 3,772 stars this week | 14MB基础型号，适用于微型设备；手机、可穿戴设备、智能家居和机器人。 | https://github.com/cactus-compute/needle |  |
| 4 | `megadose/holehe` | 13608 | 1787 | Python | 1,568 stars this week | holehe允许您检查邮件是否在Twitter、Instagram等不同网站上使用，并将检索具有忘记密码功能的网站上的信息。 | https://github.com/megadose/holehe |  |
| 5 | `basecamp/omarchy` | 26442 | 2690 | Shell | 1,802 stars this week | 漂亮、现代且自以为是的Linux | https://github.com/basecamp/omarchy |  |
| 6 | `macro-inc/macro` | 3676 | 361 | Rust | 2,627 stars this week | 宏是团队的统一工作区：电子邮件、聊天、文档、任务、座席、呼叫和CRM — @ —通过共享AI内存链接在一起。 | https://github.com/macro-inc/macro |  |
| 7 | `unslothai/unsloth` | 73604 | 6649 | Python | 3,636 stars this week | 运行和训练LLM和扩散模型的本地UI ，包括Qwen3.8、Kimi K3、MiniMax-H3、Gemma 4、DeepSeek-V4、FLUX等。 | https://github.com/unslothai/unsloth |  |
| 8 | `lightningpixel/modly` | 6699 | 654 | TypeScript | 1,600 stars this week | 使用本地AI从图像或提示生成3D模型的桌面应用程序—完全在您的GPU上运行 | https://github.com/lightningpixel/modly |  |
| 9 | `AlexsJones/llmfit` | 32736 | 2021 | Rust | 1,316 stars this week | 数以百计的模型和提供商。只需一个命令，即可查找硬件上运行的内容。 | https://github.com/AlexsJones/llmfit | 新增 |
| 10 | `public-apis/public-apis` | 464598 | 51322 | Python | 8,646 stars this week | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis | 新增 |
| 11 | `PrimeIntellect-ai/prime-agent` | 17202 | 1849 | TypeScript | 3,475 stars this week | 自我改进的RLM代理，用于编码工作流程和长期运行的自主任务。 | https://github.com/PrimeIntellect-ai/prime-agent |  |
| 12 | `3b1b/manim` | 91635 | 7564 | Python | 1,646 stars this week | 解释性数学视频的动画引擎 | https://github.com/3b1b/manim |  |
| 13 | `Lightricks/LTX-2` | 9135 | 1436 | Python | 556 stars this week | LTX-2音视频生成模型的官方Python推理和LoRA训练器包。 | https://github.com/Lightricks/LTX-2 | 新增 |
| 14 | `vitali87/code-graph-rag` | 4623 | 615 | Python | 910 stars this week | 您的monorepo的终极抹布。利用人工智能和知识图谱的力量查询、理解和编辑多语言代码库 | https://github.com/vitali87/code-graph-rag |  |
| 15 | `superradcompany/microsandbox` | 7674 | 408 | Rust | 350 stars this week | 🧱 轻松快速的本地优先microVM运行时和库 | https://github.com/superradcompany/microsandbox | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `ayghri/i-have-adhd` | 21978 | 1396 | Python | 21,447 stars this month | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 2 | `permissionlesstech/bitchat` | 35557 | 5661 | Swift | 9,555 stars this month | 蓝牙网状聊天， IRC共鸣 | https://github.com/permissionlesstech/bitchat | 新增 |
| 3 | `diegosouzapw/OmniRoute` | 50501 | 6878 | TypeScript | 32,029 stars this month | 永不停止编码。免费MIT AI网关：一个端点， 340个提供商（ 90多个免费） ， 1200多个型号— Kimi ， Claude ， GPT ， Gemini ， GLM ， DeepSeek ， MiniMax。适用于Claude Code、Codex、Cursor、OpenCode、Cline和Copilot。配额感知自动回退， RTK +穴居人压缩节省15-95% …… | https://github.com/diegosouzapw/OmniRoute |  |
| 4 | `koala73/worldmonitor` | 82976 | 12378 | TypeScript | 21,286 stars this month | 实时全球智能仪表板。在统一的态势感知界面中进行人工智能驱动的新闻聚合、地缘政治监控和基础设施跟踪 | https://github.com/koala73/worldmonitor |  |
| 5 | `TencentCloud/TencentDB-Agent-Memory` | 22982 | 2095 | TypeScript | 13,944 stars this month | TencentDB Agent Memory是AI Agent的团队级内存中心—将对话、文档和代码转换为四个可重用的内存资产（ Chat Memory、Skill、LLM-Wiki、Code-Graph ） ，这些资产在代理和框架之间进行管理、共享和配备。 | https://github.com/TencentCloud/TencentDB-Agent-Memory |  |
| 6 | `zhaoxuya520/reverse-skill` | 26361 | 3573 | PowerShell | 18,059 stars this month | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工… | https://github.com/zhaoxuya520/reverse-skill |  |
| 7 | `pingdotgg/t3code` | 19364 | 4498 | TypeScript | 5,265 stars this month | — | https://github.com/pingdotgg/t3code |  |
| 8 | `microsoft/AI-For-Beginners` | 65443 | 12695 | Jupyter Notebook | 13,156 stars this month | 12周， 24课，全民人工智能！ | https://github.com/microsoft/AI-For-Beginners |  |
| 9 | `1jehuang/jcode` | 17943 | 2015 | Rust | 9,593 stars this month | RAM效率最高的线束 | https://github.com/1jehuang/jcode |  |
| 10 | `virgiliojr94/book-to-skill` | 22867 | 2422 | Python | 14,079 stars this month | 将任何技术书籍PDF转化为Claude Code技能—随时准备在您工作时进行学习、参考和使用。 | https://github.com/virgiliojr94/book-to-skill |  |
| 11 | `earendil-works/pi` | 93155 | 11541 | TypeScript | 20,985 stars this month | AI agent toolkit ：统一LLM API、agent loop、TUI、coding agent CLI | https://github.com/earendil-works/pi |  |
| 12 | `mattpocock/skills` | 221536 | 19084 | Shell | 46,007 stars this month | 真正工程师的技能。直接来自我的.agents目录。 | https://github.com/mattpocock/skills |  |
| 13 | `every-app/open-seo` | 12555 | 1436 | TypeScript | 8,133 stars this month | Semrush和Ahrefs的开源替代品 | https://github.com/every-app/open-seo |  |
| 14 | `stablyai/orca` | 48319 | 3344 | TypeScript | 26,771 stars this month | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面、移动和VPS上使用。 | https://github.com/stablyai/orca |  |
| 15 | `HKUDS/DeepTutor` | 36315 | 4571 | Python | 8,910 stars this month | DeepTutor ：终身个性化辅导。https://deeptutor.info/。 | https://github.com/HKUDS/DeepTutor |  |
| 16 | `basecamp/omarchy` | 26442 | 2690 | Shell | 2,364 stars this month | 漂亮、现代且自以为是的Linux | https://github.com/basecamp/omarchy | 新增 |
| 17 | `oblien/openship` | 11030 | 943 | TypeScript | 10,646 stars this month | 自托管部署平台 | https://github.com/oblien/openship | 新增 |
| 18 | `UditAkhourii/adhd` | 3705 | 260 | TypeScript | 2,705 stars this month | ADHD —编码药剂的技能。基于Claude &amp; Codex Agent SDK构建的具有修剪功能的思考树。在不同的认知框架、分数、修剪陷阱下扇出平行发散的思想，加深幸存者。创造性和跨学科的轻松技能…… | https://github.com/UditAkhourii/adhd | 新增 |
| 19 | `megadose/holehe` | 13608 | 1787 | Python | 1,869 stars this month | holehe允许您检查邮件是否在Twitter、Instagram等不同网站上使用，并将检索具有忘记密码功能的网站上的信息。 | https://github.com/megadose/holehe |  |
| 20 | `lyogavin/airllm` | 31586 | 3353 | Jupyter Notebook | 8,531 stars this month | 使用单个4GB GPU的AirLLM 70B推理 | https://github.com/lyogavin/airllm |  |
| 21 | `cactus-compute/needle` | 7516 | 482 | Python | 4,174 stars this month | 14MB基础型号，适用于微型设备；手机、可穿戴设备、智能家居和机器人。 | https://github.com/cactus-compute/needle | 新增 |


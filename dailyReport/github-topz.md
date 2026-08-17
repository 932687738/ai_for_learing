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

**最近一次更新时间**（Asia/Shanghai）： 2026-08-17 09:53:37

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 540276 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 496598 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 461843 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 454156 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 394577 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 386472 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 364652 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 364247 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 10 | `jwasham/coding-interview-university` | 358968 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 11 | `vinta/awesome-python` | 314334 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `cordiverse/cordis` | 4800 | 260 | TypeScript | 720 stars today | 时空可组合性元框架 | https://github.com/cordiverse/cordis | 新增 |
| 2 | `basecamp/omarchy` | 25426 | 2596 | Shell | 270 stars today | 漂亮、现代且自以为是的Linux | https://github.com/basecamp/omarchy | 新增 |
| 3 | `unslothai/unsloth` | 72630 | 6549 | Python | 572 stars today | 运行和训练LLM和扩散模型的本地UI ，包括Qwen3.8、Kimi K3、MiniMax-H3、Gemma 4、DeepSeek-V4、FLUX等。 | https://github.com/unslothai/unsloth |  |
| 4 | `OpenCut-app/OpenCut` | 83929 | 8289 | TypeScript | 150 stars today | 开源CapCut替代方案 | https://github.com/OpenCut-app/OpenCut | 新增 |
| 5 | `public-apis/public-apis` | 461842 | 51017 | Python | 1,588 stars today | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis | 新增 |
| 6 | `ToolJet/ToolJet` | 40069 | 5331 | JavaScript | 452 stars today | ToolJet是ToolJet AI的开源基础， ToolJet AI是用于构建内部工具、仪表板、业务应用程序、工作流程和AI代理的企业应用程序生成平台 🚀 | https://github.com/ToolJet/ToolJet | 新增 |
| 7 | `cactus-compute/needle` | 6613 | 435 | Python | 443 stars today | 14MB基础型号，适用于微型设备；手机、可穿戴设备、智能家居和机器人。 | https://github.com/cactus-compute/needle |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `cathrynlavery/diagram-design` | 19590 | 1200 | HTML | 15,600 stars this week | Claude Code的29种编辑图类型。独立的HTML + SVG。没有阴影，没有美人鱼的污点。 | https://github.com/cathrynlavery/diagram-design | 新增 |
| 2 | `semantica-agi/semantica` | 8207 | 840 | Python | 5,284 stars this week | 上下文和负责任的人工智能系统的图形原生基础设施 | https://github.com/semantica-agi/semantica |  |
| 3 | `PrimeIntellect-ai/prime-agent` | 16590 | 1787 | TypeScript | 6,435 stars this week | 自我改进的RLM代理，用于编码工作流程和长期运行的自主任务。 | https://github.com/PrimeIntellect-ai/prime-agent |  |
| 4 | `NVIDIA-NeMo/Switchyard` | 1696 | 154 | Rust | 1,435 stars this week | Switchyard允许LLM应用程序跨模型和提供商路由流量，同时保留原生OpenAI和人工API兼容性，从而实现灵活的模型选择、基准测试和成本/性能优化。 | https://github.com/NVIDIA-NeMo/Switchyard | 新增 |
| 5 | `megadose/holehe` | 13299 | 1757 | Python | 1,287 stars this week | holehe允许您检查邮件是否在Twitter、Instagram等不同网站上使用，并将检索具有忘记密码功能的网站上的信息。 | https://github.com/megadose/holehe | 新增 |
| 6 | `cactus-compute/needle` | 6613 | 435 | Python | 2,950 stars this week | 14MB基础型号，适用于微型设备；手机、可穿戴设备、智能家居和机器人。 | https://github.com/cactus-compute/needle | 新增 |
| 7 | `macro-inc/macro` | 3419 | 340 | Rust | 2,588 stars this week | 宏是团队的统一工作区：电子邮件、聊天、文档、任务、座席、呼叫和CRM — @ —通过共享AI内存链接在一起。 | https://github.com/macro-inc/macro | 新增 |
| 8 | `vitali87/code-graph-rag` | 4433 | 598 | Python | 1,686 stars this week | 您的monorepo的终极抹布。利用人工智能和知识图谱的力量查询、理解和编辑多语言代码库 | https://github.com/vitali87/code-graph-rag |  |
| 9 | `ToolJet/ToolJet` | 40069 | 5331 | JavaScript | 1,518 stars this week | ToolJet是ToolJet AI的开源基础， ToolJet AI是用于构建内部工具、仪表板、业务应用程序、工作流程和AI代理的企业应用程序生成平台 🚀 | https://github.com/ToolJet/ToolJet | 新增 |
| 10 | `addyosmani/agent-skills` | 87777 | 9406 | JavaScript | 2,882 stars this week | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 11 | `3b1b/manim` | 91361 | 7555 | Python | 1,978 stars this week | 解释性数学视频的动画引擎 | https://github.com/3b1b/manim |  |
| 12 | `basecamp/omarchy` | 25426 | 2596 | Shell | 759 stars this week | 漂亮、现代且自以为是的Linux | https://github.com/basecamp/omarchy | 新增 |
| 13 | `unslothai/unsloth` | 72630 | 6549 | Python | 2,645 stars this week | 运行和训练LLM和扩散模型的本地UI ，包括Qwen3.8、Kimi K3、MiniMax-H3、Gemma 4、DeepSeek-V4、FLUX等。 | https://github.com/unslothai/unsloth | 新增 |
| 14 | `TencentCloud/TencentDB-Agent-Memory` | 22257 | 2038 | TypeScript | 3,637 stars this week | TencentDB Agent Memory是AI Agent的团队级内存中心—将对话、文档和代码转换为四个可重用的内存资产（ Chat Memory、Skill、LLM-Wiki、Code-Graph ） ，这些资产在代理和框架之间进行管理、共享和配备。 | https://github.com/TencentCloud/TencentDB-Agent-Memory |  |
| 15 | `Lightricks/LTX-2` | 9058 | 1430 | Python | 497 stars this week | LTX-2音视频生成模型的官方Python推理和LoRA训练器包。 | https://github.com/Lightricks/LTX-2 | 新增 |
| 16 | `paperclipai/paperclip` | 78527 | 14386 | TypeScript | 2,499 stars this week | 每个人都使用的开源应用程序来管理工作中的代理 | https://github.com/paperclipai/paperclip | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `bojieli/ai-agent-book` | 37921 | 4174 | Python | 37,110 stars this month | 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码 | https://github.com/bojieli/ai-agent-book | 新增 |
| 2 | `diegosouzapw/OmniRoute` | 49195 | 6707 | TypeScript | 31,374 stars this month | 永不停止编码。免费MIT AI网关：一个端点， 340个提供商（ 90多个免费） ， 1200多个型号— Kimi ， Claude ， GPT ， Gemini ， GLM ， DeepSeek ， MiniMax。适用于Claude Code、Codex、Cursor、OpenCode、Cline和Copilot。配额感知自动回退， RTK +穴居人压缩节省15-95% …… | https://github.com/diegosouzapw/OmniRoute |  |
| 3 | `koala73/worldmonitor` | 82419 | 12306 | TypeScript | 20,810 stars this month | 实时全球智能仪表板。在统一的态势感知界面中进行人工智能驱动的新闻聚合、地缘政治监控和基础设施跟踪 | https://github.com/koala73/worldmonitor |  |
| 4 | `1jehuang/jcode` | 17755 | 1993 | Rust | 9,481 stars this month | RAM效率最高的线束 | https://github.com/1jehuang/jcode |  |
| 5 | `TencentCloud/TencentDB-Agent-Memory` | 22257 | 2038 | TypeScript | 13,308 stars this month | TencentDB Agent Memory是AI Agent的团队级内存中心—将对话、文档和代码转换为四个可重用的内存资产（ Chat Memory、Skill、LLM-Wiki、Code-Graph ） ，这些资产在代理和框架之间进行管理、共享和配备。 | https://github.com/TencentCloud/TencentDB-Agent-Memory |  |
| 6 | `zhaoxuya520/reverse-skill` | 25717 | 3480 | PowerShell | 17,554 stars this month | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工… | https://github.com/zhaoxuya520/reverse-skill |  |
| 7 | `pingdotgg/t3code` | 18965 | 4399 | TypeScript | 5,027 stars this month | — | https://github.com/pingdotgg/t3code |  |
| 8 | `earendil-works/pi` | 91552 | 11355 | TypeScript | 19,903 stars this month | AI agent toolkit ：统一LLM API、agent loop、TUI、coding agent CLI | https://github.com/earendil-works/pi |  |
| 9 | `every-app/open-seo` | 12218 | 1392 | TypeScript | 7,870 stars this month | Semrush和Ahrefs的开源替代品 | https://github.com/every-app/open-seo |  |
| 10 | `mattpocock/skills` | 219341 | 18888 | Shell | 46,346 stars this month | 真正工程师的技能。直接来自我的.agents目录。 | https://github.com/mattpocock/skills |  |
| 11 | `virgiliojr94/book-to-skill` | 22239 | 2348 | Python | 13,494 stars this month | 将任何技术书籍PDF转化为Claude Code技能—随时准备在您工作时进行学习、参考和使用。 | https://github.com/virgiliojr94/book-to-skill |  |
| 12 | `stablyai/orca` | 46628 | 3255 | TypeScript | 26,429 stars this month | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面、移动和VPS上使用。 | https://github.com/stablyai/orca |  |
| 13 | `HKUDS/DeepTutor` | 35957 | 4532 | Python | 9,425 stars this month | DeepTutor ：终身个性化辅导。https://deeptutor.info/。 | https://github.com/HKUDS/DeepTutor |  |
| 14 | `tirth8205/code-review-graph` | 30358 | 2771 | Python | 10,934 stars this month | MCP和CLI的本地优先代码智能图。构建代码库的持久映射，以便AI编码工具仅读取重要内容，并对审阅和大型重构工作流进行基准上下文缩减。 | https://github.com/tirth8205/code-review-graph |  |
| 15 | `agegr/pi-web` | 4426 | 619 | TypeScript | 3,175 stars this month | Pi编码代理的Web UI | https://github.com/agegr/pi-web |  |
| 16 | `Nutlope/hallmark` | 25313 | 1288 | CSS | 15,143 stars this month | Claude Code、Cursor和Codex的防AI倾斜设计技能。 | https://github.com/Nutlope/hallmark |  |
| 17 | `lyogavin/airllm` | 31347 | 3328 | Jupyter Notebook | 8,712 stars this month | 使用单个4GB GPU的AirLLM 70B推理 | https://github.com/lyogavin/airllm | 新增 |
| 18 | `different-ai/openwork` | 22455 | 2219 | TypeScript | 5,703 stars this month | Claude Cowork的开源替代品（由opencode提供支持） | https://github.com/different-ai/openwork |  |
| 19 | `megadose/holehe` | 13300 | 1757 | Python | 1,588 stars this month | holehe允许您检查邮件是否在Twitter、Instagram等不同网站上使用，并将检索具有忘记密码功能的网站上的信息。 | https://github.com/megadose/holehe | 新增 |
| 20 | `tt-a1i/archify` | 13395 | 981 | HTML | 7,964 stars this month | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify |  |


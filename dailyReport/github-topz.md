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

**最近一次更新时间**（Asia/Shanghai）： 2026-08-25 09:27:03

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 542660 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 499629 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 469898 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 454549 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 395162 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 387442 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `donnemartin/system-design-primer` | 365832 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 8 | `nilbuild/developer-roadmap` | 365337 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 9 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 10 | `jwasham/coding-interview-university` | 359663 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 11 | `vinta/awesome-python` | 315879 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `Alishahryar1/free-claude-code` | 49008 | 8004 | Python | 891 stars today | 从您的终端、应用程序、IDE或像OpenClaw这样的手机（支持语音+ ToS友好）免费使用Claude Code、Codex、Pi和OpenCode （ 13亿+免费令牌） | https://github.com/Alishahryar1/free-claude-code |  |
| 2 | `openai/codex` | 117083 | 17850 | Rust | 1,994 stars today | 在您的终端中运行的轻量级编码代理 | https://github.com/openai/codex |  |
| 3 | `MadsLorentzen/ai-job-search` | 34096 | 11903 | Python | 434 stars today | 在您的机器上运行的作业搜索。基于Claude Code构建的人工智能求职框架：评估帖子、定制简历、撰写求职信、准备面试。分叉并拥有它。 | https://github.com/MadsLorentzen/ai-job-search | 新增 |
| 4 | `multica-ai/andrej-karpathy-skills` | 206533 | 21089 | — | 588 stars today | 一个用于改进Claude Code行为的CLAUDE.md文件，源自Andrej Karpathy对LLM编码陷阱的观察。 | https://github.com/multica-ai/andrej-karpathy-skills | 新增 |
| 5 | `makeplane/plane` | 57946 | 5489 | TypeScript | 243 stars today | 🔥🔥🔥 开源JIRA、Linear、Monday和ClickUp替代方案。Plane是一个现代化的项目管理平台，用于管理任务、冲刺、文档和分类。 | https://github.com/makeplane/plane | 新增 |
| 6 | `NousResearch/hermes-agent` | 235824 | 47582 | Python | 896 stars today | 与您一起成长的客服代表 | https://github.com/NousResearch/hermes-agent |  |
| 7 | `anthropics/claude-plugins-community` | 1362 | 153 | Python | 489 stars today | Claude Cowork和Claude Code的社区插件市场。只读镜像—在clau.de/plugin-directory-submission上提交插件。 | https://github.com/anthropics/claude-plugins-community |  |
| 8 | `AprilNEA/OpenLogi` | 15884 | 430 | Rust | 1,097 stars today | ⚡️用Rust编写的Logitech Options +的本地本地优先替代方案🦀—在HID + +上重新映射按钮、DPI和SmartShift。无帐户，无遥测。 | https://github.com/AprilNEA/OpenLogi |  |
| 9 | `apache/maka` | 2922 | 307 | TypeScript | 411 stars today | Apache Maka （孵化）是本地首个AI代理工作区。模型消息、工具调用、工具结果、权限决策和终止事件被记录为仅追加日志。 | https://github.com/apache/maka |  |
| 10 | `PostHog/posthog` | 39004 | 3275 | Python | 83 stars today | 🦔 PostHog是构建自动驾驶产品的领先平台。我们的开发人员工具–人工智能可观察性、分析、会话重播、标记、实验、错误跟踪、日志等–捕获代理诊断问题、发现机会和发布所需的所有上下文…… | https://github.com/PostHog/posthog | 新增 |
| 11 | `openclaw/openclaw` | 387442 | 81347 | TypeScript | 173 stars today | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw | 新增 |
| 12 | `AgriciDaniel/claude-obsidian` | 11925 | 1333 | Python | 310 stars today | Obsidian + Claude Code的自组织AI第二大脑。将任何来源和Claude读取、链接和文件放入您拥有的普通Markdown的一个连接知识图表中。人工智能笔记、个人知识管理（ PKM ）和开源Notion替代方案。基于Ka… | https://github.com/AgriciDaniel/claude-obsidian | 新增 |
| 13 | `rohitg00/ai-engineering-from-scratch` | 48304 | 8505 | Python | 349 stars today | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch | 新增 |
| 14 | `basecamp/omarchy` | 30165 | 3062 | Shell | 1,056 stars today | 漂亮、现代且自以为是的Linux | https://github.com/basecamp/omarchy |  |
| 15 | `tashfeenahmed/freellmapi` | 19792 | 2880 | TypeScript | 174 stars today | 每月74亿个代币。34个免费LLM提供商。635个免费模型端点。全部在一个/v1端点后面，加上任何与OpenAI兼容的自定义端点。智能路由、自动故障转移、加密密钥。仅限个人实验。 | https://github.com/tashfeenahmed/freellmapi | 新增 |
| 16 | `dani-garcia/vaultwarden` | 66129 | 3139 | Rust | 175 stars today | 用Rust编写的非官方Bitwarden兼容服务器，以前称为bitwarden_rs | https://github.com/dani-garcia/vaultwarden |  |
| 17 | `freestylefly/awesome-gpt-image-2` | 15580 | 1649 | JavaScript | 2,449 stars today | Prompt as Code · GPT-Image2 工业级提示词引擎与模板库，530+ 个案例逆向工程，20+ 套工业级模板，并提炼出Skills，持续更新中 | https://github.com/freestylefly/awesome-gpt-image-2 |  |
| 18 | `VoltAgent/awesome-agent-skills` | 31897 | 3399 | — | 602 stars today | 来自官方开发团队和社区的1000多种代理技能的精选集合，与Claude Code、Codex、Gemini CLI、Cursor等兼容。 | https://github.com/VoltAgent/awesome-agent-skills |  |
| 19 | `tinyhumansai/openhuman` | 37281 | 3700 | Rust | 515 stars today | 您的个人人工智能超级智能。一个能够构建本地第一人生记忆的大脑，一个精彩的客服代表队伍和工作流程协调者，以及一位深入的研究人员。 | https://github.com/tinyhumansai/openhuman |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `modular/modular` | 29071 | 3094 | Mojo | 2,285 stars this week | 模块化平台（包括MAX和Mojo ） | https://github.com/modular/modular |  |
| 2 | `harry0703/MoneyPrinterTurbo` | 115974 | 17622 | Python | 10,647 stars this week | 利用 AI 大模型和自动化工作流，根据主题或关键词一键生成高清短视频。Generate HD short videos from a topic or keyword with an automated AI workflow. | https://github.com/harry0703/MoneyPrinterTurbo |  |
| 3 | `AprilNEA/OpenLogi` | 15884 | 430 | Rust | 7,019 stars this week | ⚡️用Rust编写的Logitech Options +的本地本地优先替代方案🦀—在HID + +上重新映射按钮、DPI和SmartShift。无帐户，无遥测。 | https://github.com/AprilNEA/OpenLogi |  |
| 4 | `basecamp/omarchy` | 30167 | 3062 | Shell | 3,934 stars this week | 漂亮、现代且自以为是的Linux | https://github.com/basecamp/omarchy |  |
| 5 | `volcengine/OpenViking` | 32992 | 2513 | Python | 4,048 stars this week | 人工智能代理的自我进化上下文数据库。统一座席记忆、知识抹布和技能。 | https://github.com/volcengine/OpenViking |  |
| 6 | `anthropics/claude-plugins-community` | 1362 | 153 | Python | 877 stars this week | Claude Cowork和Claude Code的社区插件市场。只读镜像—在clau.de/plugin-directory-submission上提交插件。 | https://github.com/anthropics/claude-plugins-community |  |
| 7 | `cordiverse/cordis` | 7410 | 430 | TypeScript | 1,972 stars this week | 时空可组合性元框架 | https://github.com/cordiverse/cordis |  |
| 8 | `public-apis/public-apis` | 469898 | 51818 | Python | 7,069 stars this week | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 9 | `akitaonrails/ai-memory` | 4414 | 321 | Rust | 2,520 stars this week | 针对座席编码CLI的长期记忆解决方案，以及促进不同座席供应商之间切换的解决方案 | https://github.com/akitaonrails/ai-memory | 新增 |
| 10 | `jundot/omlx` | 20552 | 1737 | Python | 1,689 stars this week | LLM推理服务器，具有Apple Silicon的连续批处理和SSD缓存—通过macOS菜单栏进行管理 | https://github.com/jundot/omlx |  |
| 11 | `apache/maka` | 2922 | 307 | TypeScript | 1,313 stars this week | Apache Maka （孵化）是本地首个AI代理工作区。模型消息、工具调用、工具结果、权限决策和终止事件被记录为仅追加日志。 | https://github.com/apache/maka |  |
| 12 | `eneskirca/nodeterm` | 1190 | 123 | TypeScript | 529 stars this week | 用于AI编码代理的基于节点的终端管理器— tmux支持的终端和并行代理会话作为无限平移/缩放画布上的可拖动节点。macOS、Linux和浏览器服务器版。 | https://github.com/eneskirca/nodeterm | 新增 |
| 13 | `Tencent/AI-Infra-Guard` | 5769 | 538 | Python | 1,212 stars this week | 一个全栈AI红色团队平台，通过代理扫描、技能扫描、MCP扫描、AI Infra扫描和LLM越狱评估来保护AI生态系统。 | https://github.com/Tencent/AI-Infra-Guard | 新增 |
| 14 | `cursor/plugins` | 4982 | 407 | TypeScript | 1,832 stars this week | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `block/buzz` | 30492 | 3872 | Rust | 21,856 stars this month | 蜂巢思维沟通平台 | https://github.com/block/buzz |  |
| 2 | `TencentCloud/TencentDB-Agent-Memory` | 24261 | 2230 | TypeScript | 15,093 stars this month | TencentDB Agent Memory是AI Agent的团队级内存中心—将对话、文档和代码转换为四个可重用的内存资产（ Chat Memory、Skill、LLM-Wiki、Code-Graph ） ，这些资产在代理和框架之间进行管理、共享和配备。 | https://github.com/TencentCloud/TencentDB-Agent-Memory |  |
| 3 | `ayghri/i-have-adhd` | 23847 | 1532 | Python | 14,346 stars this month | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 4 | `basecamp/omarchy` | 30167 | 3062 | Shell | 5,853 stars this month | 漂亮、现代且自以为是的Linux | https://github.com/basecamp/omarchy |  |
| 5 | `zhaoxuya520/reverse-skill` | 28736 | 3912 | PowerShell | 19,889 stars this month | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工… | https://github.com/zhaoxuya520/reverse-skill |  |
| 6 | `microsoft/AI-For-Beginners` | 66770 | 12893 | Jupyter Notebook | 14,152 stars this month | 12周， 24课，全民人工智能！ | https://github.com/microsoft/AI-For-Beginners |  |
| 7 | `virgiliojr94/book-to-skill` | 25233 | 2622 | Python | 15,714 stars this month | 将任何技术书籍PDF转化为Claude Code技能—随时准备在您工作时进行学习、参考和使用。 | https://github.com/virgiliojr94/book-to-skill |  |
| 8 | `diegosouzapw/OmniRoute` | 54480 | 7454 | TypeScript | 26,484 stars this month | 永不停止编码。免费MIT AI网关：一个端点， 350个提供商（ 90多个免费） ， 1200多个型号Kimi、Claude、GPT、Gemini、GLM、DeepSeek、MiniMax。适用于Claude Code、Codex、Cursor、OpenCode、Cline和Copilot。配额感知自动回退， RTK +穴居人压缩节省15-95% … | https://github.com/diegosouzapw/OmniRoute |  |
| 9 | `pingdotgg/t3code` | 20363 | 4813 | TypeScript | 5,873 stars this month | — | https://github.com/pingdotgg/t3code |  |
| 10 | `bojieli/ai-agent-book` | 41781 | 4616 | Python | 23,084 stars this month | 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码 | https://github.com/bojieli/ai-agent-book |  |
| 11 | `cactus-compute/needle` | 8965 | 582 | Python | 5,654 stars this month | 14MB基础型号，适用于微型设备；手机、可穿戴设备、智能家居和机器人。 | https://github.com/cactus-compute/needle |  |
| 12 | `citrolabs/ego-lite` | 13257 | 690 | JavaScript | 11,039 stars this month | 人工智能代理运行浏览器自动化的最快浏览器，旨在与您的人工智能代理（如Codex或Claude Code ）共享您登录的浏览器状态，而不会打扰您。零成本，零配置。 | https://github.com/citrolabs/ego-lite |  |
| 13 | `volcengine/OpenViking` | 32992 | 2513 | Python | 5,784 stars this month | 人工智能代理的自我进化上下文数据库。统一座席记忆、知识抹布和技能。 | https://github.com/volcengine/OpenViking |  |
| 14 | `mattpocock/skills` | 235426 | 20060 | Shell | 50,069 stars this month | 真正工程师的技能。直接来自我的.agents目录。 | https://github.com/mattpocock/skills |  |
| 15 | `1jehuang/jcode` | 18464 | 2080 | Rust | 7,469 stars this month | RAM效率最高的线束 | https://github.com/1jehuang/jcode |  |
| 16 | `earendil-works/pi` | 96634 | 11940 | TypeScript | 19,957 stars this month | AI agent toolkit ：统一LLM API、agent loop、TUI、coding agent CLI | https://github.com/earendil-works/pi |  |
| 17 | `megadose/holehe` | 14156 | 1823 | Python | 2,386 stars this month | holehe允许您检查邮件是否在Twitter、Instagram等不同网站上使用，并将检索具有忘记密码功能的网站上的信息。 | https://github.com/megadose/holehe |  |
| 18 | `modular/modular` | 29071 | 3094 | Mojo | 2,539 stars this month | 模块化平台（包括MAX和Mojo ） | https://github.com/modular/modular |  |
| 19 | `akitaonrails/ai-memory` | 4414 | 321 | Rust | 3,151 stars this month | 针对座席编码CLI的长期记忆解决方案，以及促进不同座席供应商之间切换的解决方案 | https://github.com/akitaonrails/ai-memory | 新增 |


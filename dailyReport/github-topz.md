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

**最近一次更新时间**（Asia/Shanghai）： 2026-08-24 09:53:15

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 542375 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 499317 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 469239 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 454487 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 395090 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 387279 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `donnemartin/system-design-primer` | 365643 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 8 | `nilbuild/developer-roadmap` | 365259 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 9 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 10 | `jwasham/coding-interview-university` | 359569 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 11 | `vinta/awesome-python` | 315707 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `openai/codex` | 115337 | 17586 | Rust | 2,715 stars today | 在您的终端中运行的轻量级编码代理 | https://github.com/openai/codex | 新增 |
| 2 | `freestylefly/awesome-gpt-image-2` | 12837 | 1436 | JavaScript | 401 stars today | Prompt as Code · GPT-Image2 工业级提示词引擎与模板库，470+ 个案例逆向工程，20+ 套工业级模板，并提炼出Skills，持续更新中 | https://github.com/freestylefly/awesome-gpt-image-2 | 新增 |
| 3 | `mattpocock/skills` | 233927 | 19949 | Shell | 2,447 stars today | 真正工程师的技能。直接来自我的.agents目录。 | https://github.com/mattpocock/skills |  |
| 4 | `basecamp/omarchy` | 29171 | 2965 | Shell | 750 stars today | 漂亮、现代且自以为是的Linux | https://github.com/basecamp/omarchy | 新增 |
| 5 | `AprilNEA/OpenLogi` | 14993 | 404 | Rust | 1,009 stars today | ⚡️用Rust编写的Logitech Options +的本地本地优先替代方案🦀—在HID + +上重新映射按钮、DPI和SmartShift。无帐户，无遥测。 | https://github.com/AprilNEA/OpenLogi |  |
| 6 | `block/buzz` | 30134 | 3832 | Rust | 410 stars today | 蜂巢思维沟通平台 | https://github.com/block/buzz | 新增 |
| 7 | `apache/maka` | 2369 | 270 | TypeScript | 51 stars today | Apache Maka （孵化）是本地首个AI代理工作区。模型消息、工具调用、工具结果、权限决策和终止事件被记录为仅追加日志。 | https://github.com/apache/maka | 新增 |
| 8 | `Alishahryar1/free-claude-code` | 48005 | 7893 | Python | 1,081 stars today | 从您的终端、应用程序、IDE或像OpenClaw这样的手机（支持语音+ ToS友好）免费使用Claude Code、Codex、Pi和OpenCode （ 13亿+免费令牌） | https://github.com/Alishahryar1/free-claude-code | 新增 |
| 9 | `tinyhumansai/openhuman` | 36784 | 3673 | Rust | 39 stars today | 您的个人人工智能超级智能。一个能够构建本地第一人生记忆的大脑，一个精彩的客服代表队伍和工作流程协调者，以及一位深入的研究人员。 | https://github.com/tinyhumansai/openhuman | 新增 |
| 10 | `affaan-m/ECC` | 242579 | 36722 | JavaScript | 427 stars today | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC | 新增 |
| 11 | `ruvnet/ruflo` | 69094 | 8273 | TypeScript | 131 stars today | 🌊 原始Agent元Harness。部署智能多玩家群体，协调自主工作流程，构建对话式人工智能系统。具有自适应记忆、自我学习智能、RAG集成和原生Claude Code/Codex/Hermes等功能集成 | https://github.com/ruvnet/ruflo | 新增 |
| 12 | `VoltAgent/awesome-agent-skills` | 31323 | 3365 | — | 156 stars today | 来自官方开发团队和社区的1000多种代理技能的精选集合，与Claude Code、Codex、Gemini CLI、Cursor等兼容。 | https://github.com/VoltAgent/awesome-agent-skills | 新增 |
| 13 | `virgiliojr94/book-to-skill` | 24696 | 2584 | Python | 417 stars today | 将任何技术书籍PDF转化为Claude Code技能—随时准备在您工作时进行学习、参考和使用。 | https://github.com/virgiliojr94/book-to-skill | 新增 |
| 14 | `dani-garcia/vaultwarden` | 65970 | 3127 | Rust | 78 stars today | 用Rust编写的非官方Bitwarden兼容服务器，以前称为bitwarden_rs | https://github.com/dani-garcia/vaultwarden | 新增 |
| 15 | `anthropics/claude-plugins-community` | 983 | 127 | Python | 225 stars today | Claude Cowork和Claude Code的社区插件市场。只读镜像—在clau.de/plugin-directory-submission上提交插件。 | https://github.com/anthropics/claude-plugins-community | 新增 |
| 16 | `ripienaar/free-for-dev` | 134454 | 14064 | HTML | 615 stars today | 具有devops和infradev感兴趣的免费层的SaaS、PaaS和IaaS产品列表 | https://github.com/ripienaar/free-for-dev | 新增 |
| 17 | `Comfy-Org/ComfyUI` | 129414 | 15261 | Python | 201 stars today | 最强大、模块化的扩散模型GUI、API和后端，具有图形/节点界面。 | https://github.com/Comfy-Org/ComfyUI | 新增 |
| 18 | `NousResearch/hermes-agent` | 235025 | 47357 | Python | 454 stars today | 与您一起成长的客服代表 | https://github.com/NousResearch/hermes-agent | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `modular/modular` | 28984 | 3077 | Mojo | 2,176 stars this week | 模块化平台（包括MAX和Mojo ） | https://github.com/modular/modular |  |
| 2 | `harry0703/MoneyPrinterTurbo` | 115340 | 17522 | Python | 11,167 stars this week | 利用 AI 大模型和自动化工作流，根据主题或关键词一键生成高清短视频。Generate HD short videos from a topic or keyword with an automated AI workflow. | https://github.com/harry0703/MoneyPrinterTurbo |  |
| 3 | `basecamp/omarchy` | 29172 | 2965 | Shell | 3,660 stars this week | 漂亮、现代且自以为是的Linux | https://github.com/basecamp/omarchy |  |
| 4 | `AprilNEA/OpenLogi` | 14995 | 404 | Rust | 6,078 stars this week | ⚡️用Rust编写的Logitech Options +的本地本地优先替代方案🦀—在HID + +上重新映射按钮、DPI和SmartShift。无帐户，无遥测。 | https://github.com/AprilNEA/OpenLogi |  |
| 5 | `cordiverse/cordis` | 7253 | 420 | TypeScript | 2,725 stars this week | 时空可组合性元框架 | https://github.com/cordiverse/cordis | 新增 |
| 6 | `volcengine/OpenViking` | 32507 | 2483 | Python | 3,799 stars this week | 人工智能代理的自我进化上下文数据库。统一座席记忆、知识抹布和技能。 | https://github.com/volcengine/OpenViking |  |
| 7 | `public-apis/public-apis` | 469239 | 51758 | Python | 8,295 stars this week | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 8 | `jundot/omlx` | 20452 | 1732 | Python | 1,671 stars this week | LLM推理服务器，具有Apple Silicon的连续批处理和SSD缓存—通过macOS菜单栏进行管理 | https://github.com/jundot/omlx |  |
| 9 | `anthropics/claude-plugins-community` | 983 | 127 | Python | 406 stars this week | Claude Cowork和Claude Code的社区插件市场。只读镜像—在clau.de/plugin-directory-submission上提交插件。 | https://github.com/anthropics/claude-plugins-community | 新增 |
| 10 | `cursor/plugins` | 4827 | 396 | TypeScript | 1,761 stars this week | 光标插件规范和官方插件 | https://github.com/cursor/plugins | 新增 |
| 11 | `apache/maka` | 2369 | 270 | TypeScript | 859 stars this week | Apache Maka （孵化）是本地首个AI代理工作区。模型消息、工具调用、工具结果、权限决策和终止事件被记录为仅追加日志。 | https://github.com/apache/maka | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `block/buzz` | 30134 | 3832 | Rust | 24,429 stars this month | 蜂巢思维沟通平台 | https://github.com/block/buzz |  |
| 2 | `TencentCloud/TencentDB-Agent-Memory` | 24039 | 2215 | TypeScript | 14,878 stars this month | TencentDB Agent Memory是AI Agent的团队级内存中心—将对话、文档和代码转换为四个可重用的内存资产（ Chat Memory、Skill、LLM-Wiki、Code-Graph ） ，这些资产在代理和框架之间进行管理、共享和配备。 | https://github.com/TencentCloud/TencentDB-Agent-Memory |  |
| 3 | `ayghri/i-have-adhd` | 23494 | 1503 | Python | 14,450 stars this month | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 4 | `zhaoxuya520/reverse-skill` | 27928 | 3800 | PowerShell | 19,063 stars this month | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工… | https://github.com/zhaoxuya520/reverse-skill |  |
| 5 | `basecamp/omarchy` | 29171 | 2965 | Shell | 4,850 stars this month | 漂亮、现代且自以为是的Linux | https://github.com/basecamp/omarchy |  |
| 6 | `microsoft/AI-For-Beginners` | 66549 | 12862 | Jupyter Notebook | 13,993 stars this month | 12周， 24课，全民人工智能！ | https://github.com/microsoft/AI-For-Beginners |  |
| 7 | `diegosouzapw/OmniRoute` | 53889 | 7373 | TypeScript | 27,573 stars this month | 永不停止编码。免费MIT AI网关：一个端点， 350个提供商（ 90多个免费） ， 1200多个型号Kimi、Claude、GPT、Gemini、GLM、DeepSeek、MiniMax。适用于Claude Code、Codex、Cursor、OpenCode、Cline和Copilot。配额感知自动回退， RTK +穴居人压缩节省15-95% … | https://github.com/diegosouzapw/OmniRoute |  |
| 8 | `virgiliojr94/book-to-skill` | 24696 | 2584 | Python | 15,086 stars this month | 将任何技术书籍PDF转化为Claude Code技能—随时准备在您工作时进行学习、参考和使用。 | https://github.com/virgiliojr94/book-to-skill |  |
| 9 | `pingdotgg/t3code` | 20190 | 4771 | TypeScript | 5,876 stars this month | — | https://github.com/pingdotgg/t3code |  |
| 10 | `citrolabs/ego-lite` | 12986 | 676 | JavaScript | 11,598 stars this month | 人工智能代理运行浏览器自动化的最快浏览器，旨在与您的人工智能代理（如Codex或Claude Code ）共享您登录的浏览器状态，而不会打扰您。零成本，零配置。 | https://github.com/citrolabs/ego-lite |  |
| 11 | `bojieli/ai-agent-book` | 41225 | 4554 | Python | 23,452 stars this month | 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码 | https://github.com/bojieli/ai-agent-book |  |
| 12 | `cactus-compute/needle` | 8756 | 565 | Python | 5,464 stars this month | 14MB基础型号，适用于微型设备；手机、可穿戴设备、智能家居和机器人。 | https://github.com/cactus-compute/needle |  |
| 13 | `volcengine/OpenViking` | 32507 | 2483 | Python | 5,332 stars this month | 人工智能代理的自我进化上下文数据库。统一座席记忆、知识抹布和技能。 | https://github.com/volcengine/OpenViking | 新增 |
| 14 | `mattpocock/skills` | 233927 | 19949 | Shell | 50,629 stars this month | 真正工程师的技能。直接来自我的.agents目录。 | https://github.com/mattpocock/skills |  |
| 15 | `1jehuang/jcode` | 18358 | 2068 | Rust | 7,570 stars this month | RAM效率最高的线束 | https://github.com/1jehuang/jcode |  |
| 16 | `earendil-works/pi` | 95954 | 11873 | TypeScript | 20,046 stars this month | AI agent toolkit ：统一LLM API、agent loop、TUI、coding agent CLI | https://github.com/earendil-works/pi |  |
| 17 | `megadose/holehe` | 14076 | 1822 | Python | 2,328 stars this month | holehe允许您检查邮件是否在Twitter、Instagram等不同网站上使用，并将检索具有忘记密码功能的网站上的信息。 | https://github.com/megadose/holehe |  |
| 18 | `modular/modular` | 28984 | 3077 | Mojo | 2,426 stars this month | 模块化平台（包括MAX和Mojo ） | https://github.com/modular/modular | 新增 |
| 19 | `lyogavin/airllm` | 32291 | 3417 | Jupyter Notebook | 8,428 stars this month | 使用单个4GB GPU的AirLLM 70B推理 | https://github.com/lyogavin/airllm |  |


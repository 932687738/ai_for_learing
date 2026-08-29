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

**最近一次更新时间**（Asia/Shanghai）： 2026-08-29 09:12:27

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 543702 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 500862 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 472347 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 454750 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 395468 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 387935 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `donnemartin/system-design-primer` | 366586 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 8 | `nilbuild/developer-roadmap` | 365788 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 9 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 10 | `jwasham/coding-interview-university` | 359917 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 11 | `vinta/awesome-python` | 316783 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `tt-a1i/archify` | 27475 | 1742 | JavaScript | 4,562 stars today | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify | 新增 |
| 2 | `K-Dense-AI/scientific-agent-skills` | 36614 | 3480 | Python | 720 stars today | 将任何AI特工变成AI科学家。全球175,000多名科学家使用的排名第一的科学代理技能库。163项随时可用的经过验证的技能，以及100多个涵盖生物学、化学、医学和药物发现的科学数据库。兼容Cursor、Claude Code…… | https://github.com/K-Dense-AI/scientific-agent-skills | 新增 |
| 3 | `anthropics/claude-plugins-official` | 35037 | 3936 | Python | 457 stars today | 由Anthropic管理的高质量Claude Code插件的官方目录。 | https://github.com/anthropics/claude-plugins-official | 新增 |
| 4 | `bilawalsidhu/gods-eye-view` | 11100 | 2254 | JavaScript | 3,829 stars today | 浏览器中的间谍卫星模拟器，但数据是真实的。在逼真的3D地球仪上实时开源空间智能。 | https://github.com/bilawalsidhu/gods-eye-view | 新增 |
| 5 | `abhigyanpatwari/GitNexus` | 46158 | 5101 | TypeScript | 202 stars today | GitNexus ：零服务器代码智能引擎- GitNexus是一个完全在浏览器中运行的客户端知识图创建器。放入git存储库（ Github、Gitlab、Azure、Local ）或ZIP文件，并使用内置的Graph RAG Agent获取交互式知识图。… | https://github.com/abhigyanpatwari/GitNexus | 新增 |
| 6 | `JetBrains/go-modern-guidelines` | 2602 | 78 | Go | 574 stars today | 帮助AI编码代理编写现代Go | https://github.com/JetBrains/go-modern-guidelines | 新增 |
| 7 | `calesthio/OpenMontage` | 53319 | 6648 | Python | 1,144 stars today | 全球首个开源代理视频制作系统。12个制作管道、100多个工具、700多个代理技能和生产知识文件。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage | 新增 |
| 8 | `abi/screenshot-to-code` | 75566 | 9219 | Python | 326 stars today | 放入屏幕截图并将其转换为干净的代码（ HTML/Tailwind/React/Vue ） | https://github.com/abi/screenshot-to-code | 新增 |
| 9 | `cursor/plugins` | 5962 | 478 | TypeScript | 246 stars today | 光标插件规范和官方插件 | https://github.com/cursor/plugins | 新增 |
| 10 | `freestylefly/awesome-gpt-image-2` | 24246 | 2396 | JavaScript | 1,687 stars today | Prompt as Code · GPT-Image2 工业级提示词引擎与模板库，530+ 个案例逆向工程，20+ 套工业级模板，并提炼出Skills，持续更新中 | https://github.com/freestylefly/awesome-gpt-image-2 |  |
| 11 | `tailscale/tailcat` | 2715 | 73 | Go | 965 stars today | 像netcat一样，但是在Tailscale的数据平面上，没有Tailscale的控制平面 | https://github.com/tailscale/tailcat | 新增 |
| 12 | `NationalSecurityAgency/ghidra` | 73345 | 8013 | Java | 191 stars today | Ghidra是一个软件逆向工程（ SRE ）框架 | https://github.com/NationalSecurityAgency/ghidra | 新增 |
| 13 | `swoole/typephp` | 813 | 38 | PHP | 188 stars today | 将PHP编译为本机二进制文件 | https://github.com/swoole/typephp | 新增 |
| 14 | `marin-community/marin` | 2900 | 239 | Python | 236 stars today | 基础模型研究和开发的开源框架。 | https://github.com/marin-community/marin | 新增 |
| 15 | `tashfeenahmed/freellmapi` | 21620 | 3061 | TypeScript | 433 stars today | 每月74亿个代币。34个免费LLM提供商。635个免费模型端点。全部在一个/v1端点后面，加上任何与OpenAI兼容的自定义端点。智能路由、自动故障转移、加密密钥。仅限个人实验。 | https://github.com/tashfeenahmed/freellmapi |  |
| 16 | `ChromeDevTools/chrome-devtools-mcp` | 49973 | 3502 | TypeScript | 67 stars today | 适用于编码代理的Chrome开发者工具 | https://github.com/ChromeDevTools/chrome-devtools-mcp | 新增 |
| 17 | `rohitg00/ai-engineering-from-scratch` | 50624 | 8780 | Python | 703 stars today | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 18 | `DietrichGebert/ponytail` | 115384 | 6310 | JavaScript | 1,396 stars today | 让你的人工智能代理像房间里最懒惰的高级开发人员一样思考。最好的代码是你从未写过的代码。 | https://github.com/DietrichGebert/ponytail | 新增 |
| 19 | `google/googletest` | 39176 | 10872 | C++ | 156 stars today | GoogleTest - Google测试和模拟框架 | https://github.com/google/googletest | 新增 |
| 20 | `livekit/agents` | 13340 | 3630 | Python | 22 stars today | 构建实时语音AI代理的框架 🤖🎙️📹 | https://github.com/livekit/agents | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `anthropics/claude-plugins-community` | 2590 | 213 | Python | 2,207 stars this week | Claude Cowork和Claude Code的社区插件市场。只读镜像—在clau.de/plugin-directory-submission上提交插件。 | https://github.com/anthropics/claude-plugins-community |  |
| 2 | `freestylefly/awesome-gpt-image-2` | 24246 | 2397 | JavaScript | 12,877 stars this week | Prompt as Code · GPT-Image2 工业级提示词引擎与模板库，530+ 个案例逆向工程，20+ 套工业级模板，并提炼出Skills，持续更新中 | https://github.com/freestylefly/awesome-gpt-image-2 | 新增 |
| 3 | `basecamp/omarchy` | 33512 | 3474 | Shell | 5,942 stars this week | 漂亮、现代且自以为是的Linux | https://github.com/basecamp/omarchy |  |
| 4 | `openai/codex` | 119567 | 18254 | Rust | 9,109 stars this week | 在您的终端中运行的轻量级编码代理 | https://github.com/openai/codex | 新增 |
| 5 | `tt-a1i/archify` | 27482 | 1742 | JavaScript | 11,099 stars this week | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify | 新增 |
| 6 | `AprilNEA/OpenLogi` | 17415 | 499 | Rust | 4,825 stars this week | ⚡️用Rust编写的Logitech Options +的本地本地优先替代方案🦀—在HID + +上重新映射按钮、DPI和SmartShift。无帐户，无遥测。 | https://github.com/AprilNEA/OpenLogi |  |
| 7 | `apache/maka` | 3910 | 364 | TypeScript | 1,918 stars this week | Apache Maka （孵化）是本地首个AI代理工作区。模型消息、工具调用、工具结果、权限决策和终止事件被记录为仅追加日志。 | https://github.com/apache/maka |  |
| 8 | `tashfeenahmed/freellmapi` | 21620 | 3061 | TypeScript | 2,162 stars this week | 每月74亿个代币。34个免费LLM提供商。635个免费模型端点。全部在一个/v1端点后面，加上任何与OpenAI兼容的自定义端点。智能路由、自动故障转移、加密密钥。仅限个人实验。 | https://github.com/tashfeenahmed/freellmapi | 新增 |
| 9 | `modular/modular` | 29305 | 3118 | Mojo | 875 stars this week | 模块化平台（包括MAX和Mojo ） | https://github.com/modular/modular |  |
| 10 | `cursor/plugins` | 5962 | 478 | TypeScript | 1,594 stars this week | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 11 | `MadsLorentzen/ai-job-search` | 37738 | 12772 | Python | 4,828 stars this week | 在您的机器上运行的作业搜索。基于Claude Code构建的人工智能求职框架：评估帖子、定制简历、撰写求职信、准备面试。分叉并拥有它。 | https://github.com/MadsLorentzen/ai-job-search | 新增 |
| 12 | `tinyhumansai/openhuman` | 38728 | 3802 | Rust | 2,353 stars this week | 您的个人人工智能超级智能。一个能够构建本地第一人生记忆的大脑，一个精彩的客服代表队伍和工作流程协调者，以及一位深入的研究人员。 | https://github.com/tinyhumansai/openhuman | 新增 |
| 13 | `anthropics/claude-plugins-official` | 35037 | 3936 | Python | 1,281 stars this week | 由Anthropic管理的高质量Claude Code插件的官方目录。 | https://github.com/anthropics/claude-plugins-official | 新增 |
| 14 | `VoltAgent/awesome-agent-skills` | 33063 | 3484 | — | 2,372 stars this week | 来自官方开发团队和社区的1000多种代理技能的精选集合，与Claude Code、Codex、Gemini CLI、Cursor等兼容。 | https://github.com/VoltAgent/awesome-agent-skills | 新增 |
| 15 | `PostHog/posthog` | 39428 | 3308 | Python | 1,270 stars this week | 🦔 PostHog是构建自动驾驶产品的领先平台。我们的开发人员工具–人工智能可观察性、分析、会话重播、标记、实验、错误跟踪、日志等–捕获代理诊断问题、发现机会和发布所需的所有上下文…… | https://github.com/PostHog/posthog | 新增 |
| 16 | `rohitg00/ai-engineering-from-scratch` | 50624 | 8780 | Python | 3,263 stars this week | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch | 新增 |
| 17 | `Alishahryar1/free-claude-code` | 51201 | 8246 | Python | 4,769 stars this week | 从您的终端、应用程序、IDE或像OpenClaw这样的手机（支持语音+ ToS友好）免费使用Claude Code、Codex、Pi和OpenCode等（ 13亿+免费令牌） | https://github.com/Alishahryar1/free-claude-code | 新增 |
| 18 | `chaitanyagiri/munder-difflin` | 5226 | 629 | JavaScript | 1,853 stars this week | 局部多药剂线束 | https://github.com/chaitanyagiri/munder-difflin | 新增 |
| 19 | `bookorbit/bookorbit` | 3514 | 211 | TypeScript | 806 stars this week | BookOrbit ：您的阅读空间 | https://github.com/bookorbit/bookorbit | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `basecamp/omarchy` | 33512 | 3474 | Shell | 9,083 stars this month | 漂亮、现代且自以为是的Linux | https://github.com/basecamp/omarchy |  |
| 2 | `TencentCloud/TencentDB-Agent-Memory` | 25040 | 2323 | TypeScript | 15,798 stars this month | TencentDB Agent Memory是AI Agent的团队级内存中心—将对话、文档和代码转换为四个可重用的内存资产（ Chat Memory、Skill、LLM-Wiki、Code-Graph ） ，这些资产在代理和框架之间进行管理、共享和配备。 | https://github.com/TencentCloud/TencentDB-Agent-Memory |  |
| 3 | `freestylefly/awesome-gpt-image-2` | 24247 | 2397 | JavaScript | 15,580 stars this month | Prompt as Code · GPT-Image2 工业级提示词引擎与模板库，530+ 个案例逆向工程，20+ 套工业级模板，并提炼出Skills，持续更新中 | https://github.com/freestylefly/awesome-gpt-image-2 | 新增 |
| 4 | `zhaoxuya520/reverse-skill` | 30135 | 4122 | PowerShell | 21,291 stars this month | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工… | https://github.com/zhaoxuya520/reverse-skill |  |
| 5 | `anthropics/claude-plugins-community` | 2590 | 213 | Python | 2,246 stars this month | Claude Cowork和Claude Code的社区插件市场。只读镜像—在clau.de/plugin-directory-submission上提交插件。 | https://github.com/anthropics/claude-plugins-community | 新增 |
| 6 | `cactus-compute/needle` | 9583 | 613 | Python | 6,279 stars this month | 14MB基础型号，适用于微型设备；手机、可穿戴设备、智能家居和机器人。 | https://github.com/cactus-compute/needle |  |
| 7 | `volcengine/OpenViking` | 34150 | 2598 | Python | 6,661 stars this month | 人工智能代理的自我进化上下文数据库。统一座席记忆、知识抹布和技能。 | https://github.com/volcengine/OpenViking |  |
| 8 | `apache/maka` | 3910 | 364 | TypeScript | 2,992 stars this month | Apache Maka （孵化）是本地首个AI代理工作区。模型消息、工具调用、工具结果、权限决策和终止事件被记录为仅追加日志。 | https://github.com/apache/maka | 新增 |
| 9 | `usekaneo/kaneo` | 8630 | 724 | TypeScript | 4,703 stars this month | 你需要的一🎯切。没有什么你不需要的。开源项目管理适合您，而不是对您不利。 | https://github.com/usekaneo/kaneo | 新增 |
| 10 | `AprilNEA/OpenLogi` | 17415 | 499 | Rust | 9,621 stars this month | ⚡️用Rust编写的Logitech Options +的本地本地优先替代方案🦀—在HID + +上重新映射按钮、DPI和SmartShift。无帐户，无遥测。 | https://github.com/AprilNEA/OpenLogi | 新增 |
| 11 | `microsoft/AI-For-Beginners` | 67548 | 13019 | Jupyter Notebook | 14,701 stars this month | 12周， 24课，全民人工智能！ | https://github.com/microsoft/AI-For-Beginners |  |
| 12 | `modular/modular` | 29305 | 3118 | Mojo | 2,765 stars this month | 模块化平台（包括MAX和Mojo ） | https://github.com/modular/modular |  |
| 13 | `pingdotgg/t3code` | 20893 | 5002 | TypeScript | 5,636 stars this month | — | https://github.com/pingdotgg/t3code |  |
| 14 | `virgiliojr94/book-to-skill` | 26695 | 2767 | Python | 15,782 stars this month | 将任何技术书籍PDF转化为Claude Code技能—随时准备在您工作时进行学习、参考和使用。 | https://github.com/virgiliojr94/book-to-skill |  |
| 15 | `diegosouzapw/OmniRoute` | 57560 | 7923 | TypeScript | 25,061 stars this month | 永不停止编码。免费MIT AI网关：一个端点， 350个提供商（ 90多个免费） ， 1200多个型号Kimi、Claude、GPT、Gemini、GLM、DeepSeek、MiniMax。适用于Claude Code、Codex、Cursor、OpenCode、Cline和Copilot。配额感知自动回退， RTK +穴居人压缩节省15-95% … | https://github.com/diegosouzapw/OmniRoute |  |
| 16 | `ayghri/i-have-adhd` | 25346 | 1600 | Python | 13,080 stars this month | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 17 | `block/buzz` | 31311 | 3997 | Rust | 16,342 stars this month | 蜂巢思维沟通平台 | https://github.com/block/buzz |  |
| 18 | `lyogavin/airllm` | 32953 | 3471 | Jupyter Notebook | 8,902 stars this month | 使用单个4GB GPU的AirLLM 70B推理 | https://github.com/lyogavin/airllm | 新增 |
| 19 | `megadose/holehe` | 14396 | 1837 | Python | 2,604 stars this month | holehe允许您检查邮件是否在Twitter、Instagram等不同网站上使用，并将检索具有忘记密码功能的网站上的信息。 | https://github.com/megadose/holehe |  |
| 20 | `marin-community/marin` | 2900 | 239 | Python | 1,650 stars this month | 基础模型研究和开发的开源框架。 | https://github.com/marin-community/marin | 新增 |
| 21 | `unclebob/swarm-forge` | 2979 | 304 | Clojure | 1,587 stars this month | 用于协调多个AI代理的简单工具。 | https://github.com/unclebob/swarm-forge | 新增 |
| 22 | `earendil-works/pi` | 98767 | 12225 | TypeScript | 19,558 stars this month | AI agent toolkit ：统一LLM API、agent loop、TUI、coding agent CLI | https://github.com/earendil-works/pi |  |
| 23 | `citrolabs/ego-lite` | 14185 | 726 | JavaScript | 8,592 stars this month | 人工智能代理运行浏览器自动化的最快浏览器，旨在与您的人工智能代理（如Codex或Claude Code ）共享您登录的浏览器状态，而不会打扰您。零成本，零配置。 | https://github.com/citrolabs/ego-lite |  |


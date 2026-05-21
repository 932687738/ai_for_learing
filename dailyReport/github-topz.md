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

**最近一次更新时间**（Asia/Shanghai）： 2026-05-21 08:27:06

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 502855 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 468454 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 445190 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 436149 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 388593 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 373553 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 355145 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 349572 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 347150 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 298727 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
| 11 | `awesome-selfhosted/awesome-selfhosted` | 294092 | 可自行部署的各类自由软件网络服务与 Web 应用清单。 | https://github.com/awesome-selfhosted/awesome-selfhosted | 新增 |

---
## Trending 页面快照（HTML 抓取）

**说明**：与上方「全局 Star Search」数据源不同；本段按 GitHub trending 页的 **daily / weekly / monthly** 各拉一页并解析。**若前端改版导致选择器失效，需更新解析逻辑。**

- **标记**列：三个 `since` 子表**各自独立**对照本次拉取前文件中该小节表格已出现的 `owner/repo`；新出现的行标 **新增**。下次拉取会先清空上一轮「新增」再重算（只保留相对**上一版文件**的新仓库）。

### 今日 trending（since=daily）

**页面**： `https://github.com/trending?since=daily`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `colbymchenry/codegraph` | 9484 | 580 | TypeScript | 2,123 stars today | Claude Code、Codex、Cursor和OpenCode的预索引代码知识图—更少的代币、更少的工具调用、100%本地 | https://github.com/colbymchenry/codegraph |  |
| 2 | `Imbad0202/academic-research-skills` | 16146 | 1444 | Python | 1,667 stars today | Claude Code的学术研究技能：研究→撰写→评审→修订→最终确定 | https://github.com/Imbad0202/academic-research-skills |  |
| 3 | `tinyhumansai/openhuman` | 23607 | 2112 | Rust | 3,394 stars today | 您的个人人工智能超级智能。私密、简单且功能强大。 | https://github.com/tinyhumansai/openhuman |  |
| 4 | `multica-ai/andrej-karpathy-skills` | 140787 | 14444 | — | 2,679 stars today | 一个用于改进Claude Code行为的CLAUDE.md文件，源自Andrej Karpathy对LLM编码陷阱的观察。 | https://github.com/multica-ai/andrej-karpathy-skills |  |
| 5 | `rohitg00/ai-engineering-from-scratch` | 9537 | 1941 | Python | 765 stars today | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch | 新增 |
| 6 | `HKUDS/CLI-Anything` | 38528 | 3662 | Python | 890 stars today | "CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub: https://clianything.cc/ | https://github.com/HKUDS/CLI-Anything |  |
| 7 | `can1357/oh-my-pi` | 5394 | 454 | TypeScript | 270 stars today | 终端的AI编码代理—哈希锚定编辑、优化工具线束、LSP、Python、浏览器、子代理等 | https://github.com/can1357/oh-my-pi | 新增 |
| 8 | `obra/superpowers` | 199996 | 17834 | Shell | 1,743 stars today | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers |  |
| 9 | `anthropics/claude-plugins-official` | 20775 | 2544 | Python | 674 stars today | 由Anthropic管理的高质量Claude Code插件的官方目录。 | https://github.com/anthropics/claude-plugins-official |  |
| 10 | `msitarzewski/agency-agents` | 102821 | 16946 | Shell | 1,636 stars today | 一个完整的人工智能机构，触手可及--从前端向导到Reddit社区忍者，从奇思妙想的注入者到现实检查者。每位客服代表都是具有个性、流程和经过验证的交付成果的专家。 | https://github.com/msitarzewski/agency-agents |  |
| 11 | `rmyndharis/OpenWA` | 4851 | 983 | TypeScript | 741 stars today | 免费、开源、自托管的WhatsApp API网关 | https://github.com/rmyndharis/OpenWA | 新增 |
| 12 | `truelockmc/streambert` | 2983 | 246 | JavaScript | 582 stars today | 一个跨平台的Electron桌面应用程序，用于流式传输和下载世界上的任何电影、电视剧或动漫。零广告和跟踪 | https://github.com/truelockmc/streambert | 新增 |
| 13 | `opentoonz/opentoonz` | 6331 | 732 | C++ | 236 stars today | OpenToonz -一款开源全功能2D动画创作软件 | https://github.com/opentoonz/opentoonz | 新增 |
| 14 | `zakirullin/files.md` | 2202 | 50 | Go | 429 stars today | 🌱 私密、安静的思考空间。适用于.md文件的简单应用程序。 | https://github.com/zakirullin/files.md | 新增 |
| 15 | `rohitg00/agentmemory` | 15120 | 1250 | TypeScript | 1,080 stars today | # 1基于真实世界基准的AI编码代理持久内存 | https://github.com/rohitg00/agentmemory |  |
| 16 | `ggml-org/llama.cpp` | 111837 | 18506 | C++ | 309 stars today | C/C + +中的LLM推理 | https://github.com/ggml-org/llama.cpp | 新增 |
| 17 | `HKUDS/ViMax` | 6054 | 980 | Python | 674 stars today | "ViMax ： Agentic Video Generation （导演、编剧、制片人和视频生成器一体机）" | https://github.com/HKUDS/ViMax |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `tinyhumansai/openhuman` | 23607 | 2112 | Rust | 19,177 stars this week | 您的个人人工智能超级智能。私密、简单且功能强大。 | https://github.com/tinyhumansai/openhuman |  |
| 2 | `rohitg00/agentmemory` | 15120 | 1250 | TypeScript | 7,976 stars this week | # 1基于真实世界基准的AI编码代理持久内存 | https://github.com/rohitg00/agentmemory |  |
| 3 | `colbymchenry/codegraph` | 9484 | 580 | TypeScript | 6,731 stars this week | Claude Code、Codex、Cursor和OpenCode的预索引代码知识图—更少的代币、更少的工具调用、100%本地 | https://github.com/colbymchenry/codegraph |  |
| 4 | `CloakHQ/CloakBrowser` | 17590 | 1373 | Python | 8,348 stars this week | Stealth Chromium可通过每次机器人检测测试。插入式剧作家更换源级指纹补丁，通过30/30测试 | https://github.com/CloakHQ/CloakBrowser |  |
| 5 | `ruvnet/RuView` | 61955 | 8140 | Rust | 8,028 stars this week | π RuView将商用WiFi信号转化为实时空间智能、生命体征监测和存在检测--所有这些都无需一个像素的视频。 | https://github.com/ruvnet/RuView |  |
| 6 | `Imbad0202/academic-research-skills` | 16146 | 1444 | Python | 8,737 stars this week | Claude Code的学术研究技能：研究→撰写→评审→修订→最终确定 | https://github.com/Imbad0202/academic-research-skills |  |
| 7 | `oven-sh/bun` | 92142 | 4611 | Rust | 2,472 stars this week | 令人难以置信的快速JavaScript运行时、捆绑程序、测试运行程序和包管理器–所有功能于一身 | https://github.com/oven-sh/bun |  |
| 8 | `facebook/pyrefly` | 6348 | 374 | Rust | 629 stars this week | Python的快速类型检查器和语言服务器 | https://github.com/facebook/pyrefly |  |
| 9 | `mattpocock/skills` | 96929 | 8556 | Shell | 18,368 stars this week | 真正工程师的技能。直接来自我的.claude目录。 | https://github.com/mattpocock/skills |  |
| 10 | `yikart/AiToEarn` | 15771 | 2567 | TypeScript | 3,160 stars this week | 让我们使用人工智能来赚取收入！ | https://github.com/yikart/AiToEarn |  |
| 11 | `obra/superpowers` | 199996 | 17834 | Shell | 10,851 stars this week | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers |  |
| 12 | `datawhalechina/easy-vibe` | 13529 | 1292 | JavaScript | 2,984 stars this week | 💻 vibe coding 2026 ·您的第一个现代编程课程，供初学者一步一步掌握。 | https://github.com/datawhalechina/easy-vibe | 新增 |
| 13 | `millionco/react-doctor` | 10462 | 337 | TypeScript | 1,345 stars this week | 您的代理写入了错误的React。这会捕获它 | https://github.com/millionco/react-doctor |  |
| 14 | `anthropics/skills` | 138246 | 16304 | Python | 4,749 stars this week | 座席技能的公共存储库 | https://github.com/anthropics/skills | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `mattpocock/skills` | 96929 | 8556 | Shell | 80,029 stars this month | 真正工程师的技能。直接来自我的.claude目录。 | https://github.com/mattpocock/skills |  |
| 2 | `Alishahryar1/free-claude-code` | 26952 | 4004 | Python | 24,944 stars this month | 在终端中免费使用claude-code、VSCode扩展或像OpenClaw这样的不和谐（支持语音） | https://github.com/Alishahryar1/free-claude-code |  |
| 3 | `CloakHQ/CloakBrowser` | 17590 | 1373 | Python | 16,037 stars this month | Stealth Chromium可通过每次机器人检测测试。插入式剧作家更换源级指纹补丁，通过30/30测试 | https://github.com/CloakHQ/CloakBrowser |  |
| 4 | `multica-ai/andrej-karpathy-skills` | 140787 | 14444 | — | 76,112 stars this month | 一个用于改进Claude Code行为的CLAUDE.md文件，源自Andrej Karpathy对LLM编码陷阱的观察。 | https://github.com/multica-ai/andrej-karpathy-skills |  |
| 5 | `AIDC-AI/Pixelle-Video` | 18683 | 2658 | Python | 14,190 stars this month | 🚀 AI 全自动短视频引擎 · AI Fully Automated Short Video Engine | https://github.com/AIDC-AI/Pixelle-Video |  |
| 6 | `rohitg00/agentmemory` | 15121 | 1250 | TypeScript | 13,014 stars this month | # 1基于真实世界基准的AI编码代理持久内存 | https://github.com/rohitg00/agentmemory |  |
| 7 | `anthropics/financial-services` | 26223 | 3659 | Python | 18,624 stars this month | — | https://github.com/anthropics/financial-services |  |
| 8 | `soxoj/maigret` | 29680 | 2128 | Python | 10,198 stars this month | 通过用户名从3000多个网站🕵️‍♂️收集个人档案 | https://github.com/soxoj/maigret |  |
| 9 | `Z4nzu/hackingtool` | 75806 | 8546 | Python | 17,826 stars this month | 面向黑客的一体化黑客工具 | https://github.com/Z4nzu/hackingtool |  |
| 10 | `TauricResearch/TradingAgents` | 77777 | 15147 | Python | 26,200 stars this month | TradingAgent ：多代理LLM金融交易框架 | https://github.com/TauricResearch/TradingAgents |  |
| 11 | `Imbad0202/academic-research-skills` | 16146 | 1444 | Python | 12,191 stars this month | Claude Code的学术研究技能：研究→撰写→评审→修订→最终确定 | https://github.com/Imbad0202/academic-research-skills |  |
| 12 | `addyosmani/agent-skills` | 44246 | 4877 | Shell | 26,157 stars this month | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 13 | `colbymchenry/codegraph` | 9484 | 580 | TypeScript | 7,557 stars this month | Claude Code、Codex、Cursor和OpenCode的预索引代码知识图—更少的代币、更少的工具调用、100%本地 | https://github.com/colbymchenry/codegraph | 新增 |
| 14 | `decolua/9router` | 12887 | 1930 | JavaScript | 10,123 stars this month | 无限免费AI编码。通过40多家供应商将Claude Code、Codex、Cursor、Cline、Copilot、Antigravity连接到免费的Claude/GPT/Gemini。自动回退， RTK -40%代币，从未达到限制。 | https://github.com/decolua/9router |  |
| 15 | `Anil-matcha/Open-Generative-AI` | 16239 | 2734 | JavaScript | 10,937 stars this month | 人工智能视频平台的开源替代品—免费的人工智能图像和视频生成工作室，拥有200多种型号（ Flux、Midjourney、Kling、Sora、Veo ）。无内容过滤器。自托管，麻省理工学院许可。 | https://github.com/Anil-matcha/Open-Generative-AI |  |
| 16 | `ruvnet/ruflo` | 53596 | 6065 | TypeScript | 21,381 stars this month | 🌊 Claude的领先代理编排平台。部署智能多智能体群，协调自主工作流程，构建对话式人工智能系统。具有企业级架构、自学群体智能、RAG集成和本地Claude Code/… | https://github.com/ruvnet/ruflo |  |


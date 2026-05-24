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

**最近一次更新时间**（Asia/Shanghai）： 2026-05-24 08:16:52

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 503808 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 469401 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 445347 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 436622 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 388835 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 374181 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 355336 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 349984 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 347307 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 299246 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
| 11 | `awesome-selfhosted/awesome-selfhosted` | 294829 | 可自行部署的各类自由软件网络服务与 Web 应用清单。 | https://github.com/awesome-selfhosted/awesome-selfhosted |  |

---
## Trending 页面快照（HTML 抓取）

**说明**：与上方「全局 Star Search」数据源不同；本段按 GitHub trending 页的 **daily / weekly / monthly** 各拉一页并解析。**若前端改版导致选择器失效，需更新解析逻辑。**

- **标记**列：三个 `since` 子表**各自独立**对照本次拉取前文件中该小节表格已出现的 `owner/repo`；新出现的行标 **新增**。下次拉取会先清空上一轮「新增」再重算（只保留相对**上一版文件**的新仓库）。

### 今日 trending（since=daily）

**页面**： `https://github.com/trending?since=daily`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `Lum1104/Understand-Anything` | 21487 | 1918 | TypeScript | 2,299 stars today | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Lum1104/Understand-Anything |  |
| 2 | `anthropics/claude-plugins-official` | 26419 | 2855 | Python | 2,193 stars today | 由Anthropic管理的高质量Claude Code插件的官方目录。 | https://github.com/anthropics/claude-plugins-official |  |
| 3 | `colbymchenry/codegraph` | 19415 | 1073 | TypeScript | 2,456 stars today | Claude Code、Codex、Cursor、OpenCode和Hermes Agent的预索引代码知识图—代币更少，工具调用更少， 100%本地化 | https://github.com/colbymchenry/codegraph |  |
| 4 | `rohitg00/ai-engineering-from-scratch` | 13733 | 2567 | Python | 1,521 stars today | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 5 | `Fincept-Corporation/FinceptTerminal` | 23109 | 3189 | Python | 545 stars today | FinceptTerminal是一款现代金融应用程序，提供先进的市场分析、投资研究和经济数据工具，专为在用户友好的环境中进行交互式探索和数据驱动的决策而设计。 | https://github.com/Fincept-Corporation/FinceptTerminal |  |
| 6 | `multica-ai/andrej-karpathy-skills` | 149591 | 15336 | — | 3,507 stars today | 一个用于改进Claude Code行为的CLAUDE.md文件，源自Andrej Karpathy对LLM编码陷阱的观察。 | https://github.com/multica-ai/andrej-karpathy-skills | 新增 |
| 7 | `dotnet/skills` | 2740 | 209 | C# | 266 stars today | 用于使用.NET和C #协助AI编码代理的技能的存储库 | https://github.com/dotnet/skills |  |
| 8 | `ChromeDevTools/chrome-devtools-mcp` | 41325 | 2624 | TypeScript | 435 stars today | 适用于编码代理的Chrome开发者工具 | https://github.com/ChromeDevTools/chrome-devtools-mcp |  |
| 9 | `mukul975/Anthropic-Cybersecurity-Skills` | 7392 | 1008 | Python | 281 stars today | 人工智能代理的754种结构化网络安全技能·映射到5个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND和NIST AI RMF · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20多个平台· 26个安全数据…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills | 新增 |
| 10 | `presenton/presenton` | 6351 | 1114 | TypeScript | 241 stars today | 开源AI演示生成器和API （ Gamma、Beautiful AI、Decktopus Alternative ） | https://github.com/presenton/presenton | 新增 |
| 11 | `multica-ai/multica` | 31907 | 3858 | TypeScript | 410 stars today | 开源托管代理平台。将编码代理转变为真正的队友—分配任务、跟踪进度、复合技能。 | https://github.com/multica-ai/multica | 新增 |
| 12 | `trimstray/the-book-of-secret-knowledge` | 223831 | 13426 | — | 628 stars today | 一系列鼓舞人心的列表、手册、备忘单、博客、黑客、单行工具、cli/web工具等。 | https://github.com/trimstray/the-book-of-secret-knowledge |  |
| 13 | `odoo/odoo` | 51474 | 32529 | Python | 386 stars today | Odoo。开源应用助您拓展业务。 | https://github.com/odoo/odoo |  |
| 14 | `NVlabs/LongLive` | 1807 | 168 | Python | 94 stars today | LongLive 2.0 ： Infra - Long Video Gen | https://github.com/NVlabs/LongLive | 新增 |
| 15 | `yt-dlp/yt-dlp` | 164946 | 13858 | Python | 759 stars today | 功能丰富的命令行音频/视频下载器 | https://github.com/yt-dlp/yt-dlp |  |
| 16 | `janestreet/magic-trace` | 5848 | 180 | OCaml | 68 stars today | magic-trace收集并显示流程正在执行的高分辨率跟踪 | https://github.com/janestreet/magic-trace | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `colbymchenry/codegraph` | 19415 | 1073 | TypeScript | 15,909 stars this week | Claude Code、Codex、Cursor、OpenCode和Hermes Agent的预索引代码知识图—代币更少，工具调用更少， 100%本地化 | https://github.com/colbymchenry/codegraph |  |
| 2 | `tinyhumansai/openhuman` | 26352 | 2432 | Rust | 16,288 stars this week | 您的个人人工智能超级智能。私密、简单且功能强大。 | https://github.com/tinyhumansai/openhuman |  |
| 3 | `Imbad0202/academic-research-skills` | 19701 | 1693 | Python | 11,691 stars this week | Claude Code的学术研究技能：研究→撰写→评审→修订→最终确定 | https://github.com/Imbad0202/academic-research-skills |  |
| 4 | `ruvnet/RuView` | 64728 | 8569 | Rust | 6,741 stars this week | π RuView将商用WiFi信号转化为实时空间智能、生命体征监测和存在检测--所有这些都无需一个像素的视频。 | https://github.com/ruvnet/RuView |  |
| 5 | `rohitg00/agentmemory` | 16837 | 1387 | TypeScript | 6,734 stars this week | # 1基于真实世界基准的AI编码代理持久内存 | https://github.com/rohitg00/agentmemory |  |
| 6 | `supertone-inc/supertonic` | 9788 | 1007 | Swift | 3,281 stars this week | 闪电般的快速、设备上、多语言TTS —通过ONNX本地运行。 | https://github.com/supertone-inc/supertonic |  |
| 7 | `CloakHQ/CloakBrowser` | 19554 | 1548 | Python | 6,991 stars this week | Stealth Chromium可通过每次机器人检测测试。插入式剧作家更换源级指纹补丁，通过30/30测试 | https://github.com/CloakHQ/CloakBrowser |  |
| 8 | `HKUDS/ViMax` | 6979 | 1102 | Python | 2,790 stars this week | "ViMax ： Agentic Video Generation （导演、编剧、制片人和视频生成器一体机）" | https://github.com/HKUDS/ViMax |  |
| 9 | `humanlayer/12-factor-agents` | 21924 | 1648 | TypeScript | 2,035 stars this week | 我们可以使用哪些原则来构建基于LLM的软件，这些软件实际上足以交付给生产客户？ | https://github.com/humanlayer/12-factor-agents |  |
| 10 | `rohitg00/ai-engineering-from-scratch` | 13734 | 2567 | Python | 5,026 stars this week | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 11 | `datawhalechina/easy-vibe` | 14230 | 1356 | JavaScript | 2,711 stars this week | 💻 vibe coding 2026 ·您的第一个现代编程课程，供初学者一步一步掌握。 | https://github.com/datawhalechina/easy-vibe |  |
| 12 | `Lum1104/Understand-Anything` | 21489 | 1918 | TypeScript | 4,880 stars this week | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Lum1104/Understand-Anything | 新增 |
| 13 | `obra/superpowers` | 203968 | 18164 | Shell | 10,367 stars this week | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers |  |
| 14 | `can1357/oh-my-pi` | 6737 | 546 | TypeScript | 2,073 stars this week | 终端的AI编码代理—哈希锚定编辑、优化工具线束、LSP、Python、浏览器、子代理等 | https://github.com/can1357/oh-my-pi | 新增 |
| 15 | `K-Dense-AI/scientific-agent-skills` | 25360 | 2659 | Python | 2,522 stars this week | 一套随时可用的代理技能，用于研究、科学、工程、分析、财务和写作。 | https://github.com/K-Dense-AI/scientific-agent-skills | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `mattpocock/skills` | 102370 | 9053 | Shell | 85,195 stars this month | 真正工程师的技能。直接来自我的.claude目录。 | https://github.com/mattpocock/skills |  |
| 2 | `colbymchenry/codegraph` | 19415 | 1073 | TypeScript | 17,463 stars this month | Claude Code、Codex、Cursor、OpenCode和Hermes Agent的预索引代码知识图—代币更少，工具调用更少， 100%本地化 | https://github.com/colbymchenry/codegraph |  |
| 3 | `anthropics/financial-services` | 27032 | 3790 | Python | 19,289 stars this month | — | https://github.com/anthropics/financial-services |  |
| 4 | `CloakHQ/CloakBrowser` | 19554 | 1548 | Python | 17,847 stars this month | Stealth Chromium可通过每次机器人检测测试。插入式剧作家更换源级指纹补丁，通过30/30测试 | https://github.com/CloakHQ/CloakBrowser |  |
| 5 | `rohitg00/agentmemory` | 16837 | 1387 | TypeScript | 14,753 stars this month | # 1基于真实世界基准的AI编码代理持久内存 | https://github.com/rohitg00/agentmemory |  |
| 6 | `Alishahryar1/free-claude-code` | 28597 | 4284 | Python | 24,512 stars this month | 在终端中免费使用claude-code、VSCode扩展或像OpenClaw这样的不和谐（支持语音） | https://github.com/Alishahryar1/free-claude-code |  |
| 7 | `ComposioHQ/awesome-codex-skills` | 11258 | 1074 | Python | 10,326 stars this month | 用于跨Codex CLI和API自动化工作流程的实用Codex技能精选列表。 | https://github.com/ComposioHQ/awesome-codex-skills | 新增 |
| 8 | `Imbad0202/academic-research-skills` | 19701 | 1693 | Python | 16,073 stars this month | Claude Code的学术研究技能：研究→撰写→评审→修订→最终确定 | https://github.com/Imbad0202/academic-research-skills |  |
| 9 | `multica-ai/andrej-karpathy-skills` | 149592 | 15336 | — | 70,773 stars this month | 一个用于改进Claude Code行为的CLAUDE.md文件，源自Andrej Karpathy对LLM编码陷阱的观察。 | https://github.com/multica-ai/andrej-karpathy-skills |  |
| 10 | `soxoj/maigret` | 30054 | 2153 | Python | 10,535 stars this month | 通过用户名从3000多个网站🕵️‍♂️收集个人档案 | https://github.com/soxoj/maigret |  |
| 11 | `TauricResearch/TradingAgents` | 78915 | 15378 | Python | 26,704 stars this month | TradingAgent ：多代理LLM金融交易框架 | https://github.com/TauricResearch/TradingAgents |  |
| 12 | `AIDC-AI/Pixelle-Video` | 19356 | 2749 | Python | 13,218 stars this month | 🚀 AI 全自动短视频引擎 · AI Fully Automated Short Video Engine | https://github.com/AIDC-AI/Pixelle-Video |  |
| 13 | `decolua/9router` | 13792 | 2066 | JavaScript | 10,813 stars this month | 无限免费AI编码。通过40多家供应商将Claude Code、Codex、Cursor、Cline、Copilot、Antigravity连接到免费的Claude/GPT/Gemini。自动回退， RTK -40%代币，从未达到限制。 | https://github.com/decolua/9router |  |
| 14 | `refactoringhq/tolaria` | 11372 | 810 | TypeScript | 10,527 stars this month | 用于管理降价知识库的桌面应用程序 | https://github.com/refactoringhq/tolaria |  |
| 15 | `ruvnet/ruflo` | 54472 | 6185 | TypeScript | 21,850 stars this month | 🌊 Claude的领先代理编排平台。部署智能多智能体群，协调自主工作流程，构建对话式人工智能系统。具有企业级架构、自学群体智能、RAG集成和本地Claude Code/… | https://github.com/ruvnet/ruflo |  |
| 16 | `bytedance/UI-TARS-desktop` | 35050 | 3521 | TypeScript | 5,666 stars this month | 开源多模态人工智能代理堆栈：连接尖端人工智能模型和代理基础设施 | https://github.com/bytedance/UI-TARS-desktop |  |
| 17 | `Z4nzu/hackingtool` | 76315 | 8590 | Python | 16,237 stars this month | 面向黑客的一体化黑客工具 | https://github.com/Z4nzu/hackingtool |  |
| 18 | `addyosmani/agent-skills` | 45156 | 4995 | Shell | 23,686 stars this month | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 19 | `HKUDS/ViMax` | 6979 | 1102 | Python | 4,152 stars this month | "ViMax ： Agentic Video Generation （导演、编剧、制片人和视频生成器一体机）" | https://github.com/HKUDS/ViMax | 新增 |
| 20 | `mattpocock/sandcastle` | 4867 | 518 | TypeScript | 3,929 stars this month | 使用sandcastle.run ()在TypeScript中编排沙盒编码代理 | https://github.com/mattpocock/sandcastle | 新增 |


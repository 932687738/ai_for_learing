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

**最近一次更新时间**（Asia/Shanghai）： 2026-05-25 09:51:08

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 504287 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 469747 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 445383 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 436998 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 388924 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 374420 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 355397 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 350128 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 347356 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 299426 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
| 11 | `awesome-selfhosted/awesome-selfhosted` | 294829 | 可自行部署的各类自由软件网络服务与 Web 应用清单。 | https://github.com/awesome-selfhosted/awesome-selfhosted |  |

---
## Trending 页面快照（HTML 抓取）

**说明**：与上方「全局 Star Search」数据源不同；本段按 GitHub trending 页的 **daily / weekly / monthly** 各拉一页并解析。**若前端改版导致选择器失效，需更新解析逻辑。**

- **标记**列：三个 `since` 子表**各自独立**对照本次拉取前文件中该小节表格已出现的 `owner/repo`；新出现的行标 **新增**。下次拉取会先清空上一轮「新增」再重算（只保留相对**上一版文件**的新仓库）。

### 今日 trending（since=daily）

**页面**： `https://github.com/trending?since=daily`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `Lum1104/Understand-Anything` | 26185 | 2262 | TypeScript | 3,999 stars today | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Lum1104/Understand-Anything |  |
| 2 | `rohitg00/ai-engineering-from-scratch` | 16151 | 2864 | Python | 1,853 stars today | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 3 | `anthropics/claude-plugins-official` | 27274 | 2906 | Python | 1,173 stars today | 由Anthropic管理的高质量Claude Code插件的官方目录。 | https://github.com/anthropics/claude-plugins-official |  |
| 4 | `anthropics/knowledge-work-plugins` | 14092 | 1742 | Python | 550 stars today | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins | 新增 |
| 5 | `multica-ai/andrej-karpathy-skills` | 152220 | 15607 | — | 2,551 stars today | 一个用于改进Claude Code行为的CLAUDE.md文件，源自Andrej Karpathy对LLM编码陷阱的观察。 | https://github.com/multica-ai/andrej-karpathy-skills |  |
| 6 | `earendil-works/pi` | 53973 | 6445 | TypeScript | 456 stars today | AI代理工具包：编码代理CLI、统一LLM API、TUI和Web UI库、Slack bot、vLLM pods | https://github.com/earendil-works/pi | 新增 |
| 7 | `Alishahryar1/free-claude-code` | 29188 | 4384 | Python | 553 stars today | 在终端中免费使用claude-code、VSCode扩展或像OpenClaw这样的不和谐（支持语音） | https://github.com/Alishahryar1/free-claude-code | 新增 |
| 8 | `colbymchenry/codegraph` | 22195 | 1228 | TypeScript | 3,003 stars today | Claude Code、Codex、Cursor、OpenCode和Hermes Agent的预索引代码知识图—代币更少，工具调用更少， 100%本地化 | https://github.com/colbymchenry/codegraph |  |
| 9 | `multica-ai/multica` | 32531 | 3908 | TypeScript | 585 stars today | 开源托管代理平台。将编码代理转变为真正的队友—分配任务、跟踪进度、复合技能。 | https://github.com/multica-ai/multica |  |
| 10 | `shiyu-coder/Kronos` | 25809 | 4496 | Python | 106 stars today | Kronos ：金融市场语言的基础模型 | https://github.com/shiyu-coder/Kronos | 新增 |
| 11 | `manaflow-ai/cmux` | 19042 | 1449 | Swift | 696 stars today | 基于Ghostty的macOS终端，带有AI编码代理的垂直选项卡和通知 | https://github.com/manaflow-ai/cmux | 新增 |
| 12 | `666ghj/MiroFish` | 62173 | 9730 | Python | 197 stars today | A Simple and Universal Swarm Intelligence Engine, Predicting Anything. 简洁通用的群体智能引擎，预测万物 | https://github.com/666ghj/MiroFish | 新增 |
| 13 | `codecrafters-io/build-your-own-x` | 504287 | 47831 | Markdown | 550 stars today | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x | 新增 |
| 14 | `dotnet/skills` | 2968 | 219 | C# | 183 stars today | 用于使用.NET和C #协助AI编码代理的技能的存储库 | https://github.com/dotnet/skills |  |
| 15 | `blakeblackshear/frigate` | 32867 | 3180 | TypeScript | 181 stars today | 支持IP摄像机实时本地物体检测的NVR | https://github.com/blakeblackshear/frigate | 新增 |
| 16 | `mukul975/Anthropic-Cybersecurity-Skills` | 8385 | 1060 | Python | 930 stars today | 人工智能代理的754种结构化网络安全技能·映射到5个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND和NIST AI RMF · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20多个平台· 26个安全数据…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `colbymchenry/codegraph` | 22195 | 1228 | TypeScript | 18,136 stars this week | Claude Code、Codex、Cursor、OpenCode和Hermes Agent的预索引代码知识图—代币更少，工具调用更少， 100%本地化 | https://github.com/colbymchenry/codegraph |  |
| 2 | `tinyhumansai/openhuman` | 27193 | 2523 | Rust | 15,194 stars this week | 您的个人人工智能超级智能。私密、简单且功能强大。 | https://github.com/tinyhumansai/openhuman |  |
| 3 | `Imbad0202/academic-research-skills` | 20643 | 1759 | Python | 11,401 stars this week | Claude Code的学术研究技能：研究→撰写→评审→修订→最终确定 | https://github.com/Imbad0202/academic-research-skills |  |
| 4 | `rohitg00/ai-engineering-from-scratch` | 16153 | 2864 | Python | 6,944 stars this week | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 5 | `ruvnet/RuView` | 65441 | 8651 | Rust | 6,461 stars this week | π RuView将商用WiFi信号转化为实时空间智能、生命体征监测和存在检测--所有这些都无需一个像素的视频。 | https://github.com/ruvnet/RuView |  |
| 6 | `rohitg00/agentmemory` | 17385 | 1423 | TypeScript | 6,391 stars this week | # 1基于真实世界基准的AI编码代理持久内存 | https://github.com/rohitg00/agentmemory |  |
| 7 | `Lum1104/Understand-Anything` | 26186 | 2262 | TypeScript | 9,102 stars this week | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Lum1104/Understand-Anything |  |
| 8 | `CloakHQ/CloakBrowser` | 20369 | 1613 | Python | 6,892 stars this week | Stealth Chromium可通过每次机器人检测测试。插入式剧作家更换源级指纹补丁，通过30/30测试 | https://github.com/CloakHQ/CloakBrowser |  |
| 9 | `supertone-inc/supertonic` | 10182 | 1044 | Swift | 2,726 stars this week | 闪电般的快速、设备上、多语言TTS —通过ONNX本地运行。 | https://github.com/supertone-inc/supertonic |  |
| 10 | `can1357/oh-my-pi` | 7063 | 570 | TypeScript | 2,361 stars this week | 终端的AI编码代理—哈希锚定编辑、优化工具线束、LSP、Python、浏览器、子代理等 | https://github.com/can1357/oh-my-pi |  |
| 11 | `datawhalechina/easy-vibe` | 14503 | 1381 | JavaScript | 2,406 stars this week | 💻 vibe coding 2026 ·您的第一个现代编程课程，供初学者一步一步掌握。 | https://github.com/datawhalechina/easy-vibe |  |
| 12 | `obra/superpowers` | 205006 | 18265 | Shell | 10,171 stars this week | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers |  |
| 13 | `K-Dense-AI/scientific-agent-skills` | 25641 | 2680 | Python | 2,001 stars this week | 一套随时可用的代理技能，用于研究、科学、工程、分析、财务和写作。 | https://github.com/K-Dense-AI/scientific-agent-skills |  |
| 14 | `stablyai/orca` | 3249 | 220 | TypeScript | 554 stars this week | ORCA是使用并行代理的下一代IDE。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca | 新增 |
| 15 | `HKUDS/CLI-Anything` | 40078 | 3784 | Python | 4,759 stars this week | "CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub: https://clianything.cc/ | https://github.com/HKUDS/CLI-Anything | 新增 |
| 16 | `yikart/AiToEarn` | 16324 | 2633 | TypeScript | 1,765 stars this week | 让我们使用人工智能来赚取收入！ | https://github.com/yikart/AiToEarn | 新增 |
| 17 | `cursor/plugins` | 739 | 85 | TypeScript | 303 stars this week | 光标插件规范和官方插件 | https://github.com/cursor/plugins | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `mattpocock/skills` | 103677 | 9174 | Shell | 85,843 stars this month | 真正工程师的技能。直接来自我的.claude目录。 | https://github.com/mattpocock/skills |  |
| 2 | `colbymchenry/codegraph` | 22199 | 1228 | TypeScript | 20,676 stars this month | Claude Code、Codex、Cursor、OpenCode和Hermes Agent的预索引代码知识图—代币更少，工具调用更少， 100%本地化 | https://github.com/colbymchenry/codegraph |  |
| 3 | `anthropics/financial-services` | 27331 | 3835 | Python | 19,626 stars this month | — | https://github.com/anthropics/financial-services |  |
| 4 | `CloakHQ/CloakBrowser` | 20370 | 1613 | Python | 18,723 stars this month | Stealth Chromium可通过每次机器人检测测试。插入式剧作家更换源级指纹补丁，通过30/30测试 | https://github.com/CloakHQ/CloakBrowser |  |
| 5 | `rohitg00/agentmemory` | 17386 | 1423 | TypeScript | 15,283 stars this month | # 1基于真实世界基准的AI编码代理持久内存 | https://github.com/rohitg00/agentmemory |  |
| 6 | `Imbad0202/academic-research-skills` | 20643 | 1759 | Python | 16,935 stars this month | Claude Code的学术研究技能：研究→撰写→评审→修订→最终确定 | https://github.com/Imbad0202/academic-research-skills |  |
| 7 | `ComposioHQ/awesome-codex-skills` | 11491 | 1094 | Python | 10,414 stars this month | 用于跨Codex CLI和API自动化工作流程的实用Codex技能精选列表。 | https://github.com/ComposioHQ/awesome-codex-skills |  |
| 8 | `multica-ai/andrej-karpathy-skills` | 152221 | 15607 | — | 69,590 stars this month | 一个用于改进Claude Code行为的CLAUDE.md文件，源自Andrej Karpathy对LLM编码陷阱的观察。 | https://github.com/multica-ai/andrej-karpathy-skills |  |
| 9 | `soxoj/maigret` | 30225 | 2162 | Python | 10,671 stars this month | 通过用户名从3000多个网站🕵️‍♂️收集个人档案 | https://github.com/soxoj/maigret |  |
| 10 | `TauricResearch/TradingAgents` | 79262 | 15453 | Python | 26,930 stars this month | TradingAgent ：多代理LLM金融交易框架 | https://github.com/TauricResearch/TradingAgents |  |
| 11 | `Alishahryar1/free-claude-code` | 29188 | 4384 | Python | 22,082 stars this month | 在终端中免费使用claude-code、VSCode扩展或像OpenClaw这样的不和谐（支持语音） | https://github.com/Alishahryar1/free-claude-code |  |
| 12 | `AIDC-AI/Pixelle-Video` | 19559 | 2774 | Python | 13,052 stars this month | 🚀 AI 全自动短视频引擎 · AI Fully Automated Short Video Engine | https://github.com/AIDC-AI/Pixelle-Video |  |
| 13 | `decolua/9router` | 14035 | 2097 | JavaScript | 11,024 stars this month | 无限免费AI编码。通过40多家供应商将Claude Code、Codex、Cursor、Cline、Copilot、Antigravity连接到免费的Claude/GPT/Gemini。自动回退， RTK -40%代币，从未达到限制。 | https://github.com/decolua/9router |  |
| 14 | `HKUDS/ViMax` | 7344 | 1142 | Python | 4,531 stars this month | "ViMax ： Agentic Video Generation （导演、编剧、制片人和视频生成器一体机）" | https://github.com/HKUDS/ViMax |  |
| 15 | `ruvnet/ruflo` | 54819 | 6230 | TypeScript | 22,025 stars this month | 🌊 Claude的领先代理编排平台。部署智能多智能体群，协调自主工作流程，构建对话式人工智能系统。具有企业级架构、自学群体智能、RAG集成和本地Claude Code/… | https://github.com/ruvnet/ruflo |  |
| 16 | `yikart/AiToEarn` | 16325 | 2633 | TypeScript | 7,332 stars this month | 让我们使用人工智能来赚取收入！ | https://github.com/yikart/AiToEarn | 新增 |
| 17 | `bytedance/UI-TARS-desktop` | 35160 | 3531 | TypeScript | 5,740 stars this month | 开源多模态人工智能代理堆栈：连接尖端人工智能模型和代理基础设施 | https://github.com/bytedance/UI-TARS-desktop |  |
| 18 | `CJackHwang/ds2api` | 4580 | 1463 | Go | 3,378 stars this month | DeepSeek兼容中间件接口：围棋技术探索项目，专注于高并发协议适配。它作为将各种Web协议转换为标准化格式的参考实现。 | https://github.com/CJackHwang/ds2api | 新增 |
| 19 | `addyosmani/agent-skills` | 45419 | 5028 | Shell | 22,991 stars this month | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 20 | `mattpocock/sandcastle` | 4985 | 524 | TypeScript | 4,042 stars this month | 使用sandcastle.run ()在TypeScript中编排沙盒编码代理 | https://github.com/mattpocock/sandcastle |  |


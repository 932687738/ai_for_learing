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

**最近一次更新时间**（Asia/Shanghai）： 2026-05-22 09:14:37

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 503044 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 468804 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 445253 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 436419 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 388693 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 373766 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 355202 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 349724 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 347196 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 298900 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
| 11 | `awesome-selfhosted/awesome-selfhosted` | 294092 | 可自行部署的各类自由软件网络服务与 Web 应用清单。 | https://github.com/awesome-selfhosted/awesome-selfhosted |  |

---
## Trending 页面快照（HTML 抓取）

**说明**：与上方「全局 Star Search」数据源不同；本段按 GitHub trending 页的 **daily / weekly / monthly** 各拉一页并解析。**若前端改版导致选择器失效，需更新解析逻辑。**

- **标记**列：三个 `since` 子表**各自独立**对照本次拉取前文件中该小节表格已出现的 `owner/repo`；新出现的行标 **新增**。下次拉取会先清空上一轮「新增」再重算（只保留相对**上一版文件**的新仓库）。

### 今日 trending（since=daily）

**页面**： `https://github.com/trending?since=daily`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `anthropics/claude-plugins-official` | 22476 | 2647 | Python | 682 stars today | 由Anthropic管理的高质量Claude Code插件的官方目录。 | https://github.com/anthropics/claude-plugins-official |  |
| 2 | `colbymchenry/codegraph` | 13544 | 771 | TypeScript | 4,294 stars today | Claude Code、Codex、Cursor和OpenCode的预索引代码知识图—更少的代币、更少的工具调用、100%本地 | https://github.com/colbymchenry/codegraph |  |
| 3 | `multica-ai/andrej-karpathy-skills` | 143210 | 14685 | — | 2,614 stars today | 一个用于改进Claude Code行为的CLAUDE.md文件，源自Andrej Karpathy对LLM编码陷阱的观察。 | https://github.com/multica-ai/andrej-karpathy-skills |  |
| 4 | `dotnet/skills` | 2201 | 178 | C# | 129 stars today | 用于使用.NET和C #协助AI编码代理的技能的存储库 | https://github.com/dotnet/skills | 新增 |
| 5 | `obra/superpowers` | 201531 | 17953 | Shell | 1,576 stars today | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers |  |
| 6 | `HKUDS/CLI-Anything` | 39135 | 3713 | Python | 656 stars today | "CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub: https://clianything.cc/ | https://github.com/HKUDS/CLI-Anything |  |
| 7 | `rmyndharis/OpenWA` | 5419 | 1084 | TypeScript | 730 stars today | 免费、开源、自托管的WhatsApp API网关 | https://github.com/rmyndharis/OpenWA |  |
| 8 | `ChromeDevTools/chrome-devtools-mcp` | 40493 | 2572 | TypeScript | 151 stars today | 适用于编码代理的Chrome开发者工具 | https://github.com/ChromeDevTools/chrome-devtools-mcp | 新增 |
| 9 | `rohitg00/ai-engineering-from-scratch` | 10733 | 2122 | Python | 1,333 stars today | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 10 | `teng-lin/notebooklm-py` | 14380 | 1993 | Python | 186 stars today | Google NotebookLM的非官方Python API和代理技能。通过Python、CLI和AI代理（如Claude Code、Codex和OpenClaw ）完全以编程方式访问NotebookLM的功能，包括Web UI不公开的功能。 | https://github.com/teng-lin/notebooklm-py | 新增 |
| 11 | `can1357/oh-my-pi` | 5853 | 479 | TypeScript | 500 stars today | 终端的AI编码代理—哈希锚定编辑、优化工具线束、LSP、Python、浏览器、子代理等 | https://github.com/can1357/oh-my-pi |  |
| 12 | `antoinezambelli/forge` | 1494 | 76 | Python | 398 stars today | 用于自托管LLM工具调用和多步骤代理工作流程的Python框架 | https://github.com/antoinezambelli/forge | 新增 |
| 13 | `multica-ai/multica` | 30741 | 3735 | Go | 534 stars today | 开源托管代理平台。将编码代理转变为真正的队友—分配任务、跟踪进度、复合技能。 | https://github.com/multica-ai/multica | 新增 |
| 14 | `Imbad0202/academic-research-skills` | 18190 | 1567 | Python | 2,579 stars today | Claude Code的学术研究技能：研究→撰写→评审→修订→最终确定 | https://github.com/Imbad0202/academic-research-skills |  |
| 15 | `trimstray/the-book-of-secret-knowledge` | 222452 | 13325 | — | 756 stars today | 一系列鼓舞人心的列表、手册、备忘单、博客、黑客、单行工具、cli/web工具等。 | https://github.com/trimstray/the-book-of-secret-knowledge | 新增 |
| 16 | `truelockmc/streambert` | 4001 | 312 | JavaScript | 1,094 stars today | 一个跨平台的Electron桌面应用程序，用于流式传输和下载世界上的任何电影、电视剧或动漫。零广告和跟踪 | https://github.com/truelockmc/streambert |  |
| 17 | `msitarzewski/agency-agents` | 103678 | 17052 | Shell | 1,018 stars today | 一个完整的人工智能机构，触手可及--从前端向导到Reddit社区忍者，从奇思妙想的注入者到现实检查者。每位客服代表都是具有个性、流程和经过验证的交付成果的专家。 | https://github.com/msitarzewski/agency-agents |  |
| 18 | `alireza0/s-ui` | 8927 | 1503 | Go | 27 stars today | 高级Web面板•专为SagerNet/Sing-Box打造 | https://github.com/alireza0/s-ui | 新增 |
| 19 | `Lum1104/Understand-Anything` | 16652 | 1560 | TypeScript | 666 stars today | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Lum1104/Understand-Anything | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `tinyhumansai/openhuman` | 24875 | 2243 | Rust | 17,399 stars this week | 您的个人人工智能超级智能。私密、简单且功能强大。 | https://github.com/tinyhumansai/openhuman |  |
| 2 | `colbymchenry/codegraph` | 13547 | 771 | TypeScript | 10,749 stars this week | Claude Code、Codex、Cursor和OpenCode的预索引代码知识图—更少的代币、更少的工具调用、100%本地 | https://github.com/colbymchenry/codegraph |  |
| 3 | `Imbad0202/academic-research-skills` | 18190 | 1567 | Python | 10,737 stars this week | Claude Code的学术研究技能：研究→撰写→评审→修订→最终确定 | https://github.com/Imbad0202/academic-research-skills |  |
| 4 | `supertone-inc/supertonic` | 9153 | 939 | Swift | 4,120 stars this week | 闪电般的快速、设备上、多语言TTS —通过ONNX本地运行。 | https://github.com/supertone-inc/supertonic | 新增 |
| 5 | `rohitg00/agentmemory` | 15840 | 1311 | TypeScript | 7,000 stars this week | # 1基于真实世界基准的AI编码代理持久内存 | https://github.com/rohitg00/agentmemory |  |
| 6 | `CloakHQ/CloakBrowser` | 18232 | 1440 | Python | 7,769 stars this week | Stealth Chromium可通过每次机器人检测测试。插入式剧作家更换源级指纹补丁，通过30/30测试 | https://github.com/CloakHQ/CloakBrowser |  |
| 7 | `ruvnet/RuView` | 63068 | 8332 | Rust | 7,636 stars this week | π RuView将商用WiFi信号转化为实时空间智能、生命体征监测和存在检测--所有这些都无需一个像素的视频。 | https://github.com/ruvnet/RuView |  |
| 8 | `oven-sh/bun` | 92197 | 4632 | Rust | 2,377 stars this week | 令人难以置信的快速JavaScript运行时、捆绑程序、测试运行程序和包管理器–所有功能于一身 | https://github.com/oven-sh/bun |  |
| 9 | `humanlayer/12-factor-agents` | 21572 | 1623 | TypeScript | 1,729 stars this week | 我们可以使用哪些原则来构建基于LLM的软件，这些软件实际上足以交付给生产客户？ | https://github.com/humanlayer/12-factor-agents | 新增 |
| 10 | `datawhalechina/easy-vibe` | 13778 | 1324 | JavaScript | 2,979 stars this week | 💻 vibe coding 2026 ·您的第一个现代编程课程，供初学者一步一步掌握。 | https://github.com/datawhalechina/easy-vibe |  |
| 11 | `facebook/pyrefly` | 6389 | 379 | Rust | 572 stars this week | Python的快速类型检查器和语言服务器 | https://github.com/facebook/pyrefly |  |
| 12 | `obra/superpowers` | 201532 | 17953 | Shell | 10,688 stars this week | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers |  |
| 13 | `HKUDS/ViMax` | 6465 | 1018 | Python | 2,495 stars this week | "ViMax ： Agentic Video Generation （导演、编剧、制片人和视频生成器一体机）" | https://github.com/HKUDS/ViMax | 新增 |
| 14 | `mattpocock/skills` | 99112 | 8765 | Shell | 17,535 stars this week | 真正工程师的技能。直接来自我的.claude目录。 | https://github.com/mattpocock/skills |  |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `mattpocock/skills` | 99112 | 8765 | Shell | 81,739 stars this month | 真正工程师的技能。直接来自我的.claude目录。 | https://github.com/mattpocock/skills |  |
| 2 | `Alishahryar1/free-claude-code` | 27502 | 4082 | Python | 25,325 stars this month | 在终端中免费使用claude-code、VSCode扩展或像OpenClaw这样的不和谐（支持语音） | https://github.com/Alishahryar1/free-claude-code |  |
| 3 | `CloakHQ/CloakBrowser` | 18232 | 1440 | Python | 16,687 stars this month | Stealth Chromium可通过每次机器人检测测试。插入式剧作家更换源级指纹补丁，通过30/30测试 | https://github.com/CloakHQ/CloakBrowser |  |
| 4 | `rohitg00/agentmemory` | 15840 | 1311 | TypeScript | 13,721 stars this month | # 1基于真实世界基准的AI编码代理持久内存 | https://github.com/rohitg00/agentmemory |  |
| 5 | `anthropics/financial-services` | 26496 | 3701 | Python | 18,821 stars this month | — | https://github.com/anthropics/financial-services |  |
| 6 | `huggingface/ml-intern` | 9748 | 1038 | Python | 9,693 stars this month | 🤗 ml-intern ：一名开源机器学习工程师，负责阅读论文、训练模型和运送机器学习模型 | https://github.com/huggingface/ml-intern | 新增 |
| 7 | `colbymchenry/codegraph` | 13547 | 771 | TypeScript | 11,378 stars this month | Claude Code、Codex、Cursor和OpenCode的预索引代码知识图—更少的代币、更少的工具调用、100%本地 | https://github.com/colbymchenry/codegraph |  |
| 8 | `multica-ai/andrej-karpathy-skills` | 143210 | 14685 | — | 73,297 stars this month | 一个用于改进Claude Code行为的CLAUDE.md文件，源自Andrej Karpathy对LLM编码陷阱的观察。 | https://github.com/multica-ai/andrej-karpathy-skills |  |
| 9 | `AIDC-AI/Pixelle-Video` | 18994 | 2700 | Python | 14,121 stars this month | 🚀 AI 全自动短视频引擎 · AI Fully Automated Short Video Engine | https://github.com/AIDC-AI/Pixelle-Video |  |
| 10 | `soxoj/maigret` | 29808 | 2140 | Python | 10,311 stars this month | 通过用户名从3000多个网站🕵️‍♂️收集个人档案 | https://github.com/soxoj/maigret |  |
| 11 | `Imbad0202/academic-research-skills` | 18190 | 1567 | Python | 14,440 stars this month | Claude Code的学术研究技能：研究→撰写→评审→修订→最终确定 | https://github.com/Imbad0202/academic-research-skills |  |
| 12 | `TauricResearch/TradingAgents` | 78269 | 15249 | Python | 26,428 stars this month | TradingAgent ：多代理LLM金融交易框架 | https://github.com/TauricResearch/TradingAgents |  |
| 13 | `Z4nzu/hackingtool` | 76008 | 8556 | Python | 17,698 stars this month | 面向黑客的一体化黑客工具 | https://github.com/Z4nzu/hackingtool |  |
| 14 | `decolua/9router` | 13240 | 1980 | JavaScript | 10,342 stars this month | 无限免费AI编码。通过40多家供应商将Claude Code、Codex、Cursor、Cline、Copilot、Antigravity连接到免费的Claude/GPT/Gemini。自动回退， RTK -40%代币，从未达到限制。 | https://github.com/decolua/9router |  |
| 15 | `addyosmani/agent-skills` | 44597 | 4925 | Shell | 25,904 stars this month | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 16 | `ruvnet/ruflo` | 53933 | 6110 | TypeScript | 21,570 stars this month | 🌊 Claude的领先代理编排平台。部署智能多智能体群，协调自主工作流程，构建对话式人工智能系统。具有企业级架构、自学群体智能、RAG集成和本地Claude Code/… | https://github.com/ruvnet/ruflo |  |
| 17 | `Anil-matcha/Open-Generative-AI` | 16448 | 2765 | JavaScript | 10,989 stars this month | 人工智能视频平台的开源替代品—免费的人工智能图像和视频生成工作室，拥有200多种型号（ Flux、Midjourney、Kling、Sora、Veo ）。无内容过滤器。自托管，麻省理工学院许可。 | https://github.com/Anil-matcha/Open-Generative-AI |  |


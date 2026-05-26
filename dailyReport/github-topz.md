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

**最近一次更新时间**（Asia/Shanghai）： 2026-05-26 10:14:11

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 504691 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 470054 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 445412 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 437190 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 388987 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 374654 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 355455 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 350303 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 347397 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 299591 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
| 11 | `awesome-selfhosted/awesome-selfhosted` | 295209 | 可自行部署的各类自由软件网络服务与 Web 应用清单。 | https://github.com/awesome-selfhosted/awesome-selfhosted |  |
| 12 | `practical-tutorials/project-based-learning` | 266609 | 基于项目的教程精选列表 | https://github.com/practical-tutorials/project-based-learning |  |
| 13 | `facebook/react` | 245279 | 用于构建 Web 与原生用户界面的 React 视图库（含多端生态）。 | https://github.com/facebook/react |  |

---
## Trending 页面快照（HTML 抓取）

**说明**：与上方「全局 Star Search」数据源不同；本段按 GitHub trending 页的 **daily / weekly / monthly** 各拉一页并解析。**若前端改版导致选择器失效，需更新解析逻辑。**

- **标记**列：三个 `since` 子表**各自独立**对照本次拉取前文件中该小节表格已出现的 `owner/repo`；新出现的行标 **新增**。下次拉取会先清空上一轮「新增」再重算（只保留相对**上一版文件**的新仓库）。

### 今日 trending（since=daily）

**页面**： `https://github.com/trending?since=daily`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `Lum1104/Understand-Anything` | 31457 | 2584 | TypeScript | 5,604 stars today | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Lum1104/Understand-Anything |  |
| 2 | `anthropics/knowledge-work-plugins` | 15565 | 1876 | Python | 1,441 stars today | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins |  |
| 3 | `rohitg00/ai-engineering-from-scratch` | 18762 | 3175 | Python | 3,154 stars today | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 4 | `affaan-m/ECC` | 192475 | 29786 | JavaScript | 2,025 stars today | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 5 | `mukul975/Anthropic-Cybersecurity-Skills` | 9298 | 1139 | Python | 1,004 stars today | 人工智能代理的754种结构化网络安全技能·映射到5个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND和NIST AI RMF · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20多个平台· 26个安全数据…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills |  |
| 6 | `colbymchenry/codegraph` | 25291 | 1402 | TypeScript | 3,161 stars today | Claude Code、Codex、Cursor、OpenCode和Hermes Agent的预索引代码知识图—代币更少，工具调用更少， 100%本地化 | https://github.com/colbymchenry/codegraph |  |
| 7 | `manaflow-ai/cmux` | 19524 | 1474 | Swift | 603 stars today | 基于Ghostty的macOS终端，带有AI编码代理的垂直选项卡和通知 | https://github.com/manaflow-ai/cmux |  |
| 8 | `multica-ai/andrej-karpathy-skills` | 155120 | 15900 | — | 2,749 stars today | 一个用于改进Claude Code行为的CLAUDE.md文件，源自Andrej Karpathy对LLM编码陷阱的观察。 | https://github.com/multica-ai/andrej-karpathy-skills |  |
| 9 | `Fincept-Corporation/FinceptTerminal` | 23909 | 3287 | Python | 317 stars today | FinceptTerminal是一款现代金融应用程序，提供先进的市场分析、投资研究和经济数据工具，专为在用户友好的环境中进行交互式探索和数据驱动的决策而设计。 | https://github.com/Fincept-Corporation/FinceptTerminal |  |
| 10 | `paperless-ngx/paperless-ngx` | 41361 | 2748 | Python | 176 stars today | 社区支持的增压文档管理系统：扫描、索引和存档您的所有文档 | https://github.com/paperless-ngx/paperless-ngx |  |
| 11 | `anthropics/claude-cookbooks` | 44051 | 5052 | Jupyter Notebook | 141 stars today | 一系列笔记本/食谱，展示了一些有趣而有效的使用Claude的方法。 | https://github.com/anthropics/claude-cookbooks |  |
| 12 | `Leonxlnx/taste-skill` | 19808 | 1658 | Shell | 264 stars today | 品味技能-让您的人工智能有良好的品味。阻止人工智能产生无聊的通用斜坡 | https://github.com/Leonxlnx/taste-skill |  |
| 13 | `moeru-ai/airi` | 39756 | 4023 | TypeScript | 62 stars today | 💖🧸 自我托管，你拥有的Grok Companion ，一个包含外府灵魂的容器，将它们带入我们的世界的网络生活，希望达到Neuro-sama的高度。能够实时语音聊天、Minecraft、Factorio播放。支持Web/macOS/Windows。 | https://github.com/moeru-ai/airi |  |
| 14 | `shiyu-coder/Kronos` | 26039 | 4521 | Python | 245 stars today | Kronos ：金融市场语言的基础模型 | https://github.com/shiyu-coder/Kronos |  |
| 15 | `Axorax/awesome-free-apps` | 4577 | 233 | JavaScript | 192 stars today | 适用于PC和移动设备的最佳免费应用程序精选列表 | https://github.com/Axorax/awesome-free-apps |  |
| 16 | `hardikpandya/stop-slop` | 4441 | 385 | — | 345 stars today | 从散文中删除AI TELLS的技能文件 | https://github.com/hardikpandya/stop-slop |  |
| 17 | `garrytan/gstack` | 102539 | 15291 | TypeScript | 640 stars today | 使用Garry Tan确切的Claude Code设置： 23个自以为是的工具，分别担任首席执行官、设计师、工程经理、发布经理、文档工程师和QA | https://github.com/garrytan/gstack |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `colbymchenry/codegraph` | 25304 | 1403 | TypeScript | 20,208 stars this week | Claude Code、Codex、Cursor、OpenCode和Hermes Agent的预索引代码知识图—代币更少，工具调用更少， 100%本地化 | https://github.com/colbymchenry/codegraph |  |
| 2 | `tinyhumansai/openhuman` | 27827 | 2574 | Rust | 11,906 stars this week | 您的个人人工智能超级智能。私密、简单且功能强大。 | https://github.com/tinyhumansai/openhuman |  |
| 3 | `Lum1104/Understand-Anything` | 31468 | 2584 | TypeScript | 14,750 stars this week | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Lum1104/Understand-Anything |  |
| 4 | `Imbad0202/academic-research-skills` | 21515 | 1832 | Python | 10,678 stars this week | Claude Code的学术研究技能：研究→撰写→评审→修订→最终确定 | https://github.com/Imbad0202/academic-research-skills |  |
| 5 | `rohitg00/ai-engineering-from-scratch` | 18769 | 3175 | Python | 10,035 stars this week | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 6 | `ruvnet/RuView` | 65946 | 8721 | Rust | 6,396 stars this week | π RuView将商用WiFi信号转化为实时空间智能、生命体征监测和存在检测--所有这些都无需一个像素的视频。 | https://github.com/ruvnet/RuView |  |
| 7 | `rohitg00/agentmemory` | 17866 | 1462 | TypeScript | 5,687 stars this week | # 1基于真实世界基准的AI编码代理持久内存 | https://github.com/rohitg00/agentmemory |  |
| 8 | `CloakHQ/CloakBrowser` | 21020 | 1659 | Python | 6,167 stars this week | Stealth Chromium可通过每次机器人检测测试。插入式剧作家更换源级指纹补丁，通过30/30测试 | https://github.com/CloakHQ/CloakBrowser |  |
| 9 | `supertone-inc/supertonic` | 10478 | 1075 | Swift | 2,329 stars this week | 闪电般的快速、设备上、多语言TTS —通过ONNX本地运行。 | https://github.com/supertone-inc/supertonic |  |
| 10 | `can1357/oh-my-pi` | 7312 | 589 | TypeScript | 2,584 stars this week | 终端的AI编码代理—哈希锚定编辑、优化工具线束、LSP、Python、浏览器、子代理等 | https://github.com/can1357/oh-my-pi |  |
| 11 | `dograh-hq/dograh` | 2952 | 655 | Python | 693 stars this week | 开源语音代理平台 | https://github.com/dograh-hq/dograh |  |
| 12 | `presenton/presenton` | 6898 | 1160 | TypeScript | 1,787 stars this week | 开源AI演示生成器和API （ Gamma、Beautiful AI、Decktopus Alternative ） | https://github.com/presenton/presenton |  |
| 13 | `HKUDS/CLI-Anything` | 40395 | 3819 | Python | 4,010 stars this week | "CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub: https://clianything.cc/ | https://github.com/HKUDS/CLI-Anything |  |
| 14 | `obra/superpowers` | 206464 | 18403 | Shell | 9,950 stars this week | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers |  |
| 15 | `wechat-article/wechat-article-exporter` | 10838 | 1889 | TypeScript | 809 stars this week | 一款在线的 微信公众号文章批量下载 工具，支持导出阅读量与评论数据，无需搭建任何环境，可通过 在线网站 使用，支持 docker 私有化部署和 Cloudflare 部署。 支持下载各种文件格式，其中 HTML 格式可100%还原文章排版与样式。 | https://github.com/wechat-article/wechat-article-exporter |  |
| 16 | `cursor/plugins` | 825 | 89 | TypeScript | 366 stars this week | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 17 | `phodal/routa` | 1449 | 204 | TypeScript | 470 stars this week | 工作空间第一的人工智能开发多代理协调平台，在Web和桌面上共享规格、看板编排和MCP/ACP/A2A支持。 | https://github.com/phodal/routa |  |
| 18 | `ChromeDevTools/chrome-devtools-mcp` | 41734 | 2651 | TypeScript | 1,818 stars this week | 适用于编码代理的Chrome开发者工具 | https://github.com/ChromeDevTools/chrome-devtools-mcp |  |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `mattpocock/skills` | 105331 | 9313 | Shell | 86,188 stars this month | 真正工程师的技能。直接来自我的.claude目录。 | https://github.com/mattpocock/skills |  |
| 2 | `colbymchenry/codegraph` | 25319 | 1403 | TypeScript | 23,688 stars this month | Claude Code、Codex、Cursor、OpenCode和Hermes Agent的预索引代码知识图—代币更少，工具调用更少， 100%本地化 | https://github.com/colbymchenry/codegraph |  |
| 3 | `anthropics/financial-services` | 27570 | 3867 | Python | 19,853 stars this month | — | https://github.com/anthropics/financial-services |  |
| 4 | `CloakHQ/CloakBrowser` | 21020 | 1659 | Python | 19,438 stars this month | Stealth Chromium可通过每次机器人检测测试。插入式剧作家更换源级指纹补丁，通过30/30测试 | https://github.com/CloakHQ/CloakBrowser |  |
| 5 | `rohitg00/agentmemory` | 17868 | 1462 | TypeScript | 15,782 stars this month | # 1基于真实世界基准的AI编码代理持久内存 | https://github.com/rohitg00/agentmemory |  |
| 6 | `Imbad0202/academic-research-skills` | 21516 | 1833 | Python | 17,780 stars this month | Claude Code的学术研究技能：研究→撰写→评审→修订→最终确定 | https://github.com/Imbad0202/academic-research-skills |  |
| 7 | `soxoj/maigret` | 30389 | 2168 | Python | 10,826 stars this month | 通过用户名从3000多个网站🕵️‍♂️收集个人档案 | https://github.com/soxoj/maigret |  |
| 8 | `TauricResearch/TradingAgents` | 79554 | 15511 | Python | 27,064 stars this month | TradingAgent ：多代理LLM金融交易框架 | https://github.com/TauricResearch/TradingAgents |  |
| 9 | `multica-ai/andrej-karpathy-skills` | 155138 | 15902 | — | 68,832 stars this month | 一个用于改进Claude Code行为的CLAUDE.md文件，源自Andrej Karpathy对LLM编码陷阱的观察。 | https://github.com/multica-ai/andrej-karpathy-skills |  |
| 10 | `AIDC-AI/Pixelle-Video` | 19783 | 2792 | Python | 13,152 stars this month | 🚀 AI 全自动短视频引擎 · AI Fully Automated Short Video Engine | https://github.com/AIDC-AI/Pixelle-Video |  |
| 11 | `ComposioHQ/awesome-codex-skills` | 11678 | 1114 | Python | 10,408 stars this month | 用于跨Codex CLI和API自动化工作流程的实用Codex技能精选列表。 | https://github.com/ComposioHQ/awesome-codex-skills |  |
| 12 | `decolua/9router` | 14271 | 2140 | JavaScript | 11,172 stars this month | 无限免费AI编码。通过40多家供应商将Claude Code、Codex、Cursor、Cline、Copilot、Antigravity连接到免费的Claude/GPT/Gemini。自动回退， RTK -40%代币，从未达到限制。 | https://github.com/decolua/9router |  |
| 13 | `Lum1104/Understand-Anything` | 31491 | 2586 | TypeScript | 20,742 stars this month | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Lum1104/Understand-Anything |  |
| 14 | `Alishahryar1/free-claude-code` | 29697 | 4466 | Python | 19,114 stars this month | 在终端中免费使用claude-code、VSCode扩展或像OpenClaw这样的不和谐（支持语音） | https://github.com/Alishahryar1/free-claude-code |  |
| 15 | `ruvnet/ruflo` | 55110 | 6269 | TypeScript | 22,151 stars this month | 🌊 Claude的领先代理编排平台。部署智能多智能体群，协调自主工作流程，构建对话式人工智能系统。具有企业级架构、自学群体智能、RAG集成和本地Claude Code/… | https://github.com/ruvnet/ruflo |  |
| 16 | `yikart/AiToEarn` | 16502 | 2657 | TypeScript | 7,524 stars this month | 让我们使用人工智能来赚取收入！ | https://github.com/yikart/AiToEarn |  |
| 17 | `bytedance/UI-TARS-desktop` | 35245 | 3544 | TypeScript | 5,825 stars this month | 开源多模态人工智能代理堆栈：连接尖端人工智能模型和代理基础设施 | https://github.com/bytedance/UI-TARS-desktop |  |
| 18 | `rohitg00/ai-engineering-from-scratch` | 18779 | 3176 | Python | 12,957 stars this month | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 19 | `addyosmani/agent-skills` | 45710 | 5065 | Shell | 22,920 stars this month | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 20 | `mattpocock/sandcastle` | 5079 | 529 | TypeScript | 4,110 stars this month | 使用sandcastle.run ()在TypeScript中编排沙盒编码代理 | https://github.com/mattpocock/sandcastle |  |


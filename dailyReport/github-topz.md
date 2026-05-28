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

**最近一次更新时间**（Asia/Shanghai）： 2026-05-28 08:38:44

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 505706 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 470587 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 445472 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 437457 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 389051 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 375088 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 355576 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 350571 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 347520 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 299882 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `harry0703/MoneyPrinterTurbo` | 61955 | 9054 | Python | 1,742 stars today | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. | https://github.com/harry0703/MoneyPrinterTurbo | 新增 |
| 2 | `Lum1104/Understand-Anything` | 39760 | 3168 | TypeScript | 4,465 stars today | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Lum1104/Understand-Anything |  |
| 3 | `hardikpandya/stop-slop` | 5686 | 434 | — | 664 stars today | 从散文中删除AI TELLS的技能文件 | https://github.com/hardikpandya/stop-slop |  |
| 4 | `affaan-m/ECC` | 196011 | 30158 | JavaScript | 2,062 stars today | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 5 | `anthropics/knowledge-work-plugins` | 17265 | 2015 | Python | 695 stars today | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins |  |
| 6 | `Leonxlnx/taste-skill` | 24219 | 1870 | Shell | 2,715 stars today | 品味技能-让您的人工智能有良好的品味。阻止人工智能产生无聊的通用斜坡 | https://github.com/Leonxlnx/taste-skill |  |
| 7 | `p-e-w/heretic` | 22006 | 2348 | Python | 211 stars today | 语言模型的全自动审查删除 | https://github.com/p-e-w/heretic | 新增 |
| 8 | `shiyu-coder/Kronos` | 26879 | 4655 | Python | 401 stars today | Kronos ：金融市场语言的基础模型 | https://github.com/shiyu-coder/Kronos | 新增 |
| 9 | `mukul975/Anthropic-Cybersecurity-Skills` | 10951 | 1251 | Python | 886 stars today | 人工智能代理的754种结构化网络安全技能·映射到5个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND和NIST AI RMF · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20多个平台· 26个安全数据…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills |  |
| 10 | `twentyhq/twenty` | 47326 | 6716 | TypeScript | 519 stars today | Salesforce的开放式替代方案，专为人工智能而设计。 | https://github.com/twentyhq/twenty |  |
| 11 | `Chachamaru127/claude-code-harness` | 1815 | 198 | Shell | 87 stars today | Claude Code Dedicated Development Harness -通过自主计划→工作→审核周期实现高质量发展 | https://github.com/Chachamaru127/claude-code-harness | 新增 |
| 12 | `DigitalPlatDev/FreeDomain` | 169130 | 3198 | HTML | 2,222 stars today | DigitalPlat FreeDomain ：人人免费域名 | https://github.com/DigitalPlatDev/FreeDomain |  |
| 13 | `obra/superpowers` | 209518 | 18671 | Shell | 1,511 stars today | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers | 新增 |
| 14 | `byoungd/English-level-up-tips` | 46626 | 4890 | — | 1,163 stars today | An advanced guide to learn English which might benefit you a lot 🎉 . 离谱的英语学习指南/英语学习教程/英语学习/学英语 | https://github.com/byoungd/English-level-up-tips | 新增 |
| 15 | `iii-hq/iii` | 16863 | 1106 | Rust | 376 stars today | 首次实时轻松编写、扩展和观察每项服务。 | https://github.com/iii-hq/iii | 新增 |
| 16 | `Axorax/awesome-free-apps` | 5873 | 293 | JavaScript | 728 stars today | 适用于PC和移动设备的最佳免费应用程序精选列表 | https://github.com/Axorax/awesome-free-apps |  |
| 17 | `moeru-ai/airi` | 40214 | 4046 | TypeScript | 72 stars today | 💖🧸 自我托管，你拥有的Grok Companion ，一个包含外府灵魂的容器，将它们带入我们的世界的网络生活，希望达到Neuro-sama的高度。能够实时语音聊天、Minecraft、Factorio播放。支持Web/macOS/Windows。 | https://github.com/moeru-ai/airi | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `colbymchenry/codegraph` | 29805 | 1706 | TypeScript | 21,424 stars this week | Claude Code、Codex、Gemini、Cursor、OpenCode、AntiGravity、Kiro和Hermes Agent的预索引代码知识图—代币更少，工具调用更少， 100%本地化 | https://github.com/colbymchenry/codegraph |  |
| 2 | `Lum1104/Understand-Anything` | 39760 | 3168 | TypeScript | 23,401 stars this week | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Lum1104/Understand-Anything |  |
| 3 | `rohitg00/ai-engineering-from-scratch` | 22498 | 3684 | Python | 12,787 stars this week | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 4 | `ruvnet/RuView` | 66724 | 8851 | Rust | 5,434 stars this week | π RuView将商用WiFi信号转化为实时空间智能、生命体征监测和存在检测--所有这些都无需一个像素的视频。 | https://github.com/ruvnet/RuView |  |
| 5 | `anthropics/knowledge-work-plugins` | 17266 | 2015 | Python | 4,718 stars this week | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins |  |
| 6 | `Imbad0202/academic-research-skills` | 22756 | 1917 | Python | 7,385 stars this week | Claude Code的学术研究技能：研究→撰写→评审→修订→最终确定 | https://github.com/Imbad0202/academic-research-skills |  |
| 7 | `rmyndharis/OpenWA` | 6707 | 1378 | TypeScript | 2,113 stars this week | 免费、开源、自托管的WhatsApp API网关 | https://github.com/rmyndharis/OpenWA | 新增 |
| 8 | `HKUDS/ViMax` | 7807 | 1211 | Python | 1,940 stars this week | "ViMax ： Agentic Video Generation （导演、编剧、制片人和视频生成器一体机）" | https://github.com/HKUDS/ViMax |  |
| 9 | `tinyhumansai/openhuman` | 28847 | 2715 | Rust | 5,723 stars this week | 您的个人人工智能超级智能。私密、简单且功能强大。 | https://github.com/tinyhumansai/openhuman |  |
| 10 | `can1357/oh-my-pi` | 7879 | 635 | TypeScript | 2,514 stars this week | 终端的AI编码代理—哈希锚定编辑、优化工具线束、LSP、Python、浏览器、子代理等 | https://github.com/can1357/oh-my-pi |  |
| 11 | `cursor/plugins` | 982 | 92 | TypeScript | 548 stars this week | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 12 | `hardikpandya/stop-slop` | 5686 | 434 | — | 1,751 stars this week | 从散文中删除AI TELLS的技能文件 | https://github.com/hardikpandya/stop-slop | 新增 |
| 13 | `Chachamaru127/claude-code-harness` | 1815 | 198 | Shell | 631 stars this week | Claude Code Dedicated Development Harness -通过自主计划→工作→审核周期实现高质量发展 | https://github.com/Chachamaru127/claude-code-harness |  |
| 14 | `rohitg00/agentmemory` | 18675 | 1537 | TypeScript | 3,781 stars this week | # 1基于真实世界基准的AI编码代理持久内存 | https://github.com/rohitg00/agentmemory |  |
| 15 | `dograh-hq/dograh` | 3420 | 726 | Python | 997 stars this week | 开源语音AI平台。Vapi和Retell的自托管替代品。在PREM上， BYOK跨语音到语音或LLM/STT/TTS ，具有可视化工作流程构建器、MCP本机和电话支持。 | https://github.com/dograh-hq/dograh |  |
| 16 | `mukul975/Anthropic-Cybersecurity-Skills` | 10951 | 1251 | Python | 4,170 stars this week | 人工智能代理的754种结构化网络安全技能·映射到5个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND和NIST AI RMF · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20多个平台· 26个安全数据…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills | 新增 |
| 17 | `harry0703/MoneyPrinterTurbo` | 61955 | 9054 | Python | 3,495 stars this week | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. | https://github.com/harry0703/MoneyPrinterTurbo | 新增 |
| 18 | `supertone-inc/supertonic` | 10803 | 1117 | Swift | 1,849 stars this week | 闪电般的快速、设备上、多语言TTS —通过ONNX本地运行。 | https://github.com/supertone-inc/supertonic |  |
| 19 | `aiming-lab/AutoResearchClaw` | 12850 | 1500 | Python | 451 stars this week | 从创意到论文的完全自主和自我发展的研究。聊天创意。获取论文。 🦞 | https://github.com/aiming-lab/AutoResearchClaw | 新增 |
| 20 | `humanlayer/12-factor-agents` | 22573 | 1707 | TypeScript | 1,127 stars this week | 我们可以使用哪些原则来构建基于LLM的软件，这些软件实际上足以交付给生产客户？ | https://github.com/humanlayer/12-factor-agents |  |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `colbymchenry/codegraph` | 29805 | 1706 | TypeScript | 28,837 stars this month | Claude Code、Codex、Gemini、Cursor、OpenCode、AntiGravity、Kiro和Hermes Agent的预索引代码知识图—代币更少，工具调用更少， 100%本地化 | https://github.com/colbymchenry/codegraph |  |
| 2 | `anthropics/financial-services` | 28213 | 3954 | Python | 20,415 stars this month | — | https://github.com/anthropics/financial-services |  |
| 3 | `CloakHQ/CloakBrowser` | 21775 | 1735 | Python | 20,333 stars this month | Stealth Chromium可通过每次机器人检测测试。插入式剧作家更换源级指纹补丁，通过30/30测试 | https://github.com/CloakHQ/CloakBrowser |  |
| 4 | `mattpocock/skills` | 108514 | 9557 | Shell | 81,117 stars this month | 真正工程师的技能。直接来自我的.claude目录。 | https://github.com/mattpocock/skills |  |
| 5 | `warpdotdev/warp` | 60225 | 4786 | Rust | 34,105 stars this month | WARP是一个代理开发环境，诞生于终端之外。 | https://github.com/warpdotdev/warp | 新增 |
| 6 | `rohitg00/agentmemory` | 18677 | 1537 | TypeScript | 16,556 stars this month | # 1基于真实世界基准的AI编码代理持久内存 | https://github.com/rohitg00/agentmemory |  |
| 7 | `Lum1104/Understand-Anything` | 39761 | 3168 | TypeScript | 29,679 stars this month | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Lum1104/Understand-Anything |  |
| 8 | `Imbad0202/academic-research-skills` | 22756 | 1917 | Python | 19,046 stars this month | Claude Code的学术研究技能：研究→撰写→评审→修订→最终确定 | https://github.com/Imbad0202/academic-research-skills |  |
| 9 | `1jehuang/jcode` | 6606 | 742 | Rust | 6,232 stars this month | 编码代理线束 | https://github.com/1jehuang/jcode | 新增 |
| 10 | `HKUDS/ViMax` | 7807 | 1211 | Python | 5,067 stars this month | "ViMax ： Agentic Video Generation （导演、编剧、制片人和视频生成器一体机）" | https://github.com/HKUDS/ViMax | 新增 |
| 11 | `soxoj/maigret` | 30663 | 2191 | Python | 11,026 stars this month | 通过用户名从3000多个网站🕵️‍♂️收集个人档案 | https://github.com/soxoj/maigret |  |
| 12 | `TauricResearch/TradingAgents` | 80185 | 15611 | Python | 27,184 stars this month | TradingAgent ：多代理LLM金融交易框架 | https://github.com/TauricResearch/TradingAgents |  |
| 13 | `decolua/9router` | 14722 | 2200 | JavaScript | 11,580 stars this month | 无限免费AI编码。通过40多家供应商将Claude Code、Codex、Cursor、Cline、Copilot、Antigravity连接到免费的Claude/GPT/Gemini。自动回退， RTK -40%代币，从未达到限制。 | https://github.com/decolua/9router |  |
| 14 | `rohitg00/ai-engineering-from-scratch` | 22498 | 3684 | Python | 16,501 stars this month | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 15 | `AIDC-AI/Pixelle-Video` | 20148 | 2833 | Python | 13,195 stars this month | 🚀 AI 全自动短视频引擎 · AI Fully Automated Short Video Engine | https://github.com/AIDC-AI/Pixelle-Video |  |
| 16 | `multica-ai/andrej-karpathy-skills` | 158961 | 16302 | — | 66,700 stars this month | 一个用于改进Claude Code行为的CLAUDE.md文件，源自Andrej Karpathy对LLM编码陷阱的观察。 | https://github.com/multica-ai/andrej-karpathy-skills |  |
| 17 | `ruvnet/ruflo` | 55804 | 6347 | TypeScript | 22,453 stars this month | 🌊 Claude的领先代理编排平台。部署智能多智能体群，协调自主工作流程，构建对话式人工智能系统。具有企业级架构、自学群体智能、RAG集成和本地Claude Code/… | https://github.com/ruvnet/ruflo |  |
| 18 | `yikart/AiToEarn` | 16774 | 2684 | TypeScript | 7,860 stars this month | 让我们使用人工智能来赚取收入！ | https://github.com/yikart/AiToEarn |  |
| 19 | `bytedance/UI-TARS-desktop` | 35512 | 3568 | TypeScript | 6,059 stars this month | 开源多模态人工智能代理堆栈：连接尖端人工智能模型和代理基础设施 | https://github.com/bytedance/UI-TARS-desktop |  |
| 20 | `mattpocock/sandcastle` | 5233 | 538 | TypeScript | 4,201 stars this month | 使用sandcastle.run ()在TypeScript中编排沙盒编码代理 | https://github.com/mattpocock/sandcastle |  |
| 21 | `LearningCircuit/local-deep-research` | 8049 | 698 | Python | 3,679 stars this month | SimpleQA约95% （例如3090上的Qwen3.6-27B ）。支持所有本地和云LLM （ llama.cpp、Ollama、Google等）。10多个搜索引擎- arXiv、PubMed、您的私人文档。本地和加密的一切。 | https://github.com/LearningCircuit/local-deep-research |  |


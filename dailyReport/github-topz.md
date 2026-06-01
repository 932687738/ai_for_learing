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

**最近一次更新时间**（Asia/Shanghai）： 2026-06-01 08:55:56

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 509410 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 471819 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 445721 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 438232 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 389310 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 375882 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 355816 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 351188 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 347914 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 300624 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `harry0703/MoneyPrinterTurbo` | 74193 | 10586 | Python | 1,937 stars today | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. | https://github.com/harry0703/MoneyPrinterTurbo |  |
| 2 | `microsoft/markitdown` | 134977 | 9230 | Python | 2,798 stars today | 用于将文件和Office文档转换为Markdown的Python工具。 | https://github.com/microsoft/markitdown |  |
| 3 | `D4Vinci/Scrapling` | 56629 | 5491 | Python | 606 stars today | 🕷️ 一个自适应Web抓取框架，可处理从单个请求到全面爬网的所有内容！ | https://github.com/D4Vinci/Scrapling | 新增 |
| 4 | `nesquena/hermes-webui` | 9973 | 1371 | Python | 357 stars today | Hermes WebUI ：通过网络或手机使用Hermes Agent的最佳方式！ | https://github.com/nesquena/hermes-webui | 新增 |
| 5 | `EveryInc/compound-engineering-plugin` | 18704 | 1408 | TypeScript | 251 stars today | Claude Code、Codex、Cursor等的官方复合工程插件 | https://github.com/EveryInc/compound-engineering-plugin |  |
| 6 | `github/docs` | 19732 | 67287 | TypeScript | 27 stars today | Docs.github.com的开源存储库 | https://github.com/github/docs | 新增 |
| 7 | `OpenBMB/VoxCPM` | 23531 | 2718 | Python | 635 stars today | VoxCPM2 ：用于多语言语音生成、创意语音设计和真实克隆的无标记TTS | https://github.com/OpenBMB/VoxCPM |  |
| 8 | `revfactory/harness` | 4597 | 650 | HTML | 323 stars today | 一种元技能，用于设计特定领域的座席团队，定义专业座席，并生成他们使用的技能。 | https://github.com/revfactory/harness |  |
| 9 | `FareedKhan-dev/train-llm-from-scratch` | 2959 | 443 | Jupyter Notebook | 626 stars today | 从下载数据到生成文本，这是培训LLM的简单方法。 | https://github.com/FareedKhan-dev/train-llm-from-scratch |  |
| 10 | `supermemoryai/supermemory` | 23339 | 2107 | TypeScript | 264 stars today | 内存引擎和应用程序，速度极快，可扩展。人工智能时代的内存API。 | https://github.com/supermemoryai/supermemory | 新增 |
| 11 | `Crosstalk-Solutions/project-nomad` | 27732 | 2712 | TypeScript | 374 stars today | Project N.O.M.A.D是一款独立的离线生存计算机，配备了关键工具、知识和人工智能，可随时随地让您随时了解情况并获得授权。 | https://github.com/Crosstalk-Solutions/project-nomad |  |
| 12 | `anthropics/claude-code` | 128911 | 20999 | Python | 489 stars today | Claude Code是一个代理编码工具，它位于您的终端中，了解您的代码库，并通过执行日常任务、解释复杂代码和处理git工作流程（所有这些都通过自然语言命令）来帮助您更快地进行编码。 | https://github.com/anthropics/claude-code |  |
| 13 | `nicobailon/pi-subagents` | 1845 | 256 | TypeScript | 69 stars today | 具有截断、工件和会话共享的异步子代理委派的Pi扩展 | https://github.com/nicobailon/pi-subagents | 新增 |
| 14 | `emmabostian/developer-portfolios` | 23370 | 4611 | Python | 73 stars today | 为您提供灵感的开发者作品集列表 | https://github.com/emmabostian/developer-portfolios | 新增 |
| 15 | `codecrafters-io/build-your-own-x` | 509410 | 48317 | Markdown | 1,158 stars today | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `harry0703/MoneyPrinterTurbo` | 74195 | 10586 | Python | 15,955 stars this week | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. | https://github.com/harry0703/MoneyPrinterTurbo |  |
| 2 | `Lum1104/Understand-Anything` | 47210 | 3832 | TypeScript | 22,750 stars this week | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Lum1104/Understand-Anything |  |
| 3 | `anthropics/knowledge-work-plugins` | 18435 | 2169 | Python | 4,944 stars this week | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins |  |
| 4 | `rohitg00/ai-engineering-from-scratch` | 25793 | 4184 | Python | 10,586 stars this week | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 5 | `hardikpandya/stop-slop` | 7740 | 550 | — | 3,770 stars this week | 从散文中删除AI TELLS的技能文件 | https://github.com/hardikpandya/stop-slop |  |
| 6 | `microsoft/markitdown` | 134978 | 9230 | Python | 9,353 stars this week | 用于将文件和Office文档转换为Markdown的Python工具。 | https://github.com/microsoft/markitdown |  |
| 7 | `Leonxlnx/taste-skill` | 29903 | 2218 | Shell | 10,813 stars this week | 品味技能-让您的人工智能有良好的品味。阻止人工智能产生无聊的通用斜坡 | https://github.com/Leonxlnx/taste-skill |  |
| 8 | `colbymchenry/codegraph` | 35348 | 2189 | TypeScript | 13,925 stars this week | Claude Code、Codex、Gemini、Cursor、OpenCode、AntiGravity、Kiro和Hermes Agent的预索引代码知识图—代币更少，工具调用更少， 100%本地化 | https://github.com/colbymchenry/codegraph |  |
| 9 | `mukul975/Anthropic-Cybersecurity-Skills` | 12942 | 1513 | Python | 4,896 stars this week | 人工智能代理的754种结构化网络安全技能·映射到5个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND和NIST AI RMF · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20多个平台· 26个安全数据…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills |  |
| 10 | `affaan-m/ECC` | 200611 | 30783 | JavaScript | 10,473 stars this week | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 11 | `cursor/plugins` | 1611 | 128 | TypeScript | 882 stars this week | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 12 | `revfactory/harness` | 4597 | 650 | HTML | 957 stars this week | 一种元技能，用于设计特定领域的座席团队，定义专业座席，并生成他们使用的技能。 | https://github.com/revfactory/harness |  |
| 13 | `p-e-w/heretic` | 22758 | 2433 | Python | 1,417 stars this week | 语言模型的全自动审查删除 | https://github.com/p-e-w/heretic |  |
| 14 | `microsoft/agent-governance-toolkit` | 3564 | 509 | Python | 1,657 stars this week | AI代理治理工具包—针对自主AI代理的策略实施、零信任身份、执行沙盒和可靠性工程。涵盖10/10 OWASP Agentic Top 10。 | https://github.com/microsoft/agent-governance-toolkit |  |
| 15 | `Chachamaru127/claude-code-harness` | 2381 | 237 | Shell | 997 stars this week | Claude Code Dedicated Development Harness -通过自主计划→工作→审核周期实现高质量发展 | https://github.com/Chachamaru127/claude-code-harness |  |
| 16 | `dograh-hq/dograh` | 3982 | 797 | Python | 1,329 stars this week | 开源语音AI平台。Vapi和Retell的自托管替代品。在PREM上， BYOK跨语音到语音或LLM/STT/TTS ，具有可视化工作流程构建器、MCP本机和电话支持。 | https://github.com/dograh-hq/dograh |  |
| 17 | `ogulcancelik/herdr` | 3413 | 223 | Rust | 1,058 stars this week | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 18 | `run-llama/liteparse` | 8325 | 493 | Rust | 3,006 stars this week | 快速、实用、开源的文档解析器 | https://github.com/run-llama/liteparse | 新增 |
| 19 | `iii-hq/iii` | 17372 | 1140 | Rust | 1,394 stars this week | 首次实时轻松编写、扩展和观察每项服务。 | https://github.com/iii-hq/iii | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `colbymchenry/codegraph` | 35349 | 2189 | TypeScript | 34,446 stars this month | Claude Code、Codex、Gemini、Cursor、OpenCode、AntiGravity、Kiro和Hermes Agent的预索引代码知识图—代币更少，工具调用更少， 100%本地化 | https://github.com/colbymchenry/codegraph |  |
| 2 | `anthropics/financial-services` | 29080 | 4073 | Python | 21,308 stars this month | — | https://github.com/anthropics/financial-services |  |
| 3 | `CloakHQ/CloakBrowser` | 22878 | 1820 | Python | 21,400 stars this month | Stealth Chromium可通过每次机器人检测测试。插入式剧作家更换源级指纹补丁，通过30/30测试 | https://github.com/CloakHQ/CloakBrowser |  |
| 4 | `rohitg00/agentmemory` | 20219 | 1672 | TypeScript | 18,071 stars this month | # 1基于真实世界基准的AI编码代理持久内存 | https://github.com/rohitg00/agentmemory |  |
| 5 | `Lum1104/Understand-Anything` | 47210 | 3832 | TypeScript | 37,390 stars this month | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Lum1104/Understand-Anything |  |
| 6 | `Imbad0202/academic-research-skills` | 25112 | 2070 | Python | 21,119 stars this month | Claude Code的学术研究技能：研究→撰写→评审→修订→最终确定 | https://github.com/Imbad0202/academic-research-skills |  |
| 7 | `HKUDS/ViMax` | 8449 | 1297 | Python | 5,721 stars this month | "ViMax ： Agentic Video Generation （导演、编剧、制片人和视频生成器一体机）" | https://github.com/HKUDS/ViMax | 新增 |
| 8 | `mattpocock/skills` | 113127 | 9925 | Shell | 65,737 stars this month | 真正工程师的技能。直接来自我的.claude目录。 | https://github.com/mattpocock/skills |  |
| 9 | `rohitg00/ai-engineering-from-scratch` | 25793 | 4184 | Python | 19,640 stars this month | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 10 | `decolua/9router` | 15415 | 2310 | JavaScript | 12,051 stars this month | 无限免费AI编码。通过40多家供应商将Claude Code、Codex、Cursor、Cline、Copilot、Antigravity连接到免费的Claude/GPT/Gemini。自动回退， RTK -40%代币，从未达到限制。 | https://github.com/decolua/9router |  |
| 11 | `harry0703/MoneyPrinterTurbo` | 74195 | 10586 | Python | 16,993 stars this month | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. | https://github.com/harry0703/MoneyPrinterTurbo | 新增 |
| 12 | `yikart/AiToEarn` | 17225 | 2739 | TypeScript | 8,241 stars this month | 让我们使用人工智能来赚取收入！ | https://github.com/yikart/AiToEarn |  |
| 13 | `bytedance/UI-TARS-desktop` | 35809 | 3604 | TypeScript | 6,370 stars this month | 开源多模态人工智能代理堆栈：连接尖端人工智能模型和代理基础设施 | https://github.com/bytedance/UI-TARS-desktop |  |
| 14 | `ruvnet/ruflo` | 56962 | 6487 | TypeScript | 23,191 stars this month | 🌊 Claude的领先代理编排平台。部署智能多智能体群，协调自主工作流程，构建对话式人工智能系统。具有企业级架构、自学群体智能、RAG集成和本地Claude Code/… | https://github.com/ruvnet/ruflo |  |
| 15 | `AIDC-AI/Pixelle-Video` | 20720 | 2903 | Python | 12,581 stars this month | 🚀 AI 全自动短视频引擎 · AI Fully Automated Short Video Engine | https://github.com/AIDC-AI/Pixelle-Video |  |
| 16 | `multica-ai/andrej-karpathy-skills` | 163428 | 16740 | — | 62,506 stars this month | 一个用于改进Claude Code行为的CLAUDE.md文件，源自Andrej Karpathy对LLM编码陷阱的观察。 | https://github.com/multica-ai/andrej-karpathy-skills |  |
| 17 | `ruvnet/RuView` | 69531 | 9281 | Rust | 18,955 stars this month | π RuView将商用WiFi信号转化为实时空间智能、生命体征监测和存在检测--所有这些都无需一个像素的视频。 | https://github.com/ruvnet/RuView | 新增 |


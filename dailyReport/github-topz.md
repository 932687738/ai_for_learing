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

**最近一次更新时间**（Asia/Shanghai）： 2026-06-03 08:45:26

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 511188 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 472379 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 445911 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 438888 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 389519 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 376293 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 356061 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 351516 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 348628 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 300949 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |

---
## Trending 页面快照（HTML 抓取）

**说明**：与上方「全局 Star Search」数据源不同；本段按 GitHub trending 页的 **daily / weekly / monthly** 各拉一页并解析。**若前端改版导致选择器失效，需更新解析逻辑。**

- **标记**列：三个 `since` 子表**各自独立**对照本次拉取前文件中该小节表格已出现的 `owner/repo`；新出现的行标 **新增**。下次拉取会先清空上一轮「新增」再重算（只保留相对**上一版文件**的新仓库）。

### 今日 trending（since=daily）

**页面**： `https://github.com/trending?since=daily`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `chopratejas/headroom` | 6392 | 451 | Python | 1,265 stars today | 在工具输出、日志、文件和RAG块到达LLM之前对其进行压缩。令牌减少60-95% ，答案相同。库、代理、MCP服务器。 | https://github.com/chopratejas/headroom | 新增 |
| 2 | `microsoft/markitdown` | 141120 | 9612 | Python | 3,618 stars today | 用于将文件和Office文档转换为Markdown的Python工具。 | https://github.com/microsoft/markitdown | 新增 |
| 3 | `affaan-m/ECC` | 203940 | 31287 | JavaScript | 1,533 stars today | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC | 新增 |
| 4 | `D4Vinci/Scrapling` | 59158 | 5717 | Python | 1,182 stars today | 🕷️ 一个自适应Web抓取框架，可处理从单个请求到全面爬网的所有内容！ | https://github.com/D4Vinci/Scrapling | 新增 |
| 5 | `nesquena/hermes-webui` | 12536 | 1537 | Python | 1,722 stars today | Hermes WebUI ：通过网络或手机使用Hermes Agent的最佳方式！ | https://github.com/nesquena/hermes-webui | 新增 |
| 6 | `reconurge/flowsint` | 4503 | 582 | TypeScript | 124 stars today | 用于可视化、灵活且可扩展的基于图形的调查的现代平台。适用于网络安全分析师和调查人员。 | https://github.com/reconurge/flowsint | 新增 |
| 7 | `OpenBMB/VoxCPM` | 25109 | 2880 | Python | 783 stars today | VoxCPM2 ：用于多语言语音生成、创意语音设计和真实克隆的无标记TTS | https://github.com/OpenBMB/VoxCPM | 新增 |
| 8 | `stefan-jansen/machine-learning-for-trading` | 18459 | 5223 | Jupyter Notebook | 574 stars today | 算法交易的机器学习代码，第2版。 | https://github.com/stefan-jansen/machine-learning-for-trading | 新增 |
| 9 | `jamwithai/production-agentic-rag-course` | 6373 | 1488 | Python | 30 stars today | — | https://github.com/jamwithai/production-agentic-rag-course | 新增 |
| 10 | `supermemoryai/supermemory` | 24622 | 2177 | TypeScript | 680 stars today | 内存引擎和应用程序，速度极快，可扩展。人工智能时代的内存API。 | https://github.com/supermemoryai/supermemory | 新增 |
| 11 | `Open-LLM-VTuber/Open-LLM-VTuber` | 8354 | 1073 | Python | 66 stars today | 通过免提语音交互、语音中断和跨平台本地运行的Live2D与任何LLM交谈 | https://github.com/Open-LLM-VTuber/Open-LLM-VTuber | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `harry0703/MoneyPrinterTurbo` | 77994 | 11074 | Python | 18,982 stars this week | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. | https://github.com/harry0703/MoneyPrinterTurbo | 新增 |
| 2 | `microsoft/markitdown` | 141121 | 9612 | Python | 15,502 stars this week | 用于将文件和Office文档转换为Markdown的Python工具。 | https://github.com/microsoft/markitdown | 新增 |
| 3 | `chopratejas/headroom` | 6392 | 451 | Python | 3,002 stars this week | 在工具输出、日志、文件和RAG块到达LLM之前对其进行压缩。令牌减少60-95% ，答案相同。库、代理、MCP服务器。 | https://github.com/chopratejas/headroom | 新增 |
| 4 | `Lum1104/Understand-Anything` | 50098 | 4079 | TypeScript | 15,774 stars this week | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Lum1104/Understand-Anything | 新增 |
| 5 | `hardikpandya/stop-slop` | 8281 | 578 | — | 3,470 stars this week | 从散文中删除AI TELLS的技能文件 | https://github.com/hardikpandya/stop-slop | 新增 |
| 6 | `Leonxlnx/taste-skill` | 31765 | 2341 | Shell | 10,931 stars this week | 品味技能-让您的人工智能有良好的品味。阻止人工智能产生无聊的通用斜坡 | https://github.com/Leonxlnx/taste-skill | 新增 |
| 7 | `revfactory/harness` | 5523 | 732 | HTML | 1,870 stars this week | 一种元技能，用于设计特定领域的座席团队，定义专业座席，并生成他们使用的技能。 | https://github.com/revfactory/harness | 新增 |
| 8 | `rohitg00/ai-engineering-from-scratch` | 27374 | 4444 | Python | 7,183 stars this week | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch | 新增 |
| 9 | `colbymchenry/codegraph` | 37949 | 2346 | TypeScript | 10,793 stars this week | Claude Code、Codex、Gemini、Cursor、OpenCode、AntiGravity、Kiro和Hermes Agent的预索引代码知识图—代币更少，工具调用更少， 100%本地化 | https://github.com/colbymchenry/codegraph |  |
| 10 | `mukul975/Anthropic-Cybersecurity-Skills` | 13616 | 1590 | Python | 3,755 stars this week | 人工智能代理的754种结构化网络安全技能·映射到5个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND和NIST AI RMF · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20多个平台· 26个安全数据…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills | 新增 |
| 11 | `affaan-m/ECC` | 203940 | 31287 | JavaScript | 9,910 stars this week | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC | 新增 |
| 12 | `cursor/plugins` | 1730 | 136 | TypeScript | 842 stars this week | 光标插件规范和官方插件 | https://github.com/cursor/plugins | 新增 |
| 13 | `EveryInc/compound-engineering-plugin` | 19386 | 1442 | TypeScript | 2,143 stars this week | Claude Code、Codex、Cursor等的官方复合工程插件 | https://github.com/EveryInc/compound-engineering-plugin | 新增 |
| 14 | `anthropics/knowledge-work-plugins` | 18865 | 2212 | Python | 2,458 stars this week | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins | 新增 |
| 15 | `microsoft/agent-governance-toolkit` | 3814 | 533 | Python | 1,391 stars this week | AI代理治理工具包—针对自主AI代理的策略实施、零信任身份、执行沙盒和可靠性工程。涵盖10/10 OWASP Agentic Top 10。 | https://github.com/microsoft/agent-governance-toolkit | 新增 |
| 16 | `p-e-w/heretic` | 23291 | 2490 | Python | 1,634 stars this week | 语言模型的全自动审查删除 | https://github.com/p-e-w/heretic | 新增 |
| 17 | `Chachamaru127/claude-code-harness` | 2534 | 242 | Shell | 879 stars this week | Claude Code Dedicated Development Harness -通过自主计划→工作→审核周期实现高质量发展 | https://github.com/Chachamaru127/claude-code-harness | 新增 |
| 18 | `ogulcancelik/herdr` | 3876 | 249 | Rust | 1,327 stars this week | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr | 新增 |
| 19 | `supermemoryai/supermemory` | 24622 | 2177 | TypeScript | 1,733 stars this week | 内存引擎和应用程序，速度极快，可扩展。人工智能时代的内存API。 | https://github.com/supermemoryai/supermemory | 新增 |
| 20 | `iii-hq/iii` | 17536 | 1154 | Rust | 1,321 stars this week | 首次实时轻松编写、扩展和观察每项服务。 | https://github.com/iii-hq/iii | 新增 |
| 21 | `modelscope/FunASR` | 16912 | 1732 | Python | 544 stars this week | 工业级语音识别工具包： 170倍实时、50多种语言、说话人日志、情绪检测、流媒体和OpenAI兼容的API。 | https://github.com/modelscope/FunASR | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `colbymchenry/codegraph` | 37949 | 2346 | TypeScript | 37,126 stars this month | Claude Code、Codex、Gemini、Cursor、OpenCode、AntiGravity、Kiro和Hermes Agent的预索引代码知识图—代币更少，工具调用更少， 100%本地化 | https://github.com/colbymchenry/codegraph | 新增 |
| 2 | `Hmbown/CodeWhale` | 36707 | 3152 | Rust | 35,376 stars this month | 终端中的DeepSeek + MiMo编码代理 | https://github.com/Hmbown/CodeWhale | 新增 |
| 3 | `anthropics/financial-services` | 29524 | 4134 | Python | 21,733 stars this month | — | https://github.com/anthropics/financial-services |  |
| 4 | `CloakHQ/CloakBrowser` | 23407 | 1852 | Python | 21,929 stars this month | Stealth Chromium可通过每次机器人检测测试。插入式剧作家更换源级指纹补丁，通过30/30测试 | https://github.com/CloakHQ/CloakBrowser |  |
| 5 | `rohitg00/agentmemory` | 20766 | 1711 | TypeScript | 18,650 stars this month | # 1基于真实世界基准的AI编码代理持久内存 | https://github.com/rohitg00/agentmemory |  |
| 6 | `Lum1104/Understand-Anything` | 50099 | 4079 | TypeScript | 39,602 stars this month | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Lum1104/Understand-Anything | 新增 |
| 7 | `Imbad0202/academic-research-skills` | 26226 | 2158 | Python | 22,232 stars this month | Claude Code的学术研究技能：研究→撰写→评审→修订→最终确定 | https://github.com/Imbad0202/academic-research-skills |  |
| 8 | `fathah/hermes-desktop` | 9417 | 1140 | TypeScript | 8,524 stars this month | Hermès Agent桌面配套 | https://github.com/fathah/hermes-desktop | 新增 |
| 9 | `harry0703/MoneyPrinterTurbo` | 77994 | 11074 | Python | 21,551 stars this month | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. | https://github.com/harry0703/MoneyPrinterTurbo | 新增 |
| 10 | `rohitg00/ai-engineering-from-scratch` | 27374 | 4444 | Python | 21,199 stars this month | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch | 新增 |
| 11 | `mattpocock/skills` | 115253 | 10097 | Shell | 61,503 stars this month | 真正工程师的技能。直接来自我的.claude目录。 | https://github.com/mattpocock/skills |  |
| 12 | `decolua/9router` | 15956 | 2391 | JavaScript | 12,459 stars this month | 无限免费AI编码。通过40多家供应商将Claude Code、Codex、Cursor、Cline、Copilot、Antigravity连接到免费的Claude/GPT/Gemini。自动回退， RTK -40%代币，从未达到限制。 | https://github.com/decolua/9router |  |
| 13 | `yikart/AiToEarn` | 17555 | 2780 | TypeScript | 8,481 stars this month | 让我们使用人工智能来赚取收入！ | https://github.com/yikart/AiToEarn | 新增 |
| 14 | `bytedance/UI-TARS-desktop` | 35943 | 3618 | TypeScript | 6,498 stars this month | 开源多模态人工智能代理堆栈：连接尖端人工智能模型和代理基础设施 | https://github.com/bytedance/UI-TARS-desktop | 新增 |
| 15 | `ruvnet/RuView` | 70227 | 9391 | Rust | 19,374 stars this month | π RuView将商用WiFi信号转化为实时空间智能、生命体征监测和存在检测--所有这些都无需一个像素的视频。 | https://github.com/ruvnet/RuView | 新增 |
| 16 | `datawhalechina/easy-vibe` | 15672 | 1491 | JavaScript | 8,257 stars this month | 💻 vibe coding 2026 ·您的第一个现代编程课程，供初学者一步一步掌握。 | https://github.com/datawhalechina/easy-vibe | 新增 |
| 17 | `can1357/oh-my-pi` | 9986 | 821 | TypeScript | 6,132 stars this month | 终端的AI编码代理—哈希锚定编辑、优化工具线束、LSP、Python、浏览器、子代理等 | https://github.com/can1357/oh-my-pi | 新增 |
| 18 | `multica-ai/andrej-karpathy-skills` | 165870 | 16975 | — | 60,985 stars this month | 一个用于改进Claude Code行为的CLAUDE.md文件，源自Andrej Karpathy对LLM编码陷阱的观察。 | https://github.com/multica-ai/andrej-karpathy-skills |  |
| 19 | `AIDC-AI/Pixelle-Video` | 21070 | 2931 | Python | 12,222 stars this month | 🚀 AI 全自动短视频引擎 · AI Fully Automated Short Video Engine | https://github.com/AIDC-AI/Pixelle-Video |  |


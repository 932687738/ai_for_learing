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

**最近一次更新时间**（Asia/Shanghai）： 2026-06-06 08:53:50

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 511923 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 472956 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 446269 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 439634 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 389744 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 377111 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 356270 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 351898 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 350387 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 301486 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
| 11 | `awesome-selfhosted/awesome-selfhosted` | 297418 | 可自行部署的各类自由软件网络服务与 Web 应用清单。 | https://github.com/awesome-selfhosted/awesome-selfhosted |  |
| 12 | `996icu/996.ICU` | 276265 | 倡议关注「996」工作制、计数星标与交流的开发社区仓库（含网络迷因用语）。 | https://github.com/996icu/996.ICU | 新增 |
| 13 | `practical-tutorials/project-based-learning` | 267810 | 基于项目的教程精选列表 | https://github.com/practical-tutorials/project-based-learning |  |
| 14 | `facebook/react` | 245279 | 用于构建 Web 与原生用户界面的 React 视图库（含多端生态）。 | https://github.com/facebook/react |  |

---
## Trending 页面快照（HTML 抓取）

**说明**：与上方「全局 Star Search」数据源不同；本段按 GitHub trending 页的 **daily / weekly / monthly** 各拉一页并解析。**若前端改版导致选择器失效，需更新解析逻辑。**

- **标记**列：三个 `since` 子表**各自独立**对照本次拉取前文件中该小节表格已出现的 `owner/repo`；新出现的行标 **新增**。下次拉取会先清空上一轮「新增」再重算（只保留相对**上一版文件**的新仓库）。

### 今日 trending（since=daily）

**页面**： `https://github.com/trending?since=daily`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `NousResearch/hermes-agent` | 183126 | 31409 | Python | 1,845 stars today | 与您一起成长的客服代表 | https://github.com/NousResearch/hermes-agent |  |
| 2 | `chopratejas/headroom` | 14506 | 923 | Python | 2,473 stars today | 在工具输出、日志、文件和RAG块到达LLM之前对其进行压缩。令牌减少60-95% ，答案相同。库、代理、MCP服务器。 | https://github.com/chopratejas/headroom |  |
| 3 | `CopilotKit/CopilotKit` | 32681 | 4193 | TypeScript | 366 stars today | Agent和生成式UI的前端堆栈。React + Angular。AG-UI协议的制造商 | https://github.com/CopilotKit/CopilotKit | 新增 |
| 4 | `lfnovo/open-notebook` | 26003 | 2993 | TypeScript | 1,152 stars today | 笔记本LM的开源实现，具有更大的灵活性和功能 | https://github.com/lfnovo/open-notebook |  |
| 5 | `affaan-m/ECC` | 208360 | 31966 | JavaScript | 1,361 stars today | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 6 | `Panniantong/Agent-Reach` | 21561 | 1861 | Python | 148 stars today | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach | 新增 |
| 7 | `NVIDIA/cosmos` | 9414 | 602 | Jupyter Notebook | 479 stars today | NVIDIA Cosmos是一个开放的世界模型、数据集和工具平台，使开发人员能够为机器人、自动驾驶汽车、智能基础设施等构建物理AI。 | https://github.com/NVIDIA/cosmos |  |
| 8 | `666ghj/MiroFish` | 64699 | 10088 | Python | 320 stars today | A Simple and Universal Swarm Intelligence Engine, Predicting Anything. 简洁通用的群体智能引擎，预测万物 | https://github.com/666ghj/MiroFish | 新增 |
| 9 | `mvanhorn/last30days-skill` | 28210 | 2392 | Python | 731 stars today | 人工智能代理技能，研究Reddit、X、YouTube、HN、Polymarket和网络上的任何主题，然后合成基础摘要 | https://github.com/mvanhorn/last30days-skill |  |
| 10 | `PaddlePaddle/PaddleOCR` | 80538 | 10632 | Python | 747 stars today | 将任何PDF或图像文档转换为AI的结构化数据。功能强大、重量轻的OCR工具包，可弥合图像/PDF和LLM之间的差距。支持100多种语言。 | https://github.com/PaddlePaddle/PaddleOCR |  |
| 11 | `openai/plugins` | 1535 | 242 | JavaScript | 49 stars today | OpenAI插件 | https://github.com/openai/plugins | 新增 |
| 12 | `MemPalace/mempalace` | 53887 | 7079 | Python | 227 stars today | 最佳基准的开源AI内存系统。而且是免费的。 | https://github.com/MemPalace/mempalace | 新增 |
| 13 | `withastro/flue` | 4516 | 241 | TypeScript | 126 stars today | 沙盒代理框架。 | https://github.com/withastro/flue | 新增 |
| 14 | `openclaw/openclaw-windows-node` | 1603 | 182 | C# | 326 stars today | 适用于OpenClaw的Windows伴侣套件-系统托盘应用、共享库、节点和PowerToys命令调色板扩展 | https://github.com/openclaw/openclaw-windows-node |  |
| 15 | `aquasecurity/trivy` | 35854 | 443 | Go | 207 stars today | 查找漏洞、错误配置、秘密、容器中的SBOM、Kubernetes、代码仓库、云等 | https://github.com/aquasecurity/trivy |  |
| 16 | `jwasham/coding-interview-university` | 350387 | 83290 | — | 745 stars today | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 17 | `github/copilot-sdk` | 9241 | 1223 | Java | 309 stars today | 用于将GitHub Copilot Agent集成到应用和服务中的多平台SDK | https://github.com/github/copilot-sdk |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `chopratejas/headroom` | 14506 | 923 | Python | 11,993 stars this week | 在工具输出、日志、文件和RAG块到达LLM之前对其进行压缩。令牌减少60-95% ，答案相同。库、代理、MCP服务器。 | https://github.com/chopratejas/headroom |  |
| 2 | `microsoft/markitdown` | 145394 | 9959 | Python | 16,376 stars this week | 用于将文件和Office文档转换为Markdown的Python工具。 | https://github.com/microsoft/markitdown |  |
| 3 | `harry0703/MoneyPrinterTurbo` | 79954 | 11372 | Python | 11,388 stars this week | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. | https://github.com/harry0703/MoneyPrinterTurbo |  |
| 4 | `revfactory/harness` | 6129 | 827 | HTML | 2,030 stars this week | 一种元技能，用于设计特定领域的座席团队，定义专业座席，并生成他们使用的技能。 | https://github.com/revfactory/harness |  |
| 5 | `run-llama/liteparse` | 9218 | 554 | Rust | 2,380 stars this week | 快速、实用、开源的文档解析器 | https://github.com/run-llama/liteparse | 新增 |
| 6 | `EveryInc/compound-engineering-plugin` | 19942 | 1481 | TypeScript | 1,933 stars this week | Claude Code、Codex、Cursor等的官方复合工程插件 | https://github.com/EveryInc/compound-engineering-plugin |  |
| 7 | `supermemoryai/supermemory` | 25692 | 2246 | TypeScript | 2,944 stars this week | 内存引擎和应用程序，速度极快，可扩展。人工智能时代的内存API。 | https://github.com/supermemoryai/supermemory |  |
| 8 | `affaan-m/ECC` | 208360 | 31966 | JavaScript | 10,326 stars this week | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 9 | `Open-LLM-VTuber/Open-LLM-VTuber` | 10007 | 1193 | Python | 2,073 stars this week | 通过免提语音交互、语音中断和跨平台本地运行的Live2D与任何LLM交谈 | https://github.com/Open-LLM-VTuber/Open-LLM-VTuber | 新增 |
| 10 | `hardikpandya/stop-slop` | 8849 | 612 | — | 2,082 stars this week | 从散文中删除AI TELLS的技能文件 | https://github.com/hardikpandya/stop-slop |  |
| 11 | `can1357/oh-my-pi` | 10735 | 901 | TypeScript | 2,317 stars this week | 终端的AI编码代理—哈希锚定编辑、优化工具线束、LSP、Python、浏览器、子代理等 | https://github.com/can1357/oh-my-pi |  |
| 12 | `OpenBMB/VoxCPM` | 26494 | 3001 | Python | 4,398 stars this week | VoxCPM2 ：用于多语言语音生成、创意语音设计和真实克隆的无标记TTS | https://github.com/OpenBMB/VoxCPM |  |
| 13 | `ogulcancelik/herdr` | 4611 | 276 | Rust | 1,574 stars this week | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 14 | `Lum1104/Understand-Anything` | 52895 | 4329 | TypeScript | 8,807 stars this week | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Lum1104/Understand-Anything |  |
| 15 | `cursor/plugins` | 1863 | 149 | TypeScript | 673 stars this week | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 16 | `anthropics/claude-code` | 130432 | 21172 | Python | 2,893 stars this week | Claude Code是一个代理编码工具，它位于您的终端中，了解您的代码库，并通过执行日常任务、解释复杂代码和处理git工作流程（所有这些都通过自然语言命令）来帮助您更快地进行编码。 | https://github.com/anthropics/claude-code |  |
| 17 | `Leonxlnx/taste-skill` | 33945 | 2502 | Shell | 6,044 stars this week | 品味技能-让您的人工智能有良好的品味。阻止人工智能产生无聊的通用斜坡 | https://github.com/Leonxlnx/taste-skill |  |
| 18 | `colbymchenry/codegraph` | 42280 | 2597 | TypeScript | 9,318 stars this week | Claude Code、Codex、Gemini、Cursor、OpenCode、AntiGravity、Kiro和Hermes Agent的预索引代码知识图—代币更少，工具调用更少， 100%本地化 | https://github.com/colbymchenry/codegraph |  |
| 19 | `mukul975/Anthropic-Cybersecurity-Skills` | 14412 | 1698 | Python | 2,492 stars this week | 人工智能代理的754种结构化网络安全技能·映射到5个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND和NIST AI RMF · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20多个平台· 26个安全数据…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills |  |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `colbymchenry/codegraph` | 42281 | 2597 | TypeScript | 41,379 stars this month | Claude Code、Codex、Gemini、Cursor、OpenCode、AntiGravity、Kiro和Hermes Agent的预索引代码知识图—代币更少，工具调用更少， 100%本地化 | https://github.com/colbymchenry/codegraph |  |
| 2 | `CloakHQ/CloakBrowser` | 24189 | 1921 | Python | 22,637 stars this month | Stealth Chromium可通过每次机器人检测测试。插入式剧作家更换源级指纹补丁，通过30/30测试 | https://github.com/CloakHQ/CloakBrowser |  |
| 3 | `rohitg00/agentmemory` | 21405 | 1761 | TypeScript | 19,261 stars this month | # 1基于真实世界基准的AI编码代理持久内存 | https://github.com/rohitg00/agentmemory |  |
| 4 | `Lum1104/Understand-Anything` | 52895 | 4329 | TypeScript | 40,696 stars this month | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Lum1104/Understand-Anything |  |
| 5 | `chopratejas/headroom` | 14506 | 923 | Python | 12,410 stars this month | 在工具输出、日志、文件和RAG块到达LLM之前对其进行压缩。令牌减少60-95% ，答案相同。库、代理、MCP服务器。 | https://github.com/chopratejas/headroom |  |
| 6 | `fathah/hermes-desktop` | 10572 | 1243 | TypeScript | 9,467 stars this month | Hermès Agent桌面配套 | https://github.com/fathah/hermes-desktop |  |
| 7 | `anthropics/financial-services` | 30140 | 4248 | Python | 22,354 stars this month | — | https://github.com/anthropics/financial-services |  |
| 8 | `harry0703/MoneyPrinterTurbo` | 79954 | 11372 | Python | 23,580 stars this month | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. | https://github.com/harry0703/MoneyPrinterTurbo |  |
| 9 | `Imbad0202/academic-research-skills` | 27685 | 2282 | Python | 23,258 stars this month | Claude Code的学术研究技能：研究→撰写→评审→修订→最终确定 | https://github.com/Imbad0202/academic-research-skills |  |
| 10 | `rohitg00/ai-engineering-from-scratch` | 28830 | 4717 | Python | 22,445 stars this month | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 11 | `HKUDS/ViMax` | 8856 | 1351 | Python | 6,125 stars this month | "ViMax ： Agentic Video Generation （导演、编剧、制片人和视频生成器一体机）" | https://github.com/HKUDS/ViMax |  |
| 12 | `mattpocock/skills` | 118685 | 10395 | Shell | 58,947 stars this month | 真正工程师的技能。直接来自我的.claude目录。 | https://github.com/mattpocock/skills |  |
| 13 | `ruvnet/RuView` | 71068 | 9487 | Rust | 19,902 stars this month | π RuView将商用WiFi信号转化为实时空间智能、生命体征监测和存在检测--所有这些都无需一个像素的视频。 | https://github.com/ruvnet/RuView |  |
| 14 | `yikart/AiToEarn` | 18180 | 2844 | TypeScript | 9,082 stars this month | 让我们使用人工智能来赚取收入！ | https://github.com/yikart/AiToEarn |  |
| 15 | `decolua/9router` | 16479 | 2482 | JavaScript | 12,723 stars this month | 无限免费AI编码。通过40多家供应商将Claude Code、Codex、Cursor、Cline、Copilot、Antigravity连接到免费的Claude/GPT/Gemini。自动回退， RTK -40%代币，从未达到限制。 | https://github.com/decolua/9router |  |
| 16 | `bytedance/UI-TARS-desktop` | 36116 | 3635 | TypeScript | 6,653 stars this month | 开源多模态人工智能代理堆栈：连接尖端人工智能模型和代理基础设施 | https://github.com/bytedance/UI-TARS-desktop |  |
| 17 | `Hmbown/CodeWhale` | 37205 | 3198 | Rust | 31,602 stars this month | 终端中的DeepSeek + MiMo编码代理 | https://github.com/Hmbown/CodeWhale |  |
| 18 | `can1357/oh-my-pi` | 10735 | 901 | TypeScript | 6,817 stars this month | 终端的AI编码代理—哈希锚定编辑、优化工具线束、LSP、Python、浏览器、子代理等 | https://github.com/can1357/oh-my-pi |  |
| 19 | `datawhalechina/easy-vibe` | 16220 | 1526 | JavaScript | 8,669 stars this month | 💻 vibe coding 2026 ·您的第一个现代编程课程，供初学者一步一步掌握。 | https://github.com/datawhalechina/easy-vibe |  |


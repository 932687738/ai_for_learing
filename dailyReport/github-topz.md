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

**最近一次更新时间**（Asia/Shanghai）： 2026-06-04 09:05:55

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 511570 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 472674 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 445988 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 439142 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 389613 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 376590 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 356181 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 351635 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 349016 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 301105 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `chopratejas/headroom` | 9755 | 645 | Python | 3,530 stars today | 在工具输出、日志、文件和RAG块到达LLM之前对其进行压缩。令牌减少60-95% ，答案相同。库、代理、MCP服务器。 | https://github.com/chopratejas/headroom | 新增 |
| 2 | `affaan-m/ECC` | 205751 | 31591 | JavaScript | 2,141 stars today | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC | 新增 |
| 3 | `aquasecurity/trivy` | 35404 | 416 | Go | 24 stars today | 查找漏洞、错误配置、秘密、容器中的SBOM、Kubernetes、代码仓库、云等 | https://github.com/aquasecurity/trivy | 新增 |
| 4 | `NousResearch/hermes-agent` | 179136 | 30689 | Python | 1,735 stars today | 与您一起成长的客服代表 | https://github.com/NousResearch/hermes-agent | 新增 |
| 5 | `microsoft/markitdown` | 142876 | 9764 | Python | 1,984 stars today | 用于将文件和Office文档转换为Markdown的Python工具。 | https://github.com/microsoft/markitdown |  |
| 6 | `nesquena/hermes-webui` | 13103 | 1593 | Python | 719 stars today | Hermes WebUI ：通过网络或手机使用Hermes Agent的最佳方式！ | https://github.com/nesquena/hermes-webui |  |
| 7 | `D4Vinci/Scrapling` | 60249 | 5808 | Python | 1,067 stars today | 🕷️ 一个自适应Web抓取框架，可处理从单个请求到全面爬网的所有内容！ | https://github.com/D4Vinci/Scrapling |  |
| 8 | `opendataloader-project/opendataloader-pdf` | 23277 | 2183 | Java | 570 stars today | 适用于人工智能就绪数据的PDF解析器。自动化PDF辅助功能。开源。 | https://github.com/opendataloader-project/opendataloader-pdf | 新增 |
| 9 | `odoo/odoo` | 51935 | 32642 | Python | 29 stars today | Odoo。开源应用助您拓展业务。 | https://github.com/odoo/odoo | 新增 |
| 10 | `Open-LLM-VTuber/Open-LLM-VTuber` | 8963 | 1106 | Python | 693 stars today | 通过免提语音交互、语音中断和跨平台本地运行的Live2D与任何LLM交谈 | https://github.com/Open-LLM-VTuber/Open-LLM-VTuber | 新增 |
| 11 | `jwasham/coding-interview-university` | 349016 | 83155 | — | 330 stars today | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university | 新增 |
| 12 | `lyogavin/airllm` | 18904 | 2071 | Jupyter Notebook | 208 stars today | 使用单个4GB GPU的AirLLM 70B推理 | https://github.com/lyogavin/airllm | 新增 |
| 13 | `supermemoryai/supermemory` | 25177 | 2213 | TypeScript | 600 stars today | 内存引擎和应用程序，速度极快，可扩展。人工智能时代的内存API。 | https://github.com/supermemoryai/supermemory |  |
| 14 | `HKUDS/Vibe-Trading` | 9923 | 2005 | Python | 197 stars today | “Vibe-Trading ：您的个人交易代理” | https://github.com/HKUDS/Vibe-Trading | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `harry0703/MoneyPrinterTurbo` | 78843 | 11211 | Python | 18,553 stars this week | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. | https://github.com/harry0703/MoneyPrinterTurbo |  |
| 2 | `chopratejas/headroom` | 9758 | 645 | Python | 6,245 stars this week | 在工具输出、日志、文件和RAG块到达LLM之前对其进行压缩。令牌减少60-95% ，答案相同。库、代理、MCP服务器。 | https://github.com/chopratejas/headroom | 新增 |
| 3 | `microsoft/markitdown` | 142876 | 9764 | Python | 17,108 stars this week | 用于将文件和Office文档转换为Markdown的Python工具。 | https://github.com/microsoft/markitdown |  |
| 4 | `Lum1104/Understand-Anything` | 51133 | 4175 | TypeScript | 12,726 stars this week | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Lum1104/Understand-Anything |  |
| 5 | `revfactory/harness` | 5696 | 761 | HTML | 2,005 stars this week | 一种元技能，用于设计特定领域的座席团队，定义专业座席，并生成他们使用的技能。 | https://github.com/revfactory/harness |  |
| 6 | `hardikpandya/stop-slop` | 8537 | 596 | — | 3,103 stars this week | 从散文中删除AI TELLS的技能文件 | https://github.com/hardikpandya/stop-slop |  |
| 7 | `EveryInc/compound-engineering-plugin` | 19603 | 1455 | TypeScript | 2,116 stars this week | Claude Code、Codex、Cursor等的官方复合工程插件 | https://github.com/EveryInc/compound-engineering-plugin | 新增 |
| 8 | `Leonxlnx/taste-skill` | 32516 | 2390 | Shell | 9,084 stars this week | 品味技能-让您的人工智能有良好的品味。阻止人工智能产生无聊的通用斜坡 | https://github.com/Leonxlnx/taste-skill |  |
| 9 | `supermemoryai/supermemory` | 25177 | 2213 | TypeScript | 2,260 stars this week | 内存引擎和应用程序，速度极快，可扩展。人工智能时代的内存API。 | https://github.com/supermemoryai/supermemory | 新增 |
| 10 | `colbymchenry/codegraph` | 39337 | 2442 | TypeScript | 9,796 stars this week | Claude Code、Codex、Gemini、Cursor、OpenCode、AntiGravity、Kiro和Hermes Agent的预索引代码知识图—代币更少，工具调用更少， 100%本地化 | https://github.com/colbymchenry/codegraph |  |
| 11 | `affaan-m/ECC` | 205751 | 31591 | JavaScript | 10,008 stars this week | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 12 | `OpenMOSS/MOSS-TTS` | 2962 | 265 | Python | 974 stars this week | MOSS ‑ TTS家族是来自MOSI.AI和OpenMOSS团队的开源语音和声音生成模型家族。它专为高保真、高表现力和复杂的现实世界场景而设计，涵盖稳定的长篇语音、多扬声器对话、语音/字符设计…… | https://github.com/OpenMOSS/MOSS-TTS | 新增 |
| 13 | `mukul975/Anthropic-Cybersecurity-Skills` | 13900 | 1629 | Python | 3,247 stars this week | 人工智能代理的754种结构化网络安全技能·映射到5个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND和NIST AI RMF · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20多个平台· 26个安全数据…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills |  |
| 14 | `rohitg00/ai-engineering-from-scratch` | 27903 | 4544 | Python | 6,161 stars this week | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 15 | `cursor/plugins` | 1784 | 144 | TypeScript | 820 stars this week | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 16 | `can1357/oh-my-pi` | 10310 | 856 | TypeScript | 2,521 stars this week | 终端的AI编码代理—哈希锚定编辑、优化工具线束、LSP、Python、浏览器、子代理等 | https://github.com/can1357/oh-my-pi | 新增 |
| 17 | `microsoft/agent-governance-toolkit` | 3925 | 539 | Python | 1,000 stars this week | AI代理治理工具包—针对自主AI代理的策略实施、零信任身份、执行沙盒和可靠性工程。涵盖10/10 OWASP Agentic Top 10。 | https://github.com/microsoft/agent-governance-toolkit |  |
| 18 | `ogulcancelik/herdr` | 4108 | 259 | Rust | 1,410 stars this week | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 19 | `p-e-w/heretic` | 23423 | 2500 | Python | 1,595 stars this week | 语言模型的全自动审查删除 | https://github.com/p-e-w/heretic |  |
| 20 | `OpenBMB/VoxCPM` | 25597 | 2913 | Python | 5,640 stars this week | VoxCPM2 ：用于多语言语音生成、创意语音设计和真实克隆的无标记TTS | https://github.com/OpenBMB/VoxCPM | 新增 |
| 21 | `anthropics/claude-code` | 129865 | 21110 | Python | 3,009 stars this week | Claude Code是一个代理编码工具，它位于您的终端中，了解您的代码库，并通过执行日常任务、解释复杂代码和处理git工作流程（所有这些都通过自然语言命令）来帮助您更快地进行编码。 | https://github.com/anthropics/claude-code | 新增 |
| 22 | `iii-hq/iii` | 17612 | 1159 | Rust | 1,054 stars this week | 首次实时轻松编写、扩展和观察每项服务。 | https://github.com/iii-hq/iii |  |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `colbymchenry/codegraph` | 39337 | 2442 | TypeScript | 38,467 stars this month | Claude Code、Codex、Gemini、Cursor、OpenCode、AntiGravity、Kiro和Hermes Agent的预索引代码知识图—代币更少，工具调用更少， 100%本地化 | https://github.com/colbymchenry/codegraph |  |
| 2 | `anthropics/financial-services` | 29787 | 4183 | Python | 21,999 stars this month | — | https://github.com/anthropics/financial-services |  |
| 3 | `CloakHQ/CloakBrowser` | 23655 | 1876 | Python | 22,190 stars this month | Stealth Chromium可通过每次机器人检测测试。插入式剧作家更换源级指纹补丁，通过30/30测试 | https://github.com/CloakHQ/CloakBrowser |  |
| 4 | `Hmbown/CodeWhale` | 36898 | 3174 | Rust | 35,225 stars this month | 终端中的DeepSeek + MiMo编码代理 | https://github.com/Hmbown/CodeWhale | 新增 |
| 5 | `rohitg00/agentmemory` | 20991 | 1732 | TypeScript | 18,882 stars this month | # 1基于真实世界基准的AI编码代理持久内存 | https://github.com/rohitg00/agentmemory |  |
| 6 | `Lum1104/Understand-Anything` | 51134 | 4175 | TypeScript | 40,416 stars this month | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Lum1104/Understand-Anything |  |
| 7 | `HKUDS/ViMax` | 8634 | 1325 | Python | 5,930 stars this month | "ViMax ： Agentic Video Generation （导演、编剧、制片人和视频生成器一体机）" | https://github.com/HKUDS/ViMax |  |
| 8 | `Imbad0202/academic-research-skills` | 26727 | 2201 | Python | 22,608 stars this month | Claude Code的学术研究技能：研究→撰写→评审→修订→最终确定 | https://github.com/Imbad0202/academic-research-skills |  |
| 9 | `fathah/hermes-desktop` | 9948 | 1184 | TypeScript | 8,951 stars this month | Hermès Agent桌面配套 | https://github.com/fathah/hermes-desktop | 新增 |
| 10 | `harry0703/MoneyPrinterTurbo` | 78843 | 11211 | Python | 22,441 stars this month | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. | https://github.com/harry0703/MoneyPrinterTurbo |  |
| 11 | `rohitg00/ai-engineering-from-scratch` | 27903 | 4544 | Python | 21,631 stars this month | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 12 | `mattpocock/skills` | 116458 | 10201 | Shell | 60,443 stars this month | 真正工程师的技能。直接来自我的.claude目录。 | https://github.com/mattpocock/skills |  |
| 13 | `yikart/AiToEarn` | 17849 | 2812 | TypeScript | 8,794 stars this month | 让我们使用人工智能来赚取收入！ | https://github.com/yikart/AiToEarn |  |
| 14 | `decolua/9router` | 16132 | 2414 | JavaScript | 12,585 stars this month | 无限免费AI编码。通过40多家供应商将Claude Code、Codex、Cursor、Cline、Copilot、Antigravity连接到免费的Claude/GPT/Gemini。自动回退， RTK -40%代币，从未达到限制。 | https://github.com/decolua/9router |  |
| 15 | `bytedance/UI-TARS-desktop` | 36006 | 3623 | TypeScript | 6,551 stars this month | 开源多模态人工智能代理堆栈：连接尖端人工智能模型和代理基础设施 | https://github.com/bytedance/UI-TARS-desktop |  |
| 16 | `ruvnet/RuView` | 70536 | 9437 | Rust | 19,584 stars this month | π RuView将商用WiFi信号转化为实时空间智能、生命体征监测和存在检测--所有这些都无需一个像素的视频。 | https://github.com/ruvnet/RuView |  |
| 17 | `chopratejas/headroom` | 9759 | 645 | Python | 7,349 stars this month | 在工具输出、日志、文件和RAG块到达LLM之前对其进行压缩。令牌减少60-95% ，答案相同。库、代理、MCP服务器。 | https://github.com/chopratejas/headroom | 新增 |
| 18 | `can1357/oh-my-pi` | 10310 | 856 | TypeScript | 6,443 stars this month | 终端的AI编码代理—哈希锚定编辑、优化工具线束、LSP、Python、浏览器、子代理等 | https://github.com/can1357/oh-my-pi | 新增 |
| 19 | `datawhalechina/easy-vibe` | 15856 | 1502 | JavaScript | 8,411 stars this month | 💻 vibe coding 2026 ·您的第一个现代编程课程，供初学者一步一步掌握。 | https://github.com/datawhalechina/easy-vibe | 新增 |


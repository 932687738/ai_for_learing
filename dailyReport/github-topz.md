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

**最近一次更新时间**（Asia/Shanghai）： 2026-06-22 09:44:59

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 518129 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 477717 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 450084 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 443360 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 390611 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 379828 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 357931 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 354230 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 353430 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 304173 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
| 11 | `awesome-selfhosted/awesome-selfhosted` | 297987 | 可自行部署的各类自由软件网络服务与 Web 应用清单。 | https://github.com/awesome-selfhosted/awesome-selfhosted |  |
| 12 | `996icu/996.ICU` | 276267 | 倡议关注「996」工作制、计数星标与交流的开发社区仓库（含网络迷因用语）。 | https://github.com/996icu/996.ICU |  |
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
| 1 | `palmier-io/palmier-pro` | 5246 | 395 | Swift | 1,834 stars today | 专为人工智能打造的macOS视频编辑器 | https://github.com/palmier-io/palmier-pro | 新增 |
| 2 | `calesthio/OpenMontage` | 8834 | 1308 | Python | 987 stars today | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 3 | `chopratejas/headroom` | 44513 | 3107 | Python | 2,624 stars today | 在工具输出、日志、文件和RAG块到达LLM之前对其进行压缩。令牌减少60-95% ，答案相同。库、代理、MCP服务器。 | https://github.com/chopratejas/headroom | 新增 |
| 4 | `tursodatabase/turso` | 20827 | 1065 | Rust | 548 stars today | Turso是一个进程内SQL数据库，与SQLite兼容。 | https://github.com/tursodatabase/turso | 新增 |
| 5 | `penpot/penpot` | 52269 | 3345 | Clojure | 1,135 stars today | Penpot ：用于设计和代码协作的开源设计工具 | https://github.com/penpot/penpot |  |
| 6 | `ZhuLinsen/daily_stock_analysis` | 44529 | 41453 | Python | 568 stars today | LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。 LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs. | https://github.com/ZhuLinsen/daily_stock_analysis | 新增 |
| 7 | `koala73/worldmonitor` | 58115 | 9209 | TypeScript | 163 stars today | 实时全球智能仪表板。在统一的态势感知界面中进行人工智能驱动的新闻聚合、地缘政治监控和基础设施跟踪 | https://github.com/koala73/worldmonitor | 新增 |
| 8 | `bytedance/deer-flow` | 72606 | 9832 | Python | 442 stars today | 研究、编码和创建的开源远程SuperAgent线束。借助沙箱、内存、工具、技能、子代理和消息网关，它可以处理可能需要几分钟到几小时的不同级别的任务。 | https://github.com/bytedance/deer-flow | 新增 |
| 9 | `DeusData/codebase-memory-mcp` | 10340 | 783 | C | 1,032 stars today | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 10 | `mukul975/Anthropic-Cybersecurity-Skills` | 17724 | 2131 | Python | 361 stars today | 人工智能代理的754种结构化网络安全技能·映射到5个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND和NIST AI RMF · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20多个平台· 26个安全数据…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills | 新增 |
| 11 | `tw93/Pake` | 56258 | 11103 | Rust | 1,848 stars today | 只需一个命令，即可将任何网页🤱🏻转换为桌面应用。 | https://github.com/tw93/Pake | 新增 |
| 12 | `mikumifa/biliTickerBuy` | 3716 | 466 | Python | 67 stars today | b站会员购购票辅助工具 | https://github.com/mikumifa/biliTickerBuy | 新增 |
| 13 | `smicallef/spiderfoot` | 18776 | 3107 | Python | 294 stars today | SpiderFoot自动化OSINT以获取威胁情报并映射您的攻击面。 | https://github.com/smicallef/spiderfoot | 新增 |
| 14 | `topoteretes/cognee` | 18658 | 1969 | Python | 347 stars today | Cognee是面向智能体的开源AI内存平台。使用自托管知识图表引擎，为您的人工智能代理提供跨会话的持久长期记忆。 | https://github.com/topoteretes/cognee | 新增 |
| 15 | `byoungd/English-level-up-tips` | 54021 | 5557 | — | 125 stars today | An advanced guide to learn English which might benefit you a lot 🎉 . 离谱的英语学习指南/英语学习教程/英语学习/学英语 | https://github.com/byoungd/English-level-up-tips | 新增 |
| 16 | `asgeirtj/system_prompts_leaks` | 44425 | 7338 | JavaScript | 282 stars today | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT 5.5 Thinking ， GPT 5.5 Instant ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks | 新增 |
| 17 | `mattpocock/skills` | 139831 | 12135 | Shell | 1,443 stars today | 真正工程师的技能。直接来自我的.claude目录。 | https://github.com/mattpocock/skills |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `DeusData/codebase-memory-mcp` | 10340 | 783 | C | 6,372 stars this week | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 2 | `chopratejas/headroom` | 44513 | 3107 | Python | 16,102 stars this week | 在工具输出、日志、文件和RAG块到达LLM之前对其进行压缩。令牌减少60-95% ，答案相同。库、代理、MCP服务器。 | https://github.com/chopratejas/headroom |  |
| 3 | `Panniantong/Agent-Reach` | 36888 | 2942 | Python | 8,233 stars this week | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 4 | `iptv-org/iptv` | 127146 | 6980 | TypeScript | 7,266 stars this week | 收集来自世界各地的公开IPTV频道 | https://github.com/iptv-org/iptv |  |
| 5 | `n0-computer/iroh` | 10452 | 473 | Rust | 1,712 stars this week | IP地址中断，改为拨号键。Rust中的模块化网络堆栈。 | https://github.com/n0-computer/iroh | 新增 |
| 6 | `google-research/timesfm` | 24894 | 2365 | Python | 4,114 stars this week | TimesFM （时间序列基础模型）是由Google Research开发的用于时间序列预测的预训练时间序列基础模型。 | https://github.com/google-research/timesfm | 新增 |
| 7 | `NVIDIA/SkillSpector` | 9045 | 708 | Python | 4,055 stars this week | 人工智能代理技能的安全扫描仪。检测漏洞、恶意模式和安全风险。 | https://github.com/NVIDIA/SkillSpector |  |
| 8 | `asgeirtj/system_prompts_leaks` | 44425 | 7338 | JavaScript | 1,984 stars this week | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT 5.5 Thinking ， GPT 5.5 Instant ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 9 | `calesthio/OpenMontage` | 8836 | 1309 | Python | 2,867 stars this week | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage | 新增 |
| 10 | `withastro/flue` | 6305 | 354 | TypeScript | 1,272 stars this week | 沙盒代理框架。 | https://github.com/withastro/flue | 新增 |
| 11 | `addyosmani/agent-skills` | 64782 | 6995 | Shell | 5,610 stars this week | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 12 | `Kong/insomnia` | 39516 | 2337 | TypeScript | 1,006 stars this week | GraphQL、REST、WebSockets、SSE和gRPC的开源、跨平台API客户端。使用云、本地和Git存储。 | https://github.com/Kong/insomnia | 新增 |
| 13 | `tursodatabase/turso` | 20827 | 1065 | Rust | 1,390 stars this week | Turso是一个进程内SQL数据库，与SQLite兼容。 | https://github.com/tursodatabase/turso | 新增 |
| 14 | `makeplane/plane` | 52360 | 4650 | TypeScript | 1,514 stars this week | 🔥🔥🔥 开源JIRA、Linear、Monday和ClickUp替代方案。Plane是一个现代化的项目管理平台，用于管理任务、冲刺、文档和分类。 | https://github.com/makeplane/plane | 新增 |
| 15 | `LMCache/LMCache` | 9545 | 1364 | Python | 506 stars this week | LMCache ：使用最快的KV缓存层为您的LLM增压 | https://github.com/LMCache/LMCache |  |
| 16 | `meshery/meshery` | 11225 | 3477 | TypeScript | 921 stars this week | Meshery ，云原生管理器 | https://github.com/meshery/meshery |  |
| 17 | `chatwoot/chatwoot` | 33124 | 7814 | Ruby | 2,036 stars this week | 开源实时聊天、电子邮件支持、全渠道服务台。Intercom、Zendesk、Salesforce Service Cloud等的替代方案。 🔥💬 | https://github.com/chatwoot/chatwoot |  |
| 18 | `swc-project/swc` | 34109 | 1426 | Rust | 403 stars this week | 基于Rust的网络平台 | https://github.com/swc-project/swc | 新增 |
| 19 | `freeCodeCamp/freeCodeCamp` | 450084 | 45192 | TypeScript | 3,294 stars this week | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `chopratejas/headroom` | 44515 | 3107 | Python | 41,093 stars this month | 在工具输出、日志、文件和RAG块到达LLM之前对其进行压缩。令牌减少60-95% ，答案相同。库、代理、MCP服务器。 | https://github.com/chopratejas/headroom |  |
| 2 | `harry0703/MoneyPrinterTurbo` | 90826 | 13080 | Python | 33,719 stars this month | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. | https://github.com/harry0703/MoneyPrinterTurbo |  |
| 3 | `Egonex-AI/Understand-Anything` | 65412 | 5430 | TypeScript | 49,339 stars this month | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Egonex-AI/Understand-Anything |  |
| 4 | `esengine/DeepSeek-Reasonix` | 23585 | 1432 | Go | 18,527 stars this month | 为您的终端提供DeepSeek原生AI编码代理。围绕前缀缓存稳定性而设计—保持运行。 | https://github.com/esengine/DeepSeek-Reasonix | 新增 |
| 5 | `apple/container` | 39294 | 1139 | Swift | 12,797 stars this month | 用于在Mac上使用轻量级虚拟机创建和运行Linux容器的工具。它是用Swift编写的，并针对Apple芯片进行了优化。 | https://github.com/apple/container |  |
| 6 | `colbymchenry/codegraph` | 52643 | 3208 | TypeScript | 40,915 stars this month | 预索引的代码知识图，在代码更改时自动同步，适用于Claude Code、Codex、Gemini、Cursor、OpenCode、AntiGravity、Kiro和Hermes Agent —代币更少，工具调用更少， 100%本地 | https://github.com/colbymchenry/codegraph |  |
| 7 | `hardikpandya/stop-slop` | 11723 | 821 | — | 8,001 stars this month | 从散文中删除AI TELLS的技能文件 | https://github.com/hardikpandya/stop-slop |  |
| 8 | `microsoft/markitdown` | 157189 | 10965 | Python | 33,203 stars this month | 用于将文件和Office文档转换为Markdown的Python工具。 | https://github.com/microsoft/markitdown |  |
| 9 | `Leonxlnx/taste-skill` | 48444 | 3376 | JavaScript | 29,925 stars this month | 品味技能-让您的人工智能有良好的品味。阻止人工智能产生无聊的通用斜坡 | https://github.com/Leonxlnx/taste-skill |  |
| 10 | `mvanhorn/last30days-skill` | 45395 | 3764 | Python | 19,261 stars this month | 人工智能代理技能，研究Reddit、X、YouTube、HN、Polymarket和网络上的任何主题，然后合成基础摘要 | https://github.com/mvanhorn/last30days-skill |  |
| 11 | `iptv-org/iptv` | 127146 | 6980 | TypeScript | 10,900 stars this month | 收集来自世界各地的公开IPTV频道 | https://github.com/iptv-org/iptv |  |
| 12 | `anthropics/knowledge-work-plugins` | 21645 | 2528 | Python | 9,296 stars this month | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins |  |
| 13 | `rohitg00/ai-engineering-from-scratch` | 35353 | 5766 | Python | 25,113 stars this month | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 14 | `tashfeenahmed/freellmapi` | 11360 | 1799 | TypeScript | 8,103 stars this month | OpenAI兼容代理，将16个LLM提供商的免费层（约17亿个代币/月）堆叠在一个/v1端点后面—加上任何自定义OpenAI兼容端点。智能路由、自动故障转移、加密密钥。仅限个人实验。 | https://github.com/tashfeenahmed/freellmapi | 新增 |
| 15 | `DeusData/codebase-memory-mcp` | 10341 | 783 | C | 7,381 stars this month | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp | 新增 |
| 16 | `can1357/oh-my-pi` | 13884 | 1227 | TypeScript | 8,209 stars this month | 终端的AI编码代理—哈希锚定编辑、优化工具线束、LSP、Python、浏览器、子代理等 | https://github.com/can1357/oh-my-pi |  |
| 17 | `Panniantong/Agent-Reach` | 36888 | 2942 | Python | 16,585 stars this month | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach | 新增 |
| 18 | `mukul975/Anthropic-Cybersecurity-Skills` | 17725 | 2131 | Python | 10,828 stars this month | 人工智能代理的754种结构化网络安全技能·映射到5个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND和NIST AI RMF · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20多个平台· 26个安全数据…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills |  |
| 19 | `phuryn/pm-skills` | 20319 | 2071 | — | 8,866 stars this month | PM Skills Marketplace ： 100多种代理技能、命令和插件—从发现到战略、执行、发布和增长。 | https://github.com/phuryn/pm-skills | 新增 |
| 20 | `lfnovo/open-notebook` | 32359 | 3661 | TypeScript | 8,725 stars this month | 笔记本LM的开源实现，具有更大的灵活性和功能 | https://github.com/lfnovo/open-notebook | 新增 |
| 21 | `ogulcancelik/herdr` | 6664 | 410 | Rust | 4,711 stars this month | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 22 | `openai/plugins` | 3312 | 395 | JavaScript | 2,115 stars this month | OpenAI插件 | https://github.com/openai/plugins | 新增 |


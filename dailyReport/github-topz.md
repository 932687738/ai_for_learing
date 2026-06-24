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

**最近一次更新时间**（Asia/Shanghai）： 2026-06-24 09:16:59

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 518897 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 478288 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 450360 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 443769 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 390689 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 380150 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 358097 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 354545 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 353735 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 304505 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `calesthio/OpenMontage` | 15708 | 1867 | Python | 3,592 stars today | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 2 | `ZhuLinsen/daily_stock_analysis` | 47061 | 42386 | Python | 1,119 stars today | LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。 LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs. | https://github.com/ZhuLinsen/daily_stock_analysis |  |
| 3 | `mukul975/Anthropic-Cybersecurity-Skills` | 19713 | 2298 | Python | 1,041 stars today | 人工智能代理的817种结构化网络安全技能·映射到6个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF和MITRE F3 （打击欺诈） · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20 + p…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills |  |
| 4 | `garrytan/gstack` | 114084 | 16889 | TypeScript | 1,011 stars today | 使用Garry Tan确切的Claude Code设置： 23个自以为是的工具，分别担任首席执行官、设计师、工程经理、发布经理、文档工程师和QA | https://github.com/garrytan/gstack |  |
| 5 | `bytedance/deer-flow` | 73924 | 9973 | Python | 739 stars today | 研究、编码和创建的开源远程SuperAgent线束。借助沙箱、内存、工具、技能、子代理和消息网关，它可以处理可能需要几分钟到几小时的不同级别的任务。 | https://github.com/bytedance/deer-flow |  |
| 6 | `koala73/worldmonitor` | 59106 | 9283 | TypeScript | 294 stars today | 实时全球智能仪表板。在统一的态势感知界面中进行人工智能驱动的新闻聚合、地缘政治监控和基础设施跟踪 | https://github.com/koala73/worldmonitor | 新增 |
| 7 | `palmier-io/palmier-pro` | 8426 | 553 | Swift | 1,630 stars today | 专为人工智能打造的macOS视频编辑器 | https://github.com/palmier-io/palmier-pro |  |
| 8 | `anthropics/claude-plugins-official` | 30844 | 3361 | Python | 77 stars today | 由Anthropic管理的高质量Claude Code插件的官方目录。 | https://github.com/anthropics/claude-plugins-official | 新增 |
| 9 | `shanraisshan/claude-code-best-practice` | 59463 | 5985 | HTML | 344 stars today | 从氛围编码到代理工程-实践使克劳德完美 | https://github.com/shanraisshan/claude-code-best-practice | 新增 |
| 10 | `revfactory/harness` | 7444 | 1046 | HTML | 128 stars today | 一种元技能，用于设计特定领域的座席团队，定义专业座席，并生成他们使用的技能。 | https://github.com/revfactory/harness | 新增 |
| 11 | `jamiepine/voicebox` | 33159 | 3999 | TypeScript | 1,045 stars today | 开源AI语音工作室。克隆、命令、创建。 | https://github.com/jamiepine/voicebox |  |
| 12 | `JCodesMore/ai-website-cloner-template` | 18564 | 2807 | TypeScript | 826 stars today | 使用AI编码代理，只需一个命令即可克隆任何网站 | https://github.com/JCodesMore/ai-website-cloner-template |  |
| 13 | `byoungd/English-level-up-tips` | 54497 | 5584 | — | 125 stars today | An advanced guide to learn English which might benefit you a lot 🎉 . 人生进阶指南 离谱的人生 离谱的英语学习指南/英语学习教程/英语学习/学英语 | https://github.com/byoungd/English-level-up-tips | 新增 |
| 14 | `DeusData/codebase-memory-mcp` | 12957 | 939 | C | 1,300 stars today | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 15 | `NousResearch/hermes-agent` | 200956 | 35840 | Python | 936 stars today | 与您一起成长的客服代表 | https://github.com/NousResearch/hermes-agent | 新增 |
| 16 | `affaan-m/ECC` | 220549 | 33783 | JavaScript | 593 stars today | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `DeusData/codebase-memory-mcp` | 12958 | 939 | C | 8,536 stars this week | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 2 | `calesthio/OpenMontage` | 15710 | 1867 | Python | 9,410 stars this week | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 3 | `google-research/timesfm` | 25313 | 2408 | Python | 4,376 stars this week | TimesFM （时间序列基础模型）是由Google Research开发的用于时间序列预测的预训练时间序列基础模型。 | https://github.com/google-research/timesfm |  |
| 4 | `Panniantong/Agent-Reach` | 38642 | 3062 | Python | 6,915 stars this week | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 5 | `n0-computer/iroh` | 10629 | 484 | Rust | 1,531 stars this week | IP地址中断，改为拨号键。Rust中的模块化网络堆栈。 | https://github.com/n0-computer/iroh |  |
| 6 | `asgeirtj/system_prompts_leaks` | 45413 | 7464 | JavaScript | 2,681 stars this week | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT 5.5 Thinking ， GPT 5.5 Instant ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 7 | `koala73/worldmonitor` | 59106 | 9283 | TypeScript | 2,309 stars this week | 实时全球智能仪表板。在统一的态势感知界面中进行人工智能驱动的新闻聚合、地缘政治监控和基础设施跟踪 | https://github.com/koala73/worldmonitor |  |
| 8 | `iptv-org/iptv` | 128005 | 7044 | TypeScript | 4,378 stars this week | 收集来自世界各地的公开IPTV频道 | https://github.com/iptv-org/iptv |  |
| 9 | `penpot/penpot` | 53296 | 3415 | Clojure | 3,423 stars this week | Penpot ：用于设计和代码协作的开源设计工具 | https://github.com/penpot/penpot |  |
| 10 | `withastro/flue` | 6536 | 366 | TypeScript | 1,489 stars this week | 沙盒代理框架。 | https://github.com/withastro/flue |  |
| 11 | `OpenCut-app/OpenCut` | 59247 | 6444 | TypeScript | 3,283 stars this week | 开源CapCut替代方案 | https://github.com/OpenCut-app/OpenCut |  |
| 12 | `NVIDIA/SkillSpector` | 9857 | 775 | Python | 2,849 stars this week | 人工智能代理技能的安全扫描仪。检测漏洞、恶意模式和安全风险。 | https://github.com/NVIDIA/SkillSpector |  |
| 13 | `jamiepine/voicebox` | 33159 | 3999 | TypeScript | 2,883 stars this week | 开源AI语音工作室。克隆、命令、创建。 | https://github.com/jamiepine/voicebox | 新增 |
| 14 | `mattpocock/skills` | 143337 | 12395 | Shell | 11,784 stars this week | 真正工程师的技能。直接来自我的.claude目录。 | https://github.com/mattpocock/skills | 新增 |
| 15 | `Kong/insomnia` | 39611 | 2345 | TypeScript | 1,121 stars this week | GraphQL、REST、WebSockets、SSE和gRPC的开源、跨平台API客户端。使用云、本地和Git存储。 | https://github.com/Kong/insomnia |  |
| 16 | `makeplane/plane` | 52731 | 4698 | TypeScript | 1,804 stars this week | 🔥🔥🔥 开源JIRA、Linear、Monday和ClickUp替代方案。Plane是一个现代化的项目管理平台，用于管理任务、冲刺、文档和分类。 | https://github.com/makeplane/plane |  |
| 17 | `Stirling-Tools/Stirling-PDF` | 83703 | 7287 | Java | 2,491 stars this week | GitHub上排名第一的PDF应用程序，可让您在任何地方的任何设备上编辑PDF | https://github.com/Stirling-Tools/Stirling-PDF | 新增 |
| 18 | `addyosmani/agent-skills` | 65968 | 7117 | Shell | 5,073 stars this week | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 19 | `chatwoot/chatwoot` | 33375 | 7859 | Ruby | 1,399 stars this week | 开源实时聊天、电子邮件支持、全渠道服务台。Intercom、Zendesk、Salesforce Service Cloud等的替代方案。 🔥💬 | https://github.com/chatwoot/chatwoot | 新增 |
| 20 | `stablyai/orca` | 6321 | 464 | TypeScript | 1,216 stars this week | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca | 新增 |
| 21 | `continuedev/continue` | 34355 | 4814 | TypeScript | 620 stars this week | 开源编码代理 | https://github.com/continuedev/continue | 新增 |


### 本月 trending（since=monthly）

> Trending HTML 抓取或解析失败： `IncompleteRead(643712 bytes read)`。**since**=`monthly`。


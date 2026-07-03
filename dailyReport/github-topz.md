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

**最近一次更新时间**（Asia/Shanghai）： 2026-07-03 09:17:07

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 521877 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 480913 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 450925 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 446106 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 391161 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 381491 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 359014 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 355860 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 354883 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 306011 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
| 11 | `awesome-selfhosted/awesome-selfhosted` | 301670 | 可自行部署的各类自由软件网络服务与 Web 应用清单。 | https://github.com/awesome-selfhosted/awesome-selfhosted |  |
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
| 1 | `usestrix/strix` | 32247 | 3376 | Python | 2,137 stars today | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 2 | `JuliusBrussee/caveman` | 80964 | 4531 | JavaScript | 926 stars today | 🪨 为什么在很少令牌欺骗时使用许多令牌— Claude Code技能通过像穴居人一样说话来削减65 ％的令牌 | https://github.com/JuliusBrussee/caveman | 新增 |
| 3 | `msitarzewski/agency-agents` | 125505 | 20365 | Shell | 3,032 stars today | 一个完整的人工智能机构，触手可及--从前端向导到Reddit社区忍者，从奇思妙想的注入者到现实检查者。每位客服代表都是具有个性、流程和经过验证的交付成果的专家。 | https://github.com/msitarzewski/agency-agents |  |
| 4 | `hasaneyldrm/exercises-dataset` | 9266 | 1037 | HTML | 938 stars today | 包含433项健身练习的综合数据集。每个条目包括名称、类别、目标肌肉群、设备、说明、缩略图和动画视频。 | https://github.com/hasaneyldrm/exercises-dataset |  |
| 5 | `santifer/career-ops` | 57842 | 11391 | JavaScript | 372 stars today | 基于Claude Code构建的人工智能求职系统。14种技能模式、Go仪表板、PDF生成、批量处理。 | https://github.com/santifer/career-ops | 新增 |
| 6 | `obra/superpowers` | 244443 | 21684 | Shell | 897 stars today | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers | 新增 |
| 7 | `ChromeDevTools/chrome-devtools-mcp` | 45089 | 2934 | TypeScript | 104 stars today | 适用于编码代理的Chrome开发者工具 | https://github.com/ChromeDevTools/chrome-devtools-mcp | 新增 |
| 8 | `browser-use/video-use` | 13797 | 1695 | Python | 554 stars today | 使用编码代理编辑视频 | https://github.com/browser-use/video-use |  |
| 9 | `actions/checkout` | 8164 | 2527 | TypeScript | 26 stars today | 签出仓库的操作 | https://github.com/actions/checkout | 新增 |
| 10 | `affaan-m/ECC` | 225191 | 34459 | JavaScript | 486 stars today | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC | 新增 |
| 11 | `HKUDS/Vibe-Trading` | 17351 | 2886 | Python | 939 stars today | “Vibe-Trading ：您的个人交易代理” | https://github.com/HKUDS/Vibe-Trading |  |
| 12 | `agentskills/agentskills` | 21618 | 1375 | Python | 86 stars today | 客服代表技能的规范和文档 | https://github.com/agentskills/agentskills | 新增 |
| 13 | `openai/codex-plugin-cc` | 22639 | 1377 | JavaScript | 352 stars today | 使用Claude Code的Codex来查看代码或委派任务。 | https://github.com/openai/codex-plugin-cc | 新增 |
| 14 | `langflow-ai/langflow` | 150740 | 9397 | Python | 117 stars today | Langflow是构建和部署人工智能驱动的代理和工作流的强大工具。 | https://github.com/langflow-ai/langflow | 新增 |
| 15 | `pytorch/pytorch` | 101234 | 28227 | Python | 65 stars today | 具有强GPU加速的Python中的张量和动态神经网络 | https://github.com/pytorch/pytorch | 新增 |
| 16 | `harvard-edge/cs249r_book` | 25589 | 3068 | Python | 68 stars today | 机器学习系统 | https://github.com/harvard-edge/cs249r_book | 新增 |
| 17 | `ryanmcdermott/clean-code-javascript` | 94566 | 12473 | JavaScript | 27 stars today | 适用于JavaScript的简洁代码概念 | https://github.com/ryanmcdermott/clean-code-javascript | 新增 |


### 本周 trending（since=weekly）

> Trending HTML 抓取或解析失败： `HTTP Error 500: Internal Server Error`。**since**=`weekly`。


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `apple/container` | 45884 | 1366 | Swift | 19,269 stars this month | 用于在Mac上使用轻量级虚拟机创建和运行Linux容器的工具。它是用Swift编写的，并针对Apple芯片进行了优化。 | https://github.com/apple/container |  |
| 2 | `DeusData/codebase-memory-mcp` | 24696 | 1830 | C | 21,580 stars this month | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 3 | `calesthio/OpenMontage` | 31754 | 3607 | Python | 27,370 stars this month | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 4 | `Panniantong/Agent-Reach` | 49136 | 3918 | Python | 28,309 stars this month | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 5 | `mvanhorn/last30days-skill` | 48502 | 4013 | Python | 21,774 stars this month | 人工智能代理技能，研究Reddit、X、YouTube、HN、Polymarket和网络上的任何主题，然后合成基础摘要 | https://github.com/mvanhorn/last30days-skill |  |
| 6 | `iptv-org/iptv` | 130027 | 7211 | TypeScript | 13,585 stars this month | 收集来自世界各地的公开IPTV频道 | https://github.com/iptv-org/iptv |  |
| 7 | `phuryn/pm-skills` | 22200 | 2237 | — | 10,418 stars this month | PM Skills Marketplace ： 100多种代理技能、命令和插件—从发现到战略、执行、发布和增长。 | https://github.com/phuryn/pm-skills |  |
| 8 | `lfnovo/open-notebook` | 34529 | 3843 | TypeScript | 10,623 stars this month | 笔记本LM的开源实现，具有更大的灵活性和功能 | https://github.com/lfnovo/open-notebook |  |
| 9 | `NVIDIA/cosmos` | 10812 | 736 | Jupyter Notebook | 2,315 stars this month | NVIDIA Cosmos是一个开放的世界模型、数据集和工具平台，使开发人员能够为机器人、自动驾驶汽车、智能基础设施等构建物理AI。 | https://github.com/NVIDIA/cosmos | 新增 |
| 10 | `asgeirtj/system_prompts_leaks` | 47869 | 7795 | JavaScript | 6,834 stars this month | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT 5.5 Thinking ， GPT 5.5 Instant ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 11 | `openai/plugins` | 3933 | 462 | JavaScript | 2,606 stars this month | OpenAI插件 | https://github.com/openai/plugins |  |
| 12 | `alibaba/zvec` | 12720 | 756 | C++ | 3,005 stars this month | 轻量级、快如闪电的进程内矢量数据库 | https://github.com/alibaba/zvec | 新增 |
| 13 | `ogulcancelik/herdr` | 10180 | 599 | Rust | 6,210 stars this month | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 14 | `stablyai/orca` | 11048 | 730 | TypeScript | 6,875 stars this month | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 15 | `Leonxlnx/taste-skill` | 55033 | 3773 | JavaScript | 23,665 stars this month | 品味技能-让您的人工智能有良好的品味。阻止人工智能产生无聊的通用斜坡 | https://github.com/Leonxlnx/taste-skill |  |
| 16 | `t8y2/dbx` | 8261 | 711 | Rust | 5,093 stars this month | 15MB, lightweight, cross-platform database client. Supports MySQL, PostgreSQL, SQLite, Redis, MongoDB, DuckDB, ClickHouse, SQL Server and more.15MB，轻量级跨平台数据库客户端、数据库管理工具。支持 MySQL、PostgreSQL、SQLite、Redis、MongoDB、DuckDB、ClickHouse、SQL Server 等。 | https://github.com/t8y2/dbx |  |
| 17 | `harry0703/MoneyPrinterTurbo` | 95272 | 13854 | Python | 18,098 stars this month | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. | https://github.com/harry0703/MoneyPrinterTurbo |  |
| 18 | `n0-computer/iroh` | 11016 | 509 | Rust | 2,370 stars this month | IP地址中断，改为拨号键。将QUIC + NAT遍历添加到您的应用程序的库。 | https://github.com/n0-computer/iroh |  |
| 19 | `roboflow/supervision` | 46288 | 4104 | Python | 6,556 stars this month | 我们为您编写可重复使用的计算机视觉工具。 💜 | https://github.com/roboflow/supervision |  |
| 20 | `OpenCut-app/OpenCut` | 61358 | 6612 | TypeScript | 9,235 stars this month | 开源CapCut替代方案 | https://github.com/OpenCut-app/OpenCut |  |


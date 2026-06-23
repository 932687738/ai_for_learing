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

**最近一次更新时间**（Asia/Shanghai）： 2026-06-23 09:34:46

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 518534 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 478016 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 450227 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 443563 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 390653 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 379979 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 358015 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 354387 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 353588 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 304346 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `calesthio/OpenMontage` | 12186 | 1561 | Python | 2,938 stars today | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 2 | `palmier-io/palmier-pro` | 7411 | 506 | Swift | 2,463 stars today | 专为人工智能打造的macOS视频编辑器 | https://github.com/palmier-io/palmier-pro |  |
| 3 | `jamiepine/voicebox` | 32287 | 3936 | TypeScript | 529 stars today | 开源AI语音工作室。克隆、命令、创建。 | https://github.com/jamiepine/voicebox | 新增 |
| 4 | `mukul975/Anthropic-Cybersecurity-Skills` | 18731 | 2213 | Python | 956 stars today | 人工智能代理的817种结构化网络安全技能·映射到6个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF和MITRE F3 （打击欺诈） · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20 + p…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills |  |
| 5 | `penpot/penpot` | 52889 | 3386 | Clojure | 728 stars today | Penpot ：用于设计和代码协作的开源设计工具 | https://github.com/penpot/penpot |  |
| 6 | `Stirling-Tools/Stirling-PDF` | 82957 | 7237 | TypeScript | 547 stars today | GitHub上排名第一的PDF应用程序，可让您在任何地方的任何设备上编辑PDF | https://github.com/Stirling-Tools/Stirling-PDF | 新增 |
| 7 | `garrytan/gstack` | 113172 | 16797 | TypeScript | 573 stars today | 使用Garry Tan确切的Claude Code设置： 23个自以为是的工具，分别担任首席执行官、设计师、工程经理、发布经理、文档工程师和QA | https://github.com/garrytan/gstack | 新增 |
| 8 | `heygen-com/hyperframes` | 30034 | 2824 | TypeScript | 395 stars today | 编写HTML。渲染视频。专为客服代表打造。 | https://github.com/heygen-com/hyperframes | 新增 |
| 9 | `tursodatabase/turso` | 21499 | 1089 | Rust | 540 stars today | Turso是一个进程内SQL数据库，与SQLite兼容。 | https://github.com/tursodatabase/turso |  |
| 10 | `bytedance/deer-flow` | 73286 | 9905 | Python | 738 stars today | 研究、编码和创建的开源远程SuperAgent线束。借助沙箱、内存、工具、技能、子代理和消息网关，它可以处理可能需要几分钟到几小时的不同级别的任务。 | https://github.com/bytedance/deer-flow |  |
| 11 | `DeusData/codebase-memory-mcp` | 11623 | 857 | C | 1,185 stars today | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 12 | `ZhuLinsen/daily_stock_analysis` | 45862 | 41929 | Python | 1,557 stars today | LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。 LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs. | https://github.com/ZhuLinsen/daily_stock_analysis |  |
| 13 | `firecrawl/firecrawl` | 137324 | 7962 | TypeScript | 615 stars today | 用于大规模搜索、抓取和与Web交互的API。 🔥 | https://github.com/firecrawl/firecrawl | 新增 |
| 14 | `JCodesMore/ai-website-cloner-template` | 17770 | 2747 | TypeScript | 100 stars today | 使用AI编码代理，只需一个命令即可克隆任何网站 | https://github.com/JCodesMore/ai-website-cloner-template | 新增 |
| 15 | `lyogavin/airllm` | 21065 | 2424 | Jupyter Notebook | 193 stars today | 使用单个4GB GPU的AirLLM 70B推理 | https://github.com/lyogavin/airllm | 新增 |
| 16 | `mattpocock/skills` | 141715 | 12261 | Shell | 2,051 stars today | 真正工程师的技能。直接来自我的.claude目录。 | https://github.com/mattpocock/skills |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `DeusData/codebase-memory-mcp` | 11623 | 857 | C | 7,560 stars this week | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 2 | `calesthio/OpenMontage` | 12188 | 1561 | Python | 6,089 stars this week | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 3 | `Panniantong/Agent-Reach` | 37837 | 3002 | Python | 8,108 stars this week | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 4 | `n0-computer/iroh` | 10543 | 480 | Rust | 1,806 stars this week | IP地址中断，改为拨号键。Rust中的模块化网络堆栈。 | https://github.com/n0-computer/iroh |  |
| 5 | `google-research/timesfm` | 25151 | 2395 | Python | 4,259 stars this week | TimesFM （时间序列基础模型）是由Google Research开发的用于时间序列预测的预训练时间序列基础模型。 | https://github.com/google-research/timesfm |  |
| 6 | `iptv-org/iptv` | 127553 | 7008 | TypeScript | 5,017 stars this week | 收集来自世界各地的公开IPTV频道 | https://github.com/iptv-org/iptv |  |
| 7 | `asgeirtj/system_prompts_leaks` | 45036 | 7414 | JavaScript | 2,612 stars this week | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT 5.5 Thinking ， GPT 5.5 Instant ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 8 | `withastro/flue` | 6431 | 362 | TypeScript | 1,413 stars this week | 沙盒代理框架。 | https://github.com/withastro/flue |  |
| 9 | `NVIDIA/SkillSpector` | 9409 | 736 | Python | 3,302 stars this week | 人工智能代理技能的安全扫描仪。检测漏洞、恶意模式和安全风险。 | https://github.com/NVIDIA/SkillSpector |  |
| 10 | `teslamate-org/teslamate` | 8571 | 966 | Elixir | 401 stars this week | 为您的特斯拉🚘[main maintainer = @ JakobLichterfeld]提供的自托管数据记录器 | https://github.com/teslamate-org/teslamate | 新增 |
| 11 | `penpot/penpot` | 52891 | 3386 | Clojure | 2,983 stars this week | Penpot ：用于设计和代码协作的开源设计工具 | https://github.com/penpot/penpot | 新增 |
| 12 | `makeplane/plane` | 52576 | 4682 | TypeScript | 1,696 stars this week | 🔥🔥🔥 开源JIRA、Linear、Monday和ClickUp替代方案。Plane是一个现代化的项目管理平台，用于管理任务、冲刺、文档和分类。 | https://github.com/makeplane/plane |  |
| 13 | `Kong/insomnia` | 39556 | 2344 | TypeScript | 1,074 stars this week | GraphQL、REST、WebSockets、SSE和gRPC的开源、跨平台API客户端。使用云、本地和Git存储。 | https://github.com/Kong/insomnia |  |
| 14 | `addyosmani/agent-skills` | 65418 | 7065 | Shell | 5,277 stars this week | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 15 | `freeCodeCamp/freeCodeCamp` | 450227 | 45211 | TypeScript | 2,670 stars this week | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 16 | `koala73/worldmonitor` | 58624 | 9256 | TypeScript | 2,090 stars this week | 实时全球智能仪表板。在统一的态势感知界面中进行人工智能驱动的新闻聚合、地缘政治监控和基础设施跟踪 | https://github.com/koala73/worldmonitor | 新增 |
| 17 | `LMCache/LMCache` | 9627 | 1382 | Python | 503 stars this week | LMCache ：使用最快的KV缓存层为您的LLM增压 | https://github.com/LMCache/LMCache |  |
| 18 | `OpenCut-app/OpenCut` | 58880 | 6421 | TypeScript | 3,097 stars this week | 开源CapCut替代方案 | https://github.com/OpenCut-app/OpenCut | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `harry0703/MoneyPrinterTurbo` | 91325 | 13164 | Python | 34,221 stars this month | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. | https://github.com/harry0703/MoneyPrinterTurbo |  |
| 2 | `Egonex-AI/Understand-Anything` | 66179 | 5491 | TypeScript | 48,730 stars this month | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Egonex-AI/Understand-Anything |  |
| 3 | `apple/container` | 39542 | 1154 | Swift | 13,030 stars this month | 用于在Mac上使用轻量级虚拟机创建和运行Linux容器的工具。它是用Swift编写的，并针对Apple芯片进行了优化。 | https://github.com/apple/container |  |
| 4 | `esengine/DeepSeek-Reasonix` | 23873 | 1453 | Go | 18,633 stars this month | 为您的终端提供DeepSeek原生AI编码代理。围绕前缀缓存稳定性而设计—保持运行。 | https://github.com/esengine/DeepSeek-Reasonix |  |
| 5 | `microsoft/markitdown` | 157783 | 11014 | Python | 33,664 stars this month | 用于将文件和Office文档转换为Markdown的Python工具。 | https://github.com/microsoft/markitdown |  |
| 6 | `colbymchenry/codegraph` | 53200 | 3246 | TypeScript | 37,636 stars this month | 预索引的代码知识图，在代码更改时自动同步，适用于Claude Code、Codex、Gemini、Cursor、OpenCode、AntiGravity、Kiro和Hermes Agent —代币更少，工具调用更少， 100%本地 | https://github.com/colbymchenry/codegraph |  |
| 7 | `hardikpandya/stop-slop` | 11884 | 833 | — | 8,139 stars this month | 从散文中删除AI TELLS的技能文件 | https://github.com/hardikpandya/stop-slop |  |
| 8 | `mvanhorn/last30days-skill` | 45803 | 3803 | Python | 19,626 stars this month | 人工智能代理技能，研究Reddit、X、YouTube、HN、Polymarket和网络上的任何主题，然后合成基础摘要 | https://github.com/mvanhorn/last30days-skill |  |
| 9 | `Leonxlnx/taste-skill` | 49079 | 3407 | JavaScript | 30,554 stars this month | 品味技能-让您的人工智能有良好的品味。阻止人工智能产生无聊的通用斜坡 | https://github.com/Leonxlnx/taste-skill |  |
| 10 | `iptv-org/iptv` | 127553 | 7008 | TypeScript | 11,367 stars this month | 收集来自世界各地的公开IPTV频道 | https://github.com/iptv-org/iptv |  |
| 11 | `DeusData/codebase-memory-mcp` | 11623 | 857 | C | 8,616 stars this month | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 12 | `Panniantong/Agent-Reach` | 37837 | 3002 | Python | 17,676 stars this month | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 13 | `tashfeenahmed/freellmapi` | 11585 | 1819 | TypeScript | 7,794 stars this month | OpenAI兼容代理，将16个LLM提供商的免费层（约17亿个代币/月）堆叠在一个/v1端点后面—加上任何自定义OpenAI兼容端点。智能路由、自动故障转移、加密密钥。仅限个人实验。 | https://github.com/tashfeenahmed/freellmapi |  |
| 14 | `can1357/oh-my-pi` | 14140 | 1242 | TypeScript | 7,990 stars this month | 终端的AI编码代理—哈希锚定编辑、优化工具线束、LSP、Python、浏览器、子代理等 | https://github.com/can1357/oh-my-pi |  |
| 15 | `rohitg00/ai-engineering-from-scratch` | 35685 | 5820 | Python | 24,428 stars this month | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 16 | `lfnovo/open-notebook` | 32619 | 3687 | TypeScript | 9,014 stars this month | 笔记本LM的开源实现，具有更大的灵活性和功能 | https://github.com/lfnovo/open-notebook |  |
| 17 | `mukul975/Anthropic-Cybersecurity-Skills` | 18732 | 2213 | Python | 11,735 stars this month | 人工智能代理的817种结构化网络安全技能·映射到6个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF和MITRE F3 （打击欺诈） · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20 + p…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills |  |
| 18 | `phuryn/pm-skills` | 20555 | 2094 | — | 9,061 stars this month | PM Skills Marketplace ： 100多种代理技能、命令和插件—从发现到战略、执行、发布和增长。 | https://github.com/phuryn/pm-skills |  |
| 19 | `openai/plugins` | 3365 | 403 | JavaScript | 2,163 stars this month | OpenAI插件 | https://github.com/openai/plugins |  |
| 20 | `anthropics/knowledge-work-plugins` | 21751 | 2542 | Python | 9,392 stars this month | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins |  |
| 21 | `ogulcancelik/herdr` | 6830 | 419 | Rust | 4,737 stars this month | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |


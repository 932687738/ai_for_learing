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

**最近一次更新时间**（Asia/Shanghai）： 2026-06-10 07:23:28

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 513618 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 474320 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 446527 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 440500 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 389999 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 377827 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 356637 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 352391 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 350991 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 302119 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `mvanhorn/last30days-skill` | 37228 | 3024 | Python | 3,177 stars today | 人工智能代理技能，研究Reddit、X、YouTube、HN、Polymarket和网络上的任何主题，然后合成基础摘要 | https://github.com/mvanhorn/last30days-skill |  |
| 2 | `RyanCodrai/turbovec` | 10125 | 868 | Python | 1,800 stars today | 基于TurboQuant构建的矢量索引，用Rust和Python绑定编写 | https://github.com/RyanCodrai/turbovec |  |
| 3 | `roboflow/supervision` | 42959 | 3832 | Python | 735 stars today | 我们为您编写可重复使用的计算机视觉工具。 💜 | https://github.com/roboflow/supervision |  |
| 4 | `opencv/opencv` | 88608 | 56621 | C++ | 169 stars today | 开源计算机视觉库 | https://github.com/opencv/opencv | 新增 |
| 5 | `refactoringhq/tolaria` | 14286 | 994 | TypeScript | 821 stars today | 用于管理降价知识库的桌面应用程序 | https://github.com/refactoringhq/tolaria |  |
| 6 | `aaif-goose/goose` | 48483 | 5094 | Rust | 490 stars today | 开源、可扩展的AI代理，超越代码建议-使用任何LLM安装、执行、编辑和测试 | https://github.com/aaif-goose/goose |  |
| 7 | `Andyyyy64/whichllm` | 4060 | 225 | Python | 631 stars today | 查找在您的硬件上实际运行并表现最佳的本地LLM。按真实、近期感知的基准排名，而不是参数计数。只需一个命令，即可立即运行。 | https://github.com/Andyyyy64/whichllm |  |
| 8 | `TapXWorld/ChinaTextbook` | 73450 | 16444 | Roff | 517 stars today | 所有小初高、大学PDF教材。 | https://github.com/TapXWorld/ChinaTextbook |  |
| 9 | `x1xhlol/system-prompts-and-models-of-ai-tools` | 139132 | 34558 | — | 66 stars today | 完整的Augment Code、Claude Code、Cluely、CodeBuddy、Comet、Cursor、Devin AI、Junie、Kiro、Leap.new、Lovable、Manus、NotionAI、Orchids.app、Perplexity、Poke、Qoder、Replit、Same.dev、Trae、Traycer AI、VSCode Agent、Warp.dev、Windsurf、Xcode、Z.ai Code、Dia &amp; v0。（以及其他Ope…… | https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools | 新增 |
| 10 | `yikart/AiToEarn` | 19892 | 3017 | TypeScript | 423 stars today | 让我们使用人工智能来赚取收入！ | https://github.com/yikart/AiToEarn | 新增 |
| 11 | `phuryn/pm-skills` | 13397 | 1537 | — | 808 stars today | PM Skills Marketplace ： 100多种代理技能、命令和插件—从发现到战略、执行、发布和增长。 | https://github.com/phuryn/pm-skills |  |
| 12 | `santifer/career-ops` | 51595 | 10413 | JavaScript | 1,114 stars today | 基于Claude Code构建的人工智能求职系统。14种技能模式、Go仪表板、PDF生成、批量处理。 | https://github.com/santifer/career-ops |  |
| 13 | `openai/plugins` | 2586 | 305 | JavaScript | 284 stars today | OpenAI插件 | https://github.com/openai/plugins |  |
| 14 | `maziyarpanahi/openmed` | 1825 | 213 | Python | 165 stars today | 开源医疗保健人工智能 | https://github.com/maziyarpanahi/openmed | 新增 |
| 15 | `francescopace/espectre` | 8184 | 632 | Python | 112 stars today | 🛜 ESPectre 👻 -基于Wi-Fi光谱分析（ CSI ）的运动检测系统，与Home Assistant集成。 | https://github.com/francescopace/espectre | 新增 |
| 16 | `addyosmani/agent-skills` | 49797 | 5563 | Shell | 348 stars today | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `chopratejas/headroom` | 20490 | 1313 | Python | 14,266 stars this week | 在工具输出、日志、文件和RAG块到达LLM之前对其进行压缩。令牌减少60-95% ，答案相同。库、代理、MCP服务器。 | https://github.com/chopratejas/headroom |  |
| 2 | `mvanhorn/last30days-skill` | 37228 | 3024 | Python | 6,616 stars this week | 人工智能代理技能，研究Reddit、X、YouTube、HN、Polymarket和网络上的任何主题，然后合成基础摘要 | https://github.com/mvanhorn/last30days-skill |  |
| 3 | `microsoft/markitdown` | 149323 | 10271 | Python | 11,177 stars this week | 用于将文件和Office文档转换为Markdown的Python工具。 | https://github.com/microsoft/markitdown |  |
| 4 | `openai/plugins` | 2586 | 305 | JavaScript | 899 stars this week | OpenAI插件 | https://github.com/openai/plugins |  |
| 5 | `Panniantong/Agent-Reach` | 25533 | 2123 | Python | 3,006 stars this week | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 6 | `Leonxlnx/taste-skill` | 39520 | 2794 | Shell | 7,597 stars this week | 品味技能-让您的人工智能有良好的品味。阻止人工智能产生无聊的通用斜坡 | https://github.com/Leonxlnx/taste-skill |  |
| 7 | `lfnovo/open-notebook` | 28566 | 3233 | TypeScript | 3,891 stars this week | 笔记本LM的开源实现，具有更大的灵活性和功能 | https://github.com/lfnovo/open-notebook |  |
| 8 | `Open-LLM-VTuber/Open-LLM-VTuber` | 10723 | 1244 | Python | 2,528 stars this week | 通过免提语音交互、语音中断和跨平台本地运行的Live2D与任何LLM交谈 | https://github.com/Open-LLM-VTuber/Open-LLM-VTuber |  |
| 9 | `affaan-m/ECC` | 211857 | 32517 | JavaScript | 9,301 stars this week | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 10 | `aquasecurity/trivy` | 36235 | 465 | Go | 919 stars this week | 查找漏洞、错误配置、秘密、容器中的SBOM、Kubernetes、代码仓库、云等 | https://github.com/aquasecurity/trivy |  |
| 11 | `revfactory/harness` | 6666 | 909 | HTML | 1,553 stars this week | 一种元技能，用于设计特定领域的座席团队，定义专业座席，并生成他们使用的技能。 | https://github.com/revfactory/harness |  |
| 12 | `NousResearch/hermes-agent` | 188771 | 32555 | Python | 11,747 stars this week | 与您一起成长的客服代表 | https://github.com/NousResearch/hermes-agent |  |
| 13 | `phuryn/pm-skills` | 13397 | 1537 | — | 640 stars this week | PM Skills Marketplace ： 100多种代理技能、命令和插件—从发现到战略、执行、发布和增长。 | https://github.com/phuryn/pm-skills |  |
| 14 | `supermemoryai/supermemory` | 26337 | 2292 | TypeScript | 2,434 stars this week | 内存引擎和应用程序，速度极快，可扩展。人工智能时代的内存API。 | https://github.com/supermemoryai/supermemory |  |
| 15 | `CopilotKit/CopilotKit` | 34452 | 4320 | TypeScript | 2,173 stars this week | Agent和生成式UI的前端堆栈。React、Angular、Mobile、Slack等。AG-UI协议的制定者 | https://github.com/CopilotKit/CopilotKit | 新增 |
| 16 | `pbakaus/impeccable` | 36776 | 2005 | JavaScript | 3,736 stars this week | 让您的人工智能更好地进行设计的设计语言。 | https://github.com/pbakaus/impeccable |  |
| 17 | `can1357/oh-my-pi` | 11528 | 970 | TypeScript | 1,952 stars this week | 终端的AI编码代理—哈希锚定编辑、优化工具线束、LSP、Python、浏览器、子代理等 | https://github.com/can1357/oh-my-pi |  |
| 18 | `EveryInc/compound-engineering-plugin` | 20767 | 1533 | TypeScript | 1,568 stars this week | Claude Code、Codex、Cursor等的官方复合工程插件 | https://github.com/EveryInc/compound-engineering-plugin | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `colbymchenry/codegraph` | 45881 | 2810 | TypeScript | 43,749 stars this month | Claude Code、Codex、Gemini、Cursor、OpenCode、AntiGravity、Kiro和Hermes Agent的预索引代码知识图—代币更少，工具调用更少， 100%本地化 | https://github.com/colbymchenry/codegraph |  |
| 2 | `chopratejas/headroom` | 20490 | 1313 | Python | 16,237 stars this month | 在工具输出、日志、文件和RAG块到达LLM之前对其进行压缩。令牌减少60-95% ，答案相同。库、代理、MCP服务器。 | https://github.com/chopratejas/headroom |  |
| 3 | `Egonex-AI/Understand-Anything` | 55896 | 4627 | TypeScript | 41,974 stars this month | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Egonex-AI/Understand-Anything |  |
| 4 | `harry0703/MoneyPrinterTurbo` | 83662 | 11911 | Python | 25,436 stars this month | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. | https://github.com/harry0703/MoneyPrinterTurbo |  |
| 5 | `CloakHQ/CloakBrowser` | 25173 | 2004 | Python | 22,447 stars this month | Stealth Chromium可通过每次机器人检测测试。插入式剧作家更换源级指纹补丁，通过30/30测试 | https://github.com/CloakHQ/CloakBrowser |  |
| 6 | `rohitg00/agentmemory` | 22110 | 1815 | TypeScript | 19,359 stars this month | # 1基于真实世界基准的AI编码代理持久内存 | https://github.com/rohitg00/agentmemory |  |
| 7 | `rohitg00/ai-engineering-from-scratch` | 30731 | 5008 | Python | 23,852 stars this month | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 8 | `Imbad0202/academic-research-skills` | 29488 | 2441 | Python | 24,020 stars this month | Claude Code的学术研究技能：研究→撰写→评审→修订→最终确定 | https://github.com/Imbad0202/academic-research-skills |  |
| 9 | `ruvnet/RuView` | 72425 | 9685 | Rust | 20,463 stars this month | π RuView将商用WiFi信号转化为实时空间智能、生命体征监测和存在检测--所有这些都无需一个像素的视频。 | https://github.com/ruvnet/RuView |  |
| 10 | `fathah/hermes-desktop` | 11541 | 1311 | TypeScript | 9,936 stars this month | Hermès Agent桌面配套 | https://github.com/fathah/hermes-desktop |  |
| 11 | `can1357/oh-my-pi` | 11528 | 970 | TypeScript | 7,167 stars this month | 终端的AI编码代理—哈希锚定编辑、优化工具线束、LSP、Python、浏览器、子代理等 | https://github.com/can1357/oh-my-pi |  |
| 12 | `mattpocock/skills` | 123140 | 10757 | Shell | 55,905 stars this month | 真正工程师的技能。直接来自我的.claude目录。 | https://github.com/mattpocock/skills |  |
| 13 | `yikart/AiToEarn` | 19892 | 3017 | TypeScript | 10,222 stars this month | 让我们使用人工智能来赚取收入！ | https://github.com/yikart/AiToEarn |  |
| 14 | `HKUDS/ViMax` | 9473 | 1418 | Python | 5,702 stars this month | "ViMax ： Agentic Video Generation （导演、编剧、制片人和视频生成器一体机）" | https://github.com/HKUDS/ViMax |  |
| 15 | `anthropics/knowledge-work-plugins` | 19920 | 2377 | Python | 7,829 stars this month | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins | 新增 |
| 16 | `microsoft/markitdown` | 149323 | 10271 | Python | 26,881 stars this month | 用于将文件和Office文档转换为Markdown的Python工具。 | https://github.com/microsoft/markitdown |  |
| 17 | `Leonxlnx/taste-skill` | 39521 | 2794 | Shell | 22,388 stars this month | 品味技能-让您的人工智能有良好的品味。阻止人工智能产生无聊的通用斜坡 | https://github.com/Leonxlnx/taste-skill | 新增 |
| 18 | `hardikpandya/stop-slop` | 9702 | 686 | — | 6,143 stars this month | 从散文中删除AI TELLS的技能文件 | https://github.com/hardikpandya/stop-slop | 新增 |
| 19 | `oven-sh/bun` | 93007 | 4693 | Rust | 3,777 stars this month | 令人难以置信的快速JavaScript运行时、捆绑程序、测试运行程序和包管理器–所有功能于一身 | https://github.com/oven-sh/bun |  |


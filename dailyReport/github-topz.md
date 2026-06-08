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

**最近一次更新时间**（Asia/Shanghai）： 2026-06-08 09:03:40

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 512885 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 473803 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 446377 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 440032 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 389846 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 377443 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 356484 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 352137 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 350770 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 301815 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
| 11 | `awesome-selfhosted/awesome-selfhosted` | 297418 | 可自行部署的各类自由软件网络服务与 Web 应用清单。 | https://github.com/awesome-selfhosted/awesome-selfhosted |  |
| 12 | `996icu/996.ICU` | 276265 | 倡议关注「996」工作制、计数星标与交流的开发社区仓库（含网络迷因用语）。 | https://github.com/996icu/996.ICU |  |
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
| 1 | `mvanhorn/last30days-skill` | 31019 | 2595 | Python | 1,111 stars today | 人工智能代理技能，研究Reddit、X、YouTube、HN、Polymarket和网络上的任何主题，然后合成基础摘要 | https://github.com/mvanhorn/last30days-skill |  |
| 2 | `opencv/opencv` | 88088 | 56597 | C++ | 65 stars today | 开源计算机视觉库 | https://github.com/opencv/opencv | 新增 |
| 3 | `Leonxlnx/taste-skill` | 36643 | 2642 | Shell | 1,103 stars today | 品味技能-让您的人工智能有良好的品味。阻止人工智能产生无聊的通用斜坡 | https://github.com/Leonxlnx/taste-skill | 新增 |
| 4 | `NousResearch/hermes-agent` | 185950 | 31984 | Python | 1,112 stars today | 与您一起成长的客服代表 | https://github.com/NousResearch/hermes-agent |  |
| 5 | `lfnovo/open-notebook` | 27263 | 3098 | TypeScript | 554 stars today | 笔记本LM的开源实现，具有更大的灵活性和功能 | https://github.com/lfnovo/open-notebook |  |
| 6 | `yikart/AiToEarn` | 18757 | 2909 | TypeScript | 183 stars today | 让我们使用人工智能来赚取收入！ | https://github.com/yikart/AiToEarn | 新增 |
| 7 | `aaif-goose/goose` | 47513 | 5014 | Rust | 322 stars today | 开源、可扩展的AI代理，超越代码建议-使用任何LLM安装、执行、编辑和测试 | https://github.com/aaif-goose/goose | 新增 |
| 8 | `Crosstalk-Solutions/project-nomad` | 29725 | 2946 | TypeScript | 309 stars today | Project N.O.M.A.D是一款独立的离线生存计算机，配备了关键工具、知识和人工智能，可随时随地让您随时了解情况并获得授权。 | https://github.com/Crosstalk-Solutions/project-nomad | 新增 |
| 9 | `ggml-org/llama.cpp` | 115329 | 19302 | C++ | 158 stars today | C/C + +中的LLM推理 | https://github.com/ggml-org/llama.cpp | 新增 |
| 10 | `RyanCodrai/turbovec` | 7188 | 699 | Python | 1,554 stars today | 基于TurboQuant构建的矢量索引，用Rust和Python绑定编写 | https://github.com/RyanCodrai/turbovec | 新增 |
| 11 | `TapXWorld/ChinaTextbook` | 72451 | 16239 | Roff | 350 stars today | 所有小初高、大学PDF教材。 | https://github.com/TapXWorld/ChinaTextbook | 新增 |
| 12 | `openai/plugins` | 2032 | 271 | JavaScript | 262 stars today | OpenAI插件 | https://github.com/openai/plugins |  |
| 13 | `refactoringhq/tolaria` | 12878 | 909 | TypeScript | 245 stars today | 用于管理降价知识库的桌面应用程序 | https://github.com/refactoringhq/tolaria | 新增 |
| 14 | `HunxByts/GhostTrack` | 13732 | 1834 | Python | 28 stars today | 跟踪位置或手机号码的有用工具 | https://github.com/HunxByts/GhostTrack | 新增 |
| 15 | `microsoft/pg_durable` | 1456 | 33 | Rust | 316 stars today | PostgreSQL数据库内持久执行 | https://github.com/microsoft/pg_durable | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `chopratejas/headroom` | 16937 | 1081 | Python | 14,272 stars this week | 在工具输出、日志、文件和RAG块到达LLM之前对其进行压缩。令牌减少60-95% ，答案相同。库、代理、MCP服务器。 | https://github.com/chopratejas/headroom |  |
| 2 | `microsoft/markitdown` | 147348 | 10099 | Python | 13,359 stars this week | 用于将文件和Office文档转换为Markdown的Python工具。 | https://github.com/microsoft/markitdown |  |
| 3 | `harry0703/MoneyPrinterTurbo` | 81198 | 11560 | Python | 7,992 stars this week | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. | https://github.com/harry0703/MoneyPrinterTurbo |  |
| 4 | `supermemoryai/supermemory` | 26015 | 2268 | TypeScript | 2,924 stars this week | 内存引擎和应用程序，速度极快，可扩展。人工智能时代的内存API。 | https://github.com/supermemoryai/supermemory |  |
| 5 | `affaan-m/ECC` | 209848 | 32170 | JavaScript | 10,207 stars this week | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 6 | `Open-LLM-VTuber/Open-LLM-VTuber` | 10355 | 1219 | Python | 2,388 stars this week | 通过免提语音交互、语音中断和跨平台本地运行的Live2D与任何LLM交谈 | https://github.com/Open-LLM-VTuber/Open-LLM-VTuber |  |
| 7 | `revfactory/harness` | 6414 | 868 | HTML | 1,958 stars this week | 一种元技能，用于设计特定领域的座席团队，定义专业座席，并生成他们使用的技能。 | https://github.com/revfactory/harness |  |
| 8 | `mvanhorn/last30days-skill` | 31020 | 2595 | Python | 2,718 stars this week | 人工智能代理技能，研究Reddit、X、YouTube、HN、Polymarket和网络上的任何主题，然后合成基础摘要 | https://github.com/mvanhorn/last30days-skill | 新增 |
| 9 | `Leonxlnx/taste-skill` | 36643 | 2642 | Shell | 6,385 stars this week | 品味技能-让您的人工智能有良好的品味。阻止人工智能产生无聊的通用斜坡 | https://github.com/Leonxlnx/taste-skill |  |
| 10 | `EveryInc/compound-engineering-plugin` | 20369 | 1511 | TypeScript | 1,762 stars this week | Claude Code、Codex、Cursor等的官方复合工程插件 | https://github.com/EveryInc/compound-engineering-plugin |  |
| 11 | `can1357/oh-my-pi` | 11094 | 935 | TypeScript | 2,117 stars this week | 终端的AI编码代理—哈希锚定编辑、优化工具线束、LSP、Python、浏览器、子代理等 | https://github.com/can1357/oh-my-pi |  |
| 12 | `openai/plugins` | 2032 | 272 | JavaScript | 595 stars this week | OpenAI插件 | https://github.com/openai/plugins | 新增 |
| 13 | `aquasecurity/trivy` | 36113 | 457 | Go | 844 stars this week | 查找漏洞、错误配置、秘密、容器中的SBOM、Kubernetes、代码仓库、云等 | https://github.com/aquasecurity/trivy | 新增 |
| 14 | `Panniantong/Agent-Reach` | 23159 | 1958 | Python | 2,289 stars this week | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach | 新增 |
| 15 | `NousResearch/hermes-agent` | 185950 | 31984 | Python | 11,427 stars this week | 与您一起成长的客服代表 | https://github.com/NousResearch/hermes-agent | 新增 |
| 16 | `lfnovo/open-notebook` | 27263 | 3098 | TypeScript | 2,993 stars this week | 笔记本LM的开源实现，具有更大的灵活性和功能 | https://github.com/lfnovo/open-notebook | 新增 |
| 17 | `pbakaus/impeccable` | 35556 | 1939 | JavaScript | 3,586 stars this week | 让您的人工智能更好地进行设计的设计语言。 | https://github.com/pbakaus/impeccable | 新增 |
| 18 | `nesquena/hermes-webui` | 13847 | 1701 | Python | 4,281 stars this week | Hermes WebUI ：通过网络或手机使用Hermes Agent的最佳方式！ | https://github.com/nesquena/hermes-webui | 新增 |
| 19 | `dmtrKovalenko/fff` | 7677 | 310 | Rust | 879 stars this week | 适用于AI代理、Neovim、Rust、C和NodeJS的最快、最准确的文件搜索工具包 | https://github.com/dmtrKovalenko/fff | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `colbymchenry/codegraph` | 43768 | 2694 | TypeScript | 42,778 stars this month | Claude Code、Codex、Gemini、Cursor、OpenCode、AntiGravity、Kiro和Hermes Agent的预索引代码知识图—代币更少，工具调用更少， 100%本地化 | https://github.com/colbymchenry/codegraph |  |
| 2 | `chopratejas/headroom` | 16937 | 1081 | Python | 14,922 stars this month | 在工具输出、日志、文件和RAG块到达LLM之前对其进行压缩。令牌减少60-95% ，答案相同。库、代理、MCP服务器。 | https://github.com/chopratejas/headroom |  |
| 3 | `CloakHQ/CloakBrowser` | 24688 | 1971 | Python | 22,732 stars this month | Stealth Chromium可通过每次机器人检测测试。插入式剧作家更换源级指纹补丁，通过30/30测试 | https://github.com/CloakHQ/CloakBrowser |  |
| 4 | `Lum1104/Understand-Anything` | 54378 | 4489 | TypeScript | 41,326 stars this month | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Lum1104/Understand-Anything |  |
| 5 | `rohitg00/agentmemory` | 21740 | 1790 | TypeScript | 19,547 stars this month | # 1基于真实世界基准的AI编码代理持久内存 | https://github.com/rohitg00/agentmemory |  |
| 6 | `harry0703/MoneyPrinterTurbo` | 81198 | 11560 | Python | 24,500 stars this month | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. | https://github.com/harry0703/MoneyPrinterTurbo |  |
| 7 | `fathah/hermes-desktop` | 11005 | 1282 | TypeScript | 9,784 stars this month | Hermès Agent桌面配套 | https://github.com/fathah/hermes-desktop |  |
| 8 | `Imbad0202/academic-research-skills` | 28542 | 2371 | Python | 23,725 stars this month | Claude Code的学术研究技能：研究→撰写→评审→修订→最终确定 | https://github.com/Imbad0202/academic-research-skills |  |
| 9 | `rohitg00/ai-engineering-from-scratch` | 29877 | 4869 | Python | 23,390 stars this month | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 10 | `ruvnet/RuView` | 71680 | 9556 | Rust | 20,236 stars this month | π RuView将商用WiFi信号转化为实时空间智能、生命体征监测和存在检测--所有这些都无需一个像素的视频。 | https://github.com/ruvnet/RuView |  |
| 11 | `yikart/AiToEarn` | 18757 | 2909 | TypeScript | 9,466 stars this month | 让我们使用人工智能来赚取收入！ | https://github.com/yikart/AiToEarn |  |
| 12 | `mattpocock/skills` | 120413 | 10554 | Shell | 56,562 stars this month | 真正工程师的技能。直接来自我的.claude目录。 | https://github.com/mattpocock/skills |  |
| 13 | `can1357/oh-my-pi` | 11094 | 935 | TypeScript | 7,042 stars this month | 终端的AI编码代理—哈希锚定编辑、优化工具线束、LSP、Python、浏览器、子代理等 | https://github.com/can1357/oh-my-pi |  |
| 14 | `HKUDS/ViMax` | 9021 | 1373 | Python | 5,983 stars this month | "ViMax ： Agentic Video Generation （导演、编剧、制片人和视频生成器一体机）" | https://github.com/HKUDS/ViMax |  |
| 15 | `anthropics/financial-services` | 30400 | 4293 | Python | 20,299 stars this month | — | https://github.com/anthropics/financial-services |  |
| 16 | `millionco/react-doctor` | 12336 | 392 | TypeScript | 5,994 stars this month | 您的代理写入了错误的React。这会捕获它 | https://github.com/millionco/react-doctor | 新增 |
| 17 | `decolua/9router` | 16782 | 2537 | JavaScript | 12,666 stars this month | 无限免费AI编码。通过40多家供应商将Claude Code、Codex、Cursor、Cline、Copilot、Antigravity连接到免费的Claude/GPT/Gemini。自动回退， RTK -40%代币，从未达到限制。 | https://github.com/decolua/9router |  |
| 18 | `microsoft/markitdown` | 147349 | 10099 | Python | 26,145 stars this month | 用于将文件和Office文档转换为Markdown的Python工具。 | https://github.com/microsoft/markitdown | 新增 |
| 19 | `nesquena/hermes-webui` | 13847 | 1701 | Python | 7,927 stars this month | Hermes WebUI ：通过网络或手机使用Hermes Agent的最佳方式！ | https://github.com/nesquena/hermes-webui | 新增 |


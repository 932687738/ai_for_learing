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

**最近一次更新时间**（Asia/Shanghai）： 2026-07-07 09:08:49

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 523037 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 482292 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 451178 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 447244 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 391382 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 381955 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 359526 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 356423 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 355304 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 306705 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
| 11 | `awesome-selfhosted/awesome-selfhosted` | 301670 | 可自行部署的各类自由软件网络服务与 Web 应用清单。 | https://github.com/awesome-selfhosted/awesome-selfhosted |  |
| 12 | `996icu/996.ICU` | 276361 | 倡议关注「996」工作制、计数星标与交流的开发社区仓库（含网络迷因用语）。 | https://github.com/996icu/996.ICU |  |
| 13 | `practical-tutorials/project-based-learning` | 272207 | 基于项目的教程精选列表 | https://github.com/practical-tutorials/project-based-learning |  |
| 14 | `obra/superpowers` | 246876 | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers |  |
| 15 | `facebook/react` | 245279 | 用于构建 Web 与原生用户界面的 React 视图库（含多端生态）。 | https://github.com/facebook/react |  |
| 16 | `torvalds/linux` | 238531 | Linux内核源树 | https://github.com/torvalds/linux |  |

---
## Trending 页面快照（HTML 抓取）

**说明**：与上方「全局 Star Search」数据源不同；本段按 GitHub trending 页的 **daily / weekly / monthly** 各拉一页并解析。**若前端改版导致选择器失效，需更新解析逻辑。**

- **标记**列：三个 `since` 子表**各自独立**对照本次拉取前文件中该小节表格已出现的 `owner/repo`；新出现的行标 **新增**。下次拉取会先清空上一轮「新增」再重算（只保留相对**上一版文件**的新仓库）。

### 今日 trending（since=daily）

**页面**： `https://github.com/trending?since=daily`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `asgeirtj/system_prompts_leaks` | 51543 | 8398 | JavaScript | 1,378 stars today | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT 5.5 Thinking ， GPT 5.5 Instant ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 2 | `addyosmani/agent-skills` | 70829 | 7676 | JavaScript | 1,112 stars today | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills | 新增 |
| 3 | `Zackriya-Solutions/meetily` | 19400 | 1966 | Rust | 2,494 stars today | 隐私第一，基于Rust构建的人工智能会议助手，具有4倍的Parakeet/Whisper实时转录、扬声器日记和Ollama摘要。100%本地处理。无需云。Meetily （ Meetly Ai - https://meetily.ai ）是首屈一指的自托管、开源Ai会议...... | https://github.com/Zackriya-Solutions/meetily |  |
| 4 | `ruvnet/RuView` | 77527 | 10413 | Rust | 470 stars today | π RuView将商用WiFi信号转化为实时空间智能、生命体征监测和存在检测--所有这些都无需一个像素的视频。 | https://github.com/ruvnet/RuView |  |
| 5 | `Leonxlnx/taste-skill` | 58947 | 4015 | JavaScript | 1,458 stars today | 品味技能-让您的人工智能有良好的品味。阻止人工智能产生无聊的通用斜坡 | https://github.com/Leonxlnx/taste-skill |  |
| 6 | `alirezarezvani/claude-skills` | 21155 | 2841 | Python | 610 stars today | 345 Claude Code技能和代理技能和插件（ 30多个代理、70多个自定义命令、330多个技能、可定制的参考、脚本） ，适用于Claude Code、Codex、Gemini CLI、Cursor和其他8个编码代理—工程、营销、产品、合规、C级咨询、研究…… | https://github.com/alirezarezvani/claude-skills |  |
| 7 | `openai/codex-plugin-cc` | 26283 | 1573 | JavaScript | 906 stars today | 使用Claude Code的Codex来查看代码或委派任务。 | https://github.com/openai/codex-plugin-cc |  |
| 8 | `mvanhorn/last30days-skill` | 49758 | 4145 | Python | 458 stars today | 人工智能代理技能，研究Reddit、X、YouTube、HN、Polymarket和网络上的任何主题，然后合成基础摘要 | https://github.com/mvanhorn/last30days-skill | 新增 |
| 9 | `ogulcancelik/herdr` | 12873 | 748 | Rust | 779 stars today | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 10 | `bradautomates/claude-video` | 4242 | 603 | Python | 427 stars today | 让Claude能够观看任何视频。/观看下载、提取帧、转录，并将所有内容交给Claude。 | https://github.com/bradautomates/claude-video | 新增 |
| 11 | `karakeep-app/karakeep` | 26902 | 1319 | TypeScript | 199 stars today | 可自托管的书签应用程序（链接、笔记和图像） ，具有基于AI的自动标记和全文搜索功能 | https://github.com/karakeep-app/karakeep | 新增 |
| 12 | `firecrawl/firecrawl` | 146267 | 8412 | TypeScript | 867 stars today | 用于大规模搜索、抓取和与Web交互的API。 🔥 | https://github.com/firecrawl/firecrawl | 新增 |
| 13 | `steipete/CodexBar` | 16738 | 1375 | Swift | 598 stars today | 显示OpenAI Codex和Claude Code的使用统计信息，无需登录。 | https://github.com/steipete/CodexBar |  |
| 14 | `alibaba/zvec` | 13508 | 823 | C++ | 382 stars today | 轻量级、快如闪电的进程内矢量数据库 | https://github.com/alibaba/zvec | 新增 |
| 15 | `sindresorhus/awesome` | 482292 | 35737 | — | 345 stars today | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome | 新增 |
| 16 | `gastownhall/gastown` | 16697 | 1539 | Go | 291 stars today | Gas Town -多代理工作区经理 | https://github.com/gastownhall/gastown |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `usestrix/strix` | 37988 | 3860 | Python | 10,759 stars this week | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 2 | `hasaneyldrm/exercises-dataset` | 10200 | 1154 | HTML | 5,665 stars this week | 包含433项健身练习的综合数据集。每个条目包括名称、类别、目标肌肉群、设备、说明、缩略图和动画视频。 | https://github.com/hasaneyldrm/exercises-dataset | 新增 |
| 3 | `diegosouzapw/OmniRoute` | 12588 | 1827 | TypeScript | 4,594 stars this week | 永不停止编码。免费AI网关：一个端点， 231多家提供商（ 50多家免费） ，将Claude Code、Codex、Cursor、Cline和Copilot连接到免费的Claude/GPT/Gemini。RTK + Caveman堆叠压缩可节省15-95%的代币、智能自动回退、MCP/A2A、多模式API、桌面/PWA。 | https://github.com/diegosouzapw/OmniRoute |  |
| 4 | `Zackriya-Solutions/meetily` | 19401 | 1966 | Rust | 5,769 stars this week | 隐私第一，基于Rust构建的人工智能会议助手，具有4倍的Parakeet/Whisper实时转录、扬声器日记和Ollama摘要。100%本地处理。无需云。Meetily （ Meetly Ai - https://meetily.ai ）是首屈一指的自托管、开源Ai会议...... | https://github.com/Zackriya-Solutions/meetily |  |
| 5 | `altic-dev/FluidVoice` | 6417 | 400 | Swift | 2,127 stars this week | 具有设备上STT和定制训练的人工智能增强模型的最快且唯一的macOS听写应用程序。本地Wispr Flow替代方案。⭐帮助大量:) Windows和iOS等待名单打开。Linux即将推出。 | https://github.com/altic-dev/FluidVoice | 新增 |
| 6 | `ogulcancelik/herdr` | 12873 | 748 | Rust | 4,348 stars this week | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 7 | `xbtlin/ai-berkshire` | 11143 | 1441 | Python | 4,616 stars this week | AI 时代的伯克希尔：基于 Claude Code / Codex 的价值投资研究框架。巴菲特·芒格·段永平·李录四大师方法论 + 多Agent并行研究。· AI-era Berkshire: a value investing research framework built for Claude Code / Codex. 4 masters' methodologies + multi-agent adversarial analysis. | https://github.com/xbtlin/ai-berkshire |  |
| 8 | `alibaba/page-agent` | 24615 | 2107 | TypeScript | 3,989 stars this week | JavaScript页面内GUI代理。使用自然语言控制Web界面。 | https://github.com/alibaba/page-agent |  |
| 9 | `browser-use/video-use` | 15470 | 1808 | Python | 3,706 stars this week | 使用编码代理编辑视频 | https://github.com/browser-use/video-use |  |
| 10 | `Robbyant/lingbot-map` | 10065 | 997 | Python | 1,525 stars this week | 用于从流数据重建场景的前馈3D基础模型 | https://github.com/Robbyant/lingbot-map |  |
| 11 | `huggingface/speech-to-speech` | 5480 | 671 | Python | 533 stars this week | 使用开源模型构建本地语音代理 | https://github.com/huggingface/speech-to-speech | 新增 |
| 12 | `allenai/olmocr` | 18891 | 1549 | Python | 1,243 stars this week | 用于线性化LLM数据集/培训的PDF的工具包 | https://github.com/allenai/olmocr |  |
| 13 | `openai/codex-plugin-cc` | 26283 | 1573 | JavaScript | 4,329 stars this week | 使用Claude Code的Codex来查看代码或委派任务。 | https://github.com/openai/codex-plugin-cc |  |
| 14 | `Starmel/OpenSuperWhisper` | 1889 | 157 | Swift | 530 stars this week | macOS听写应用 | https://github.com/Starmel/OpenSuperWhisper |  |
| 15 | `immich-app/immich` | 106518 | 6086 | TypeScript | 1,848 stars this week | 高性能自托管照片和视频管理解决方案。 | https://github.com/immich-app/immich | 新增 |
| 16 | `msitarzewski/agency-agents` | 128153 | 20814 | Shell | 9,706 stars this week | 一个完整的人工智能机构，触手可及--从前端向导到Reddit社区忍者，从奇思妙想的注入者到现实检查者。每位客服代表都是具有个性、流程和经过验证的交付成果的专家。 | https://github.com/msitarzewski/agency-agents |  |
| 17 | `JuliusBrussee/caveman` | 85708 | 4773 | JavaScript | 7,780 stars this week | 🪨 为什么在很少令牌欺骗时使用许多令牌— Claude Code技能通过像穴居人一样说话来削减65 ％的令牌 | https://github.com/JuliusBrussee/caveman | 新增 |
| 18 | `DeusData/codebase-memory-mcp` | 27393 | 2038 | C | 6,309 stars this week | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 19 | `stablyai/orca` | 12869 | 873 | TypeScript | 3,794 stars this week | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 20 | `ChromeDevTools/chrome-devtools-mcp` | 46093 | 3000 | TypeScript | 1,394 stars this week | 适用于编码代理的Chrome开发者工具 | https://github.com/ChromeDevTools/chrome-devtools-mcp | 新增 |
| 21 | `JCodesMore/ai-website-cloner-template` | 26238 | 3698 | TypeScript | 2,825 stars this week | 使用AI编码代理，只需一个命令即可克隆任何网站 | https://github.com/JCodesMore/ai-website-cloner-template |  |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `apple/container` | 46806 | 1406 | Swift | 20,137 stars this month | 用于在Mac上使用轻量级虚拟机创建和运行Linux容器的工具。它是用Swift编写的，并针对Apple芯片进行了优化。 | https://github.com/apple/container |  |
| 2 | `DeusData/codebase-memory-mcp` | 27394 | 2038 | C | 24,223 stars this month | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 3 | `calesthio/OpenMontage` | 34346 | 3929 | Python | 29,796 stars this month | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 4 | `NVIDIA/SkillSpector` | 12151 | 1002 | Python | 10,867 stars this month | 人工智能代理技能的安全扫描仪。检测漏洞、恶意模式和安全风险。 | https://github.com/NVIDIA/SkillSpector | 新增 |
| 5 | `Panniantong/Agent-Reach` | 52044 | 4183 | Python | 30,168 stars this month | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 6 | `iptv-org/iptv` | 130770 | 7275 | TypeScript | 14,204 stars this month | 收集来自世界各地的公开IPTV频道 | https://github.com/iptv-org/iptv |  |
| 7 | `mvanhorn/last30days-skill` | 49760 | 4145 | Python | 21,391 stars this month | 人工智能代理技能，研究Reddit、X、YouTube、HN、Polymarket和网络上的任何主题，然后合成基础摘要 | https://github.com/mvanhorn/last30days-skill |  |
| 8 | `simplex-chat/simplex-chat` | 18005 | 1061 | Haskell | 6,897 stars this month | SimpleX -第一个没有任何类型用户标识符的消息传递网络-设计为100 ％私有！ iOS ， Android和桌面应用程序📱！ | https://github.com/simplex-chat/simplex-chat | 新增 |
| 9 | `asgeirtj/system_prompts_leaks` | 51543 | 8398 | JavaScript | 9,636 stars this month | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT 5.5 Thinking ， GPT 5.5 Instant ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 10 | `interviewstreet/hiring-agent` | 4967 | 932 | Python | 4,089 stars this month | 用于评估和评分简历的AI代理。 | https://github.com/interviewstreet/hiring-agent |  |
| 11 | `usestrix/strix` | 37988 | 3860 | Python | 12,018 stars this month | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 12 | `phuryn/pm-skills` | 22777 | 2290 | — | 10,741 stars this month | PM Skills Marketplace ： 100多种代理技能、命令和插件—从发现到战略、执行、发布和增长。 | https://github.com/phuryn/pm-skills |  |
| 13 | `ogulcancelik/herdr` | 12873 | 748 | Rust | 7,878 stars this month | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 14 | `stablyai/orca` | 12869 | 873 | TypeScript | 8,457 stars this month | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 15 | `alibaba/zvec` | 13508 | 823 | C++ | 3,459 stars this month | 轻量级、快如闪电的进程内矢量数据库 | https://github.com/alibaba/zvec | 新增 |
| 16 | `kenn-io/agentsview` | 3988 | 305 | Go | 2,701 stars this month | 编码代理的本地首次会话搜索、分析、见解和令牌使用统计信息，支持Claude Code、Codex和其他20多个代理。 | https://github.com/kenn-io/agentsview |  |
| 17 | `n0-computer/iroh` | 11169 | 515 | Rust | 2,504 stars this month | IP地址中断，改为拨号键。将QUIC + NAT遍历添加到您的应用程序的库。 | https://github.com/n0-computer/iroh |  |
| 18 | `t8y2/dbx` | 8920 | 754 | Rust | 4,953 stars this month | 20MB, lightweight, cross-platform database client. Supports MySQL, PostgreSQL, SQLite, Redis, MongoDB, DuckDB, ClickHouse, SQL Server and more.20MB，轻量级跨平台数据库客户端、数据库管理工具。支持 MySQL、PostgreSQL、SQLite、Redis、MongoDB、DuckDB、ClickHouse、SQL Server 等。 | https://github.com/t8y2/dbx |  |
| 19 | `roboflow/supervision` | 46978 | 4185 | Python | 6,991 stars this month | 我们为您编写可重复使用的计算机视觉工具。 💜 | https://github.com/roboflow/supervision |  |


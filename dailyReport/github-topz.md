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

**最近一次更新时间**（Asia/Shanghai）： 2026-07-13 09:15:32

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 524581 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 484339 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 451658 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 449394 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 391800 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 382707 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode | 新增 |
| 8 | `nilbuild/developer-roadmap` | 360634 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 9 | `donnemartin/system-design-primer` | 357307 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 10 | `jwasham/coding-interview-university` | 356031 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 11 | `vinta/awesome-python` | 307417 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
| 12 | `awesome-selfhosted/awesome-selfhosted` | 303934 | 可自行部署的各类自由软件网络服务与 Web 应用清单。 | https://github.com/awesome-selfhosted/awesome-selfhosted |  |
| 13 | `996icu/996.ICU` | 276361 | 倡议关注「996」工作制、计数星标与交流的开发社区仓库（含网络迷因用语）。 | https://github.com/996icu/996.ICU |  |
| 14 | `practical-tutorials/project-based-learning` | 272563 | 基于项目的教程精选列表 | https://github.com/practical-tutorials/project-based-learning |  |
| 15 | `obra/superpowers` | 246876 | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers |  |
| 16 | `react/react` | 246311 | 用于Web和本机用户界面的库。 | https://github.com/react/react |  |
| 17 | `facebook/react` | 245279 | 用于构建 Web 与原生用户界面的 React 视图库（含多端生态）。 | https://github.com/facebook/react |  |
| 18 | `torvalds/linux` | 238531 | Linux内核源树 | https://github.com/torvalds/linux |  |
| 19 | `vuejs/vue` | 209989 | 这是Vue 2的存储库。如需了解VUE 3 ，请访问https://github.com/vuejs/core | https://github.com/vuejs/vue |  |
| 20 | `n8n-io/n8n` | 195721 | 具有原生AI功能的公平代码工作流程自动化平台。将视觉构建与自定义代码、自托管或云、400多个集成相结合。 | https://github.com/n8n-io/n8n |  |
| 21 | `microsoft/vscode` | 187216 | Visual Studio Code | https://github.com/microsoft/vscode |  |

---
## Trending 页面快照（HTML 抓取）

**说明**：与上方「全局 Star Search」数据源不同；本段按 GitHub trending 页的 **daily / weekly / monthly** 各拉一页并解析。**若前端改版导致选择器失效，需更新解析逻辑。**

- **标记**列：三个 `since` 子表**各自独立**对照本次拉取前文件中该小节表格已出现的 `owner/repo`；新出现的行标 **新增**。下次拉取会先清空上一轮「新增」再重算（只保留相对**上一版文件**的新仓库）。

### 今日 trending（since=daily）

**页面**： `https://github.com/trending?since=daily`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `Dicklesworthstone/destructive_command_guard` | 2916 | 108 | Rust | 444 stars today | 破坏性命令防护(dcg)用于阻止代理执行危险的git和shell命令。 | https://github.com/Dicklesworthstone/destructive_command_guard | 新增 |
| 2 | `wonderwhy-er/DesktopCommanderMCP` | 7992 | 985 | TypeScript | 210 stars today | 这是Claude的MCP服务器，具有终端控制、文件系统搜索和diff文件编辑功能 | https://github.com/wonderwhy-er/DesktopCommanderMCP |  |
| 3 | `HKUDS/Vibe-Trading` | 20563 | 3601 | Python | 768 stars today | “Vibe-Trading ：您的个人交易代理” | https://github.com/HKUDS/Vibe-Trading | 新增 |
| 4 | `PrefectHQ/prefect` | 23147 | 2391 | Python | 66 stars today | Prefect是一个工作流编排框架，用于在Python中构建弹性数据管道。 | https://github.com/PrefectHQ/prefect | 新增 |
| 5 | `Shubhamsaboo/awesome-llm-apps` | 118556 | 17632 | Python | 408 stars today | 100多个AI Agent和RAG应用程序，您可以实际运行—克隆、自定义、发货。 | https://github.com/Shubhamsaboo/awesome-llm-apps | 新增 |
| 6 | `anthropics/claude-cookbooks` | 48415 | 5731 | Jupyter Notebook | 459 stars today | 一系列笔记本/食谱，展示了一些有趣而有效的使用Claude的方法。 | https://github.com/anthropics/claude-cookbooks | 新增 |
| 7 | `home-assistant/core` | 89069 | 38084 | Python | 400 stars today | 🏡 开源家庭自动化，将本地控制和隐私放在首位。 | https://github.com/home-assistant/core | 新增 |
| 8 | `Crosstalk-Solutions/project-nomad` | 33808 | 3391 | TypeScript | 125 stars today | Project N.O.M.A.D是一款独立的离线生存计算机，配备了关键工具、知识和人工智能，可随时随地让您随时了解情况并获得授权。 | https://github.com/Crosstalk-Solutions/project-nomad | 新增 |
| 9 | `ColeMurray/background-agents` | 2262 | 342 | TypeScript | 16 stars today | 开源后台代理编码系统 | https://github.com/ColeMurray/background-agents | 新增 |
| 10 | `k1tbyte/Wand-Enhancer` | 6958 | 19512 | C# | 609 stars today | Wand (WeMod)应用程序的高级用户体验和互操作性扩展 | https://github.com/k1tbyte/Wand-Enhancer | 新增 |
| 11 | `pingdotgg/t3code` | 13748 | 2891 | TypeScript | 75 stars today | — | https://github.com/pingdotgg/t3code | 新增 |
| 12 | `virattt/ai-hedge-fund` | 61405 | 10858 | Python | 115 stars today | 人工智能对冲基金团队 | https://github.com/virattt/ai-hedge-fund | 新增 |
| 13 | `chen08209/FlClash` | 45223 | 2854 | Dart | 154 stars today | 基于ClashMeta的多平台代理客户端，简单易用，开源且无广告。 | https://github.com/chen08209/FlClash | 新增 |
| 14 | `davila7/claude-code-templates` | 29240 | 3204 | Python | 274 stars today | 用于配置和监控Claude Code的CLI工具 | https://github.com/davila7/claude-code-templates |  |
| 15 | `par274/sharpemu` | 1265 | 76 | C# | 314 stars today | 一个实验性的PlayStation 5模拟器项目。 | https://github.com/par274/sharpemu | 新增 |
| 16 | `malisper/pgrust` | 2472 | 67 | Rust | 518 stars today | 在Rust中重写的Postgres ，现在通过了100%的Postgres回归测试 | https://github.com/malisper/pgrust | 新增 |
| 17 | `Nutlope/hallmark` | 4285 | 253 | CSS | 155 stars today | Claude Code、Cursor和Codex的防AI倾斜设计技能。 | https://github.com/Nutlope/hallmark | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `Zackriya-Solutions/meetily` | 23589 | 2486 | Rust | 7,440 stars this week | 隐私第一，基于Rust构建的人工智能会议助手，具有4倍的Parakeet/Whisper实时转录、扬声器日记和Ollama摘要。100%本地处理。无需云。Meetily （ Meetly Ai - https://meetily.ai ）是首屈一指的自托管、开源Ai会议...... | https://github.com/Zackriya-Solutions/meetily |  |
| 2 | `wonderwhy-er/DesktopCommanderMCP` | 7992 | 985 | TypeScript | 1,678 stars this week | 这是Claude的MCP服务器，具有终端控制、文件系统搜索和diff文件编辑功能 | https://github.com/wonderwhy-er/DesktopCommanderMCP |  |
| 3 | `openai/codex-plugin-cc` | 28063 | 1836 | JavaScript | 2,803 stars this week | 使用Claude Code的Codex来查看代码或委派任务。 | https://github.com/openai/codex-plugin-cc |  |
| 4 | `TencentCloud/CubeSandbox` | 9808 | 964 | Rust | 2,490 stars this week | 适用于人工智能代理的即时、并发、安全和轻量级沙盒。 | https://github.com/TencentCloud/CubeSandbox |  |
| 5 | `abseil/abseil-cpp` | 17946 | 3217 | C++ | 600 stars this week | Abseil通用库（ C + + ） | https://github.com/abseil/abseil-cpp | 新增 |
| 6 | `ogulcancelik/herdr` | 15795 | 1060 | Rust | 3,928 stars this week | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 7 | `asgeirtj/system_prompts_leaks` | 56736 | 9379 | JavaScript | 7,155 stars this week | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT GPT-5.6、Codex GPT-5.6、GPT-5.5。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 8 | `diegosouzapw/OmniRoute` | 16232 | 2477 | TypeScript | 4,506 stars this week | 永不停止编码。免费AI网关：一个端点， 231多家提供商（ 50多家免费） ，将Claude Code、Codex、Cursor、Cline和Copilot连接到免费的Claude/GPT/Gemini。RTK + Caveman堆叠压缩可节省15-95%的代币、智能自动回退、MCP/A2A、多模式API、桌面/PWA。 | https://github.com/diegosouzapw/OmniRoute |  |
| 9 | `stablyai/orca` | 17018 | 1336 | TypeScript | 4,481 stars this week | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 10 | `bradautomates/claude-video` | 7838 | 876 | Python | 4,353 stars this week | 让Claude能够观看任何视频。/观看下载、提取帧、转录，并将所有内容交给Claude。 | https://github.com/bradautomates/claude-video |  |
| 11 | `facebook/astryx` | 8190 | 691 | TypeScript | 2,397 stars this week | 完全可定制和代理就绪的开源设计系统 | https://github.com/facebook/astryx |  |
| 12 | `iOfficeAI/OfficeCLI` | 15436 | 1053 | C# | 6,978 stars this week | OfficeCLI是第一个也是最好的Office套件，专为AI代理读取、编辑和自动化Word、Excel和PowerPoint文件而构建。免费、开源、单一二进制文件，无需安装Office。 | https://github.com/iOfficeAI/OfficeCLI |  |
| 13 | `usestrix/strix` | 40860 | 4313 | Python | 4,143 stars this week | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 14 | `tt-a1i/archify` | 3921 | 379 | JavaScript | 1,180 stars this week | 任何代理技能：使用暗/亮主题切换和PNG/JPEG/WebP/SVG导出生成漂亮的架构图 | https://github.com/tt-a1i/archify |  |
| 15 | `alibaba/page-agent` | 26224 | 2415 | TypeScript | 2,666 stars this week | JavaScript页面内GUI代理。使用自然语言控制Web界面。 | https://github.com/alibaba/page-agent |  |
| 16 | `alirezarezvani/claude-skills` | 22384 | 3120 | Python | 1,993 stars this week | 345 Claude Code技能和代理技能和插件（ 30多个代理、70多个自定义命令、330多个技能、可定制的参考、脚本） ，适用于Claude Code、Codex、Gemini CLI、Cursor和其他8个编码代理—工程、营销、产品、合规、C级咨询、研究…… | https://github.com/alirezarezvani/claude-skills |  |
| 17 | `ChromeDevTools/chrome-devtools-mcp` | 46770 | 3202 | TypeScript | 872 stars this week | 适用于编码代理的Chrome开发者工具 | https://github.com/ChromeDevTools/chrome-devtools-mcp | 新增 |
| 18 | `vxcontrol/pentagi` | 20175 | 2685 | Go | 1,989 stars this week | 完全自主的AI Agents系统，能够执行复杂的渗透测试任务 | https://github.com/vxcontrol/pentagi | 新增 |
| 19 | `ruvnet/RuView` | 80258 | 10811 | Rust | 3,763 stars this week | π RuView将商用WiFi信号转化为实时空间智能、生命体征监测和存在检测--所有这些都无需一个像素的视频。 | https://github.com/ruvnet/RuView |  |
| 20 | `JuliusBrussee/caveman` | 88547 | 5089 | JavaScript | 3,992 stars this week | 🪨 为什么在很少令牌欺骗时使用许多令牌— Claude Code技能通过像穴居人一样说话来削减65 ％的令牌 | https://github.com/JuliusBrussee/caveman |  |
| 21 | `pbakaus/impeccable` | 45984 | 2785 | JavaScript | 2,272 stars this week | 让您的人工智能更好地进行设计的设计语言。 | https://github.com/pbakaus/impeccable | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `DeusData/codebase-memory-mcp` | 30627 | 2451 | C | 27,178 stars this month | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 2 | `calesthio/OpenMontage` | 37534 | 4533 | Python | 32,911 stars this month | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 3 | `Panniantong/Agent-Reach` | 55333 | 4564 | Python | 28,973 stars this month | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 4 | `asgeirtj/system_prompts_leaks` | 56736 | 9379 | JavaScript | 14,973 stars this month | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT GPT-5.6、Codex GPT-5.6、GPT-5.5。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 5 | `kunchenguid/no-mistakes` | 6025 | 536 | Go | 4,726 stars this month | git push no-mistakes | https://github.com/kunchenguid/no-mistakes |  |
| 6 | `usestrix/strix` | 40860 | 4313 | Python | 14,993 stars this month | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 7 | `ogulcancelik/herdr` | 15796 | 1060 | Rust | 10,286 stars this month | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 8 | `stablyai/orca` | 17018 | 1336 | TypeScript | 12,079 stars this month | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 9 | `Zackriya-Solutions/meetily` | 23589 | 2486 | Rust | 10,839 stars this month | 隐私第一，基于Rust构建的人工智能会议助手，具有4倍的Parakeet/Whisper实时转录、扬声器日记和Ollama摘要。100%本地处理。无需云。Meetily （ Meetly Ai - https://meetily.ai ）是首屈一指的自托管、开源Ai会议...... | https://github.com/Zackriya-Solutions/meetily |  |
| 10 | `interviewstreet/hiring-agent` | 5650 | 1134 | Python | 4,540 stars this month | 用于评估和评分简历的AI代理。 | https://github.com/interviewstreet/hiring-agent |  |
| 11 | `alibaba/zvec` | 14813 | 921 | C++ | 5,073 stars this month | 轻量级、快如闪电的进程内矢量数据库 | https://github.com/alibaba/zvec | 新增 |
| 12 | `diegosouzapw/OmniRoute` | 16232 | 2477 | TypeScript | 10,055 stars this month | 永不停止编码。免费AI网关：一个端点， 231多家提供商（ 50多家免费） ，将Claude Code、Codex、Cursor、Cline和Copilot连接到免费的Claude/GPT/Gemini。RTK + Caveman堆叠压缩可节省15-95%的代币、智能自动回退、MCP/A2A、多模式API、桌面/PWA。 | https://github.com/diegosouzapw/OmniRoute |  |
| 13 | `alibaba/page-agent` | 26224 | 2415 | TypeScript | 7,797 stars this month | JavaScript页面内GUI代理。使用自然语言控制Web界面。 | https://github.com/alibaba/page-agent |  |
| 14 | `simplex-chat/simplex-chat` | 18511 | 1243 | Haskell | 7,392 stars this month | SimpleX -第一个没有任何类型用户标识符的消息传递网络-设计为100 ％私有！ iOS ， Android和桌面应用程序📱！ | https://github.com/simplex-chat/simplex-chat |  |
| 15 | `iptv-org/iptv` | 132623 | 7567 | TypeScript | 15,178 stars this month | 收集来自世界各地的公开IPTV频道 | https://github.com/iptv-org/iptv |  |
| 16 | `gabime/spdlog` | 29176 | 5323 | C++ | 308 stars this month | 快速C + +日志记录库。 | https://github.com/gabime/spdlog | 新增 |
| 17 | `n0-computer/iroh` | 11596 | 680 | Rust | 2,909 stars this month | IP地址中断，改为拨号键。将QUIC + NAT遍历添加到您的应用程序的库。 | https://github.com/n0-computer/iroh |  |
| 18 | `NVIDIA/SkillSpector` | 13017 | 1059 | Python | 9,876 stars this month | 人工智能代理技能的安全扫描仪。检测漏洞、恶意模式和安全风险。 | https://github.com/NVIDIA/SkillSpector |  |
| 19 | `mauriceboe/TREK` | 10188 | 968 | TypeScript | 4,546 stars this month | 自托管行程/行程规划工具，提供实时协作、互动地图、PWA支持、SSO、预算、装箱单等功能。 | https://github.com/mauriceboe/TREK |  |
| 20 | `ocornut/imgui` | 74542 | 12001 | C++ | 843 stars this month | 尊敬的ImGui ：无臃肿的C + +图形用户界面，依赖关系最少 | https://github.com/ocornut/imgui | 新增 |
| 21 | `topoteretes/cognee` | 27650 | 2743 | Python | 9,895 stars this month | Cognee是面向智能体的开源AI内存平台。使用自托管知识图表引擎，为您的人工智能代理提供跨会话的持久长期记忆。 | https://github.com/topoteretes/cognee | 新增 |


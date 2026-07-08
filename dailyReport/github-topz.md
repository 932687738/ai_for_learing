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

**最近一次更新时间**（Asia/Shanghai）： 2026-07-08 09:16:39

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 523318 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 482844 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 451253 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 447682 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 391444 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 382104 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 359618 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 356605 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 355406 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 306878 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `MadsLorentzen/ai-job-search` | 10955 | 3676 | TypeScript | 2,514 stars today | 基于Claude Code构建的人工智能工作申请框架。分叉，填写您的个人资料，让Claude评估工作，定制简历，写求职信，并为面试做好准备。 | https://github.com/MadsLorentzen/ai-job-search | 新增 |
| 2 | `Zackriya-Solutions/meetily` | 20745 | 2078 | Rust | 1,777 stars today | 隐私第一，基于Rust构建的人工智能会议助手，具有4倍的Parakeet/Whisper实时转录、扬声器日记和Ollama摘要。100%本地处理。无需云。Meetily （ Meetly Ai - https://meetily.ai ）是首屈一指的自托管、开源Ai会议...... | https://github.com/Zackriya-Solutions/meetily |  |
| 3 | `addyosmani/agent-skills` | 72162 | 7815 | JavaScript | 1,317 stars today | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 4 | `ruvnet/RuView` | 78519 | 10563 | Rust | 1,129 stars today | π RuView将商用WiFi信号转化为实时空间智能、生命体征监测和存在检测--所有这些都无需一个像素的视频。 | https://github.com/ruvnet/RuView |  |
| 5 | `asgeirtj/system_prompts_leaks` | 53015 | 8642 | JavaScript | 1,691 stars today | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT 5.5 Thinking ， GPT 5.5 Instant ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 6 | `TencentCloud/CubeSandbox` | 8466 | 711 | Rust | 664 stars today | 适用于人工智能代理的即时、并发、安全和轻量级沙盒。 | https://github.com/TencentCloud/CubeSandbox | 新增 |
| 7 | `AhmadIbrahiim/Website-downloader` | 4011 | 987 | HTML | 140 stars today | 💡 下载任何网站（包括所有资产）的完整源代码。[Javascripts, Stylesheets, Images]使用Node.js | https://github.com/AhmadIbrahiim/Website-downloader | 新增 |
| 8 | `steipete/CodexBar` | 17036 | 1388 | Swift | 376 stars today | 显示OpenAI Codex和Claude Code的使用统计信息，无需登录。 | https://github.com/steipete/CodexBar |  |
| 9 | `dotnet/skills` | 4308 | 324 | C# | 64 stars today | 用于使用.NET和C #协助AI编码代理的技能的存储库 | https://github.com/dotnet/skills | 新增 |
| 10 | `iOfficeAI/OfficeCLI` | 9985 | 680 | C# | 893 stars today | OfficeCLI是第一个也是最好的Office套件，专为AI代理读取、编辑和自动化Word、Excel和PowerPoint文件而构建。免费、开源、单一二进制文件，无需安装Office。 | https://github.com/iOfficeAI/OfficeCLI | 新增 |
| 11 | `bradautomates/claude-video` | 5175 | 663 | Python | 965 stars today | 让Claude能够观看任何视频。/观看下载、提取帧、转录，并将所有内容交给Claude。 | https://github.com/bradautomates/claude-video |  |
| 12 | `kyutai-labs/pocket-tts` | 6181 | 646 | Python | 531 stars today | 适合计划工作站（和口袋）的TTS | https://github.com/kyutai-labs/pocket-tts | 新增 |
| 13 | `hesreallyhim/awesome-claude-code` | 49133 | 4281 | Python | 144 stars today | 来自Anthropic PBC不可阻挡团队的编码伙伴无可争议的冠军Claude Code ，为最优秀的代理人精心挑选了最优秀的资源。顶级技能的精彩展示，双手灵巧的代理，闪烁的状态线， t… | https://github.com/hesreallyhim/awesome-claude-code | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `usestrix/strix` | 38576 | 3917 | Python | 10,741 stars this week | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 2 | `Zackriya-Solutions/meetily` | 20745 | 2078 | Rust | 7,349 stars this week | 隐私第一，基于Rust构建的人工智能会议助手，具有4倍的Parakeet/Whisper实时转录、扬声器日记和Ollama摘要。100%本地处理。无需云。Meetily （ Meetly Ai - https://meetily.ai ）是首屈一指的自托管、开源Ai会议...... | https://github.com/Zackriya-Solutions/meetily |  |
| 3 | `hasaneyldrm/exercises-dataset` | 10721 | 1204 | HTML | 4,950 stars this week | 包含433项健身练习的综合数据集。每个条目包括名称、类别、目标肌肉群、设备、说明、缩略图和动画视频。 | https://github.com/hasaneyldrm/exercises-dataset |  |
| 4 | `ogulcancelik/herdr` | 13570 | 788 | Rust | 4,557 stars this week | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 5 | `diegosouzapw/OmniRoute` | 13149 | 1922 | TypeScript | 4,797 stars this week | 永不停止编码。免费AI网关：一个端点， 231多家提供商（ 50多家免费） ，将Claude Code、Codex、Cursor、Cline和Copilot连接到免费的Claude/GPT/Gemini。RTK + Caveman堆叠压缩可节省15-95%的代币、智能自动回退、MCP/A2A、多模式API、桌面/PWA。 | https://github.com/diegosouzapw/OmniRoute |  |
| 6 | `alibaba/page-agent` | 24934 | 2134 | TypeScript | 4,163 stars this week | JavaScript页面内GUI代理。使用自然语言控制Web界面。 | https://github.com/alibaba/page-agent |  |
| 7 | `openai/codex-plugin-cc` | 26628 | 1600 | JavaScript | 4,725 stars this week | 使用Claude Code的Codex来查看代码或委派任务。 | https://github.com/openai/codex-plugin-cc |  |
| 8 | `MadsLorentzen/ai-job-search` | 10957 | 3676 | TypeScript | 5,363 stars this week | 基于Claude Code构建的人工智能工作申请框架。分叉，填写您的个人资料，让Claude评估工作，定制简历，写求职信，并为面试做好准备。 | https://github.com/MadsLorentzen/ai-job-search | 新增 |
| 9 | `altic-dev/FluidVoice` | 6696 | 422 | Swift | 1,865 stars this week | 具有设备上STT和定制训练的人工智能增强模型的最快且唯一的macOS听写应用程序。本地Wispr Flow替代方案。⭐帮助大量:) Windows和iOS等待名单打开。Linux即将推出。 | https://github.com/altic-dev/FluidVoice |  |
| 10 | `TencentCloud/CubeSandbox` | 8466 | 711 | Rust | 1,692 stars this week | 适用于人工智能代理的即时、并发、安全和轻量级沙盒。 | https://github.com/TencentCloud/CubeSandbox | 新增 |
| 11 | `xbtlin/ai-berkshire` | 11698 | 1514 | Python | 4,262 stars this week | AI 时代的伯克希尔：基于 Claude Code / Codex 的价值投资研究框架。巴菲特·芒格·段永平·李录四大师方法论 + 多Agent并行研究。· AI-era Berkshire: a value investing research framework built for Claude Code / Codex. 4 masters' methodologies + multi-agent adversarial analysis. | https://github.com/xbtlin/ai-berkshire |  |
| 12 | `msitarzewski/agency-agents` | 128788 | 20940 | Shell | 8,597 stars this week | 一个完整的人工智能机构，触手可及--从前端向导到Reddit社区忍者，从奇思妙想的注入者到现实检查者。每位客服代表都是具有个性、流程和经过验证的交付成果的专家。 | https://github.com/msitarzewski/agency-agents |  |
| 13 | `immich-app/immich` | 106732 | 6111 | TypeScript | 1,984 stars this week | 高性能自托管照片和视频管理解决方案。 | https://github.com/immich-app/immich |  |
| 14 | `huggingface/speech-to-speech` | 5587 | 677 | Python | 645 stars this week | 使用开源模型构建本地语音代理 | https://github.com/huggingface/speech-to-speech |  |
| 15 | `allenai/olmocr` | 18957 | 1559 | Python | 1,134 stars this week | 用于线性化LLM数据集/培训的PDF的工具包 | https://github.com/allenai/olmocr |  |
| 16 | `browser-use/video-use` | 15892 | 1845 | Python | 3,435 stars this week | 使用编码代理编辑视频 | https://github.com/browser-use/video-use |  |
| 17 | `dotnet/skills` | 4308 | 324 | C# | 687 stars this week | 用于使用.NET和C #协助AI编码代理的技能的存储库 | https://github.com/dotnet/skills | 新增 |
| 18 | `JuliusBrussee/caveman` | 86276 | 4809 | JavaScript | 8,066 stars this week | 🪨 为什么在很少令牌欺骗时使用许多令牌— Claude Code技能通过像穴居人一样说话来削减65 ％的令牌 | https://github.com/JuliusBrussee/caveman |  |
| 19 | `stablyai/orca` | 13554 | 910 | TypeScript | 3,820 stars this week | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 20 | `Robbyant/lingbot-map` | 10201 | 1022 | Python | 1,451 stars this week | 用于从流数据重建场景的前馈3D基础模型 | https://github.com/Robbyant/lingbot-map |  |
| 21 | `asgeirtj/system_prompts_leaks` | 53015 | 8642 | JavaScript | 5,337 stars this week | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT 5.5 Thinking ， GPT 5.5 Instant ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks | 新增 |
| 22 | `ChromeDevTools/chrome-devtools-mcp` | 46251 | 3018 | TypeScript | 1,480 stars this week | 适用于编码代理的Chrome开发者工具 | https://github.com/ChromeDevTools/chrome-devtools-mcp |  |
| 23 | `DeusData/codebase-memory-mcp` | 28017 | 2084 | C | 5,457 stars this week | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `apple/container` | 46998 | 1420 | Swift | 20,326 stars this month | 用于在Mac上使用轻量级虚拟机创建和运行Linux容器的工具。它是用Swift编写的，并针对Apple芯片进行了优化。 | https://github.com/apple/container |  |
| 2 | `DeusData/codebase-memory-mcp` | 28017 | 2084 | C | 24,857 stars this month | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 3 | `calesthio/OpenMontage` | 35036 | 4031 | Python | 30,474 stars this month | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 4 | `NVIDIA/SkillSpector` | 12320 | 1016 | Python | 10,999 stars this month | 人工智能代理技能的安全扫描仪。检测漏洞、恶意模式和安全风险。 | https://github.com/NVIDIA/SkillSpector |  |
| 5 | `Panniantong/Agent-Reach` | 52707 | 4240 | Python | 29,851 stars this month | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 6 | `iptv-org/iptv` | 131011 | 7294 | TypeScript | 14,047 stars this month | 收集来自世界各地的公开IPTV频道 | https://github.com/iptv-org/iptv |  |
| 7 | `asgeirtj/system_prompts_leaks` | 53015 | 8642 | JavaScript | 11,323 stars this month | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT 5.5 Thinking ， GPT 5.5 Instant ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 8 | `simplex-chat/simplex-chat` | 18080 | 1070 | Haskell | 6,973 stars this month | SimpleX -第一个没有任何类型用户标识符的消息传递网络-设计为100 ％私有！ iOS ， Android和桌面应用程序📱！ | https://github.com/simplex-chat/simplex-chat |  |
| 9 | `usestrix/strix` | 38576 | 3917 | Python | 12,644 stars this month | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 10 | `ogulcancelik/herdr` | 13571 | 788 | Rust | 8,492 stars this month | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 11 | `interviewstreet/hiring-agent` | 5095 | 949 | Python | 4,098 stars this month | 用于评估和评分简历的AI代理。 | https://github.com/interviewstreet/hiring-agent |  |
| 12 | `alibaba/zvec` | 14042 | 854 | C++ | 4,145 stars this month | 轻量级、快如闪电的进程内矢量数据库 | https://github.com/alibaba/zvec |  |
| 13 | `stablyai/orca` | 13554 | 910 | TypeScript | 8,947 stars this month | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 14 | `phuryn/pm-skills` | 22920 | 2309 | — | 10,794 stars this month | PM Skills Marketplace ： 100多种代理技能、命令和插件—从发现到战略、执行、发布和增长。 | https://github.com/phuryn/pm-skills |  |
| 15 | `mvanhorn/last30days-skill` | 50330 | 4198 | Python | 20,890 stars this month | 人工智能代理技能，研究Reddit、X、YouTube、HN、Polymarket和网络上的任何主题，然后合成基础摘要 | https://github.com/mvanhorn/last30days-skill |  |
| 16 | `Zackriya-Solutions/meetily` | 20746 | 2078 | Rust | 7,651 stars this month | 隐私第一，基于Rust构建的人工智能会议助手，具有4倍的Parakeet/Whisper实时转录、扬声器日记和Ollama摘要。100%本地处理。无需云。Meetily （ Meetly Ai - https://meetily.ai ）是首屈一指的自托管、开源Ai会议...... | https://github.com/Zackriya-Solutions/meetily | 新增 |
| 17 | `n0-computer/iroh` | 11218 | 517 | Rust | 2,542 stars this month | IP地址中断，改为拨号键。将QUIC + NAT遍历添加到您的应用程序的库。 | https://github.com/n0-computer/iroh |  |
| 18 | `MadsLorentzen/ai-job-search` | 10957 | 3676 | TypeScript | 5,887 stars this month | 基于Claude Code构建的人工智能工作申请框架。分叉，填写您的个人资料，让Claude评估工作，定制简历，写求职信，并为面试做好准备。 | https://github.com/MadsLorentzen/ai-job-search | 新增 |
| 19 | `alibaba/page-agent` | 24934 | 2134 | TypeScript | 6,603 stars this month | JavaScript页面内GUI代理。使用自然语言控制Web界面。 | https://github.com/alibaba/page-agent | 新增 |
| 20 | `t8y2/dbx` | 9099 | 774 | Rust | 5,048 stars this month | 20MB, lightweight, cross-platform database client. Supports MySQL, PostgreSQL, SQLite, Redis, MongoDB, DuckDB, ClickHouse, SQL Server and more.20MB，轻量级跨平台数据库客户端、数据库管理工具。支持 MySQL、PostgreSQL、SQLite、Redis、MongoDB、DuckDB、ClickHouse、SQL Server 等。 | https://github.com/t8y2/dbx |  |
| 21 | `ZhuLinsen/daily_stock_analysis` | 55551 | 47948 | Python | 14,631 stars this month | LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。 LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs. | https://github.com/ZhuLinsen/daily_stock_analysis | 新增 |


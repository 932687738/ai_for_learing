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

**最近一次更新时间**（Asia/Shanghai）： 2026-07-11 06:39:09

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 524093 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 483708 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 451518 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 448641 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 391608 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 382506 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 360293 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 356990 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 355801 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 307417 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
| 11 | `awesome-selfhosted/awesome-selfhosted` | 303934 | 可自行部署的各类自由软件网络服务与 Web 应用清单。 | https://github.com/awesome-selfhosted/awesome-selfhosted |  |
| 12 | `996icu/996.ICU` | 276361 | 倡议关注「996」工作制、计数星标与交流的开发社区仓库（含网络迷因用语）。 | https://github.com/996icu/996.ICU |  |
| 13 | `practical-tutorials/project-based-learning` | 272563 | 基于项目的教程精选列表 | https://github.com/practical-tutorials/project-based-learning |  |
| 14 | `obra/superpowers` | 246876 | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers |  |
| 15 | `react/react` | 246311 | 用于Web和本机用户界面的库。 | https://github.com/react/react |  |
| 16 | `facebook/react` | 245279 | 用于构建 Web 与原生用户界面的 React 视图库（含多端生态）。 | https://github.com/facebook/react |  |
| 17 | `torvalds/linux` | 238531 | Linux内核源树 | https://github.com/torvalds/linux |  |
| 18 | `vuejs/vue` | 209989 | 这是Vue 2的存储库。如需了解VUE 3 ，请访问https://github.com/vuejs/core | https://github.com/vuejs/vue |  |
| 19 | `n8n-io/n8n` | 195721 | 具有原生AI功能的公平代码工作流程自动化平台。将视觉构建与自定义代码、自托管或云、400多个集成相结合。 | https://github.com/n8n-io/n8n |  |
| 20 | `microsoft/vscode` | 187216 | Visual Studio Code | https://github.com/microsoft/vscode |  |

---
## Trending 页面快照（HTML 抓取）

**说明**：与上方「全局 Star Search」数据源不同；本段按 GitHub trending 页的 **daily / weekly / monthly** 各拉一页并解析。**若前端改版导致选择器失效，需更新解析逻辑。**

- **标记**列：三个 `since` 子表**各自独立**对照本次拉取前文件中该小节表格已出现的 `owner/repo`；新出现的行标 **新增**。下次拉取会先清空上一轮「新增」再重算（只保留相对**上一版文件**的新仓库）。

### 今日 trending（since=daily）

**页面**： `https://github.com/trending?since=daily`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `wonderwhy-er/DesktopCommanderMCP` | 7238 | 921 | TypeScript | 349 stars today | 这是Claude的MCP服务器，具有终端控制、文件系统搜索和diff文件编辑功能 | https://github.com/wonderwhy-er/DesktopCommanderMCP |  |
| 2 | `oven-sh/bun` | 94178 | 4938 | Rust | 307 stars today | 令人难以置信的快速JavaScript运行时、捆绑程序、测试运行程序和包管理器–所有功能于一身 | https://github.com/oven-sh/bun | 新增 |
| 3 | `abseil/abseil-cpp` | 17506 | 3193 | C++ | 106 stars today | Abseil通用库（ C + + ） | https://github.com/abseil/abseil-cpp | 新增 |
| 4 | `addyosmani/agent-skills` | 76773 | 8245 | JavaScript | 1,114 stars today | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 5 | `jbeder/yaml-cpp` | 6072 | 2255 | C++ | 65 stars today | C + +中的YAML解析器和发射器 | https://github.com/jbeder/yaml-cpp | 新增 |
| 6 | `mattpocock/skills` | 164539 | 14157 | Shell | 1,663 stars today | 真正工程师的技能。直接来自我的.claude目录。 | https://github.com/mattpocock/skills | 新增 |
| 7 | `obra/superpowers` | 251746 | 22462 | Shell | 969 stars today | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers | 新增 |
| 8 | `microsoft/TypeScript` | 109760 | 13631 | TypeScript | 166 stars today | TypeScript是JavaScript的超集，可编译以清除JavaScript输出。 | https://github.com/microsoft/TypeScript | 新增 |
| 9 | `catchorg/Catch2` | 20605 | 3406 | C++ | 69 stars today | 用于单元测试、TDD和BDD的现代C + +原生测试框架-使用C + +14、C + +17及更高版本（ C + +11支持v2.x分支， C + +03支持Catch1.x分支） | https://github.com/catchorg/Catch2 | 新增 |
| 10 | `chriskohlhoff/asio` | 6064 | 1499 | C++ | 87 stars today | Asio C + +库 | https://github.com/chriskohlhoff/asio | 新增 |
| 11 | `TencentCloud/TencentDB-Agent-Memory` | 8204 | 754 | TypeScript | 134 stars today | TencentDB Agent Memory通过4层渐进式管道为AI Agent提供完全本地化的长期内存，无外部API依赖。 | https://github.com/TencentCloud/TencentDB-Agent-Memory | 新增 |
| 12 | `davila7/claude-code-templates` | 28749 | 3160 | Python | 104 stars today | 用于配置和监控Claude Code的CLI工具 | https://github.com/davila7/claude-code-templates | 新增 |
| 13 | `zeux/meshoptimizer` | 8014 | 782 | C++ | 86 stars today | 网格优化库，使网格更小，渲染速度更快 | https://github.com/zeux/meshoptimizer | 新增 |
| 14 | `tailscale/tailscale` | 33618 | 2909 | Go | 183 stars today | 使用WireGuard和2FA最简单、最安全的方式。 | https://github.com/tailscale/tailscale | 新增 |
| 15 | `google-labs-code/stitch-skills` | 6712 | 927 | TypeScript | 101 stars today | 专为与Stitch MCP服务器配合使用而设计的代理技能库。每项技能都遵循Agent Skills开放标准，与Antigravity、Gemini CLI、Claude Code、Cursor等编码代理兼容。 | https://github.com/google-labs-code/stitch-skills | 新增 |
| 16 | `iOfficeAI/OfficeCLI` | 14386 | 974 | C# | 1,210 stars today | OfficeCLI是第一个也是最好的Office套件，专为AI代理读取、编辑和自动化Word、Excel和PowerPoint文件而构建。免费、开源、单一二进制文件，无需安装Office。 | https://github.com/iOfficeAI/OfficeCLI |  |
| 17 | `hashicorp/terraform` | 49144 | 10672 | Go | 168 stars today | Terraform使您能够安全、可预测地创建、更改和改进基础设施。它是一个源代码可用的工具，将API编码为声明性配置文件，可以在团队成员之间共享，被视为代码，编辑，审查和版本控制。 | https://github.com/hashicorp/terraform | 新增 |
| 18 | `grpc/grpc` | 45127 | 11319 | C++ | 68 stars today | 基于C + +的gRPC （ C + +、Python、Ruby、Objective-C、PHP、C # ） | https://github.com/grpc/grpc | 新增 |
| 19 | `vercel/next.js` | 140678 | 31522 | JavaScript | 176 stars today | React框架 | https://github.com/vercel/next.js | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `Zackriya-Solutions/meetily` | 22643 | 2382 | Rust | 8,885 stars this week | 隐私第一，基于Rust构建的人工智能会议助手，具有4倍的Parakeet/Whisper实时转录、扬声器日记和Ollama摘要。100%本地处理。无需云。Meetily （ Meetly Ai - https://meetily.ai ）是首屈一指的自托管、开源Ai会议...... | https://github.com/Zackriya-Solutions/meetily |  |
| 2 | `asgeirtj/system_prompts_leaks` | 55800 | 9200 | JavaScript | 7,149 stars this week | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT GPT-5.6、Codex GPT-5.6、GPT-5.5。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 3 | `usestrix/strix` | 40110 | 4205 | Python | 8,370 stars this week | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 4 | `openai/codex-plugin-cc` | 27419 | 1775 | JavaScript | 4,792 stars this week | 使用Claude Code的Codex来查看代码或委派任务。 | https://github.com/openai/codex-plugin-cc |  |
| 5 | `ogulcancelik/herdr` | 15197 | 1006 | Rust | 4,756 stars this week | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 6 | `bradautomates/claude-video` | 7164 | 799 | Python | 3,630 stars this week | 让Claude能够观看任何视频。/观看下载、提取帧、转录，并将所有内容交给Claude。 | https://github.com/bradautomates/claude-video |  |
| 7 | `facebook/astryx` | 7723 | 643 | TypeScript | 4,087 stars this week | 完全可定制和代理就绪的开源设计系统 | https://github.com/facebook/astryx |  |
| 8 | `alibaba/page-agent` | 25810 | 2372 | TypeScript | 4,459 stars this week | JavaScript页面内GUI代理。使用自然语言控制Web界面。 | https://github.com/alibaba/page-agent |  |
| 9 | `TencentCloud/CubeSandbox` | 9578 | 937 | Rust | 2,284 stars this week | 适用于人工智能代理的即时、并发、安全和轻量级沙盒。 | https://github.com/TencentCloud/CubeSandbox |  |
| 10 | `diegosouzapw/OmniRoute` | 15017 | 2297 | TypeScript | 4,119 stars this week | 永不停止编码。免费AI网关：一个端点， 231多家提供商（ 50多家免费） ，将Claude Code、Codex、Cursor、Cline和Copilot连接到免费的Claude/GPT/Gemini。RTK + Caveman堆叠压缩可节省15-95%的代币、智能自动回退、MCP/A2A、多模式API、桌面/PWA。 | https://github.com/diegosouzapw/OmniRoute |  |
| 11 | `stablyai/orca` | 15915 | 1241 | TypeScript | 4,111 stars this week | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 12 | `huggingface/speech-to-speech` | 5996 | 839 | Python | 788 stars this week | 使用开源模型构建本地语音代理 | https://github.com/huggingface/speech-to-speech |  |
| 13 | `ruvnet/RuView` | 79872 | 10750 | Rust | 3,537 stars this week | π RuView将商用WiFi信号转化为实时空间智能、生命体征监测和存在检测--所有这些都无需一个像素的视频。 | https://github.com/ruvnet/RuView |  |
| 14 | `tt-a1i/archify` | 3429 | 357 | JavaScript | 1,013 stars this week | 任何代理技能：使用暗/亮主题切换和PNG/JPEG/WebP/SVG导出生成漂亮的架构图 | https://github.com/tt-a1i/archify | 新增 |
| 15 | `iOfficeAI/OfficeCLI` | 14386 | 974 | C# | 4,872 stars this week | OfficeCLI是第一个也是最好的Office套件，专为AI代理读取、编辑和自动化Word、Excel和PowerPoint文件而构建。免费、开源、单一二进制文件，无需安装Office。 | https://github.com/iOfficeAI/OfficeCLI | 新增 |
| 16 | `xbtlin/ai-berkshire` | 12633 | 1787 | Python | 3,757 stars this week | AI 时代的伯克希尔：基于 Claude Code / Codex 的价值投资研究框架。巴菲特·芒格·段永平·李录四大师方法论 + 多Agent并行研究。· AI-era Berkshire: a value investing research framework built for Claude Code / Codex. 4 masters' methodologies + multi-agent adversarial analysis. | https://github.com/xbtlin/ai-berkshire |  |
| 17 | `wonderwhy-er/DesktopCommanderMCP` | 7238 | 921 | TypeScript | 297 stars this week | 这是Claude的MCP服务器，具有终端控制、文件系统搜索和diff文件编辑功能 | https://github.com/wonderwhy-er/DesktopCommanderMCP | 新增 |
| 18 | `dotnet/skills` | 4543 | 332 | C# | 886 stars this week | 用于使用.NET和C #协助AI编码代理的技能的存储库 | https://github.com/dotnet/skills |  |
| 19 | `alirezarezvani/claude-skills` | 22065 | 3084 | Python | 2,178 stars this week | 345 Claude Code技能和代理技能和插件（ 30多个代理、70多个自定义命令、330多个技能、可定制的参考、脚本） ，适用于Claude Code、Codex、Gemini CLI、Cursor和其他8个编码代理—工程、营销、产品、合规、C级咨询、研究…… | https://github.com/alirezarezvani/claude-skills | 新增 |
| 20 | `JuliusBrussee/caveman` | 87750 | 5034 | JavaScript | 7,184 stars this week | 🪨 为什么在很少令牌欺骗时使用许多令牌— Claude Code技能通过像穴居人一样说话来削减65 ％的令牌 | https://github.com/JuliusBrussee/caveman | 新增 |
| 21 | `addyosmani/agent-skills` | 76773 | 8245 | JavaScript | 7,236 stars this week | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `DeusData/codebase-memory-mcp` | 29675 | 2358 | C | 26,040 stars this month | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 2 | `calesthio/OpenMontage` | 36671 | 4415 | Python | 31,648 stars this month | 世界上第一个开源代理视频制作系统。12个管道， 52个工具， 500多个代理技能。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage |  |
| 3 | `Panniantong/Agent-Reach` | 54442 | 4489 | Python | 28,801 stars this month | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 4 | `asgeirtj/system_prompts_leaks` | 55800 | 9200 | JavaScript | 13,616 stars this month | 从Anthropic - Claude Fable 5、Opus 4.8、Claude Code、Claude Design中提取系统提示。OpenAI - ChatGPT GPT-5.6、Codex GPT-5.6、GPT-5.5。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 5 | `NVIDIA/SkillSpector` | 12768 | 1047 | Python | 10,971 stars this month | 人工智能代理技能的安全扫描仪。检测漏洞、恶意模式和安全风险。 | https://github.com/NVIDIA/SkillSpector |  |
| 6 | `kunchenguid/no-mistakes` | 5815 | 504 | Go | 4,513 stars this month | git push no-mistakes | https://github.com/kunchenguid/no-mistakes | 新增 |
| 7 | `usestrix/strix` | 40110 | 4205 | Python | 13,697 stars this month | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 8 | `ogulcancelik/herdr` | 15197 | 1006 | Rust | 9,607 stars this month | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 9 | `iptv-org/iptv` | 132080 | 7515 | TypeScript | 14,536 stars this month | 收集来自世界各地的公开IPTV频道 | https://github.com/iptv-org/iptv |  |
| 10 | `simplex-chat/simplex-chat` | 18363 | 1223 | Haskell | 7,111 stars this month | SimpleX -第一个没有任何类型用户标识符的消息传递网络-设计为100 ％私有！ iOS ， Android和桌面应用程序📱！ | https://github.com/simplex-chat/simplex-chat |  |
| 11 | `Zackriya-Solutions/meetily` | 22643 | 2382 | Rust | 9,534 stars this month | 隐私第一，基于Rust构建的人工智能会议助手，具有4倍的Parakeet/Whisper实时转录、扬声器日记和Ollama摘要。100%本地处理。无需云。Meetily （ Meetly Ai - https://meetily.ai ）是首屈一指的自托管、开源Ai会议...... | https://github.com/Zackriya-Solutions/meetily |  |
| 12 | `stablyai/orca` | 15916 | 1241 | TypeScript | 10,439 stars this month | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面和移动设备上使用。 | https://github.com/stablyai/orca |  |
| 13 | `apple/container` | 47462 | 1584 | Swift | 20,582 stars this month | 用于在Mac上使用轻量级虚拟机创建和运行Linux容器的工具。它是用Swift编写的，并针对Apple芯片进行了优化。 | https://github.com/apple/container |  |
| 14 | `interviewstreet/hiring-agent` | 5471 | 1113 | Python | 4,239 stars this month | 用于评估和评分简历的AI代理。 | https://github.com/interviewstreet/hiring-agent |  |
| 15 | `alibaba/page-agent` | 25810 | 2372 | TypeScript | 7,146 stars this month | JavaScript页面内GUI代理。使用自然语言控制Web界面。 | https://github.com/alibaba/page-agent |  |
| 16 | `diegosouzapw/OmniRoute` | 15017 | 2297 | TypeScript | 8,325 stars this month | 永不停止编码。免费AI网关：一个端点， 231多家提供商（ 50多家免费） ，将Claude Code、Codex、Cursor、Cline和Copilot连接到免费的Claude/GPT/Gemini。RTK + Caveman堆叠压缩可节省15-95%的代币、智能自动回退、MCP/A2A、多模式API、桌面/PWA。 | https://github.com/diegosouzapw/OmniRoute |  |
| 17 | `n0-computer/iroh` | 11421 | 668 | Rust | 2,617 stars this month | IP地址中断，改为拨号键。将QUIC + NAT遍历添加到您的应用程序的库。 | https://github.com/n0-computer/iroh |  |
| 18 | `mauriceboe/TREK` | 9994 | 944 | TypeScript | 4,177 stars this month | 自托管行程/行程规划工具，提供实时协作、互动地图、PWA支持、SSO、预算、装箱单等功能。 | https://github.com/mauriceboe/TREK |  |
| 19 | `bradautomates/claude-video` | 7164 | 799 | Python | 4,609 stars this month | 让Claude能够观看任何视频。/观看下载、提取帧、转录，并将所有内容交给Claude。 | https://github.com/bradautomates/claude-video | 新增 |
| 20 | `JCodesMore/ai-website-cloner-template` | 27497 | 4008 | TypeScript | 10,636 stars this month | 使用AI编码代理，只需一个命令即可克隆任何网站 | https://github.com/JCodesMore/ai-website-cloner-template |  |


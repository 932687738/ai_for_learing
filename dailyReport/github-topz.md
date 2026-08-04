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

**最近一次更新时间**（Asia/Shanghai）： 2026-08-04 09:41:40

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 535673 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 492117 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 454266 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 453431 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 393653 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 385048 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 363500 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 9 | `donnemartin/system-design-primer` | 360550 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 10 | `jwasham/coding-interview-university` | 357737 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 11 | `vinta/awesome-python` | 312007 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `lyogavin/airllm` | 27176 | 2976 | Jupyter Notebook | 1,085 stars today | 使用单个4GB GPU的AirLLM 70B推理 | https://github.com/lyogavin/airllm |  |
| 2 | `zhaoxuya520/reverse-skill` | 15867 | 2236 | PowerShell | 2,446 stars today | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工… | https://github.com/zhaoxuya520/reverse-skill |  |
| 3 | `firecrawl/pdf-inspector` | 8332 | 551 | Rust | 1,699 stars today | 用于PDF检查、分类和文本提取的快速Rust库。智能检测扫描的PDF和基于文本的PDF ，以实现智能路由决策。 | https://github.com/firecrawl/pdf-inspector | 新增 |
| 4 | `esengine/DeepSeek-Reasonix` | 29969 | 1922 | Go | 883 stars today | 为您的终端提供DeepSeek原生AI编码代理。围绕前缀缓存稳定性而设计—保持运行。 | https://github.com/esengine/DeepSeek-Reasonix |  |
| 5 | `TencentCloud/TencentDB-Agent-Memory` | 12147 | 1147 | TypeScript | 1,090 stars today | TencentDB Agent Memory是AI Agent的团队级内存中心—将对话、文档和代码转换为四个可重用的内存资产（ Chat Memory、Skill、LLM-Wiki、Code-Graph ） ，这些资产在代理和框架之间进行管理、共享和配备。 | https://github.com/TencentCloud/TencentDB-Agent-Memory |  |
| 6 | `microsoft/AI-For-Beginners` | 60787 | 11838 | Jupyter Notebook | 1,902 stars today | 12周， 24课，全民人工智能！ | https://github.com/microsoft/AI-For-Beginners |  |
| 7 | `microsoft/generative-ai-for-beginners` | 115582 | 61441 | Jupyter Notebook | 775 stars today | 21节课，开始使用生成式人工智能构建 | https://github.com/microsoft/generative-ai-for-beginners |  |
| 8 | `donnemartin/system-design-primer` | 360550 | 57528 | Python | 237 stars today | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer | 新增 |
| 9 | `antirez/ds4` | 20373 | 1802 | C | 384 stars today | 适用于Metal、CUDA和ROCm的DeepSeek 4 Flash和PRO本地推理引擎 | https://github.com/antirez/ds4 |  |
| 10 | `shiyu-coder/Kronos` | 35830 | 5963 | Python | 200 stars today | Kronos ：金融市场语言的基础模型 | https://github.com/shiyu-coder/Kronos | 新增 |
| 11 | `Panniantong/Agent-Reach` | 65749 | 5457 | Python | 1,057 stars today | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 12 | `Alishahryar1/free-claude-code` | 44055 | 7270 | Python | 278 stars today | 从您的终端、应用程序、IDE或OpenClaw等手机（支持语音）免费使用Claude Code、Codex和Pi | https://github.com/Alishahryar1/free-claude-code | 新增 |
| 13 | `iv-org/invidious` | 22278 | 2480 | Crystal | 402 stars today | Invidious是YouTube的替代前端 | https://github.com/iv-org/invidious |  |
| 14 | `livekit/agents` | 12005 | 3458 | Python | 148 stars today | 构建实时语音AI代理的框架 🤖🎙️📹 | https://github.com/livekit/agents | 新增 |
| 15 | `usekaneo/kaneo` | 6883 | 553 | TypeScript | 665 stars today | 你需要的一🎯切。没有什么你不需要的。开源项目管理适合您，而不是对您不利。 | https://github.com/usekaneo/kaneo |  |
| 16 | `jamiepine/voicebox` | 48696 | 5994 | TypeScript | 412 stars today | 开源AI语音工作室。克隆、命令、创建。 | https://github.com/jamiepine/voicebox | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `block/buzz` | 21867 | 2393 | Rust | 7,372 stars this week | 蜂巢思维沟通平台 | https://github.com/block/buzz |  |
| 2 | `microsoft/AI-For-Beginners` | 60788 | 11838 | Jupyter Notebook | 7,554 stars this week | 12周， 24课，全民人工智能！ | https://github.com/microsoft/AI-For-Beginners |  |
| 3 | `virgiliojr94/book-to-skill` | 15938 | 1705 | Python | 5,405 stars this week | 将任何技术书籍PDF转化为Claude Code技能—随时准备在您工作时进行学习、参考和使用。 | https://github.com/virgiliojr94/book-to-skill |  |
| 4 | `zhaoxuya520/reverse-skill` | 15867 | 2236 | PowerShell | 6,154 stars this week | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工… | https://github.com/zhaoxuya520/reverse-skill | 新增 |
| 5 | `ayghri/i-have-adhd` | 16310 | 918 | Python | 5,012 stars this week | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 6 | `1jehuang/jcode` | 15597 | 1720 | Rust | 3,735 stars this week | RAM效率最高的线束 | https://github.com/1jehuang/jcode |  |
| 7 | `moeru-ai/airi` | 46717 | 4609 | TypeScript | 2,978 stars this week | 💖🧸 自我托管，你拥有的Grok Companion ，一个包含外府灵魂的容器，将它们带入我们的世界的网络生活，希望达到Neuro-sama的高度。能够实时语音聊天、Minecraft、Factorio播放。支持Web/macOS/Windows。 | https://github.com/moeru-ai/airi |  |
| 8 | `opengeos/GeoLibre` | 5210 | 517 | TypeScript | 2,630 stars this week | 一个轻量级的云原生GIS平台，用于可视化、探索和分析地理空间数据。它在Web浏览器、桌面、移动设备和Jupyter笔记本中运行。 | https://github.com/opengeos/GeoLibre |  |
| 9 | `pascalorg/editor` | 20940 | 2678 | TypeScript | 2,953 stars this week | 创建和共享3D建筑项目。 | https://github.com/pascalorg/editor |  |
| 10 | `different-ai/openwork` | 20685 | 2033 | TypeScript | 3,429 stars this week | Claude Cowork的开源替代品（由opencode提供支持） | https://github.com/different-ai/openwork |  |
| 11 | `andrewyng/aisuite` | 15964 | 1684 | Python | 444 stars this week | 面向多个生成式人工智能提供商的简单、统一的界面 | https://github.com/andrewyng/aisuite |  |
| 12 | `alibaba/open-code-review` | 18455 | 1243 | Go | 3,881 stars this week | 快速、高效、经受住阿里巴巴规模的考验。混合架构代码审核工具：确定性流水线+ LLM Agent、精确的行级注释、内置多语言规则集（ NPE、线程安全、XSS、SQL注入）、OpenAI &amp; Anthropic兼容。 | https://github.com/alibaba/open-code-review |  |
| 13 | `citrolabs/ego-lite` | 8044 | 394 | JavaScript | 2,625 stars this week | 人工智能代理运行浏览器自动化的最快浏览器，旨在与您的人工智能代理（如Codex或Claude Code ）共享您登录的浏览器状态，而不会打扰您。零成本，零配置。 | https://github.com/citrolabs/ego-lite |  |
| 14 | `pingdotgg/t3code` | 16510 | 3695 | TypeScript | 1,270 stars this week | — | https://github.com/pingdotgg/t3code |  |
| 15 | `microsoft/TRELLIS.2` | 10318 | 1235 | Python | 1,250 stars this week | 用于3D生成的本机和紧凑型结构化潜点 | https://github.com/microsoft/TRELLIS.2 |  |
| 16 | `earthtojake/text-to-cad` | 12695 | 1342 | JavaScript | 1,908 stars this week | CAD、CAE和CAM的代理技能库 | https://github.com/earthtojake/text-to-cad |  |
| 17 | `lyogavin/airllm` | 27176 | 2976 | Jupyter Notebook | 2,410 stars this week | 使用单个4GB GPU的AirLLM 70B推理 | https://github.com/lyogavin/airllm | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `permissionlesstech/bitchat` | 34324 | 5477 | Swift | 8,367 stars this month | 蓝牙网状聊天， IRC共鸣 | https://github.com/permissionlesstech/bitchat |  |
| 2 | `diegosouzapw/OmniRoute` | 38833 | 5131 | TypeScript | 28,232 stars this month | 永不停止编码。免费MIT AI网关：一个端点， 290多个提供商（ 90多个免费） ， 500多个型号— Kimi ， Claude ， GPT ， OpenAI ， Gemini ， GLM ， DeepSeek ， MiniMax。适用于Claude Code、Codex、Cursor、OpenCode、Cline和Copilot。配额感知自动回退， RTK +穴居人压缩保存…… | https://github.com/diegosouzapw/OmniRoute |  |
| 3 | `stablyai/orca` | 36687 | 2605 | TypeScript | 25,250 stars this month | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面、移动和VPS上使用。 | https://github.com/stablyai/orca |  |
| 4 | `emilkowalski/skills` | 24402 | 1317 | — | 19,789 stars this month | 设计师和工程师的技能。 | https://github.com/emilkowalski/skills |  |
| 5 | `tt-a1i/archify` | 8861 | 719 | HTML | 6,501 stars this month | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify |  |
| 6 | `koala73/worldmonitor` | 78498 | 11726 | TypeScript | 17,517 stars this month | 实时全球智能仪表板。在统一的态势感知界面中进行人工智能驱动的新闻聚合、地缘政治监控和基础设施跟踪 | https://github.com/koala73/worldmonitor |  |
| 7 | `Nutlope/hallmark` | 21242 | 1072 | CSS | 17,706 stars this month | Claude Code、Cursor和Codex的防AI倾斜设计技能。 | https://github.com/Nutlope/hallmark |  |
| 8 | `iOfficeAI/OfficeCLI` | 24873 | 1676 | C# | 16,458 stars this month | OfficeCLI是第一个也是最好的Office套件，专为AI代理读取、编辑和自动化Word、Excel和PowerPoint文件而构建。免费、开源、单一二进制文件，无需安装Office。 | https://github.com/iOfficeAI/OfficeCLI |  |
| 9 | `bradautomates/claude-video` | 13680 | 1330 | Python | 10,750 stars this month | 让Claude能够观看任何视频。/观看下载、提取帧、转录，并将所有内容交给Claude。 | https://github.com/bradautomates/claude-video |  |
| 10 | `Zackriya-Solutions/meetily` | 28147 | 2943 | Rust | 14,535 stars this month | 隐私第一，基于Rust构建的人工智能会议助手，具有4倍的Parakeet/Whisper实时转录、扬声器日记和Ollama摘要。100%本地处理。无需云。Meetily （ Meetly Ai - https://meetily.ai ）是首屈一指的自托管、开源Ai会议...... | https://github.com/Zackriya-Solutions/meetily |  |
| 11 | `huggingface/speech-to-speech` | 10716 | 1315 | Python | 5,579 stars this month | 使用开源模型构建本地语音代理 | https://github.com/huggingface/speech-to-speech |  |
| 12 | `wonderwhy-er/DesktopCommanderMCP` | 9123 | 1091 | TypeScript | 3,006 stars this month | 这是Claude的MCP服务器，具有终端控制、文件系统搜索和diff文件编辑功能 | https://github.com/wonderwhy-er/DesktopCommanderMCP |  |
| 13 | `facebook/astryx` | 11448 | 974 | TypeScript | 7,387 stars this month | 完全可定制和代理就绪的开源设计系统 | https://github.com/facebook/astryx |  |
| 14 | `openai/codex-plugin-cc` | 31153 | 2097 | JavaScript | 8,384 stars this month | 使用Claude Code的Codex来查看代码或委派任务。 | https://github.com/openai/codex-plugin-cc |  |
| 15 | `asgeirtj/system_prompts_leaks` | 62171 | 10193 | JavaScript | 14,503 stars this month | 从Anthropic - Claude Fable 5、Opus 5、Claude Design、Claude Code中提取系统提示。OpenAI - ChatGPT GPT-5.6-Sol ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 16 | `1jehuang/jcode` | 15597 | 1720 | Rust | 7,469 stars this month | RAM效率最高的线束 | https://github.com/1jehuang/jcode |  |
| 17 | `Shubhamsaboo/awesome-llm-apps` | 130233 | 19225 | Python | 14,250 stars this month | 100多个人工智能代理、代理技能和RAG应用程序-免费开源。 | https://github.com/Shubhamsaboo/awesome-llm-apps |  |
| 18 | `HKUDS/DeepTutor` | 32232 | 4212 | Python | 7,155 stars this month | DeepTutor ：终身个性化辅导。https://deeptutor.info/。 | https://github.com/HKUDS/DeepTutor |  |
| 19 | `pbakaus/impeccable` | 54505 | 3279 | JavaScript | 11,471 stars this month | 让您的人工智能更好地进行设计的设计语言。 | https://github.com/pbakaus/impeccable |  |
| 20 | `usestrix/strix` | 47251 | 4998 | Python | 13,453 stars this month | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 21 | `OpenCut-app/OpenCut` | 80745 | 8014 | TypeScript | 19,626 stars this month | 开源CapCut替代方案 | https://github.com/OpenCut-app/OpenCut |  |
| 22 | `pingdotgg/t3code` | 16510 | 3695 | TypeScript | 3,384 stars this month | — | https://github.com/pingdotgg/t3code | 新增 |


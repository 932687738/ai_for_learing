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

**最近一次更新时间**（Asia/Shanghai）： 2026-08-05 09:38:57

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 536075 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 492440 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 454391 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 453492 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 393725 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 385144 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 363618 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 9 | `donnemartin/system-design-primer` | 360997 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 10 | `jwasham/coding-interview-university` | 357807 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 11 | `vinta/awesome-python` | 312210 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `TencentCloud/TencentDB-Agent-Memory` | 13675 | 1284 | TypeScript | 1,111 stars today | TencentDB Agent Memory是AI Agent的团队级内存中心—将对话、文档和代码转换为四个可重用的内存资产（ Chat Memory、Skill、LLM-Wiki、Code-Graph ） ，这些资产在代理和框架之间进行管理、共享和配备。 | https://github.com/TencentCloud/TencentDB-Agent-Memory |  |
| 2 | `zhaoxuya520/reverse-skill` | 17942 | 2460 | PowerShell | 2,297 stars today | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工… | https://github.com/zhaoxuya520/reverse-skill |  |
| 3 | `firecrawl/pdf-inspector` | 10071 | 660 | Rust | 2,540 stars today | 用于PDF检查、分类和文本提取的快速Rust库。智能检测扫描的PDF和基于文本的PDF ，以实现智能路由决策。 | https://github.com/firecrawl/pdf-inspector |  |
| 4 | `uber/ADR` | 693 | 69 | Python | 148 stars today | ADR通过可观察性、安全基准测试和威胁检测来保护企业AI代理。已部署到优步。 | https://github.com/uber/ADR | 新增 |
| 5 | `obra/superpowers` | 266502 | 23829 | Shell | 653 stars today | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers | 新增 |
| 6 | `microsoft/generative-ai-for-beginners` | 116283 | 61551 | Jupyter Notebook | 783 stars today | 21节课，开始使用生成式人工智能构建 | https://github.com/microsoft/generative-ai-for-beginners |  |
| 7 | `cypress-io/cypress` | 50799 | 3628 | TypeScript | 11 stars today | 对浏览器中运行的任何内容进行快速、简单和可靠的测试。 | https://github.com/cypress-io/cypress | 新增 |
| 8 | `lyogavin/airllm` | 28407 | 3065 | Jupyter Notebook | 1,711 stars today | 使用单个4GB GPU的AirLLM 70B推理 | https://github.com/lyogavin/airllm |  |
| 9 | `webpack/webpack` | 65940 | 9528 | JavaScript | 10 stars today | Javascript和朋友的捆绑包。将许多模块打包成几个捆绑资产。代码拆分允许按需加载应用程序的部分。通过“加载器” ，模块可以是CommonJs、AMD、ES6模块、CSS、图像、JSON、Coffeescript、LESS……以及您的自定义填充物…… | https://github.com/webpack/webpack | 新增 |
| 10 | `gabime/spdlog` | 29380 | 5372 | C++ | 10 stars today | 快速C + +日志记录库。 | https://github.com/gabime/spdlog | 新增 |
| 11 | `denoland/deno` | 108067 | 6306 | Rust | 31 stars today | JavaScript和TypeScript的现代运行时。 | https://github.com/denoland/deno | 新增 |
| 12 | `usekaneo/kaneo` | 7308 | 579 | TypeScript | 559 stars today | 你需要的一🎯切。没有什么你不需要的。开源项目管理适合您，而不是对您不利。 | https://github.com/usekaneo/kaneo |  |
| 13 | `livekit/agents` | 12421 | 3483 | Python | 432 stars today | 构建实时语音AI代理的框架 🤖🎙️📹 | https://github.com/livekit/agents |  |
| 14 | `angular/angular` | 100835 | 27401 | TypeScript | 13 stars today | 放心交付网络应用 🚀 | https://github.com/angular/angular | 新增 |
| 15 | `tailwindlabs/tailwindcss` | 96486 | 5533 | TypeScript | 52 stars today | 实用程序优先的CSS框架，用于快速UI开发。 | https://github.com/tailwindlabs/tailwindcss | 新增 |
| 16 | `browser-use/video-use` | 19347 | 2409 | Python | 320 stars today | 使用编码代理编辑视频 | https://github.com/browser-use/video-use | 新增 |
| 17 | `esengine/DeepSeek-Reasonix` | 30805 | 1982 | Go | 922 stars today | 为您的终端提供DeepSeek原生AI编码代理。围绕前缀缓存稳定性而设计—保持运行。 | https://github.com/esengine/DeepSeek-Reasonix |  |
| 18 | `EveryInc/compound-engineering-plugin` | 23882 | 1958 | TypeScript | 40 stars today | Claude Code、Codex、Cursor等的官方复合工程插件 | https://github.com/EveryInc/compound-engineering-plugin | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `zhaoxuya520/reverse-skill` | 17944 | 2460 | PowerShell | 8,386 stars this week | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工… | https://github.com/zhaoxuya520/reverse-skill |  |
| 2 | `microsoft/AI-For-Beginners` | 61691 | 11982 | Jupyter Notebook | 8,582 stars this week | 12周， 24课，全民人工智能！ | https://github.com/microsoft/AI-For-Beginners |  |
| 3 | `block/buzz` | 22561 | 2526 | Rust | 7,262 stars this week | 蜂巢思维沟通平台 | https://github.com/block/buzz |  |
| 4 | `virgiliojr94/book-to-skill` | 16417 | 1745 | Python | 5,420 stars this week | 将任何技术书籍PDF转化为Claude Code技能—随时准备在您工作时进行学习、参考和使用。 | https://github.com/virgiliojr94/book-to-skill |  |
| 5 | `different-ai/openwork` | 20926 | 2057 | TypeScript | 3,601 stars this week | Claude Cowork的开源替代品（由opencode提供支持） | https://github.com/different-ai/openwork |  |
| 6 | `ayghri/i-have-adhd` | 16799 | 947 | Python | 4,389 stars this week | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 7 | `lyogavin/airllm` | 28408 | 3066 | Jupyter Notebook | 3,911 stars this week | 使用单个4GB GPU的AirLLM 70B推理 | https://github.com/lyogavin/airllm |  |
| 8 | `1jehuang/jcode` | 15894 | 1753 | Rust | 3,294 stars this week | RAM效率最高的线束 | https://github.com/1jehuang/jcode |  |
| 9 | `TencentCloud/TencentDB-Agent-Memory` | 13677 | 1284 | TypeScript | 3,659 stars this week | TencentDB Agent Memory是AI Agent的团队级内存中心—将对话、文档和代码转换为四个可重用的内存资产（ Chat Memory、Skill、LLM-Wiki、Code-Graph ） ，这些资产在代理和框架之间进行管理、共享和配备。 | https://github.com/TencentCloud/TencentDB-Agent-Memory | 新增 |
| 10 | `opengeos/GeoLibre` | 5391 | 531 | TypeScript | 2,236 stars this week | 一个轻量级的云原生GIS平台，用于可视化、探索和分析地理空间数据。它在Web浏览器、桌面、移动设备和Jupyter笔记本中运行。 | https://github.com/opengeos/GeoLibre |  |
| 11 | `moeru-ai/airi` | 46873 | 4632 | TypeScript | 2,358 stars this week | 💖🧸 自我托管，你拥有的Grok Companion ，一个包含外府灵魂的容器，将它们带入我们的世界的网络生活，希望达到Neuro-sama的高度。能够实时语音聊天、Minecraft、Factorio播放。支持Web/macOS/Windows。 | https://github.com/moeru-ai/airi |  |
| 12 | `alibaba/open-code-review` | 18802 | 1269 | Go | 3,361 stars this week | 快速、高效、经受住阿里巴巴规模的考验。混合架构代码审核工具：确定性流水线+ LLM Agent、精确的行级注释、内置多语言规则集（ NPE、线程安全、XSS、SQL注入）、OpenAI &amp; Anthropic兼容。 | https://github.com/alibaba/open-code-review |  |
| 13 | `pascalorg/editor` | 21055 | 2688 | TypeScript | 2,696 stars this week | 创建和共享3D建筑项目。 | https://github.com/pascalorg/editor |  |
| 14 | `citrolabs/ego-lite` | 8358 | 405 | JavaScript | 2,633 stars this week | 人工智能代理运行浏览器自动化的最快浏览器，旨在与您的人工智能代理（如Codex或Claude Code ）共享您登录的浏览器状态，而不会打扰您。零成本，零配置。 | https://github.com/citrolabs/ego-lite |  |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `permissionlesstech/bitchat` | 34440 | 5501 | Swift | 8,467 stars this month | 蓝牙网状聊天， IRC共鸣 | https://github.com/permissionlesstech/bitchat |  |
| 2 | `diegosouzapw/OmniRoute` | 39719 | 5256 | TypeScript | 28,511 stars this month | 永不停止编码。免费MIT AI网关：一个端点， 290多个提供商（ 90多个免费） ， 500多个型号— Kimi ， Claude ， GPT ， OpenAI ， Gemini ， GLM ， DeepSeek ， MiniMax。适用于Claude Code、Codex、Cursor、OpenCode、Cline和Copilot。配额感知自动回退， RTK +穴居人压缩保存…… | https://github.com/diegosouzapw/OmniRoute |  |
| 3 | `MadsLorentzen/ai-job-search` | 29693 | 10083 | TypeScript | 25,195 stars this month | 在您的机器上运行的作业搜索。基于Claude Code构建的人工智能求职框架：评估帖子、定制简历、撰写求职信、准备面试。分叉并拥有它。 | https://github.com/MadsLorentzen/ai-job-search | 新增 |
| 4 | `stablyai/orca` | 37469 | 2653 | TypeScript | 25,624 stars this month | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面、移动和VPS上使用。 | https://github.com/stablyai/orca |  |
| 5 | `emilkowalski/skills` | 24952 | 1345 | — | 20,079 stars this month | 设计师和工程师的技能。 | https://github.com/emilkowalski/skills |  |
| 6 | `tt-a1i/archify` | 9153 | 734 | HTML | 6,627 stars this month | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify |  |
| 7 | `Nutlope/hallmark` | 21700 | 1101 | CSS | 18,119 stars this month | Claude Code、Cursor和Codex的防AI倾斜设计技能。 | https://github.com/Nutlope/hallmark |  |
| 8 | `koala73/worldmonitor` | 78834 | 11777 | TypeScript | 17,795 stars this month | 实时全球智能仪表板。在统一的态势感知界面中进行人工智能驱动的新闻聚合、地缘政治监控和基础设施跟踪 | https://github.com/koala73/worldmonitor |  |
| 9 | `iOfficeAI/OfficeCLI` | 25428 | 1710 | C# | 17,070 stars this month | OfficeCLI是第一个也是最好的Office套件，专为AI代理读取、编辑和自动化Word、Excel和PowerPoint文件而构建。免费、开源、单一二进制文件，无需安装Office。 | https://github.com/iOfficeAI/OfficeCLI |  |
| 10 | `huggingface/speech-to-speech` | 10957 | 1350 | Python | 5,734 stars this month | 使用开源模型构建本地语音代理 | https://github.com/huggingface/speech-to-speech |  |
| 11 | `bradautomates/claude-video` | 13896 | 1344 | Python | 10,848 stars this month | 让Claude能够观看任何视频。/观看下载、提取帧、转录，并将所有内容交给Claude。 | https://github.com/bradautomates/claude-video |  |
| 12 | `wonderwhy-er/DesktopCommanderMCP` | 9160 | 1101 | TypeScript | 3,053 stars this month | 这是Claude的MCP服务器，具有终端控制、文件系统搜索和diff文件编辑功能 | https://github.com/wonderwhy-er/DesktopCommanderMCP |  |
| 13 | `1jehuang/jcode` | 15894 | 1753 | Rust | 7,778 stars this month | RAM效率最高的线束 | https://github.com/1jehuang/jcode |  |
| 14 | `Shubhamsaboo/awesome-llm-apps` | 130529 | 19260 | Python | 14,514 stars this month | 100多个人工智能代理、代理技能和RAG应用程序-免费开源。 | https://github.com/Shubhamsaboo/awesome-llm-apps |  |
| 15 | `HKUDS/DeepTutor` | 32420 | 4234 | Python | 7,338 stars this month | DeepTutor ：终身个性化辅导。https://deeptutor.info/。 | https://github.com/HKUDS/DeepTutor |  |
| 16 | `pbakaus/impeccable` | 55245 | 3345 | JavaScript | 11,861 stars this month | 让您的人工智能更好地进行设计的设计语言。 | https://github.com/pbakaus/impeccable |  |
| 17 | `facebook/astryx` | 11601 | 986 | TypeScript | 6,591 stars this month | 完全可定制和代理就绪的开源设计系统 | https://github.com/facebook/astryx |  |
| 18 | `pingdotgg/t3code` | 16654 | 3730 | TypeScript | 3,503 stars this month | — | https://github.com/pingdotgg/t3code |  |
| 19 | `OpenCut-app/OpenCut` | 80943 | 8029 | TypeScript | 19,775 stars this month | 开源CapCut替代方案 | https://github.com/OpenCut-app/OpenCut |  |
| 20 | `HKUDS/Vibe-Trading` | 29638 | 4776 | Python | 12,089 stars this month | “Vibe-Trading ：您的个人交易代理” | https://github.com/HKUDS/Vibe-Trading | 新增 |
| 21 | `openai/codex-plugin-cc` | 31293 | 2116 | JavaScript | 7,731 stars this month | 使用Claude Code的Codex来查看代码或委派任务。 | https://github.com/openai/codex-plugin-cc |  |
| 22 | `every-app/open-seo` | 10422 | 1197 | TypeScript | 6,380 stars this month | Semrush和Ahrefs的开源替代品 | https://github.com/every-app/open-seo | 新增 |
| 23 | `usestrix/strix` | 48356 | 5101 | Python | 12,737 stars this month | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |


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

**最近一次更新时间**（Asia/Shanghai）： 2026-08-03 10:33:02

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 534972 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 491656 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 454136 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 453366 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 393576 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 384964 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 363417 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 9 | `donnemartin/system-design-primer` | 360163 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 10 | `jwasham/coding-interview-university` | 357692 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 11 | `vinta/awesome-python` | 311805 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `microsoft/AI-For-Beginners` | 59252 | 11633 | Jupyter Notebook | 2,629 stars today | 12周， 24课，全民人工智能！ | https://github.com/microsoft/AI-For-Beginners |  |
| 2 | `usekaneo/kaneo` | 6229 | 518 | TypeScript | 496 stars today | 你需要的一🎯切。没有什么你不需要的。开源项目管理适合您，而不是对您不利。 | https://github.com/usekaneo/kaneo | 新增 |
| 3 | `lyogavin/airllm` | 25762 | 2890 | Jupyter Notebook | 819 stars today | 使用单个4GB GPU的AirLLM 70B推理 | https://github.com/lyogavin/airllm | 新增 |
| 4 | `iv-org/invidious` | 22008 | 2459 | Crystal | 305 stars today | Invidious是YouTube的替代前端 | https://github.com/iv-org/invidious | 新增 |
| 5 | `codecrafters-io/build-your-own-x` | 534972 | 50567 | Markdown | 674 stars today | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x | 新增 |
| 6 | `zhaoxuya520/reverse-skill` | 13722 | 2040 | PowerShell | 1,141 stars today | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工… | https://github.com/zhaoxuya520/reverse-skill | 新增 |
| 7 | `different-ai/openwork` | 20378 | 2092 | TypeScript | 280 stars today | Claude Cowork的开源替代品（由opencode提供支持） | https://github.com/different-ai/openwork |  |
| 8 | `microsoft/generative-ai-for-beginners` | 114850 | 61301 | Jupyter Notebook | 588 stars today | 21节课，开始使用生成式人工智能构建 | https://github.com/microsoft/generative-ai-for-beginners | 新增 |
| 9 | `Panniantong/Agent-Reach` | 64803 | 5357 | Python | 659 stars today | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach | 新增 |
| 10 | `TencentCloud/TencentDB-Agent-Memory` | 11145 | 1060 | TypeScript | 602 stars today | TencentDB Agent Memory是AI Agent的团队级内存中心—将对话、文档和代码转换为四个可重用的内存资产（ Chat Memory、Skill、LLM-Wiki、Code-Graph ） ，这些资产在代理和框架之间进行管理、共享和配备。 | https://github.com/TencentCloud/TencentDB-Agent-Memory | 新增 |
| 11 | `mvanhorn/last30days-skill` | 56909 | 4979 | Python | 206 stars today | 人工智能代理技能，研究Reddit、X、YouTube、HN、Polymarket和网络上的任何主题，然后合成基础摘要 | https://github.com/mvanhorn/last30days-skill |  |
| 12 | `NomaDamas/k-skill` | 6904 | 810 | JavaScript | 177 stars today | 한국인을 위한 스킬 모음집 - 에이전트를 한국인으로 | https://github.com/NomaDamas/k-skill | 新增 |
| 13 | `HarbourMasters/Lighthouse` | 229 | 18 | C | 65 stars today | — | https://github.com/HarbourMasters/Lighthouse | 新增 |
| 14 | `antirez/ds4` | 20036 | 1776 | C | 139 stars today | 适用于Metal、CUDA和ROCm的DeepSeek 4 Flash和PRO本地推理引擎 | https://github.com/antirez/ds4 | 新增 |
| 15 | `esengine/DeepSeek-Reasonix` | 29150 | 1875 | Go | 333 stars today | 为您的终端提供DeepSeek原生AI编码代理。围绕前缀缓存稳定性而设计—保持运行。 | https://github.com/esengine/DeepSeek-Reasonix | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `block/buzz` | 21159 | 2263 | Rust | 8,217 stars this week | 蜂巢思维沟通平台 | https://github.com/block/buzz |  |
| 2 | `virgiliojr94/book-to-skill` | 15429 | 1663 | Python | 5,223 stars this week | 将任何技术书籍PDF转化为Claude Code技能—随时准备在您工作时进行学习、参考和使用。 | https://github.com/virgiliojr94/book-to-skill |  |
| 3 | `ayghri/i-have-adhd` | 15734 | 881 | Python | 5,225 stars this week | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 4 | `microsoft/AI-For-Beginners` | 59255 | 11633 | Jupyter Notebook | 5,601 stars this week | 12周， 24课，全民人工智能！ | https://github.com/microsoft/AI-For-Beginners | 新增 |
| 5 | `1jehuang/jcode` | 15291 | 1693 | Rust | 3,620 stars this week | RAM效率最高的线束 | https://github.com/1jehuang/jcode |  |
| 6 | `pascalorg/editor` | 20758 | 2664 | TypeScript | 3,163 stars this week | 创建和共享3D建筑项目。 | https://github.com/pascalorg/editor |  |
| 7 | `alibaba/open-code-review` | 17956 | 1210 | Go | 4,365 stars this week | 开源和免费—在阿里巴巴的规模上经过测试。混合架构代码审核工具：确定性流水线+ LLM Agent、精确的行级注释、内置多语言规则集（ NPE、线程安全、XSS、SQL注入）、OpenAI &amp; Anthropic兼容。 | https://github.com/alibaba/open-code-review |  |
| 8 | `permissionlesstech/bitchat` | 34170 | 5457 | Swift | 4,942 stars this week | 蓝牙网状聊天， IRC共鸣 | https://github.com/permissionlesstech/bitchat | 新增 |
| 9 | `moeru-ai/airi` | 46566 | 4592 | TypeScript | 3,431 stars this week | 💖🧸 自我托管，你拥有的Grok Companion ，一个包含外府灵魂的容器，将它们带入我们的世界的网络生活，希望达到Neuro-sama的高度。能够实时语音聊天、Minecraft、Factorio播放。支持Web/macOS/Windows。 | https://github.com/moeru-ai/airi |  |
| 10 | `andrewyng/aisuite` | 15904 | 1685 | Python | 576 stars this week | 面向多个生成式人工智能提供商的简单、统一的界面 | https://github.com/andrewyng/aisuite | 新增 |
| 11 | `opengeos/GeoLibre` | 4998 | 499 | TypeScript | 2,933 stars this week | 一个轻量级的云原生GIS平台，用于可视化、探索和分析地理空间数据。它在Web浏览器、桌面、移动设备和Jupyter笔记本中运行。 | https://github.com/opengeos/GeoLibre |  |
| 12 | `citrolabs/ego-lite` | 7701 | 381 | JavaScript | 3,582 stars this week | 人工智能代理运行浏览器自动化的最快浏览器，旨在与您的人工智能代理（如Codex或Claude Code ）共享您登录的浏览器状态，而不会打扰您。零成本，零配置。 | https://github.com/citrolabs/ego-lite |  |
| 13 | `pingdotgg/t3code` | 16353 | 3645 | TypeScript | 1,431 stars this week | — | https://github.com/pingdotgg/t3code |  |
| 14 | `diegosouzapw/OmniRoute` | 37958 | 4949 | TypeScript | 7,141 stars this week | 永不停止编码。免费MIT AI网关：一个端点， 290多个提供商（ 90多个免费） ， 500多个型号— Kimi ， Claude ， GPT ， OpenAI ， Gemini ， GLM ， DeepSeek ， MiniMax。适用于Claude Code、Codex、Cursor、OpenCode、Cline和Copilot。配额感知自动回退， RTK +穴居人压缩保存…… | https://github.com/diegosouzapw/OmniRoute |  |
| 15 | `earthtojake/text-to-cad` | 12535 | 1328 | JavaScript | 2,063 stars this week | CAD、CAE和CAM的代理技能库 | https://github.com/earthtojake/text-to-cad | 新增 |
| 16 | `microsoft/TRELLIS.2` | 10173 | 1222 | Python | 1,106 stars this week | 用于3D生成的本机和紧凑型结构化潜点 | https://github.com/microsoft/TRELLIS.2 | 新增 |
| 17 | `different-ai/openwork` | 20378 | 2092 | TypeScript | 2,925 stars this week | Claude Cowork的开源替代品（由opencode提供支持） | https://github.com/different-ai/openwork | 新增 |
| 18 | `permissionlesstech/bitchat-android` | 7263 | 1789 | Kotlin | 928 stars this week | 去中心化网格聊天 | https://github.com/permissionlesstech/bitchat-android | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `permissionlesstech/bitchat` | 34170 | 5457 | Swift | 8,160 stars this month | 蓝牙网状聊天， IRC共鸣 | https://github.com/permissionlesstech/bitchat |  |
| 2 | `diegosouzapw/OmniRoute` | 37958 | 4949 | TypeScript | 27,721 stars this month | 永不停止编码。免费MIT AI网关：一个端点， 290多个提供商（ 90多个免费） ， 500多个型号— Kimi ， Claude ， GPT ， OpenAI ， Gemini ， GLM ， DeepSeek ， MiniMax。适用于Claude Code、Codex、Cursor、OpenCode、Cline和Copilot。配额感知自动回退， RTK +穴居人压缩保存…… | https://github.com/diegosouzapw/OmniRoute |  |
| 3 | `stablyai/orca` | 35876 | 2523 | TypeScript | 25,091 stars this month | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面、移动和VPS上使用。 | https://github.com/stablyai/orca |  |
| 4 | `emilkowalski/skills` | 24011 | 1299 | — | 19,563 stars this month | 设计师和工程师的技能。 | https://github.com/emilkowalski/skills |  |
| 5 | `tt-a1i/archify` | 8558 | 665 | HTML | 6,402 stars this month | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify | 新增 |
| 6 | `Nutlope/hallmark` | 20888 | 1047 | CSS | 17,319 stars this month | Claude Code、Cursor和Codex的防AI倾斜设计技能。 | https://github.com/Nutlope/hallmark |  |
| 7 | `koala73/worldmonitor` | 78181 | 11686 | TypeScript | 17,164 stars this month | 实时全球智能仪表板。在统一的态势感知界面中进行人工智能驱动的新闻聚合、地缘政治监控和基础设施跟踪 | https://github.com/koala73/worldmonitor |  |
| 8 | `bradautomates/claude-video` | 13485 | 1315 | Python | 10,606 stars this month | 让Claude能够观看任何视频。/观看下载、提取帧、转录，并将所有内容交给Claude。 | https://github.com/bradautomates/claude-video |  |
| 9 | `Zackriya-Solutions/meetily` | 28015 | 2894 | Rust | 14,974 stars this month | 隐私第一，基于Rust构建的人工智能会议助手，具有4倍的Parakeet/Whisper实时转录、扬声器日记和Ollama摘要。100%本地处理。无需云。Meetily （ Meetly Ai - https://meetily.ai ）是首屈一指的自托管、开源Ai会议...... | https://github.com/Zackriya-Solutions/meetily |  |
| 10 | `iOfficeAI/OfficeCLI` | 24350 | 1645 | C# | 16,040 stars this month | OfficeCLI是第一个也是最好的Office套件，专为AI代理读取、编辑和自动化Word、Excel和PowerPoint文件而构建。免费、开源、单一二进制文件，无需安装Office。 | https://github.com/iOfficeAI/OfficeCLI |  |
| 11 | `asgeirtj/system_prompts_leaks` | 62010 | 10124 | JavaScript | 14,554 stars this month | 从Anthropic - Claude Fable 5、Opus 5、Claude Design、Claude Code中提取系统提示。OpenAI - ChatGPT GPT-5.6-Sol ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 12 | `openai/codex-plugin-cc` | 30993 | 2052 | JavaScript | 8,880 stars this month | 使用Claude Code的Codex来查看代码或委派任务。 | https://github.com/openai/codex-plugin-cc |  |
| 13 | `facebook/astryx` | 11312 | 933 | TypeScript | 8,233 stars this month | 完全可定制和代理就绪的开源设计系统 | https://github.com/facebook/astryx | 新增 |
| 14 | `huggingface/speech-to-speech` | 10489 | 1281 | Python | 5,497 stars this month | 使用开源模型构建本地语音代理 | https://github.com/huggingface/speech-to-speech |  |
| 15 | `wonderwhy-er/DesktopCommanderMCP` | 9083 | 1052 | TypeScript | 2,976 stars this month | 这是Claude的MCP服务器，具有终端控制、文件系统搜索和diff文件编辑功能 | https://github.com/wonderwhy-er/DesktopCommanderMCP |  |
| 16 | `usestrix/strix` | 46683 | 4912 | Python | 16,165 stars this month | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 17 | `1jehuang/jcode` | 15291 | 1693 | Rust | 7,157 stars this month | RAM效率最高的线束 | https://github.com/1jehuang/jcode | 新增 |
| 18 | `Shubhamsaboo/awesome-llm-apps` | 129868 | 19161 | Python | 13,958 stars this month | 100多个人工智能代理、代理技能和RAG应用程序-免费开源。 | https://github.com/Shubhamsaboo/awesome-llm-apps |  |
| 19 | `pbakaus/impeccable` | 54116 | 3213 | JavaScript | 11,349 stars this month | 让您的人工智能更好地进行设计的设计语言。 | https://github.com/pbakaus/impeccable | 新增 |
| 20 | `OpenCut-app/OpenCut` | 80560 | 7998 | TypeScript | 19,604 stars this month | 开源CapCut替代方案 | https://github.com/OpenCut-app/OpenCut |  |
| 21 | `HKUDS/DeepTutor` | 32030 | 4186 | Python | 6,905 stars this month | DeepTutor ：终身个性化辅导。https://deeptutor.info/。 | https://github.com/HKUDS/DeepTutor | 新增 |
| 22 | `Emily2040/seedance-2.0` | 5926 | 893 | Python | 4,195 stars this month | 使用Seedance 2.0进行四模态人工智能电影制作的综合生产流水线 | https://github.com/Emily2040/seedance-2.0 | 新增 |


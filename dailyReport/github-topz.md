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

**最近一次更新时间**（Asia/Shanghai）： 2026-07-28 16:19:45

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 532279 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 489792 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 453015 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 452987 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 393176 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 384382 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 362916 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 9 | `donnemartin/system-design-primer` | 359458 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 10 | `jwasham/coding-interview-university` | 357292 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 11 | `vinta/awesome-python` | 310747 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `permissionlesstech/bitchat` | 32712 | 5133 | Swift | 2,346 stars today | 蓝牙网状聊天， IRC共鸣 | https://github.com/permissionlesstech/bitchat | 新增 |
| 2 | `amnezia-vpn/amnezia-client` | 14029 | 1042 | C++ | 515 stars today | Amnezia VPN客户端（桌面版+移动版） | https://github.com/amnezia-vpn/amnezia-client | 新增 |
| 3 | `moeru-ai/airi` | 44347 | 4417 | TypeScript | 572 stars today | 💖🧸 自我托管，你拥有的Grok Companion ，一个包含外府灵魂的容器，将它们带入我们的世界的网络生活，希望达到Neuro-sama的高度。能够实时语音聊天、Minecraft、Factorio播放。支持Web/macOS/Windows。 | https://github.com/moeru-ai/airi | 新增 |
| 4 | `opengeos/GeoLibre` | 2951 | 369 | TypeScript | 420 stars today | 一个轻量级的云原生GIS平台，用于可视化、探索和分析地理空间数据。它在Web浏览器、桌面、移动设备和Jupyter笔记本中运行。 | https://github.com/opengeos/GeoLibre | 新增 |
| 5 | `yorukot/superfile` | 21094 | 675 | Go | 600 stars today | 漂亮的现代终端文件管理器 | https://github.com/yorukot/superfile | 新增 |
| 6 | `NanmiCoder/MediaCrawler` | 58648 | 11637 | Python | 362 stars today | 小红书笔记 · 评论爬虫、抖音视频 · 评论爬虫、快手视频 · 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖子 ｜ 百度贴吧评论回复爬虫 · 知乎问答文章｜评论爬虫 | https://github.com/NanmiCoder/MediaCrawler | 新增 |
| 7 | `pbakaus/impeccable` | 51881 | 3048 | JavaScript | 847 stars today | 让您的人工智能更好地进行设计的设计语言。 | https://github.com/pbakaus/impeccable | 新增 |
| 8 | `shiyu-coder/Kronos` | 34692 | 5809 | Python | 441 stars today | Kronos ：金融市场语言的基础模型 | https://github.com/shiyu-coder/Kronos | 新增 |
| 9 | `alibaba/open-code-review` | 15212 | 1024 | Go | 979 stars today | 开源和免费—在阿里巴巴的规模上经过测试。混合架构代码审核工具：确定性流水线+ LLM Agent、精确的行级注释、内置微调规则集（ NPE、线程安全、XSS、SQL注入）、OpenAI &amp; Anthropic兼容。 | https://github.com/alibaba/open-code-review | 新增 |
| 10 | `jenkinsci/jenkins` | 25939 | 9678 | Java | 180 stars today | Jenkins自动化服务器 | https://github.com/jenkinsci/jenkins | 新增 |
| 11 | `bradautomates/claude-video` | 11455 | 1161 | Python | 434 stars today | 让Claude能够观看任何视频。/观看下载、提取帧、转录，并将所有内容交给Claude。 | https://github.com/bradautomates/claude-video | 新增 |
| 12 | `vudovn/ag-kit` | 8034 | 1514 | TypeScript | 14 stars today | — | https://github.com/vudovn/ag-kit | 新增 |
| 13 | `apache/cassandra` | 10012 | 4005 | Java | 11 stars today | 开源事务性分布式数据库。商品硬件或云基础设施上的线性可扩展性和经过验证的容错性，而不会影响性能。 | https://github.com/apache/cassandra | 新增 |
| 14 | `mvanhorn/last30days-skill` | 54392 | 4704 | Python | 240 stars today | 人工智能代理技能，研究Reddit、X、YouTube、HN、Polymarket和网络上的任何主题，然后合成基础摘要 | https://github.com/mvanhorn/last30days-skill | 新增 |
| 15 | `ocornut/imgui` | 75275 | 11971 | C++ | 51 stars today | 尊敬的ImGui ：无臃肿的C + +图形用户界面，依赖关系最少 | https://github.com/ocornut/imgui | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `ayghri/i-have-adhd` | 11810 | 596 | Python | 6,961 stars this week | 您的编码代理阻止其埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd | 新增 |
| 2 | `koala73/worldmonitor` | 75569 | 11319 | TypeScript | 13,231 stars this week | 实时全球智能仪表板。在统一的态势感知界面中进行人工智能驱动的新闻聚合、地缘政治监控和基础设施跟踪 | https://github.com/koala73/worldmonitor | 新增 |
| 3 | `bojieli/ai-agent-book` | 23627 | 2398 | Python | 13,627 stars this week | 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码 | https://github.com/bojieli/ai-agent-book | 新增 |
| 4 | `oblien/openship` | 9063 | 735 | TypeScript | 4,911 stars this week | 自托管部署平台 | https://github.com/oblien/openship | 新增 |
| 5 | `agegr/pi-web` | 3053 | 400 | TypeScript | 1,676 stars this week | Pi编码代理的Web UI | https://github.com/agegr/pi-web | 新增 |
| 6 | `tirth8205/code-review-graph` | 27133 | 2512 | Python | 4,577 stars this week | MCP和CLI的本地优先代码智能图。构建代码库的持久映射，以便AI编码工具仅读取重要内容，并对审阅和大型重构工作流进行基准上下文缩减。 | https://github.com/tirth8205/code-review-graph | 新增 |
| 7 | `diegosouzapw/OmniRoute` | 32483 | 4206 | TypeScript | 11,057 stars this week | 永不停止编码。免费MIT AI网关：一个端点， 290多个提供商（ 90多个免费） ， 500多个型号— Kimi ， Claude ， GPT ， OpenAI ， Gemini ， GLM ， DeepSeek ， MiniMax。适用于Claude Code、Codex、Cursor、OpenCode、Cline和Copilot。配额感知自动回退， RTK +穴居人压缩保存…… | https://github.com/diegosouzapw/OmniRoute |  |
| 8 | `1jehuang/jcode` | 12359 | 1360 | Rust | 2,585 stars this week | 最具RAM效率的线束 | https://github.com/1jehuang/jcode | 新增 |
| 9 | `mattpocock/skills` | 192012 | 16499 | Shell | 12,682 stars this week | 真正工程师的技能。直接来自我的.agents目录。 | https://github.com/mattpocock/skills | 新增 |
| 10 | `earendil-works/pi` | 79341 | 9749 | TypeScript | 5,751 stars this week | AI agent toolkit ：统一LLM API、agent loop、TUI、coding agent CLI | https://github.com/earendil-works/pi | 新增 |
| 11 | `ruvnet/RuView` | 87067 | 11582 | Rust | 5,662 stars this week | π RuView将商用WiFi信号转化为实时空间智能、生命体征监测和存在检测--所有这些都无需一个像素的视频。 | https://github.com/ruvnet/RuView | 新增 |
| 12 | `shiyu-coder/Kronos` | 34692 | 5809 | Python | 2,167 stars this week | Kronos ：金融市场语言的基础模型 | https://github.com/shiyu-coder/Kronos | 新增 |
| 13 | `Pumpkin-MC/Pumpkin` | 10231 | 688 | Rust | 2,192 stars this week | 让每个人都能托管快速高效的Minecraft服务器。 | https://github.com/Pumpkin-MC/Pumpkin | 新增 |
| 14 | `rohitg00/ai-engineering-from-scratch` | 44379 | 7489 | Python | 3,961 stars this week | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch | 新增 |
| 15 | `HKUDS/DeepTutor` | 30691 | 4025 | Python | 2,172 stars this week | DeepTutor ：终身个性化辅导。https://deeptutor.info/。 | https://github.com/HKUDS/DeepTutor |  |
| 16 | `MoonshotAI/kimi-code` | 5451 | 801 | TypeScript | 1,263 stars this week | Kimi Code CLI —新一代代理的起点 | https://github.com/MoonshotAI/kimi-code | 新增 |
| 17 | `schollz/croc` | 38904 | 1544 | Go | 2,738 stars this week | 轻松安全地将物品从一台计算机发送到另一台计算机 🐊 📦 | https://github.com/schollz/croc | 新增 |
| 18 | `earthtojake/text-to-cad` | 11108 | 1199 | JavaScript | 2,262 stars this week | CAD、机器人和硬件设计的代理技能集合 | https://github.com/earthtojake/text-to-cad | 新增 |
| 19 | `CoreBunch/Instatic` | 6314 | 557 | TypeScript | 2,523 stars this week | Webflow、Framer和WordPress的开源替代品。Agentic自托管可视化CMS输出干净的静态页面。用户、角色、插件、内容、数据库，应有尽有。 | https://github.com/CoreBunch/Instatic | 新增 |
| 20 | `pingdotgg/t3code` | 15344 | 3351 | TypeScript | 1,050 stars this week | — | https://github.com/pingdotgg/t3code | 新增 |
| 21 | `hyprwm/Hyprland` | 37571 | 1894 | C++ | 782 stars this week | Hyprland是一款独立的、高度可定制的动态平铺Wayland合成器，不会牺牲外观。 | https://github.com/hyprwm/Hyprland | 新增 |
| 22 | `every-app/open-seo` | 8805 | 985 | TypeScript | 3,015 stars this week | Semrush和Ahrefs的开源替代品 | https://github.com/every-app/open-seo | 新增 |
| 23 | `Nutlope/hallmark` | 19034 | 953 | CSS | 4,758 stars this week | Claude Code、Cursor和Codex的防AI倾斜设计技能。 | https://github.com/Nutlope/hallmark |  |
| 24 | `stablyai/orca` | 31198 | 2207 | TypeScript | 7,546 stars this week | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面、移动和VPS上使用。 | https://github.com/stablyai/orca |  |
| 25 | `KnockOutEZ/wigolo` | 3781 | 249 | TypeScript | 1,478 stars this week | 您的AI编码代理的首选网络—通过MCP进行本地优先搜索、获取、抓取和研究。无API密钥，无云，每次查询$ 0。公开测试版。 | https://github.com/KnockOutEZ/wigolo | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `diegosouzapw/OmniRoute` | 32483 | 4206 | TypeScript | 24,936 stars this month | 永不停止编码。免费MIT AI网关：一个端点， 290多个提供商（ 90多个免费） ， 500多个型号— Kimi ， Claude ， GPT ， OpenAI ， Gemini ， GLM ， DeepSeek ， MiniMax。适用于Claude Code、Codex、Cursor、OpenCode、Cline和Copilot。配额感知自动回退， RTK +穴居人压缩保存…… | https://github.com/diegosouzapw/OmniRoute |  |
| 2 | `usestrix/strix` | 45107 | 4719 | Python | 18,948 stars this month | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 3 | `hasaneyldrm/exercises-dataset` | 17433 | 2131 | HTML | 16,896 stars this month | 1,324个运动健身数据集—动画GIF、180 × 180缩略图、肌肉群和设备数据，以及6种语言的分步说明。LogPress应用程序背后的运动数据层。 | https://github.com/hasaneyldrm/exercises-dataset | 新增 |
| 4 | `permissionlesstech/bitchat` | 32712 | 5133 | Swift | 5,679 stars this month | 蓝牙网状聊天， IRC共鸣 | https://github.com/permissionlesstech/bitchat | 新增 |
| 5 | `stablyai/orca` | 31198 | 2207 | TypeScript | 22,573 stars this month | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面、移动和VPS上使用。 | https://github.com/stablyai/orca |  |
| 6 | `catchorg/Catch2` | 21372 | 3390 | C++ | 1,057 stars this month | 用于单元测试、TDD和BDD的现代C + +原生测试框架-使用C + +14、C + +17及更高版本（ C + +11支持v2.x分支， C + +03支持Catch1.x分支） | https://github.com/catchorg/Catch2 | 新增 |
| 7 | `ogulcancelik/herdr` | 21672 | 1457 | Rust | 13,835 stars this month | 位于您终端中的座席多路复用器。 | https://github.com/ogulcancelik/herdr |  |
| 8 | `emilkowalski/skills` | 21781 | 1179 | — | 17,933 stars this month | 设计工程师的技能。 | https://github.com/emilkowalski/skills | 新增 |
| 9 | `Zackriya-Solutions/meetily` | 27077 | 2750 | Rust | 14,255 stars this month | 隐私第一，基于Rust构建的人工智能会议助手，具有4倍的Parakeet/Whisper实时转录、扬声器日记和Ollama摘要。100%本地处理。无需云。Meetily （ Meetly Ai - https://meetily.ai ）是首屈一指的自托管、开源Ai会议...... | https://github.com/Zackriya-Solutions/meetily |  |
| 10 | `Nutlope/hallmark` | 19034 | 953 | CSS | 15,231 stars this month | Claude Code、Cursor和Codex的防AI倾斜设计技能。 | https://github.com/Nutlope/hallmark | 新增 |
| 11 | `xbtlin/ai-berkshire` | 14524 | 2039 | Python | 10,999 stars this month | AI 时代的伯克希尔：基于 Claude Code / Codex 的价值投资研究框架。巴菲特·芒格·段永平·李录四大师方法论 + 多Agent并行研究。· AI-era Berkshire: a value investing research framework built for Claude Code / Codex. 4 masters' methodologies + multi-agent adversarial analysis. | https://github.com/xbtlin/ai-berkshire | 新增 |
| 12 | `asgeirtj/system_prompts_leaks` | 61029 | 9969 | JavaScript | 14,761 stars this month | 从Anthropic - Claude Fable 5、Opus 5、Claude Design、Claude Code中提取系统提示。OpenAI - ChatGPT GPT-5.6-Sol ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 13 | `Robbyant/lingbot-map` | 15717 | 1657 | Python | 8,189 stars this month | 用于从流数据重建场景的前馈3D基础模型 | https://github.com/Robbyant/lingbot-map | 新增 |
| 14 | `koala73/worldmonitor` | 75569 | 11319 | TypeScript | 15,236 stars this month | 实时全球智能仪表板。在统一的态势感知界面中进行人工智能驱动的新闻聚合、地缘政治监控和基础设施跟踪 | https://github.com/koala73/worldmonitor | 新增 |
| 15 | `iOfficeAI/OfficeCLI` | 22751 | 1532 | C# | 14,550 stars this month | OfficeCLI是第一个也是最好的Office套件，专为AI代理读取、编辑和自动化Word、Excel和PowerPoint文件而构建。免费、开源、单一二进制文件，无需安装Office。 | https://github.com/iOfficeAI/OfficeCLI |  |
| 16 | `DeusData/codebase-memory-mcp` | 36026 | 2816 | C | 19,689 stars this month | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp |  |
| 17 | `ocornut/imgui` | 75275 | 11971 | C++ | 1,186 stars this month | 尊敬的ImGui ：无臃肿的C + +图形用户界面，依赖关系最少 | https://github.com/ocornut/imgui |  |
| 18 | `HKUDS/Vibe-Trading` | 28172 | 4567 | Python | 14,723 stars this month | “Vibe-Trading ：您的个人交易代理” | https://github.com/HKUDS/Vibe-Trading | 新增 |
| 19 | `wonderwhy-er/DesktopCommanderMCP` | 8903 | 1010 | TypeScript | 2,807 stars this month | 这是Claude的MCP服务器，具有终端控制、文件系统搜索和diff文件编辑功能 | https://github.com/wonderwhy-er/DesktopCommanderMCP |  |
| 20 | `bradautomates/claude-video` | 11456 | 1161 | Python | 8,199 stars this month | 让Claude能够观看任何视频。/观看下载、提取帧、转录，并将所有内容交给Claude。 | https://github.com/bradautomates/claude-video | 新增 |
| 21 | `alibaba/page-agent` | 28037 | 2465 | TypeScript | 7,926 stars this month | JavaScript页面内GUI代理。使用自然语言控制Web界面。 | https://github.com/alibaba/page-agent |  |
| 22 | `openai/codex-plugin-cc` | 30164 | 1974 | JavaScript | 8,576 stars this month | 使用Claude Code的Codex来查看代码或委派任务。 | https://github.com/openai/codex-plugin-cc | 新增 |


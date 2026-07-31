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

**最近一次更新时间**（Asia/Shanghai）： 2026-07-31 10:07:56

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 533095 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 490770 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 453670 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 453220 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 393369 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 384622 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 363196 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 9 | `donnemartin/system-design-primer` | 359811 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 10 | `jwasham/coding-interview-university` | 357510 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 11 | `vinta/awesome-python` | 311268 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `huggingface/speech-to-speech` | 8943 | 1098 | Python | 628 stars today | 使用开源模型构建本地语音代理 | https://github.com/huggingface/speech-to-speech |  |
| 2 | `microsoft/AI-For-Beginners` | 54061 | 10963 | Jupyter Notebook | 155 stars today | 12周， 24课，全民人工智能！ | https://github.com/microsoft/AI-For-Beginners | 新增 |
| 3 | `paperswithbacktest/awesome-systematic-trading` | 11096 | 1420 | Python | 621 stars today | 精心策划的系统交易库、包、策略、书籍、博客和教程列表。 | https://github.com/paperswithbacktest/awesome-systematic-trading |  |
| 4 | `different-ai/openwork` | 18789 | 1910 | TypeScript | 915 stars today | Claude Cowork的开源替代品（由opencode提供支持） | https://github.com/different-ai/openwork |  |
| 5 | `WhiskeySockets/Baileys` | 10447 | 3254 | JavaScript | 19 stars today | 适用于WhatsApp Web的基于套接字的TS/JavaScript API | https://github.com/WhiskeySockets/Baileys | 新增 |
| 6 | `pascalorg/editor` | 20147 | 2621 | TypeScript | 625 stars today | 创建和共享3D建筑项目。 | https://github.com/pascalorg/editor |  |
| 7 | `mvanhorn/last30days-skill` | 55586 | 4787 | Python | 378 stars today | 人工智能代理技能，研究Reddit、X、YouTube、HN、Polymarket和网络上的任何主题，然后合成基础摘要 | https://github.com/mvanhorn/last30days-skill | 新增 |
| 8 | `dotnet/aspnetcore` | 38300 | 10859 | C# | 7 stars today | ASP.NET Core是一个跨平台.NET框架，用于在Windows、Mac或Linux上构建基于云的现代Web应用程序。 | https://github.com/dotnet/aspnetcore | 新增 |
| 9 | `microsoft/PowerToys` | 137147 | 8364 | C | 70 stars today | Microsoft PowerToys是一组实用程序，可在Windows上提高生产力和自定义 | https://github.com/microsoft/PowerToys | 新增 |
| 10 | `ansible/ansible` | 69902 | 24252 | Python | 29 stars today | Ansible是一个极其简单的IT自动化平台，使您的应用程序和系统更易于部署和维护。自动化从代码部署到网络配置到云管理的一切，使用简单的英语，使用SSH ，没有年龄…… | https://github.com/ansible/ansible | 新增 |
| 11 | `ChromeDevTools/chrome-devtools-mcp` | 48079 | 3261 | TypeScript | 80 stars today | 适用于编码代理的Chrome开发者工具 | https://github.com/ChromeDevTools/chrome-devtools-mcp | 新增 |
| 12 | `jenkinsci/jenkins` | 26305 | 9719 | Java | 25 stars today | Jenkins自动化服务器 | https://github.com/jenkinsci/jenkins | 新增 |
| 13 | `agavra/tuicr` | 1881 | 161 | Rust | 190 stars today | 使用vim键绑定的代码审查TUI | https://github.com/agavra/tuicr | 新增 |
| 14 | `affaan-m/ECC` | 236255 | 35928 | JavaScript | 804 stars today | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `block/buzz` | 18508 | 1810 | Rust | 12,444 stars this week | 蜂巢思维沟通平台 | https://github.com/block/buzz |  |
| 2 | `citrolabs/ego-lite` | 6567 | 315 | JavaScript | 5,037 stars this week | 人工智能代理运行浏览器自动化的最快浏览器，旨在与您的人工智能代理（如Codex或Claude Code ）共享您登录的浏览器状态，而不会打扰您。零成本，零配置。 | https://github.com/citrolabs/ego-lite |  |
| 3 | `koala73/worldmonitor` | 77012 | 11477 | TypeScript | 6,150 stars this week | 实时全球智能仪表板。在统一的态势感知界面中进行人工智能驱动的新闻聚合、地缘政治监控和基础设施跟踪 | https://github.com/koala73/worldmonitor |  |
| 4 | `ayghri/i-have-adhd` | 14256 | 758 | Python | 4,978 stars this week | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 5 | `bojieli/ai-agent-book` | 27494 | 2887 | Python | 9,304 stars this week | 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码 | https://github.com/bojieli/ai-agent-book |  |
| 6 | `alibaba/open-code-review` | 16605 | 1123 | Go | 5,322 stars this week | 开源和免费—在阿里巴巴的规模上经过测试。混合架构代码审核工具：确定性流水线+ LLM Agent、精确的行级注释、内置微调规则集（ NPE、线程安全、XSS、SQL注入）、OpenAI &amp; Anthropic兼容。 | https://github.com/alibaba/open-code-review |  |
| 7 | `mattpocock/skills` | 196377 | 16926 | Shell | 12,147 stars this week | 真正工程师的技能。直接来自我的.agents目录。 | https://github.com/mattpocock/skills |  |
| 8 | `diegosouzapw/OmniRoute` | 35199 | 4538 | TypeScript | 8,464 stars this week | 永不停止编码。免费MIT AI网关：一个端点， 290多个提供商（ 90多个免费） ， 500多个型号— Kimi ， Claude ， GPT ， OpenAI ， Gemini ， GLM ， DeepSeek ， MiniMax。适用于Claude Code、Codex、Cursor、OpenCode、Cline和Copilot。配额感知自动回退， RTK +穴居人压缩保存…… | https://github.com/diegosouzapw/OmniRoute |  |
| 9 | `shiyu-coder/Kronos` | 35121 | 5856 | Python | 2,258 stars this week | Kronos ：金融市场语言的基础模型 | https://github.com/shiyu-coder/Kronos |  |
| 10 | `1jehuang/jcode` | 14232 | 1567 | Rust | 3,107 stars this week | RAM效率最高的线束 | https://github.com/1jehuang/jcode |  |
| 11 | `pingdotgg/t3code` | 15908 | 3516 | TypeScript | 1,402 stars this week | — | https://github.com/pingdotgg/t3code |  |
| 12 | `pascalorg/editor` | 20147 | 2621 | TypeScript | 2,433 stars this week | 创建和共享3D建筑项目。 | https://github.com/pascalorg/editor | 新增 |
| 13 | `tokio-rs/topcoat` | 3948 | 132 | Rust | 1,263 stars this week | 用于构建Web应用程序的包含电池的框架 | https://github.com/tokio-rs/topcoat | 新增 |
| 14 | `CoreBunch/Instatic` | 6810 | 599 | TypeScript | 2,872 stars this week | Webflow、Framer和WordPress的开源替代品。Agentic自托管可视化CMS输出干净的静态页面。用户、角色、插件、内容、数据库，应有尽有。 | https://github.com/CoreBunch/Instatic |  |
| 15 | `UditAkhourii/adhd` | 2888 | 219 | TypeScript | 791 stars this week | ADHD —编码药剂的技能。基于Claude &amp; Codex Agent SDK构建的具有修剪功能的思考树。在不同的认知框架、分数、修剪陷阱下扇出平行发散的思想，加深幸存者。创造性和跨学科的轻松技能…… | https://github.com/UditAkhourii/adhd |  |
| 16 | `virgiliojr94/book-to-skill` | 13744 | 1494 | Python | 4,135 stars this week | 将任何技术书籍PDF转化为Claude Code技能—随时准备在您工作时进行学习、参考和使用。 | https://github.com/virgiliojr94/book-to-skill | 新增 |
| 17 | `Pumpkin-MC/Pumpkin` | 10439 | 697 | Rust | 1,714 stars this week | 让每个人都能托管快速高效的Minecraft服务器。 | https://github.com/Pumpkin-MC/Pumpkin |  |
| 18 | `earendil-works/pi` | 80960 | 9995 | TypeScript | 4,799 stars this week | AI agent toolkit ：统一LLM API、agent loop、TUI、coding agent CLI | https://github.com/earendil-works/pi |  |
| 19 | `opengeos/GeoLibre` | 4532 | 461 | TypeScript | 2,601 stars this week | 一个轻量级的云原生GIS平台，用于可视化、探索和分析地理空间数据。它在Web浏览器、桌面、移动设备和Jupyter笔记本中运行。 | https://github.com/opengeos/GeoLibre | 新增 |
| 20 | `Automattic/harper` | 14000 | 540 | Rust | 2,026 stars this week | 离线、隐私至上的语法检查器。快速、开源、Rust驱动 | https://github.com/Automattic/harper | 新增 |
| 21 | `moeru-ai/airi` | 45900 | 4526 | TypeScript | 2,815 stars this week | 💖🧸 自我托管，你拥有的Grok Companion ，一个包含外府灵魂的容器，将它们带入我们的世界的网络生活，希望达到Neuro-sama的高度。能够实时语音聊天、Minecraft、Factorio播放。支持Web/macOS/Windows。 | https://github.com/moeru-ai/airi | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `permissionlesstech/bitchat` | 33531 | 5322 | Swift | 7,511 stars this month | 蓝牙网状聊天， IRC共鸣 | https://github.com/permissionlesstech/bitchat |  |
| 2 | `diegosouzapw/OmniRoute` | 35199 | 4538 | TypeScript | 27,274 stars this month | 永不停止编码。免费MIT AI网关：一个端点， 290多个提供商（ 90多个免费） ， 500多个型号— Kimi ， Claude ， GPT ， OpenAI ， Gemini ， GLM ， DeepSeek ， MiniMax。适用于Claude Code、Codex、Cursor、OpenCode、Cline和Copilot。配额感知自动回退， RTK +穴居人压缩保存…… | https://github.com/diegosouzapw/OmniRoute |  |
| 3 | `stablyai/orca` | 33931 | 2370 | TypeScript | 24,858 stars this month | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面、移动和VPS上使用。 | https://github.com/stablyai/orca |  |
| 4 | `usestrix/strix` | 45927 | 4807 | Python | 19,044 stars this month | 开源人工智能渗透测试工具，用于查找和修复应用程序的漏洞。 | https://github.com/usestrix/strix |  |
| 5 | `Zackriya-Solutions/meetily` | 27544 | 2827 | Rust | 14,791 stars this month | 隐私第一，基于Rust构建的人工智能会议助手，具有4倍的Parakeet/Whisper实时转录、扬声器日记和Ollama摘要。100%本地处理。无需云。Meetily （ Meetly Ai - https://meetily.ai ）是首屈一指的自托管、开源Ai会议...... | https://github.com/Zackriya-Solutions/meetily |  |
| 6 | `emilkowalski/skills` | 23008 | 1255 | — | 19,220 stars this month | 设计工程师的技能。 | https://github.com/emilkowalski/skills |  |
| 7 | `Nutlope/hallmark` | 20047 | 990 | CSS | 16,556 stars this month | Claude Code、Cursor和Codex的防AI倾斜设计技能。 | https://github.com/Nutlope/hallmark |  |
| 8 | `asgeirtj/system_prompts_leaks` | 61540 | 10054 | JavaScript | 14,820 stars this month | 从Anthropic - Claude Fable 5、Opus 5、Claude Design、Claude Code中提取系统提示。OpenAI - ChatGPT GPT-5.6-Sol ， Codex。Google - Gemini 3.5 Flash、3.1 Pro、Antigravity。xAI - Grok、Cursor、Copilot、VS Code、Perplexity等。定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 9 | `koala73/worldmonitor` | 77012 | 11477 | TypeScript | 16,358 stars this month | 实时全球智能仪表板。在统一的态势感知界面中进行人工智能驱动的新闻聚合、地缘政治监控和基础设施跟踪 | https://github.com/koala73/worldmonitor |  |
| 10 | `openai/codex-plugin-cc` | 30561 | 2013 | JavaScript | 8,889 stars this month | 使用Claude Code的Codex来查看代码或委派任务。 | https://github.com/openai/codex-plugin-cc |  |
| 11 | `bradautomates/claude-video` | 12930 | 1272 | Python | 10,204 stars this month | 让Claude能够观看任何视频。/观看下载、提取帧、转录，并将所有内容交给Claude。 | https://github.com/bradautomates/claude-video |  |
| 12 | `iOfficeAI/OfficeCLI` | 23595 | 1587 | C# | 15,403 stars this month | OfficeCLI是第一个也是最好的Office套件，专为AI代理读取、编辑和自动化Word、Excel和PowerPoint文件而构建。免费、开源、单一二进制文件，无需安装Office。 | https://github.com/iOfficeAI/OfficeCLI |  |
| 13 | `wonderwhy-er/DesktopCommanderMCP` | 8990 | 1029 | TypeScript | 2,898 stars this month | 这是Claude的MCP服务器，具有终端控制、文件系统搜索和diff文件编辑功能 | https://github.com/wonderwhy-er/DesktopCommanderMCP |  |
| 14 | `huggingface/speech-to-speech` | 8944 | 1098 | Python | 3,496 stars this month | 使用开源模型构建本地语音代理 | https://github.com/huggingface/speech-to-speech |  |
| 15 | `HKUDS/Vibe-Trading` | 28790 | 4649 | Python | 14,101 stars this month | “Vibe-Trading ：您的个人交易代理” | https://github.com/HKUDS/Vibe-Trading |  |
| 16 | `OpenCut-app/OpenCut` | 79999 | 7950 | TypeScript | 19,863 stars this month | 开源CapCut替代方案 | https://github.com/OpenCut-app/OpenCut |  |
| 17 | `every-app/open-seo` | 9676 | 1104 | TypeScript | 5,867 stars this month | Semrush和Ahrefs的开源替代品 | https://github.com/every-app/open-seo |  |
| 18 | `Robbyant/lingbot-map` | 15952 | 1695 | Python | 7,577 stars this month | 用于从流数据重建场景的前馈3D基础模型 | https://github.com/Robbyant/lingbot-map |  |
| 19 | `hasaneyldrm/exercises-dataset` | 18146 | 2201 | HTML | 13,734 stars this month | 1,324个运动健身数据集—动画GIF、180 × 180缩略图、肌肉群和设备数据，以及6种语言的分步说明。LogPress应用程序背后的运动数据层。 | https://github.com/hasaneyldrm/exercises-dataset |  |
| 20 | `Shubhamsaboo/awesome-llm-apps` | 129090 | 19046 | Python | 13,402 stars this month | 100多个人工智能代理、代理技能和RAG应用程序-免费开源。 | https://github.com/Shubhamsaboo/awesome-llm-apps | 新增 |
| 21 | `alibaba/page-agent` | 28256 | 2484 | TypeScript | 7,914 stars this month | JavaScript页面内GUI代理。使用自然语言控制Web界面。 | https://github.com/alibaba/page-agent |  |


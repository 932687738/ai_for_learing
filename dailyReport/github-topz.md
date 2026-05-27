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

**最近一次更新时间**（Asia/Shanghai）： 2026-05-27 08:54:03

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 504942 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 470303 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `freeCodeCamp/freeCodeCamp` | 445423 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 4 | `public-apis/public-apis` | 437297 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 5 | `EbookFoundation/free-programming-books` | 389005 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 374874 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `nilbuild/developer-roadmap` | 355499 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 8 | `donnemartin/system-design-primer` | 350420 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 9 | `jwasham/coding-interview-university` | 347446 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `vinta/awesome-python` | 299735 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
| 11 | `awesome-selfhosted/awesome-selfhosted` | 295209 | 可自行部署的各类自由软件网络服务与 Web 应用清单。 | https://github.com/awesome-selfhosted/awesome-selfhosted |  |
| 12 | `practical-tutorials/project-based-learning` | 266609 | 基于项目的教程精选列表 | https://github.com/practical-tutorials/project-based-learning |  |
| 13 | `facebook/react` | 245279 | 用于构建 Web 与原生用户界面的 React 视图库（含多端生态）。 | https://github.com/facebook/react |  |

---
## Trending 页面快照（HTML 抓取）

**说明**：与上方「全局 Star Search」数据源不同；本段按 GitHub trending 页的 **daily / weekly / monthly** 各拉一页并解析。**若前端改版导致选择器失效，需更新解析逻辑。**

- **标记**列：三个 `since` 子表**各自独立**对照本次拉取前文件中该小节表格已出现的 `owner/repo`；新出现的行标 **新增**。下次拉取会先清空上一轮「新增」再重算（只保留相对**上一版文件**的新仓库）。

### 今日 trending（since=daily）

**页面**： `https://github.com/trending?since=daily`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `Lum1104/Understand-Anything` | 35828 | 2877 | TypeScript | 4,697 stars today | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Lum1104/Understand-Anything |  |
| 2 | `affaan-m/ECC` | 194365 | 29966 | JavaScript | 1,915 stars today | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 3 | `rohitg00/ai-engineering-from-scratch` | 20727 | 3451 | Python | 2,155 stars today | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 4 | `anthropics/knowledge-work-plugins` | 16666 | 1952 | Python | 1,718 stars today | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins |  |
| 5 | `mukul975/Anthropic-Cybersecurity-Skills` | 10109 | 1188 | Python | 880 stars today | 人工智能代理的754种结构化网络安全技能·映射到5个框架： MITRE ATT&amp;CK、NIST CSF 2.0、MITRE ATLAS、D3FEND和NIST AI RMF · agentskills.io标准·适用于Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI和20多个平台· 26个安全数据…… | https://github.com/mukul975/Anthropic-Cybersecurity-Skills |  |
| 6 | `hardikpandya/stop-slop` | 5017 | 402 | — | 539 stars today | 从散文中删除AI TELLS的技能文件 | https://github.com/hardikpandya/stop-slop |  |
| 7 | `Leonxlnx/taste-skill` | 21709 | 1741 | Shell | 1,430 stars today | 品味技能-让您的人工智能有良好的品味。阻止人工智能产生无聊的通用斜坡 | https://github.com/Leonxlnx/taste-skill |  |
| 8 | `DigitalPlatDev/FreeDomain` | 167369 | 3084 | HTML | 1,219 stars today | DigitalPlat FreeDomain ：人人免费域名 | https://github.com/DigitalPlatDev/FreeDomain | 新增 |
| 9 | `jellyfin/jellyfin` | 52380 | 4870 | C# | 83 stars today | 自由软件媒体系统-服务器后端和API | https://github.com/jellyfin/jellyfin | 新增 |
| 10 | `Axorax/awesome-free-apps` | 5263 | 268 | JavaScript | 731 stars today | 适用于PC和移动设备的最佳免费应用程序精选列表 | https://github.com/Axorax/awesome-free-apps |  |
| 11 | `twentyhq/twenty` | 46857 | 6652 | TypeScript | 216 stars today | Salesforce的开放式替代方案，专为人工智能而设计。 | https://github.com/twentyhq/twenty | 新增 |
| 12 | `Open-Dev-Society/OpenStock` | 12109 | 1627 | TypeScript | 156 stars today | OpenStock是昂贵市场平台的开源替代品。实时跟踪价格，设置个性化提醒，并探索详细的公司洞察--为每个人公开构建，永远免费。 | https://github.com/Open-Dev-Society/OpenStock | 新增 |
| 13 | `thedotmack/claude-mem` | 78657 | 6768 | TypeScript | 352 stars today | 每个座席跨会话的持久上下文–捕获座席在会话期间执行的所有操作，使用AI对其进行压缩，并将相关上下文注入到未来的会话中。适用于Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode等 | https://github.com/thedotmack/claude-mem | 新增 |
| 14 | `st-tech/ppf-contact-solver` | 3490 | 250 | Python | 170 stars today | 用于涉及👚壳🪵体、固体和🪢棒材的基于物理学的模拟的接触解算器。 | https://github.com/st-tech/ppf-contact-solver | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `colbymchenry/codegraph` | 27729 | 1565 | TypeScript | 21,211 stars this week | Claude Code、Codex、Gemini、Cursor、OpenCode、AntiGravity、Kiro和Hermes Agent的预索引代码知识图—代币更少，工具调用更少， 100%本地化 | https://github.com/colbymchenry/codegraph |  |
| 2 | `Lum1104/Understand-Anything` | 35829 | 2877 | TypeScript | 19,191 stars this week | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Lum1104/Understand-Anything |  |
| 3 | `rohitg00/ai-engineering-from-scratch` | 20727 | 3451 | Python | 11,840 stars this week | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 4 | `tinyhumansai/openhuman` | 28324 | 2636 | Rust | 8,542 stars this week | 您的个人人工智能超级智能。私密、简单且功能强大。 | https://github.com/tinyhumansai/openhuman |  |
| 5 | `Imbad0202/academic-research-skills` | 22158 | 1879 | Python | 8,422 stars this week | Claude Code的学术研究技能：研究→撰写→评审→修订→最终确定 | https://github.com/Imbad0202/academic-research-skills |  |
| 6 | `ruvnet/RuView` | 66326 | 8788 | Rust | 5,986 stars this week | π RuView将商用WiFi信号转化为实时空间智能、生命体征监测和存在检测--所有这些都无需一个像素的视频。 | https://github.com/ruvnet/RuView |  |
| 7 | `HKUDS/ViMax` | 7629 | 1193 | Python | 2,466 stars this week | "ViMax ： Agentic Video Generation （导演、编剧、制片人和视频生成器一体机）" | https://github.com/HKUDS/ViMax | 新增 |
| 8 | `rohitg00/agentmemory` | 18228 | 1504 | TypeScript | 4,444 stars this week | # 1基于真实世界基准的AI编码代理持久内存 | https://github.com/rohitg00/agentmemory |  |
| 9 | `can1357/oh-my-pi` | 7535 | 610 | TypeScript | 2,508 stars this week | 终端的AI编码代理—哈希锚定编辑、优化工具线束、LSP、Python、浏览器、子代理等 | https://github.com/can1357/oh-my-pi |  |
| 10 | `NVlabs/Sana` | 7710 | 592 | Python | 780 stars this week | SANA ：采用线性扩散变压器的高效高分辨率图像合成 | https://github.com/NVlabs/Sana | 新增 |
| 11 | `presenton/presenton` | 7083 | 1174 | TypeScript | 1,981 stars this week | 开源AI演示生成器和API （ Gamma、Beautiful AI、Decktopus Alternative ） | https://github.com/presenton/presenton |  |
| 12 | `humanlayer/12-factor-agents` | 22423 | 1692 | TypeScript | 1,393 stars this week | 我们可以使用哪些原则来构建基于LLM的软件，这些软件实际上足以交付给生产客户？ | https://github.com/humanlayer/12-factor-agents | 新增 |
| 13 | `anthropics/knowledge-work-plugins` | 16666 | 1952 | Python | 4,086 stars this week | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins | 新增 |
| 14 | `supertone-inc/supertonic` | 10644 | 1099 | Swift | 1,944 stars this week | 闪电般的快速、设备上、多语言TTS —通过ONNX本地运行。 | https://github.com/supertone-inc/supertonic |  |
| 15 | `dograh-hq/dograh` | 3262 | 708 | Python | 881 stars this week | 开源语音AI平台。Vapi和Retell的自托管替代品。在PREM上， BYOK跨语音到语音或LLM/STT/TTS ，具有可视化工作流程构建器、MCP本机和电话支持。 | https://github.com/dograh-hq/dograh |  |
| 16 | `HKUDS/CLI-Anything` | 40626 | 3842 | Python | 3,203 stars this week | "CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub: https://clianything.cc/ | https://github.com/HKUDS/CLI-Anything |  |
| 17 | `Chachamaru127/claude-code-harness` | 1690 | 186 | Shell | 704 stars this week | Claude Code Dedicated Development Harness -通过自主计划→工作→审核周期实现高质量发展 | https://github.com/Chachamaru127/claude-code-harness | 新增 |
| 18 | `cursor/plugins` | 911 | 91 | TypeScript | 464 stars this week | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 19 | `dotnet/skills` | 3115 | 228 | C# | 1,292 stars this week | 用于使用.NET和C #协助AI编码代理的技能的存储库 | https://github.com/dotnet/skills | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `colbymchenry/codegraph` | 27729 | 1565 | TypeScript | 26,518 stars this month | Claude Code、Codex、Gemini、Cursor、OpenCode、AntiGravity、Kiro和Hermes Agent的预索引代码知识图—代币更少，工具调用更少， 100%本地化 | https://github.com/colbymchenry/codegraph |  |
| 2 | `mattpocock/skills` | 106912 | 9444 | Shell | 85,195 stars this month | 真正工程师的技能。直接来自我的.claude目录。 | https://github.com/mattpocock/skills |  |
| 3 | `anthropics/financial-services` | 27794 | 3900 | Python | 20,088 stars this month | — | https://github.com/anthropics/financial-services |  |
| 4 | `CloakHQ/CloakBrowser` | 21428 | 1702 | Python | 19,976 stars this month | Stealth Chromium可通过每次机器人检测测试。插入式剧作家更换源级指纹补丁，通过30/30测试 | https://github.com/CloakHQ/CloakBrowser |  |
| 5 | `rohitg00/agentmemory` | 18228 | 1504 | TypeScript | 16,176 stars this month | # 1基于真实世界基准的AI编码代理持久内存 | https://github.com/rohitg00/agentmemory |  |
| 6 | `Imbad0202/academic-research-skills` | 22158 | 1879 | Python | 18,500 stars this month | Claude Code的学术研究技能：研究→撰写→评审→修订→最终确定 | https://github.com/Imbad0202/academic-research-skills |  |
| 7 | `Lum1104/Understand-Anything` | 35830 | 2877 | TypeScript | 25,394 stars this month | 教学图表&gt;令人印象深刻的图表。将任何代码转换为交互式知识图表，您可以对其进行探索、搜索和提出问题。适用于Claude Code、Codex、Cursor、Copilot、Gemini CLI等。 | https://github.com/Lum1104/Understand-Anything |  |
| 8 | `soxoj/maigret` | 30541 | 2181 | Python | 10,987 stars this month | 通过用户名从3000多个网站🕵️‍♂️收集个人档案 | https://github.com/soxoj/maigret |  |
| 9 | `TauricResearch/TradingAgents` | 79835 | 15560 | Python | 27,088 stars this month | TradingAgent ：多代理LLM金融交易框架 | https://github.com/TauricResearch/TradingAgents |  |
| 10 | `multica-ai/andrej-karpathy-skills` | 157139 | 16096 | — | 68,097 stars this month | 一个用于改进Claude Code行为的CLAUDE.md文件，源自Andrej Karpathy对LLM编码陷阱的观察。 | https://github.com/multica-ai/andrej-karpathy-skills |  |
| 11 | `AIDC-AI/Pixelle-Video` | 19965 | 2807 | Python | 13,230 stars this month | 🚀 AI 全自动短视频引擎 · AI Fully Automated Short Video Engine | https://github.com/AIDC-AI/Pixelle-Video |  |
| 12 | `decolua/9router` | 14548 | 2175 | JavaScript | 11,432 stars this month | 无限免费AI编码。通过40多家供应商将Claude Code、Codex、Cursor、Cline、Copilot、Antigravity连接到免费的Claude/GPT/Gemini。自动回退， RTK -40%代币，从未达到限制。 | https://github.com/decolua/9router |  |
| 13 | `ruvnet/ruflo` | 55462 | 6300 | TypeScript | 22,289 stars this month | 🌊 Claude的领先代理编排平台。部署智能多智能体群，协调自主工作流程，构建对话式人工智能系统。具有企业级架构、自学群体智能、RAG集成和本地Claude Code/… | https://github.com/ruvnet/ruflo |  |
| 14 | `rohitg00/ai-engineering-from-scratch` | 20727 | 3451 | Python | 14,997 stars this month | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 15 | `yikart/AiToEarn` | 16644 | 2672 | TypeScript | 7,702 stars this month | 让我们使用人工智能来赚取收入！ | https://github.com/yikart/AiToEarn |  |
| 16 | `bytedance/UI-TARS-desktop` | 35362 | 3555 | TypeScript | 5,915 stars this month | 开源多模态人工智能代理堆栈：连接尖端人工智能模型和代理基础设施 | https://github.com/bytedance/UI-TARS-desktop |  |
| 17 | `ComposioHQ/awesome-codex-skills` | 11886 | 1131 | Python | 10,072 stars this month | 用于跨Codex CLI和API自动化工作流程的实用Codex技能精选列表。 | https://github.com/ComposioHQ/awesome-codex-skills |  |
| 18 | `Alishahryar1/free-claude-code` | 30042 | 4527 | Python | 17,716 stars this month | 在终端中免费使用claude-code、VSCode扩展或像OpenClaw这样的不和谐（支持语音） | https://github.com/Alishahryar1/free-claude-code |  |
| 19 | `LearningCircuit/local-deep-research` | 7999 | 696 | Python | 3,637 stars this month | SimpleQA约95% （例如3090上的Qwen3.6-27B ）。支持所有本地和云LLM （ llama.cpp、Ollama、Google等）。10多个搜索引擎- arXiv、PubMed、您的私人文档。本地和加密的一切。 | https://github.com/LearningCircuit/local-deep-research | 新增 |
| 20 | `mattpocock/sandcastle` | 5165 | 534 | TypeScript | 4,159 stars this month | 使用sandcastle.run ()在TypeScript中编排沙盒编码代理 | https://github.com/mattpocock/sandcastle |  |
| 21 | `addyosmani/agent-skills` | 46080 | 5113 | Shell | 22,719 stars this month | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |


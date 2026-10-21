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

**最近一次更新时间**（Asia/Shanghai）： 2026-10-21 09:34:10

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 554863 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 521960 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 490887 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 457589 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 399684 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 392687 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `donnemartin/system-design-primer` | 374931 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 8 | `nilbuild/developer-roadmap` | 369992 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 9 | `jwasham/coding-interview-university` | 363175 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 11 | `morluto/rea` | 348337 | 使用代理对任何内容进行反向工程，从应用行为到本机二进制文件。 | https://github.com/morluto/rea |  |
| 12 | `vinta/awesome-python` | 328498 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
| 13 | `awesome-selfhosted/awesome-selfhosted` | 326814 | 可自行部署的各类自由软件网络服务与 Web 应用清单。 | https://github.com/awesome-selfhosted/awesome-selfhosted |  |
| 14 | `996icu/996.ICU` | 276361 | 倡议关注「996」工作制、计数星标与交流的开发社区仓库（含网络迷因用语）。 | https://github.com/996icu/996.ICU |  |
| 15 | `practical-tutorials/project-based-learning` | 272563 | 基于项目的教程精选列表 | https://github.com/practical-tutorials/project-based-learning |  |
| 16 | `obra/superpowers` | 246876 | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers |  |
| 17 | `react/react` | 246311 | 用于Web和本机用户界面的库。 | https://github.com/react/react |  |
| 18 | `facebook/react` | 245279 | 用于构建 Web 与原生用户界面的 React 视图库（含多端生态）。 | https://github.com/facebook/react |  |
| 19 | `torvalds/linux` | 238531 | Linux内核源树 | https://github.com/torvalds/linux |  |
| 20 | `vuejs/vue` | 209989 | 这是Vue 2的存储库。如需了解VUE 3 ，请访问https://github.com/vuejs/core | https://github.com/vuejs/vue |  |
| 21 | `n8n-io/n8n` | 195721 | 具有原生AI功能的公平代码工作流程自动化平台。将视觉构建与自定义代码、自托管或云、400多个集成相结合。 | https://github.com/n8n-io/n8n |  |
| 22 | `microsoft/vscode` | 187216 | Visual Studio Code | https://github.com/microsoft/vscode |  |

---
## Trending 页面快照（HTML 抓取）

**说明**：与上方「全局 Star Search」数据源不同；本段按 GitHub trending 页的 **daily / weekly / monthly** 各拉一页并解析。**若前端改版导致选择器失效，需更新解析逻辑。**

- **标记**列：三个 `since` 子表**各自独立**对照本次拉取前文件中该小节表格已出现的 `owner/repo`；新出现的行标 **新增**。下次拉取会先清空上一轮「新增」再重算（只保留相对**上一版文件**的新仓库）。

### 今日 trending（since=daily）

**页面**： `https://github.com/trending?since=daily`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `MadsLorentzen/ai-job-search` | 60673 | 18911 | Python | 3,861 stars today | 在您的机器上运行的作业搜索。基于Claude Code构建的人工智能求职框架：评估帖子、定制简历、撰写求职信、准备面试。分叉并拥有它。 | https://github.com/MadsLorentzen/ai-job-search |  |
| 2 | `cloudflare/security-audit-skill` | 34298 | 2143 | JavaScript | 1,712 stars today | 用于多阶段安全审核的编码代理技能，具有经过独立验证的机器可读结果 | https://github.com/cloudflare/security-audit-skill | 新增 |
| 3 | `stablyai/orca` | 99785 | 6322 | TypeScript | 1,565 stars today | ORCA是与代理团队合作的地方（例如Grok Bot、Claude Code ）。使用您自己的订阅运行任何编码代理。可在桌面、移动和远程运行时使用。 | https://github.com/stablyai/orca |  |
| 4 | `DietrichGebert/ponytail` | 169735 | 9230 | JavaScript | 1,208 stars today | 让你的人工智能代理像房间里最懒惰的高级开发人员一样思考。最好的代码是你从未写过的代码。 | https://github.com/DietrichGebert/ponytail | 新增 |
| 5 | `Comfy-Org/ComfyUI` | 140805 | 16665 | Python | 1,206 stars today | 最强大、模块化的扩散模型GUI、API和后端，具有图形/节点界面。世界上最快的本地推理引擎。 | https://github.com/Comfy-Org/ComfyUI |  |
| 6 | `ruvnet/ruflo` | 77867 | 9161 | TypeScript | 684 stars today | 🌊 原始代理线束。部署智能多玩家群体，协调自主工作流程，构建对话式人工智能系统。具有自适应记忆、自我学习智能、联合、矢量RAG集成、原生Claude Code/Codex/Hermes和许多…… | https://github.com/ruvnet/ruflo |  |
| 7 | `Graphify-Labs/graphify` | 130293 | 12544 | Python | 802 stars today | 将任何代码库及其文档、SQL架构、配置和PDF转换为可查询的知识图。Claude Code、Cursor、Codex和Gemini CLI的A/graphify技能：本地确定性AST解析，解释每个边缘，没有矢量存储。 | https://github.com/Graphify-Labs/graphify | 新增 |
| 8 | `anomalyco/opencode` | 218961 | 29211 | TypeScript | 1,240 stars today | 开源编码代理。 | https://github.com/anomalyco/opencode |  |
| 9 | `msitarzewski/agency-agents` | 162378 | 26230 | Shell | 562 stars today | 一个完整的人工智能机构，触手可及--从前端向导到Reddit社区忍者，从奇思妙想的注入者到现实检查者。每位客服代表都是具有个性、流程和经过验证的交付成果的专家。 | https://github.com/msitarzewski/agency-agents | 新增 |
| 10 | `headroomlabs-ai/headroom` | 76781 | 5960 | Python | 549 stars today | 在工具输出、日志、文件和RAG块到达LLM之前对其进行压缩。编码代理的令牌减少20% ， JSON的令牌减少60-95% ，答案相同。库、代理、MCP服务器。 | https://github.com/headroomlabs-ai/headroom |  |
| 11 | `anthropics/knowledge-work-plugins` | 30806 | 3464 | Python | 267 stars today | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins | 新增 |
| 12 | `wshobson/agents` | 41264 | 4393 | Python | 93 stars today | Claude Code、Codex、Cursor、OpenCode、GitHub Copilot、Google Antigravity和Pi的多线程代理插件市场 | https://github.com/wshobson/agents | 新增 |
| 13 | `sickn33/agentic-awesome-skills` | 48113 | 7021 | Python | 83 stars today | AAS Core是本地、代理优先的控制平面，用于完整的目录发现、代理拥有的选择、堆栈验证和规划，由2,600多种代理技能提供支持。包括CLI、本地MCP、目录、插件和Workbench。 | https://github.com/sickn33/agentic-awesome-skills | 新增 |
| 14 | `shiyu-coder/Kronos` | 42365 | 7014 | Python | 733 stars today | Kronos ：金融市场语言的基础模型 | https://github.com/shiyu-coder/Kronos |  |
| 15 | `vllm-project/vllm` | 94449 | 23675 | Python | 128 stars today | LLM的高吞吐量和内存效率推断和服务引擎 | https://github.com/vllm-project/vllm | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `morluto/rea` | 348337 | 87626 | TypeScript | 157,631 stars this week | 使用代理对任何内容进行反向工程，从应用行为到本机二进制文件。 | https://github.com/morluto/rea |  |
| 2 | `MadsLorentzen/ai-job-search` | 60675 | 18911 | Python | 12,848 stars this week | 在您的机器上运行的作业搜索。基于Claude Code构建的人工智能求职框架：评估帖子、定制简历、撰写求职信、准备面试。分叉并拥有它。 | https://github.com/MadsLorentzen/ai-job-search |  |
| 3 | `anthropics/claude-plugins-official` | 43420 | 4584 | Python | 5,650 stars this week | 由Anthropic管理的高质量Claude Code插件的官方目录。 | https://github.com/anthropics/claude-plugins-official |  |
| 4 | `mksglu/context-mode` | 31371 | 2209 | TypeScript | 3,556 stars this week | 人工智能编码代理的上下文窗口优化。沙盒工具输出（减少98 ％ ） ，保持会话内存，并通过MCP +钩子在17个平台上强制路由。 | https://github.com/mksglu/context-mode |  |
| 5 | `NationalSecurityAgency/ghidra` | 92167 | 10322 | Java | 6,184 stars this week | Ghidra是一个软件逆向工程（ SRE ）框架 | https://github.com/NationalSecurityAgency/ghidra |  |
| 6 | `K-Dense-AI/scientific-agent-skills` | 53274 | 4707 | Python | 4,549 stars this week | 将任何AI特工变成AI科学家。首屈一指的科学代理技能库，全球超过25万名科学家使用。177项随时可用的经验证的技能，以及100多个涵盖生物学、化学、医学和药物发现的科学数据库。兼容Cursor、Claude Code…… | https://github.com/K-Dense-AI/scientific-agent-skills |  |
| 7 | `heygen-com/hyperframes` | 68529 | 6200 | TypeScript | 5,994 stars this week | 编写HTML。渲染视频。专为客服代表打造。 | https://github.com/heygen-com/hyperframes |  |
| 8 | `debpalash/VoiceStudio` | 79021 | 8686 | Python | 17,057 stars this week | VoiceStudio是开源、完全本地的ElevenLabs替代品--语音克隆、语音设计、视频配音、听写、转录和有声读物创作，支持646种语言。 | https://github.com/debpalash/VoiceStudio |  |
| 9 | `ruvnet/ruflo` | 77867 | 9161 | TypeScript | 3,143 stars this week | 🌊 原始代理线束。部署智能多玩家群体，协调自主工作流程，构建对话式人工智能系统。具有自适应记忆、自我学习智能、联合、矢量RAG集成、原生Claude Code/Codex/Hermes和许多…… | https://github.com/ruvnet/ruflo |  |
| 10 | `android/skills` | 9059 | 586 | Kotlin | 1,255 stars this week | — | https://github.com/android/skills | 新增 |
| 11 | `boykopovar/AnyPS5` | 45560 | 4182 | C++ | 11,169 stars this week | 用于自动将PS5可执行文件移植到Linux和Windows的工具 | https://github.com/boykopovar/AnyPS5 |  |
| 12 | `cursor/plugins` | 13250 | 1305 | TypeScript | 2,040 stars this week | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 13 | `cathrynlavery/diagram-design` | 59003 | 3795 | HTML | 5,473 stars this week | Claude Code、Codex、GitHub Copilot、Cursor、Factory Droid和Pi的编辑图设计。44种图类型。独立的HTML + SVG。没有阴影，没有美人鱼粪便。 | https://github.com/cathrynlavery/diagram-design |  |
| 14 | `storytold/artcraft` | 34553 | 5470 | Rust | 10,287 stars this week | ArtCraft是艺术家、设计师和电影制作人的特意制作引擎 | https://github.com/storytold/artcraft |  |
| 15 | `wshobson/agents` | 41264 | 4393 | Python | 665 stars this week | Claude Code、Codex、Cursor、OpenCode、GitHub Copilot、Google Antigravity和Pi的多线程代理插件市场 | https://github.com/wshobson/agents | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `debpalash/VoiceStudio` | 79021 | 8686 | Python | 45,470 stars this month | VoiceStudio是开源、完全本地的ElevenLabs替代品--语音克隆、语音设计、视频配音、听写、转录和有声读物创作，支持646种语言。 | https://github.com/debpalash/VoiceStudio |  |
| 2 | `paperclipai/paperclip` | 105262 | 17529 | TypeScript | 24,372 stars this month | 每个人都使用的开源应用程序来管理工作中的代理 | https://github.com/paperclipai/paperclip |  |
| 3 | `vectorize-io/hindsight` | 52038 | 6189 | Python | 28,261 stars this month | 后见之明：学习的客服代表记忆 | https://github.com/vectorize-io/hindsight |  |
| 4 | `heygen-com/hyperframes` | 68529 | 6200 | TypeScript | 16,644 stars this month | 编写HTML。渲染视频。专为客服代表打造。 | https://github.com/heygen-com/hyperframes |  |
| 5 | `anthropics/financial-services` | 40559 | 5665 | Python | 5,457 stars this month | — | https://github.com/anthropics/financial-services |  |
| 6 | `cloudflare/security-audit-skill` | 34299 | 2144 | JavaScript | 15,824 stars this month | 用于多阶段安全审核的编码代理技能，具有经过独立验证的机器可读结果 | https://github.com/cloudflare/security-audit-skill |  |
| 7 | `mksglu/context-mode` | 31371 | 2209 | TypeScript | 7,699 stars this month | 人工智能编码代理的上下文窗口优化。沙盒工具输出（减少98 ％ ） ，保持会话内存，并通过MCP +钩子在17个平台上强制路由。 | https://github.com/mksglu/context-mode |  |
| 8 | `NVIDIA/OpenShell` | 16826 | 1790 | Rust | 8,173 stars this month | OpenShell是自主AI代理的安全、私有运行时。 | https://github.com/NVIDIA/OpenShell |  |
| 9 | `anthropics/knowledge-work-plugins` | 30806 | 3464 | Python | 5,496 stars this month | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins |  |
| 10 | `NationalSecurityAgency/ghidra` | 92167 | 10322 | Java | 13,031 stars this month | Ghidra是一个软件逆向工程（ SRE ）框架 | https://github.com/NationalSecurityAgency/ghidra |  |
| 11 | `anthropics/claude-plugins-official` | 43420 | 4584 | Python | 6,997 stars this month | 由Anthropic管理的高质量Claude Code插件的官方目录。 | https://github.com/anthropics/claude-plugins-official |  |
| 12 | `tashfeenahmed/freellmapi` | 38351 | 5172 | TypeScript | 10,683 stars this month | 每月74亿个代币。34个免费LLM提供商。635个免费模型端点。全部在一个/v1端点后面，加上任何与OpenAI兼容的自定义端点。智能路由、自动故障转移、加密密钥。仅限个人实验。 | https://github.com/tashfeenahmed/freellmapi |  |
| 13 | `cursor/plugins` | 13250 | 1305 | TypeScript | 5,033 stars this month | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 14 | `rohitg00/ai-engineering-from-scratch` | 71800 | 12634 | Python | 16,986 stars this month | 学习人工智能工程！学习它。建造它。为别人运送它。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 15 | `affaan-m/ECC` | 284932 | 42278 | JavaScript | 22,836 stars this month | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 16 | `agent-substrate/substrate` | 5674 | 613 | Go | 3,659 stars this month | Agent Substrate ：核心系统 | https://github.com/agent-substrate/substrate |  |
| 17 | `TencentCloud/Octop` | 10473 | 1309 | Python | 6,143 stars this month | 更智能、自托管的人工智能助手—多用户、多代理。 | https://github.com/TencentCloud/Octop |  |
| 18 | `earthtojake/text-to-cad` | 21996 | 2160 | Python | 5,836 stars this month | 为您的代理商提供CAD超能力。 | https://github.com/earthtojake/text-to-cad |  |
| 19 | `HKUDS/CLI-Anything` | 55680 | 5020 | Python | 6,135 stars this month | "CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub: https://clianything.cc/ | https://github.com/HKUDS/CLI-Anything |  |
| 20 | `pingdotgg/t3code` | 28872 | 7756 | TypeScript | 5,793 stars this month | — | https://github.com/pingdotgg/t3code | 新增 |
| 21 | `VectifyAI/PageIndex` | 39379 | 3420 | Python | 3,715 stars this month | 📑 PageIndex ：无矢量、基于推理的RAG的文档索引 | https://github.com/VectifyAI/PageIndex | 新增 |
| 22 | `pbakaus/impeccable` | 83863 | 5025 | Rust | 14,636 stars this month | 让您的人工智能更好地进行设计的设计语言。 | https://github.com/pbakaus/impeccable |  |


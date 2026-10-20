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

**最近一次更新时间**（Asia/Shanghai）： 2026-10-20 10:47:24

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 554620 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 521513 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 490557 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 457536 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 399604 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 392747 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `donnemartin/system-design-primer` | 374809 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 8 | `nilbuild/developer-roadmap` | 369915 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 9 | `jwasham/coding-interview-university` | 363105 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 11 | `morluto/rea` | 337847 | Reverse engineer anything with agents, from app behavior down to native binaries. | https://github.com/morluto/rea | 新增 |
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
| 1 | `MadsLorentzen/ai-job-search` | 57581 | 18267 | Python | 3,856 stars today | The job search that runs on your machine. AI job application framework built on Claude Code: evaluate postings, tailor CVs, write cover letters, prep interviews. Fork it and own it. | https://github.com/MadsLorentzen/ai-job-search |  |
| 2 | `anomalyco/opencode` | 217915 | 29124 | TypeScript | 1,311 stars today | The open source coding agent. | https://github.com/anomalyco/opencode |  |
| 3 | `akitaonrails/ai-memory` | 11427 | 812 | Rust | 666 stars today | Solution for long term memory for agent coding CLIs and to facilitate handoff between different agent vendors | https://github.com/akitaonrails/ai-memory |  |
| 4 | `Comfy-Org/ComfyUI` | 139831 | 16592 | Python | 1,011 stars today | The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface. The fastest local inference engine in the world. | https://github.com/Comfy-Org/ComfyUI |  |
| 5 | `ruvnet/ruflo` | 77262 | 9107 | TypeScript | 564 stars today | 🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many… | https://github.com/ruvnet/ruflo |  |
| 6 | `stablyai/orca` | 98402 | 6278 | TypeScript | 1,590 stars today | Orca is the place for working with a fleet of agents (e.g. Grok Bot, Claude Code). Run any coding agent with your own subscription. Available on desktop, mobile and remote runtime. | https://github.com/stablyai/orca |  |
| 7 | `headroomlabs-ai/headroom` | 76292 | 5924 | Python | 310 stars today | Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server. | https://github.com/headroomlabs-ai/headroom | 新增 |
| 8 | `withmarbleapp/os-taxonomy` | 6190 | 1013 | JavaScript | 284 stars today | — | https://github.com/withmarbleapp/os-taxonomy | 新增 |
| 9 | `Kruk2/jasna` | 2953 | 214 | Python | 498 stars today | Video restoration tool | https://github.com/Kruk2/jasna |  |
| 10 | `HKUDS/CLI-Anything` | 55301 | 4989 | Python | 606 stars today | "CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub: https://clianything.cc/ | https://github.com/HKUDS/CLI-Anything |  |
| 11 | `anthropics/claude-code` | 152688 | 27146 | TypeScript | 167 stars today | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. | https://github.com/anthropics/claude-code | 新增 |
| 12 | `shiyu-coder/Kronos` | 41740 | 6932 | Python | 363 stars today | Kronos: A Foundation Model for the Language of Financial Markets | https://github.com/shiyu-coder/Kronos | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `morluto/rea` | 337851 | 85307 | TypeScript | 201,065 stars this week | Reverse engineer anything with agents, from app behavior down to native binaries. | https://github.com/morluto/rea |  |
| 2 | `anthropics/claude-plugins-official` | 43200 | 4572 | Python | 5,441 stars this week | Official, Anthropic-managed directory of high quality Claude Code Plugins. | https://github.com/anthropics/claude-plugins-official |  |
| 3 | `storytold/artcraft` | 33804 | 5351 | Rust | 13,572 stars this week | ArtCraft is an intentional crafting engine for artists, designers, and filmmakers | https://github.com/storytold/artcraft |  |
| 4 | `MadsLorentzen/ai-job-search` | 57581 | 18267 | Python | 9,073 stars this week | The job search that runs on your machine. AI job application framework built on Claude Code: evaluate postings, tailor CVs, write cover letters, prep interviews. Fork it and own it. | https://github.com/MadsLorentzen/ai-job-search |  |
| 5 | `boykopovar/AnyPS5` | 44571 | 4072 | C++ | 12,389 stars this week | Tool for automatic PS5 executables porting to Linux and Windows | https://github.com/boykopovar/AnyPS5 |  |
| 6 | `NationalSecurityAgency/ghidra` | 91642 | 10269 | Java | 7,152 stars this week | Ghidra is a software reverse engineering (SRE) framework | https://github.com/NationalSecurityAgency/ghidra |  |
| 7 | `mksglu/context-mode` | 31111 | 2336 | TypeScript | 4,224 stars this week | Context window optimization for AI coding agents. Sandboxes tool output (98% reduction), persists session memory, and enforces routing across 17 platforms via MCP + hooks. | https://github.com/mksglu/context-mode |  |
| 8 | `heygen-com/hyperframes` | 67733 | 6123 | TypeScript | 5,945 stars this week | Write HTML. Render video. Built for agents. | https://github.com/heygen-com/hyperframes |  |
| 9 | `cathrynlavery/diagram-design` | 58493 | 3757 | HTML | 6,638 stars this week | Editorial diagram design for Claude Code, Codex, GitHub Copilot, Cursor, Factory Droid, and Pi. 44 diagram types. Self-contained HTML + SVG. No shadows. No Mermaid slop. | https://github.com/cathrynlavery/diagram-design |  |
| 10 | `K-Dense-AI/scientific-agent-skills` | 52962 | 4688 | Python | 4,355 stars this week | Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by 250,000+ scientists worldwide. 177 ready-to-use validated skills plus 100+ scientific databases covering biology, chemistry, medicine, and drug discovery. Compatible with Cursor, Claude Code… | https://github.com/K-Dense-AI/scientific-agent-skills | 新增 |
| 11 | `cursor/plugins` | 13071 | 1283 | TypeScript | 1,975 stars this week | Cursor plugin specification and official plugins | https://github.com/cursor/plugins |  |
| 12 | `debpalash/VoiceStudio` | 77643 | 8509 | Python | 17,291 stars this week | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voice design, video dubbing, dictation, transcription &amp; audiobook creation in 646 languages. | https://github.com/debpalash/VoiceStudio | 新增 |
| 13 | `YuJunZhiXue/dsh-purge` | 9202 | 1666 | JavaScript | 2,933 stars this week | DeepSeek Harness 破甲：让所有模型都能破甲，不同模型可换不同提示词；默认提示词面向国模「小码酱」。Jailbreak for every model — swap prompts per model. 求 Star 收藏 ⭐ 如要二开，请查看署名要求部分 | https://github.com/YuJunZhiXue/dsh-purge | 新增 |
| 14 | `ruvnet/ruflo` | 77262 | 9107 | TypeScript | 2,543 stars this week | 🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many… | https://github.com/ruvnet/ruflo | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `paperclipai/paperclip` | 104792 | 17469 | TypeScript | 23,845 stars this month | The open-source app everyone uses to manage agents at work | https://github.com/paperclipai/paperclip |  |
| 2 | `debpalash/VoiceStudio` | 77643 | 8509 | Python | 44,161 stars this month | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voice design, video dubbing, dictation, transcription &amp; audiobook creation in 646 languages. | https://github.com/debpalash/VoiceStudio |  |
| 3 | `heygen-com/hyperframes` | 67733 | 6123 | TypeScript | 16,049 stars this month | Write HTML. Render video. Built for agents. | https://github.com/heygen-com/hyperframes |  |
| 4 | `vectorize-io/hindsight` | 51700 | 6172 | Python | 27,932 stars this month | Hindsight: Agent Memory That Learns | https://github.com/vectorize-io/hindsight |  |
| 5 | `anthropics/financial-services` | 40442 | 5658 | Python | 5,573 stars this month | — | https://github.com/anthropics/financial-services |  |
| 6 | `cloudflare/security-audit-skill` | 32616 | 2040 | JavaScript | 16,536 stars this month | A coding-agent skill for multi-phase security audits with independently verified, machine-readable findings | https://github.com/cloudflare/security-audit-skill |  |
| 7 | `mksglu/context-mode` | 31111 | 2336 | TypeScript | 7,498 stars this month | Context window optimization for AI coding agents. Sandboxes tool output (98% reduction), persists session memory, and enforces routing across 17 platforms via MCP + hooks. | https://github.com/mksglu/context-mode |  |
| 8 | `NVIDIA/OpenShell` | 16726 | 1819 | Rust | 8,061 stars this month | OpenShell is the safe, private runtime for autonomous AI agents. | https://github.com/NVIDIA/OpenShell |  |
| 9 | `agent-substrate/substrate` | 5608 | 607 | Go | 3,612 stars this month | Agent Substrate: the core system | https://github.com/agent-substrate/substrate |  |
| 10 | `tashfeenahmed/freellmapi` | 37701 | 5086 | TypeScript | 10,330 stars this month | 7.4 billion tokens per month. 34 free LLM providers. 635 free model endpoints. All behind one /v1 endpoint, plus any custom OpenAI-compatible endpoint. Smart routing, automatic failover, encrypted keys. Personal experimentation only. | https://github.com/tashfeenahmed/freellmapi |  |
| 11 | `anthropics/knowledge-work-plugins` | 30525 | 3444 | Python | 5,489 stars this month | Open source repository of plugins primarily intended for knowledge workers to use in Claude Cowork | https://github.com/anthropics/knowledge-work-plugins |  |
| 12 | `affaan-m/ECC` | 284191 | 42213 | JavaScript | 22,807 stars this month | The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond. | https://github.com/affaan-m/ECC |  |
| 13 | `cursor/plugins` | 13071 | 1283 | TypeScript | 4,862 stars this month | Cursor plugin specification and official plugins | https://github.com/cursor/plugins |  |
| 14 | `NationalSecurityAgency/ghidra` | 91642 | 10269 | Java | 12,523 stars this month | Ghidra is a software reverse engineering (SRE) framework | https://github.com/NationalSecurityAgency/ghidra |  |
| 15 | `anthropics/claude-plugins-official` | 43200 | 4572 | Python | 6,772 stars this month | Official, Anthropic-managed directory of high quality Claude Code Plugins. | https://github.com/anthropics/claude-plugins-official |  |
| 16 | `rohitg00/ai-engineering-from-scratch` | 71471 | 12572 | Python | 16,662 stars this month | Learn AI Engineering! Learn it. Build it. Ship it for others. | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 17 | `TencentCloud/Octop` | 10312 | 1306 | Python | 6,077 stars this month | A smarter, self-hosted AI assistant — multi-user, multi-agent. | https://github.com/TencentCloud/Octop |  |
| 18 | `earthtojake/text-to-cad` | 21764 | 2144 | Python | 5,595 stars this month | Give your agent CAD superpowers. | https://github.com/earthtojake/text-to-cad | 新增 |
| 19 | `HKUDS/CLI-Anything` | 55301 | 4989 | Python | 5,545 stars this month | "CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub: https://clianything.cc/ | https://github.com/HKUDS/CLI-Anything | 新增 |
| 20 | `pbakaus/impeccable` | 83279 | 5038 | Rust | 14,255 stars this month | The design language that makes your AI harness better at design. | https://github.com/pbakaus/impeccable | 新增 |
| 21 | `longbridge/gpui-kit` | 18348 | 1112 | Rust | 3,797 stars this month | Rust GUI components for building fantastic cross-platform desktop application by using GPUI. | https://github.com/longbridge/gpui-kit |  |


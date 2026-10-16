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

**最近一次更新时间**（Asia/Shanghai）： 2026-10-16 09:26:11

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 553479 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 519521 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 489139 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 457124 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 399142 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 392130 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `donnemartin/system-design-primer` | 374350 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 8 | `nilbuild/developer-roadmap` | 369496 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 9 | `jwasham/coding-interview-university` | 362546 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 11 | `vinta/awesome-python` | 327704 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
| 12 | `awesome-selfhosted/awesome-selfhosted` | 326814 | 可自行部署的各类自由软件网络服务与 Web 应用清单。 | https://github.com/awesome-selfhosted/awesome-selfhosted |  |
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
| 1 | `morluto/rea` | 270918 | 68023 | TypeScript | 32,314 stars today | 使用代理对任何内容进行反向工程，从应用行为到本机二进制文件。 | https://github.com/morluto/rea |  |
| 2 | `anthropics/claude-plugins-official` | 39130 | 4325 | Python | 307 stars today | 由Anthropic管理的高质量Claude Code插件的官方目录。 | https://github.com/anthropics/claude-plugins-official |  |
| 3 | `K-Dense-AI/scientific-agent-skills` | 50498 | 4489 | Python | 1,091 stars today | 将任何AI特工变成AI科学家。首屈一指的科学代理技能库，全球超过25万名科学家使用。177项随时可用的经验证的技能，以及100多个涵盖生物学、化学、医学和药物发现的科学数据库。兼容Cursor、Claude Code…… | https://github.com/K-Dense-AI/scientific-agent-skills |  |
| 4 | `JuliusBrussee/caveman` | 112575 | 6521 | Go | 433 stars today | 🪨 为什么在很少令牌做恶作剧时使用许多令牌。病毒技能+编码代理的代理，通过像穴居人一样说话来削减65%的代币。 | https://github.com/JuliusBrussee/caveman |  |
| 5 | `debpalash/VoiceStudio` | 69147 | 7567 | Python | 3,024 stars today | VoiceStudio是开源、完全本地的ElevenLabs替代品--语音克隆、语音设计、视频配音、听写、转录和有声读物创作，支持646种语言。 | https://github.com/debpalash/VoiceStudio |  |
| 6 | `obra/superpowers` | 299916 | 26785 | Shell | 582 stars today | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers |  |
| 7 | `ruvnet/ruflo` | 75142 | 8928 | TypeScript | 147 stars today | 🌊 原始代理线束。部署智能多玩家群体，协调自主工作流程，构建对话式人工智能系统。具有自适应记忆、自我学习智能、联合、矢量RAG集成、原生Claude Code/Codex/Hermes和许多…… | https://github.com/ruvnet/ruflo |  |
| 8 | `mksglu/context-mode` | 29803 | 2083 | TypeScript | 904 stars today | 人工智能编码代理的上下文窗口优化。沙盒工具输出（减少98 ％ ） ，保持会话内存，并通过MCP +钩子在17个平台上强制路由。 | https://github.com/mksglu/context-mode |  |
| 9 | `NationalSecurityAgency/ghidra` | 88788 | 9904 | Java | 1,369 stars today | Ghidra是一个软件逆向工程（ SRE ）框架 | https://github.com/NationalSecurityAgency/ghidra |  |
| 10 | `affaan-m/ECC` | 280418 | 41706 | JavaScript | 1,013 stars today | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 11 | `lightseekorg/tokenspeed` | 2496 | 336 | Python | 30 stars today | TokenSpeed是一款光速LLM推理引擎。 | https://github.com/lightseekorg/tokenspeed |  |
| 12 | `xerj-org/xerj` | 5682 | 308 | Rust | 715 stars today | XERJ是人工智能搜索数据的新方式。其自动索引功能可激活代理了解您的数据，而无需浪费grep和sed的代币。一个命令索引代码、文档、日志和PDF ，用于搜索、RAG、安全审核和代理内存，使用的令牌比grep少40倍。其他…… | https://github.com/xerj-org/xerj |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `morluto/rea` | 270923 | 68026 | TypeScript | 239,477 stars this week | 使用代理对任何内容进行反向工程，从应用行为到本机二进制文件。 | https://github.com/morluto/rea |  |
| 2 | `boykopovar/AnyPS5` | 38709 | 3445 | C++ | 25,174 stars this week | 用于自动将PS5可执行文件移植到Linux和Windows的工具 | https://github.com/boykopovar/AnyPS5 |  |
| 3 | `mattpocock/skills` | 292887 | 24554 | Shell | 12,147 stars this week | 真正工程师的技能。直接来自我的.agents目录。 | https://github.com/mattpocock/skills |  |
| 4 | `heygen-com/hyperframes` | 64581 | 5801 | TypeScript | 5,318 stars this week | 编写HTML。渲染视频。专为客服代表打造。 | https://github.com/heygen-com/hyperframes |  |
| 5 | `cathrynlavery/diagram-design` | 55938 | 3536 | HTML | 10,237 stars this week | Claude Code、Codex、GitHub Copilot、Cursor、Factory Droid和Pi的编辑图设计。44种图类型。独立的HTML + SVG。没有阴影，没有美人鱼粪便。 | https://github.com/cathrynlavery/diagram-design |  |
| 6 | `NationalSecurityAgency/ghidra` | 88788 | 9904 | Java | 6,614 stars this week | Ghidra是一个软件逆向工程（ SRE ）框架 | https://github.com/NationalSecurityAgency/ghidra |  |
| 7 | `ranxianglei/billion-context` | 1386 | 116 | TypeScript | 659 stars this week | A context-compression plugin for small context windows (a 100K context is enough), token savings (5x fewer tokens), and month-long single sessions (billions of tokens).上下文压缩插件，兼顾小窗口(100k上下文足矣)省token(省5倍token)和超长会话(数月级别几十亿token单会话)。billion-context is all you need | https://github.com/ranxianglei/billion-context |  |
| 8 | `earthtojake/text-to-cad` | 20718 | 2050 | Python | 2,244 stars this week | 为您的代理商提供CAD超能力。 | https://github.com/earthtojake/text-to-cad |  |
| 9 | `twostraws/SwiftUI-Agent-Skill` | 6098 | 221 | — | 900 stars this week | 适用于Claude Code、Codex和其他AI工具的SwiftUI代理技能。 | https://github.com/twostraws/SwiftUI-Agent-Skill |  |
| 10 | `DuarteSantos8/openGym` | 12365 | 1515 | JavaScript | 4,471 stars this week | 自我托管的健身房和体重跟踪器—计划例行公事、日志锻炼（超组、热身、有氧运动）、查看哪些肌肉经过训练、疲劳或脱锻、从FitNotes/Strong/Hevy导入、密钥登录。您的数据，您的服务器。 | https://github.com/DuarteSantos8/openGym |  |
| 11 | `cursor/plugins` | 11648 | 1136 | TypeScript | 1,214 stars this week | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `paperclipai/paperclip` | 102739 | 17207 | TypeScript | 22,181 stars this month | 每个人都使用的开源应用程序来管理工作中的代理 | https://github.com/paperclipai/paperclip |  |
| 2 | `anthropics/financial-services` | 40008 | 5621 | Python | 5,252 stars this month | — | https://github.com/anthropics/financial-services |  |
| 3 | `vectorize-io/hindsight` | 50070 | 6085 | Python | 26,652 stars this month | 后见之明：学习的客服代表记忆 | https://github.com/vectorize-io/hindsight |  |
| 4 | `debpalash/VoiceStudio` | 69147 | 7567 | Python | 38,181 stars this month | VoiceStudio是开源、完全本地的ElevenLabs替代品--语音克隆、语音设计、视频配音、听写、转录和有声读物创作，支持646种语言。 | https://github.com/debpalash/VoiceStudio |  |
| 5 | `heygen-com/hyperframes` | 64581 | 5801 | TypeScript | 14,246 stars this month | 编写HTML。渲染视频。专为客服代表打造。 | https://github.com/heygen-com/hyperframes |  |
| 6 | `affaan-m/ECC` | 280418 | 41706 | JavaScript | 22,953 stars this month | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 7 | `anthropics/knowledge-work-plugins` | 29803 | 3370 | Python | 5,835 stars this month | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins |  |
| 8 | `agent-substrate/substrate` | 5234 | 578 | Go | 3,368 stars this month | Agent Substrate ：核心系统 | https://github.com/agent-substrate/substrate |  |
| 9 | `alibaba/open-code-review` | 47392 | 3450 | Go | 20,351 stars this month | 安全、快速、高效，经受住阿里巴巴规模的考验。混合架构代码审核工具：确定性流水线+ LLM Agent、精确的行级注释、内置多语言规则集（ NPE、线程安全、XSS、SQL注入）、OpenAI &amp; Anthropic兼容。 | https://github.com/alibaba/open-code-review |  |
| 10 | `NVIDIA/OpenShell` | 16349 | 1795 | Rust | 7,813 stars this month | OpenShell是自主AI代理的安全、私有运行时。 | https://github.com/NVIDIA/OpenShell |  |
| 11 | `TencentCloud/Octop` | 9550 | 1188 | Python | 7,082 stars this month | 更智能、自托管的人工智能助手—多用户、多代理。 | https://github.com/TencentCloud/Octop |  |
| 12 | `mksglu/context-mode` | 29803 | 2083 | TypeScript | 6,744 stars this month | 人工智能编码代理的上下文窗口优化。沙盒工具输出（减少98 ％ ） ，保持会话内存，并通过MCP +钩子在17个平台上强制路由。 | https://github.com/mksglu/context-mode |  |
| 13 | `tashfeenahmed/freellmapi` | 35794 | 4834 | TypeScript | 9,499 stars this month | 每月74亿个代币。34个免费LLM提供商。635个免费模型端点。全部在一个/v1端点后面，加上任何与OpenAI兼容的自定义端点。智能路由、自动故障转移、加密密钥。仅限个人实验。 | https://github.com/tashfeenahmed/freellmapi |  |
| 14 | `Tencent/WeKnora` | 34219 | 4562 | Go | 10,698 stars this month | 开源LLM知识平台：将原始文档转化为可查询的RAG、自主推理代理和自我维护的Wiki。 | https://github.com/Tencent/WeKnora |  |
| 15 | `trycua/cua` | 29875 | 2141 | Rust | 7,322 stars this month | 通过开源驱动程序、跨操作系统车队以及培训、评估和数据生成的基准来扩展计算机使用2.0。 | https://github.com/trycua/cua |  |
| 16 | `addyosmani/agent-skills` | 107055 | 11132 | JavaScript | 13,095 stars this month | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 17 | `anthropics/claude-code` | 151074 | 26689 | TypeScript | 6,760 stars this month | Claude Code是一个代理编码工具，它位于您的终端中，了解您的代码库，并通过执行日常任务、解释复杂代码和处理git工作流程（所有这些都通过自然语言命令）来帮助您更快地进行编码。 | https://github.com/anthropics/claude-code |  |
| 18 | `NationalSecurityAgency/ghidra` | 88789 | 9904 | Java | 12,092 stars this month | Ghidra是一个软件逆向工程（ SRE ）框架 | https://github.com/NationalSecurityAgency/ghidra |  |
| 19 | `rohitg00/ai-engineering-from-scratch` | 69791 | 12259 | Python | 15,242 stars this month | 学习人工智能工程！学习它。建造它。为别人运送它。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 20 | `cursor/plugins` | 11648 | 1136 | TypeScript | 3,928 stars this month | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 21 | `longbridge/gpui-kit` | 17629 | 1074 | Rust | 3,233 stars this month | 使用GPUI构建梦幻般的跨平台桌面应用程序的Rust GUI组件。 | https://github.com/longbridge/gpui-kit |  |
| 22 | `thedotmack/claude-mem` | 101064 | 8844 | TypeScript | 7,470 stars this month | 每个座席跨会话的持久上下文–捕获座席在会话期间执行的所有操作，使用AI对其进行压缩，并将相关上下文注入到未来的会话中。适用于Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode等 | https://github.com/thedotmack/claude-mem |  |


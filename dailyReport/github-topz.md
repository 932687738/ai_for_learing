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

**最近一次更新时间**（Asia/Shanghai）： 2026-10-19 09:17:10

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 554346 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 520990 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 490108 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 457443 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 399483 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 392401 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `donnemartin/system-design-primer` | 374657 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 8 | `nilbuild/developer-roadmap` | 369802 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 9 | `jwasham/coding-interview-university` | 362834 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 11 | `vinta/awesome-python` | 328498 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `MadsLorentzen/ai-job-search` | 53258 | 17396 | Python | 2,232 stars today | 在您的机器上运行的作业搜索。基于Claude Code构建的人工智能求职框架：评估帖子、定制简历、撰写求职信、准备面试。分叉并拥有它。 | https://github.com/MadsLorentzen/ai-job-search | 新增 |
| 2 | `anthropics/claude-plugins-official` | 42708 | 4535 | Python | 1,175 stars today | 由Anthropic管理的高质量Claude Code插件的官方目录。 | https://github.com/anthropics/claude-plugins-official |  |
| 3 | `anomalyco/opencode` | 216618 | 29003 | TypeScript | 1,414 stars today | 开源编码代理。 | https://github.com/anomalyco/opencode | 新增 |
| 4 | `cursor/plugins` | 12751 | 1256 | TypeScript | 350 stars today | 光标插件规范和官方插件 | https://github.com/cursor/plugins | 新增 |
| 5 | `ruvnet/ruflo` | 76527 | 9050 | TypeScript | 513 stars today | 🌊 原始代理线束。部署智能多玩家群体，协调自主工作流程，构建对话式人工智能系统。具有自适应记忆、自我学习智能、联合、矢量RAG集成、原生Claude Code/Codex/Hermes和许多…… | https://github.com/ruvnet/ruflo |  |
| 6 | `akitaonrails/ai-memory` | 10500 | 749 | Rust | 512 stars today | 针对座席编码CLI的长期记忆解决方案，以及促进不同座席供应商之间切换的解决方案 | https://github.com/akitaonrails/ai-memory | 新增 |
| 7 | `stablyai/orca` | 96680 | 6177 | TypeScript | 1,146 stars today | ORCA是与代理团队合作的地方（例如Grok Bot、Claude Code ）。使用您自己的订阅运行任何编码代理。可在桌面、移动和远程运行时使用。 | https://github.com/stablyai/orca | 新增 |
| 8 | `HKUDS/CLI-Anything` | 54598 | 4948 | Python | 589 stars today | "CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub: https://clianything.cc/ | https://github.com/HKUDS/CLI-Anything | 新增 |
| 9 | `debpalash/VoiceStudio` | 75420 | 8257 | Python | 2,082 stars today | VoiceStudio是开源、完全本地的ElevenLabs替代品--语音克隆、语音设计、视频配音、听写、转录和有声读物创作，支持646种语言。 | https://github.com/debpalash/VoiceStudio |  |
| 10 | `android/skills` | 8778 | 568 | Kotlin | 375 stars today | — | https://github.com/android/skills | 新增 |
| 11 | `mlabonne/llm-course` | 84042 | 9784 | — | 81 stars today | 通过路线图和Colab笔记本进入大型语言模型（ LLM ）的课程。 | https://github.com/mlabonne/llm-course | 新增 |
| 12 | `Kruk2/jasna` | 2412 | 187 | Python | 115 stars today | 视频还原工具 | https://github.com/Kruk2/jasna | 新增 |
| 13 | `Comfy-Org/ComfyUI` | 138627 | 16503 | Python | 154 stars today | 最强大、模块化的扩散模型GUI、API和后端，具有图形/节点界面。世界上最快的本地推理引擎。 | https://github.com/Comfy-Org/ComfyUI | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `morluto/rea` | 322542 | 81728 | TypeScript | 229,268 stars this week | 使用代理对任何内容进行反向工程，从应用行为到本机二进制文件。 | https://github.com/morluto/rea |  |
| 2 | `storytold/artcraft` | 32749 | 5188 | Rust | 16,379 stars this week | ArtCraft是艺术家、设计师和电影制作人的特意制作引擎 | https://github.com/storytold/artcraft | 新增 |
| 3 | `boykopovar/AnyPS5` | 43231 | 3922 | C++ | 14,224 stars this week | 用于自动将PS5可执行文件移植到Linux和Windows的工具 | https://github.com/boykopovar/AnyPS5 |  |
| 4 | `anthropics/claude-plugins-official` | 42708 | 4535 | Python | 4,774 stars this week | 由Anthropic管理的高质量Claude Code插件的官方目录。 | https://github.com/anthropics/claude-plugins-official | 新增 |
| 5 | `mksglu/context-mode` | 30763 | 2278 | TypeScript | 4,138 stars this week | 人工智能编码代理的上下文窗口优化。沙盒工具输出（减少98 ％ ） ，保持会话内存，并通过MCP +钩子在17个平台上强制路由。 | https://github.com/mksglu/context-mode | 新增 |
| 6 | `cathrynlavery/diagram-design` | 57711 | 3695 | HTML | 7,901 stars this week | Claude Code、Codex、GitHub Copilot、Cursor、Factory Droid和Pi的编辑图设计。44种图类型。独立的HTML + SVG。没有阴影，没有美人鱼粪便。 | https://github.com/cathrynlavery/diagram-design |  |
| 7 | `NationalSecurityAgency/ghidra` | 90916 | 10180 | Java | 7,602 stars this week | Ghidra是一个软件逆向工程（ SRE ）框架 | https://github.com/NationalSecurityAgency/ghidra |  |
| 8 | `heygen-com/hyperframes` | 66756 | 6056 | TypeScript | 5,883 stars this week | 编写HTML。渲染视频。专为客服代表打造。 | https://github.com/heygen-com/hyperframes |  |
| 9 | `cursor/plugins` | 12751 | 1256 | TypeScript | 1,717 stars this week | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 10 | `MadsLorentzen/ai-job-search` | 53258 | 17396 | Python | 5,742 stars this week | 在您的机器上运行的作业搜索。基于Claude Code构建的人工智能求职框架：评估帖子、定制简历、撰写求职信、准备面试。分叉并拥有它。 | https://github.com/MadsLorentzen/ai-job-search | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `paperclipai/paperclip` | 104134 | 17401 | TypeScript | 23,340 stars this month | 每个人都使用的开源应用程序来管理工作中的代理 | https://github.com/paperclipai/paperclip |  |
| 2 | `debpalash/VoiceStudio` | 75421 | 8257 | Python | 42,036 stars this month | VoiceStudio是开源、完全本地的ElevenLabs替代品--语音克隆、语音设计、视频配音、听写、转录和有声读物创作，支持646种语言。 | https://github.com/debpalash/VoiceStudio |  |
| 3 | `heygen-com/hyperframes` | 66756 | 6056 | TypeScript | 15,429 stars this month | 编写HTML。渲染视频。专为客服代表打造。 | https://github.com/heygen-com/hyperframes |  |
| 4 | `anthropics/financial-services` | 40289 | 5650 | Python | 5,498 stars this month | — | https://github.com/anthropics/financial-services |  |
| 5 | `vectorize-io/hindsight` | 51243 | 6150 | Python | 27,550 stars this month | 后见之明：学习的客服代表记忆 | https://github.com/vectorize-io/hindsight |  |
| 6 | `cloudflare/security-audit-skill` | 31169 | 1953 | JavaScript | 19,109 stars this month | 用于多阶段安全审核的编码代理技能，具有经过独立验证的机器可读结果 | https://github.com/cloudflare/security-audit-skill | 新增 |
| 7 | `agent-substrate/substrate` | 5510 | 601 | Go | 3,533 stars this month | Agent Substrate ：核心系统 | https://github.com/agent-substrate/substrate |  |
| 8 | `mksglu/context-mode` | 30763 | 2278 | TypeScript | 7,319 stars this month | 人工智能编码代理的上下文窗口优化。沙盒工具输出（减少98 ％ ） ，保持会话内存，并通过MCP +钩子在17个平台上强制路由。 | https://github.com/mksglu/context-mode |  |
| 9 | `NVIDIA/OpenShell` | 16627 | 1811 | Rust | 7,995 stars this month | OpenShell是自主AI代理的安全、私有运行时。 | https://github.com/NVIDIA/OpenShell |  |
| 10 | `affaan-m/ECC` | 283300 | 42078 | JavaScript | 23,080 stars this month | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 11 | `tashfeenahmed/freellmapi` | 37093 | 5014 | TypeScript | 10,063 stars this month | 每月74亿个代币。34个免费LLM提供商。635个免费模型端点。全部在一个/v1端点后面，加上任何与OpenAI兼容的自定义端点。智能路由、自动故障转移、加密密钥。仅限个人实验。 | https://github.com/tashfeenahmed/freellmapi |  |
| 12 | `anthropics/knowledge-work-plugins` | 30202 | 3414 | Python | 5,493 stars this month | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins |  |
| 13 | `NationalSecurityAgency/ghidra` | 90917 | 10180 | Java | 12,009 stars this month | Ghidra是一个软件逆向工程（ SRE ）框架 | https://github.com/NationalSecurityAgency/ghidra |  |
| 14 | `cursor/plugins` | 12751 | 1256 | TypeScript | 4,507 stars this month | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 15 | `rohitg00/ai-engineering-from-scratch` | 71048 | 12497 | Python | 16,300 stars this month | 学习人工智能工程！学习它。建造它。为别人运送它。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 16 | `anthropics/claude-plugins-official` | 42708 | 4535 | Python | 6,015 stars this month | 由Anthropic管理的高质量Claude Code插件的官方目录。 | https://github.com/anthropics/claude-plugins-official | 新增 |
| 17 | `TencentCloud/Octop` | 9902 | 1272 | Python | 6,138 stars this month | 更智能、自托管的人工智能助手—多用户、多代理。 | https://github.com/TencentCloud/Octop |  |
| 18 | `trycua/cua` | 30140 | 2168 | Rust | 7,211 stars this month | 通过开源驱动程序、跨操作系统沙箱和用于培训、评估和数据生成的基准来扩展计算机使用2.0。 | https://github.com/trycua/cua |  |
| 19 | `longbridge/gpui-kit` | 18132 | 1099 | Rust | 3,632 stars this month | 使用GPUI构建梦幻般的跨平台桌面应用程序的Rust GUI组件。 | https://github.com/longbridge/gpui-kit |  |
| 20 | `pingdotgg/t3code` | 28370 | 7576 | TypeScript | 5,415 stars this month | — | https://github.com/pingdotgg/t3code | 新增 |


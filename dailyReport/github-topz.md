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

**最近一次更新时间**（Asia/Shanghai）： 2026-10-14 09:18:53

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 553065 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 518671 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 488442 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 457006 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 398984 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 391910 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `donnemartin/system-design-primer` | 374118 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 8 | `nilbuild/developer-roadmap` | 369321 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 9 | `jwasham/coding-interview-university` | 362460 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 11 | `vinta/awesome-python` | 327195 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `morluto/rea` | 208221 | 50881 | TypeScript | 54,679 stars today | 使用代理对任何内容进行反向工程，从应用行为到本机二进制文件。 | https://github.com/morluto/rea |  |
| 2 | `bilawalsidhu/gods-eye-view` | 55424 | 10835 | JavaScript | 1,961 stars today | 浏览器中的间谍卫星模拟器，但数据是真实的。在逼真的3D地球仪上实时开源空间智能。 | https://github.com/bilawalsidhu/gods-eye-view | 新增 |
| 3 | `debpalash/VoiceStudio` | 63351 | 7047 | Python | 1,748 stars today | VoiceStudio是开源、完全本地的ElevenLabs替代品--语音克隆、语音设计、视频配音、听写、转录和有声读物创作，支持646种语言。 | https://github.com/debpalash/VoiceStudio | 新增 |
| 4 | `mksglu/context-mode` | 28259 | 1995 | TypeScript | 969 stars today | 人工智能编码代理的上下文窗口优化。沙盒工具输出（减少98 ％ ） ，保持会话内存，并通过MCP +钩子在17个平台上强制路由。 | https://github.com/mksglu/context-mode | 新增 |
| 5 | `cathrynlavery/diagram-design` | 54150 | 3436 | HTML | 1,815 stars today | Claude Code、Codex、GitHub Copilot、Cursor、Factory Droid和Pi的编辑图设计。44种图类型。独立的HTML + SVG。没有阴影，没有美人鱼粪便。 | https://github.com/cathrynlavery/diagram-design |  |
| 6 | `vercel-labs/skills` | 34522 | 2953 | TypeScript | 190 stars today | 开放式客服代表技能工具- npx技能 | https://github.com/vercel-labs/skills | 新增 |
| 7 | `lyogavin/airllm` | 38345 | 3920 | Jupyter Notebook | 1,001 stars today | AirLLM 2.8T LLM推理，带单个4GB显卡 | https://github.com/lyogavin/airllm | 新增 |
| 8 | `storytold/artcraft` | 25718 | 4031 | Rust | 4,081 stars today | ArtCraft是艺术家、设计师和电影制作人的特意制作引擎 | https://github.com/storytold/artcraft |  |
| 9 | `xtool-org/xtool` | 9396 | 398 | Swift | 1,198 stars today | 跨平台Xcode替换。在Linux、Windows、macOS上使用SwiftPM构建和部署iOS应用。 | https://github.com/xtool-org/xtool | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `boykopovar/AnyPS5` | 35385 | 3073 | C++ | 28,663 stars this week | 用于自动将PS5可执行文件移植到Linux和Windows的工具 | https://github.com/boykopovar/AnyPS5 |  |
| 2 | `mattpocock/skills` | 289712 | 24312 | Shell | 11,955 stars this week | 真正工程师的技能。直接来自我的.agents目录。 | https://github.com/mattpocock/skills |  |
| 3 | `tester-army/e2e` | 10108 | 487 | TypeScript | 4,426 stars this week | 适用于网络和移动应用程序的下一代e2e测试框架。 | https://github.com/tester-army/e2e | 新增 |
| 4 | `EpicGames/raddebugger` | 8486 | 413 | C | 857 stars this week | 本机、用户模式、多进程、图形调试器。 | https://github.com/EpicGames/raddebugger |  |
| 5 | `heygen-com/hyperframes` | 62814 | 5633 | TypeScript | 4,732 stars this week | 编写HTML。渲染视频。专为客服代表打造。 | https://github.com/heygen-com/hyperframes |  |
| 6 | `thedotmack/claude-mem` | 100449 | 8801 | TypeScript | 3,587 stars this week | 每个座席跨会话的持久上下文–捕获座席在会话期间执行的所有操作，使用AI对其进行压缩，并将相关上下文注入到未来的会话中。适用于Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode等 | https://github.com/thedotmack/claude-mem |  |
| 7 | `cursor/plugins` | 11230 | 1092 | TypeScript | 1,141 stars this week | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 8 | `earthtojake/text-to-cad` | 19992 | 1964 | Python | 2,173 stars this week | 为您的代理商提供CAD超能力。 | https://github.com/earthtojake/text-to-cad |  |
| 9 | `flutter/flutter` | 180111 | 34017 | Dart | 967 stars this week | Flutter可以轻松快速地为移动设备及其他设备构建漂亮的应用程序 | https://github.com/flutter/flutter | 新增 |
| 10 | `cathrynlavery/diagram-design` | 54151 | 3436 | HTML | 9,867 stars this week | Claude Code、Codex、GitHub Copilot、Cursor、Factory Droid和Pi的编辑图设计。44种图类型。独立的HTML + SVG。没有阴影，没有美人鱼粪便。 | https://github.com/cathrynlavery/diagram-design | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `alibaba/open-code-review` | 46919 | 3406 | Go | 24,283 stars this month | 安全、快速、高效，经受住阿里巴巴规模的考验。混合架构代码审核工具：确定性流水线+ LLM Agent、精确的行级注释、内置多语言规则集（ NPE、线程安全、XSS、SQL注入）、OpenAI &amp; Anthropic兼容。 | https://github.com/alibaba/open-code-review |  |
| 2 | `paperclipai/paperclip` | 101580 | 17041 | TypeScript | 21,106 stars this month | 每个人都使用的开源应用程序来管理工作中的代理 | https://github.com/paperclipai/paperclip |  |
| 3 | `anthropics/financial-services` | 39725 | 5596 | Python | 4,971 stars this month | — | https://github.com/anthropics/financial-services |  |
| 4 | `debpalash/VoiceStudio` | 63352 | 7047 | Python | 36,408 stars this month | VoiceStudio是开源、完全本地的ElevenLabs替代品--语音克隆、语音设计、视频配音、听写、转录和有声读物创作，支持646种语言。 | https://github.com/debpalash/VoiceStudio |  |
| 5 | `vectorize-io/hindsight` | 49278 | 6036 | Python | 25,874 stars this month | 后见之明：学习的客服代表记忆 | https://github.com/vectorize-io/hindsight |  |
| 6 | `affaan-m/ECC` | 278622 | 41498 | JavaScript | 22,653 stars this month | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 7 | `anthropics/knowledge-work-plugins` | 29549 | 3352 | Python | 5,569 stars this month | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins |  |
| 8 | `heygen-com/hyperframes` | 62814 | 5633 | TypeScript | 13,203 stars this month | 编写HTML。渲染视频。专为客服代表打造。 | https://github.com/heygen-com/hyperframes |  |
| 9 | `anthropics/claude-code` | 150661 | 26463 | TypeScript | 6,545 stars this month | Claude Code是一个代理编码工具，它位于您的终端中，了解您的代码库，并通过执行日常任务、解释复杂代码和处理git工作流程（所有这些都通过自然语言命令）来帮助您更快地进行编码。 | https://github.com/anthropics/claude-code |  |
| 10 | `TencentCloud/Octop` | 9165 | 1125 | Python | 7,517 stars this month | 更智能、自托管的人工智能助手—多用户、多代理。 | https://github.com/TencentCloud/Octop |  |
| 11 | `Tencent/WeKnora` | 33776 | 4491 | Go | 11,177 stars this month | 开源LLM知识平台：将原始文档转化为可查询的RAG、自主推理代理和自我维护的Wiki。 | https://github.com/Tencent/WeKnora |  |
| 12 | `agent-substrate/substrate` | 5058 | 564 | Go | 3,190 stars this month | Agent Substrate ：核心系统 | https://github.com/agent-substrate/substrate |  |
| 13 | `NVIDIA/OpenShell` | 16120 | 1776 | Rust | 7,574 stars this month | OpenShell是自主AI代理的安全、私有运行时。 | https://github.com/NVIDIA/OpenShell |  |
| 14 | `addyosmani/agent-skills` | 106223 | 11072 | JavaScript | 12,820 stars this month | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 15 | `tashfeenahmed/freellmapi` | 34723 | 4729 | TypeScript | 8,786 stars this month | 每月74亿个代币。34个免费LLM提供商。635个免费模型端点。全部在一个/v1端点后面，加上任何与OpenAI兼容的自定义端点。智能路由、自动故障转移、加密密钥。仅限个人实验。 | https://github.com/tashfeenahmed/freellmapi |  |
| 16 | `trycua/cua` | 29634 | 2118 | Rust | 7,159 stars this month | 通过开源驱动程序、跨操作系统车队以及培训、评估和数据生成的基准来扩展计算机使用2.0。 | https://github.com/trycua/cua |  |
| 17 | `mksglu/context-mode` | 28259 | 1995 | TypeScript | 5,378 stars this month | 人工智能编码代理的上下文窗口优化。沙盒工具输出（减少98 ％ ） ，保持会话内存，并通过MCP +钩子在17个平台上强制路由。 | https://github.com/mksglu/context-mode |  |
| 18 | `cursor/plugins` | 11230 | 1092 | TypeScript | 3,795 stars this month | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 19 | `NationalSecurityAgency/ghidra` | 86360 | 9618 | Java | 11,115 stars this month | Ghidra是一个软件逆向工程（ SRE ）框架 | https://github.com/NationalSecurityAgency/ghidra | 新增 |
| 20 | `JustVugg/colibri` | 41759 | 4619 | C | 13,015 stars this month | 在您已经拥有的硬件上运行前沿MoE模型—纯C ，零DEPS ，从磁盘流式传输的专家。微型引擎，超大型号。 🐦 | https://github.com/JustVugg/colibri |  |
| 21 | `rohitg00/ai-engineering-from-scratch` | 68684 | 12025 | Python | 14,347 stars this month | 学习人工智能工程！学习它。建造它。为别人运送它。 | https://github.com/rohitg00/ai-engineering-from-scratch | 新增 |
| 22 | `google/artemis` | 11549 | 1187 | Python | 7,039 stars this month | ARTEMIS将自然语言指令转化为可靠的Android自动化。它自动化端到端工作流程，捕获日志，并与Antigravity、Codex和Claude Code等AI编码助手无缝集成。它在AndroidWorld Ben上的成功率也达到了99%以上…… | https://github.com/google/artemis | 新增 |
| 23 | `longbridge/gpui-kit` | 17194 | 1056 | Rust | 2,812 stars this month | 使用GPUI构建梦幻般的跨平台桌面应用程序的Rust GUI组件。 | https://github.com/longbridge/gpui-kit | 新增 |


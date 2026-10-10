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

**最近一次更新时间**（Asia/Shanghai）： 2026-10-10 09:25:41

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 552224 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 516803 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 487010 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 456779 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 398573 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 391530 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `donnemartin/system-design-primer` | 373579 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 8 | `nilbuild/developer-roadmap` | 369047 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 9 | `jwasham/coding-interview-university` | 362355 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 11 | `vinta/awesome-python` | 326167 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `morluto/rea` | 46882 | 7557 | TypeScript | 14,927 stars today | 使用代理对任何内容进行反向工程，从应用行为到本机二进制文件。 | https://github.com/morluto/rea |  |
| 2 | `boykopovar/AnyPS5` | 22459 | 1827 | C++ | 5,868 stars today | 用于自动将PS5可执行文件移植到Linux和Windows的工具 | https://github.com/boykopovar/AnyPS5 |  |
| 3 | `mattpocock/skills` | 282744 | 23689 | Shell | 1,687 stars today | 真正工程师的技能。直接来自我的.agents目录。 | https://github.com/mattpocock/skills |  |
| 4 | `cathrynlavery/diagram-design` | 47902 | 3034 | HTML | 1,739 stars today | Claude Code、Codex、GitHub Copilot、Factory Droid和Pi的编辑图设计。42种图类型。独立的HTML + SVG。没有阴影，没有美人鱼粪便。 | https://github.com/cathrynlavery/diagram-design |  |
| 5 | `alibaba/open-code-review` | 45251 | 3263 | Go | 326 stars today | 安全、快速、高效，经受住阿里巴巴规模的考验。混合架构代码审核工具：确定性流水线+ LLM Agent、精确的行级注释、内置多语言规则集（ NPE、线程安全、XSS、SQL注入）、OpenAI &amp; Anthropic兼容。 | https://github.com/alibaba/open-code-review | 新增 |
| 6 | `anthropics/knowledge-work-plugins` | 28276 | 3246 | Python | 709 stars today | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins | 新增 |
| 7 | `BerriAI/litellm` | 60676 | 12188 | Python | 95 stars today | 最快、最轻的人工智能网关。使用Python SDK的Rust核心。调用100多个OpenAI （或本机）格式的LLM API ，包括成本跟踪、护栏、负载平衡和日志记录[Bedrock、Azure、OpenAI、Anthropic、OpenAI、VertexAI、vLLM、Nvidia NIM] | https://github.com/BerriAI/litellm | 新增 |
| 8 | `addyosmani/agent-skills` | 104003 | 10868 | JavaScript | 436 stars today | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 9 | `storytold/artcraft` | 11563 | 1746 | Rust | 3,752 stars today | ArtCraft是艺术家、设计师和电影制作人的特意制作引擎 | https://github.com/storytold/artcraft | 新增 |
| 10 | `Robbyant/lingbot-map` | 17709 | 1951 | Python | 110 stars today | [ECCV 2026最佳论文奖候选人] LingBot-Map ：用于流式3D重建的几何上下文变换器 | https://github.com/Robbyant/lingbot-map | 新增 |
| 11 | `twostraws/SwiftUI-Agent-Skill` | 5444 | 196 | — | 65 stars today | 适用于Claude Code、Codex和其他AI工具的SwiftUI代理技能。 | https://github.com/twostraws/SwiftUI-Agent-Skill | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `boykopovar/AnyPS5` | 22460 | 1827 | C++ | 15,539 stars this week | 用于自动将PS5可执行文件移植到Linux和Windows的工具 | https://github.com/boykopovar/AnyPS5 |  |
| 2 | `mvschwarz/openrig` | 6462 | 473 | TypeScript | 2,338 stars this week | 从Claude Code、Codex和Pi构建您自己的代理网络：具有角色、共享上下文和所有工作的持久团队。 | https://github.com/mvschwarz/openrig |  |
| 3 | `mattpocock/skills` | 282744 | 23689 | Shell | 8,156 stars this week | 真正工程师的技能。直接来自我的.agents目录。 | https://github.com/mattpocock/skills | 新增 |
| 4 | `heygen-com/hyperframes` | 59812 | 5338 | TypeScript | 4,003 stars this week | 编写HTML。渲染视频。专为客服代表打造。 | https://github.com/heygen-com/hyperframes |  |
| 5 | `cursor/plugins` | 10594 | 1001 | TypeScript | 1,125 stars this week | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 6 | `EpicGames/raddebugger` | 8267 | 394 | C | 654 stars this week | 本机、用户模式、多进程、图形调试器。 | https://github.com/EpicGames/raddebugger | 新增 |
| 7 | `thedotmack/claude-mem` | 98996 | 8671 | TypeScript | 3,850 stars this week | 每个座席跨会话的持久上下文–捕获座席在会话期间执行的所有操作，使用AI对其进行压缩，并将相关上下文注入到未来的会话中。适用于Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode等 | https://github.com/thedotmack/claude-mem |  |
| 8 | `earthtojake/text-to-cad` | 18768 | 1859 | Python | 2,125 stars this week | 为您的代理商提供CAD超能力。 | https://github.com/earthtojake/text-to-cad | 新增 |
| 9 | `pingdotgg/t3code` | 26643 | 6957 | TypeScript | 2,379 stars this week | — | https://github.com/pingdotgg/t3code | 新增 |
| 10 | `Panniantong/Agent-Reach` | 94913 | 8298 | Python | 7,084 stars this week | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 11 | `DuarteSantos8/openGym` | 8680 | 1082 | JavaScript | 6,749 stars this week | 自我托管的健身房和体重跟踪器—计划例行公事、日志锻炼（超组、热身、有氧运动）、查看哪些肌肉经过训练、疲劳或脱锻、从FitNotes/Strong/Hevy导入、密钥登录。您的数据，您的服务器。 | https://github.com/DuarteSantos8/openGym |  |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `alibaba/open-code-review` | 45252 | 3263 | Go | 23,028 stars this month | 安全、快速、高效，经受住阿里巴巴规模的考验。混合架构代码审核工具：确定性流水线+ LLM Agent、精确的行级注释、内置多语言规则集（ NPE、线程安全、XSS、SQL注入）、OpenAI &amp; Anthropic兼容。 | https://github.com/alibaba/open-code-review |  |
| 2 | `debpalash/VoiceStudio` | 56325 | 6317 | Python | 34,560 stars this month | VoiceStudio是开源、完全本地的ElevenLabs替代品--语音克隆、语音设计、视频配音、听写、转录和有声读物创作，支持646种语言。 | https://github.com/debpalash/VoiceStudio | 新增 |
| 3 | `anthropics/financial-services` | 39175 | 5569 | Python | 4,495 stars this month | — | https://github.com/anthropics/financial-services |  |
| 4 | `paperclipai/paperclip` | 99248 | 16749 | TypeScript | 19,137 stars this month | 每个人都使用的开源应用程序来管理工作中的代理 | https://github.com/paperclipai/paperclip |  |
| 5 | `affaan-m/ECC` | 275994 | 41178 | JavaScript | 22,710 stars this month | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 6 | `bilawalsidhu/gods-eye-view` | 49660 | 10041 | JavaScript | 29,212 stars this month | 浏览器中的间谍卫星模拟器，但数据是真实的。在逼真的3D地球仪上实时开源空间智能。 | https://github.com/bilawalsidhu/gods-eye-view |  |
| 7 | `vectorize-io/hindsight` | 47716 | 5977 | Python | 24,617 stars this month | 后见之明：学习的客服代表记忆 | https://github.com/vectorize-io/hindsight |  |
| 8 | `Tencent/WeKnora` | 32841 | 4364 | Go | 11,118 stars this month | 开源LLM知识平台：将原始文档转化为可查询的RAG、自主推理代理和自我维护的Wiki。 | https://github.com/Tencent/WeKnora |  |
| 9 | `anthropics/claude-code` | 149880 | 25945 | TypeScript | 6,173 stars this month | Claude Code是一个代理编码工具，它位于您的终端中，了解您的代码库，并通过执行日常任务、解释复杂代码和处理git工作流程（所有这些都通过自然语言命令）来帮助您更快地进行编码。 | https://github.com/anthropics/claude-code |  |
| 10 | `TencentCloud/Octop` | 8247 | 998 | Python | 6,720 stars this month | 更智能、自托管的人工智能助手—多用户、多代理。 | https://github.com/TencentCloud/Octop |  |
| 11 | `anthropics/knowledge-work-plugins` | 28276 | 3247 | Python | 4,131 stars this month | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins |  |
| 12 | `agent-substrate/substrate` | 4709 | 536 | Go | 2,879 stars this month | Agent Substrate ：核心系统 | https://github.com/agent-substrate/substrate |  |
| 13 | `NVIDIA/OpenShell` | 15605 | 1749 | Rust | 7,118 stars this month | OpenShell是自主AI代理的安全、私有运行时。 | https://github.com/NVIDIA/OpenShell |  |
| 14 | `heygen-com/hyperframes` | 59812 | 5338 | TypeScript | 11,576 stars this month | 编写HTML。渲染视频。专为客服代表打造。 | https://github.com/heygen-com/hyperframes |  |
| 15 | `JustVugg/colibri` | 40818 | 4482 | C | 13,755 stars this month | 在您已经拥有的硬件上运行前沿MoE模型—纯C ，零DEPS ，从磁盘流式传输的专家。微型引擎，超大型号。 🐦 | https://github.com/JustVugg/colibri |  |
| 16 | `mksglu/context-mode` | 25975 | 1875 | TypeScript | 4,398 stars this month | 人工智能编码代理的上下文窗口优化。沙盒工具输出（减少98 ％ ） ，保持会话内存，并通过MCP +钩子在17个平台上强制路由。 | https://github.com/mksglu/context-mode |  |
| 17 | `trycua/cua` | 29189 | 2061 | Rust | 6,877 stars this month | 通过开源驱动程序、跨操作系统车队以及培训、评估和数据生成的基准来扩展计算机使用2.0。 | https://github.com/trycua/cua |  |
| 18 | `tashfeenahmed/freellmapi` | 32552 | 4514 | TypeScript | 7,455 stars this month | 每月74亿个代币。34个免费LLM提供商。635个免费模型端点。全部在一个/v1端点后面，加上任何与OpenAI兼容的自定义端点。智能路由、自动故障转移、加密密钥。仅限个人实验。 | https://github.com/tashfeenahmed/freellmapi |  |
| 19 | `cursor/plugins` | 10594 | 1001 | TypeScript | 3,503 stars this month | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 20 | `addyosmani/agent-skills` | 104003 | 10868 | JavaScript | 11,155 stars this month | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 21 | `DietrichGebert/ponytail` | 159662 | 8588 | JavaScript | 27,290 stars this month | 让你的人工智能代理像房间里最懒惰的高级开发人员一样思考。最好的代码是你从未写过的代码。 | https://github.com/DietrichGebert/ponytail |  |
| 22 | `max-sixty/worktrunk` | 9134 | 328 | Rust | 2,301 stars this month | Worktrunk是用于Git工作树管理的CLI ，专为并行AI代理工作流程而设计 | https://github.com/max-sixty/worktrunk |  |


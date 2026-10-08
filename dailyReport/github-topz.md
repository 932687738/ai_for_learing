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

**最近一次更新时间**（Asia/Shanghai）： 2026-10-08 09:24:26

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 552063 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 516120 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 486775 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 456907 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 398661 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 391598 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `donnemartin/system-design-primer` | 373538 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 8 | `nilbuild/developer-roadmap` | 369113 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 9 | `jwasham/coding-interview-university` | 362507 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 11 | `vinta/awesome-python` | 325920 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `morluto/rea` | 15312 | 1594 | TypeScript | 4,655 stars today | 使用代理对任何内容进行反向工程，从应用行为到本机二进制文件。 | https://github.com/morluto/rea | 新增 |
| 2 | `mattpocock/skills` | 279627 | 23435 | Shell | 1,403 stars today | 真正工程师的技能。直接来自我的.agents目录。 | https://github.com/mattpocock/skills |  |
| 3 | `boykopovar/AnyPS5` | 10669 | 804 | C++ | 2,716 stars today | 用于自动将PS5可执行文件移植到Linux和Windows的工具 | https://github.com/boykopovar/AnyPS5 | 新增 |
| 4 | `ayghri/i-have-adhd` | 55137 | 3161 | Python | 619 stars today | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd | 新增 |
| 5 | `cathrynlavery/diagram-design` | 44985 | 2889 | HTML | 825 stars today | Claude Code、Codex、GitHub Copilot、Factory Droid和Pi的编辑图设计。42种图类型。独立的HTML + SVG。没有阴影，没有美人鱼粪便。 | https://github.com/cathrynlavery/diagram-design | 新增 |
| 6 | `addyosmani/agent-skills` | 102833 | 10771 | JavaScript | 677 stars today | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills | 新增 |
| 7 | `EpicGames/raddebugger` | 7866 | 383 | C | 90 stars today | 本机、用户模式、多进程、图形调试器。 | https://github.com/EpicGames/raddebugger | 新增 |
| 8 | `thedotmack/claude-mem` | 97738 | 8605 | TypeScript | 578 stars today | 每个座席跨会话的持久上下文–捕获座席在会话期间执行的所有操作，使用AI对其进行压缩，并将相关上下文注入到未来的会话中。适用于Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode等 | https://github.com/thedotmack/claude-mem | 新增 |
| 9 | `manaflow-ai/cmux` | 27849 | 2462 | Swift | 44 stars today | 基于Ghostty的开源macOS终端，具有针对AI编码代理的垂直选项卡和通知。专为多任务处理、组织和可编程性而打造。 | https://github.com/manaflow-ai/cmux | 新增 |
| 10 | `trycua/cua` | 28761 | 2040 | Rust | 228 stars today | 通过开源驱动程序、跨操作系统车队以及培训、评估和数据生成的基准来扩展计算机使用2.0。 | https://github.com/trycua/cua | 新增 |
| 11 | `cloudflare/security-audit-skill` | 26064 | 1565 | JavaScript | 576 stars today | 用于多阶段安全审核的编码代理技能，具有经过独立验证的机器可读结果 | https://github.com/cloudflare/security-audit-skill | 新增 |
| 12 | `tester-army/e2e` | 7471 | 341 | TypeScript | 1,390 stars today | 适用于网络和移动应用程序的下一代e2e测试框架。 | https://github.com/tester-army/e2e | 新增 |
| 13 | `DuarteSantos8/openGym` | 6926 | 909 | JavaScript | 1,493 stars today | 自我托管的健身房和体重跟踪器—计划例行公事、日志锻炼（超组、热身、有氧运动）、查看哪些肌肉经过训练、疲劳或脱锻、从FitNotes/Strong/Hevy导入、密钥登录。您的数据，您的服务器。 | https://github.com/DuarteSantos8/openGym | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `mvschwarz/openrig` | 5789 | 428 | TypeScript | 2,912 stars this week | 从Claude Code、Codex和Pi构建您自己的代理网络：具有角色、共享上下文和所有工作的持久团队。 | https://github.com/mvschwarz/openrig | 新增 |
| 2 | `boykopovar/AnyPS5` | 10669 | 804 | C++ | 6,075 stars this week | 用于自动将PS5可执行文件移植到Linux和Windows的工具 | https://github.com/boykopovar/AnyPS5 | 新增 |
| 3 | `heygen-com/hyperframes` | 58559 | 5209 | TypeScript | 3,908 stars this week | 编写HTML。渲染视频。专为客服代表打造。 | https://github.com/heygen-com/hyperframes |  |
| 4 | `cursor/plugins` | 10258 | 974 | TypeScript | 1,109 stars this week | 光标插件规范和官方插件 | https://github.com/cursor/plugins | 新增 |
| 5 | `NVIDIA/OpenShell` | 15304 | 1727 | Rust | 3,690 stars this week | OpenShell是自主AI代理的安全、私有运行时。 | https://github.com/NVIDIA/OpenShell | 新增 |
| 6 | `Panniantong/Agent-Reach` | 93260 | 8171 | Python | 6,912 stars this week | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach | 新增 |
| 7 | `thedotmack/claude-mem` | 97738 | 8605 | TypeScript | 2,607 stars this week | 每个座席跨会话的持久上下文–捕获座席在会话期间执行的所有操作，使用AI对其进行压缩，并将相关上下文注入到未来的会话中。适用于Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode等 | https://github.com/thedotmack/claude-mem | 新增 |
| 8 | `pablostanley/yoinks` | 5106 | 443 | TypeScript | 2,732 stars this week | yoink您终端上的任何视频。没有阴暗的广告。 | https://github.com/pablostanley/yoinks |  |
| 9 | `DuarteSantos8/openGym` | 6926 | 909 | JavaScript | 4,906 stars this week | 自我托管的健身房和体重跟踪器—计划例行公事、日志锻炼（超组、热身、有氧运动）、查看哪些肌肉经过训练、疲劳或脱锻、从FitNotes/Strong/Hevy导入、密钥登录。您的数据，您的服务器。 | https://github.com/DuarteSantos8/openGym | 新增 |
| 10 | `tile-ai/tilelang` | 8474 | 856 | Python | 639 stars this week | 特定于领域的语言，旨在简化高性能GPU/CPU/加速器内核的开发 | https://github.com/tile-ai/tilelang |  |
| 11 | `HunxByts/GhostTrack` | 17390 | 2355 | Python | 1,534 stars this week | 跟踪位置或手机号码的有用工具 | https://github.com/HunxByts/GhostTrack | 新增 |
| 12 | `Friedrich-M/UniMate` | 1571 | 152 | Python | 716 stars this week | [SIGGRAPH ASIA 2026] UniMate ：一个统一的模型来动画化不同的骨架 | https://github.com/Friedrich-M/UniMate | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `alibaba/open-code-review` | 44246 | 3196 | Go | 22,512 stars this month | 安全、快速、高效，经受住阿里巴巴规模的考验。混合架构代码审核工具：确定性流水线+ LLM Agent、精确的行级注释、内置多语言规则集（ NPE、线程安全、XSS、SQL注入）、OpenAI &amp; Anthropic兼容。 | https://github.com/alibaba/open-code-review |  |
| 2 | `bilawalsidhu/gods-eye-view` | 48767 | 9915 | JavaScript | 30,152 stars this month | 浏览器中的间谍卫星模拟器，但数据是真实的。在逼真的3D地球仪上实时开源空间智能。 | https://github.com/bilawalsidhu/gods-eye-view |  |
| 3 | `affaan-m/ECC` | 274946 | 41020 | JavaScript | 23,835 stars this month | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 4 | `anthropics/financial-services` | 38947 | 5565 | Python | 4,318 stars this month | — | https://github.com/anthropics/financial-services |  |
| 5 | `paperclipai/paperclip` | 98465 | 16638 | TypeScript | 18,524 stars this month | 每个人都使用的开源应用程序来管理工作中的代理 | https://github.com/paperclipai/paperclip |  |
| 6 | `ayghri/i-have-adhd` | 55137 | 3161 | Python | 27,500 stars this month | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 7 | `vectorize-io/hindsight` | 46832 | 5961 | Python | 23,808 stars this month | 后见之明：学习的客服代表记忆 | https://github.com/vectorize-io/hindsight |  |
| 8 | `spotify/portal-ai-plugins` | 2414 | 198 | TypeScript | 2,181 stars this month | — | https://github.com/spotify/portal-ai-plugins | 新增 |
| 9 | `Tencent/WeKnora` | 32440 | 4319 | Go | 10,980 stars this month | 开源LLM知识平台：将原始文档转化为可查询的RAG、自主推理代理和自我维护的Wiki。 | https://github.com/Tencent/WeKnora |  |
| 10 | `anthropics/claude-code` | 149781 | 25720 | TypeScript | 6,067 stars this month | Claude Code是一个代理编码工具，它位于您的终端中，了解您的代码库，并通过执行日常任务、解释复杂代码和处理git工作流程（所有这些都通过自然语言命令）来帮助您更快地进行编码。 | https://github.com/anthropics/claude-code |  |
| 11 | `TencentCloud/Octop` | 7726 | 930 | Python | 6,193 stars this month | 更智能、自托管的人工智能助手—多用户、多代理。 | https://github.com/TencentCloud/Octop |  |
| 12 | `mksglu/context-mode` | 25627 | 1848 | TypeScript | 5,129 stars this month | 人工智能编码代理的上下文窗口优化。沙盒工具输出（减少98 ％ ） ，保持会话内存，并通过MCP +钩子在17个平台上强制路由。 | https://github.com/mksglu/context-mode |  |
| 13 | `agent-substrate/substrate` | 4522 | 525 | Go | 2,712 stars this month | Agent Substrate ：核心系统 | https://github.com/agent-substrate/substrate | 新增 |
| 14 | `NVIDIA/OpenShell` | 15304 | 1727 | Rust | 6,795 stars this month | OpenShell是自主AI代理的安全、私有运行时。 | https://github.com/NVIDIA/OpenShell | 新增 |
| 15 | `heygen-com/hyperframes` | 58559 | 5209 | TypeScript | 13,601 stars this month | 编写HTML。渲染视频。专为客服代表打造。 | https://github.com/heygen-com/hyperframes |  |
| 16 | `DietrichGebert/ponytail` | 157615 | 8467 | JavaScript | 27,653 stars this month | 让你的人工智能代理像房间里最懒惰的高级开发人员一样思考。最好的代码是你从未写过的代码。 | https://github.com/DietrichGebert/ponytail |  |
| 17 | `cursor/plugins` | 10258 | 974 | TypeScript | 3,377 stars this month | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 18 | `JustVugg/colibri` | 40331 | 4434 | C | 13,446 stars this month | 在您已经拥有的硬件上运行前沿MoE模型—纯C ，零DEPS ，从磁盘流式传输的专家。微型引擎，超大型号。 🐦 | https://github.com/JustVugg/colibri | 新增 |
| 19 | `trycua/cua` | 28761 | 2040 | Rust | 6,438 stars this month | 通过开源驱动程序、跨操作系统车队以及培训、评估和数据生成的基准来扩展计算机使用2.0。 | https://github.com/trycua/cua |  |
| 20 | `tashfeenahmed/freellmapi` | 31707 | 4424 | TypeScript | 6,960 stars this month | 每月74亿个代币。34个免费LLM提供商。635个免费模型端点。全部在一个/v1端点后面，加上任何与OpenAI兼容的自定义端点。智能路由、自动故障转移、加密密钥。仅限个人实验。 | https://github.com/tashfeenahmed/freellmapi |  |
| 21 | `tt-a1i/archify` | 79250 | 5315 | JavaScript | 27,502 stars this month | 将任何想法、计划或代码库转换为漂亮的交互式图表。Claude Code、Codex等的代理技能。 | https://github.com/tt-a1i/archify |  |
| 22 | `anthropics/knowledge-work-plugins` | 27145 | 3175 | Python | 3,123 stars this month | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins |  |
| 23 | `addyosmani/agent-skills` | 102833 | 10771 | JavaScript | 10,376 stars this month | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills | 新增 |
| 24 | `max-sixty/worktrunk` | 8968 | 323 | Rust | 2,196 stars this month | Worktrunk是用于Git工作树管理的CLI ，专为并行AI代理工作流程而设计 | https://github.com/max-sixty/worktrunk |  |
| 25 | `NationalSecurityAgency/ghidra` | 81432 | 9042 | Java | 6,914 stars this month | Ghidra是一个软件逆向工程（ SRE ）框架 | https://github.com/NationalSecurityAgency/ghidra | 新增 |


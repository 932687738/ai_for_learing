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

**最近一次更新时间**（Asia/Shanghai）： 2026-10-02 19:38:32

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 551142 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 513486 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 485418 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 456625 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 398300 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 391192 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `donnemartin/system-design-primer` | 372887 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 8 | `nilbuild/developer-roadmap` | 368695 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 9 | `jwasham/coding-interview-university` | 362228 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 11 | `vinta/awesome-python` | 324616 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `Panniantong/Agent-Reach` | 87746 | 7739 | Python | 683 stars today | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach | 新增 |
| 2 | `JuliusBrussee/caveman` | 108839 | 6310 | Go | 193 stars today | 🪨 为什么在很少令牌做恶作剧时使用许多令牌。病毒技能+编码代理的代理，通过像穴居人一样说话来削减65%的代币。 | https://github.com/JuliusBrussee/caveman | 新增 |
| 3 | `obra/superpowers` | 294180 | 26310 | Shell | 455 stars today | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers |  |
| 4 | `DietrichGebert/ponytail` | 151123 | 8107 | JavaScript | 1,194 stars today | 让你的人工智能代理像房间里最懒惰的高级开发人员一样思考。最好的代码是你从未写过的代码。 | https://github.com/DietrichGebert/ponytail |  |
| 5 | `pbakaus/impeccable` | 73956 | 4462 | JavaScript | 495 stars today | 让您的人工智能更好地进行设计的设计语言。 | https://github.com/pbakaus/impeccable |  |
| 6 | `mattpocock/skills` | 274312 | 23042 | Shell | 883 stars today | 真正工程师的技能。直接来自我的.agents目录。 | https://github.com/mattpocock/skills |  |
| 7 | `NVIDIA/OpenShell` | 14220 | 1643 | Rust | 2,456 stars today | OpenShell是自主AI代理的安全、私有运行时。 | https://github.com/NVIDIA/OpenShell |  |
| 8 | `coreyhaines31/marketingskills` | 52223 | 7870 | JavaScript | 139 stars today | Claude Code和人工智能代理的营销技能。CRO、文案撰写、搜索引擎优化、分析和增长工程。 | https://github.com/coreyhaines31/marketingskills | 新增 |
| 9 | `heygen-com/hyperframes` | 55581 | 5033 | TypeScript | 627 stars today | 编写HTML。渲染视频。专为客服代表打造。 | https://github.com/heygen-com/hyperframes |  |
| 10 | `mksglu/context-mode` | 24910 | 1790 | TypeScript | 362 stars today | 人工智能编码代理的上下文窗口优化。沙盒工具输出（减少98 ％ ） ，保持会话内存，并通过MCP +钩子在17个平台上强制路由。 | https://github.com/mksglu/context-mode |  |
| 11 | `google/skills` | 20591 | 1711 | Python | 30 stars today | Google产品和技术的代理技能 | https://github.com/google/skills | 新增 |
| 12 | `getsentry/sentry` | 44912 | 4881 | Python | 12 stars today | 开发人员优先的错误跟踪和性能监控 | https://github.com/getsentry/sentry | 新增 |
| 13 | `colbymchenry/codegraph` | 72818 | 4677 | C | 241 stars today | 预索引的代码知识图，在代码更改时自动同步，适用于Claude Code、Codex、Gemini、Cursor、OpenCode、AntiGravity、Kiro、CoPilot和Hermes Agent —代币更少，工具调用更少， 100%本地 | https://github.com/colbymchenry/codegraph | 新增 |
| 14 | `cursor/plugins` | 9395 | 887 | TypeScript | 150 stars today | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 15 | `mvschwarz/openrig` | 3992 | 264 | TypeScript | 642 stars today | 从Claude Code、Codex和Pi构建您自己的代理网络：具有角色、共享上下文和所有工作的持久团队。 | https://github.com/mvschwarz/openrig |  |
| 16 | `Effect-TS/effect` | 16384 | 793 | TypeScript | 76 stars today | 在TypeScript中构建生产就绪应用程序 | https://github.com/Effect-TS/effect | 新增 |
| 17 | `pablostanley/yoinks` | 3196 | 295 | TypeScript | 361 stars today | yoink您终端上的任何视频。没有阴暗的广告。 | https://github.com/pablostanley/yoinks |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `paperclipai/paperclip` | 96051 | 16278 | TypeScript | 14,335 stars this week | 每个人都使用的开源应用程序来管理工作中的代理 | https://github.com/paperclipai/paperclip |  |
| 2 | `vectorize-io/hindsight` | 44504 | 5858 | Python | 17,403 stars this week | 后见之明：学习的客服代表记忆 | https://github.com/vectorize-io/hindsight |  |
| 3 | `debpalash/VoiceStudio` | 51637 | 5756 | Python | 16,114 stars this week | VoiceStudio是开源、完全本地的ElevenLabs替代品--语音克隆、语音设计、视频配音、听写、转录和有声读物创作，支持646种语言。 | https://github.com/debpalash/VoiceStudio |  |
| 4 | `rohitg00/ai-engineering-from-scratch` | 62562 | 10697 | Python | 6,469 stars this week | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 5 | `flutter/flutter` | 179226 | 32764 | Dart | 147 stars this week | Flutter可以轻松快速地为移动设备及其他设备构建漂亮的应用程序 | https://github.com/flutter/flutter |  |
| 6 | `pbakaus/impeccable` | 73956 | 4462 | JavaScript | 2,704 stars this week | 让您的人工智能更好地进行设计的设计语言。 | https://github.com/pbakaus/impeccable |  |
| 7 | `vercel/next.js` | 142982 | 33580 | JavaScript | 624 stars this week | React框架 | https://github.com/vercel/next.js |  |
| 8 | `alirezarezvani/claude-skills` | 27238 | 3845 | Python | 743 stars this week | 380 Claude Code技能和代理技能和插件（ 30 +代理、70 +自定义命令、380 +技能、可定制参考、脚本） ，适用于Claude Code、Codex、Gemini CLI、Cursor和其他8个编码代理—工程、营销、产品、合规、C级咨询、研究…… | https://github.com/alirezarezvani/claude-skills |  |
| 9 | `heygen-com/hyperframes` | 55581 | 5033 | TypeScript | 2,667 stars this week | 编写HTML。渲染视频。专为客服代表打造。 | https://github.com/heygen-com/hyperframes | 新增 |
| 10 | `TencentCloud/Octop` | 6315 | 788 | Python | 1,360 stars this week | 更智能、自托管的人工智能助手—多用户、多代理。 | https://github.com/TencentCloud/Octop |  |
| 11 | `google/ax` | 12825 | 629 | Go | 2,919 stars this week | Google的开放代理编排运行时 | https://github.com/google/ax | 新增 |
| 12 | `anthropics/financial-services` | 38508 | 5540 | Python | 1,270 stars this week | — | https://github.com/anthropics/financial-services |  |
| 13 | `tile-ai/tilelang` | 8207 | 824 | Python | 481 stars this week | 特定于领域的语言，旨在简化高性能GPU/CPU/加速器内核的开发 | https://github.com/tile-ai/tilelang |  |
| 14 | `anthropics/claude-code-action` | 9352 | 2184 | TypeScript | 376 stars this week | — | https://github.com/anthropics/claude-code-action |  |
| 15 | `pytorch/pytorch` | 103612 | 31055 | Python | 376 stars this week | 具有强GPU加速的Python中的张量和动态神经网络 | https://github.com/pytorch/pytorch | 新增 |
| 16 | `harry0703/MoneyPrinterTurbo` | 128041 | 20041 | Python | 2,548 stars this week | 利用 AI 大模型和自动化工作流，根据主题或关键词一键生成高清短视频。Generate HD short videos from a topic or keyword with an automated AI workflow. | https://github.com/harry0703/MoneyPrinterTurbo | 新增 |
| 17 | `pablostanley/yoinks` | 3196 | 295 | TypeScript | 1,069 stars this week | yoink您终端上的任何视频。没有阴暗的广告。 | https://github.com/pablostanley/yoinks | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `bilawalsidhu/gods-eye-view` | 46378 | 9492 | JavaScript | 31,240 stars this month | 浏览器中的间谍卫星模拟器，但数据是真实的。在逼真的3D地球仪上实时开源空间智能。 | https://github.com/bilawalsidhu/gods-eye-view |  |
| 2 | `alibaba/open-code-review` | 43268 | 3117 | Go | 21,646 stars this month | 安全、快速、高效，经受住阿里巴巴规模的考验。混合架构代码审核工具：确定性流水线+ LLM Agent、精确的行级注释、内置多语言规则集（ NPE、线程安全、XSS、SQL注入）、OpenAI &amp; Anthropic兼容。 | https://github.com/alibaba/open-code-review |  |
| 3 | `affaan-m/ECC` | 270926 | 40505 | JavaScript | 26,450 stars this month | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 4 | `ayghri/i-have-adhd` | 52818 | 3041 | Python | 26,584 stars this month | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 5 | `Tencent/WeKnora` | 31713 | 4233 | Go | 10,740 stars this month | 开源LLM知识平台：将原始文档转化为可查询的RAG、自主推理代理和自我维护的Wiki。 | https://github.com/Tencent/WeKnora |  |
| 6 | `tt-a1i/archify` | 76064 | 5120 | JavaScript | 35,068 stars this month | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify |  |
| 7 | `paperclipai/paperclip` | 96051 | 16278 | TypeScript | 16,130 stars this month | 每个人都使用的开源应用程序来管理工作中的代理 | https://github.com/paperclipai/paperclip |  |
| 8 | `anthropics/financial-services` | 38508 | 5540 | Python | 3,930 stars this month | — | https://github.com/anthropics/financial-services |  |
| 9 | `mksglu/context-mode` | 24910 | 1790 | TypeScript | 4,470 stars this month | 人工智能编码代理的上下文窗口优化。沙盒工具输出（减少98 ％ ） ，保持会话内存，并通过MCP +钩子在17个平台上强制路由。 | https://github.com/mksglu/context-mode |  |
| 10 | `superdesigndev/treg` | 4015 | 332 | Python | 3,249 stars this month | 适用于代理工具的OpenRouter。在这里加入社区： https://discord.gg/6mQYYfFMAn | https://github.com/superdesigndev/treg |  |
| 11 | `vectorize-io/hindsight` | 44504 | 5858 | Python | 22,416 stars this month | 后见之明：学习的客服代表记忆 | https://github.com/vectorize-io/hindsight |  |
| 12 | `heygen-com/hyperframes` | 55581 | 5033 | TypeScript | 11,734 stars this month | 编写HTML。渲染视频。专为客服代表打造。 | https://github.com/heygen-com/hyperframes |  |
| 13 | `DietrichGebert/ponytail` | 151125 | 8107 | JavaScript | 31,160 stars this month | 让你的人工智能代理像房间里最懒惰的高级开发人员一样思考。最好的代码是你从未写过的代码。 | https://github.com/DietrichGebert/ponytail |  |
| 14 | `anthropics/claude-code` | 148932 | 25156 | TypeScript | 5,819 stars this month | Claude Code是一个代理编码工具，它位于您的终端中，了解您的代码库，并通过执行日常任务、解释复杂代码和处理git工作流程（所有这些都通过自然语言命令）来帮助您更快地进行编码。 | https://github.com/anthropics/claude-code |  |
| 15 | `TencentCloud/Octop` | 6315 | 788 | Python | 4,888 stars this month | 更智能、自托管的人工智能助手—多用户、多代理。 | https://github.com/TencentCloud/Octop |  |
| 16 | `trycua/cua` | 27740 | 1952 | Rust | 5,674 stars this month | 通过开源驱动程序、跨操作系统车队以及培训、评估和数据生成的基准来扩展计算机使用2.0。 | https://github.com/trycua/cua |  |
| 17 | `cursor/plugins` | 9395 | 887 | TypeScript | 2,977 stars this month | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 18 | `max-sixty/worktrunk` | 8642 | 309 | Rust | 1,903 stars this month | Worktrunk是用于Git工作树管理的CLI ，专为并行AI代理工作流程而设计 | https://github.com/max-sixty/worktrunk |  |
| 19 | `tashfeenahmed/freellmapi` | 30075 | 4212 | TypeScript | 6,611 stars this month | 每月74亿个代币。34个免费LLM提供商。635个免费模型端点。全部在一个/v1端点后面，加上任何与OpenAI兼容的自定义端点。智能路由、自动故障转移、加密密钥。仅限个人实验。 | https://github.com/tashfeenahmed/freellmapi |  |
| 20 | `anthropics/knowledge-work-plugins` | 25965 | 3050 | Python | 2,254 stars this month | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins | 新增 |
| 21 | `THU-MAIC/OpenMAIC` | 39801 | 6167 | TypeScript | 11,062 stars this month | 开放式多座席互动课堂—只需点击一下，即可获得身临其境的多座席学习体验 | https://github.com/THU-MAIC/OpenMAIC |  |
| 22 | `NVIDIA/SkillSpector` | 19029 | 1656 | Python | 3,423 stars this month | 人工智能代理技能的安全扫描仪。在安装之前，检测Claude Code、Codex和MCP技能中的漏洞、恶意模式、安全风险、提示注入、数据泄露和供应链风险。 | https://github.com/NVIDIA/SkillSpector |  |
| 23 | `longbridge/gpui-kit` | 15600 | 964 | Rust | 1,786 stars this month | 使用GPUI构建梦幻般的跨平台桌面应用程序的Rust GUI组件。 | https://github.com/longbridge/gpui-kit |  |


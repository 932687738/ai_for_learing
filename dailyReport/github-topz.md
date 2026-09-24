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

**最近一次更新时间**（Asia/Shanghai）： 2026-09-24 09:15:33

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 549081 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 509472 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 482575 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 456049 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 397532 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 390348 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `donnemartin/system-design-primer` | 371472 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 8 | `nilbuild/developer-roadmap` | 367981 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 9 | `jwasham/coding-interview-university` | 361778 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 11 | `vinta/awesome-python` | 322584 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `anthropics/financial-services` | 36946 | 5377 | Python | 664 stars today | — | https://github.com/anthropics/financial-services |  |
| 2 | `google/ax` | 9075 | 436 | Go | 1,543 stars today | Google的开放代理编排运行时 | https://github.com/google/ax |  |
| 3 | `davila7/claude-code-templates` | 31503 | 3580 | Python | 389 stars today | 用于配置和监控Claude Code的CLI工具 | https://github.com/davila7/claude-code-templates |  |
| 4 | `BuilderIO/agent-native` | 6548 | 587 | TypeScript | 87 stars today | 构建代理应用的框架 | https://github.com/BuilderIO/agent-native | 新增 |
| 5 | `obra/superpowers` | 290687 | 26012 | Shell | 474 stars today | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers | 新增 |
| 6 | `dream-num/univer` | 16334 | 1435 | TypeScript | 1,142 stars today | 适用于AI代理的Office线束—电子表格、文档、幻灯片、画布、关系表和PDF在一个运行时中。 | https://github.com/dream-num/univer |  |
| 7 | `Open-Dev-Society/OpenStock` | 18833 | 2286 | TypeScript | 344 stars today | OpenStock是昂贵市场平台的开源替代品。实时跟踪价格，设置个性化提醒，并探索详细的公司洞察--为每个人公开构建，永远免费。 | https://github.com/Open-Dev-Society/OpenStock | 新增 |
| 8 | `agent-substrate/substrate` | 3501 | 413 | Go | 558 stars today | Agent Substrate ：核心系统 | https://github.com/agent-substrate/substrate |  |
| 9 | `strands-agents/harness-sdk` | 7846 | 1201 | Python | 115 stars today | 构建代理线束并进行端到端控制。适用于Python和TypeScript中生产AI代理的开源SDK -任何模型，任何云。 | https://github.com/strands-agents/harness-sdk | 新增 |
| 10 | `HKUDS/CLI-Anything` | 49931 | 4601 | Python | 57 stars today | "CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub: https://clianything.cc/ | https://github.com/HKUDS/CLI-Anything | 新增 |
| 11 | `superdesigndev/treg` | 2718 | 242 | Python | 506 stars today | 适用于代理工具的OpenRouter。在这里加入社区： https://discord.gg/6mQYYfFMAn | https://github.com/superdesigndev/treg |  |
| 12 | `pbakaus/impeccable` | 70345 | 4271 | JavaScript | 304 stars today | 让您的人工智能更好地进行设计的设计语言。 | https://github.com/pbakaus/impeccable | 新增 |
| 13 | `mvt-project/mvt` | 14483 | 1383 | Python | 543 stars today | MVT （移动验证工具包）有助于对移动设备进行取证，以发现潜在泄露的迹象。 | https://github.com/mvt-project/mvt |  |
| 14 | `DeusData/codebase-memory-mcp` | 44569 | 3638 | C | 190 stars today | 高性能代码智能MCP服务器。将代码库编入持久知识图表—以毫秒为单位的平均存储库。158种语言，子MS查询，令牌减少99 ％。单个静态二进制文件，零依赖关系。 | https://github.com/DeusData/codebase-memory-mcp | 新增 |
| 15 | `harry7557558/spirula-studio` | 741 | 56 | C++ | 69 stars today | 跨供应商3D高斯溅射训练器-溅射到网格、Vulkan或CUDA的视频。 | https://github.com/harry7557558/spirula-studio | 新增 |
| 16 | `browser-use/video-use` | 26495 | 3166 | Python | 746 stars today | 使用编码代理编辑视频 | https://github.com/browser-use/video-use |  |
| 17 | `TNT-Likely/PanWatch` | 1508 | 298 | Python | 95 stars today | 盯盘侠 PanWatch · 自托管 AI 盯盘助手，集成 TradingAgents 多 Agent 投资决策 · A股/港股/美股实时监控、持仓管理、智能分析、全渠道推送 | https://github.com/TNT-Likely/PanWatch | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `alibaba/open-code-review` | 40203 | 2887 | Go | 9,833 stars this week | 安全、快速、高效，经受住阿里巴巴规模的考验。混合架构代码审核工具：确定性流水线+ LLM Agent、精确的行级注释、内置多语言规则集（ NPE、线程安全、XSS、SQL注入）、OpenAI &amp; Anthropic兼容。 | https://github.com/alibaba/open-code-review |  |
| 2 | `anthropics/claude-code` | 147811 | 24219 | TypeScript | 2,762 stars this week | Claude Code是一个代理编码工具，它位于您的终端中，了解您的代码库，并通过执行日常任务、解释复杂代码和处理git工作流程（所有这些都通过自然语言命令）来帮助您更快地进行编码。 | https://github.com/anthropics/claude-code |  |
| 3 | `anthropics/financial-services` | 36947 | 5377 | Python | 1,895 stars this week | — | https://github.com/anthropics/financial-services |  |
| 4 | `Tencent/WeKnora` | 29353 | 3950 | Go | 4,522 stars this week | 开源LLM知识平台：将原始文档转化为可查询的RAG、自主推理代理和自我维护的Wiki。 | https://github.com/Tencent/WeKnora |  |
| 5 | `affaan-m/ECC` | 266196 | 39781 | JavaScript | 6,695 stars this week | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 6 | `addyosmani/agent-skills` | 98717 | 10371 | JavaScript | 3,867 stars this week | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 7 | `anthropics/knowledge-work-plugins` | 25501 | 3024 | Python | 1,358 stars this week | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins |  |
| 8 | `JustVugg/colibri` | 37363 | 4037 | C | 2,739 stars this week | 在您已经拥有的硬件上运行前沿MoE模型—纯C ，零DEPS ，从磁盘流式传输的专家。微型引擎，超大型号。 🐦 | https://github.com/JustVugg/colibri |  |
| 9 | `TencentCloud/Octop` | 4763 | 563 | Python | 1,877 stars this week | 更智能、自托管的人工智能助手—多用户、多代理。 | https://github.com/TencentCloud/Octop |  |
| 10 | `stablyai/orca` | 76602 | 5019 | TypeScript | 6,435 stars this week | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面、移动和远程运行时使用。 | https://github.com/stablyai/orca |  |
| 11 | `davila7/claude-code-templates` | 31503 | 3580 | Python | 613 stars this week | 用于配置和监控Claude Code的CLI工具 | https://github.com/davila7/claude-code-templates | 新增 |
| 12 | `cloudflare/quiche` | 12537 | 1145 | Rust | 707 stars this week | 🥧 QUIC传输协议和HTTP/3的有效实施 | https://github.com/cloudflare/quiche |  |
| 13 | `danny-avila/LibreChat` | 44797 | 9187 | TypeScript | 949 stars this week | 增强的ChatGPT克隆：功能Agent、MCP、Skills、DeepSeek、Anthropic、AWS、OpenAI、Responses API、Azure、Groq、o1、GPT-5、Mistral、OpenRouter、Vertex AI、Gemini、Artifacts、AI模型切换、消息搜索、Code Interpreter、langchain、DALL-E-3、OpenAPI Actions、Functions…… | https://github.com/danny-avila/LibreChat |  |
| 14 | `cline/cline` | 69182 | 7498 | TypeScript | 1,177 stars this week | 自主编码代理作为SDK、IDE扩展或CLI助手。 | https://github.com/cline/cline |  |
| 15 | `pytorch/pytorch` | 103218 | 30094 | Python | 196 stars this week | 具有强GPU加速的Python中的张量和动态神经网络 | https://github.com/pytorch/pytorch | 新增 |
| 16 | `cilium/cilium` | 25494 | 4098 | Go | 447 stars this week | 基于eBPF的网络、安全性和可观察性 | https://github.com/cilium/cilium |  |
| 17 | `Fission-AI/OpenSpec` | 70057 | 4793 | TypeScript | 1,538 stars this week | AI编码助手的规范驱动开发（ SDD ）。 | https://github.com/Fission-AI/OpenSpec | 新增 |
| 18 | `cloudflare/security-audit-skill` | 20917 | 1198 | JavaScript | 15,280 stars this week | 用于多阶段安全审核的编码代理技能，具有经过独立验证的机器可读结果 | https://github.com/cloudflare/security-audit-skill |  |
| 19 | `Open-Dev-Society/OpenStock` | 18833 | 2286 | TypeScript | 4,356 stars this week | OpenStock是昂贵市场平台的开源替代品。实时跟踪价格，设置个性化提醒，并探索详细的公司洞察--为每个人公开构建，永远免费。 | https://github.com/Open-Dev-Society/OpenStock |  |
| 20 | `superdesigndev/treg` | 2719 | 242 | Python | 1,067 stars this week | 适用于代理工具的OpenRouter。在这里加入社区： https://discord.gg/6mQYYfFMAn | https://github.com/superdesigndev/treg | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `bilawalsidhu/gods-eye-view` | 41912 | 8530 | JavaScript | 41,118 stars this month | 浏览器中的间谍卫星模拟器，但数据是真实的。在逼真的3D地球仪上实时开源空间智能。 | https://github.com/bilawalsidhu/gods-eye-view | 新增 |
| 2 | `tt-a1i/archify` | 70618 | 4748 | JavaScript | 55,857 stars this month | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify |  |
| 3 | `cloudflare/security-audit-skill` | 20917 | 1198 | JavaScript | 17,893 stars this month | 用于多阶段安全审核的编码代理技能，具有经过独立验证的机器可读结果 | https://github.com/cloudflare/security-audit-skill |  |
| 4 | `THU-MAIC/OpenMAIC` | 38793 | 6065 | TypeScript | 18,072 stars this month | 开放式多座席互动课堂—只需点击一下，即可获得身临其境的多座席学习体验 | https://github.com/THU-MAIC/OpenMAIC |  |
| 5 | `alibaba/open-code-review` | 40204 | 2887 | Go | 19,196 stars this month | 安全、快速、高效，经受住阿里巴巴规模的考验。混合架构代码审核工具：确定性流水线+ LLM Agent、精确的行级注释、内置多语言规则集（ NPE、线程安全、XSS、SQL注入）、OpenAI &amp; Anthropic兼容。 | https://github.com/alibaba/open-code-review |  |
| 6 | `debpalash/VoiceStudio` | 34900 | 4121 | Python | 23,623 stars this month | VoiceStudio是开源、完全本地的ElevenLabs替代品--语音克隆、语音设计、视频配音、听写、转录和有声读物创作，支持646种语言。 | https://github.com/debpalash/VoiceStudio |  |
| 7 | `ayghri/i-have-adhd` | 50697 | 2927 | Python | 27,477 stars this month | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 8 | `cursor/plugins` | 8499 | 795 | TypeScript | 3,900 stars this month | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 9 | `zedeus/nitter` | 14482 | 1366 | Nim | 1,046 stars this month | 替代Twitter前端 | https://github.com/zedeus/nitter | 新增 |
| 10 | `magnitudedev/magnitude` | 4947 | 374 | TypeScript | 3,430 stars this month | 您已拥有硬件的开源推理引擎。分析您的机器，为其推荐最佳的开放型号，并针对您的确切硬件进行调整。适用于Apple Silicon、NVIDIA、AMD或CPU。 | https://github.com/magnitudedev/magnitude |  |
| 11 | `Lakr233/vphone-cli` | 14310 | 1688 | Swift | 6,370 stars this month | — | https://github.com/Lakr233/vphone-cli |  |
| 12 | `freestylefly/awesome-gpt-image-2` | 33397 | 3216 | JavaScript | 21,457 stars this month | Prompt as Code · GPT Image 2 / 2.5 提示词与案例库，530+ 个案例、20+ 套工业级模板与可复用 Skills，新增 2.5 同提示词对比专区，附完整提示词与生成记录，持续更新。 | https://github.com/freestylefly/awesome-gpt-image-2 |  |
| 13 | `tech-leads-club/agent-skills` | 6716 | 551 | TypeScript | 1,759 stars this month | 专业AI编码代理的安全、经过验证的技能注册表。绝对自信地扩展Antigravity、Claude Code、Cursor、Copilot等。 | https://github.com/tech-leads-club/agent-skills |  |
| 14 | `omacom/omarchy` | 42879 | 4966 | Shell | 14,577 stars this month | 漂亮、现代且自以为是的Linux | https://github.com/omacom/omarchy |  |
| 15 | `Tencent/WeKnora` | 29353 | 3950 | Go | 9,078 stars this month | 开源LLM知识平台：将原始文档转化为可查询的RAG、自主推理代理和自我维护的Wiki。 | https://github.com/Tencent/WeKnora |  |
| 16 | `google-research/timesfm` | 33580 | 3242 | Python | 5,563 stars this month | TimesFM （时间序列基础模型）是由Google Research开发的用于时间序列预测的预训练时间序列基础模型。 | https://github.com/google-research/timesfm |  |
| 17 | `jingyaogong/minimind` | 62338 | 8106 | Python | 7,561 stars this month | 在短短2小时内从头开始🧠培训64M参数LLM ！ | https://github.com/jingyaogong/minimind |  |
| 18 | `Tencent/BrowserSkill` | 6926 | 501 | TypeScript | 5,647 stars this month | 让人工智能代理使用您真实登录的浏览器，而不会中断您的工作。CLI +扩展用于跨任何支持外壳的AI代理的浏览器自动化。 | https://github.com/Tencent/BrowserSkill |  |
| 19 | `every-app/open-seo` | 20560 | 2635 | TypeScript | 7,313 stars this month | Semrush和Ahrefs的开源替代品 | https://github.com/every-app/open-seo |  |
| 20 | `K-Dense-AI/scientific-agent-skills` | 46347 | 4195 | Python | 12,304 stars this month | 将任何AI特工变成AI科学家。首屈一指的科学代理技能库，全球超过19万名科学家使用。165项随时可用的经验证的技能，以及100多个涵盖生物学、化学、医学和药物发现的科学数据库。兼容Cursor、Claude Code…… | https://github.com/K-Dense-AI/scientific-agent-skills | 新增 |
| 21 | `melgarafael/DeskcommCRM` | 3613 | 900 | TypeScript | 3,113 stars this month | 开源AI销售操作系统—使用本地AI代理+ WhatsApp (WAHA)的自托管CRM。对于任何通过聊天销售的企业， Kommo、Octadesk和Intercom的替代方案都是开放的。MCP就绪、多租户、LGPD。 | https://github.com/melgarafael/DeskcommCRM |  |


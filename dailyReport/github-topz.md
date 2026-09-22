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

**最近一次更新时间**（Asia/Shanghai）： 2026-09-22 09:16:01

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 548649 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 508658 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 482090 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 455912 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 397378 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 390223 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `donnemartin/system-design-primer` | 371152 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 8 | `nilbuild/developer-roadmap` | 367849 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 9 | `jwasham/coding-interview-university` | 361646 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 11 | `vinta/awesome-python` | 322168 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `BuilderIO/agent-native` | 5920 | 536 | TypeScript | 607 stars today | 构建代理应用的框架 | https://github.com/BuilderIO/agent-native |  |
| 2 | `trycua/cua` | 25702 | 1768 | HTML | 609 stars today | 通过开源驱动程序、跨操作系统车队以及培训、评估和数据生成的基准来扩展计算机使用2.0。 | https://github.com/trycua/cua |  |
| 3 | `Open-Dev-Society/OpenStock` | 17745 | 2195 | TypeScript | 844 stars today | OpenStock是昂贵市场平台的开源替代品。实时跟踪价格，设置个性化提醒，并探索详细的公司洞察--为每个人公开构建，永远免费。 | https://github.com/Open-Dev-Society/OpenStock |  |
| 4 | `akitaonrails/ai-memory` | 7693 | 521 | Rust | 167 stars today | 针对座席编码CLI的长期记忆解决方案，以及促进不同座席供应商之间切换的解决方案 | https://github.com/akitaonrails/ai-memory | 新增 |
| 5 | `coder/coder` | 16430 | 1565 | Go | 460 stars today | 为开发人员及其代理提供安全的环境 | https://github.com/coder/coder |  |
| 6 | `anthropics/financial-services` | 35840 | 5268 | Python | 424 stars today | — | https://github.com/anthropics/financial-services |  |
| 7 | `cloudflare/quiche` | 12360 | 1133 | Rust | 32 stars today | 🥧 QUIC传输协议和HTTP/3的有效实施 | https://github.com/cloudflare/quiche | 新增 |
| 8 | `mvt-project/mvt` | 13601 | 1325 | Python | 169 stars today | MVT （移动验证工具包）有助于对移动设备进行取证，以发现潜在泄露的迹象。 | https://github.com/mvt-project/mvt | 新增 |
| 9 | `zhouxiaoka/autoclip` | 8255 | 1572 | Python | 250 stars today | AutoClip : AI-powered video clipping and highlight generation · 一款智能高光提取与剪辑的二创工具 | https://github.com/zhouxiaoka/autoclip | 新增 |
| 10 | `ruanyf/weekly` | 103945 | 4447 | — | 182 stars today | 科技爱好者周刊，每周五发布 | https://github.com/ruanyf/weekly | 新增 |
| 11 | `Crosstalk-Solutions/project-nomad` | 37873 | 3767 | TypeScript | 394 stars today | Project NOMAD是一个离线优先的知识和教育服务器。维基百科、成千上万的书籍、课程、地图和可选的本地人工智能，所有这些都运行在您拥有的硬件上，无需互联网。 | https://github.com/Crosstalk-Solutions/project-nomad | 新增 |
| 12 | `yynxxxxx/Codex-X` | 3691 | 462 | Rust | 50 stars today | OpenAI Codex 桌面端/CLI 的可视化管理工具，具有Provider/API 切换、会话同步、提示词注入、Skills/MCP 管理、TOML 配置可视化的跨平台工具。 | https://github.com/yynxxxxx/Codex-X | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `alibaba/open-code-review` | 39218 | 2806 | Go | 14,499 stars this week | 安全、快速、高效，经受住阿里巴巴规模的考验。混合架构代码审核工具：确定性流水线+ LLM Agent、精确的行级注释、内置多语言规则集（ NPE、线程安全、XSS、SQL注入）、OpenAI &amp; Anthropic兼容。 | https://github.com/alibaba/open-code-review |  |
| 2 | `anthropics/claude-code` | 147471 | 24114 | TypeScript | 2,731 stars this week | Claude Code是一个代理编码工具，它位于您的终端中，了解您的代码库，并通过执行日常任务、解释复杂代码和处理git工作流程（所有这些都通过自然语言命令）来帮助您更快地进行编码。 | https://github.com/anthropics/claude-code |  |
| 3 | `JustVugg/colibri` | 36868 | 3945 | C | 5,565 stars this week | 在您已经拥有的硬件上运行前沿MoE模型—纯C ，零DEPS ，从磁盘流式传输的专家。微型引擎，超大型号。 🐦 | https://github.com/JustVugg/colibri | 新增 |
| 4 | `Tencent/WeKnora` | 28521 | 3834 | Go | 5,455 stars this week | 开源LLM知识平台：将原始文档转化为可查询的RAG、自主推理代理和自我维护的Wiki。 | https://github.com/Tencent/WeKnora |  |
| 5 | `affaan-m/ECC` | 264759 | 39564 | JavaScript | 6,865 stars this week | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 6 | `anthropics/knowledge-work-plugins` | 25361 | 3016 | Python | 1,350 stars this week | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins |  |
| 7 | `addyosmani/agent-skills` | 98141 | 10319 | JavaScript | 4,197 stars this week | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 8 | `stablyai/orca` | 74708 | 4884 | TypeScript | 6,125 stars this week | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面、移动和远程运行时使用。 | https://github.com/stablyai/orca |  |
| 9 | `mksglu/context-mode` | 23888 | 1722 | TypeScript | 1,089 stars this week | 人工智能编码代理的上下文窗口优化。沙盒工具输出（减少98 ％ ） ，保持会话内存，并通过MCP +钩子在17个平台上强制路由。 | https://github.com/mksglu/context-mode |  |
| 10 | `home-assistant/core` | 90978 | 38722 | Python | 526 stars this week | 🏡 开源家庭自动化，将本地控制和隐私放在首位。 | https://github.com/home-assistant/core |  |
| 11 | `danny-avila/LibreChat` | 44584 | 9152 | TypeScript | 1,401 stars this week | 增强的ChatGPT克隆：功能Agent、MCP、Skills、DeepSeek、Anthropic、AWS、OpenAI、Responses API、Azure、Groq、o1、GPT-5、Mistral、OpenRouter、Vertex AI、Gemini、Artifacts、AI模型切换、消息搜索、Code Interpreter、langchain、DALL-E-3、OpenAPI Actions、Functions…… | https://github.com/danny-avila/LibreChat |  |
| 12 | `bilawalsidhu/gods-eye-view` | 40611 | 8249 | JavaScript | 7,318 stars this week | 浏览器中的间谍卫星模拟器，但数据是真实的。在逼真的3D地球仪上实时开源空间智能。 | https://github.com/bilawalsidhu/gods-eye-view |  |
| 13 | `Panniantong/Agent-Reach` | 84379 | 7411 | Python | 3,526 stars this week | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 14 | `blader/humanizer` | 51089 | 4099 | Python | 3,023 stars this week | 从文本中删除人工智能生成文字的迹象的代理技能 | https://github.com/blader/humanizer |  |
| 15 | `cline/cline` | 68979 | 7474 | TypeScript | 1,204 stars this week | 自主编码代理作为SDK、IDE扩展或CLI助手。 | https://github.com/cline/cline |  |
| 16 | `max-sixty/worktrunk` | 8298 | 290 | Rust | 751 stars this week | Worktrunk是用于Git工作树管理的CLI ，专为并行AI代理工作流程而设计 | https://github.com/max-sixty/worktrunk |  |
| 17 | `cloudflare/quiche` | 12360 | 1133 | Rust | 345 stars this week | 🥧 QUIC传输协议和HTTP/3的有效实施 | https://github.com/cloudflare/quiche | 新增 |
| 18 | `cilium/cilium` | 25425 | 4085 | Go | 412 stars this week | 基于eBPF的网络、安全性和可观察性 | https://github.com/cilium/cilium |  |
| 19 | `supabase/supabase` | 110529 | 14513 | TypeScript | 1,518 stars this week | Postgres开发平台。Supabase为您提供了一个专用的Postgres数据库，用于构建您的Web、移动和人工智能应用程序。 | https://github.com/supabase/supabase |  |
| 20 | `cloudflare/security-audit-skill` | 19011 | 1065 | JavaScript | 15,675 stars this week | 用于多阶段安全审核的编码代理技能，具有经过独立验证的机器可读结果 | https://github.com/cloudflare/security-audit-skill | 新增 |
| 21 | `vastsa/PI-Desktop` | 4969 | 415 | TypeScript | 1,370 stars this week | 本地优先AI编码代理桌面： Electron + Rust host core + pi Agent Harness +用户可安装插件 | https://github.com/vastsa/PI-Desktop | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `tt-a1i/archify` | 69134 | 4636 | JavaScript | 54,494 stars this month | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify |  |
| 2 | `FlashML-org/FreeToken` | 13470 | 1329 | Python | 13,373 stars this month | FreeToken将数据中心规模的模型提供给您的桌面。在本地快速高效地运行大规模模型。 | https://github.com/FlashML-org/FreeToken | 新增 |
| 3 | `THU-MAIC/OpenMAIC` | 38445 | 6024 | TypeScript | 17,721 stars this month | 开放式多座席互动课堂—只需点击一下，即可获得身临其境的多座席学习体验 | https://github.com/THU-MAIC/OpenMAIC |  |
| 4 | `anthropics/claude-plugins-community` | 4353 | 312 | Python | 4,049 stars this month | Claude Cowork和Claude Code的社区插件市场。只读镜像—在clau.de/plugin-directory-submission上提交插件。 | https://github.com/anthropics/claude-plugins-community |  |
| 5 | `cloudflare/security-audit-skill` | 19013 | 1065 | JavaScript | 15,924 stars this month | 用于多阶段安全审核的编码代理技能，具有经过独立验证的机器可读结果 | https://github.com/cloudflare/security-audit-skill |  |
| 6 | `freestylefly/awesome-gpt-image-2` | 33163 | 3193 | JavaScript | 22,108 stars this month | Prompt as Code · GPT Image 2 / 2.5 提示词与案例库，530+ 个案例、20+ 套工业级模板与可复用 Skills，新增 2.5 同提示词对比专区，附完整提示词与生成记录，持续更新。 | https://github.com/freestylefly/awesome-gpt-image-2 |  |
| 7 | `cursor/plugins` | 8313 | 774 | TypeScript | 4,224 stars this month | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 8 | `debpalash/VoiceStudio` | 33922 | 3989 | Python | 22,973 stars this month | VoiceStudio是开源、完全本地的ElevenLabs替代品--语音克隆、语音设计、视频配音、听写、转录和有声读物创作，支持646种语言。 | https://github.com/debpalash/VoiceStudio |  |
| 9 | `omacom/omarchy` | 42547 | 4918 | Shell | 15,721 stars this month | 漂亮、现代且自以为是的Linux | https://github.com/omacom/omarchy |  |
| 10 | `ayghri/i-have-adhd` | 49846 | 2875 | Python | 27,004 stars this month | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 11 | `alibaba/open-code-review` | 39221 | 2805 | Go | 18,217 stars this month | 安全、快速、高效，经受住阿里巴巴规模的考验。混合架构代码审核工具：确定性流水线+ LLM Agent、精确的行级注释、内置多语言规则集（ NPE、线程安全、XSS、SQL注入）、OpenAI &amp; Anthropic兼容。 | https://github.com/alibaba/open-code-review |  |
| 12 | `magnitudedev/magnitude` | 4771 | 367 | TypeScript | 3,303 stars this month | 针对消费硬件优化的开源推理引擎。分析您的机器，为其推荐最佳型号，然后下载、调整和运行它们。适用于Apple Silicon、NVIDIA、AMD或CPU。 | https://github.com/magnitudedev/magnitude | 新增 |
| 13 | `Lakr233/vphone-cli` | 14177 | 1679 | Swift | 6,273 stars this month | — | https://github.com/Lakr233/vphone-cli |  |
| 14 | `tech-leads-club/agent-skills` | 6603 | 544 | TypeScript | 1,658 stars this month | 专业AI编码代理的安全、经过验证的技能注册表。绝对自信地扩展Antigravity、Claude Code、Cursor、Copilot等。 | https://github.com/tech-leads-club/agent-skills |  |
| 15 | `vorssaint/vorssaint-utils` | 20414 | 748 | Swift | 14,671 stars this month | 免费开源的macOS菜单栏工具包。 | https://github.com/vorssaint/vorssaint-utils |  |
| 16 | `google-research/timesfm` | 33405 | 3224 | Python | 5,427 stars this month | TimesFM （时间序列基础模型）是由Google Research开发的用于时间序列预测的预训练时间序列基础模型。 | https://github.com/google-research/timesfm |  |
| 17 | `Tencent/WeKnora` | 28523 | 3835 | Go | 8,321 stars this month | 开源LLM知识平台：将原始文档转化为可查询的RAG、自主推理代理和自我维护的Wiki。 | https://github.com/Tencent/WeKnora |  |
| 18 | `jingyaogong/minimind` | 62037 | 8075 | Python | 7,274 stars this month | 在短短2小时内从头开始🧠培训64M参数LLM ！ | https://github.com/jingyaogong/minimind |  |
| 19 | `Tencent/BrowserSkill` | 6348 | 462 | TypeScript | 5,066 stars this month | 让人工智能代理使用您真实登录的浏览器，而不会中断您的工作。CLI +扩展用于跨任何支持外壳的AI代理的浏览器自动化。 | https://github.com/Tencent/BrowserSkill |  |
| 20 | `AprilNEA/OpenLogi` | 21871 | 718 | Rust | 9,466 stars this month | ⚡️用Rust编写的Logitech Options +的本地本地优先替代方案🦀—在HID + +上重新映射按钮、DPI和SmartShift。无帐户，无遥测。 | https://github.com/AprilNEA/OpenLogi |  |
| 21 | `every-app/open-seo` | 19886 | 2563 | TypeScript | 6,955 stars this month | Semrush和Ahrefs的开源替代品 | https://github.com/every-app/open-seo |  |


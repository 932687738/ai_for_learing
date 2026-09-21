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

**最近一次更新时间**（Asia/Shanghai）： 2026-09-21 09:14:39

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 548474 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 508267 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 481896 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 455855 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 397318 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 390159 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `donnemartin/system-design-primer` | 370983 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 8 | `nilbuild/developer-roadmap` | 367777 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 9 | `jwasham/coding-interview-university` | 361256 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 11 | `vinta/awesome-python` | 321964 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `affaan-m/ECC` | 263751 | 39457 | JavaScript | 826 stars today | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC | 新增 |
| 2 | `BuilderIO/agent-native` | 5224 | 485 | TypeScript | 98 stars today | 构建代理应用的框架 | https://github.com/BuilderIO/agent-native | 新增 |
| 3 | `cloudflare/security-audit-skill` | 18043 | 1000 | JavaScript | 2,428 stars today | 用于多阶段安全审核的编码代理技能，具有经过独立验证的机器可读结果 | https://github.com/cloudflare/security-audit-skill |  |
| 4 | `trycua/cua` | 25155 | 1730 | HTML | 1,018 stars today | 通过开源驱动程序、跨操作系统车队以及培训、评估和数据生成的基准来扩展计算机使用2.0。 | https://github.com/trycua/cua |  |
| 5 | `anthropics/financial-services` | 35372 | 5248 | Python | 260 stars today | — | https://github.com/anthropics/financial-services | 新增 |
| 6 | `paperless-ngx/paperless-ngx` | 45575 | 3146 | Python | 57 stars today | 社区支持的增压文档管理系统：扫描、索引和存档您的所有文档 | https://github.com/paperless-ngx/paperless-ngx | 新增 |
| 7 | `anthropics/claude-code` | 147132 | 24063 | TypeScript | 419 stars today | Claude Code是一个代理编码工具，它位于您的终端中，了解您的代码库，并通过执行日常任务、解释复杂代码和处理git工作流程（所有这些都通过自然语言命令）来帮助您更快地进行编码。 | https://github.com/anthropics/claude-code |  |
| 8 | `mihail911/modern-software-dev-assignments` | 4558 | 1010 | Python | 172 stars today | CS146S作业：现代软件开发（斯坦福大学2026/2025年秋季） | https://github.com/mihail911/modern-software-dev-assignments | 新增 |
| 9 | `higgsfield-ai/higgsfield` | 5387 | 956 | Jupyter Notebook | 465 stars today | 容错、高度可扩展的GPU编排，以及专为训练具有数十亿至数万亿参数的模型而设计的机器学习框架 | https://github.com/higgsfield-ai/higgsfield |  |
| 10 | `Open-Dev-Society/OpenStock` | 16837 | 2133 | TypeScript | 755 stars today | OpenStock是昂贵市场平台的开源替代品。实时跟踪价格，设置个性化提醒，并探索详细的公司洞察--为每个人公开构建，永远免费。 | https://github.com/Open-Dev-Society/OpenStock |  |
| 11 | `coder/coder` | 16064 | 1542 | Go | 379 stars today | 为开发人员及其代理提供安全的环境 | https://github.com/coder/coder |  |
| 12 | `vercel-labs/json-render` | 17322 | 919 | TypeScript | 291 stars today | 生成式UI框架 | https://github.com/vercel-labs/json-render | 新增 |
| 13 | `addyosmani/agent-skills` | 97705 | 10295 | JavaScript | 736 stars today | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `alibaba/open-code-review` | 38402 | 2738 | Go | 15,504 stars this week | 安全、快速、高效，经受住阿里巴巴规模的考验。混合架构代码审核工具：确定性流水线+ LLM Agent、精确的行级注释、内置多语言规则集（ NPE、线程安全、XSS、SQL注入）、OpenAI &amp; Anthropic兼容。 | https://github.com/alibaba/open-code-review |  |
| 2 | `anthropics/claude-code` | 147132 | 24063 | TypeScript | 2,342 stars this week | Claude Code是一个代理编码工具，它位于您的终端中，了解您的代码库，并通过执行日常任务、解释复杂代码和处理git工作流程（所有这些都通过自然语言命令）来帮助您更快地进行编码。 | https://github.com/anthropics/claude-code |  |
| 3 | `affaan-m/ECC` | 263751 | 39457 | JavaScript | 6,453 stars this week | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 4 | `Tencent/WeKnora` | 28011 | 3764 | Go | 5,242 stars this week | 开源LLM知识平台：将原始文档转化为可查询的RAG、自主推理代理和自我维护的Wiki。 | https://github.com/Tencent/WeKnora |  |
| 5 | `addyosmani/agent-skills` | 97705 | 10295 | JavaScript | 3,986 stars this week | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 6 | `anthropics/knowledge-work-plugins` | 25283 | 3007 | Python | 1,298 stars this week | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins |  |
| 7 | `bilawalsidhu/gods-eye-view` | 39651 | 8022 | JavaScript | 8,111 stars this week | 浏览器中的间谍卫星模拟器，但数据是真实的。在逼真的3D地球仪上实时开源空间智能。 | https://github.com/bilawalsidhu/gods-eye-view |  |
| 8 | `mksglu/context-mode` | 23774 | 1715 | TypeScript | 1,242 stars this week | 人工智能编码代理的上下文窗口优化。沙盒工具输出（减少98 ％ ） ，保持会话内存，并通过MCP +钩子在17个平台上强制路由。 | https://github.com/mksglu/context-mode |  |
| 9 | `max-sixty/worktrunk` | 8209 | 284 | Rust | 822 stars this week | Worktrunk是用于Git工作树管理的CLI ，专为并行AI代理工作流程而设计 | https://github.com/max-sixty/worktrunk |  |
| 10 | `home-assistant/core` | 90894 | 38714 | Python | 480 stars this week | 🏡 开源家庭自动化，将本地控制和隐私放在首位。 | https://github.com/home-assistant/core |  |
| 11 | `blader/humanizer` | 50638 | 4073 | Python | 3,045 stars this week | 从文本中删除人工智能生成文字的迹象的代理技能 | https://github.com/blader/humanizer |  |
| 12 | `stablyai/orca` | 73624 | 4823 | TypeScript | 5,841 stars this week | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面、移动和远程运行时使用。 | https://github.com/stablyai/orca |  |
| 13 | `Panniantong/Agent-Reach` | 83856 | 7349 | Python | 3,690 stars this week | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 14 | `heygen-com/hyperframes` | 51962 | 4732 | TypeScript | 2,546 stars this week | 编写HTML。渲染视频。专为客服代表打造。 | https://github.com/heygen-com/hyperframes |  |
| 15 | `danny-avila/LibreChat` | 44491 | 9138 | TypeScript | 1,600 stars this week | 增强的ChatGPT克隆：功能Agent、MCP、Skills、DeepSeek、Anthropic、AWS、OpenAI、Responses API、Azure、Groq、o1、GPT-5、Mistral、OpenRouter、Vertex AI、Gemini、Artifacts、AI模型切换、消息搜索、Code Interpreter、langchain、DALL-E-3、OpenAPI Actions、Functions…… | https://github.com/danny-avila/LibreChat |  |
| 16 | `ayghri/i-have-adhd` | 49244 | 2853 | Python | 5,249 stars this week | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 17 | `cline/cline` | 68892 | 7462 | TypeScript | 1,167 stars this week | 自主编码代理作为SDK、IDE扩展或CLI助手。 | https://github.com/cline/cline | 新增 |
| 18 | `petergyang/no-ai-slop` | 10823 | 737 | Python | 1,819 stars this week | 从任何文字中删除20多种AI斜坡图案。 | https://github.com/petergyang/no-ai-slop | 新增 |
| 19 | `supabase/supabase` | 110437 | 14477 | TypeScript | 1,484 stars this week | Postgres开发平台。Supabase为您提供了一个专用的Postgres数据库，用于构建您的Web、移动和人工智能应用程序。 | https://github.com/supabase/supabase |  |
| 20 | `microsoft/markitdown` | 185947 | 13689 | Python | 2,521 stars this week | 用于将文件和Office文档转换为Markdown的Python工具。 | https://github.com/microsoft/markitdown |  |
| 21 | `cilium/cilium` | 25386 | 4085 | Go | 373 stars this week | 基于eBPF的网络、安全性和可观察性 | https://github.com/cilium/cilium | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `tt-a1i/archify` | 68277 | 4566 | JavaScript | 53,904 stars this month | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify |  |
| 2 | `THU-MAIC/OpenMAIC` | 38204 | 5990 | TypeScript | 17,511 stars this month | 开放式多座席互动课堂—只需点击一下，即可获得身临其境的多座席学习体验 | https://github.com/THU-MAIC/OpenMAIC |  |
| 3 | `anthropics/claude-plugins-community` | 4311 | 311 | Python | 4,010 stars this month | Claude Cowork和Claude Code的社区插件市场。只读镜像—在clau.de/plugin-directory-submission上提交插件。 | https://github.com/anthropics/claude-plugins-community |  |
| 4 | `omacom/omarchy` | 42374 | 4880 | Shell | 15,720 stars this month | 漂亮、现代且自以为是的Linux | https://github.com/omacom/omarchy |  |
| 5 | `freestylefly/awesome-gpt-image-2` | 33002 | 3180 | JavaScript | 22,015 stars this month | Prompt as Code · GPT Image 2 / 2.5 提示词与案例库，530+ 个案例、20+ 套工业级模板与可复用 Skills，新增 2.5 同提示词对比专区，附完整提示词与生成记录，持续更新。 | https://github.com/freestylefly/awesome-gpt-image-2 |  |
| 6 | `cursor/plugins` | 8235 | 758 | TypeScript | 4,521 stars this month | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 7 | `debpalash/VoiceStudio` | 33555 | 3966 | Python | 22,901 stars this month | VoiceStudio是开源、完全本地的ElevenLabs替代品--语音克隆、语音设计、视频配音、听写、转录和有声读物创作，支持646种语言。 | https://github.com/debpalash/VoiceStudio |  |
| 8 | `cloudflare/security-audit-skill` | 18043 | 1000 | JavaScript | 14,879 stars this month | 用于多阶段安全审核的编码代理技能，具有经过独立验证的机器可读结果 | https://github.com/cloudflare/security-audit-skill |  |
| 9 | `vorssaint/vorssaint-utils` | 20247 | 739 | Swift | 14,605 stars this month | 免费开源的macOS菜单栏工具包。 | https://github.com/vorssaint/vorssaint-utils |  |
| 10 | `ayghri/i-have-adhd` | 49244 | 2853 | Python | 26,844 stars this month | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 11 | `alibaba/open-code-review` | 38402 | 2738 | Go | 17,582 stars this month | 安全、快速、高效，经受住阿里巴巴规模的考验。混合架构代码审核工具：确定性流水线+ LLM Agent、精确的行级注释、内置多语言规则集（ NPE、线程安全、XSS、SQL注入）、OpenAI &amp; Anthropic兼容。 | https://github.com/alibaba/open-code-review |  |
| 12 | `Lakr233/vphone-cli` | 14089 | 1663 | Swift | 6,211 stars this month | — | https://github.com/Lakr233/vphone-cli |  |
| 13 | `AprilNEA/OpenLogi` | 21750 | 710 | Rust | 10,567 stars this month | ⚡️用Rust编写的Logitech Options +的本地本地优先替代方案🦀—在HID + +上重新映射按钮、DPI和SmartShift。无帐户，无遥测。 | https://github.com/AprilNEA/OpenLogi |  |
| 14 | `tech-leads-club/agent-skills` | 6548 | 537 | TypeScript | 1,604 stars this month | 专业AI编码代理的安全、经过验证的技能注册表。绝对自信地扩展Antigravity、Claude Code、Cursor、Copilot等。 | https://github.com/tech-leads-club/agent-skills |  |
| 15 | `google-research/timesfm` | 33334 | 3218 | Python | 5,364 stars this month | TimesFM （时间序列基础模型）是由Google Research开发的用于时间序列预测的预训练时间序列基础模型。 | https://github.com/google-research/timesfm |  |
| 16 | `cathrynlavery/diagram-design` | 41588 | 2668 | HTML | 17,716 stars this month | Claude Code、Codex和Pi的编辑图设计。独立的HTML + SVG。没有阴影，没有美人鱼粪便。 | https://github.com/cathrynlavery/diagram-design |  |
| 17 | `jingyaogong/minimind` | 61844 | 8049 | Python | 7,126 stars this month | 在短短2小时内从头开始🧠培训64M参数LLM ！ | https://github.com/jingyaogong/minimind |  |
| 18 | `Tencent/WeKnora` | 28011 | 3764 | Go | 7,936 stars this month | 开源LLM知识平台：将原始文档转化为可查询的RAG、自主推理代理和自我维护的Wiki。 | https://github.com/Tencent/WeKnora |  |
| 19 | `Tencent/BrowserSkill` | 6062 | 432 | TypeScript | 4,797 stars this month | 让人工智能代理使用您真实登录的浏览器，而不会中断您的工作。CLI +扩展用于跨任何支持外壳的AI代理的浏览器自动化。 | https://github.com/Tencent/BrowserSkill | 新增 |
| 20 | `every-app/open-seo` | 19721 | 2536 | TypeScript | 6,976 stars this month | Semrush和Ahrefs的开源替代品 | https://github.com/every-app/open-seo |  |


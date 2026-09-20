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

**最近一次更新时间**（Asia/Shanghai）： 2026-09-20 09:20:27

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 548268 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 507886 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 481647 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 455787 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 397256 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 390105 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `donnemartin/system-design-primer` | 370782 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 8 | `nilbuild/developer-roadmap` | 367720 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 9 | `jwasham/coding-interview-university` | 361208 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 11 | `vinta/awesome-python` | 321764 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `cloudflare/security-audit-skill` | 16382 | 896 | JavaScript | 3,155 stars today | 用于多阶段安全审核的编码代理技能，具有经过独立验证的机器可读结果 | https://github.com/cloudflare/security-audit-skill |  |
| 2 | `trycua/cua` | 24425 | 1681 | HTML | 859 stars today | 通过开源驱动程序、跨操作系统车队以及培训、评估和数据生成的基准来扩展计算机使用2.0。 | https://github.com/trycua/cua |  |
| 3 | `addyosmani/agent-skills` | 97048 | 10241 | JavaScript | 556 stars today | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 4 | `coder/coder` | 15627 | 1522 | Go | 402 stars today | 为开发人员及其代理提供安全的环境 | https://github.com/coder/coder |  |
| 5 | `anthropics/claude-code` | 146719 | 23930 | TypeScript | 483 stars today | Claude Code是一个代理编码工具，它位于您的终端中，了解您的代码库，并通过执行日常任务、解释复杂代码和处理git工作流程（所有这些都通过自然语言命令）来帮助您更快地进行编码。 | https://github.com/anthropics/claude-code |  |
| 6 | `Open-Dev-Society/OpenStock` | 16058 | 2087 | TypeScript | 472 stars today | OpenStock是昂贵市场平台的开源替代品。实时跟踪价格，设置个性化提醒，并探索详细的公司洞察--为每个人公开构建，永远免费。 | https://github.com/Open-Dev-Society/OpenStock |  |
| 7 | `higgsfield-ai/higgsfield` | 4962 | 912 | Jupyter Notebook | 196 stars today | 容错、高度可扩展的GPU编排，以及专为训练具有数十亿至数万亿参数的模型而设计的机器学习框架 | https://github.com/higgsfield-ai/higgsfield |  |
| 8 | `docling-project/docling` | 67064 | 4833 | Python | 129 stars today | 让您的文档为人工智能时代做好准备 | https://github.com/docling-project/docling |  |
| 9 | `cloudflare/quiche` | 12019 | 1115 | Rust | 31 stars today | 🥧 QUIC传输协议和HTTP/3的有效实施 | https://github.com/cloudflare/quiche |  |
| 10 | `asciimoo/hister` | 5231 | 219 | Go | 420 stars today | 您自己的搜索引擎 | https://github.com/asciimoo/hister |  |
| 11 | `ruanyf/weekly` | 103149 | 4425 | — | 98 stars today | 科技爱好者周刊，每周五发布 | https://github.com/ruanyf/weekly |  |
| 12 | `ZuodaoTech/everyone-can-use-english` | 37801 | 5208 | TypeScript | 48 stars today | 人人都能用英语 | https://github.com/ZuodaoTech/everyone-can-use-english |  |
| 13 | `anthropics/knowledge-work-plugins` | 25132 | 2994 | Python | 281 stars today | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins |  |
| 14 | `cactus-compute/needle` | 11612 | 742 | Python | 234 stars today | 微型设备的自动化基础模型： 2位、8-29 MB、工具调用、手机、可穿戴设备、智能家居、机器人、汽车和微控制器上的结构化提取和嵌入。 | https://github.com/cactus-compute/needle |  |
| 15 | `yynxxxxx/Codex-X` | 3401 | 447 | Rust | 32 stars today | OpenAI Codex 桌面端/CLI 的可视化管理工具，具有Provider/API 切换、会话同步、提示词注入、Skills/MCP 管理、TOML 配置可视化的跨平台工具。 | https://github.com/yynxxxxx/Codex-X |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `alibaba/open-code-review` | 37570 | 2684 | Go | 15,028 stars this week | 安全、快速、高效，经受住阿里巴巴规模的考验。混合架构代码审核工具：确定性流水线+ LLM Agent、精确的行级注释、内置多语言规则集（ NPE、线程安全、XSS、SQL注入）、OpenAI &amp; Anthropic兼容。 | https://github.com/alibaba/open-code-review |  |
| 2 | `anthropics/claude-code` | 146719 | 23930 | TypeScript | 1,999 stars this week | Claude Code是一个代理编码工具，它位于您的终端中，了解您的代码库，并通过执行日常任务、解释复杂代码和处理git工作流程（所有这些都通过自然语言命令）来帮助您更快地进行编码。 | https://github.com/anthropics/claude-code |  |
| 3 | `affaan-m/ECC` | 262967 | 39348 | JavaScript | 6,265 stars this week | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 4 | `Tencent/WeKnora` | 27442 | 3697 | Go | 4,867 stars this week | 开源LLM知识平台：将原始文档转化为可查询的RAG、自主推理代理和自我维护的Wiki。 | https://github.com/Tencent/WeKnora |  |
| 5 | `bilawalsidhu/gods-eye-view` | 38644 | 7802 | JavaScript | 10,207 stars this week | 浏览器中的间谍卫星模拟器，但数据是真实的。在逼真的3D地球仪上实时开源空间智能。 | https://github.com/bilawalsidhu/gods-eye-view |  |
| 6 | `addyosmani/agent-skills` | 97048 | 10241 | JavaScript | 3,445 stars this week | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 7 | `anthropics/knowledge-work-plugins` | 25132 | 2994 | Python | 1,034 stars this week | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins |  |
| 8 | `ayghri/i-have-adhd` | 48705 | 2833 | Python | 5,589 stars this week | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 9 | `mksglu/context-mode` | 23668 | 1707 | TypeScript | 1,359 stars this week | 人工智能编码代理的上下文窗口优化。沙盒工具输出（减少98 ％ ） ，保持会话内存，并通过MCP +钩子在17个平台上强制路由。 | https://github.com/mksglu/context-mode |  |
| 10 | `max-sixty/worktrunk` | 8119 | 280 | Rust | 1,141 stars this week | Worktrunk是用于Git工作树管理的CLI ，专为并行AI代理工作流程而设计 | https://github.com/max-sixty/worktrunk |  |
| 11 | `blader/humanizer` | 50258 | 4055 | Python | 3,024 stars this week | 从文本中删除人工智能生成文字的迹象的代理技能 | https://github.com/blader/humanizer |  |
| 12 | `home-assistant/core` | 90823 | 38709 | Python | 417 stars this week | 🏡 开源家庭自动化，将本地控制和隐私放在首位。 | https://github.com/home-assistant/core |  |
| 13 | `microsoft/markitdown` | 185664 | 13673 | Python | 2,767 stars this week | 用于将文件和Office文档转换为Markdown的Python工具。 | https://github.com/microsoft/markitdown |  |
| 14 | `kunchenguid/firstmate` | 6737 | 2032 | Shell | 1,073 stars this week | 与一位客服代表交谈。船上有船员。 | https://github.com/kunchenguid/firstmate |  |
| 15 | `Panniantong/Agent-Reach` | 83466 | 7314 | Python | 3,914 stars this week | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach |  |
| 16 | `heygen-com/hyperframes` | 51659 | 4707 | TypeScript | 2,498 stars this week | 编写HTML。渲染视频。专为客服代表打造。 | https://github.com/heygen-com/hyperframes |  |
| 17 | `stablyai/orca` | 72634 | 4752 | TypeScript | 5,404 stars this week | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面、移动和远程运行时使用。 | https://github.com/stablyai/orca |  |
| 18 | `openai/plugins` | 7034 | 910 | JavaScript | 522 stars this week | OpenAI插件 | https://github.com/openai/plugins |  |
| 19 | `danny-avila/LibreChat` | 44404 | 9120 | TypeScript | 1,573 stars this week | 增强的ChatGPT克隆：功能Agent、MCP、Skills、DeepSeek、Anthropic、AWS、OpenAI、Responses API、Azure、Groq、o1、GPT-5、Mistral、OpenRouter、Vertex AI、Gemini、Artifacts、AI模型切换、消息搜索、Code Interpreter、langchain、DALL-E-3、OpenAPI Actions、Functions…… | https://github.com/danny-avila/LibreChat |  |
| 20 | `supabase/supabase` | 110332 | 14398 | TypeScript | 1,389 stars this week | Postgres开发平台。Supabase为您提供了一个专用的Postgres数据库，用于构建您的Web、移动和人工智能应用程序。 | https://github.com/supabase/supabase |  |
| 21 | `huggingface/transformers` | 166393 | 34630 | Python | 1,290 stars this week | 🤗 Transformers ：用于推理和训练的文本、视觉、音频和多模态模型中最先进的机器学习模型的模型定义框架。 | https://github.com/huggingface/transformers |  |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `tt-a1i/archify` | 67483 | 4510 | JavaScript | 53,311 stars this month | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify |  |
| 2 | `omacom/omarchy` | 42136 | 4845 | Shell | 15,717 stars this month | 漂亮、现代且自以为是的Linux | https://github.com/omacom/omarchy |  |
| 3 | `anthropics/claude-plugins-community` | 4269 | 309 | Python | 3,968 stars this month | Claude Cowork和Claude Code的社区插件市场。只读镜像—在clau.de/plugin-directory-submission上提交插件。 | https://github.com/anthropics/claude-plugins-community |  |
| 4 | `THU-MAIC/OpenMAIC` | 38001 | 5966 | TypeScript | 17,316 stars this month | 开放式多座席互动课堂—只需点击一下，即可获得身临其境的多座席学习体验 | https://github.com/THU-MAIC/OpenMAIC |  |
| 5 | `freestylefly/awesome-gpt-image-2` | 32817 | 3167 | JavaScript | 21,920 stars this month | Prompt as Code · GPT Image 2 / 2.5 提示词与案例库，530+ 个案例、20+ 套工业级模板与可复用 Skills，新增 2.5 同提示词对比专区，附完整提示词与生成记录，持续更新。 | https://github.com/freestylefly/awesome-gpt-image-2 |  |
| 6 | `cursor/plugins` | 8184 | 751 | TypeScript | 4,944 stars this month | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 7 | `debpalash/VoiceStudio` | 33203 | 3924 | Python | 23,139 stars this month | VoiceStudio是开源、完全本地的ElevenLabs替代品--语音克隆、语音设计、视频配音、听写、转录和有声读物创作，支持646种语言。 | https://github.com/debpalash/VoiceStudio |  |
| 8 | `AprilNEA/OpenLogi` | 21648 | 701 | Rust | 12,141 stars this month | ⚡️用Rust编写的Logitech Options +的本地本地优先替代方案🦀—在HID + +上重新映射按钮、DPI和SmartShift。无帐户，无遥测。 | https://github.com/AprilNEA/OpenLogi |  |
| 9 | `vorssaint/vorssaint-utils` | 20031 | 731 | Swift | 14,438 stars this month | 免费开源的macOS菜单栏工具包。 | https://github.com/vorssaint/vorssaint-utils |  |
| 10 | `ayghri/i-have-adhd` | 48705 | 2833 | Python | 26,527 stars this month | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 11 | `cloudflare/security-audit-skill` | 16383 | 896 | JavaScript | 12,420 stars this month | 用于多阶段安全审核的编码代理技能，具有经过独立验证的机器可读结果 | https://github.com/cloudflare/security-audit-skill |  |
| 12 | `Lakr233/vphone-cli` | 13986 | 1651 | Swift | 6,183 stars this month | — | https://github.com/Lakr233/vphone-cli |  |
| 13 | `alibaba/open-code-review` | 37571 | 2684 | Go | 16,711 stars this month | 安全、快速、高效，经受住阿里巴巴规模的考验。混合架构代码审核工具：确定性流水线+ LLM Agent、精确的行级注释、内置多语言规则集（ NPE、线程安全、XSS、SQL注入）、OpenAI &amp; Anthropic兼容。 | https://github.com/alibaba/open-code-review |  |
| 14 | `cathrynlavery/diagram-design` | 41348 | 2648 | HTML | 18,899 stars this month | Claude Code、Codex和Pi的编辑图设计。独立的HTML + SVG。没有阴影，没有美人鱼粪便。 | https://github.com/cathrynlavery/diagram-design |  |
| 15 | `google-research/timesfm` | 33244 | 3201 | Python | 5,274 stars this month | TimesFM （时间序列基础模型）是由Google Research开发的用于时间序列预测的预训练时间序列基础模型。 | https://github.com/google-research/timesfm |  |
| 16 | `jingyaogong/minimind` | 61711 | 8031 | Python | 7,036 stars this month | 在短短2小时内从头开始🧠培训64M参数LLM ！ | https://github.com/jingyaogong/minimind |  |
| 17 | `Tencent/WeKnora` | 27442 | 3697 | Go | 7,397 stars this month | 开源LLM知识平台：将原始文档转化为可查询的RAG、自主推理代理和自我维护的Wiki。 | https://github.com/Tencent/WeKnora |  |
| 18 | `tashfeenahmed/freellmapi` | 27440 | 3748 | TypeScript | 8,646 stars this month | 每月74亿个代币。34个免费LLM提供商。635个免费模型端点。全部在一个/v1端点后面，加上任何与OpenAI兼容的自定义端点。智能路由、自动故障转移、加密密钥。仅限个人实验。 | https://github.com/tashfeenahmed/freellmapi |  |
| 19 | `tech-leads-club/agent-skills` | 6469 | 537 | TypeScript | 1,527 stars this month | 专业AI编码代理的安全、经过验证的技能注册表。绝对自信地扩展Antigravity、Claude Code、Cursor、Copilot等。 | https://github.com/tech-leads-club/agent-skills |  |
| 20 | `every-app/open-seo` | 19516 | 2507 | TypeScript | 6,917 stars this month | Semrush和Ahrefs的开源替代品 | https://github.com/every-app/open-seo |  |
| 21 | `melgarafael/DeskcommCRM` | 3310 | 804 | TypeScript | 2,827 stars this month | 开源AI销售操作系统—使用本地AI代理+ WhatsApp (WAHA)的自托管CRM。对于任何通过聊天销售的企业， Kommo、Octadesk和Intercom的替代方案都是开放的。MCP就绪、多租户、LGPD。 | https://github.com/melgarafael/DeskcommCRM |  |
| 22 | `abue-ammar/tinycast` | 6670 | 310 | Swift | 4,979 stars this month | Tinycast —一个小巧、完全原生的macOS启动器、热键和剪贴板历史记录。 | https://github.com/abue-ammar/tinycast |  |


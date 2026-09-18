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

**最近一次更新时间**（Asia/Shanghai）： 2026-09-18 09:15:40

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 547915 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 507190 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 481233 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 455695 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 397063 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 390006 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `donnemartin/system-design-primer` | 370543 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 8 | `nilbuild/developer-roadmap` | 367552 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 9 | `jwasham/coding-interview-university` | 361115 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 10 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 11 | `vinta/awesome-python` | 321348 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `alibaba/open-code-review` | 34792 | 2474 | Go | 3,286 stars today | 快速、高效、经受住阿里巴巴规模的考验。混合架构代码审核工具：确定性流水线+ LLM Agent、精确的行级注释、内置多语言规则集（ NPE、线程安全、XSS、SQL注入）、OpenAI &amp; Anthropic兼容。 | https://github.com/alibaba/open-code-review |  |
| 2 | `cloudflare/security-audit-skill` | 10689 | 570 | JavaScript | 3,607 stars today | 用于多阶段安全审核的编码代理技能，具有经过独立验证的机器可读结果 | https://github.com/cloudflare/security-audit-skill |  |
| 3 | `addyosmani/agent-skills` | 95858 | 10145 | JavaScript | 680 stars today | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 4 | `Tencent/BrowserSkill` | 4164 | 296 | TypeScript | 1,302 stars today | 让人工智能代理使用您真实登录的浏览器，而不会中断您的工作。CLI +扩展用于跨任何支持外壳的AI代理的浏览器自动化。 | https://github.com/Tencent/BrowserSkill | 新增 |
| 5 | `alphaXiv/OpenResearch` | 4957 | 306 | Rust | 939 stars today | 将您的编码代理转变为研究代理 | https://github.com/alphaXiv/OpenResearch |  |
| 6 | `anthropics/claude-code` | 145878 | 23639 | TypeScript | 538 stars today | Claude Code是一个代理编码工具，它位于您的终端中，了解您的代码库，并通过执行日常任务、解释复杂代码和处理git工作流程（所有这些都通过自然语言命令）来帮助您更快地进行编码。 | https://github.com/anthropics/claude-code |  |
| 7 | `NationalSecurityAgency/ghidra` | 78496 | 8684 | Java | 912 stars today | Ghidra是一个软件逆向工程（ SRE ）框架 | https://github.com/NationalSecurityAgency/ghidra |  |
| 8 | `anthropics/knowledge-work-plugins` | 24568 | 2944 | Python | 287 stars today | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins |  |
| 9 | `Tencent/WeKnora` | 26239 | 3555 | Go | 1,125 stars today | 开源LLM知识平台：将原始文档转化为可查询的RAG、自主推理代理和自我维护的Wiki。 | https://github.com/Tencent/WeKnora |  |
| 10 | `abue-ammar/tinycast` | 6153 | 286 | Swift | 739 stars today | Tinycast —一个小巧、完全原生的macOS启动器、热键和剪贴板历史记录。 | https://github.com/abue-ammar/tinycast |  |
| 11 | `cilium/cilium` | 25270 | 4073 | Go | 111 stars today | 基于eBPF的网络、安全性和可观察性 | https://github.com/cilium/cilium | 新增 |
| 12 | `jamiepine/voicebox` | 54854 | 6826 | TypeScript | 667 stars today | 开源AI语音工作室。克隆、命令、创建。 | https://github.com/jamiepine/voicebox |  |
| 13 | `affaan-m/ECC` | 261177 | 39097 | JavaScript | 1,171 stars today | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 14 | `roboflow/supervision` | 50803 | 4828 | Python | 329 stars today | 我们为您编写可重复使用的计算机视觉工具。 💜 | https://github.com/roboflow/supervision |  |
| 15 | `JustVugg/colibri` | 35747 | 3755 | C | 873 stars today | 在您已经拥有的硬件上运行前沿MoE模型—纯C ，零DEPS ，从磁盘流式传输的专家。微型引擎，超大型号。 🐦 | https://github.com/JustVugg/colibri |  |
| 16 | `TencentCloud/Octop` | 3455 | 360 | Python | 367 stars today | 更智能、自托管的人工智能助手—多用户、多代理。 | https://github.com/TencentCloud/Octop | 新增 |
| 17 | `ever-co/ever-gauzy` | 7547 | 1121 | TypeScript | 470 stars today | Ever ® Gauzy™ -开放式业务管理平台（ ERP/CRM/HRM/ATS/PM ） - https://gauzy.co | https://github.com/ever-co/ever-gauzy |  |
| 18 | `cline/cline` | 68561 | 7415 | TypeScript | 380 stars today | 自主编码代理作为SDK、IDE扩展或CLI助手。 | https://github.com/cline/cline |  |
| 19 | `coder/coder` | 14842 | 1486 | Go | 145 stars today | 为开发人员及其代理提供安全的环境 | https://github.com/coder/coder | 新增 |
| 20 | `n8n-io/n8n` | 205003 | 60745 | TypeScript | 281 stars today | 具有原生AI功能的公平代码工作流程自动化平台。将视觉构建与自定义代码、自托管或云、400多个集成相结合。 | https://github.com/n8n-io/n8n | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `alibaba/open-code-review` | 34795 | 2474 | Go | 11,489 stars this week | 快速、高效、经受住阿里巴巴规模的考验。混合架构代码审核工具：确定性流水线+ LLM Agent、精确的行级注释、内置多语言规则集（ NPE、线程安全、XSS、SQL注入）、OpenAI &amp; Anthropic兼容。 | https://github.com/alibaba/open-code-review |  |
| 2 | `ayghri/i-have-adhd` | 47474 | 2765 | Python | 10,800 stars this week | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 3 | `bilawalsidhu/gods-eye-view` | 37109 | 7460 | JavaScript | 14,460 stars this week | 浏览器中的间谍卫星模拟器，但数据是真实的。在逼真的3D地球仪上实时开源空间智能。 | https://github.com/bilawalsidhu/gods-eye-view |  |
| 4 | `affaan-m/ECC` | 261178 | 39097 | JavaScript | 5,607 stars this week | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 5 | `mksglu/context-mode` | 23398 | 1684 | TypeScript | 1,482 stars this week | 人工智能编码代理的上下文窗口优化。沙盒工具输出（减少98 ％ ） ，保持会话内存，并通过MCP +钩子在17个平台上强制路由。 | https://github.com/mksglu/context-mode |  |
| 6 | `Tencent/WeKnora` | 26239 | 3556 | Go | 3,982 stars this week | 开源LLM知识平台：将原始文档转化为可查询的RAG、自主推理代理和自我维护的Wiki。 | https://github.com/Tencent/WeKnora |  |
| 7 | `openai/plugins` | 6915 | 900 | JavaScript | 564 stars this week | OpenAI插件 | https://github.com/openai/plugins |  |
| 8 | `max-sixty/worktrunk` | 7940 | 272 | Rust | 1,060 stars this week | Worktrunk是用于Git工作树管理的CLI ，专为并行AI代理工作流程而设计 | https://github.com/max-sixty/worktrunk |  |
| 9 | `addyosmani/agent-skills` | 95858 | 10145 | JavaScript | 2,560 stars this week | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills |  |
| 10 | `anthropics/claude-code` | 145878 | 23639 | TypeScript | 1,294 stars this week | Claude Code是一个代理编码工具，它位于您的终端中，了解您的代码库，并通过执行日常任务、解释复杂代码和处理git工作流程（所有这些都通过自然语言命令）来帮助您更快地进行编码。 | https://github.com/anthropics/claude-code | 新增 |
| 11 | `anthropics/knowledge-work-plugins` | 24569 | 2944 | Python | 488 stars this week | 主要供知识工作者在Claude Cowork中使用的插件的开源存储库 | https://github.com/anthropics/knowledge-work-plugins | 新增 |
| 12 | `obra/superpowers` | 288132 | 25774 | Shell | 3,821 stars this week | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers |  |
| 13 | `blader/humanizer` | 49595 | 4018 | Python | 3,235 stars this week | 从文本中删除人工智能生成文字的迹象的代理技能 | https://github.com/blader/humanizer |  |
| 14 | `microsoft/markitdown` | 185133 | 13631 | Python | 2,814 stars this week | 用于将文件和Office文档转换为Markdown的Python工具。 | https://github.com/microsoft/markitdown |  |
| 15 | `home-assistant/core` | 90668 | 38689 | Python | 285 stars this week | 🏡 开源家庭自动化，将本地控制和隐私放在首位。 | https://github.com/home-assistant/core |  |
| 16 | `kunchenguid/firstmate` | 6407 | 1965 | Shell | 890 stars this week | 与一位客服代表交谈。船上有船员。 | https://github.com/kunchenguid/firstmate |  |
| 17 | `petergyang/no-ai-slop` | 10377 | 726 | Python | 2,256 stars this week | 从任何文字中删除20多种AI斜坡图案。 | https://github.com/petergyang/no-ai-slop |  |
| 18 | `danny-avila/LibreChat` | 44238 | 9093 | TypeScript | 1,421 stars this week | 增强的ChatGPT克隆：功能Agent、MCP、Skills、DeepSeek、Anthropic、AWS、OpenAI、Responses API、Azure、Groq、o1、GPT-5、Mistral、OpenRouter、Vertex AI、Gemini、Artifacts、AI模型切换、消息搜索、Code Interpreter、langchain、DALL-E-3、OpenAPI Actions、Functions…… | https://github.com/danny-avila/LibreChat |  |
| 19 | `stablyai/orca` | 71157 | 4653 | TypeScript | 5,305 stars this week | ORCA是ADE ，用于与一群并行代理商合作。使用您自己的订阅运行任何编码代理。可在桌面、移动和远程运行时使用。 | https://github.com/stablyai/orca | 新增 |
| 20 | `Panniantong/Agent-Reach` | 82816 | 7246 | Python | 3,670 stars this week | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach | 新增 |
| 21 | `decolua/9router` | 29176 | 5376 | JavaScript | 871 stars this week | 无限免费AI编码。通过40多家供应商将Claude Code、Codex、Cursor、Cline、Copilot、Antigravity连接到免费的Claude/GPT/Gemini。自动回退， RTK -40%代币，从未达到限制。 | https://github.com/decolua/9router | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `tt-a1i/archify` | 65860 | 4399 | JavaScript | 52,260 stars this month | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify |  |
| 2 | `omacom/omarchy` | 41742 | 4757 | Shell | 16,196 stars this month | 漂亮、现代且自以为是的Linux | https://github.com/omacom/omarchy |  |
| 3 | `anthropics/claude-plugins-community` | 4193 | 306 | Python | 3,896 stars this month | Claude Cowork和Claude Code的社区插件市场。只读镜像—在clau.de/plugin-directory-submission上提交插件。 | https://github.com/anthropics/claude-plugins-community |  |
| 4 | `cursor/plugins` | 8044 | 727 | TypeScript | 5,130 stars this month | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 5 | `AprilNEA/OpenLogi` | 21453 | 694 | Rust | 12,913 stars this month | ⚡️用Rust编写的Logitech Options +的本地本地优先替代方案🦀—在HID + +上重新映射按钮、DPI和SmartShift。无帐户，无遥测。 | https://github.com/AprilNEA/OpenLogi |  |
| 6 | `THU-MAIC/OpenMAIC` | 37623 | 5913 | TypeScript | 16,970 stars this month | 开放式多座席互动课堂—只需点击一下，即可获得身临其境的多座席学习体验 | https://github.com/THU-MAIC/OpenMAIC |  |
| 7 | `freestylefly/awesome-gpt-image-2` | 32482 | 3136 | JavaScript | 21,929 stars this month | Prompt as Code · GPT Image 2 / 2.5 提示词与案例库，530+ 个案例、20+ 套工业级模板与可复用 Skills，新增 2.5 同提示词对比专区，附完整提示词与生成记录，持续更新。 | https://github.com/freestylefly/awesome-gpt-image-2 |  |
| 8 | `ayghri/i-have-adhd` | 47474 | 2765 | Python | 26,237 stars this month | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 9 | `vorssaint/vorssaint-utils` | 19666 | 714 | Swift | 14,192 stars this month | 免费开源的macOS菜单栏工具包。 | https://github.com/vorssaint/vorssaint-utils |  |
| 10 | `debpalash/VoiceStudio` | 32489 | 3855 | Python | 22,507 stars this month | VoiceStudio是开源、完全本地的ElevenLabs替代品--语音克隆、语音设计、视频配音、听写、转录和有声读物创作，支持646种语言。 | https://github.com/debpalash/VoiceStudio |  |
| 11 | `cathrynlavery/diagram-design` | 40812 | 2604 | HTML | 20,738 stars this month | Claude Code、Codex和Pi的38种编辑图类型。独立的HTML + SVG。没有阴影，没有美人鱼粪便。 | https://github.com/cathrynlavery/diagram-design |  |
| 12 | `Lakr233/vphone-cli` | 13781 | 1626 | Swift | 5,998 stars this month | — | https://github.com/Lakr233/vphone-cli |  |
| 13 | `apache/maka` | 5544 | 514 | TypeScript | 4,224 stars this month | Apache Maka （孵化）是一个高性能代理工作区，可完整记录其所做的一切。 | https://github.com/apache/maka |  |
| 14 | `chaitanyagiri/munder-difflin` | 7532 | 983 | TypeScript | 6,168 stars this month | 与您现有的Claude Code、Codex订阅配合使用的本地多代理线束可让您运营代理商办公室 | https://github.com/chaitanyagiri/munder-difflin |  |
| 15 | `google-research/timesfm` | 33029 | 3178 | Python | 5,145 stars this month | TimesFM （时间序列基础模型）是由Google Research开发的用于时间序列预测的预训练时间序列基础模型。 | https://github.com/google-research/timesfm |  |
| 16 | `jingyaogong/minimind` | 61488 | 8003 | Python | 6,867 stars this month | 在短短2小时内从头开始🧠培训64M参数LLM ！ | https://github.com/jingyaogong/minimind |  |
| 17 | `modular/modular` | 29804 | 3176 | Mojo | 3,082 stars this month | 模块化平台（包括MAX和Mojo ） | https://github.com/modular/modular |  |
| 18 | `tashfeenahmed/freellmapi` | 26946 | 3677 | TypeScript | 8,304 stars this month | 每月74亿个代币。34个免费LLM提供商。635个免费模型端点。全部在一个/v1端点后面，加上任何与OpenAI兼容的自定义端点。智能路由、自动故障转移、加密密钥。仅限个人实验。 | https://github.com/tashfeenahmed/freellmapi |  |
| 19 | `tech-leads-club/agent-skills` | 6344 | 531 | TypeScript | 1,398 stars this month | 专业AI编码代理的安全、经过验证的技能注册表。绝对自信地扩展Antigravity、Claude Code、Cursor、Copilot等。 | https://github.com/tech-leads-club/agent-skills |  |
| 20 | `abue-ammar/tinycast` | 6153 | 286 | Swift | 4,365 stars this month | Tinycast —一个小巧、完全原生的macOS启动器、热键和剪贴板历史记录。 | https://github.com/abue-ammar/tinycast | 新增 |
| 21 | `securo-finance/securo` | 3541 | 445 | Python | 1,902 stars this month | 开源个人理财经理。自托管，隐私至上。 | https://github.com/securo-finance/securo | 新增 |
| 22 | `melgarafael/DeskcommCRM` | 3070 | 759 | TypeScript | 2,586 stars this month | 开源AI销售操作系统—使用本地AI代理+ WhatsApp (WAHA)的自托管CRM。对于任何通过聊天销售的企业， Kommo、Octadesk和Intercom的替代方案都是开放的。MCP就绪、多租户、LGPD。 | https://github.com/melgarafael/DeskcommCRM | 新增 |


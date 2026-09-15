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

**最近一次更新时间**（Asia/Shanghai）： 2026-09-15 11:02:51

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 547287 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 506095 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 480248 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 455446 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 396779 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 389709 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `donnemartin/system-design-primer` | 370043 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 8 | `nilbuild/developer-roadmap` | 367235 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 9 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 10 | `jwasham/coding-interview-university` | 360902 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 11 | `vinta/awesome-python` | 320680 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `JustVugg/colibri` | 32246 | 3398 | C | 2,173 stars today | 在您已经拥有的硬件上运行前沿MoE模型—纯C ，零DEPS ，从磁盘流式传输的专家。微型引擎，超大型号。 🐦 | https://github.com/JustVugg/colibri |  |
| 2 | `alibaba/open-code-review` | 26041 | 1881 | Go | 1,571 stars today | 快速、高效、经受住阿里巴巴规模的考验。混合架构代码审核工具：确定性流水线+ LLM Agent、精确的行级注释、内置多语言规则集（ NPE、线程安全、XSS、SQL注入）、OpenAI &amp; Anthropic兼容。 | https://github.com/alibaba/open-code-review |  |
| 3 | `multimodal-art-projection/YuE` | 8450 | 912 | Python | 559 stars today | YuE2 ：具有象征性规划、零封面和代理音乐编辑的前沿音乐生成。 | https://github.com/multimodal-art-projection/YuE |  |
| 4 | `debpalash/VoiceStudio` | 29434 | 3570 | Python | 2,776 stars today | VoiceStudio是开源、完全本地的ElevenLabs替代品--语音克隆、语音设计、视频配音、听写、转录和有声读物创作，支持646种语言。 | https://github.com/debpalash/VoiceStudio |  |
| 5 | `666ghj/MiroFish` | 73254 | 11294 | Python | 560 stars today | A Simple and Universal Swarm Intelligence Engine, Predicting Anything. 简洁通用的群体智能引擎，预测万物 | https://github.com/666ghj/MiroFish | 新增 |
| 6 | `Panniantong/Agent-Reach` | 81408 | 7083 | Python | 651 stars today | 让您的人工智能代理看到整个互联网。阅读和搜索Twitter、Reddit、YouTube、GitHub、Bilibili、XiaoHongShu —一个CLI ，无API费用。 | https://github.com/Panniantong/Agent-Reach | 新增 |
| 7 | `asgeirtj/system_prompts_leaks` | 66845 | 10875 | JavaScript | 764 stars today | 从Anthropic - Claude Fable 5.1、Opus 5、Claude Design、Claude Code中提取系统提示。OpenAI - ChatGPT GPT-6-Astra ， Codex。Google - Gemini 3.8 Flash、3.1 Pro、Antigravity。xAI - Grok、Grok Bot、Cursor、Kimi等！定期更新。 | https://github.com/asgeirtj/system_prompts_leaks |  |
| 8 | `rlaope/oh-my-hermes` | 2118 | 163 | Python | 77 stars today | Hermès Agent编码智能、长期⚚记忆系统和模型优化工作流程包的一体化插件 | https://github.com/rlaope/oh-my-hermes | 新增 |
| 9 | `localsend/localsend` | 91391 | 5098 | Dart | 251 stars today | AirDrop的开源跨平台替代方案 | https://github.com/localsend/localsend | 新增 |
| 10 | `dani-garcia/vaultwarden` | 67561 | 3213 | Rust | 115 stars today | 用Rust编写的非官方Bitwarden兼容服务器，以前称为bitwarden_rs | https://github.com/dani-garcia/vaultwarden | 新增 |
| 11 | `TauricResearch/TradingAgents` | 106230 | 20315 | Python | 745 stars today | TradingAgent ：多代理LLM金融交易框架 | https://github.com/TauricResearch/TradingAgents | 新增 |
| 12 | `ruvnet/RuView` | 93902 | 12437 | Rust | 383 stars today | π RuView将商用WiFi信号转化为实时空间智能、生命体征监测和存在检测--所有这些都无需一个像素的视频。 | https://github.com/ruvnet/RuView | 新增 |
| 13 | `tech-leads-club/agent-skills` | 6103 | 519 | TypeScript | 512 stars today | 专业AI编码代理的安全、经过验证的技能注册表。绝对自信地扩展Antigravity、Claude Code、Cursor、Copilot等。 | https://github.com/tech-leads-club/agent-skills |  |
| 14 | `OpenBMB/VoxCPM` | 37414 | 4250 | Python | 216 stars today | VoxCPM2 ：用于多语言语音生成、创意语音设计和真实克隆的无标记TTS | https://github.com/OpenBMB/VoxCPM | 新增 |
| 15 | `huggingface/transformers` | 166026 | 34580 | Python | 536 stars today | 🤗 Transformers ：用于推理和训练的文本、视觉、音频和多模态模型中最先进的机器学习模型的模型定义框架。 | https://github.com/huggingface/transformers |  |
| 16 | `ever-co/ever-gauzy` | 6042 | 987 | TypeScript | 1,130 stars today | Ever ® Gauzy™ -开放式业务管理平台（ ERP/CRM/HRM/ATS/PM ） - https://gauzy.co | https://github.com/ever-co/ever-gauzy |  |
| 17 | `Crosstalk-Solutions/project-nomad` | 36951 | 3687 | TypeScript | 40 stars today | Project NOMAD是一个离线优先的知识和教育服务器。维基百科、成千上万的书籍、课程、地图和可选的本地人工智能，所有这些都运行在您拥有的硬件上，无需互联网。 | https://github.com/Crosstalk-Solutions/project-nomad | 新增 |
| 18 | `reconurge/flowsint` | 8383 | 1028 | TypeScript | 280 stars today | 用于可视化、灵活且可扩展的基于图形的调查的现代平台。适用于网络安全分析师和调查人员。 | https://github.com/reconurge/flowsint | 新增 |
| 19 | `peetzweg/opendisplay` | 3645 | 251 | Swift | 229 stars today | 免费、开源的Sidecar/Duet替代品—通过USB或WiFi将您的iPhone或iPad用作Mac的真正第二显示器。低延迟H.264 ， Retina HiDPI ，触摸输入。 | https://github.com/peetzweg/opendisplay | 新增 |
| 20 | `SnailSploit/Claude-Red` | 4810 | 633 | Python | 579 stars today | claude-red是为Claude技能系统设计的攻击性安全技能精心策划的图书馆。每个技能都是一个结构化的SKILL.md文件，为Claude提供了针对特定攻击面的专家级方法--从SQLi到shellcode ，从EDR规避到利用开发人员…… | https://github.com/SnailSploit/Claude-Red |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `ayghri/i-have-adhd` | 45525 | 2640 | Python | 17,658 stars this week | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 2 | `bilawalsidhu/gods-eye-view` | 33691 | 6723 | JavaScript | 14,403 stars this week | 浏览器中的间谍卫星模拟器，但数据是真实的。在逼真的3D地球仪上实时开源空间智能。 | https://github.com/bilawalsidhu/gods-eye-view |  |
| 3 | `affaan-m/ECC` | 258444 | 38660 | JavaScript | 6,085 stars this week | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 4 | `openai/plugins` | 6716 | 880 | JavaScript | 1,233 stars this week | OpenAI插件 | https://github.com/openai/plugins |  |
| 5 | `DietrichGebert/ponytail` | 138543 | 7441 | JavaScript | 7,722 stars this week | 让你的人工智能代理像房间里最懒惰的高级开发人员一样思考。最好的代码是你从未写过的代码。 | https://github.com/DietrichGebert/ponytail |  |
| 6 | `mksglu/context-mode` | 22887 | 1655 | TypeScript | 2,241 stars this week | 人工智能编码代理的上下文窗口优化。沙盒工具输出（减少98 ％ ） ，保持会话内存，并通过MCP +钩子在17个平台上强制路由。 | https://github.com/mksglu/context-mode |  |
| 7 | `heygen-com/hyperframes` | 50068 | 4570 | TypeScript | 5,052 stars this week | 编写HTML。渲染视频。专为客服代表打造。 | https://github.com/heygen-com/hyperframes |  |
| 8 | `tt-a1i/archify` | 62426 | 4121 | JavaScript | 9,868 stars this week | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify |  |
| 9 | `openai/skills` | 27205 | 1814 | Python | 1,350 stars this week | Codex技能目录 | https://github.com/openai/skills |  |
| 10 | `microsoft/markitdown` | 184050 | 13547 | Python | 4,604 stars this week | 用于将文件和Office文档转换为Markdown的Python工具。 | https://github.com/microsoft/markitdown |  |
| 11 | `obra/superpowers` | 286743 | 25647 | Shell | 4,124 stars this week | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers |  |
| 12 | `blader/humanizer` | 48190 | 3927 | Python | 3,201 stars this week | 从文本中删除人工智能生成文字的迹象的代理技能 | https://github.com/blader/humanizer |  |
| 13 | `max-sixty/worktrunk` | 7684 | 273 | Rust | 761 stars this week | Worktrunk是用于Git工作树管理的CLI ，专为并行AI代理工作流程而设计 | https://github.com/max-sixty/worktrunk |  |
| 14 | `THU-MAIC/OpenMAIC` | 36871 | 5823 | TypeScript | 3,950 stars this week | 开放式多座席互动课堂—只需点击一下，即可获得身临其境的多座席学习体验 | https://github.com/THU-MAIC/OpenMAIC |  |
| 15 | `cathrynlavery/diagram-design` | 39868 | 2528 | HTML | 6,604 stars this week | Claude Code、Codex和Pi的38种编辑图类型。独立的HTML + SVG。没有阴影，没有美人鱼粪便。 | https://github.com/cathrynlavery/diagram-design |  |
| 16 | `ChromeDevTools/chrome-devtools-mcp` | 51963 | 3646 | TypeScript | 702 stars this week | 适用于编码代理的Chrome开发者工具 | https://github.com/ChromeDevTools/chrome-devtools-mcp |  |
| 17 | `Tencent/WeKnora` | 23308 | 3309 | Go | 1,460 stars this week | 开源LLM知识平台：将原始文档转化为可查询的RAG、自主推理代理和自我维护的Wiki。 | https://github.com/Tencent/WeKnora |  |
| 18 | `coreyhaines31/marketingskills` | 50267 | 7610 | JavaScript | 2,344 stars this week | Claude Code和人工智能代理的营销技能。CRO、文案撰写、搜索引擎优化、分析和增长工程。 | https://github.com/coreyhaines31/marketingskills |  |
| 19 | `earthtojake/text-to-cad` | 15796 | 1632 | Python | 1,194 stars this week | CAD、CAE和CAM的代理技能库 | https://github.com/earthtojake/text-to-cad |  |
| 20 | `petergyang/no-ai-slop` | 9585 | 689 | Python | 1,946 stars this week | 从任何文字中删除20多种AI斜坡图案。 | https://github.com/petergyang/no-ai-slop |  |
| 21 | `github/spec-kit` | 136823 | 12271 | Python | 2,952 stars this week | 帮助您开始规格驱动开发💫的工具包 | https://github.com/github/spec-kit |  |
| 22 | `alibaba/open-code-review` | 26041 | 1881 | Go | 2,709 stars this week | 快速、高效、经受住阿里巴巴规模的考验。混合架构代码审核工具：确定性流水线+ LLM Agent、精确的行级注释、内置多语言规则集（ NPE、线程安全、XSS、SQL注入）、OpenAI &amp; Anthropic兼容。 | https://github.com/alibaba/open-code-review | 新增 |
| 23 | `kunchenguid/firstmate` | 5964 | 1830 | Shell | 978 stars this week | 与一位客服代表交谈。船上有船员。 | https://github.com/kunchenguid/firstmate |  |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `omacom/omarchy` | 41107 | 4626 | Shell | 16,712 stars this month | 漂亮、现代且自以为是的Linux | https://github.com/omacom/omarchy |  |
| 2 | `tt-a1i/archify` | 62427 | 4121 | JavaScript | 49,900 stars this month | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify |  |
| 3 | `anthropics/claude-plugins-community` | 4033 | 297 | Python | 3,715 stars this month | Claude Cowork和Claude Code的社区插件市场。只读镜像—在clau.de/plugin-directory-submission上提交插件。 | https://github.com/anthropics/claude-plugins-community |  |
| 4 | `AprilNEA/OpenLogi` | 21095 | 679 | Rust | 12,695 stars this month | ⚡️用Rust编写的Logitech Options +的本地本地优先替代方案🦀—在HID + +上重新映射按钮、DPI和SmartShift。无帐户，无遥测。 | https://github.com/AprilNEA/OpenLogi |  |
| 5 | `cursor/plugins` | 7751 | 687 | TypeScript | 5,026 stars this month | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 6 | `volcengine/OpenViking` | 37275 | 2868 | Python | 8,921 stars this month | 人工智能代理的自我进化上下文数据库。统一座席记忆、知识抹布和技能。 | https://github.com/volcengine/OpenViking |  |
| 7 | `freestylefly/awesome-gpt-image-2` | 31919 | 3076 | JavaScript | 22,081 stars this month | Prompt as Code · GPT Image 2 / 2.5 提示词与案例库，530+ 个案例、20+ 套工业级模板与可复用 Skills，新增 2.5 同提示词对比专区，附完整提示词与生成记录，持续更新。 | https://github.com/freestylefly/awesome-gpt-image-2 |  |
| 8 | `cathrynlavery/diagram-design` | 39868 | 2528 | HTML | 23,268 stars this month | Claude Code、Codex和Pi的38种编辑图类型。独立的HTML + SVG。没有阴影，没有美人鱼粪便。 | https://github.com/cathrynlavery/diagram-design |  |
| 9 | `THU-MAIC/OpenMAIC` | 36872 | 5823 | TypeScript | 16,207 stars this month | 开放式多座席互动课堂—只需点击一下，即可获得身临其境的多座席学习体验 | https://github.com/THU-MAIC/OpenMAIC |  |
| 10 | `ayghri/i-have-adhd` | 45527 | 2640 | Python | 24,963 stars this month | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 11 | `vorssaint/vorssaint-utils` | 19035 | 679 | Swift | 13,706 stars this month | 免费开源的macOS菜单栏工具包。 | https://github.com/vorssaint/vorssaint-utils |  |
| 12 | `debpalash/VoiceStudio` | 29436 | 3570 | Python | 18,692 stars this month | VoiceStudio是开源、完全本地的ElevenLabs替代品--语音克隆、语音设计、视频配音、听写、转录和有声读物创作，支持646种语言。 | https://github.com/debpalash/VoiceStudio |  |
| 13 | `modular/modular` | 29748 | 3173 | Mojo | 3,049 stars this month | 模块化平台（包括MAX和Mojo ） | https://github.com/modular/modular |  |
| 14 | `akitaonrails/ai-memory` | 6828 | 460 | Rust | 5,351 stars this month | 针对座席编码CLI的长期记忆解决方案，以及促进不同座席供应商之间切换的解决方案 | https://github.com/akitaonrails/ai-memory |  |
| 15 | `Lakr233/vphone-cli` | 12122 | 1516 | Swift | 4,310 stars this month | — | https://github.com/Lakr233/vphone-cli |  |
| 16 | `apache/maka` | 5414 | 502 | TypeScript | 4,111 stars this month | Apache Maka （孵化）是一个高性能代理工作区，可完整记录其所做的一切。 | https://github.com/apache/maka |  |
| 17 | `microsoft/data-formulator` | 17189 | 1673 | Python | 1,158 stars this month | 🪄 Data Formulator是一个交互式人工智能数据分析系统，可轻松连接、探索和可视化数据。 | https://github.com/microsoft/data-formulator | 新增 |
| 18 | `public-apis/public-apis` | 480248 | 52967 | Python | 23,551 stars this month | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis | 新增 |
| 19 | `google-research/timesfm` | 32507 | 3116 | Python | 5,252 stars this month | TimesFM （时间序列基础模型）是由Google Research开发的用于时间序列预测的预训练时间序列基础模型。 | https://github.com/google-research/timesfm | 新增 |


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

**最近一次更新时间**（Asia/Shanghai）： 2026-09-14 09:19:11

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 547053 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 505779 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 479776 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 455401 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 396703 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 389620 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `donnemartin/system-design-primer` | 369821 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 8 | `nilbuild/developer-roadmap` | 367100 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 9 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 10 | `jwasham/coding-interview-university` | 360845 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 11 | `vinta/awesome-python` | 320453 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `JustVugg/colibri` | 29864 | 3250 | C | 868 stars today | 在您已经拥有的硬件上运行前沿MoE模型—纯C ，零DEPS ，从磁盘流式传输的专家。微型引擎，超大型号。 🐦 | https://github.com/JustVugg/colibri |  |
| 2 | `ever-co/ever-gauzy` | 5101 | 946 | TypeScript | 191 stars today | Ever ® Gauzy™ -开放式业务管理平台（ ERP/CRM/HRM/ATS/PM ） - https://gauzy.co | https://github.com/ever-co/ever-gauzy | 新增 |
| 3 | `bilawalsidhu/gods-eye-view` | 31926 | 6409 | JavaScript | 2,680 stars today | 浏览器中的间谍卫星模拟器，但数据是真实的。在逼真的3D地球仪上实时开源空间智能。 | https://github.com/bilawalsidhu/gods-eye-view |  |
| 4 | `tech-leads-club/agent-skills` | 5661 | 499 | TypeScript | 265 stars today | 专业AI编码代理的安全、经过验证的技能注册表。绝对自信地扩展Antigravity、Claude Code、Cursor、Copilot等。 | https://github.com/tech-leads-club/agent-skills | 新增 |
| 5 | `melgarafael/DeskcommCRM` | 2196 | 595 | TypeScript | 432 stars today | 开源AI销售操作系统—使用本地AI代理+ WhatsApp (WAHA)的自托管CRM。对于任何通过聊天销售的企业， Kommo、Octadesk和Intercom的替代方案都是开放的。MCP就绪、多租户、LGPD。 | https://github.com/melgarafael/DeskcommCRM | 新增 |
| 6 | `calesthio/OpenMontage` | 58451 | 7356 | Python | 380 stars today | 全球首个开源代理视频制作系统。12个制作管道、100多个工具、700多个代理技能和生产知识文件。将您的AI编码助手变成一个完整的视频制作工作室。 | https://github.com/calesthio/OpenMontage | 新增 |
| 7 | `asgeirtj/system_prompts_leaks` | 66048 | 10803 | JavaScript | 706 stars today | 从Anthropic - Claude Fable 5.1、Opus 5、Claude Design、Claude Code中提取系统提示。OpenAI - ChatGPT GPT-6-Astra ， Codex。Google - Gemini 3.8 Flash、3.1 Pro、Antigravity。xAI - Grok、Grok Bot、Cursor、Kimi等！定期更新。 | https://github.com/asgeirtj/system_prompts_leaks | 新增 |
| 8 | `vxcontrol/pentagi` | 23983 | 3095 | Go | 590 stars today | 完全自主的AI Agents系统，能够执行复杂的渗透测试任务 | https://github.com/vxcontrol/pentagi | 新增 |
| 9 | `multimodal-art-projection/YuE` | 7757 | 866 | Python | 487 stars today | YuE2 ：具有象征性规划、零封面和代理音乐编辑的前沿音乐生成。 | https://github.com/multimodal-art-projection/YuE | 新增 |
| 10 | `yuliskov/SmartTube` | 33453 | 2032 | Java | 233 stars today | 在Android TV上使用您自己的规则浏览媒体内容 | https://github.com/yuliskov/SmartTube | 新增 |
| 11 | `alphaXiv/OpenResearch` | 2072 | 144 | Rust | 289 stars today | 使用任何模型运行并行研究代理 | https://github.com/alphaXiv/OpenResearch | 新增 |
| 12 | `debpalash/VoiceStudio` | 26873 | 3316 | Python | 2,632 stars today | VoiceStudio是开源、完全本地的ElevenLabs替代品--语音克隆、语音设计、视频配音、听写、转录和有声读物创作，支持646种语言。 | https://github.com/debpalash/VoiceStudio | 新增 |
| 13 | `SnailSploit/Claude-Red` | 4155 | 592 | Python | 506 stars today | claude-red是为Claude技能系统设计的攻击性安全技能精心策划的图书馆。每个技能都是一个结构化的SKILL.md文件，为Claude提供了针对特定攻击面的专家级方法--从SQLi到shellcode ，从EDR规避到利用开发人员…… | https://github.com/SnailSploit/Claude-Red | 新增 |
| 14 | `alibaba/open-code-review` | 23537 | 1742 | Go | 443 stars today | 快速、高效、经受住阿里巴巴规模的考验。混合架构代码审核工具：确定性流水线+ LLM Agent、精确的行级注释、内置多语言规则集（ NPE、线程安全、XSS、SQL注入）、OpenAI &amp; Anthropic兼容。 | https://github.com/alibaba/open-code-review | 新增 |
| 15 | `jihe520/MathModelAgent` | 5354 | 408 | Python | 246 stars today | 🤖📐专为数学建模设计的 Agent &amp; skills ,自动完成数学建模，生成一份完整的可以直接提交的论文。 An Agent Designed for Mathematical Modeling ,Automatically complete mathmodel and generate a complete paper ready for submission. | https://github.com/jihe520/MathModelAgent | 新增 |
| 16 | `tonhowtf/omniget` | 11674 | 1021 | Rust | 507 stars today | 下载Udemy和Hotmart课程、YouTube视频、音乐和书籍—超过1800个网站，无终端。适用于Windows、macOS和Linux的免费开源桌面应用程序，内置课程播放器、PDF/EPUB阅读器和音乐库。由yt-dlp提供支持。您的文件将保存在您的计算机上。 | https://github.com/tonhowtf/omniget | 新增 |
| 17 | `jiji262/douyin-downloader` | 11368 | 1751 | Python | 452 stars today | A practical Douyin downloader for both single-item and profile batch downloads, with progress display, retries, SQLite deduplication, and browser fallback support. 抖音批量下载工具，去水印，支持视频、图集、合集、音乐(原声)。 | https://github.com/jiji262/douyin-downloader | 新增 |
| 18 | `Swordfish90/cool-retro-term` | 26229 | 1016 | QML | 57 stars today | 一个好看的终端模拟器，模仿旧的阴极显示器... | https://github.com/Swordfish90/cool-retro-term | 新增 |
| 19 | `huggingface/transformers` | 165532 | 34557 | Python | 152 stars today | 🤗 Transformers ：用于推理和训练的文本、视觉、音频和多模态模型中最先进的机器学习模型的模型定义框架。 | https://github.com/huggingface/transformers | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `ayghri/i-have-adhd` | 44342 | 2547 | Python | 16,740 stars this week | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 2 | `affaan-m/ECC` | 257767 | 38551 | JavaScript | 7,264 stars this week | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 3 | `openai/plugins` | 6618 | 871 | JavaScript | 1,181 stars this week | OpenAI插件 | https://github.com/openai/plugins |  |
| 4 | `bilawalsidhu/gods-eye-view` | 31926 | 6409 | JavaScript | 12,931 stars this week | 浏览器中的间谍卫星模拟器，但数据是真实的。在逼真的3D地球仪上实时开源空间智能。 | https://github.com/bilawalsidhu/gods-eye-view |  |
| 5 | `mksglu/context-mode` | 22630 | 1631 | TypeScript | 2,102 stars this week | 人工智能编码代理的上下文窗口优化。沙盒工具输出（减少98 ％ ） ，保持会话内存，并通过MCP +钩子在17个平台上强制路由。 | https://github.com/mksglu/context-mode |  |
| 6 | `DietrichGebert/ponytail` | 137341 | 7376 | JavaScript | 8,444 stars this week | 让你的人工智能代理像房间里最懒惰的高级开发人员一样思考。最好的代码是你从未写过的代码。 | https://github.com/DietrichGebert/ponytail |  |
| 7 | `tt-a1i/archify` | 60790 | 3995 | JavaScript | 10,132 stars this week | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify |  |
| 8 | `openai/skills` | 27096 | 1809 | Python | 1,622 stars this week | Codex技能目录 | https://github.com/openai/skills |  |
| 9 | `heygen-com/hyperframes` | 49606 | 4532 | TypeScript | 5,146 stars this week | 编写HTML。渲染视频。专为客服代表打造。 | https://github.com/heygen-com/hyperframes |  |
| 10 | `microsoft/markitdown` | 183599 | 13509 | Python | 5,191 stars this week | 用于将文件和Office文档转换为Markdown的Python工具。 | https://github.com/microsoft/markitdown |  |
| 11 | `obra/superpowers` | 286205 | 25606 | Shell | 4,068 stars this week | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers | 新增 |
| 12 | `coreyhaines31/marketingskills` | 49996 | 7590 | JavaScript | 2,678 stars this week | Claude Code和人工智能代理的营销技能。CRO、文案撰写、搜索引擎优化、分析和增长工程。 | https://github.com/coreyhaines31/marketingskills |  |
| 13 | `ChromeDevTools/chrome-devtools-mcp` | 51845 | 3641 | TypeScript | 736 stars this week | 适用于编码代理的Chrome开发者工具 | https://github.com/ChromeDevTools/chrome-devtools-mcp |  |
| 14 | `cathrynlavery/diagram-design` | 39224 | 2490 | HTML | 7,129 stars this week | Claude Code、Codex和Pi的38种编辑图类型。独立的HTML + SVG。没有阴影，没有美人鱼粪便。 | https://github.com/cathrynlavery/diagram-design |  |
| 15 | `THU-MAIC/OpenMAIC` | 36479 | 5782 | TypeScript | 4,202 stars this week | 开放式多座席互动课堂—只需点击一下，即可获得身临其境的多座席学习体验 | https://github.com/THU-MAIC/OpenMAIC |  |
| 16 | `Tencent/WeKnora` | 22883 | 3267 | Go | 1,302 stars this week | 开源LLM知识平台：将原始文档转化为可查询的RAG、自主推理代理和自我维护的Wiki。 | https://github.com/Tencent/WeKnora | 新增 |
| 17 | `blader/humanizer` | 47674 | 3880 | Python | 3,673 stars this week | 从文本中删除人工智能生成文字的迹象的代理技能 | https://github.com/blader/humanizer |  |
| 18 | `max-sixty/worktrunk` | 7523 | 269 | Rust | 588 stars this week | Worktrunk是用于Git工作树管理的CLI ，专为并行AI代理工作流程而设计 | https://github.com/max-sixty/worktrunk | 新增 |
| 19 | `humanlayer/skills` | 4000 | 121 | TypeScript | 1,004 stars this week | — | https://github.com/humanlayer/skills | 新增 |
| 20 | `earthtojake/text-to-cad` | 15591 | 1611 | Python | 1,054 stars this week | CAD、CAE和CAM的代理技能库 | https://github.com/earthtojake/text-to-cad | 新增 |
| 21 | `petergyang/no-ai-slop` | 9201 | 672 | Python | 1,668 stars this week | 从任何文字中删除20多种AI斜坡图案。 | https://github.com/petergyang/no-ai-slop | 新增 |
| 22 | `github/spec-kit` | 136417 | 12252 | Python | 2,642 stars this week | 帮助您开始规格驱动开发💫的工具包 | https://github.com/github/spec-kit | 新增 |
| 23 | `kunchenguid/firstmate` | 5748 | 1785 | Shell | 778 stars this week | 与一位客服代表交谈。船上有船员。 | https://github.com/kunchenguid/firstmate | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `omacom/omarchy` | 40852 | 4582 | Shell | 16,489 stars this month | 漂亮、现代且自以为是的Linux | https://github.com/omacom/omarchy |  |
| 2 | `tt-a1i/archify` | 60791 | 3995 | JavaScript | 48,808 stars this month | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify |  |
| 3 | `anthropics/claude-plugins-community` | 3941 | 289 | Python | 3,635 stars this month | Claude Cowork和Claude Code的社区插件市场。只读镜像—在clau.de/plugin-directory-submission上提交插件。 | https://github.com/anthropics/claude-plugins-community |  |
| 4 | `AprilNEA/OpenLogi` | 20944 | 674 | Rust | 12,557 stars this month | ⚡️用Rust编写的Logitech Options +的本地本地优先替代方案🦀—在HID + +上重新映射按钮、DPI和SmartShift。无帐户，无遥测。 | https://github.com/AprilNEA/OpenLogi |  |
| 5 | `cursor/plugins` | 7623 | 673 | TypeScript | 4,967 stars this month | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 6 | `volcengine/OpenViking` | 37031 | 2843 | Python | 8,745 stars this month | 人工智能代理的自我进化上下文数据库。统一座席记忆、知识抹布和技能。 | https://github.com/volcengine/OpenViking |  |
| 7 | `cathrynlavery/diagram-design` | 39225 | 2490 | HTML | 26,213 stars this month | Claude Code、Codex和Pi的38种编辑图类型。独立的HTML + SVG。没有阴影，没有美人鱼粪便。 | https://github.com/cathrynlavery/diagram-design |  |
| 8 | `freestylefly/awesome-gpt-image-2` | 31655 | 3062 | JavaScript | 21,897 stars this month | Prompt as Code · GPT Image 2 / 2.5 提示词与案例库，530+ 个案例、20+ 套工业级模板与可复用 Skills，新增 2.5 同提示词对比专区，附完整提示词与生成记录，持续更新。 | https://github.com/freestylefly/awesome-gpt-image-2 |  |
| 9 | `THU-MAIC/OpenMAIC` | 36479 | 5782 | TypeScript | 15,888 stars this month | 开放式多座席互动课堂—只需点击一下，即可获得身临其境的多座席学习体验 | https://github.com/THU-MAIC/OpenMAIC |  |
| 10 | `ayghri/i-have-adhd` | 44342 | 2547 | Python | 24,025 stars this month | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 11 | `vorssaint/vorssaint-utils` | 18770 | 673 | Swift | 13,520 stars this month | 免费开源的macOS菜单栏工具包。 | https://github.com/vorssaint/vorssaint-utils |  |
| 12 | `modular/modular` | 29729 | 3169 | Mojo | 3,049 stars this month | 模块化平台（包括MAX和Mojo ） | https://github.com/modular/modular |  |
| 13 | `akitaonrails/ai-memory` | 6695 | 453 | Rust | 5,269 stars this month | 针对座席编码CLI的长期记忆解决方案，以及促进不同座席供应商之间切换的解决方案 | https://github.com/akitaonrails/ai-memory |  |
| 14 | `Lakr233/vphone-cli` | 11846 | 1491 | Swift | 4,221 stars this month | — | https://github.com/Lakr233/vphone-cli |  |
| 15 | `debpalash/VoiceStudio` | 26875 | 3316 | Python | 15,895 stars this month | VoiceStudio是开源、完全本地的ElevenLabs替代品--语音克隆、语音设计、视频配音、听写、转录和有声读物创作，支持646种语言。 | https://github.com/debpalash/VoiceStudio |  |
| 16 | `apache/maka` | 5346 | 497 | TypeScript | 4,056 stars this month | Apache Maka （孵化）是一个高性能代理工作区，可完整记录其所做的一切。 | https://github.com/apache/maka |  |
| 17 | `cordiverse/cordis` | 8451 | 528 | TypeScript | 7,887 stars this month | 时空可组合性元框架 | https://github.com/cordiverse/cordis | 新增 |


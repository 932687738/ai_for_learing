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

**最近一次更新时间**（Asia/Shanghai）： 2026-09-11 11:41:45

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 546452 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 504889 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 478687 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 455281 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 396470 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 389413 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `donnemartin/system-design-primer` | 369307 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 8 | `nilbuild/developer-roadmap` | 366855 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 9 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 10 | `jwasham/coding-interview-university` | 360714 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 11 | `vinta/awesome-python` | 319852 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `ayghri/i-have-adhd` | 38745 | 2220 | Python | 3,882 stars today | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 2 | `bilawalsidhu/gods-eye-view` | 24673 | 5109 | JavaScript | 1,762 stars today | 浏览器中的间谍卫星模拟器，但数据是真实的。在逼真的3D地球仪上实时开源空间智能。 | https://github.com/bilawalsidhu/gods-eye-view | 新增 |
| 3 | `obra/superpowers` | 284786 | 25476 | Shell | 732 stars today | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers |  |
| 4 | `alsk1992/CloddsBot` | 1742 | 261 | TypeScript | 277 stars today | 开源AI交易代理，在1000多个市场（ Polymarket、Kalshi、Binance、Hyperliquid、Solana DEXs、5条EVM链）自主运营。扫描边缘，即时执行，在您睡觉时管理风险。机器对机器支付的代理商务协议。Self-hos… | https://github.com/alsk1992/CloddsBot | 新增 |
| 5 | `Tencent/teamai-cli` | 3891 | 252 | TypeScript | 841 stars today | 让每个团队都成为原生AI | https://github.com/Tencent/teamai-cli |  |
| 6 | `AlexsJones/llmfit` | 35806 | 2270 | Rust | 258 stars today | 数以百计的模型和提供商。只需一个命令，即可查找硬件上运行的内容。 | https://github.com/AlexsJones/llmfit | 新增 |
| 7 | `liquidslr/system-design-notes` | 18902 | 3495 | — | 900 stars today | 《System Desgin Interview - An Insider's Guide》一书的笔记 | https://github.com/liquidslr/system-design-notes |  |
| 8 | `cathrynlavery/diagram-design` | 37900 | 2399 | HTML | 1,294 stars today | Claude Code、Codex和Pi的38种编辑图类型。独立的HTML + SVG。没有阴影，没有美人鱼粪便。 | https://github.com/cathrynlavery/diagram-design |  |
| 9 | `freestylefly/awesome-gpt-image-2` | 30972 | 3001 | JavaScript | 962 stars today | Prompt as Code · GPT Image 2 / 2.5 提示词与案例库，530+ 个案例、20+ 套工业级模板与可复用 Skills，新增 2.5 同提示词对比专区，附完整提示词与生成记录，持续更新。 | https://github.com/freestylefly/awesome-gpt-image-2 |  |
| 10 | `armory3d/armorpaint` | 4464 | 522 | C | 72 stars today | 图形创建工具 | https://github.com/armory3d/armorpaint | 新增 |
| 11 | `diegosouzapw/OmniRoute` | 64344 | 9004 | TypeScript | 626 stars today | 永不停止编码。免费MIT AI网关：一个端点， 352个提供商（ 150多个免费） ， 1200多个型号Kimi、Claude、GPT、Gemini、GLM、DeepSeek、MiniMax。适用于Claude Code、Codex、Cursor、OpenCode、Cline和Copilot。配额感知自动回退， RTK +穴居人压缩节省15-95% …… | https://github.com/diegosouzapw/OmniRoute | 新增 |
| 12 | `JustVugg/colibri` | 27515 | 3014 | C | 98 stars today | 在您已经拥有的硬件上运行前沿MoE模型—纯C ，零DEPS ，从磁盘流式传输的专家。微型引擎，超大型号。 🐦 | https://github.com/JustVugg/colibri | 新增 |
| 13 | `THU-MAIC/OpenMAIC` | 35454 | 5652 | TypeScript | 837 stars today | 开放式多座席互动课堂—只需点击一下，即可获得身临其境的多座席学习体验 | https://github.com/THU-MAIC/OpenMAIC | 新增 |
| 14 | `nashsu/llm_wiki` | 18200 | 2104 | TypeScript | 142 stars today | LLM Wiki是一个跨平台的桌面应用程序，可自动将您的文档转换为有组织的、相互关联的知识库。LLM不是传统的RAG （每次都从头开始检索和回答） ，而是逐渐构建和维护一个永久的wiki…… | https://github.com/nashsu/llm_wiki | 新增 |
| 15 | `vercel-labs/skills` | 31218 | 2665 | TypeScript | 122 stars today | 开放式客服代表技能工具- npx技能 | https://github.com/vercel-labs/skills | 新增 |
| 16 | `vastsa/PI-Desktop` | 2378 | 197 | TypeScript | 624 stars today | 本地优先AI编码代理桌面： Electron + Rust host core + pi Agent Harness +用户可安装插件 | https://github.com/vastsa/PI-Desktop |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `affaan-m/ECC` | 255965 | 38310 | JavaScript | 9,257 stars this week | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 2 | `ayghri/i-have-adhd` | 38745 | 2220 | Python | 10,215 stars this week | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 3 | `DietrichGebert/ponytail` | 134912 | 7230 | JavaScript | 11,638 stars this week | 让你的人工智能代理像房间里最懒惰的高级开发人员一样思考。最好的代码是你从未写过的代码。 | https://github.com/DietrichGebert/ponytail |  |
| 4 | `tt-a1i/archify` | 57567 | 3762 | JavaScript | 11,958 stars this week | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify |  |
| 5 | `fmtlib/fmt` | 25723 | 3059 | C++ | 920 stars this week | 现代格式化库 | https://github.com/fmtlib/fmt |  |
| 6 | `mattpocock/skills` | 258982 | 21821 | Shell | 12,356 stars this week | 真正工程师的技能。直接来自我的.agents目录。 | https://github.com/mattpocock/skills |  |
| 7 | `openai/plugins` | 6392 | 842 | JavaScript | 1,018 stars this week | OpenAI插件 | https://github.com/openai/plugins |  |
| 8 | `blader/humanizer` | 46553 | 3807 | Python | 5,224 stars this week | 从文本中删除人工智能生成文字的迹象的代理技能 | https://github.com/blader/humanizer |  |
| 9 | `mksglu/context-mode` | 22035 | 1586 | TypeScript | 1,619 stars this week | 人工智能编码代理的上下文窗口优化。沙盒工具输出（减少98 ％ ） ，保持会话内存，并通过MCP +钩子在17个平台上强制路由。 | https://github.com/mksglu/context-mode |  |
| 10 | `openai/skills` | 26869 | 1801 | Python | 1,490 stars this week | Codex技能目录 | https://github.com/openai/skills |  |
| 11 | `heygen-com/hyperframes` | 48810 | 4465 | TypeScript | 4,896 stars this week | 编写HTML。渲染视频。专为客服代表打造。 | https://github.com/heygen-com/hyperframes |  |
| 12 | `ChromeDevTools/chrome-devtools-mcp` | 51592 | 3625 | TypeScript | 791 stars this week | 适用于编码代理的Chrome开发者工具 | https://github.com/ChromeDevTools/chrome-devtools-mcp |  |
| 13 | `NousResearch/hermes-agent` | 244261 | 50541 | Python | 3,769 stars this week | 与您一起成长的客服代表 | https://github.com/NousResearch/hermes-agent |  |
| 14 | `coreyhaines31/marketingskills` | 49470 | 7535 | JavaScript | 2,711 stars this week | Claude Code和人工智能代理的营销技能。CRO、文案撰写、搜索引擎优化、分析和增长工程。 | https://github.com/coreyhaines31/marketingskills |  |
| 15 | `cathrynlavery/diagram-design` | 37901 | 2399 | HTML | 7,329 stars this week | Claude Code、Codex和Pi的38种编辑图类型。独立的HTML + SVG。没有阴影，没有美人鱼粪便。 | https://github.com/cathrynlavery/diagram-design | 新增 |
| 16 | `microsoft/markitdown` | 182477 | 13412 | Python | 4,579 stars this week | 用于将文件和Office文档转换为Markdown的Python工具。 | https://github.com/microsoft/markitdown | 新增 |
| 17 | `ruvnet/ruflo` | 72006 | 8518 | TypeScript | 1,694 stars this week | 🌊 原始Agent元Harness。部署智能多玩家群体，协调自主工作流程，构建对话式人工智能系统。具有自适应记忆、自我学习智能、RAG集成和原生Claude Code/Codex/Hermes等功能集成 | https://github.com/ruvnet/ruflo |  |
| 18 | `THU-MAIC/OpenMAIC` | 35454 | 5652 | TypeScript | 4,174 stars this week | 开放式多座席互动课堂—只需点击一下，即可获得身临其境的多座席学习体验 | https://github.com/THU-MAIC/OpenMAIC |  |
| 19 | `anthropics/skills` | 175696 | 20791 | Python | 2,234 stars this week | 座席技能的公共存储库 | https://github.com/anthropics/skills | 新增 |
| 20 | `bilawalsidhu/gods-eye-view` | 24674 | 5109 | JavaScript | 6,051 stars this week | 浏览器中的间谍卫星模拟器，但数据是真实的。在逼真的3D地球仪上实时开源空间智能。 | https://github.com/bilawalsidhu/gods-eye-view | 新增 |
| 21 | `every-app/open-seo` | 18307 | 2315 | TypeScript | 1,679 stars this week | Semrush和Ahrefs的开源替代品 | https://github.com/every-app/open-seo |  |
| 22 | `anomalyco/opencode` | 206523 | 27003 | TypeScript | 3,139 stars this week | 开源编码代理。 | https://github.com/anomalyco/opencode | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `omacom/omarchy` | 40103 | 4401 | Shell | 15,894 stars this month | 漂亮、现代且自以为是的Linux | https://github.com/omacom/omarchy |  |
| 2 | `cathrynlavery/diagram-design` | 37901 | 2399 | HTML | 33,361 stars this month | Claude Code、Codex和Pi的38种编辑图类型。独立的HTML + SVG。没有阴影，没有美人鱼粪便。 | https://github.com/cathrynlavery/diagram-design |  |
| 3 | `cursor/plugins` | 7394 | 647 | TypeScript | 4,798 stars this month | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 4 | `tt-a1i/archify` | 57568 | 3762 | JavaScript | 46,339 stars this month | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify |  |
| 5 | `anthropics/claude-plugins-community` | 3755 | 283 | Python | 3,460 stars this month | Claude Cowork和Claude Code的社区插件市场。只读镜像—在clau.de/plugin-directory-submission上提交插件。 | https://github.com/anthropics/claude-plugins-community |  |
| 6 | `AprilNEA/OpenLogi` | 20561 | 642 | Rust | 12,225 stars this month | ⚡️用Rust编写的Logitech Options +的本地本地优先替代方案🦀—在HID + +上重新映射按钮、DPI和SmartShift。无帐户，无遥测。 | https://github.com/AprilNEA/OpenLogi |  |
| 7 | `volcengine/OpenViking` | 36550 | 2798 | Python | 8,469 stars this month | 人工智能代理的自我进化上下文数据库。统一座席记忆、知识抹布和技能。 | https://github.com/volcengine/OpenViking |  |
| 8 | `xai-org/x-algorithm` | 33080 | 5383 | Rust | 6,248 stars this month | 为X上的For You馈送供电的算法 | https://github.com/xai-org/x-algorithm |  |
| 9 | `freestylefly/awesome-gpt-image-2` | 30973 | 3001 | JavaScript | 21,157 stars this month | Prompt as Code · GPT Image 2 / 2.5 提示词与案例库，530+ 个案例、20+ 套工业级模板与可复用 Skills，新增 2.5 同提示词对比专区，附完整提示词与生成记录，持续更新。 | https://github.com/freestylefly/awesome-gpt-image-2 |  |
| 10 | `NVIDIA-NeMo/Switchyard` | 2839 | 257 | Python | 2,628 stars this month | Switchyard允许LLM应用程序跨模型和提供商路由流量，同时保留原生OpenAI和人工API兼容性，从而实现灵活的模型选择、基准测试和成本/性能优化。 | https://github.com/NVIDIA-NeMo/Switchyard | 新增 |
| 11 | `semantica-agi/semantica` | 12623 | 1414 | Python | 8,849 stars this month | 上下文和负责任的人工智能系统的图形原生基础设施 | https://github.com/semantica-agi/semantica |  |
| 12 | `THU-MAIC/OpenMAIC` | 35454 | 5652 | TypeScript | 14,604 stars this month | 开放式多座席互动课堂—只需点击一下，即可获得身临其境的多座席学习体验 | https://github.com/THU-MAIC/OpenMAIC |  |
| 13 | `youssofal/MTPLX` | 2218 | 164 | Python | 1,060 stars this month | 在MLX上速度提高3倍· Qwen 3.8 27B ·在Apple Silicon上进行原生MTP投机解码，无需外部绘图员。 | https://github.com/youssofal/MTPLX | 新增 |
| 14 | `vorssaint/vorssaint-utils` | 18125 | 643 | Swift | 13,129 stars this month | 免费开源的macOS菜单栏工具包。 | https://github.com/vorssaint/vorssaint-utils |  |
| 15 | `modular/modular` | 29672 | 3165 | Mojo | 3,080 stars this month | 模块化平台（包括MAX和Mojo ） | https://github.com/modular/modular |  |
| 16 | `debpalash/VoiceStudio` | 22299 | 2744 | Python | 12,418 stars this month | VoiceStudio是开源、完全本地的ElevenLabs替代品--语音克隆、语音设计、视频配音、听写、转录和有声读物创作，支持646种语言。 | https://github.com/debpalash/VoiceStudio |  |
| 17 | `akitaonrails/ai-memory` | 6484 | 446 | Rust | 5,026 stars this month | 针对座席编码CLI的长期记忆解决方案，以及促进不同座席供应商之间切换的解决方案 | https://github.com/akitaonrails/ai-memory |  |
| 18 | `Lakr233/vphone-cli` | 11486 | 1459 | Swift | 3,892 stars this month | — | https://github.com/Lakr233/vphone-cli |  |
| 19 | `public-apis/public-apis` | 478687 | 52834 | Python | 24,223 stars this month | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 20 | `cactus-compute/needle` | 10776 | 688 | Python | 7,395 stars this month | 14MB基础型号，适用于微型设备；手机、可穿戴设备、智能家居和机器人。 | https://github.com/cactus-compute/needle |  |
| 21 | `apache/maka` | 5206 | 484 | TypeScript | 3,941 stars this month | Apache Maka （孵化）是一个高性能代理工作区，可完整记录其所做的一切。 | https://github.com/apache/maka |  |
| 22 | `AlexsJones/llmfit` | 35806 | 2270 | Rust | 4,375 stars this month | 数以百计的模型和提供商。只需一个命令，即可查找硬件上运行的内容。 | https://github.com/AlexsJones/llmfit | 新增 |
| 23 | `ayghri/i-have-adhd` | 38745 | 2220 | Python | 18,245 stars this month | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd | 新增 |
| 24 | `harry0703/MoneyPrinterTurbo` | 122287 | 18886 | Python | 20,448 stars this month | 利用 AI 大模型和自动化工作流，根据主题或关键词一键生成高清短视频。Generate HD short videos from a topic or keyword with an automated AI workflow. | https://github.com/harry0703/MoneyPrinterTurbo | 新增 |


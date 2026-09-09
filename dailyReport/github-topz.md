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

**最近一次更新时间**（Asia/Shanghai）： 2026-09-09 09:10:42

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 546068 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 504287 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 477622 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 455236 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 396304 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 389250 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `donnemartin/system-design-primer` | 368817 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 8 | `nilbuild/developer-roadmap` | 366630 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 9 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 10 | `jwasham/coding-interview-university` | 360600 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 11 | `vinta/awesome-python` | 319387 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `ayghri/i-have-adhd` | 30490 | 1858 | Python | 656 stars today | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 2 | `cathrynlavery/diagram-design` | 34836 | 2203 | HTML | 710 stars today | Claude Code、Codex和Pi的38种编辑图类型。独立的HTML + SVG。没有阴影，没有美人鱼粪便。 | https://github.com/cathrynlavery/diagram-design |  |
| 3 | `openai/skills` | 26518 | 1776 | Python | 490 stars today | Codex技能目录 | https://github.com/openai/skills |  |
| 4 | `affaan-m/ECC` | 254308 | 38112 | JavaScript | 1,427 stars today | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 5 | `heygen-com/hyperframes` | 47766 | 4393 | TypeScript | 2,627 stars today | 编写HTML。渲染视频。专为客服代表打造。 | https://github.com/heygen-com/hyperframes |  |
| 6 | `coreyhaines31/marketingskills` | 48823 | 7495 | JavaScript | 666 stars today | Claude Code和人工智能代理的营销技能。CRO、文案撰写、搜索引擎优化、分析和增长工程。 | https://github.com/coreyhaines31/marketingskills |  |
| 7 | `obra/superpowers` | 283364 | 25368 | Shell | 452 stars today | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers |  |
| 8 | `multica-ai/andrej-karpathy-skills` | 211459 | 21473 | — | 333 stars today | 一个用于改进Claude Code行为的CLAUDE.md文件，源自Andrej Karpathy对LLM编码陷阱的观察。 | https://github.com/multica-ai/andrej-karpathy-skills |  |
| 9 | `microsoft/markitdown` | 181692 | 13347 | Python | 2,047 stars today | 用于将文件和Office文档转换为Markdown的Python工具。 | https://github.com/microsoft/markitdown |  |
| 10 | `jo-inc/camofox-browser` | 10500 | 1052 | JavaScript | 871 stars today | 适用于AI代理的隐形无头浏览器—绕过Cloudflare、机器人检测和反抓取。代替偶人/剧作家。 | https://github.com/jo-inc/camofox-browser |  |
| 11 | `MoonTechLab/LunaTV` | 10175 | 9046 | TypeScript | 505 stars today | 本项目采用 CC BY-NC-SA 协议，禁止任何商业化行为，任何衍生项目必须保留本项目地址并以相同协议开源 | https://github.com/MoonTechLab/LunaTV |  |
| 12 | `browser-use/browser-use` | 113513 | 12489 | Python | 228 stars today | 使用浏览器的代理。 | https://github.com/browser-use/browser-use |  |
| 13 | `mksglu/context-mode` | 21398 | 1544 | TypeScript | 651 stars today | 人工智能编码代理的上下文窗口优化。沙盒工具输出（减少98 ％ ） ，保持会话内存，并通过MCP +钩子在17个平台上强制路由。 | https://github.com/mksglu/context-mode |  |
| 14 | `The-Swarm-Corporation/AutoHedge` | 5711 | 840 | Python | 494 stars today | 在几分钟内建立您的自主对冲基金。AutoHedge利用群体智能和人工智能代理的强大功能，实现市场分析、风险管理和交易执行的自动化。 | https://github.com/The-Swarm-Corporation/AutoHedge |  |
| 15 | `viarotel-org/escrcpy` | 11404 | 795 | JavaScript | 178 stars today | 使用scrcpy以图形方式📱显示和控制您的Android设备。 | https://github.com/viarotel-org/escrcpy |  |
| 16 | `openai/plugins` | 5800 | 800 | JavaScript | 105 stars today | OpenAI插件 | https://github.com/openai/plugins |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `fmtlib/fmt` | 25680 | 3049 | C++ | 1,935 stars this week | 现代格式化库 | https://github.com/fmtlib/fmt |  |
| 2 | `affaan-m/ECC` | 254308 | 38112 | JavaScript | 8,527 stars this week | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 3 | `DietrichGebert/ponytail` | 132212 | 7073 | JavaScript | 12,598 stars this week | 让你的人工智能代理像房间里最懒惰的高级开发人员一样思考。最好的代码是你从未写过的代码。 | https://github.com/DietrichGebert/ponytail |  |
| 4 | `tt-a1i/archify` | 54728 | 3587 | JavaScript | 13,318 stars this week | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify |  |
| 5 | `blader/humanizer` | 45420 | 3744 | Python | 5,790 stars this week | 从文本中删除人工智能生成文字的迹象的代理技能 | https://github.com/blader/humanizer |  |
| 6 | `Imbad0202/academic-research-skills` | 47055 | 3682 | Python | 2,430 stars this week | Claude Code的学术研究技能：研究→撰写→评审→修订→最终确定 | https://github.com/Imbad0202/academic-research-skills |  |
| 7 | `mattpocock/skills` | 256975 | 21645 | Shell | 13,419 stars this week | 真正工程师的技能。直接来自我的.agents目录。 | https://github.com/mattpocock/skills |  |
| 8 | `coreyhaines31/marketingskills` | 48823 | 7495 | JavaScript | 2,141 stars this week | Claude Code和人工智能代理的营销技能。CRO、文案撰写、搜索引擎优化、分析和增长工程。 | https://github.com/coreyhaines31/marketingskills |  |
| 9 | `ChromeDevTools/chrome-devtools-mcp` | 51375 | 3607 | TypeScript | 1,014 stars this week | 适用于编码代理的Chrome开发者工具 | https://github.com/ChromeDevTools/chrome-devtools-mcp |  |
| 10 | `llvm/llvm-project` | 40345 | 18592 | LLVM | 304 stars this week | LLVM项目是模块化和可重用编译器和工具链技术的集合。 | https://github.com/llvm/llvm-project |  |
| 11 | `mksglu/context-mode` | 21398 | 1544 | TypeScript | 935 stars this week | 人工智能编码代理的上下文窗口优化。沙盒工具输出（减少98 ％ ） ，保持会话内存，并通过MCP +钩子在17个平台上强制路由。 | https://github.com/mksglu/context-mode |  |
| 12 | `NousResearch/hermes-agent` | 243457 | 50209 | Python | 4,221 stars this week | 与您一起成长的客服代表 | https://github.com/NousResearch/hermes-agent |  |
| 13 | `heygen-com/hyperframes` | 47766 | 4393 | TypeScript | 3,886 stars this week | 编写HTML。渲染视频。专为客服代表打造。 | https://github.com/heygen-com/hyperframes |  |
| 14 | `facebook/zstd` | 27760 | 2589 | C | 88 stars this week | Zstandard -快速实时压缩算法 | https://github.com/facebook/zstd |  |
| 15 | `openai/skills` | 26518 | 1776 | Python | 1,005 stars this week | Codex技能目录 | https://github.com/openai/skills |  |
| 16 | `nvm-sh/nvm` | 95036 | 10439 | Shell | 257 stars this week | 节点版本管理器-兼容POSIX的bash脚本，用于管理多个活动的node.js版本。$ nvm: 3ArcxqLtXMmBnWbbtfwQgVL3MNnDsggzgGDtXMnjpump | https://github.com/nvm-sh/nvm |  |
| 17 | `bilawalsidhu/gods-eye-view` | 19452 | 3949 | JavaScript | 4,196 stars this week | 浏览器中的间谍卫星模拟器，但数据是真实的。在逼真的3D地球仪上实时开源空间智能。 | https://github.com/bilawalsidhu/gods-eye-view |  |
| 18 | `every-app/open-seo` | 17928 | 2263 | TypeScript | 1,846 stars this week | Semrush和Ahrefs的开源替代品 | https://github.com/every-app/open-seo |  |
| 19 | `ruvnet/ruflo` | 71679 | 8482 | TypeScript | 1,585 stars this week | 🌊 原始Agent元Harness。部署智能多玩家群体，协调自主工作流程，构建对话式人工智能系统。具有自适应记忆、自我学习智能、RAG集成和原生Claude Code/Codex/Hermes等功能集成 | https://github.com/ruvnet/ruflo |  |
| 20 | `google-research/timesfm` | 32016 | 3062 | Python | 3,365 stars this week | TimesFM （时间序列基础模型）是由Google Research开发的用于时间序列预测的预训练时间序列基础模型。 | https://github.com/google-research/timesfm |  |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `cathrynlavery/diagram-design` | 34836 | 2203 | HTML | 30,797 stars this month | Claude Code、Codex和Pi的38种编辑图类型。独立的HTML + SVG。没有阴影，没有美人鱼粪便。 | https://github.com/cathrynlavery/diagram-design |  |
| 2 | `omacom/omarchy` | 39427 | 4273 | Shell | 15,226 stars this month | 漂亮、现代且自以为是的Linux | https://github.com/omacom/omarchy |  |
| 3 | `cursor/plugins` | 7146 | 618 | TypeScript | 4,574 stars this month | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 4 | `tt-a1i/archify` | 54728 | 3587 | JavaScript | 44,220 stars this month | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify |  |
| 5 | `anthropics/claude-plugins-community` | 3634 | 282 | Python | 3,348 stars this month | Claude Cowork和Claude Code的社区插件市场。只读镜像—在clau.de/plugin-directory-submission上提交插件。 | https://github.com/anthropics/claude-plugins-community |  |
| 6 | `semantica-agi/semantica` | 12411 | 1393 | Python | 9,951 stars this month | 上下文和负责任的人工智能系统的图形原生基础设施 | https://github.com/semantica-agi/semantica |  |
| 7 | `AprilNEA/OpenLogi` | 20186 | 625 | Rust | 11,896 stars this month | ⚡️用Rust编写的Logitech Options +的本地本地优先替代方案🦀—在HID + +上重新映射按钮、DPI和SmartShift。无帐户，无遥测。 | https://github.com/AprilNEA/OpenLogi |  |
| 8 | `volcengine/OpenViking` | 36079 | 2751 | Python | 8,115 stars this month | 人工智能代理的自我进化上下文数据库。统一座席记忆、知识抹布和技能。 | https://github.com/volcengine/OpenViking |  |
| 9 | `xai-org/x-algorithm` | 32937 | 5375 | Rust | 6,114 stars this month | 为X上的For You馈送供电的算法 | https://github.com/xai-org/x-algorithm |  |
| 10 | `freestylefly/awesome-gpt-image-2` | 29311 | 2812 | JavaScript | 19,654 stars this month | Prompt as Code · GPT-Image2 工业级提示词引擎与模板库，530+ 个案例逆向工程，20+ 套工业级模板，并提炼出Skills，持续更新中 | https://github.com/freestylefly/awesome-gpt-image-2 |  |
| 11 | `THU-MAIC/OpenMAIC` | 33562 | 5425 | TypeScript | 13,038 stars this month | 开放式多座席互动课堂—只需点击一下，即可获得身临其境的多座席学习体验 | https://github.com/THU-MAIC/OpenMAIC |  |
| 12 | `cactus-compute/needle` | 10598 | 677 | Python | 7,220 stars this month | 14MB基础型号，适用于微型设备；手机、可穿戴设备、智能家居和机器人。 | https://github.com/cactus-compute/needle |  |
| 13 | `vorssaint/vorssaint-utils` | 17186 | 596 | Swift | 12,282 stars this month | 免费开源的macOS菜单栏工具包。 | https://github.com/vorssaint/vorssaint-utils |  |
| 14 | `modular/modular` | 29634 | 3161 | Mojo | 3,036 stars this month | 模块化平台（包括MAX和Mojo ） | https://github.com/modular/modular |  |
| 15 | `akitaonrails/ai-memory` | 6135 | 426 | Rust | 4,716 stars this month | 针对座席编码CLI的长期记忆解决方案，以及促进不同座席供应商之间切换的解决方案 | https://github.com/akitaonrails/ai-memory |  |
| 16 | `debpalash/VoiceStudio` | 21348 | 2642 | Python | 11,516 stars this month | VoiceStudio是开源、完全本地的ElevenLabs替代品--语音克隆、语音设计、视频配音、听写、转录和有声读物创作，支持646种语言。 | https://github.com/debpalash/VoiceStudio |  |
| 17 | `apache/maka` | 5064 | 471 | TypeScript | 3,835 stars this month | Apache Maka （孵化）是一个高性能代理工作区，可完整记录其所做的一切。 | https://github.com/apache/maka |  |
| 18 | `public-apis/public-apis` | 477622 | 52727 | Python | 23,450 stars this month | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 19 | `3b1b/manim` | 93514 | 7683 | Python | 4,394 stars this month | 解释性数学视频的动画引擎 | https://github.com/3b1b/manim |  |
| 20 | `Lakr233/vphone-cli` | 11285 | 1433 | Swift | 3,705 stars this month | — | https://github.com/Lakr233/vphone-cli |  |
| 21 | `megadose/holehe` | 14782 | 1881 | Python | 2,856 stars this month | holehe允许您检查邮件是否在Twitter、Instagram等不同网站上使用，并将检索具有忘记密码功能的网站上的信息。 | https://github.com/megadose/holehe |  |
| 22 | `MiaAI-Lab/DeepSeek-v4-Flash-DSpark-2x-DGX-Spark` | 1291 | 179 | Python | 812 stars this month | DeepSeek-v4-Flash 0731 2x DGX Sparks配方 | https://github.com/MiaAI-Lab/DeepSeek-v4-Flash-DSpark-2x-DGX-Spark |  |
| 23 | `unslothai/unsloth` | 75873 | 6900 | Python | 6,357 stars this month | 运行和训练LLM和扩散模型的本地UI。支持GGUF、MLX、Qwen3.8、DeepSeek-V4、MiniMax-H3、Gemma 4、FLUX等。 | https://github.com/unslothai/unsloth |  |


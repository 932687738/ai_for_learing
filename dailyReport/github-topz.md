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

**最近一次更新时间**（Asia/Shanghai）： 2026-09-02 09:59:01

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 544621 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 502065 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 474276 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 454850 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 395766 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 388528 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `donnemartin/system-design-primer` | 367516 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 8 | `nilbuild/developer-roadmap` | 366092 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 9 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 10 | `jwasham/coding-interview-university` | 360197 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 11 | `vinta/awesome-python` | 317845 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `Gitlawb/openclaude` | 31348 | 8951 | TypeScript | 80 stars today | 在任何地方运行。使用任何东西 | https://github.com/Gitlawb/openclaude | 新增 |
| 2 | `Imbad0202/academic-research-skills` | 44936 | 3551 | Python | 193 stars today | Claude Code的学术研究技能：研究→撰写→评审→修订→最终确定 | https://github.com/Imbad0202/academic-research-skills | 新增 |
| 3 | `THU-MAIC/OpenMAIC` | 29567 | 4979 | TypeScript | 3,128 stars today | 开放式多座席互动课堂—只需点击一下，即可获得身临其境的多座席学习体验 | https://github.com/THU-MAIC/OpenMAIC |  |
| 4 | `iv-org/invidious` | 23779 | 2674 | Crystal | 577 stars today | Invidious是YouTube的替代前端 | https://github.com/iv-org/invidious | 新增 |
| 5 | `jingyaogong/minimind` | 57133 | 7429 | Python | 1,005 stars today | 在短短2小时内从头开始🧠培训64M参数LLM ！ | https://github.com/jingyaogong/minimind | 新增 |
| 6 | `3b1b/manim` | 92583 | 7619 | Python | 86 stars today | 解释性数学视频的动画引擎 | https://github.com/3b1b/manim | 新增 |
| 7 | `firecrawl/pdf-inspector` | 17963 | 1223 | Rust | 541 stars today | 用于PDF检查、分类和文本提取的快速Rust库。智能检测扫描的PDF和基于文本的PDF ，以实现智能路由决策。 | https://github.com/firecrawl/pdf-inspector | 新增 |
| 8 | `browser-use/video-use` | 22986 | 2816 | Python | 472 stars today | 使用编码代理编辑视频 | https://github.com/browser-use/video-use | 新增 |
| 9 | `K-Dense-AI/scientific-agent-skills` | 41571 | 3828 | Python | 912 stars today | 将任何AI特工变成AI科学家。首屈一指的科学代理技能库，全球超过19万名科学家使用。165项随时可用的经验证的技能，以及100多个涵盖生物学、化学、医学和药物发现的科学数据库。兼容Cursor、Claude Code…… | https://github.com/K-Dense-AI/scientific-agent-skills |  |
| 10 | `handsomestWei/patent-disclosure-skill` | 6750 | 761 | Python | 501 stars today | 中国专利.skill：专利点挖掘与交底书（发明/实用/外观）编写，通俗解读专利，嗅探政策动向，辅助审查答复。 | https://github.com/handsomestWei/patent-disclosure-skill |  |
| 11 | `VoltAgent/awesome-design-md` | 112827 | 12775 | — | 323 stars today | 由流行品牌设计系统进行的DESIGN.md文件分析的集合。将一个放入您的项目中，让编码代理生成匹配的UI。 | https://github.com/VoltAgent/awesome-design-md | 新增 |
| 12 | `averygan/reclip` | 7696 | 1318 | HTML | 56 stars today | 从几乎所有网站下载视频。轻量级的自托管媒体下载器，具有干净的Web UI。 | https://github.com/averygan/reclip | 新增 |
| 13 | `affaan-m/ECC` | 245783 | 37089 | JavaScript | 623 stars today | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC | 新增 |
| 14 | `unclecode/crawl4ai` | 80875 | 8358 | Python | 145 stars today | 🚀🤖 Crawl4AI ：开源LLM友好的网络爬虫和爬虫。不要害羞，在这里加入： https://discord.gg/jP8KfhDhyN | https://github.com/unclecode/crawl4ai |  |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `tt-a1i/archify` | 42031 | 2675 | JavaScript | 25,469 stars this week | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify |  |
| 2 | `anthropics/claude-plugins-community` | 3175 | 248 | Python | 1,634 stars this week | Claude Cowork和Claude Code的社区插件市场。只读镜像—在clau.de/plugin-directory-submission上提交插件。 | https://github.com/anthropics/claude-plugins-community |  |
| 3 | `cursor/plugins` | 6536 | 536 | TypeScript | 1,377 stars this week | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 4 | `THU-MAIC/OpenMAIC` | 29567 | 4979 | TypeScript | 8,014 stars this week | 开放式多座席互动课堂—只需点击一下，即可获得身临其境的多座席学习体验 | https://github.com/THU-MAIC/OpenMAIC |  |
| 5 | `freestylefly/awesome-gpt-image-2` | 26987 | 2621 | JavaScript | 10,669 stars this week | Prompt as Code · GPT-Image2 工业级提示词引擎与模板库，530+ 个案例逆向工程，20+ 套工业级模板，并提炼出Skills，持续更新中 | https://github.com/freestylefly/awesome-gpt-image-2 |  |
| 6 | `omacom/omarchy` | 36858 | 3837 | Shell | 6,006 stars this week | 漂亮、现代且自以为是的Linux | https://github.com/omacom/omarchy |  |
| 7 | `tashfeenahmed/freellmapi` | 23612 | 3230 | TypeScript | 3,452 stars this week | 每月74亿个代币。34个免费LLM提供商。635个免费模型端点。全部在一个/v1端点后面，加上任何与OpenAI兼容的自定义端点。智能路由、自动故障转移、加密密钥。仅限个人实验。 | https://github.com/tashfeenahmed/freellmapi |  |
| 8 | `K-Dense-AI/scientific-agent-skills` | 41571 | 3828 | Python | 6,962 stars this week | 将任何AI特工变成AI科学家。首屈一指的科学代理技能库，全球超过19万名科学家使用。165项随时可用的经验证的技能，以及100多个涵盖生物学、化学、医学和药物发现的科学数据库。兼容Cursor、Claude Code…… | https://github.com/K-Dense-AI/scientific-agent-skills |  |
| 9 | `rohitg00/ai-engineering-from-scratch` | 51846 | 8979 | Python | 3,427 stars this week | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 10 | `every-app/open-seo` | 16151 | 1962 | TypeScript | 2,625 stars this week | Semrush和Ahrefs的开源替代品 | https://github.com/every-app/open-seo | 新增 |
| 11 | `p-e-w/heretic` | 30021 | 3300 | Python | 1,874 stars this week | 语言模型的全自动审查删除 | https://github.com/p-e-w/heretic | 新增 |
| 12 | `abi/screenshot-to-code` | 77008 | 9385 | Python | 2,485 stars this week | 放入屏幕截图并将其转换为干净的代码（ HTML/Tailwind/React/Vue ） | https://github.com/abi/screenshot-to-code |  |
| 13 | `OpenCut-app/OpenCut` | 88356 | 8715 | TypeScript | 2,630 stars this week | 开源CapCut替代方案 | https://github.com/OpenCut-app/OpenCut | 新增 |
| 14 | `MadsLorentzen/ai-job-search` | 39858 | 13515 | Python | 4,841 stars this week | 在您的机器上运行的作业搜索。基于Claude Code构建的人工智能求职框架：评估帖子、定制简历、撰写求职信、准备面试。分叉并拥有它。 | https://github.com/MadsLorentzen/ai-job-search |  |
| 15 | `AprilNEA/OpenLogi` | 18400 | 548 | Rust | 2,089 stars this week | ⚡️用Rust编写的Logitech Options +的本地本地优先替代方案🦀—在HID + +上重新映射按钮、DPI和SmartShift。无帐户，无遥测。 | https://github.com/AprilNEA/OpenLogi |  |
| 16 | `ConardLi/garden-skills` | 12019 | 1470 | CSS | 1,340 stars this week | ConardLi的开源Skills系列，包括网页设计、知识检索、图像生成等。 | https://github.com/ConardLi/garden-skills |  |
| 17 | `google/googletest` | 39436 | 10885 | C++ | 492 stars this week | GoogleTest - Google测试和模拟框架 | https://github.com/google/googletest |  |
| 18 | `punkpeye/awesome-mcp-servers` | 93723 | 15434 | — | 919 stars this week | MCP服务器的集合。 | https://github.com/punkpeye/awesome-mcp-servers | 新增 |
| 19 | `apache/maka` | 4448 | 413 | TypeScript | 1,285 stars this week | Apache Maka （孵化）是本地首个AI代理工作区。模型消息、工具调用、工具结果、权限决策和终止事件被记录为仅追加日志。 | https://github.com/apache/maka |  |
| 20 | `thedotmack/claude-mem` | 92920 | 8171 | JavaScript | 1,164 stars this week | 每个座席跨会话的持久上下文–捕获座席在会话期间执行的所有操作，使用AI对其进行压缩，并将相关上下文注入到未来的会话中。适用于Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode等 | https://github.com/thedotmack/claude-mem | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `omacom/omarchy` | 36858 | 3837 | Shell | 12,675 stars this month | 漂亮、现代且自以为是的Linux | https://github.com/omacom/omarchy |  |
| 2 | `cursor/plugins` | 6536 | 536 | TypeScript | 4,020 stars this month | 光标插件规范和官方插件 | https://github.com/cursor/plugins | 新增 |
| 3 | `anthropics/claude-plugins-community` | 3175 | 248 | Python | 2,866 stars this month | Claude Cowork和Claude Code的社区插件市场。只读镜像—在clau.de/plugin-directory-submission上提交插件。 | https://github.com/anthropics/claude-plugins-community |  |
| 4 | `tt-a1i/archify` | 42031 | 2675 | JavaScript | 33,153 stars this month | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify |  |
| 5 | `AprilNEA/OpenLogi` | 18400 | 548 | Rust | 10,446 stars this month | ⚡️用Rust编写的Logitech Options +的本地本地优先替代方案🦀—在HID + +上重新映射按钮、DPI和SmartShift。无帐户，无遥测。 | https://github.com/AprilNEA/OpenLogi |  |
| 6 | `volcengine/OpenViking` | 34963 | 2674 | Python | 7,321 stars this month | 人工智能代理的自我进化上下文数据库。统一座席记忆、知识抹布和技能。 | https://github.com/volcengine/OpenViking |  |
| 7 | `TencentCloud/TencentDB-Agent-Memory` | 25588 | 2387 | TypeScript | 15,686 stars this month | TencentDB Agent Memory是AI Agent的团队级内存中心—将对话、文档和代码转换为四个可重用的内存资产（ Chat Memory、Skill、LLM-Wiki、Code-Graph ） ，这些资产在代理和框架之间进行管理、共享和配备。 | https://github.com/TencentCloud/TencentDB-Agent-Memory |  |
| 8 | `huangruiteng/loopx` | 5396 | 481 | Python | 5,248 stars this month | 跨Codex、Claude Code和其他线束的耐用、受管控工作的长期代理控制平面。 | https://github.com/huangruiteng/loopx | 新增 |
| 9 | `freestylefly/awesome-gpt-image-2` | 26987 | 2621 | JavaScript | 18,278 stars this month | Prompt as Code · GPT-Image2 工业级提示词引擎与模板库，530+ 个案例逆向工程，20+ 套工业级模板，并提炼出Skills，持续更新中 | https://github.com/freestylefly/awesome-gpt-image-2 |  |
| 10 | `ayghri/i-have-adhd` | 26411 | 1659 | Python | 11,429 stars this month | 阻止您的编码代理埋葬答案的技能。ADHD友好的输出。 | https://github.com/ayghri/i-have-adhd |  |
| 11 | `firecrawl/pdf-inspector` | 17963 | 1223 | Rust | 15,440 stars this month | 用于PDF检查、分类和文本提取的快速Rust库。智能检测扫描的PDF和基于文本的PDF ，以实现智能路由决策。 | https://github.com/firecrawl/pdf-inspector |  |
| 12 | `apache/maka` | 4448 | 413 | TypeScript | 3,448 stars this month | Apache Maka （孵化）是本地首个AI代理工作区。模型消息、工具调用、工具结果、权限决策和终止事件被记录为仅追加日志。 | https://github.com/apache/maka |  |
| 13 | `cactus-compute/needle` | 9994 | 649 | Python | 6,669 stars this month | 14MB基础型号，适用于微型设备；手机、可穿戴设备、智能家居和机器人。 | https://github.com/cactus-compute/needle |  |
| 14 | `zhaoxuya520/reverse-skill` | 33785 | 4576 | PowerShell | 22,512 stars this month | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-demand toolchain bootstrapping + Self-evolving knowledge base Supports Claude Code, Kiro, Cursor, Cline, and other AI coding clients 逆向/渗透/安全技能路由包 - AI 自动路由 + 按需自举工… | https://github.com/zhaoxuya520/reverse-skill |  |
| 15 | `donnemartin/system-design-primer` | 367516 | 58178 | Python | 7,979 stars this month | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer | 新增 |
| 16 | `unclebob/swarm-forge` | 3526 | 348 | Clojure | 2,062 stars this month | 用于协调多个AI代理的简单工具。 | https://github.com/unclebob/swarm-forge |  |
| 17 | `modular/modular` | 29436 | 3131 | Mojo | 2,891 stars this month | 模块化平台（包括MAX和Mojo ） | https://github.com/modular/modular |  |
| 18 | `pingdotgg/t3code` | 21371 | 5161 | TypeScript | 5,323 stars this month | — | https://github.com/pingdotgg/t3code |  |
| 19 | `google/skills` | 19155 | 1544 | Python | 3,797 stars this month | Google产品和技术的代理技能 | https://github.com/google/skills | 新增 |
| 20 | `youssofal/MTPLX` | 1894 | 143 | Python | 766 stars this month | 在MLX上速度提高3倍· Qwen 3.8 27B ·在Apple Silicon上进行原生MTP投机解码，无需外部绘图员。 | https://github.com/youssofal/MTPLX | 新增 |
| 21 | `3b1b/manim` | 92583 | 7619 | Python | 3,476 stars this month | 解释性数学视频的动画引擎 | https://github.com/3b1b/manim | 新增 |
| 22 | `THU-MAIC/OpenMAIC` | 29568 | 4979 | TypeScript | 8,755 stars this month | 开放式多座席互动课堂—只需点击一下，即可获得身临其境的多座席学习体验 | https://github.com/THU-MAIC/OpenMAIC | 新增 |


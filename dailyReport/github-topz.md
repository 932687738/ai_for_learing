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

**最近一次更新时间**（Asia/Shanghai）： 2026-09-04 10:22:24

| 序号 | 仓库 | Stars | 仓库简介（中文） | 链接 | 标记 |
| --- | --- | ---:| --- | --- | --- |
| 1 | `codecrafters-io/build-your-own-x` | 545047 | 通过从零重写各类代表性技术来学习编程与设计，加深对底层原理的理解。 | https://github.com/codecrafters-io/build-your-own-x |  |
| 2 | `sindresorhus/awesome` | 502742 | 围绕多种主题整理的「Awesome」精品清单合集。 | https://github.com/sindresorhus/awesome |  |
| 3 | `public-apis/public-apis` | 474987 | 免费可用的公共 API 资源汇总清单。 | https://github.com/public-apis/public-apis |  |
| 4 | `freeCodeCamp/freeCodeCamp` | 454977 | freeCodeCamp 官网开源代码与学习课程：可免费学习编程、数学与计算机科学。 | https://github.com/freeCodeCamp/freeCodeCamp |  |
| 5 | `EbookFoundation/free-programming-books` | 395914 | 可免费获取的编程与计算机类书籍书单汇总。 | https://github.com/EbookFoundation/free-programming-books |  |
| 6 | `openclaw/openclaw` | 388793 | 可在多系统运行的个人 AI 助手（吉祥物为龙虾图标）。 | https://github.com/openclaw/openclaw |  |
| 7 | `donnemartin/system-design-primer` | 367760 | 大厂级系统设计学习与面试备战材料（含 Anki 卡片范例）。 | https://github.com/donnemartin/system-design-primer |  |
| 8 | `nilbuild/developer-roadmap` | 366251 | 交互式开发者路线图、入门与进阶教程等学习资料合集。 | https://github.com/nilbuild/developer-roadmap |  |
| 9 | `re4/LibreCode` | 361048 | LibreCode -类似编码/反转接口的Ollama光标 | https://github.com/re4/LibreCode |  |
| 10 | `jwasham/coding-interview-university` | 360309 | 面向软件工程师岗位的系统化计算机科学与面试自学路线图。 | https://github.com/jwasham/coding-interview-university |  |
| 11 | `vinta/awesome-python` | 318081 | 带选型倾向的 Python 框架、扩展库、工具与学习资源合集。 | https://github.com/vinta/awesome-python |  |
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
| 1 | `fmtlib/fmt` | 25126 | 3017 | C++ | 963 stars today | 现代格式化库 | https://github.com/fmtlib/fmt | 新增 |
| 2 | `mattpocock/skills` | 247561 | 20990 | Shell | 1,601 stars today | 真正工程师的技能。直接来自我的.agents目录。 | https://github.com/mattpocock/skills | 新增 |
| 3 | `NousResearch/hermes-agent` | 240888 | 49362 | Python | 774 stars today | 与您一起成长的客服代表 | https://github.com/NousResearch/hermes-agent | 新增 |
| 4 | `DietrichGebert/ponytail` | 123549 | 6675 | JavaScript | 2,128 stars today | 让你的人工智能代理像房间里最懒惰的高级开发人员一样思考。最好的代码是你从未写过的代码。 | https://github.com/DietrichGebert/ponytail | 新增 |
| 5 | `anthropics/skills` | 173693 | 20608 | Python | 281 stars today | 座席技能的公共存储库 | https://github.com/anthropics/skills | 新增 |
| 6 | `affaan-m/ECC` | 247261 | 37259 | JavaScript | 751 stars today | 座席线束性能优化系统。Claude Code、Codex、Opencode、Cursor等的技能、本能、记忆、安全和研究优先开发。 | https://github.com/affaan-m/ECC |  |
| 7 | `JuliusBrussee/caveman` | 103138 | 5995 | Go | 543 stars today | 🪨 为什么在很少令牌欺骗时使用许多令牌— Claude Code技能通过像穴居人一样说话来削减65 ％的令牌 | https://github.com/JuliusBrussee/caveman | 新增 |
| 8 | `blader/humanizer` | 41571 | 3555 | Python | 1,208 stars today | 从文本中删除人工智能生成文字的迹象的代理技能 | https://github.com/blader/humanizer | 新增 |
| 9 | `google-research/timesfm` | 30725 | 2934 | Python | 1,618 stars today | TimesFM （时间序列基础模型）是由Google Research开发的用于时间序列预测的预训练时间序列基础模型。 | https://github.com/google-research/timesfm | 新增 |
| 10 | `averygan/reclip` | 8418 | 1366 | HTML | 88 stars today | 从几乎所有网站下载视频。轻量级的自托管媒体下载器，具有干净的Web UI。 | https://github.com/averygan/reclip |  |
| 11 | `bannedbook/fanqiang` | 52246 | 8481 | Kotlin | 522 stars today | 翻墙-科学上网 | https://github.com/bannedbook/fanqiang | 新增 |
| 12 | `addyosmani/agent-skills` | 92049 | 9812 | JavaScript | 264 stars today | AI编码代理的生产级工程技能。 | https://github.com/addyosmani/agent-skills | 新增 |
| 13 | `ByteByteGoHq/system-design-101` | 88380 | 9823 | — | 171 stars today | 使用视觉效果和简单术语解释复杂系统。帮助您准备系统设计面试。 | https://github.com/ByteByteGoHq/system-design-101 | 新增 |
| 14 | `magnitudedev/magnitude` | 1978 | 143 | TypeScript | 161 stars today | 开源推理服务器，为您的硬件运行最佳本地模型，插入到您已经使用的代理中。适用于Pi、OpenCode、Hermes、OpenClaw、Codex、Claude Code、Oh My Pi和Cline。 | https://github.com/magnitudedev/magnitude | 新增 |
| 15 | `Imbad0202/academic-research-skills` | 46010 | 3605 | Python | 496 stars today | Claude Code的学术研究技能：研究→撰写→评审→修订→最终确定 | https://github.com/Imbad0202/academic-research-skills |  |
| 16 | `Gitlawb/openclaude` | 32364 | 9019 | TypeScript | 451 stars today | 在任何地方运行。使用任何东西 | https://github.com/Gitlawb/openclaude |  |
| 17 | `debpalash/VoiceStudio` | 16356 | 2216 | Python | 1,672 stars today | VoiceStudio是开源、完全本地的ElevenLabs替代品--语音克隆、语音设计、视频配音、听写、转录和有声读物创作，支持646种语言。 | https://github.com/debpalash/VoiceStudio | 新增 |
| 18 | `f/prompts.chat` | 169034 | 21766 | HTML | 168 stars today | f.k.a. Awesome ChatGPT提示。分享、发现和收集社区提示。免费开源--为您的组织提供完全隐私的自助出租服务。 | https://github.com/f/prompts.chat | 新增 |
| 19 | `obra/superpowers` | 281370 | 25207 | Shell | 462 stars today | 有效的代理技能框架和软件开发方法。 | https://github.com/obra/superpowers | 新增 |


### 本周 trending（since=weekly）

**页面**： `https://github.com/trending?since=weekly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `tt-a1i/archify` | 45994 | 2951 | JavaScript | 24,227 stars this week | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify |  |
| 2 | `bilawalsidhu/gods-eye-view` | 16981 | 3411 | JavaScript | 10,485 stars this week | 浏览器中的间谍卫星模拟器，但数据是真实的。在逼真的3D地球仪上实时开源空间智能。 | https://github.com/bilawalsidhu/gods-eye-view | 新增 |
| 3 | `THU-MAIC/OpenMAIC` | 31092 | 5140 | TypeScript | 10,023 stars this week | 开放式多座席互动课堂—只需点击一下，即可获得身临其境的多座席学习体验 | https://github.com/THU-MAIC/OpenMAIC |  |
| 4 | `JetBrains/go-modern-guidelines` | 3116 | 87 | Go | 1,213 stars this week | 帮助AI编码代理编写现代Go | https://github.com/JetBrains/go-modern-guidelines | 新增 |
| 5 | `Gitlawb/openclaude` | 32364 | 9019 | TypeScript | 1,389 stars this week | 在任何地方运行。使用任何东西 | https://github.com/Gitlawb/openclaude | 新增 |
| 6 | `K-Dense-AI/scientific-agent-skills` | 42402 | 3885 | Python | 7,370 stars this week | 将任何AI特工变成AI科学家。首屈一指的科学代理技能库，全球超过19万名科学家使用。165项随时可用的经验证的技能，以及100多个涵盖生物学、化学、医学和药物发现的科学数据库。兼容Cursor、Claude Code…… | https://github.com/K-Dense-AI/scientific-agent-skills |  |
| 7 | `jingyaogong/minimind` | 58265 | 7571 | Python | 3,122 stars this week | 在短短2小时内从头开始🧠培训64M参数LLM ！ | https://github.com/jingyaogong/minimind | 新增 |
| 8 | `every-app/open-seo` | 16670 | 2059 | TypeScript | 2,941 stars this week | Semrush和Ahrefs的开源替代品 | https://github.com/every-app/open-seo |  |
| 9 | `omacom/omarchy` | 37741 | 3975 | Shell | 5,296 stars this week | 漂亮、现代且自以为是的Linux | https://github.com/omacom/omarchy |  |
| 10 | `google-research/timesfm` | 30725 | 2934 | Python | 2,324 stars this week | TimesFM （时间序列基础模型）是由Google Research开发的用于时间序列预测的预训练时间序列基础模型。 | https://github.com/google-research/timesfm | 新增 |
| 11 | `p-e-w/heretic` | 30326 | 3355 | Python | 2,146 stars this week | 语言模型的全自动审查删除 | https://github.com/p-e-w/heretic |  |
| 12 | `freestylefly/awesome-gpt-image-2` | 27771 | 2683 | JavaScript | 5,425 stars this week | Prompt as Code · GPT-Image2 工业级提示词引擎与模板库，530+ 个案例逆向工程，20+ 套工业级模板，并提炼出Skills，持续更新中 | https://github.com/freestylefly/awesome-gpt-image-2 |  |
| 13 | `cursor/plugins` | 6787 | 558 | TypeScript | 1,159 stars this week | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 14 | `abi/screenshot-to-code` | 77446 | 9433 | Python | 2,412 stars this week | 放入屏幕截图并将其转换为干净的代码（ HTML/Tailwind/React/Vue ） | https://github.com/abi/screenshot-to-code |  |
| 15 | `colinhacks/zod` | 43818 | 2174 | TypeScript | 277 stars this week | 使用静态类型推断的TypeScript优先架构验证 | https://github.com/colinhacks/zod | 新增 |
| 16 | `zedeus/nitter` | 14096 | 1295 | Nim | 467 stars this week | 替代Twitter前端 | https://github.com/zedeus/nitter | 新增 |
| 17 | `tashfeenahmed/freellmapi` | 24126 | 3285 | TypeScript | 3,194 stars this week | 每月74亿个代币。34个免费LLM提供商。635个免费模型端点。全部在一个/v1端点后面，加上任何与OpenAI兼容的自定义端点。智能路由、自动故障转移、加密密钥。仅限个人实验。 | https://github.com/tashfeenahmed/freellmapi |  |
| 18 | `debpalash/VoiceStudio` | 16357 | 2216 | Python | 3,902 stars this week | VoiceStudio是开源、完全本地的ElevenLabs替代品--语音克隆、语音设计、视频配音、听写、转录和有声读物创作，支持646种语言。 | https://github.com/debpalash/VoiceStudio | 新增 |
| 19 | `punkpeye/awesome-mcp-servers` | 94019 | 15586 | — | 1,130 stars this week | MCP服务器的集合。 | https://github.com/punkpeye/awesome-mcp-servers |  |
| 20 | `handsomestWei/patent-disclosure-skill` | 7214 | 796 | Python | 1,846 stars this week | 中国专利.skill：专利点挖掘与交底书（发明/实用/外观）编写，通俗解读专利，嗅探政策动向，辅助审查答复。 | https://github.com/handsomestWei/patent-disclosure-skill | 新增 |
| 21 | `rohitg00/ai-engineering-from-scratch` | 52299 | 9056 | Python | 2,525 stars this week | 学习它，构建它。为其他人运送。 | https://github.com/rohitg00/ai-engineering-from-scratch |  |
| 22 | `majd/ipatool` | 10804 | 908 | Go | 847 stars this week | 命令行工具，允许从App Store搜索和下载iOS、iPadOS、tvOS和visionOS的应用程序包（称为ipa文件）。 | https://github.com/majd/ipatool | 新增 |
| 23 | `fmtlib/fmt` | 25126 | 3017 | C++ | 993 stars this week | 现代格式化库 | https://github.com/fmtlib/fmt | 新增 |


### 本月 trending（since=monthly）

**页面**： `https://github.com/trending?since=monthly`

| # | 仓库 | Stars | Forks | 语言 | 周期动向 | 仓库简介（中文） | 链接 | 标记 |
| ---: | --- | ---:| ---:| --- | --- | --- | --- | --- |
| 1 | `omacom/omarchy` | 37741 | 3975 | Shell | 13,597 stars this month | 漂亮、现代且自以为是的Linux | https://github.com/omacom/omarchy |  |
| 2 | `semantica-agi/semantica` | 11875 | 1337 | Python | 10,058 stars this month | 上下文和负责任的人工智能系统的图形原生基础设施 | https://github.com/semantica-agi/semantica | 新增 |
| 3 | `cursor/plugins` | 6787 | 558 | TypeScript | 4,258 stars this month | 光标插件规范和官方插件 | https://github.com/cursor/plugins |  |
| 4 | `cloudflare/cloudflare-os` | 9577 | 1124 | TypeScript | 9,562 stars this month | 基于Cloudflare Workers构建的代理工作区，用于创建文档、构建应用以及根据贵公司的上下文和系统运行代理。 | https://github.com/cloudflare/cloudflare-os | 新增 |
| 5 | `tt-a1i/archify` | 46000 | 2951 | JavaScript | 36,689 stars this month | 美观、可验证的架构、工作流程、序列、数据流和生命周期图的代理技能--具有运动和清晰导出的自包含HTML。 | https://github.com/tt-a1i/archify |  |
| 6 | `anthropics/claude-plugins-community` | 3357 | 257 | Python | 3,067 stars this month | Claude Cowork和Claude Code的社区插件市场。只读镜像—在clau.de/plugin-directory-submission上提交插件。 | https://github.com/anthropics/claude-plugins-community |  |
| 7 | `AprilNEA/OpenLogi` | 18905 | 571 | Rust | 10,662 stars this month | ⚡️用Rust编写的Logitech Options +的本地本地优先替代方案🦀—在HID + +上重新映射按钮、DPI和SmartShift。无帐户，无遥测。 | https://github.com/AprilNEA/OpenLogi |  |
| 8 | `volcengine/OpenViking` | 35373 | 2708 | Python | 7,659 stars this month | 人工智能代理的自我进化上下文数据库。统一座席记忆、知识抹布和技能。 | https://github.com/volcengine/OpenViking |  |
| 9 | `freestylefly/awesome-gpt-image-2` | 27771 | 2683 | JavaScript | 19,065 stars this month | Prompt as Code · GPT-Image2 工业级提示词引擎与模板库，530+ 个案例逆向工程，20+ 套工业级模板，并提炼出Skills，持续更新中 | https://github.com/freestylefly/awesome-gpt-image-2 |  |
| 10 | `vitali87/code-graph-rag` | 4944 | 653 | Python | 2,456 stars this month | 您的monorepo的终极抹布。利用人工智能和知识图谱的力量查询、理解和编辑多语言代码库 | https://github.com/vitali87/code-graph-rag | 新增 |
| 11 | `xai-org/x-algorithm` | 32589 | 5357 | Rust | 5,828 stars this month | 为X上的For You馈送供电的算法 | https://github.com/xai-org/x-algorithm | 新增 |
| 12 | `THU-MAIC/OpenMAIC` | 31092 | 5140 | TypeScript | 10,599 stars this month | 开放式多座席互动课堂—只需点击一下，即可获得身临其境的多座席学习体验 | https://github.com/THU-MAIC/OpenMAIC |  |
| 13 | `cactus-compute/needle` | 10192 | 655 | Python | 6,855 stars this month | 14MB基础型号，适用于微型设备；手机、可穿戴设备、智能家居和机器人。 | https://github.com/cactus-compute/needle |  |
| 14 | `apache/maka` | 4655 | 438 | TypeScript | 3,545 stars this month | Apache Maka （孵化）是本地首个AI代理工作区。模型消息、工具调用、工具结果、权限决策和终止事件被记录为仅追加日志。 | https://github.com/apache/maka |  |
| 15 | `TencentCloud/TencentDB-Agent-Memory` | 25856 | 2413 | TypeScript | 14,291 stars this month | TencentDB Agent Memory是AI Agent的团队级内存中心—将对话、文档和代码转换为四个可重用的内存资产（ Chat Memory、Skill、LLM-Wiki、Code-Graph ） ，这些资产在代理和框架之间进行管理、共享和配备。 | https://github.com/TencentCloud/TencentDB-Agent-Memory |  |
| 16 | `youssofal/MTPLX` | 2011 | 148 | Python | 870 stars this month | 在MLX上速度提高3倍· Qwen 3.8 27B ·在Apple Silicon上进行原生MTP投机解码，无需外部绘图员。 | https://github.com/youssofal/MTPLX |  |
| 17 | `cloudflare/computer` | 8983 | 502 | TypeScript | 8,938 stars this month | 为您的代理提供一台电脑 👾 | https://github.com/cloudflare/computer | 新增 |
| 18 | `google/skills` | 19407 | 1560 | Python | 4,004 stars this month | Google产品和技术的代理技能 | https://github.com/google/skills |  |
| 19 | `modular/modular` | 29521 | 3144 | Mojo | 2,953 stars this month | 模块化平台（包括MAX和Mojo ） | https://github.com/modular/modular |  |
| 20 | `huangruiteng/loopx` | 5565 | 496 | Python | 4,713 stars this month | 跨Codex、Claude Code和其他线束的耐用、受管控工作的长期代理控制平面。 | https://github.com/huangruiteng/loopx |  |


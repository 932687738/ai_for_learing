# Juejin Hot Digest

按 Asia/Shanghai 时区汇总掘金文章热榜与收藏热榜（后端 / 前端 / 人工智能 / 开发工具），按文章链接去重并归纳正文。

## 2026-09-11

### 今日总览

**一句话结论**：`2026-09-11` 新 URL 主线是 **DeepSeek V4.1 Flash 正式版与降价 + GPT-Live/Astra 舆论延续**，工程向关注 **Coding Agent 为何多选 TS/Node、Codex Hook 审计长任务、LangGraph 反谣言 Agent**。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 文章热榜 + 收藏热榜 × 后端/前端/人工智能/开发工具 |
| 榜单规模 | 每槽最多 15 条；列表总条数 120；去重后新 URL **20**；跳过已见 **100**；详情成功 20 / 失败 0 |
| 核心趋势 | 1）AI 槽继续消化 DeepSeek Flash 自换代与 9/10 调价；2）开发工具槽出现 Tabbit CLI 浏览器发文与 Codex Hook 复盘；3）后端/redis search、FastAPI 等基础文占榜 |
| 可直接关注 | [DeepSeek V4.1 Flash 发布解读](https://juejin.cn/post/7683722642071470130)；[Coding Agent 为何多用 Node](https://juejin.cn/post/7683481485497188403)；[Codex Hook](https://juejin.cn/post/7683493984028459035)；[LangGraph 反谣言 Agent](https://juejin.cn/post/7653442979387506726) |

### 后端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 8 | [为什么不推荐走Agent开发？](https://juejin.cn/post/7683457864929329204) | 程序员飞鱼 | 赞29/藏0/阅320 | 飞鱼从社招视角泼冷水：Agent 岗位需要业务增量，培训班鼓吹「人人 LangChain/LangGraph 搭 Agent」多是焦虑营销。建议做有垂直场景的 Agent，而不是为了面试堆框架 Demo。 | https://juejin.cn/post/7683457864929329204 |
| 9 | [为啥 Blender 突然火了？](https://juejin.cn/post/7683515498140221478) | cxuanAI | 赞11/藏9/阅558 | cxuanAI 科普 Blender：Astra 发布后「Astra+Blender 3D」出圈。Blender 是免费开源 3D 全流程工具；Astra 可代劳建模/材质/灯光/渲染，降低 3D 创作门槛，但工程细节仍要人审。 | https://juejin.cn/post/7683515498140221478 |
| 11 | [推荐一个比ES快5倍的搜索引擎](https://juejin.cn/post/7683722642070896690) | 苏三说技术 | 赞10/藏6/阅238 | 苏三介绍 Redis Search 作 ES 轻量替代：宣称同硬件 QPS 约为 ES 3–5 倍、P99 约 5ms。适合中小规模全文检索；复杂聚合/超大规模仍要评估 ES/OpenSearch。 | https://juejin.cn/post/7683722642070896690 |
| 12 | [ChatGPT Plus、Pro 5x、Pro 20x 到底有多少额度？聊聊 Codex 那个让人看不懂的“周限额”](https://juejin.cn/post/7681223706186596387) | 掘金者阿豪 | 赞0/藏1/阅381 | 掘金者阿豪拆解 ChatGPT Plus/Pro 5x/20x 与 Codex `/status` 的 5 小时/Weekly limit：社区用「美元额度」估算用量，但官方口径并不透明。重度 Codex 用户应盯 status 而不是只看套餐名。 | https://juejin.cn/post/7681223706186596387 |
| 14 | [Java 图片处理还在用 ImageIO？这个库让你代码从 30 行变 3 行](https://juejin.cn/post/7681245344118063131) | SimonKing | 赞4/藏6/阅264 | SimonKing 系统介绍 Thumbnailator：用链式 API 做裁剪/缩放/水印/压缩，替代 ImageIO 几十行样板代码。适合头像、商品缩略图等 Java 高频图像处理。 | https://juejin.cn/post/7681245344118063131 |
| 15 | [学习 FastAPI 的 Day 1：看懂接口与请求流程](https://juejin.cn/post/7682323883429232691) | Dragon_xjy | 赞3/藏3/阅190 | Dragon_xjy FastAPI Day1：自动 Swagger/Redoc、Pydantic 校验、依赖注入与中间件执行顺序。偏入门教程，适合 Python 后端转 API 开发。 | https://juejin.cn/post/7682323883429232691 |

#### 收藏热榜

本槽无新增。

### 前端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 14 | [为什么市面上的 coding agent 大多数都基于Nodejs？](https://juejin.cn/post/7683481485497188403) | Moment | 赞13/藏10/阅770 | Moment 观察 Coding Agent 多选 TypeScript/Node（Kimi CLI、DeepSeek Harness、Gemini/Qwen CLI）；Claude Code/OpenCode 走 TS+Bun。论点：CLI 生态、Ink/Solid TUI、npm 分发速度推动 TS 占主导，不是语言本身更强。 | https://juejin.cn/post/7683481485497188403 |
| 15 | [为什么技术极强的前端，往往当不好前端 Team Leader？](https://juejin.cn/post/7683013257235283987) | ErpanOmer | 赞5/藏6/阅613 | ErpanOmer 谈「技术极强前端难当 TL」：个人英雄主义、不愿授权、用写代码速度替代管理，在 2026 缩编环境下更易拖垮团队。偏管理随笔，技术增量有限。 | https://juejin.cn/post/7683013257235283987 |

#### 收藏热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 15 | [我给 AI 搭了个法庭：一个前端仔的 LangGraph 实战全记录](https://juejin.cn/post/7653442979387506726) | 波棱盖卡住了 | 赞59/藏86/阅4949 | 波棱盖用 LangGraph 搭「反谣言」搜索 Agent：灵感来自知乎直答 API，模式分简单/深度/DeepSearch；前端作者学 Python agent 管道全记录。固定来源外技术文，作 LangGraph 实践参考。 | https://juejin.cn/post/7653442979387506726 |

### 人工智能

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 4 | [DeepSeek V4.1 Flash：一次把自家旗舰送走的发布](https://juejin.cn/post/7683722642071470130) | 码事漫谈 | 赞15/藏6/阅569 | 码事漫谈解读 DeepSeek V4.1 Flash 正式版（9/10 12:00）：官方称全面超越 V4 Pro，计划 9/14 下线 Pro 并静默路由到 Flash。48h 内测名带 expires 0910，属激进自换代。 | https://juejin.cn/post/7683722642071470130 |
| 5 | [DeepSeek 明天又降价（涵历史价格对比）](https://juejin.cn/post/7683347149876051977) | 码事漫谈 | 赞4/藏5/阅819 | 同作者对照 Flash 三次调价：9/10 起缓存命中回到 0.02、未命中 1、输出 4（高峰翻倍）。结论：输入两档退回 8/17 前，输出只降 11% 未完全回原点。Agent/RAG 应盯缓存命中率。 | https://juejin.cn/post/7683347149876051977 |
| 7 | [每天白嫖 WorkBuddy 100 积分，我让WorkBuddy自己领](https://juejin.cn/post/7683353819855077412) | 程序员晓凡 | 赞4/藏5/阅477 | 晓凡分享 WorkBuddy「积分助手」Skill：自动签到领 100 分、可定时触发，避免断签丢 7 日奖励。产品技巧文，展示 Skill 连接器做日常自动化。 | https://juejin.cn/post/7683353819855077412 |
| 13 | [GPT images 2.5 一手实测，这也太颠了。。。](https://juejin.cn/post/7683072481465057323) | cxuanAI | 赞5/藏1/阅399 | cxuanAI 实测 ChatGPT Images 2.5（9/8–9/9 发布，热榜传播）：更快、更逼真、可 Sketch 草图转图与照片转艺术风。发布窗口 API 曾报错，属相邻日期产品体验文。 | https://juejin.cn/post/7683072481465057323 |
| 14 | [从 ChatGPT 到 Astra：四年走完的路，AGI 真的来了吗？](https://juejin.cn/post/7682634449856675867) | Cosolar | 赞6/藏1/阅364 | Cosolar 复盘 Astra 发布与 Brockman「AGI era」引语：从 ChatGPT→o1→Astra 时间线、Lean 数学与 benchmark 叙事。观点文，重大事实需回 OpenAI 官方页。 | https://juejin.cn/post/7682634449856675867 |
| 15 | [GPT-6 Astra 发布：OpenAI 正式宣告“AGI 时代到来”](https://juejin.cn/post/7681626346015916068) | 全栈弄潮儿 | 赞3/藏2/阅450 | 全栈弄潮儿 Astra 发布解读：代际跃迁、定价与开发者影响综述。与上篇同类，作传播窗口补充。 | https://juejin.cn/post/7681626346015916068 |

#### 收藏热榜

本槽无新增。

### 开发工具

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 1 | [会开完了，活还是没人干？我用 AiiOnly + Workbuddy 做了个「会议行动项助手」](https://juejin.cn/post/7683062233580634122) | 倔强的石头_ | 赞1/藏1/阅435 | 石头用 AiiOnly + WorkBuddy 做「会议行动项助手」：输入纪要输出可派工任务台账（负责人/DDL/完成标准），而不是摘要。适合内部办公 Agent PoC。 | https://juejin.cn/post/7683062233580634122 |
| 8 | [Codex、Claude Code、WorkBuddy + Tabbit CLI：让 AI 操控浏览器发文章](https://juejin.cn/post/7683738599201685538) | 若丶相见 | 赞1/藏0/阅66 | 若丶相见 实操 Codex+Tabbit CLI 操控浏览器发掘金：AI 填正文/传图，人工点发布。展示 browser automation + coding agent 分工，Codex/Claude Code/WorkBuddy 均可接 Tabbit Skill。 | https://juejin.cn/post/7683738599201685538 |
| 13 | [TraeCode从0.5开发微信小程序【需求-开发-测试】](https://juejin.cn/post/7683095604146421802) | 夜果子 | 赞1/藏1/阅40 | 夜果子用 TraeCode 积分开发微信小程序：先让 AI 拆需求文档再修 bug。Trae 靠签到/赠送积分计费，适合轻量小程序，不等于生产级 CI。 | https://juejin.cn/post/7683095604146421802 |
| 14 | [Codex 里很好用但容易被忽视的功能：Hook](https://juejin.cn/post/7683493984028459035) | 四七伵 | 赞0/藏0/阅67 | 四七伵介绍 Codex Hook：长任务（如 71 分钟）结束后汇总 skill/子 agent/文件 diff/shell 调用，降低复盘成本。Hook 内置于 Codex，适合审计型 workflow。 | https://juejin.cn/post/7683493984028459035 |
| 15 | [Windows MySQL8.0.44 保姆级超详细安装配置教程（含 ZIP 免安装、MSI 图形安装、完整卸载流程）](https://juejin.cn/post/7682663370555899958) | 知码研习 | 赞0/藏0/阅88 | 知码研习 MySQL 8.0.44 Windows 安装：ZIP 免安装、MSI、卸载三套流程 + utf8mb4 + Navicat。环境搭建教程，与 AI 无关。 | https://juejin.cn/post/7682663370555899958 |

#### 收藏热榜

本槽无新增。


### 跨榜重复与去重说明

- 本轮新摘要 URL 数：20
- 因 `seen_urls` 跳过：100（只给数量；不要把已见文再展开成表行）
- 同文多标签/双榜出现：无

### 来源清单

- 快照日：2026-09-11（Asia/Shanghai）
- 页面：https://juejin.cn/hot/articles 、 https://juejin.cn/hot/collected-articles
- 抓取：`tools/juejin_hot_fetch.py` → `_staging_latest.json`

| 标签 | 榜单 | 标题 | 链接 |
| --- | --- | --- | --- |
| 后端 | 文章热榜 | 为什么不推荐走Agent开发？ | https://juejin.cn/post/7683457864929329204 |
| 后端 | 文章热榜 | 为啥 Blender 突然火了？ | https://juejin.cn/post/7683515498140221478 |
| 后端 | 文章热榜 | 推荐一个比ES快5倍的搜索引擎 | https://juejin.cn/post/7683722642070896690 |
| 后端 | 文章热榜 | ChatGPT Plus、Pro 5x、Pro 20x 到底有多少额度？聊聊 Codex 那个让人看不懂的“周限额” | https://juejin.cn/post/7681223706186596387 |
| 后端 | 文章热榜 | Java 图片处理还在用 ImageIO？这个库让你代码从 30 行变 3 行 | https://juejin.cn/post/7681245344118063131 |
| 后端 | 文章热榜 | 学习 FastAPI 的 Day 1：看懂接口与请求流程 | https://juejin.cn/post/7682323883429232691 |
| 前端 | 文章热榜 | 为什么市面上的 coding agent 大多数都基于Nodejs？ | https://juejin.cn/post/7683481485497188403 |
| 前端 | 文章热榜 | 为什么技术极强的前端，往往当不好前端 Team Leader？ | https://juejin.cn/post/7683013257235283987 |
| 人工智能 | 文章热榜 | DeepSeek V4.1 Flash：一次把自家旗舰送走的发布 | https://juejin.cn/post/7683722642071470130 |
| 人工智能 | 文章热榜 | DeepSeek 明天又降价（涵历史价格对比） | https://juejin.cn/post/7683347149876051977 |
| 人工智能 | 文章热榜 | 每天白嫖 WorkBuddy 100 积分，我让WorkBuddy自己领 | https://juejin.cn/post/7683353819855077412 |
| 人工智能 | 文章热榜 | GPT images 2.5 一手实测，这也太颠了。。。 | https://juejin.cn/post/7683072481465057323 |
| 人工智能 | 文章热榜 | 从 ChatGPT 到 Astra：四年走完的路，AGI 真的来了吗？ | https://juejin.cn/post/7682634449856675867 |
| 人工智能 | 文章热榜 | GPT-6 Astra 发布：OpenAI 正式宣告“AGI 时代到来” | https://juejin.cn/post/7681626346015916068 |
| 开发工具 | 文章热榜 | 会开完了，活还是没人干？我用 AiiOnly + Workbuddy 做了个「会议行动项助手」 | https://juejin.cn/post/7683062233580634122 |
| 开发工具 | 文章热榜 | Codex、Claude Code、WorkBuddy + Tabbit CLI：让 AI 操控浏览器发文章 | https://juejin.cn/post/7683738599201685538 |
| 开发工具 | 文章热榜 | TraeCode从0.5开发微信小程序【需求-开发-测试】 | https://juejin.cn/post/7683095604146421802 |
| 开发工具 | 文章热榜 | Codex 里很好用但容易被忽视的功能：Hook | https://juejin.cn/post/7683493984028459035 |
| 开发工具 | 文章热榜 | Windows MySQL8.0.44 保姆级超详细安装配置教程（含 ZIP 免安装、MSI 图形安装、完整卸载流程） | https://juejin.cn/post/7682663370555899958 |
| 前端 | 收藏热榜 | 我给 AI 搭了个法庭：一个前端仔的 LangGraph 实战全记录 | https://juejin.cn/post/7653442979387506726 |

## 2026-09-10

### 今日总览

**一句话结论**：`2026-09-10` 新 URL 主线是 **Astra 价格/基准争议 + Cursor 团队上下文 + Remix 3 RC**，后端补 **固话校验正则**，开发工具补 **货拉拉 Cursor 实践和 Kaneo MCP 项目管理**。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 文章热榜 + 收藏热榜 × 后端/前端/人工智能/开发工具 |
| 榜单规模 | 每槽最多 15 条；列表总条数 120；去重后新 URL **15**；跳过已见 **105**；详情成功 15 / 失败 0 |
| 核心趋势 | 1）AI 槽继续消化 GPT-6 Astra：单价、幻觉率快照、Codex vs Cursor；2）前端值得点的是 Remix 3「不再基于 React」；3）工程文比职场焦虑/CRUD 软文更有复用价值 |
| 可直接关注 | [固话校验](https://juejin.cn/post/7682724380078080015)；[Remix 3 RC](https://juejin.cn/post/7682949323614224390)；[货拉拉 Cursor 实践](https://juejin.cn/post/7683049897089335336)；[Astra 单价](https://juejin.cn/post/7682069529204686891) |

### 后端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 1 | [固定电话验证详解：区号、号码、分机号的完整验证](https://juejin.cn/post/7682724380078080015) | vipxieliang | 赞4/藏7/阅13705 | 拆中国大陆固话三段：区号 `0`+2~3 位、本地 7~8 位、分机 1~6 位。对照常见伪正则（锁死 4+8、不强制 0 开头、分机无上限）。ValidX 用 `@ChineseLandline` 收口，并和手机/固话二选一注解划边界。适合写通讯录/政务表单校验的人。 | https://juejin.cn/post/7682724380078080015 |
| 13 | [全网 8k star 的 BuildAdmin 正式发布 Golang 版本](https://juejin.cn/post/7682190370525970442) | 妙码生花 | 赞3/藏4/阅192 | 偏产品发布：BuildAdmin 出 Golang 版，叙事是 CRUD/全栈+AI。技术细节少，适合扫一眼生态，不当架构范文。 | https://juejin.cn/post/7682190370525970442 |

#### 收藏热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 15 | [Spring之父再次出山，开发了新的AI框架！](https://juejin.cn/post/7668305038255521838) | 苏三说技术 | 赞35/藏56/阅3752 | 介绍 Rod Johnson 新做的 AI 框架方向，把 Spring 时代的「少写样板、约定大于配置」对照到 agent/框架选型。收藏榜长尾文，读观点即可，先核对项目是否仍活跃再跟。 | https://juejin.cn/post/7668305038255521838 |

### 前端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 7 | [9 月第一周，前端圈又炸了四次](https://juejin.cn/post/7682949323614224390) | 涛涛ing | 赞12/藏6/阅1181 | 周报体。头条是 Remix 3 RC：不再「基于 React」，自己做全栈运行时。其余几条是同周前端圈事件速览。适合用来定位要不要打开 Remix 官方 RC 说明，不要只停在标题。 | https://juejin.cn/post/7682949323614224390 |
| 14 | [大环境或许真的恶劣了起来，打工人你焦虑吗？](https://juejin.cn/post/7683049897088843816) | 李剑一 | 赞8/藏2/阅847 | 职场焦虑随笔，几乎无技术增量。偏情绪向，略读即可。 | https://juejin.cn/post/7683049897088843816 |

#### 收藏热榜

本槽无新增。

### 人工智能

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 10 | [GPT-6单价变成2.5倍，写代码却未必更贵](https://juejin.cn/post/7682069529204686891) | 孟健AI编程 | 赞4/藏2/阅439 | Astra API 标价约是前代 2.5 倍，但作者用 Artificial Analysis Coding Agent Index（9/3）论证：完成同样 coding agent 任务的有效成本不一定更高。读的时候把「评测日」和「官方价目」分开，别把指数当发票。 | https://juejin.cn/post/7682069529204686891 |
| 12 | [一次面试让我重新认识了 Codex，顺便搞懂了 GPT-6 Astra](https://juejin.cn/post/7681939121792778266) | 怕浪猫 | 赞4/藏6/阅429 | 从「Codex 和 Cursor 有何不同」面试题切入：一个是模型/CLI 运行时，一个是 IDE 编排层。顺带补 Astra 能力口径。适合面试备课，不是发布说明。 | https://juejin.cn/post/7681939121792778266 |
| 13 | [四、《从零手撸 Agent》 — 流式输出](https://juejin.cn/post/7681521114217791528) | 编程干货铺 | 赞8/藏10/阅312 | 系列第 4 篇：SSE/streaming 把 token 边生成边推到 UI，对比「等完整 JSON」。适合自己写 Agent 前端的人，注意和业务流式协议对齐取消/断线。 | https://juejin.cn/post/7681521114217791528 |
| 14 | [幻觉率从 4.2% 降到 2% 又退回，GPT-6 Astra 到底在藏什么](https://juejin.cn/post/7682241475045687339) | 计算机魔术师 | 赞4/藏1/阅360 | 转述 Fortune 对官方基准页快照的对比：幻觉率和部分对手分数被改过。当作「基准页会改」的提醒，数字以官方页当时版本为准，不要当学术结论。 | https://juejin.cn/post/7682241475045687339 |
| 15 | [三年前估值45亿，现在129亿——Hugging Face凭什么被老黄盯上？](https://juejin.cn/post/7681266980104421382) | 计算机魔术师 | 赞4/藏4/阅366 | 复盘 NVIDIA 收购 Hugging Face 的叙事（文内事件日为 9/3）：买的是开发者/模型生态话语权。热榜传播窗口文，细节需回官方收购稿。 | https://juejin.cn/post/7681266980104421382 |

#### 收藏热榜

本槽无新增。

### 开发工具

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 3 | [让 AI 真正读懂你的代码：一套可复用的 Cursor 辅助编码实践](https://juejin.cn/post/7683049897089335336) | 货拉拉技术 | 赞5/藏2/阅161 | 痛点是模型「会写但不知你们仓库」。货拉拉文走可复用的 Cursor 上下文：分层、命名、约定写进规则/技能，减少每轮口述架构。适合要给团队定 AI coding 手册的人。 | https://juejin.cn/post/7683049897089335336 |
| 10 | [别只拿 GPT-6 Astra 聊天，它真正恐怖的是开始会“干活”了](https://juejin.cn/post/7683152167265026111) | 摆烂工程师 | 赞2/藏0/阅72 | 反驳「Astra 聊天体感没提升」：差距在长程干活/agent 任务，不在闲聊。观点文，和孟健单价文同一主线，交叉看即可。 | https://juejin.cn/post/7683152167265026111 |
| 13 | [一天一个开源项目（第208篇）：Kaneo](https://juejin.cn/post/7681675659219025946) | 冬奇Lab | 赞0/藏1/阅115 | Kaneo：极简自托管项目管理，内置 MCP，GitHub 集成，Board/List 双视图同一数据源。适合想让 Agent 直接改任务板的小团队，先看权限模型再接到生产。 | https://juejin.cn/post/7681675659219025946 |
| 14 | [CloudDM 支持达梦、KingbaseES、GoldenDB](https://juejin.cn/post/7681476107400675337) | ClouGence | 赞0/藏1/阅68 | 产品文：统一管国产库的访问、对象、SQL 审核、工单、脱敏和 CI/CD。偏厂商能力清单。 | https://juejin.cn/post/7681476107400675337 |

#### 收藏热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 15 | [AI时代全栈面试通关指南：从背八股到聊架构](https://juejin.cn/post/7669636337370267691) | 西安小哥 | 赞7/藏16/阅562 | 面试向：AI 能写代码之后，考官更问场景和架构。当作提纲，不要当标准答案库。 | https://juejin.cn/post/7669636337370267691 |

### 跨榜重复与去重说明

- 本轮新摘要 URL 数：15
- 因 `seen_urls` 跳过：105（只给数量；不要把已见文再展开成表行）
- 同文多标签/双榜出现：无（15 条新 URL 均只出现在单一槽位）

### 来源清单

- 快照日：2026-09-10（Asia/Shanghai）
- 页面：https://juejin.cn/hot/articles 、 https://juejin.cn/hot/collected-articles
- 抓取：`tools/juejin_hot_fetch.py` → `_staging_latest.json`

| 标签 | 榜单 | 标题 | 链接 |
| --- | --- | --- | --- |
| 后端 | 文章热榜 | 固定电话验证详解：区号、号码、分机号的完整验证 | https://juejin.cn/post/7682724380078080015 |
| 后端 | 文章热榜 | 全网 8k star 的 BuildAdmin 正式发布 Golang 版本 | https://juejin.cn/post/7682190370525970442 |
| 后端 | 收藏热榜 | Spring之父再次出山，开发了新的AI框架！ | https://juejin.cn/post/7668305038255521838 |
| 前端 | 文章热榜 | 9 月第一周，前端圈又炸了四次 | https://juejin.cn/post/7682949323614224390 |
| 前端 | 文章热榜 | 大环境或许真的恶劣了起来，打工人你焦虑吗？ | https://juejin.cn/post/7683049897088843816 |
| 人工智能 | 文章热榜 | GPT-6单价变成2.5倍，写代码却未必更贵 | https://juejin.cn/post/7682069529204686891 |
| 人工智能 | 文章热榜 | 一次面试让我重新认识了 Codex，顺便搞懂了 GPT-6 Astra | https://juejin.cn/post/7681939121792778266 |
| 人工智能 | 文章热榜 | 四、《从零手撸 Agent》 — 流式输出 | https://juejin.cn/post/7681521114217791528 |
| 人工智能 | 文章热榜 | 幻觉率从 4.2% 降到 2% 又退回，GPT-6 Astra 到底在藏什么 | https://juejin.cn/post/7682241475045687339 |
| 人工智能 | 文章热榜 | 三年前估值45亿，现在129亿——Hugging Face凭什么被老黄盯上？ | https://juejin.cn/post/7681266980104421382 |
| 开发工具 | 文章热榜 | 让 AI 真正读懂你的代码：一套可复用的 Cursor 辅助编码实践 | https://juejin.cn/post/7683049897089335336 |
| 开发工具 | 文章热榜 | 别只拿 GPT-6 Astra 聊天，它真正恐怖的是开始会“干活”了 | https://juejin.cn/post/7683152167265026111 |
| 开发工具 | 文章热榜 | 一天一个开源项目（第208篇）：Kaneo | https://juejin.cn/post/7681675659219025946 |
| 开发工具 | 文章热榜 | CloudDM 支持达梦、KingbaseES、GoldenDB | https://juejin.cn/post/7681476107400675337 |
| 开发工具 | 收藏热榜 | AI时代全栈面试通关指南：从背八股到聊架构 | https://juejin.cn/post/7669636337370267691 |

## 2026-09-09

### 今日总览

**一句话结论**：`2026-09-09` 新 URL 主线是 **Agent 记忆 / AGENTS.md 治理 / Astra 提示词与发布混乱**，后端补 **open-code-review 与 EasyExcel 后继**，前端补 **DPR 糊图、流式 Markdown、独立部署地图**。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 文章热榜 + 收藏热榜 × 后端/前端/人工智能/开发工具 |
| 榜单规模 | 每槽最多 15 条；列表总条数 120；去重后新 URL **35**；跳过已见 **85**；详情成功 35 / 失败 0 |
| 核心趋势 | 1）AI 槽从「再装 Skill」转到「记忆跨会话」和「Skill/AGENTS.md 该删」；2）前端工程文比鸡汤更值得点；3）开发工具槽热度低，多是清单和排障 |
| 可直接关注 | [让 Agent 记住你](https://juejin.cn/post/7682394398210932763)；[别再堆 AGENTS.md](https://juejin.cn/post/7682611037704011827)；[Skill 大扫除](https://juejin.cn/post/7681931232724860970)；[流式 Markdown](https://juejin.cn/post/7682217734722027558) |

### 后端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 3 | [GPT - 6 Astra 的使用焚诀](https://juejin.cn/post/7682634449856217115) | cxuanAI | 赞14/藏11/阅1414 | 先排到第三方工具改了 Codex 模型列表，所以官方更新推不出 Astra；再转述 OpenAI 刚放出的 Astra 提示词，强调防偏移、指令遵循和个性化。适合刚切默认模型却看不到 Astra 的人。提示词以官方为准。 | https://juejin.cn/post/7682634449856217115 |
| 4 | [异构数据同步不只追延迟：用 KFS 守住不停机迁移的每一笔账](https://juejin.cn/post/7682364222383308850) | 一只牛博 | 赞1/藏3/阅1774 | 不停机迁移的风险不是延迟数字，而是源库持续写入时目标库对不上。主张用 Kingbase FlySync 做持续校验，而不是割接夜赌一次行数。厂商文，先当问题定义再看产品。 | https://juejin.cn/post/7682364222383308850 |
| 6 | [聊聊怎么缓解找工作的焦虑感？](https://juejin.cn/post/7682362046578884660) | 程序员飞鱼 | 赞38/藏3/阅467 | 对照「理想求职剧本」和「海投无回」的落差，给节奏与预期管理。职场向，技术增量少。 | https://juejin.cn/post/7682362046578884660 |
| 7 | [阿里开源了一个神级Agent项目](https://juejin.cn/post/7681931232724910122) | 苏三说技术 | 赞5/藏11/阅831 | 介绍阿里开源 open-code-review：内部 AI 审代码助手外放，面向多文件 PR 逐行看。适合缺 reviewer 的老项目。标题党，先看仓库能力边界。 | https://juejin.cn/post/7681931232724910122 |
| 8 | [再见了EasyExcel，我决定用Apache Fesod](https://juejin.cn/post/7682698191628632107) | 苏三说技术 | 赞12/藏9/阅540 | EasyExcel 仓库 2025-09 归档后，作者线走到 FastExcel 再改名 Apache Fesod。适合还卡在 EasyExcel 的 Java 表格项目，升级前对一下包名与兼容。 | https://juejin.cn/post/7682698191628632107 |
| 9 | [读《阿里巴巴Java开发手册》五年，这7条规约救了我太多次](https://juejin.cn/post/7681797570142732331) | 气泡水好喝 | 赞9/藏14/阅454 | 用生产事故回看手册：线程池、NPE、序列化等 7 条。入门复盘，不是新规范。 | https://juejin.cn/post/7681797570142732331 |
| 12 | [别再堆 AGENTS.md 了：前端团队如何把 AI Coding 做成一套可执行的工程系统](https://juejin.cn/post/7682611037704011827) | LEE | 赞8/藏9/阅236 | 把 AGENTS.md 当宪法而不是杂物箱：上下文、动作、质量门要分文件。和 AI 槽「Skill 大扫除」同一主线，后端槽也能看。 | https://juejin.cn/post/7682611037704011827 |

#### 收藏热榜

本槽无新增。

### 前端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 3 | [设计稿里的图片明明很清晰，为什么到了手机上却糊了？一文讲透 DPR、压缩与格式选择](https://juejin.cn/post/7682406523184709670) | 不一样的少年_ | 赞22/藏23/阅860 | 从像素、DPR、倍图讲到有损压缩、色带和 JPG/PNG/WebP/AVIF/SVG 选型。适合设计稿「很清、真机很糊」的排障。 | https://juejin.cn/post/7682406523184709670 |
| 6 | [支持独立部署的地图方案](https://juejin.cn/post/7682362046578966580) | Gyrate | 赞19/藏44/阅777 | 城市治理/数字孪生在内网或断网时不能只绑高德 JSAPI，要自建底图、POI 和 GL。有石河子项目对照。适合政企大屏。 | https://juejin.cn/post/7682362046578966580 |
| 9 | [面试官：Markdown 流式解析如何避免标签截断？](https://juejin.cn/post/7682217734722027558) | 秋天的一阵风 | 赞13/藏20/阅884 | 全量重跑 marked 会抖、半截标签会破 DOM。讲增量解析和未闭合标签缓冲。做 AI 对话页的人值得看。 | https://juejin.cn/post/7682217734722027558 |
| 10 | [明明做了很多事，为什么简历看起来还是没含金量？](https://juejin.cn/post/7682253775991734323) | 不一样的少年_ | 赞20/藏26/阅636 | 批评简历堆系统名、不写约束和结果。求职向。 | https://juejin.cn/post/7682253775991734323 |
| 11 | [别卷CRUD了！前端用Next.js+LangChain.js，低成本冲进AI高薪赛道](https://juejin.cn/post/7681252693901885478) | 码农悟道 | 赞9/藏14/阅894 | 主张前端用 JS 栈做 RAG/Agent，不必先转 Python。路径向，含金量看你有没有可演示仓库。 | https://juejin.cn/post/7681252693901885478 |
| 12 | [提前还贷，缩短年限和降低月供其实是一样的](https://juejin.cn/post/7682013859251896320) | 背对疾风 | 赞8/藏4/阅802 | 用还款模拟器讲等额本息。和生活计算有关，和前端工程无关。 | https://juejin.cn/post/7682013859251896320 |
| 13 | [太好了！NestJS 12 大版本转向 ESM，新项目默认构建换 Rspack](https://juejin.cn/post/7681204371800948736) | Moment | 赞10/藏5/阅782 | 记录 `@nestjs/core` 12.0.1：ESM 默认、新项目构建换 Rspack。升级前先对装饰器和现有 CJS。 | https://juejin.cn/post/7681204371800948736 |
| 15 | [首屏Banner压到40KB，LCP还是4秒？原来一直搞错了最大渲染元素](https://juejin.cn/post/7682046779555315763) | 秋天的一阵风 | 赞6/藏8/阅714 | LCP 元素经常不是你优化的 Banner。先用 Performance 认元素再压图。面试和线上都常用。 | https://juejin.cn/post/7682046779555315763 |

#### 收藏热榜

本槽无新增。

### 人工智能

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 1 | [走进AI Agent第三篇：让 Agent 记住你](https://juejin.cn/post/7682394398210932763) | 老王以为 | 赞20/藏23/阅8199 | 会话内压缩/KV 管不了「下次还认识你」。拆跨会话记忆：写什么、何时写、怎么检索，避免把整段聊天当记忆。系列文，本篇只谈用户记忆。 | https://juejin.cn/post/7682394398210932763 |
| 2 | [三年了，AI为何还没有抢走程序员饭碗？](https://juejin.cn/post/7682262550978936884) | 写代码像蔡徐抻 | 赞45/藏17/阅4304 | 用交付责任、评测和遗留系统解释为什么到 Fable 5 / GPT-6 仍没大裁员。评论多，观点文。 | https://juejin.cn/post/7682262550978936884 |
| 5 | [OpenAI ：GPT-6 开始你需要给 Skill 和 AGENTS.md 做一次大扫除了](https://juejin.cn/post/7681931232724860970) | 恋猫de小郭 | 赞10/藏7/阅1557 | 强模型下 Superpowers 一类长流程 skill 会变负优化。主张少装、可验证、能删。和后端槽 AGENTS.md 文对读。 | https://juejin.cn/post/7681931232724860970 |
| 7 | [奥尔特曼致歉 GPT-6 Astra 发布混乱，现已面向所有 Plus / Pro 等用户推出](https://juejin.cn/post/7681733440023183414) | 计算机魔术师 | 赞3/藏3/阅694 | 复盘 9/3 发布后 Plus/Pro 先用不上、CEO 致歉、两天后放开。时间线向，规格看官方。 | https://juejin.cn/post/7681733440023183414 |
| 10 | [英伟达砸130亿美元买下一个平台，黄仁勋到底在怕什么？](https://juejin.cn/post/7681266980104683526) | 计算机魔术师 | 赞2/藏2/阅465 | 按 SEC 文件拆 Hugging Face 收购对价，解释「守模型分发入口」。产业评论。 | https://juejin.cn/post/7681266980104683526 |
| 12 | [从 Token 到蒸馏：一步步理解大模型如何工作](https://juejin.cn/post/7681213028792500287) | 杨杨杨大侠 | 赞5/藏5/阅337 | 用本机 Qwen2.5 0.5B 串 Token、参数、训练、蒸馏、量化。入门向。 | https://juejin.cn/post/7681213028792500287 |
| 13 | [刚刚，Claude 5.1 发布！全球最强模型来了？](https://juejin.cn/post/7680471403955683334) | Behaviour | 赞5/藏3/阅383 | 转述 9/1 Fable 5.1 / Mythos 5.1。发布已过一周，当传播窗口摘要即可。 | https://juejin.cn/post/7680471403955683334 |
| 14 | [Anthropic 自己承认：模型越来越难管住了](https://juejin.cn/post/7680405261430587428) | 计算机魔术师 | 赞4/藏4/阅399 | 读 Fable 5.1 系统卡：隐蔽绕过监督者的比例升高。和 AI 日报对齐主题同周，社区转述。 | https://juejin.cn/post/7680405261430587428 |
| 15 | [AI 说话越来越难懂？Anthropic 员工都在用 ELI5 这个图解 Skill](https://juejin.cn/post/7681574954577281076) | 深小乐go | 赞8/藏7/阅275 | 介绍内部流行的 ELI5 图解 Skill。一个小 skill 案例，不是平台更新。 | https://juejin.cn/post/7681574954577281076 |

#### 收藏热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 14 | [凌晨睡不着，我给台风巴威写了个追踪网站](https://juejin.cn/post/7659393583027896330) | HiSt | 赞151/藏82/阅19793 | 用 Claude Fable 5 把四家气象路径叠到一张地图。旧文因本轮新 URL 入表。仓库在 GitHub，偏周末项目。 | https://juejin.cn/post/7659393583027896330 |
| 15 | [22道AI Agent 工程师必会的面试题](https://juejin.cn/post/7660415930171490356) | Coffeeee | 赞40/藏77/阅1862 | Agent/RAG/MCP/Skill 面试笔记。旧文新 URL，当题单不要当标准答案。 | https://juejin.cn/post/7660415930171490356 |

### 开发工具

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 5 | [现在回头看，Dart取消宏是无比正确的决定](https://juejin.cn/post/7683027781632294946) | 程序员老刘 | 赞1/藏0/阅89 | 认为宏/注解/编译期生成会挡 AI 读代码，语言会回到更直的语法。观点文，热度低。 | https://juejin.cn/post/7683027781632294946 |
| 6 | [别只会用 Postman 了，这 15 款接口测试工具你可能还不知道](https://juejin.cn/post/7682711436210241563) | 狂师 | 赞1/藏0/阅103 | Postman 免费版收紧后的替代清单。清单向，按开源/协作需求自选。 | https://juejin.cn/post/7682711436210241563 |
| 7 | [录屏总黑屏？90% 的人没关这个开关](https://juejin.cn/post/7681138712659492879) | 搬砖记录员 | 赞0/藏0/阅123 | 浏览器硬件加速和录屏抢 GPU。关加速、降分辨率/码率、清权限三步。 | https://juejin.cn/post/7681138712659492879 |
| 9 | [CC Switch 切换 Codex 中转站后历史会话打不开？](https://juejin.cn/post/7680471403956322310) | 凭君语未可 | 赞0/藏0/阅122 | 切 custom provider 后旧会话绑着已经不存在的 `model_provider`。改 config 或只在新会话切站。 | https://juejin.cn/post/7680471403956322310 |
| 11 | [Docker 部署 go2rtc：轻松搭建摄像头多协议流媒体平台](https://juejin.cn/post/7681959629414694954) | 程序员老赵 | 赞1/藏2/阅91 | 用 go2rtc 1.9.14 把门铃/RTSP 转浏览器可播。家庭监控向。 | https://juejin.cn/post/7681959629414694954 |
| 12 | [企业级 Agent 平台开源：ZGI 把模型、知识库、Skills 和 Workflow 放进同一个 Runtime](https://juejin.cn/post/7681830868798865427) | ZGIAI | 赞2/藏1/阅67 | 作者推销自研 Runtime：模型/知识/Skill/流程/治理一体。偏产品稿，先看许可和是否真开源。 | https://juejin.cn/post/7681830868798865427 |
| 13 | [GitHub 从入门到精通（精炼版）：30 分钟跑通建仓、提交与协作](https://juejin.cn/post/7680996030842273828) | 编程快车 | 赞1/藏2/阅81 | clone/commit/PR 入门。给完全没碰过 GitHub 的人。 | https://juejin.cn/post/7680996030842273828 |

#### 收藏热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 12 | [实测 9 款 AI 架构图工具：从 Mermaid 美化到 GPT-Image2](https://juejin.cn/post/7669611082151706643) | 京东云开发者 | 赞3/藏17/阅509 | 对比拖拽工具和 DSL 美化，给评审/PPT 用图选型。旧文新 URL。作者挂京东云。 | https://juejin.cn/post/7669611082151706643 |
| 13 | [公司取消前端岗后，做了 10 年 Java 的我，第一次认真拥抱 AI](https://juejin.cn/post/7668341210563870720) | 天天摸鱼的java工程师 | 赞22/藏18/阅3126 | 前端岗收缩后的 Java 转 AI 全栈心路。旧文，情绪向。 | https://juejin.cn/post/7668341210563870720 |

### 跨榜重复与去重说明

- 本轮新摘要 URL 数：35
- 因 `seen_urls` 跳过：85（只给数量；已见文不占表行）
- 同文多标签/双榜出现：本轮 35 条均只出现在单一 `(标签, 榜单)` 槽位

### 来源清单

- 快照日：2026-09-09（Asia/Shanghai）
- 页面：https://juejin.cn/hot/articles 、 https://juejin.cn/hot/collected-articles
- 抓取：`tools/juejin_hot_fetch.py` → `_staging_latest.json`

| 标签 | 榜单 | 标题 | 链接 |
| --- | --- | --- | --- |
| 后端 | 文章热榜 | GPT - 6 Astra 的使用焚诀 | https://juejin.cn/post/7682634449856217115 |
| 后端 | 文章热榜 | 异构数据同步不只追延迟：用 KFS 守住不停机迁移的每一笔账 | https://juejin.cn/post/7682364222383308850 |
| 后端 | 文章热榜 | 聊聊怎么缓解找工作的焦虑感？ | https://juejin.cn/post/7682362046578884660 |
| 后端 | 文章热榜 | 阿里开源了一个神级Agent项目 | https://juejin.cn/post/7681931232724910122 |
| 后端 | 文章热榜 | 再见了EasyExcel，我决定用Apache Fesod | https://juejin.cn/post/7682698191628632107 |
| 后端 | 文章热榜 | 读《阿里巴巴Java开发手册》五年，这7条规约救了我太多次 | https://juejin.cn/post/7681797570142732331 |
| 后端 | 文章热榜 | 别再堆 AGENTS.md 了 | https://juejin.cn/post/7682611037704011827 |
| 前端 | 文章热榜 | 设计稿里的图片明明很清晰，为什么到了手机上却糊了？ | https://juejin.cn/post/7682406523184709670 |
| 前端 | 文章热榜 | 支持独立部署的地图方案 | https://juejin.cn/post/7682362046578966580 |
| 前端 | 文章热榜 | Markdown 流式解析如何避免标签截断？ | https://juejin.cn/post/7682217734722027558 |
| 前端 | 文章热榜 | 明明做了很多事，为什么简历看起来还是没含金量？ | https://juejin.cn/post/7682253775991734323 |
| 前端 | 文章热榜 | 别卷CRUD了！前端用Next.js+LangChain.js | https://juejin.cn/post/7681252693901885478 |
| 前端 | 文章热榜 | 提前还贷，缩短年限和降低月供其实是一样的 | https://juejin.cn/post/7682013859251896320 |
| 前端 | 文章热榜 | NestJS 12 大版本转向 ESM | https://juejin.cn/post/7681204371800948736 |
| 前端 | 文章热榜 | 首屏Banner压到40KB，LCP还是4秒？ | https://juejin.cn/post/7682046779555315763 |
| 人工智能 | 文章热榜 | 走进AI Agent第三篇：让 Agent 记住你 | https://juejin.cn/post/7682394398210932763 |
| 人工智能 | 文章热榜 | 三年了，AI为何还没有抢走程序员饭碗？ | https://juejin.cn/post/7682262550978936884 |
| 人工智能 | 文章热榜 | GPT-6 开始你需要给 Skill 和 AGENTS.md 做一次大扫除了 | https://juejin.cn/post/7681931232724860970 |
| 人工智能 | 文章热榜 | 奥尔特曼致歉 GPT-6 Astra 发布混乱 | https://juejin.cn/post/7681733440023183414 |
| 人工智能 | 文章热榜 | 英伟达砸130亿美元买下一个平台 | https://juejin.cn/post/7681266980104683526 |
| 人工智能 | 文章热榜 | 从 Token 到蒸馏 | https://juejin.cn/post/7681213028792500287 |
| 人工智能 | 文章热榜 | 刚刚，Claude 5.1 发布！ | https://juejin.cn/post/7680471403955683334 |
| 人工智能 | 文章热榜 | Anthropic 自己承认：模型越来越难管住了 | https://juejin.cn/post/7680405261430587428 |
| 人工智能 | 文章热榜 | Anthropic 员工都在用 ELI5 | https://juejin.cn/post/7681574954577281076 |
| 开发工具 | 文章热榜 | Dart取消宏是无比正确的决定 | https://juejin.cn/post/7683027781632294946 |
| 开发工具 | 文章热榜 | 15 款接口测试工具 | https://juejin.cn/post/7682711436210241563 |
| 开发工具 | 文章热榜 | 录屏总黑屏 | https://juejin.cn/post/7681138712659492879 |
| 开发工具 | 文章热榜 | CC Switch 切换后历史会话打不开 | https://juejin.cn/post/7680471403956322310 |
| 开发工具 | 文章热榜 | Docker 部署 go2rtc | https://juejin.cn/post/7681959629414694954 |
| 开发工具 | 文章热榜 | ZGI 企业级 Agent 平台 | https://juejin.cn/post/7681830868798865427 |
| 开发工具 | 文章热榜 | GitHub 从入门到精通 | https://juejin.cn/post/7680996030842273828 |
| 人工智能 | 收藏热榜 | 台风巴威追踪网站 | https://juejin.cn/post/7659393583027896330 |
| 人工智能 | 收藏热榜 | 22道AI Agent 面试题 | https://juejin.cn/post/7660415930171490356 |
| 开发工具 | 收藏热榜 | 实测 9 款 AI 架构图工具 | https://juejin.cn/post/7669611082151706643 |
| 开发工具 | 收藏热榜 | 取消前端岗后拥抱 AI | https://juejin.cn/post/7668341210563870720 |

## 2026-09-07

### 今日总览

**一句话结论**：`2026-09-07` 新 URL 主线是 **Astra 选型与发布日多模型宕机、Harness/Runtime 术语澄清，以及 UniApp 路由守卫 / 余额扣减等工程短文**；收藏榜仅后端补一篇 Tika。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 文章热榜 + 收藏热榜 × 后端/前端/人工智能/开发工具 |
| 榜单规模 | 每槽最多 15 条；列表总条数 120；去重后新 URL **28**；跳过已见 **92**；详情成功 28 / 失败 0 |
| 核心趋势 | 1）AI 槽从「装插件」转到「默认模型贵不贵、全家桶会不会一起挂」；2）前端继续 Rust 工具链 + 一人交货叙事；3）开发工具出现 Codex 账号切换与京东云移动端交付链路 |
| 可直接关注 | [Astra vs Sol](https://juejin.cn/post/7681223706187153443)；[宕机复盘](https://juejin.cn/post/7681475476906950691)；[Harness vs Runtime](https://juejin.cn/post/7679753075939524623)；[UniApp middleware](https://juejin.cn/post/7681170932347830310) |

### 后端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 6 | [GPT-6 Astra 来了，GPT-5.6 Sol 还值得用吗？聊聊 Coding、百万上下文、价格和 Plus/Pro](https://juejin.cn/post/7681223706187153443) | 掘金者阿豪 | 赞8/藏4/阅762 | 用 Coding、上下文和 Plus/Pro 价格讨论 Astra 该不该替换 Sol。适合额度敏感的人。社区对比，规格以官方为准。 | https://juejin.cn/post/7681223706187153443 |
| 9 | [MyBatis-Plus 项目为什么越写越复杂：从一行 Wrapper 说起](https://juejin.cn/post/7680812218214236194) | 落木萧萧825 | 赞4/藏4/阅227 | 从一行 Wrapper 讲到条件膨胀、XML 回潮和「便捷 API 把复杂度藏进调用方」。适合 MP 项目开始难改的人。 | https://juejin.cn/post/7680812218214236194 |
| 10 | [从零到上线：全栈项目部署全流程实战](https://juejin.cn/post/7680457986106736667) | mONESY | 赞7/藏9/阅196 | 先拆清部署的是 dist、API 还是数据库，再谈 Nginx/进程/迁移。适合第一次上线前后端分离的人。 | https://juejin.cn/post/7680457986106736667 |
| 12 | [打破传统 MVC：在 Go 中实践高内聚的业务驱动架构](https://juejin.cn/post/7681143768221974568) | Vespeng | 赞1/藏4/阅185 | 批评水平分层在 Go 里来回跳目录，主张按业务包高内聚。适合 Go 服务开始膨胀的人。一种口味，不是标准。 | https://juejin.cn/post/7681143768221974568 |
| 14 | [高并发下怎么做余额扣减？](https://juejin.cn/post/7681245344118210587) | 花宝宝Dev | 赞2/藏6/阅193 | 「先查再扣」在并发下会超扣，要用条件更新或账本。入门向，适合补并发课。 | https://juejin.cn/post/7681245344118210587 |
| 15 | [GenOffice上手指南：免费替代Word+PPT+Excel的AI办公神器](https://juejin.cn/post/7680916426782998538) | SimonKing | 赞1/藏4/阅192 | 安利开源 AI 办公套件 GenOffice。产品向，先看许可与数据是否出域。 | https://juejin.cn/post/7680916426782998538 |

#### 收藏热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 14 | [为什么越来越多人用Apache Tika？](https://juejin.cn/post/7667853684410302490) | 苏三说技术 | 赞31/藏58/阅2682 | 一种格式一个解析库会把依赖撕开，Tika 当统一文本抽取门面。适合文档管道，不是新文（7 月），因本轮新 URL 才入表。 | https://juejin.cn/post/7667853684410302490 |

### 前端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 5 | [Bun 真的能取代 Node.js 吗？](https://juejin.cn/post/7680899684959272970) | ErpanOmer | 赞14/藏6/阅885 | Bun 冷启动和装包快，但生态和 JavaScriptCore 限制仍在。结论是场景分流，不是替换宣言。 | https://juejin.cn/post/7680899684959272970 |
| 6 | [用 17 行代码给 UniApp 加上全局登录拦截](https://juejin.cn/post/7681170932347830310) | skiyee | 赞18/藏17/阅739 | 给 oiyo/UniApp 路由加 middleware 做登录守卫。适合小程序/App 统一鉴权。17 行是作者最小实现。 | https://juejin.cn/post/7681170932347830310 |
| 9 | [一周之内，前端 AI 编程的格局被彻底改写了三次](https://juejin.cn/post/7681146373547868166) | 涛涛ing | 赞7/藏6/阅898 | 从 Qwen3.8-Max 上前端榜讲「格局改写」。观察文，榜单会变，勿当规格。 | https://juejin.cn/post/7681146373547868166 |
| 13 | [2026 年前端的“新王登基”：Rust 正在吃掉整个工具链](https://juejin.cn/post/7680841873821728810) | 涛涛ing | 赞5/藏8/阅606 | 用 npm install 过慢引出 Rust 工具链叙事。趋势文，迁移成本要自己算。 | https://juejin.cn/post/7680841873821728810 |
| 14 | [一个人，4个岗位，20天：我用Cursor+Codex上线了一款微信小游戏](https://juejin.cn/post/7681286465168769067) | 亿元程序员 | 赞10/藏12/阅467 | 一人分美术/策划/程序/运营，用 Cursor+Codex 20 天上微信小游戏。个案，验收物比工具清单重要。 | https://juejin.cn/post/7681286465168769067 |
| 15 | [前端学了 Next.js，后端该学啥？NestJS 就是 Node 版的蜜雪冰城](https://juejin.cn/post/7680766055174651947) | 默_笙 | 赞12/藏10/阅460 | 用 Next vs Nest 定位：SSR/API 路由对企业 API。入门向，标题营销。 | https://juejin.cn/post/7680766055174651947 |

#### 收藏热榜

本槽无新增。

### 人工智能

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 5 | [GPT-6 发布当晚，三大 AI 集体宕机 4 小时——我扒完时间线，发现最该慌的不是宕机](https://juejin.cn/post/7681475476906950691) | kyriewen | 赞9/藏7/阅1026 | 整理 ChatGPT/Claude/Grok 同时不可用的时间线，强调工具全家桶的单点故障。时间线是作者整理，官方事故页为准。 | https://juejin.cn/post/7681475476906950691 |
| 8 | [一、《从零手撸 Agent》 我用 10 行代码跑通了第一次大模型调用（顺便踩了 4 个坑）](https://juejin.cn/post/7680471403955191814) | 编程干货铺 | 赞12/藏8/阅548 | 从 Key、计费和第一次 HTTP 调用讲起。适合完全没接过 API 的人。系列开篇。 | https://juejin.cn/post/7680471403955191814 |
| 10 | [一文弄懂 Agent Harness 与 Agent Runtime 的区别](https://juejin.cn/post/7679753075939524623) | Cosolar | 赞9/藏6/阅504 | 澄清 2026 上半年「外层工程」被叫成 Harness 或 Runtime 的术语漂移。适合开会对齐词汇的人。8 月文，本轮新 URL。 | https://juejin.cn/post/7679753075939524623 |
| 11 | [Fable 5.1 实测：15.84 美元，Pro 用户该买吗？](https://juejin.cn/post/7680761768890253322) | 孟健AI编程 | 赞7/藏7/阅424 | 一次 30 分 43 秒任务按 Claude Code telemetry 约 15.84 美元。适合算 Pro 月费够不够的人。口径是作者本次 run。 | https://juejin.cn/post/7680761768890253322 |
| 12 | [天才陨落了！三大 AI 集体不可用！](https://juejin.cn/post/7681160462331772969) | 陈大鱼头 | 赞5/藏6/阅466 | 同一窗口的不可用见闻，信息密度低于 kyriewen 复盘。可略读。 | https://juejin.cn/post/7681160462331772969 |
| 13 | [DeepSeek Harness 从零上手：从认识到写出第一个插件](https://juejin.cn/post/7680183953518690338) | 前端梦工厂 | 赞5/藏9/阅439 | 真机走通 DeepSeek Harness 安装到第一个工具插件。适合要最小可运行单元的人。 | https://juejin.cn/post/7680183953518690338 |
| 14 | [AI 视频迎来了奇点时刻](https://juejin.cn/post/7680387129118277686) | stormzhangV | 赞11/藏9/阅315 | MiniMax H3 Max 出片速度 + fal 开源互动直播。产品观察，偏营销可略读。 | https://juejin.cn/post/7680387129118277686 |
| 15 | [豆包完胜 DeepSeek ？！零玩家竞技场，AI Agent 专属对弈！](https://juejin.cn/post/7680833230097481763) | xiaohe0601 | 赞5/藏2/阅293 | 用斗破文风包装 Agent 对弈。娱乐向，技术增量有限。 | https://juejin.cn/post/7680833230097481763 |

#### 收藏热榜

本槽无新增。

### 开发工具

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 8 | [零成本搭文档站：VitePress + GitHub Pages 就够了](https://juejin.cn/post/7682024345256624166) | 羽升 | 赞2/藏0/阅52 | Markdown 提示词做成可搜索 VitePress，接 Actions 发布。适合内部笔记站。 | https://juejin.cn/post/7682024345256624166 |
| 9 | [Codex 多账号切换不再折腾：OAuth 配对与 Auth 迁移实践](https://juejin.cn/post/7681135640989499434) | Mintimate | 赞0/藏1/阅83 | 本地管理多 Codex 账号：切换、OAuth 配对、一次性 Auth 迁移、凭据校验与原子替换。只讲本机管理，不涉及绕过官方登录。 | https://juejin.cn/post/7681135640989499434 |
| 10 | [Codex 驱动的移动端AI全栈开发：从 Relay 原型图到可交付链路](https://juejin.cn/post/7680938642576277538) | 京东云开发者 | 赞0/藏1/阅97 | 「AI 写了页面」不等于移动端交付：C 端约束、组件库和验收链路。京东云开发者，偏实践。 | https://juejin.cn/post/7680938642576277538 |
| 11 | [用例写不完、回归跑不动？我把最磨人的活交给 TestHub，KPI 反而稳了](https://juejin.cn/post/7680764114492555274) | 大刚测试开发实战 | 赞0/藏0/阅80 | 用 TestHub 扛需求转用例和回归。偏产品软文，可当问题清单略读。 | https://juejin.cn/post/7680764114492555274 |
| 13 | [tmux 会话管理在 AI 编程中的高级实战](https://juejin.cn/post/7680023541135999017) | CaoZH | 赞0/藏0/阅91 | 用 tmux 同时管多个 Claude Code/Codex 会话并跨机器恢复。适合终端重度用户。 | https://juejin.cn/post/7680023541135999017 |
| 14 | [告别臃肿与局限，FlyEnv 让本地开发环境管理更便捷](https://juejin.cn/post/7661544967236010010) | hezhifu | 赞0/藏0/阅99 | FlyEnv 把本地 Web/DB/运行时收进原生二进制面板。7 月文，本轮新 URL。容器派可跳过。 | https://juejin.cn/post/7661544967236010010 |
| 15 | [看 react-bits，不要只看“酷炫”：一套阅读动画交互组件库的框架](https://juejin.cn/post/7681797570133737535) | 吴琼琼 | 赞2/藏2/阅34 | 给高星动画库一套阅读顺序，先问复用再问特效。和上一轮 react-bits 安利文 complementary。 | https://juejin.cn/post/7681797570133737535 |

#### 收藏热榜

本槽无新增。

### 跨榜重复与去重说明

- 本轮新摘要 URL 数：28
- 因 `seen_urls` 跳过：92（只给数量；不要把已见文再展开成表行）
- 同文多标签/双榜出现：无（28 条均只出现在一个槽位）

### 来源清单

- 快照日：2026-09-07（Asia/Shanghai）
- 页面：https://juejin.cn/hot/articles 、 https://juejin.cn/hot/collected-articles
- 抓取：`tools/juejin_hot_fetch.py` → `_staging_latest.json`

| 标签 | 榜单 | 标题 | 链接 |
| --- | --- | --- | --- |
| 后端 | 文章热榜 | GPT-6 Astra 来了，GPT-5.6 Sol 还值得用吗？ | https://juejin.cn/post/7681223706187153443 |
| 后端 | 文章热榜 | MyBatis-Plus 项目为什么越写越复杂 | https://juejin.cn/post/7680812218214236194 |
| 后端 | 文章热榜 | 从零到上线：全栈项目部署全流程实战 | https://juejin.cn/post/7680457986106736667 |
| 后端 | 文章热榜 | 打破传统 MVC：在 Go 中实践高内聚的业务驱动架构 | https://juejin.cn/post/7681143768221974568 |
| 后端 | 文章热榜 | 高并发下怎么做余额扣减？ | https://juejin.cn/post/7681245344118210587 |
| 后端 | 文章热榜 | GenOffice上手指南 | https://juejin.cn/post/7680916426782998538 |
| 后端 | 收藏热榜 | 为什么越来越多人用Apache Tika？ | https://juejin.cn/post/7667853684410302490 |
| 前端 | 文章热榜 | Bun 真的能取代 Node.js 吗？ | https://juejin.cn/post/7680899684959272970 |
| 前端 | 文章热榜 | 用 17 行代码给 UniApp 加上全局登录拦截 | https://juejin.cn/post/7681170932347830310 |
| 前端 | 文章热榜 | 一周之内，前端 AI 编程的格局被彻底改写了三次 | https://juejin.cn/post/7681146373547868166 |
| 前端 | 文章热榜 | Rust 正在吃掉整个工具链 | https://juejin.cn/post/7680841873821728810 |
| 前端 | 文章热榜 | 一个人，4个岗位，20天：微信小游戏 | https://juejin.cn/post/7681286465168769067 |
| 前端 | 文章热榜 | NestJS 就是 Node 版的蜜雪冰城 | https://juejin.cn/post/7680766055174651947 |
| 人工智能 | 文章热榜 | GPT-6 发布当晚，三大 AI 集体宕机 4 小时 | https://juejin.cn/post/7681475476906950691 |
| 人工智能 | 文章热榜 | 从零手撸 Agent：第一次大模型调用 | https://juejin.cn/post/7680471403955191814 |
| 人工智能 | 文章热榜 | Agent Harness 与 Agent Runtime 的区别 | https://juejin.cn/post/7679753075939524623 |
| 人工智能 | 文章热榜 | Fable 5.1 实测：15.84 美元 | https://juejin.cn/post/7680761768890253322 |
| 人工智能 | 文章热榜 | 天才陨落了！三大 AI 集体不可用 | https://juejin.cn/post/7681160462331772969 |
| 人工智能 | 文章热榜 | DeepSeek Harness 从零上手 | https://juejin.cn/post/7680183953518690338 |
| 人工智能 | 文章热榜 | AI 视频迎来了奇点时刻 | https://juejin.cn/post/7680387129118277686 |
| 人工智能 | 文章热榜 | 豆包完胜 DeepSeek ？零玩家竞技场 | https://juejin.cn/post/7680833230097481763 |
| 开发工具 | 文章热榜 | 零成本搭文档站：VitePress | https://juejin.cn/post/7682024345256624166 |
| 开发工具 | 文章热榜 | Codex 多账号切换：OAuth 配对 | https://juejin.cn/post/7681135640989499434 |
| 开发工具 | 文章热榜 | Codex 驱动的移动端 AI 全栈开发 | https://juejin.cn/post/7680938642576277538 |
| 开发工具 | 文章热榜 | TestHub 用例与回归 | https://juejin.cn/post/7680764114492555274 |
| 开发工具 | 文章热榜 | tmux 会话管理在 AI 编程中的高级实战 | https://juejin.cn/post/7680023541135999017 |
| 开发工具 | 文章热榜 | FlyEnv 本地开发环境 | https://juejin.cn/post/7661544967236010010 |
| 开发工具 | 文章热榜 | 看 react-bits，不要只看“酷炫” | https://juejin.cn/post/7681797570133737535 |

## 2026-09-04

### 今日总览

**一句话结论**：`2026-09-04` 新 URL 主线是 **Skill 分工/Harness 落地、微信登录坑、WebMCP 澄清，以及 CodeSchema 这类「按需喂上下文」索引**；后端仍是 AOP/备份边界，收藏榜补 Netmaker。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 文章热榜 + 收藏热榜 × 后端/前端/人工智能/开发工具 |
| 榜单规模 | 每槽最多 15 条；列表总条数 120；去重后新 URL **29**；跳过已见 **91**；详情成功 29 / 失败 0 |
| 核心趋势 | 1）前端/AI 槽从「必装清单」转到「岗位/短步/验收物」；2）开发工具出现代码图谱类索引服务；3）后端热榜回到基础组件与备份语义 |
| 可直接关注 | [8 岗位 Skill](https://juejin.cn/post/7680043958139748406)；[Codex 短步](https://juejin.cn/post/7680500716225871910)；[WebMCP](https://juejin.cn/post/7680216488121303050)；[CodeSchema](https://juejin.cn/post/7680757400489000996) |

### 后端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 1 | [Java切面编程（AOP）详解：从核心概念到实战应用](https://juejin.cn/post/7680496681512042548) | vipxieliang | 赞8/藏9/阅14657 | Java AOP 从横切关注点讲到 Aspect/JoinPoint/Pointcut/Advice。适合刚碰 Spring 的人。综述入门，版本细节以当下 Spring 为准。 | https://juejin.cn/post/7680496681512042548 |
| 5 | [sys_dump 备了库，角色和权限别漏在外面](https://juejin.cn/post/7680551559094517802) | 一只牛博 | 赞0/藏0/阅1562 | sys_dump 只备份单库，角色/表空间等全局对象不在包里，还原会报 role does not exist。适合做库迁移的人。先单独导出角色再还数据。 | https://juejin.cn/post/7680551559094517802 |
| 8 | [内网穿透原来这么简单：Natapp 从注册到公网访问完整教程](https://juejin.cn/post/7680877878047408154) | 一只牛博 | 赞0/藏1/阅641 | Natapp 从注册、实名到第一条公网隧道，对比自建 FRP。适合要尽快把本地服务暴露出去的人。偏产品教程，安全与实名以官网为准。 | https://juejin.cn/post/7680877878047408154 |
| 11 | [换了工作流引擎，前端一行代码没改](https://juejin.cn/post/7680094035273121802) | mldong | 赞2/藏2/阅237 | jeeflow 第 12 篇：换工作流引擎但前端契约（code=0、分页五键、42 个 action）不变，框架只留薄翻译层。适合做引擎替换的人。数字来自作者仓库。 | https://juejin.cn/post/7680094035273121802 |
| 12 | [手机投屏到电脑，不用装任何 App，这个开源工具免费搞定：QtScrcpy](https://juejin.cn/post/7680456045867483145) | SimonKing | 赞6/藏6/阅149 | 安利 QtScrcpy：无 root、USB/无线把安卓投到电脑，带按键映射。适合演示移动端的人。基于 scrcpy，权限仍要自己管。 | https://juejin.cn/post/7680456045867483145 |
| 14 | [个人RAG上线翻车实录-记一次 API 延迟排查](https://juejin.cn/post/7679458659610394674) | 张炯炯 | 赞2/藏4/阅217 | 个人 RAG 上线后问答从 8 秒变成 2–5 分钟，五步计时锁定 Redis 缓存。适合刚把 RAG 推生产的人。案例小，方法是先打点再猜。 | https://juejin.cn/post/7679458659610394674 |
| 15 | [Rust 桌面宠物拖拽踩坑实录：重影、不跟手、置顶失效](https://juejin.cn/post/7679133086102110254) | 再吃一根胡萝卜 | 赞1/藏6/阅226 | Rust+winit 做桌面宠物：重影、拖拽不跟手、置顶失效。适合写无边框透明窗的人。Windows/DPI 向。 | https://juejin.cn/post/7679133086102110254 |

#### 收藏热榜

本槽无新增。

### 前端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 6 | [我装了30多个Skill，给AI安排了8个岗位](https://juejin.cn/post/7680043958139748406) | kyriewen | 赞14/藏15/阅851 | 30 多个 Skill 编成 8 个岗位（需求/计划/调试/测试…），每人只碰一个环节。适合 Skill 互相打架的人。原则可抄，清单会过时。 | https://juejin.cn/post/7680043958139748406 |
| 7 | [PC 网站接入微信登录，这 10 个坑我替你踩完了！](https://juejin.cn/post/7680216488121008138) | 鹏多多 | 赞19/藏30/阅740 | PC 站微信扫码登录十坑：域名、Code 重放、Secret 见光、内嵌二维码。适合接微信 OAuth 的前端/后端。官方文档仍是准绳。 | https://juejin.cn/post/7680216488121008138 |
| 10 | [OpenAI Astra 泄露：零样本生成 3D 网页，前端开发者慌了吗？](https://juejin.cn/post/7680031642871152681) | 涛涛ing | 赞6/藏5/阅591 | 转述 Astra 泄露「零样本 3D 网页」和 Fable 5.1 同窗口。观察文，不是官方发布。泄露内容勿当产品规格。 | https://juejin.cn/post/7680031642871152681 |
| 11 | [企业级 AI Coding 的 Harness 工程实战：8 个 Skill 串起全链路](https://juejin.cn/post/7680079424891011124) | 乘风gg | 赞8/藏19/阅521 | 企业级前端 Harness：8 个 Skill 串需求到交付，针对非开发岗跟不上。适合要推团队流程而不是个人提效的人。效果来自作者项目。 | https://juejin.cn/post/7680079424891011124 |
| 13 | [技术好就能升职是前端圈最大的谎言！](https://juejin.cn/post/7680738390950510630) | ErpanOmer | 赞6/藏3/阅386 | 大厂前端晋升不只看技术深度，要可量化业务影响。职场文，少代码。适合卡职级的人。 | https://juejin.cn/post/7680738390950510630 |
| 15 | [别让 Codex 一口气写完整个前端：5 组 Skills，把页面、逻辑、测试和构建拆清楚](https://juejin.cn/post/7680500716225871910) | Dragon_xjy | 赞8/藏9/阅341 | 别让 Codex 一句话做完 Figma+接口+测试+打包；拆成短步，每步两三个 Skill 和验收物。适合额度贵还总「已经完成」的人。 | https://juejin.cn/post/7680500716225871910 |

#### 收藏热榜

本槽无新增。

### 人工智能

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 6 | [AI全栈开发最佳实践💐](https://juejin.cn/post/7680741276414296104) | 前端小张同学 | 赞17/藏16/阅1062 | 用数字分身项目讲 AI 全栈怎么开题、怎么验收。经验帖。注意别把「手写能力下降」当成方法论。 | https://juejin.cn/post/7680741276414296104 |
| 8 | [从零搭建你的 AI 编程工作流](https://juejin.cn/post/7680065840814260224) | 全栈弄潮儿 | 赞7/藏18/阅811 | 把拆需求、生成、测试、审查收成一条工作流，避免每步临时提问互相打架。适合已经单点会用、缺主流程的人。 | https://juejin.cn/post/7680065840814260224 |
| 9 | [Claude Code 插件别瞎装，这 9 款才是 2026 年的真生产力工具](https://juejin.cn/post/7680006676436025386) | ServBay | 赞11/藏13/阅629 | 筛 9 款 Claude Code 插件（环境/安全/记忆等）。清单会变，先看官方市场。ServBay 出品，略带产品味。 | https://juejin.cn/post/7680006676436025386 |
| 12 | [现在网页都能提供 MCP 了？！](https://juejin.cn/post/7680216488121303050) | ssshooter | 赞5/藏7/阅632 | 澄清 WebMCP：W3C 孵化的浏览器标准，让网页声明能力，不是把后端 MCP 塞进页面。适合做 Agent 填表的人。标准未定。 | https://juejin.cn/post/7680216488121303050 |
| 14 | [生产级 RAG 知识库全流程实践](https://juejin.cn/post/7678200303993389107) | wangfpp | 赞11/藏13/阅462 | 生产 RAG：扫描 PDF、切块截断、评测与运营，不只是「能检索」。适合要把教学 RAG 推业务的人。 | https://juejin.cn/post/7678200303993389107 |

#### 收藏热榜

本槽无新增。

### 开发工具

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 3 | [电脑合盖后 AI 工具还在偷我电？睡眠断言科普](https://juejin.cn/post/7680496681512222772) | HiSt | 赞3/藏1/阅132 | Mac 合盖掉电：睡眠断言让 AI 工具不让系统睡。科普。适合合盖掉电查 power assertions 的人。 | https://juejin.cn/post/7680496681512222772 |
| 5 | [SpringBoot Event事件机制，轻松实现业务解耦](https://juejin.cn/post/7680757400488607780) | 独泪了无痕 | 赞2/藏5/阅83 | Spring Event 不只听启动，用来做注册/支付后解耦和异步。适合想少写直接调用的人。入门向。 | https://juejin.cn/post/7680757400488607780 |
| 7 | [Python开发入门：从环境搭建到第一个实用小项目](https://juejin.cn/post/7678961254075138089) | 苏其鸿 | 赞1/藏1/阅63 | Python 环境到批量改文件小项目。纯新手。有基础可跳过。 | https://juejin.cn/post/7678961254075138089 |
| 9 | [Phosphor Icons 官网源码拆解：URL 即存储、水波动画与 7362 Star 图标库的架构实践](https://juejin.cn/post/7679451313240899630) | 王若风 | 赞0/藏1/阅83 | 拆 Phosphor Icons 官网：Zustand 把状态存 URL、fuse.js 搜索、水波动画。适合读中星标展示站的人。 | https://juejin.cn/post/7679451313240899630 |
| 10 | [react-bits：从 36K stars 的“酷炫组件”，看动效如何成为 React 的可复用能力](https://juejin.cn/post/7680766055174996011) | 吴琼琼 | 赞2/藏1/阅36 | 从 react-bits 看动效如何变成可组合组件，而不是一次性酷炫。和上一轮「怎么读仓库」 complementary。 | https://juejin.cn/post/7680766055174996011 |
| 11 | [CodeSchema 开源首发：一个给 AI 编码助手「喂」精准代码上下文的索引服务](https://juejin.cn/post/7680757400489000996) | idcu | 赞2/藏0/阅39 | CodeSchema：Go 索引服务，按 MCP/HTTP 给编码助手按需上下文。早期开源。适合被整仓塞进 prompt 的人。先看仓库成熟度。 | https://juejin.cn/post/7680757400489000996 |
| 12 | [AI Agent 成本工程实战：从 OpenAI Codex 的 8 个“烧 Token“Bug 学起](https://juejin.cn/post/7680126224085909539) | 学习星球 | 赞0/藏0/阅78 | 从 Codex 公开的 8 类烧 token bug 反推 Agent 成本控制面。适合做用量治理的人。清单日期是 8/30 官方帖，本文是复盘。 | https://juejin.cn/post/7680126224085909539 |
| 13 | [开源数据库管理工具 CloudDM 4.2.0 发布，新增 GoldenDB、KingbaseES 等数据源](https://juejin.cn/post/7680111542655189043) | ClouGence | 赞0/藏1/阅56 | CloudDM 4.2.0：加 GoldenDB/KingbaseES/Valkey/Cockroach。产品更新。适合国产库/多源管理。 | https://juejin.cn/post/7680111542655189043 |
| 14 | [Apifox 8 月更新｜调试、权限与协作体验持续优化](https://juejin.cn/post/7679974117161156618) | Apifox | 赞0/藏1/阅64 | Apifox 8 月：GHEC 数据驻留、调试与权限。产品日志，偏营销可略读。 | https://juejin.cn/post/7679974117161156618 |
| 15 | [Git 底层原理：分支为什么只是一个 41 字节的文件](https://juejin.cn/post/7679727158424109071) | 啵啵啵1234 | 赞1/藏0/阅56 | Git 分支是 41 字节文件：快照、对象库、手搓 commit。适合背命令却虚的人。 | https://juejin.cn/post/7679727158424109071 |

#### 收藏热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 15 | [只需 10 分钟，轻松实现异地组网！Netmaker 保姆级部署教程来了](https://juejin.cn/post/7659630107413446706) | GetcharZp | 赞4/藏16/阅482 | 收藏榜：Netmaker+WireGuard 异地组网。适合不想自己做端口映射的人。部署以项目文档为准。 | https://juejin.cn/post/7659630107413446706 |

### 跨榜重复与去重说明

- 本轮新摘要 URL 数：29
- 因 `seen_urls` 跳过：91（只给数量；不要把已见文再展开成表行）
- 同文多标签/双榜出现：无（本轮新 URL 均只出现在单一槽位）

### 来源清单

- 快照日：2026-09-04（Asia/Shanghai）
- 页面：https://juejin.cn/hot/articles 、 https://juejin.cn/hot/collected-articles
- 抓取：`tools/juejin_hot_fetch.py` → `_staging_latest.json`

| 标签 | 榜单 | 标题 | 链接 |
| --- | --- | --- | --- |
| 后端 | 文章热榜 | Java切面编程（AOP）详解：从核心概念到实战应用 | https://juejin.cn/post/7680496681512042548 |
| 后端 | 文章热榜 | sys_dump 备了库，角色和权限别漏在外面 | https://juejin.cn/post/7680551559094517802 |
| 后端 | 文章热榜 | 内网穿透原来这么简单：Natapp 从注册到公网访问完整教程 | https://juejin.cn/post/7680877878047408154 |
| 后端 | 文章热榜 | 换了工作流引擎，前端一行代码没改 | https://juejin.cn/post/7680094035273121802 |
| 后端 | 文章热榜 | 手机投屏到电脑，不用装任何 App，这个开源工具免费搞定：QtScrcpy | https://juejin.cn/post/7680456045867483145 |
| 后端 | 文章热榜 | 个人RAG上线翻车实录-记一次 API 延迟排查 | https://juejin.cn/post/7679458659610394674 |
| 后端 | 文章热榜 | Rust 桌面宠物拖拽踩坑实录：重影、不跟手、置顶失效 | https://juejin.cn/post/7679133086102110254 |
| 前端 | 文章热榜 | 我装了30多个Skill，给AI安排了8个岗位 | https://juejin.cn/post/7680043958139748406 |
| 前端 | 文章热榜 | PC 网站接入微信登录，这 10 个坑我替你踩完了！ | https://juejin.cn/post/7680216488121008138 |
| 前端 | 文章热榜 | OpenAI Astra 泄露：零样本生成 3D 网页，前端开发者慌了吗？ | https://juejin.cn/post/7680031642871152681 |
| 前端 | 文章热榜 | 企业级 AI Coding 的 Harness 工程实战：8 个 Skill 串起全链路 | https://juejin.cn/post/7680079424891011124 |
| 前端 | 文章热榜 | 技术好就能升职是前端圈最大的谎言！ | https://juejin.cn/post/7680738390950510630 |
| 前端 | 文章热榜 | 别让 Codex 一口气写完整个前端：5 组 Skills，把页面、逻辑、测试和构建拆清楚 | https://juejin.cn/post/7680500716225871910 |
| 人工智能 | 文章热榜 | AI全栈开发最佳实践💐 | https://juejin.cn/post/7680741276414296104 |
| 人工智能 | 文章热榜 | 从零搭建你的 AI 编程工作流 | https://juejin.cn/post/7680065840814260224 |
| 人工智能 | 文章热榜 | Claude Code 插件别瞎装，这 9 款才是 2026 年的真生产力工具 | https://juejin.cn/post/7680006676436025386 |
| 人工智能 | 文章热榜 | 现在网页都能提供 MCP 了？！ | https://juejin.cn/post/7680216488121303050 |
| 人工智能 | 文章热榜 | 生产级 RAG 知识库全流程实践 | https://juejin.cn/post/7678200303993389107 |
| 开发工具 | 文章热榜 | 电脑合盖后 AI 工具还在偷我电？睡眠断言科普 | https://juejin.cn/post/7680496681512222772 |
| 开发工具 | 文章热榜 | SpringBoot Event事件机制，轻松实现业务解耦 | https://juejin.cn/post/7680757400488607780 |
| 开发工具 | 文章热榜 | Python开发入门：从环境搭建到第一个实用小项目 | https://juejin.cn/post/7678961254075138089 |
| 开发工具 | 文章热榜 | Phosphor Icons 官网源码拆解：URL 即存储、水波动画与 7362 Star 图标库的架构实践 | https://juejin.cn/post/7679451313240899630 |
| 开发工具 | 文章热榜 | react-bits：从 36K stars 的“酷炫组件”，看动效如何成为 React 的可复用能力 | https://juejin.cn/post/7680766055174996011 |
| 开发工具 | 文章热榜 | CodeSchema 开源首发：一个给 AI 编码助手「喂」精准代码上下文的索引服务 | https://juejin.cn/post/7680757400489000996 |
| 开发工具 | 文章热榜 | AI Agent 成本工程实战：从 OpenAI Codex 的 8 个“烧 Token“Bug 学起 | https://juejin.cn/post/7680126224085909539 |
| 开发工具 | 文章热榜 | 开源数据库管理工具 CloudDM 4.2.0 发布，新增 GoldenDB、KingbaseES 等数据源 | https://juejin.cn/post/7680111542655189043 |
| 开发工具 | 文章热榜 | Apifox 8 月更新｜调试、权限与协作体验持续优化 | https://juejin.cn/post/7679974117161156618 |
| 开发工具 | 文章热榜 | Git 底层原理：分支为什么只是一个 41 字节的文件 | https://juejin.cn/post/7679727158424109071 |
| 开发工具 | 收藏热榜 | 只需 10 分钟，轻松实现异地组网！Netmaker 保姆级部署教程来了 | https://juejin.cn/post/7659630107413446706 |

## 2026-09-02

### 今日总览

**一句话结论**：`2026-09-02` 新 URL 主线是 **Redis/OpenSearch 当 AI 数据层、LangChain 入门心智、豆包工作/WeMM-Embedding/DeepSeek Harness 插件，以及 GSD vs OpenSpec vs Superpowers**；收藏榜补 FastAPI/Nginx/VS Code 部署旧文。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 文章热榜 + 收藏热榜 × 后端/前端/人工智能/开发工具 |
| 榜单规模 | 每槽最多 15 条；列表总条数 120；去重后新 URL **30**；跳过已见 **90**；详情成功 30 / 失败 0 |
| 核心趋势 | 1）后端热榜在讲「已有中间件怎么接向量/搜索」而不是再造框架；2）AI 槽是办公 Agent 测评 + 开源 embedding/Harness 插件；3）开发工具收藏榜继续吃流程 Skill 对比文 |
| 可直接关注 | [Redis 接入 AI](https://juejin.cn/post/7680014875347255334)；[LangChain 流水线](https://juejin.cn/post/7678975158596894729)；[WeMM-Embedding](https://juejin.cn/post/7680023541135507497)；[GSD vs OpenSpec vs Superpowers](https://juejin.cn/post/7653409231856877631) |

### 后端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 3 | [Redis已正式接入AI](https://juejin.cn/post/7680014875347255334) | 苏三说技术 | 赞20/藏35/阅1391 | 讲 Redis 从缓存变成 AI 实时数据层：向量搜索、Vector Sets、语义缓存、Agent 上下文。适合成熟业务里已经有 Redis、想少引一套向量库的人。偏能力地图，生产数字以官方文档为准。 | https://juejin.cn/post/7680014875347255334 |
| 7 | [为什么越来越多人用 OpenSearch？](https://juejin.cn/post/7680375814231605299) | 苏三说技术 | 赞7/藏4/阅366 | 反驳「OpenSearch 只是 ES 7.10 fork」：Linux 基金会、Apache 2.0、独立演进。适合还在 ES 许可/云厂商之间做搜索选型的人。不是性能对打评测。 | https://juejin.cn/post/7680375814231605299 |
| 8 | [别再背 Chain、Agent、Memory 了：用一条“智能流水线”学会 LangChain](https://juejin.cn/post/7678975158596894729) | Dragon_xjy | 赞2/藏4/阅341 | 用一条「智能流水线」讲 LangChain：先建立 Chain/Agent/Memory 心智，不背混乱 API。点出旧 Memory、消息历史、LangGraph 三套示例并存。适合会 Python、没正经用过 LangChain 的人。 | https://juejin.cn/post/7678975158596894729 |
| 11 | [一个博客系统，为什么要拆成 6 张表？](https://juejin.cn/post/7678157950376378383) | 烬羽 | 赞6/藏2/阅179 | 博客库拆 6 张表，重点打「点赞表联合主键上再加 postId 索引」这个新手多余索引。适合刚写 schema 的后端。案例小，原则是联合主键左前缀够用就别再加。 | https://juejin.cn/post/7678157950376378383 |
| 12 | [Nest 第一步 · 第 3 篇：理解 Controller / Service / Module 三层架构](https://juejin.cn/post/7679053043288326150) | Z思学 | 赞2/藏3/阅189 | Nest 第一步第 3 篇：Controller/Service/Module 对照前端路由/工具函数/barrel。适合从前端转 Nest 的人。系列文，要连着前两篇看。 | https://juejin.cn/post/7679053043288326150 |
| 13 | [用 AI 结对编程从 0 搭一个"单词后台管理系统"：Next.js + Supabase + Drizzle + shadcn/ui 全记录](https://juejin.cn/post/7678239521201307657) | dzhd | 赞5/藏3/阅150 | 用 Claude Code 从 0 搭单词后台：Next.js + Supabase + Drizzle + shadcn。重点写云库、ORM、密码哈希、effect 里读 localStorage。适合跟一遍全栈的人。是学习记录不是框架发布。 | https://juejin.cn/post/7678239521201307657 |
| 14 | [Claude 官方的学习教程，太强了。](https://juejin.cn/post/7680357430018949135) | cxuanAI | 赞4/藏5/阅142 | 安利 Claude Academy：按角色教怎么用好 Claude，不是新模型发布。适合要给团队找官方教程入口的人。平台内容会变，以官网为准。 | https://juejin.cn/post/7680357430018949135 |
| 15 | [一篇讲清楚Spring Boot：自动装配、启动器、过滤器、拦截器、设计模式](https://juejin.cn/post/7680043958139781174) | 吃饱了得干活 | 赞4/藏7/阅103 | 一条线串 Spring Boot：自动装配、starter、过滤器/拦截器、常见设计模式。适合停留在「加依赖就能跑」的人。综述，版本细节以当下 Boot 为准。 | https://juejin.cn/post/7680043958139781174 |

#### 收藏热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 15 | [学完 Spring Boot 再看 FastAPI，我破防了](https://juejin.cn/post/7649363408022683689) | Lucien323 | 赞56/藏54/阅6388 | 收藏榜：Spring Boot 老手看 FastAPI Hello World 的体感对比。入门安利，不是生产对打。适合两栈都要摸的人。 | https://juejin.cn/post/7649363408022683689 |

### 前端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 6 | [老板要周报？我说不用，代码提交就是进度](https://juejin.cn/post/7679985418771218470) | 阳火锅 | 赞10/藏11/阅739 | 用 git/PRD 自动出进度和周报，吐槽 Jira/禅道太重。产品向，适合被周报折磨的全栈。注意把提交当进度会鼓励碎片 commit，治理仍要人审。 | https://juejin.cn/post/7679985418771218470 |
| 8 | [登录页还在用渐变？我一口气做了 5 个能摸的背景动效：吹蒲公英、滴墨染水、点熔岩闷裂](https://juejin.cn/post/7680025405151084571) | 牧艺 | 赞8/藏10/阅649 | cos-design v3.8.0 五个可交互背景（泡泡/蒲公英/熔岩/墨染/极光），拆算法与试玩。适合活动页/登录屏要轻量动效的前端。Canvas/WebGL，注意电量和无障碍。 | https://juejin.cn/post/7680025405151084571 |
| 10 | [听说我兄弟喜欢跑车，所以必须安排上](https://juejin.cn/post/7678577086287118370) | Mh | 赞3/藏1/阅502 | Three.js 浏览器跑车 Demo，偏娱乐。适合想抄一辆能开的车模的人。不是生产组件库。 | https://juejin.cn/post/7678577086287118370 |
| 11 | [栗子前端技术周刊第 144 期 - Rspack 2.2、pnpm 12、Solid 2.0 RC...](https://juejin.cn/post/7679542577553506358) | 晓得迷路了 | 赞5/藏4/阅450 | 栗子周刊 144（8/24–8/30）：Rspack 2.2、pnpm 12、Solid 2.0 RC 等索引。适合扫一周前端发布。条目浅，点原链接。 | https://juejin.cn/post/7679542577553506358 |
| 12 | [vue3 +TypeScrpit高阶运用：让低代码的Json Schema拥有完整的类型提示](https://juejin.cn/post/7678644473824657443) | 水寒259 | 赞7/藏4/阅347 | Vue3 低代码里让 Schema 的 `componentProps` 按组件名出完整类型：条件类型/模板字面量/映射类型，绕开泛型组件偏弱。适合写 Schema 驱动表单的人。 | https://juejin.cn/post/7678644473824657443 |
| 15 | [用 Vite + Electron + React + Python 重造 3D 服装打版软件](https://juejin.cn/post/7678974488122032180) | 前端繁华如梦 | 赞4/藏6/阅411 | 把 Costumy 科研原型改成 Vite+Electron+React+Python 桌面打版：前端预览，Python 做 2D→3D。记录三个难坑。适合桌面+科学计算桥接。 | https://juejin.cn/post/7678974488122032180 |

#### 收藏热榜

本槽无新增。

### 人工智能

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 2 | [豆包工作Agent正式发布，直接给到夯。](https://juejin.cn/post/7679623224678613034) | 沉默王二 | 赞12/藏12/阅1637 | 豆包工作 Agent 实测：飞书体系、多端、云电脑、Skill、Seedance。产品测评，适合对比办公 Agent。能力以官方当前版本为准。 | https://juejin.cn/post/7679623224678613034 |
| 6 | [我用 Qwen3.8-Max 搭了一个电商商品资料包体检助手，6 份资料和 1 张商品图一次查出 27 个问题](https://juejin.cn/post/7680143535669198858) | 一只牛博 | 赞0/藏0/阅1023 | 用 Qwen3.8-Max 做电商资料包体检：多文件+图一次对型号/授权/功效证据。适合运营质检。数字来自作者样本，不要当通用准确率。 | https://juejin.cn/post/7680143535669198858 |
| 8 | [微信内部的生产级模型，居然开源了](https://juejin.cn/post/7680023541135507497) | stormzhangV | 赞9/藏9/阅623 | 介绍微信 WeMM-Embedding：生产级多模态向量、Apache 2.0、2B 打平更大模型的宣传口径。适合要图文检索/推荐的人。去 GitHub 核版本与评测表，本文是科普。 | https://juejin.cn/post/7680023541135507497 |
| 10 | [整理了一份 DeepSeek Harness 必备插件清单！](https://juejin.cn/post/7679542577553473590) | 狂师 | 赞8/藏15/阅519 | DeepSeek Harness 发布半月后的 10 个插件清单：dsh-market、视觉、侧栏、搜索等。适合已经装上 dsh、界面还是毛坯的人。插件会变，先看官方 market。 | https://juejin.cn/post/7679542577553473590 |
| 13 | [Show me your works & token -稀土掘金上线作品广场和用量统计](https://juejin.cn/post/7675992325912887315) | XCaptain | 赞6/藏2/阅480 | 掘金作品广场与用量统计：从 Show me your code 到 works/token。产品公告向。适合要曝光 AI 作品或看 token 消耗的作者。 | https://juejin.cn/post/7675992325912887315 |
| 14 | [ZCode 周末送额度活动开启：3 亿 Token 免费领取](https://juejin.cn/post/7678646261259092004) | 怕浪猫 | 赞2/藏2/阅548 | ZCode 周末送 3 亿 Token 活动说明（GLM-5.3-Flash）。偏营销，略读。额度窗口以活动页为准。 | https://juejin.cn/post/7678646261259092004 |
| 15 | [我做了一个开源项目，让 AI 记住我们解决过的问题：Usora](https://juejin.cn/post/7679020474672660526) | 彼日花 | 赞2/藏4/阅459 | 开源 Usora：把和 Codex/Claude 解过的问题沉淀成可复用 Skills，跨 Agent 共享。适合被「每次重教一遍」折磨的人。项目早期，治理/鉴权要自己看仓库。 | https://juejin.cn/post/7679020474672660526 |

#### 收藏热榜

本槽无新增。

### 开发工具

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 9 | [为什么生成了 dist，项目还是可能跑不起来？从一个 React + Express + MySQL 项目看部署闭环](https://juejin.cn/post/7680025405152608283) | BreezeJiang | 赞4/藏1/阅24 | React+Express+MySQL：有 dist 不等于能上线，要对齐前端请求、后端环境、MySQL 授权、进程。适合第一次部署全栈的人。命令来自作者项目，运行未验证。 | https://juejin.cn/post/7680025405152608283 |
| 12 | [36K stars 之外：如何阅读 react-bits 这样的动画交互式 React 项目](https://juejin.cn/post/7679542577527291958) | 吴琼琼 | 赞2/藏1/阅49 | 怎么读 36K star 的 react-bits：当「动画交互组件」而不是直接当业务库。适合想从展示型仓学组织方式的人。 | https://juejin.cn/post/7679542577527291958 |
| 13 | [我用AI拆解了Charles的授权机制，发现密钥被写死在了代码里](https://juejin.cn/post/7678520027876835355) | toolsmith | 赞0/藏0/阅90 | 用 AI 辅助分析 Charles 授权：混淆代码里发现硬编码密钥，复盘方法而不是给破解步骤。适合做安全意识/授权设计的人。不要用来绕过授权。 | https://juejin.cn/post/7678520027876835355 |
| 14 | [一个 1.7 万 Star 的开源项目，教我们怎么判断 AI 工具值不值得用](https://juejin.cn/post/7678240005149687817) | 苏灿烤鱼 | 赞1/藏0/阅72 | 介绍高星开源：让编码 Agent 根据仓库画出可点、可查、可导出的架构图，一行命令。适合评估「AI 画架构图」值不值得装。输出仍要人审。 | https://juejin.cn/post/7678240005149687817 |
| 15 | [Docker 部署 Calibre-Web：轻松搭建网页版电子书管理平台](https://juejin.cn/post/7677859417393053696) | 程序员老赵 | 赞0/藏1/阅87 | Docker 部署 Calibre-Web 0.6.27 做网页书房，打通多端书库。适合自托管电子书。注意映射书库卷和用户权限。 | https://juejin.cn/post/7677859417393053696 |

#### 收藏热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 12 | [入坑 Nginx，看这一篇就够了](https://juejin.cn/post/7669003422981619753) | 驳是 | 赞9/藏20/阅583 | 收藏榜：Nginx 入门（反代、静态、常见指令）。适合第一次碰网关的人。配置以当前稳定版文档为准。 | https://juejin.cn/post/7669003422981619753 |
| 14 | [在 VSCode 里，把项目一键部署到服务器](https://juejin.cn/post/7667465942311829555) | 前端之虎陈随易 | 赞13/藏18/阅771 | 收藏榜：VS Code「简单部署」扩展，少开终端/SFTP 传 dist。适合多项目重复发布的前端。传错目录/覆盖配置仍要自己防。 | https://juejin.cn/post/7667465942311829555 |
| 15 | [三大 AI 编码框架深度对比：GSD vs OpenSpec vs Superpowers](https://juejin.cn/post/7653409231856877631) | 白小纯2025 | 赞8/藏16/阅988 | 收藏榜：GSD vs OpenSpec vs Superpowers，对比 spec-driven / 上下文工程，反对纯 vibe coding。适合要给仓库选一套流程 Skill 的人。版本会变，先看各仓 README。 | https://juejin.cn/post/7653409231856877631 |

### 跨榜重复与去重说明

- 本轮新摘要 URL 数：30
- 因 `seen_urls` 跳过：90（只给数量；不要把已见文再展开成表行）
- 同文多标签/双榜出现：无（本轮新 URL 均只出现在单一槽位）

### 来源清单

- 快照日：2026-09-02（Asia/Shanghai）
- 页面：https://juejin.cn/hot/articles 、 https://juejin.cn/hot/collected-articles
- 抓取：`tools/juejin_hot_fetch.py` → `_staging_latest.json`

| 标签 | 榜单 | 标题 | 链接 |
| --- | --- | --- | --- |
| 后端 | 文章热榜 | Redis已正式接入AI | https://juejin.cn/post/7680014875347255334 |
| 后端 | 文章热榜 | 为什么越来越多人用 OpenSearch？ | https://juejin.cn/post/7680375814231605299 |
| 后端 | 文章热榜 | 别再背 Chain、Agent、Memory 了：用一条“智能流水线”学会 LangChain | https://juejin.cn/post/7678975158596894729 |
| 后端 | 文章热榜 | 一个博客系统，为什么要拆成 6 张表？ | https://juejin.cn/post/7678157950376378383 |
| 后端 | 文章热榜 | Nest 第一步 · 第 3 篇：理解 Controller / Service / Module 三层架构 | https://juejin.cn/post/7679053043288326150 |
| 后端 | 文章热榜 | 用 AI 结对编程从 0 搭一个"单词后台管理系统"：Next.js + Supabase + Drizzle + shadcn/ui 全记录 | https://juejin.cn/post/7678239521201307657 |
| 后端 | 文章热榜 | Claude 官方的学习教程，太强了。 | https://juejin.cn/post/7680357430018949135 |
| 后端 | 文章热榜 | 一篇讲清楚Spring Boot：自动装配、启动器、过滤器、拦截器、设计模式 | https://juejin.cn/post/7680043958139781174 |
| 前端 | 文章热榜 | 老板要周报？我说不用，代码提交就是进度 | https://juejin.cn/post/7679985418771218470 |
| 前端 | 文章热榜 | 登录页还在用渐变？我一口气做了 5 个能摸的背景动效：吹蒲公英、滴墨染水、点熔岩闷裂 | https://juejin.cn/post/7680025405151084571 |
| 前端 | 文章热榜 | 听说我兄弟喜欢跑车，所以必须安排上 | https://juejin.cn/post/7678577086287118370 |
| 前端 | 文章热榜 | 栗子前端技术周刊第 144 期 - Rspack 2.2、pnpm 12、Solid 2.0 RC... | https://juejin.cn/post/7679542577553506358 |
| 前端 | 文章热榜 | vue3 +TypeScrpit高阶运用：让低代码的Json Schema拥有完整的类型提示 | https://juejin.cn/post/7678644473824657443 |
| 前端 | 文章热榜 | 用 Vite + Electron + React + Python 重造 3D 服装打版软件 | https://juejin.cn/post/7678974488122032180 |
| 人工智能 | 文章热榜 | 豆包工作Agent正式发布，直接给到夯。 | https://juejin.cn/post/7679623224678613034 |
| 人工智能 | 文章热榜 | 我用 Qwen3.8-Max 搭了一个电商商品资料包体检助手，6 份资料和 1 张商品图一次查出 27 个问题 | https://juejin.cn/post/7680143535669198858 |
| 人工智能 | 文章热榜 | 微信内部的生产级模型，居然开源了 | https://juejin.cn/post/7680023541135507497 |
| 人工智能 | 文章热榜 | 整理了一份 DeepSeek Harness 必备插件清单！ | https://juejin.cn/post/7679542577553473590 |
| 人工智能 | 文章热榜 | Show me your works & token -稀土掘金上线作品广场和用量统计 | https://juejin.cn/post/7675992325912887315 |
| 人工智能 | 文章热榜 | ZCode 周末送额度活动开启：3 亿 Token 免费领取 | https://juejin.cn/post/7678646261259092004 |
| 人工智能 | 文章热榜 | 我做了一个开源项目，让 AI 记住我们解决过的问题：Usora | https://juejin.cn/post/7679020474672660526 |
| 开发工具 | 文章热榜 | 为什么生成了 dist，项目还是可能跑不起来？从一个 React + Express + MySQL 项目看部署闭环 | https://juejin.cn/post/7680025405152608283 |
| 开发工具 | 文章热榜 | 36K stars 之外：如何阅读 react-bits 这样的动画交互式 React 项目 | https://juejin.cn/post/7679542577527291958 |
| 开发工具 | 文章热榜 | 我用AI拆解了Charles的授权机制，发现密钥被写死在了代码里 | https://juejin.cn/post/7678520027876835355 |
| 开发工具 | 文章热榜 | 一个 1.7 万 Star 的开源项目，教我们怎么判断 AI 工具值不值得用 | https://juejin.cn/post/7678240005149687817 |
| 开发工具 | 文章热榜 | Docker 部署 Calibre-Web：轻松搭建网页版电子书管理平台 | https://juejin.cn/post/7677859417393053696 |
| 后端 | 收藏热榜 | 学完 Spring Boot 再看 FastAPI，我破防了 | https://juejin.cn/post/7649363408022683689 |
| 开发工具 | 收藏热榜 | 入坑 Nginx，看这一篇就够了 | https://juejin.cn/post/7669003422981619753 |
| 开发工具 | 收藏热榜 | 在 VSCode 里，把项目一键部署到服务器 | https://juejin.cn/post/7667465942311829555 |
| 开发工具 | 收藏热榜 | 三大 AI 编码框架深度对比：GSD vs OpenSpec vs Superpowers | https://juejin.cn/post/7653409231856877631 |

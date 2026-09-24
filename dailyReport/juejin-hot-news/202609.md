# Juejin Hot Digest

按 Asia/Shanghai 时区汇总掘金文章热榜与收藏热榜（后端 / 前端 / 人工智能 / 开发工具），按文章链接去重并归纳正文。

## 2026-09-24

### 今日总览

**一句话结论**：`2026-09-24` 新 URL 主线是 **多租户校验与分布式 SQL 对照**，人工智能槽补 **Jev 用法与三进制本地模型**，开发工具槽是 Cursor/Claude Code 入门与 Trae 接 Jev。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 文章热榜 + 收藏热榜 × 后端/前端/人工智能/开发工具 |
| 榜单规模 | 列表 120；新 URL **11**；跳过已见 **109**；详情成功 11 / 失败 0 |
| 核心趋势 | 1）后端热榜抬头是数据隔离与复杂 SQL 路径；2）Jev 仍在跨标签扩散；3）开发工具以教程连载为主 |
| 可直接关注 | [ValidX 多租户](https://juejin.cn/post/7688298824980987919)；[PI Harness](https://juejin.cn/post/7686462220679594034)；[Jev 讲透](https://juejin.cn/post/7688238990706016283) |

### 后端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 1 | [ValidX 多租户系统的数据验证方案](https://juejin.cn/post/7688298824980987919) | vipxieliang | 赞2/藏2/阅11877 | 把多租户当成校验问题：共享/隔离模式、租户 ID 权限、Service 层守门、跨租户边界和 SaaS 用户模块示例。 | https://juejin.cn/post/7688298824980987919 |
| 9 | [OceanBase VS 金仓：同一组复杂 SQL](https://juejin.cn/post/7688300268688572442) | 一只牛博 | 赞0/藏1/阅746 | 用同一条报表 SQL 对照分布式分区路由与集中式共享存储，延迟差在跨节点取数和中间聚合，不拿无环境的耗时排座次。 | https://juejin.cn/post/7688300268688572442 |

#### 收藏热榜

本槽无新增。

### 前端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 14 | [网页端 40MB 离线模型自动抠图](https://juejin.cn/post/7686043275371282466) | 半刻维度 | 赞10/藏16/阅459 | 浏览器内抠图，不依赖 Python/GPU/API。作者在老机器上约 8 秒一张，模型约 40MB。 | https://juejin.cn/post/7686043275371282466 |
| 15 | [把 Agent 框架拆开：PI 开发生产级 Harness](https://juejin.cn/post/7686462220679594034) | 65岁退休Coder | 赞6/藏9/阅465 | `pi-ai` 管模型与协议，`pi-agent-core` 管 loop、session、tool、skill。对照 LangChain/LangGraph 的职责表。 | https://juejin.cn/post/7686462220679594034 |

#### 收藏热榜

本槽无新增。

### 人工智能

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 13 | [最近全网爆火的 Jev 到底是什么](https://juejin.cn/post/7688238990706016283) | 狂师 | 赞13/藏12/阅607 | 面向测试开发：Jev 做结构化判断（紧急度、分流），不替代生成模型；文中日期与官方 9/15 发布略有出入，以厂商公告为准。 | https://juejin.cn/post/7688238990706016283 |
| 15 | [16GB 显卡跑 Qwen3.8-27B，只要 7GB](https://juejin.cn/post/7687509634027831348) | 雪隐_上班了 | 赞4/藏4/阅753 | 三进制权重把 27B 压到约 7GB，并对比两种 GGUF 打包。效果数字来自作者转述，部署前看仓库实测。 | https://juejin.cn/post/7687509634027831348 |

#### 收藏热榜

本槽无新增。

### 开发工具

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 6 | [看不懂的装修图纸，豆包 2.1 Pro 变成 3D](https://juejin.cn/post/7687995393330561078) | 倔强的石头_ | 赞1/藏1/阅245 | 把平面/剖面施工图交给多模态模型生成可走进的 3D。偏生活演示，不是工程框架。 | https://juejin.cn/post/7687995393330561078 |
| 12 | [02# Cursor 实战：从安装到 Agent 模式](https://juejin.cn/post/7686078320400056358) | 东方红杉 | 赞0/藏1/阅162 | 连载：装 Cursor、配 Rules、三种交互，最后用 Agent 写任务卡片。免费额度以官网为准。 | https://juejin.cn/post/7686078320400056358 |
| 13 | [Jev 是什么？如何在 TraeCode 中使用](https://juejin.cn/post/7688018731444584457) | TRAE_ai | 赞1/藏2/阅131 | 用客服分流说明「要数字不要作文」，并接到 TraeCode。产品向介绍。 | https://juejin.cn/post/7688018731444584457 |
| 14 | [03# Claude Code 实战：终端里的逻辑引擎](https://juejin.cn/post/7686472562256805926) | 东方红杉 | 赞1/藏1/阅134 | 用 Claude Code 写后端 API，强调终端命令与 `AGENTS.md` 记住项目状态。入门向。 | https://juejin.cn/post/7686472562256805926 |
| 15 | [Git 学习指南：从日常命令到多人协作](https://juejin.cn/post/7686472562230444042) | 为你学会写情书 | 赞3/藏2/阅86 | 工作区/暂存区/提交与 Conventional Commits 速查，无 AI 增量。 | https://juejin.cn/post/7686472562230444042 |

#### 收藏热榜

本槽无新增。

### 跨榜重复与去重说明

- 本轮新摘要 URL 数：11
- 因 `seen_urls` 跳过：109
- 同文多标签/双榜出现：无（11 条各只出现在一个槽位）

### 来源清单

- 快照日：2026-09-24（Asia/Shanghai）
- 页面：https://juejin.cn/hot/articles 、 https://juejin.cn/hot/collected-articles
- 抓取：`tools/juejin_hot_fetch.py` → `_staging_latest.json`

| 标签 | 榜单 | 标题 | 链接 |
| --- | --- | --- | --- |
| 后端 | 文章热榜 | ValidX 多租户验证 | https://juejin.cn/post/7688298824980987919 |
| 后端 | 文章热榜 | OceanBase VS 金仓 | https://juejin.cn/post/7688300268688572442 |
| 前端 | 文章热榜 | 40MB 离线抠图 | https://juejin.cn/post/7686043275371282466 |
| 前端 | 文章热榜 | PI 生产级 Harness | https://juejin.cn/post/7686462220679594034 |
| 人工智能 | 文章热榜 | Jev 讲透 | https://juejin.cn/post/7688238990706016283 |
| 人工智能 | 文章热榜 | Bonsai 2 部署 | https://juejin.cn/post/7687509634027831348 |
| 开发工具 | 文章热榜 | 豆包装修 3D | https://juejin.cn/post/7687995393330561078 |
| 开发工具 | 文章热榜 | Cursor 实战 02 | https://juejin.cn/post/7686078320400056358 |
| 开发工具 | 文章热榜 | TraeCode 用 Jev | https://juejin.cn/post/7688018731444584457 |
| 开发工具 | 文章热榜 | Claude Code 实战 03 | https://juejin.cn/post/7686472562256805926 |
| 开发工具 | 文章热榜 | Git 学习指南 | https://juejin.cn/post/7686472562230444042 |

## 2026-09-23

### 今日总览

**一句话结论**：`2026-09-23` 新 URL 主线是 **Jev 正反辩论**、**ZCode 开源后的证据链质疑**，前端补像素/StyleX，后端补 Spring AI RAG 与学习方法。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 文章热榜 + 收藏热榜 × 后端/前端/人工智能/开发工具 |
| 榜单规模 | 列表 120；新 URL **17**；跳过已见 **103**；详情成功 17 / 失败 0 |
| 核心趋势 | 1）Jev 从安利转入「别吹」；2）ZCode 开源仍回答不了历史是否上传；3）收藏榜回看 AI 面试能力 |
| 可直接关注 | [别吹 Jev](https://juejin.cn/post/7687793891199418374)；[ZCode 开源 24h](https://juejin.cn/post/7688252916676231168)；[Spring AI RAG](https://juejin.cn/post/7687176748632293419) |

### 后端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 10 | [聊聊我的AI学习方法与思考！](https://juejin.cn/post/7687505412876075008) | 程序员飞鱼 | 赞17/藏1/阅226 | 主张「干中学」：提示词模板过时，真实项目里把需求说清楚比堆模板更有效；工具半衰期短，要靠落地反馈。 | https://juejin.cn/post/7687505412876075008 |
| 14 | [从零到一跑通苍穹外卖：一个大二学生的暑假项目复盘](https://juejin.cn/post/7686376405304344628) | 飞虹地星海 | 赞6/藏6/阅253 | JDK17+SpringBoot3+Redis+Nginx 跟做苍穹外卖；写清 AI 能加速环境/代码，但调试与业务理解仍靠手写。 | https://juejin.cn/post/7686376405304344628 |
| 15 | [知识库已经有了，Java 程序员还要做什么？Spring AI RAG 实战](https://juejin.cn/post/7687176748632293419) | 杨杨杨大侠 | 赞5/藏5/阅234 | 基于 Spring AI 2.0.1：对齐 Embedding、租户/权限过滤、召回阈值、拒答、引用与 token/耗时记录。1.x API 不兼容。 | https://juejin.cn/post/7687176748632293419 |

#### 收藏热榜

本槽无新增。

### 前端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 6 | [为什么死磕 1px 的团队，用户体验反而更差？](https://juejin.cn/post/7687972882228461609) | ErpanOmer | 赞21/藏10/阅1071 | 多设备 DPR/宽度下像素级还原不可实现；主张弹性约束，把时间留给性能与体验。 | https://juejin.cn/post/7687972882228461609 |
| 8 | [上线 24 小时，13% 的付费团队连夜换到 Jev](https://juejin.cn/post/7687855879103021108) | 秋天的一阵风 | 赞6/藏6/阅1429 | 转述 TypeSafe/Jev 与 Vercel Gateway 首日采用；定位「不说话」的结构化决策，非聊天模型。 | https://juejin.cn/post/7687855879103021108 |
| 13 | [Sass 和 Less 在 2026 年彻底多余了吗？](https://juejin.cn/post/7687521521468325929) | ErpanOmer | 赞5/藏5/阅649 | 变量/嵌套/颜色函数已被原生 CSS 覆盖；Mixin/循环仍无平替，新项目可优先原生。 | https://juejin.cn/post/7687521521468325929 |
| 14 | [React 19.3 发布，但真正的赢家是 StyleX](https://juejin.cn/post/7686769981477814313) | 涛涛ing | 赞8/藏8/阅626 | React 19.3 视图过渡稳定；文称 Linear/Cursor 迁 StyleX，理由是 Agent 更能读懂约束样式。 | https://juejin.cn/post/7686769981477814313 |

#### 收藏热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 15 | [我扒了最近的前端面经——2026年面试不背八股文了，考这5样](https://juejin.cn/post/7664799547449835558) | kyriewen | 赞46/藏84/阅3508 | 7 月旧文上收藏榜：现场用 AI 解题、审 AI 代码、拆需求、讲踩坑、保证可上线。 | https://juejin.cn/post/7664799547449835558 |

### 人工智能

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 8 | [Jev是什么？哑巴模型居然全网爆火](https://juejin.cn/post/7687630544474701870) | ServBay | 赞18/藏10/阅1464 | 用「业务要判断不要小作文」解释 Jev：结构化决策、低延迟，对照 LLM 幻觉与吹捧。 | https://juejin.cn/post/7687630544474701870 |
| 11 | [别吹 Jev 了](https://juejin.cn/post/7687793891199418374) | stormzhangV | 赞14/藏2/阅994 | 认为爆点是 token 贵和慢，不是新范式；适合工单分流/护栏，不能当通用 Agent。 | https://juejin.cn/post/7687793891199418374 |
| 13 | [为什么全世界的 AI 都画不好一只骑自行车的鹈鹕](https://juejin.cn/post/7687439830713417737) | 犀利豆 | 赞9/藏3/阅797 | 以 Willison 鹈鹕 SVG 题回看两年多模态空间关系，仍是直观尺子。 | https://juejin.cn/post/7687439830713417737 |
| 14 | [Jev 入门第一课](https://juejin.cn/post/7686925590315696138) | XiaoLei_Liu | 赞3/藏8/阅823 | 对照 LLM：输出接口、并行 Schema、无自然语言；当业务流里的判断函数。 | https://juejin.cn/post/7686925590315696138 |
| 15 | [DeepSeek V4.1 Flash，等等，为什么现在大家都在卷 Flash？](https://juejin.cn/post/7687537292214501412) | RockByte | 赞8/藏1/阅546 | 梳理 2026 各家 Flash：高并发便宜档，复杂长循环仍建议 Max。 | https://juejin.cn/post/7687537292214501412 |

#### 收藏热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 14 | [天天 AI Coding 的你，如果出去面试，你的竞争力是什么？](https://juejin.cn/post/7670094721701445672) | Coffeeee | 赞78/藏83/阅10904 | 8 月旧文：嘲「全交给 AI」后，面试考的是审代码、定位与上线责任。 | https://juejin.cn/post/7670094721701445672 |

### 开发工具

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 5 | [ZCode 开源 24 小时：一份没有历史的账本](https://juejin.cn/post/7688252916676231168) | 勇宝趣学前端 | 赞4/藏0/阅223 | 9/21 开源 zai-org/ZCode 后社区质疑：仓库证明不了历史上传包内容；危机响应快不等于免责。 | https://juejin.cn/post/7688252916676231168 |
| 14 | [GitHub 日榜趋势速报 \| 2026-09-22](https://juejin.cn/post/7687818534404210738) | miofly | 赞1/藏0/阅133 | 聚合 9/22 Star 增量：laya、jev-ultrafast 等决策/浏览器代理相关仓。 | https://juejin.cn/post/7687818534404210738 |
| 15 | [从 0 到百万级关注：我用 TraeCode 做了一款大学生求职应用](https://juejin.cn/post/7686674237757407270) | TRAE_ai | 赞1/藏0/阅140 | FResume Web+插件：强调 AI 编程应把人推向真正值得想的产品问题。偏案例。 | https://juejin.cn/post/7686674237757407270 |

#### 收藏热榜

本槽无新增。

### 跨榜重复与去重说明

- 本轮新摘要 URL 数：17
- 因 `seen_urls` 跳过：103（只给数量；不要把已见文再展开成表行）
- 同文多标签/双榜出现：无（17 条各只出现在一个槽位）

### 来源清单

- 快照日：2026-09-23（Asia/Shanghai）
- 页面：https://juejin.cn/hot/articles 、 https://juejin.cn/hot/collected-articles
- 抓取：`tools/juejin_hot_fetch.py` → `_staging_latest.json`

| 标签 | 榜单 | 标题 | 链接 |
| --- | --- | --- | --- |
| 后端 | 文章热榜 | 聊聊我的AI学习方法与思考！ | https://juejin.cn/post/7687505412876075008 |
| 后端 | 文章热榜 | 从零到一跑通苍穹外卖 | https://juejin.cn/post/7686376405304344628 |
| 后端 | 文章热榜 | Spring AI RAG 实战 | https://juejin.cn/post/7687176748632293419 |
| 前端 | 文章热榜 | 为什么死磕 1px | https://juejin.cn/post/7687972882228461609 |
| 前端 | 文章热榜 | 13% 付费团队换到 Jev | https://juejin.cn/post/7687855879103021108 |
| 前端 | 文章热榜 | Sass 和 Less 还多余吗 | https://juejin.cn/post/7687521521468325929 |
| 前端 | 文章热榜 | React 19.3 与 StyleX | https://juejin.cn/post/7686769981477814313 |
| 前端 | 收藏热榜 | 2026 前端面经五维度 | https://juejin.cn/post/7664799547449835558 |
| 人工智能 | 文章热榜 | Jev 是什么 | https://juejin.cn/post/7687630544474701870 |
| 人工智能 | 文章热榜 | 别吹 Jev 了 | https://juejin.cn/post/7687793891199418374 |
| 人工智能 | 文章热榜 | 骑自行车的鹈鹕 | https://juejin.cn/post/7687439830713417737 |
| 人工智能 | 文章热榜 | Jev 入门第一课 | https://juejin.cn/post/7686925590315696138 |
| 人工智能 | 文章热榜 | 为什么都在卷 Flash | https://juejin.cn/post/7687537292214501412 |
| 人工智能 | 收藏热榜 | AI Coding 面试竞争力 | https://juejin.cn/post/7670094721701445672 |
| 开发工具 | 文章热榜 | ZCode 开源 24 小时 | https://juejin.cn/post/7688252916676231168 |
| 开发工具 | 文章热榜 | GitHub 日榜 2026-09-22 | https://juejin.cn/post/7687818534404210738 |
| 开发工具 | 文章热榜 | TraeCode 求职应用 | https://juejin.cn/post/7686674237757407270 |

## 2026-09-22

### 今日总览

**一句话结论**：`2026-09-22` 新 URL 主线是 **ZCode 信任危机与 JEV/框架选型**、**Qwen/AgentScope 实践**，开发工具槽补 Hypit 与 XXL-JOB Docker。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 文章热榜 + 收藏热榜 × 后端/前端/人工智能/开发工具 |
| 榜单规模 | 列表 120；新 URL **16**；跳过已见 **104**；详情成功 16 / 失败 0 |
| 核心趋势 | 1）Java AI 框架选型热；2）Agent IDE 上传 .git 成 AI 榜头条；3）JEV 结构化决策持续发酵 |
| 可直接关注 | [ZCode 复盘](https://juejin.cn/post/7687441604429692955)；[框架选型](https://juejin.cn/post/7687440193649033222)；[JEV 实战](https://juejin.cn/post/7686808742222856211) |

### 后端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 8 | [Spring AI、LangChain4j、AgentScope、Embabel，哪个AI框架更好？](https://juejin.cn/post/7687440193649033222) | 作者见文 | 赞10/藏13/阅521 | 智能客服立项：四人争论 Spring AI 官方稳、LangChain4j 灵活、AgentScope 阿里系等；对比 Embabel，给选型维度而非结论。 | https://juejin.cn/post/7687440193649033222 |
| 10 | [为什么最近开始关注 JEV？几个实战案例告诉你答案](https://juejin.cn/post/7686808742222856211) | 作者见文 | 赞9/藏4/阅564 | JEV 做路由/RAG 排序/代码审查/风险判断等结构化决策，非文本生成；与 TypeSafe System One 叙事一致。 | https://juejin.cn/post/7686808742222856211 |
| 11 | [推荐一个牛逼的AgentScope系统](https://juejin.cn/post/7687438959296413732) | 苏三 | 赞7/藏8/阅407 | 基于 AgentScope 的多 Agent 企业招聘系统；作者系列第 14 个 SpringBoot/AI 项目之一。 | https://juejin.cn/post/7687438959296413732 |
| 15 | [弃用 ZCode，转 DeepSeek Harness：GitHub Actions 自建 Windows 打包](https://juejin.cn/post/7686780705862582278) | 作者见文 | 赞1/藏3/阅361 | ZCode 静默上传实锤后改 DSH；无官方 Windows 包则 fork 用 Actions 打 .exe，浏览器操作实录。 | https://juejin.cn/post/7686780705862582278 |

#### 收藏热榜

本槽无新增。

### 前端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 10 | [2026年9月，前端圈同时发生了四件事](https://juejin.cn/post/7687443714885959699) | 作者见文 | 赞12/藏8/阅1024 | ES2026 Temporal、Tailwind/Shopify、Lynx-for-AI、WeaveFox 等四线汇总，指向前端为 Agent 服务。 | https://juejin.cn/post/7687443714885959699 |
| 14 | [从 0 到 1，记录我的第一个出海 SaaS](https://juejin.cn/post/7687457196955631657) | 作者见文 | 赞17/藏8/阅344 | 独立开发者出海：万事达卡、域名、工具站冷启动；非 AI 专文。 | https://juejin.cn/post/7687457196955631657 |
| 15 | [这个小程序是 AI 帮我写的，可它里面一个 AI 功能都没有](https://juejin.cn/post/7686699741968400430) | 作者见文 | 赞6/藏3/阅474 | 厨菜记小程序：家庭私有菜单，无推荐流；AI 辅助开发但产品本身不做 AI 功能。 | https://juejin.cn/post/7686699741968400430 |

#### 收藏热榜

本槽无新增。

### 人工智能

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 4 | [智谱 ZCode 静默上传 Git 历史：48 小时信任危机复盘](https://juejin.cn/post/7687441604429692955) | 作者见文 | 赞19/藏8/阅2086 | ferstar 发现 ~/.zcode 313MB 加密包与状态文件；披露本地商业项目 Git 历史被上传 OSS 的时间线。 | https://juejin.cn/post/7687441604429692955 |
| 7 | [本地图库语义搜索实战：接上蓝耘元生代](https://juejin.cn/post/7687331138987196425) | 作者见文 | 赞5/藏2/阅1880 | 本地图库用多模态 embedding 做「傍晚海边」类语义搜图；工程向 RAG/视觉检索。 | https://juejin.cn/post/7687331138987196425 |
| 13 | [WorkBuddy 最值得落地的 10 个技能](https://juejin.cn/post/7686407614478893108) | 作者见文 | 赞8/藏14/阅676 | Java 后端向：springboot-scaffold、code-review、mcp-builder、TDD 等 skill 清单。 | https://juejin.cn/post/7686407614478893108 |
| 14 | [【AI+Gpt-Image2.5】虚拟角色](https://juejin.cn/post/7685701789799022602) | 作者见文 | 赞7/藏6/阅526 | 图像生成趣味实践；偏创意非工程框架。 | https://juejin.cn/post/7685701789799022602 |
| 15 | [AI越来越强了，为什么测试人反而越来越累](https://juejin.cn/post/7686408837754748978) | 作者见文 | 赞10/藏10/阅474 | AI 提效研发但测试成瓶颈；「迎合 vs 挑刺」与验证难以线性扩展。 | https://juejin.cn/post/7686408837754748978 |

#### 收藏热榜

本槽无新增。

### 开发工具

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 7 | [一行命令复刻爆款视频，Hypit 从安装到出片](https://juejin.cn/post/7687521521469440041) | 怕浪猫 | 赞4/藏2/阅153 | Hypit CLI 复刻短视频广告结构；9/17 文，热榜传播。 | https://juejin.cn/post/7687521521469440041 |
| 11 | [Docker 部署 XXL-JOB 3.4.2](https://juejin.cn/post/7686043275372183586) | 作者见文 | 赞1/藏3/阅140 | 分布式任务调度 Docker 部署教程；无 AI 增量。 | https://juejin.cn/post/7686043275372183586 |
| 14 | [Wails v2 + Go + Vue3 架构约定编译成会变红的测试](https://juejin.cn/post/7686798164308279330) | 作者见文 | 赞2/藏1/阅86 | 把 ARCH 规范变成失败即红的测试，防止脚手架文档腐烂。 | https://juejin.cn/post/7686798164308279330 |
| 15 | [如何用 TraeCode 构建个人知识库 Wiki](https://juejin.cn/post/7686674237757898790) | 作者见文 | 赞1/藏0/阅139 | LLM Wiki：人策展、LLM 维护摘要与交叉引用；个人知识库模式。 | https://juejin.cn/post/7686674237757898790 |

#### 收藏热榜

本槽无新增。

### 跨榜重复与去重说明

- 本轮新摘要 URL 数：16
- 因 `seen_urls` 跳过：104
- 同文多榜：本轮均单槽

### 来源清单

- 快照日：2026-09-22（Asia/Shanghai）
- 页面：https://juejin.cn/hot/articles 、 https://juejin.cn/hot/collected-articles

| 标签 | 榜单 | 标题 | 链接 |
| --- | --- | --- | --- |
| 后端 | 文章热榜 | Spring AI、LangChain4j、AgentScope、Embabel，哪个AI框架更好？ | https://juejin.cn/post/7687440193649033222 |
| 后端 | 文章热榜 | 为什么最近开始关注 JEV？几个实战案例告诉你答案 | https://juejin.cn/post/7686808742222856211 |
| 后端 | 文章热榜 | 推荐一个牛逼的AgentScope系统 | https://juejin.cn/post/7687438959296413732 |
| 后端 | 文章热榜 | 弃用 ZCode，转 DeepSeek Harness：GitHub Actions 自建 Windows 打包 | https://juejin.cn/post/7686780705862582278 |
| 前端 | 文章热榜 | 2026年9月，前端圈同时发生了四件事 | https://juejin.cn/post/7687443714885959699 |
| 前端 | 文章热榜 | 从 0 到 1，记录我的第一个出海 SaaS | https://juejin.cn/post/7687457196955631657 |
| 前端 | 文章热榜 | 这个小程序是 AI 帮我写的，可它里面一个 AI 功能都没有 | https://juejin.cn/post/7686699741968400430 |
| 人工智能 | 文章热榜 | 智谱 ZCode 静默上传 Git 历史：48 小时信任危机复盘 | https://juejin.cn/post/7687441604429692955 |
| 人工智能 | 文章热榜 | 本地图库语义搜索实战：接上蓝耘元生代 | https://juejin.cn/post/7687331138987196425 |
| 人工智能 | 文章热榜 | WorkBuddy 最值得落地的 10 个技能 | https://juejin.cn/post/7686407614478893108 |
| 人工智能 | 文章热榜 | 【AI+Gpt-Image2.5】虚拟角色 | https://juejin.cn/post/7685701789799022602 |
| 人工智能 | 文章热榜 | AI越来越强了，为什么测试人反而越来越累 | https://juejin.cn/post/7686408837754748978 |
| 开发工具 | 文章热榜 | 一行命令复刻爆款视频，Hypit 从安装到出片 | https://juejin.cn/post/7687521521469440041 |
| 开发工具 | 文章热榜 | Docker 部署 XXL-JOB 3.4.2 | https://juejin.cn/post/7686043275372183586 |
| 开发工具 | 文章热榜 | Wails v2 + Go + Vue3 架构约定编译成会变红的测试 | https://juejin.cn/post/7686798164308279330 |
| 开发工具 | 文章热榜 | 如何用 TraeCode 构建个人知识库 Wiki | https://juejin.cn/post/7686674237757898790 |

## 2026-09-21

### 今日总览

**一句话结论**：`2026-09-21` 新 URL 主线是 **RAG 管道系列爆热**、**NeoHorse-1/ Lynx-for-AI** 与 **Agent IDE 供应链（ZCode）**，后端槽补单表恢复与 Canvas 游戏。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 文章热榜 + 收藏热榜 × 后端/前端/人工智能/开发工具 |
| 榜单规模 | 每槽最多 15 条；列表总条数 120；去重后新 URL **15**；跳过已见 **105**；详情成功 15 / 失败 0 |
| 核心趋势 | 1）RAG/框架-for-AI 长文占前端榜；2）安全从模型转向客户端静默上传；3）老 Skill 文首次进入热榜 |
| 可直接关注 | [RAG 第四篇](https://juejin.cn/post/7687422041256689691)；[ZCode 逆向](https://juejin.cn/post/7686534839903535144)；[NeoHorse-1](https://juejin.cn/post/7686341072615948326) |

### 后端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 10 | [只恢复一张表，别把整个库都还回去](https://juejin.cn/post/7687439830713237513) | vipxieliang | 赞1/藏0/阅719 | 单表误删/误改时用 binlog 或备份只还原一张表，避免全库 PITR。偏 DBA 实操。 | https://juejin.cn/post/7687439830713237513 |
| 13 | [真没想到，AI 圈又杀出来一匹黑马！](https://juejin.cn/post/7686341072615948326) | 作者见文 | 赞3/藏3/阅429 | 介绍 NeoHorse-1：Harness+Agentic Routing 记录调用轨迹，筛成后训练数据，探索 RSI 工程路径；4B 赛道评测叙事。 | https://juejin.cn/post/7686341072615948326 |
| 14 | [为什么 AI 写代码时，总喜欢“防御性编程”？](https://juejin.cn/post/7686396501736357951) | 作者见文 | 赞5/藏3/阅308 | 简单方法被 AI 堆满判空/校验/重试；讨论 prompt 与 review 如何约束过度防御。 | https://juejin.cn/post/7686396501736357951 |
| 15 | [不用游戏引擎，用 Canvas 2D 做搜打撤游戏](https://juejin.cn/post/7686283257302925338) | 作者见文 | 赞4/藏7/阅304 | Canvas 2D 实现背包归属、掩体挡子弹、撤离结算等状态机；无引擎游戏逻辑向。 | https://juejin.cn/post/7686283257302925338 |

#### 收藏热榜

本槽无新增。

### 前端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 1 | [走进 AI Agent 第四篇：知识获取管道——RAG 基础](https://juejin.cn/post/7687422041256689691) | 作者见文 | 赞9/藏7/阅12103 | 企业知识更新：分块、稠密/稀疏嵌入、混合检索到 Agent 可读上下文；系列第四篇。 | https://juejin.cn/post/7687422041256689691 |
| 11 | [ZCode 把整个 Git 仓库加密上传到了阿里云 OSS](https://juejin.cn/post/7686534839903535144) | 作者见文 | 赞3/藏3/阅1243 | 逆向智谱 ZCode：登录后静默打包含 Git 历史的加密包上传 OSS；Agent IDE 供应链警示。 | https://juejin.cn/post/7686534839903535144 |
| 12 | [2026年，前端框架开始为 AI 而生了](https://juejin.cn/post/7686452260913053715) | 作者见文 | 赞8/藏11/阅735 | Lynx 4.0 发布 lynx-api-docs Skill 与 A2UI；WeaveFox 多 Agent 协同与百万行生成量。 | https://juejin.cn/post/7686452260913053715 |
| 13 | [记录一种很新的大屏开发方式](https://juejin.cn/post/7687436260063100963) | 作者见文 | 赞18/藏10/阅456 | AI 承接园区三维大屏：Revit/IFC→Three.js→Vue iframe；LOD 与构件交互。 | https://juejin.cn/post/7687436260063100963 |
| 14 | [为什么越来越多开发者开始用 PostgreSQL？](https://juejin.cn/post/7686397150886477851) | 作者见文 | 赞6/藏6/阅660 | Stack Overflow 调查趋势解读：Postgres 占比上升；选型讨论，非 9/21 官方发布。 | https://juejin.cn/post/7686397150886477851 |
| 14 | [摸鱼神器：一边写代码，一边刷剧](https://juejin.cn/post/7685770509586284550) | 作者见文 | 赞9/藏7/阅668 | Vibe Coding 等待窗口的趣味工具文；与 AI 工作流相关但偏娱乐。 | https://juejin.cn/post/7685770509586284550 |

#### 收藏热榜

本槽无新增。

### 人工智能

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 4 | [货拉拉开源Hadice：安卓 & 鸿蒙桌面调试工具](https://juejin.cn/post/7687209773675937818) | 货拉拉技术 | 赞6/藏1/阅187 | Hadice 开源：Android/HarmonyOS 桌面调试，内部经验沉淀。 | https://juejin.cn/post/7687209773675937818 |
| 10 | [我终于遇到一台懂 AI 编程的专业编程显示器！](https://juejin.cn/post/7687386851712991278) | 作者见文 | 赞2/藏0/阅105 | 显示器评测向；Vibe Coding 阅读体验，偏硬件。 | https://juejin.cn/post/7687386851712991278 |
| 15 | [OpenTiny NEXT 如何构建 Agent 时代的 Web 应用？](https://juejin.cn/post/7686078320399974438) | 作者见文 | 赞1/藏1/阅101 | OpenTiny NEXT：Agent Skills、TinyRobot、GenUI SDK 等前端 AI 工具链介绍。 | https://juejin.cn/post/7686078320399974438 |

#### 收藏热榜

本槽无新增。

### 开发工具

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 14 | [Agent 新手 Skill 优先级指南](https://juejin.cn/post/7663018729802498082) | 作者见文 | 赞8/藏16/阅404 | Skill 像 SOP：先装证据收集/测试再补专业能力；新手优先级清单。 | https://juejin.cn/post/7663018729802498082 |
| 15 | [分享一套 AICoding 组合拳](https://juejin.cn/post/7664486932710113331) | 歪歪 | 赞47/藏88/阅2964 | GitHub 上一套 skills 工作流：从想法到 AICoding 落地；老文首次上热榜。 | https://juejin.cn/post/7664486932710113331 |

#### 收藏热榜

本槽无新增。

### 跨榜重复与去重说明

- 本轮新摘要 URL 数：15
- 因 `seen_urls` 跳过：105
- 同文多榜：本轮 15 篇均仅单槽

### 来源清单

- 快照日：2026-09-21（Asia/Shanghai）
- 页面：https://juejin.cn/hot/articles 、 https://juejin.cn/hot/collected-articles
- 抓取：`tools/juejin_hot_fetch.py` → `_staging_latest.json`

| 标签 | 榜单 | 标题 | 链接 |
| --- | --- | --- | --- |
| 后端 | 文章热榜 | 只恢复一张表，别把整个库都还回去 | https://juejin.cn/post/7687439830713237513 |
| 后端 | 文章热榜 | 真没想到，AI 圈又杀出来一匹黑马！ | https://juejin.cn/post/7686341072615948326 |
| 后端 | 文章热榜 | 为什么 AI 写代码时，总喜欢“防御性编程”？ | https://juejin.cn/post/7686396501736357951 |
| 后端 | 文章热榜 | 不用游戏引擎，用 Canvas 2D 做搜打撤游戏 | https://juejin.cn/post/7686283257302925338 |
| 前端 | 文章热榜 | 走进 AI Agent 第四篇：知识获取管道——RAG 基础 | https://juejin.cn/post/7687422041256689691 |
| 前端 | 文章热榜 | 2026年，前端框架开始为 AI 而生了 | https://juejin.cn/post/7686452260913053715 |
| 前端 | 文章热榜 | 记录一种很新的大屏开发方式 | https://juejin.cn/post/7687436260063100963 |
| 前端 | 文章热榜 | 为什么越来越多开发者开始用 PostgreSQL？ | https://juejin.cn/post/7686397150886477851 |
| 前端 | 文章热榜 | ZCode 把整个 Git 仓库加密上传到了阿里云 OSS | https://juejin.cn/post/7686534839903535144 |
| 前端 | 文章热榜 | 摸鱼神器：一边写代码，一边刷剧 | https://juejin.cn/post/7685770509586284550 |
| 人工智能 | 文章热榜 | 货拉拉开源Hadice：安卓 & 鸿蒙桌面调试工具 | https://juejin.cn/post/7687209773675937818 |
| 人工智能 | 文章热榜 | 我终于遇到一台懂 AI 编程的专业编程显示器！ | https://juejin.cn/post/7687386851712991278 |
| 人工智能 | 文章热榜 | OpenTiny NEXT 如何构建 Agent 时代的 Web 应用？ | https://juejin.cn/post/7686078320399974438 |
| 开发工具 | 文章热榜 | 分享一套 AICoding 组合拳 | https://juejin.cn/post/7664486932710113331 |
| 开发工具 | 文章热榜 | Agent 新手 Skill 优先级指南 | https://juejin.cn/post/7663018729802498082 |

## 2026-09-20

### 今日总览

**一句话结论**：`2026-09-20` 新 URL 主线是 **AGENTS.md 分层治理**、**若依+jeeflow 审批** 与 **本地 AI Gateway/自托管 Agent 平台**，AI 槽补 **结构化决策模型 Jev** 与 **微信小微** 体验文。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 文章热榜 + 收藏热榜 × 后端/前端/人工智能/开发工具 |
| 榜单规模 | 每槽最多 15 条；列表总条数 120；去重后新 URL **15**；跳过已见 **105**；详情成功 15 / 失败 0 |
| 核心趋势 | 1）Coding Agent 说明文件从「堆规则」转向分层；2）后端热文偏 Java 生态落地（若依/FastAPI/JDK）；3）开发工具槽集中本地网关与自托管 PaaS |
| 可直接关注 | [AGENTS.md 分层](https://juejin.cn/post/7685944661652602914)；[若依+jeeflow](https://juejin.cn/post/7685577977079185423)；[ServBay AI Gateway](https://juejin.cn/post/7685936943797141558) |

### 后端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 10 | [学习 FastAPI 的 Day 4：完成用户系统与接口联调（完结）](https://juejin.cn/post/7684893611952619529) | Dragon_xjy | 赞4/藏8/阅747 | FastAPI 系列收官：注册/登录/资料/改密串成链路，并导入 Apifox 联调。适合已跟前三篇的入门者；源码 dragonxjy/FastAPI。 | https://juejin.cn/post/7684893611952619529 |
| 11 | [给若依加审批流，不用 Flowable](https://juejin.cn/post/7685577977079185423) | mldong | 赞11/藏10/阅501 | 若依 3.9.2 免费版无审批流：用 jeeflow 而非 Flowable，后端一依赖+前端宿主组件，菜单 SQL 收口 RBAC，半天跑通待办/会签/设计器。附真机截图与踩坑。 | https://juejin.cn/post/7685577977079185423 |
| 14 | [从 0 到 1 速通 WorkBuddy](https://juejin.cn/post/7686090678486073395) | cxuanAI | 赞6/藏8/阅454 | WorkBuddy 从 0 到 1 第一篇：安装后主页三大场景（办公/代码/设计）与中文界面 walkthrough。系列长文，偏产品导览。 | https://juejin.cn/post/7686090678486073395 |

#### 收藏热榜

本槽无新增。

### 前端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 5 | [用了一个月 WorkBuddy，聊聊我的真实感受](https://juejin.cn/post/7686407614478237748) | 勇宝趣学前端 | 赞16/藏9/阅1730 | 作者长期使用第三方 GPT 中转站的体验：高峰超时、断连丢上下文、站点跑路风险；引出对稳定官方/自建通道的需求。偏叙事，非技术方案。 | https://juejin.cn/post/7686407614478237748 |
| 10 | [周下载量1.1亿的Tailwind，为什么养不活自己？](https://juejin.cn/post/7686054741464694826) | 涛涛ing | 赞7/藏4/阅974 | Tailwind 加入 Shopify 背景：周安装 1.1 亿但文档流量降 40%、付费 UI 收入近崩。论点：AI 写 UI 绕过文档，冲击 Tailwind Plus 商业模式。 | https://juejin.cn/post/7686054741464694826 |
| 11 | [掌控自己的 K 线数据：TradingView 本地部署与数据源接入](https://juejin.cn/post/7685573804516868105) | Dragon_xjy | 赞4/藏5/阅1054 | Vue 集成 TradingView 图表：本地部署 charting library、历史 K 线格式转换、PubSub+WebSocket 推实时 bar。含在线 demo 链接，地址用占位符。 | https://juejin.cn/post/7685573804516868105 |
| 12 | [别再堆 AGENTS.md 了：前端团队的 Agent 上下文分层落地指南](https://juejin.cn/post/7685944661652602914) | 作者见榜 | 赞/藏/阅见榜 | 前端团队 AGENTS.md 从 40 行涨到 600 行仍管不住 Agent：提出分层（宪法/技能/任务）而非单文件堆规则；与 Claude Code 2.1.277 读 AGENTS.md 同题。 | https://juejin.cn/post/7685944661652602914 |

#### 收藏热榜

本槽无新增。

### 人工智能

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 3 | [电商资料包合规体检实战：用蓝耘元生代把 20 分钟人工核验压成一分半](https://juejin.cn/post/7686361321609887790) | 勇宝趣学前端 | 赞4/藏5/阅1054 | 电商六份上架资料（说明书/检测/授权/规则/参数/文案）字段一致性：蓝耘元生代分工文本模型+视觉模型，把约 20 分钟人工核对压到约 1.5 分钟。多模态合规体检案例。 | https://juejin.cn/post/7686361321609887790 |
| 12 | [发布 3 天登顶 HN：不生成一个字的模型 Jev，我把它的源码和黑料都扒了一遍](https://juejin.cn/post/7686669083098775562) | 涛涛ing | 赞22/藏40/阅623 | TypeSafe AI 的 Jev 模型（9/15 发布）：结构化决策输出、不生成自由文本；作者扒源码并标注早期 HN 热度与官方自报指标水分。研究向。 | https://juejin.cn/post/7686669083098775562 |
| 14 | [微信里多了个[小微]，可以帮你看朋友圈、发消息、点外卖了](https://juejin.cn/post/7685606304111509545) | 晓凡 | 赞4/藏3/阅2464 | 微信「小微」助手实测：看朋友圈、代发消息、点外卖等；入口在聊天列表或右滑。体验向，能力随版本变化。 | https://juejin.cn/post/7685606304111509545 |

#### 收藏热榜

本槽无新增。

### 开发工具

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 6 | [跨平台开发地图 \| 2026年9月](https://juejin.cn/post/7686341837753368611) | 老刘 | 赞4/藏1/阅1144 | 2026 年 9 月跨平台地图：KMP 2.4.20 正式版 Swift 互操作转正；.NET 11 RC1 go-live；Flutter 3.47.4 hotfix；RN/uni-app 空窗。信息汇总帖。 | https://juejin.cn/post/7686341837753368611 |
| 7 | [从 0 到 1 搭建你的 AI Agent 平台：当 Agent 有了工厂，人人都能造同事](https://juejin.cn/post/7686588753231560740) | Dragon_xjy | 赞6/藏2/阅832 | 浏览器式 Agent 平台：Next.js + FastAPI + LiteLLM + ChromaDB，Docker 一键部署，支持创建/编排 Agent。系列第 7 篇，偏全栈脚手架。 | https://juejin.cn/post/7686588753231560740 |
| 8 | [一天一个开源项目（第219篇）：Openship —— 自托管部署平台](https://juejin.cn/post/7685982562691416070) | tingke | 赞1/藏1/阅202 | Openship 开源自托管部署：push 触发构建 Docker、OpenResty 路由 TLS，对标 Vercel 体验但数据在自有服务器。系列第 219 篇介绍文。 | https://juejin.cn/post/7685982562691416070 |
| 9 | [ServBay 1.33.0 来了：AI Gateway 一键接管主流 AI CLI 与多模型](https://juejin.cn/post/7685936943797141558) | ServBay | 赞1/藏3/阅139 | ServBay 1.33.0 本地 AI Gateway：聚合 Claude Code 等 CLI 的多模型 endpoint、Key 与用量控制，减少环境变量散落与代理调试。 | https://juejin.cn/post/7685936943797141558 |
| 13 | [Docker 部署填鸭表单完整教程：搭建私有化问卷与表单收集平台](https://juejin.cn/post/7685659198119542818) | 一只牛博 | 赞0/藏2/阅142 | Docker 部署填鸭 tduck 社区版 6.0 私有化问卷：数据不出域、Spring Boot 2.7.8 栈。跟做 latest 镜像，Ubuntu 24.04 实测。 | https://juejin.cn/post/7685659198119542818 |

#### 收藏热榜

本槽无新增。

### 跨榜重复与去重说明

- 本轮新摘要 URL 数：15
- 因 `seen_urls` 跳过：105
- 同文多榜：本轮 15 篇均仅出现在单槽

### 来源清单

- 快照日：2026-09-20（Asia/Shanghai）
- 页面：https://juejin.cn/hot/articles 、 https://juejin.cn/hot/collected-articles
- 抓取：`tools/juejin_hot_fetch.py` → `_staging_latest.json`

| 标签 | 榜单 | 标题 | 链接 |
| --- | --- | --- | --- |
| 后端 | 文章热榜 | 学习 FastAPI 的 Day 4：完成用户系统与接口联调（完结） | https://juejin.cn/post/7684893611952619529 |
| 后端 | 文章热榜 | 给若依加审批流，不用 Flowable | https://juejin.cn/post/7685577977079185423 |
| 后端 | 文章热榜 | 从 0 到 1 速通 WorkBuddy | https://juejin.cn/post/7686090678486073395 |
| 前端 | 文章热榜 | 用了一个月 WorkBuddy，聊聊我的真实感受 | https://juejin.cn/post/7686407614478237748 |
| 前端 | 文章热榜 | 周下载量1.1亿的Tailwind，为什么养不活自己？ | https://juejin.cn/post/7686054741464694826 |
| 前端 | 文章热榜 | 掌控自己的 K 线数据：TradingView 本地部署与数据源接入 | https://juejin.cn/post/7685573804516868105 |
| 前端 | 文章热榜 | 别再堆 AGENTS.md 了：前端团队的 Agent 上下文分层落地指南 | https://juejin.cn/post/7685944661652602914 |
| 人工智能 | 文章热榜 | 电商资料包合规体检实战：用蓝耘元生代把 20 分钟人工核验压成一分半 | https://juejin.cn/post/7686361321609887790 |
| 人工智能 | 文章热榜 | 发布 3 天登顶 HN：不生成一个字的模型 Jev，我把它的源码和黑料都扒了一遍 | https://juejin.cn/post/7686669083098775562 |
| 人工智能 | 文章热榜 | 微信里多了个[小微]，可以帮你看朋友圈、发消息、点外卖了 | https://juejin.cn/post/7685606304111509545 |
| 开发工具 | 文章热榜 | 跨平台开发地图 | 2026年9月 | https://juejin.cn/post/7686341837753368611 |
| 开发工具 | 文章热榜 | 从 0 到 1 搭建你的 AI Agent 平台：当 Agent 有了工厂，人人都能造同事 | https://juejin.cn/post/7686588753231560740 |
| 开发工具 | 文章热榜 | 一天一个开源项目（第219篇）：Openship —— 自托管部署平台，把 Vercel 的体验搬到你自己的服务器上 | https://juejin.cn/post/7685982562691416070 |
| 开发工具 | 文章热榜 | ServBay 1.33.0 来了：AI Gateway 一键接管主流 AI CLI 与多模型 | https://juejin.cn/post/7685936943797141558 |
| 开发工具 | 文章热榜 | Docker 部署填鸭表单完整教程：搭建私有化问卷与表单收集平台 | https://juejin.cn/post/7685659198119542818 |

## 2026-09-18

### 今日总览

**一句话结论**：`2026-09-18` 新 URL 主线是 **组织级 AI Coding 产线** 与 **前端性能/复用闸门**，开发工具槽补真浏览器 Skill 和 Agent 行为评估。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 文章热榜 + 收藏热榜 × 后端/前端/人工智能/开发工具 |
| 榜单规模 | 每槽最多 15 条；列表总条数 120；去重后新 URL **11**；跳过已见 **109**；详情成功 11 / 失败 0 |
| 核心趋势 | 1）热文从「个人无限 token」转到「组织怎么度量、怎么收口」；2）前端同时打交互性能和 AI 造轮子；3）收藏槽全是已见文 |
| 可直接关注 | [货拉拉实践](https://juejin.cn/post/7685936943796977718)；[组件复用闭环](https://juejin.cn/post/7685970177332592655)；[BrowserAct](https://juejin.cn/post/7685691414155935790)；[行为评估](https://juejin.cn/post/7686010356546011199) |

### 后端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 8 | [JDK27正式发布，人麻了!](https://juejin.cn/post/7686174631263404073) | 苏三说技术 | 赞10/藏4/阅713 | 社区拆 JEP：G1 成全环境默认 GC、紧凑对象头默认、TLS 1.3 后量子混合。作者强调默认行为变更，升级即受益。细节回 Oracle/JEP。 | https://juejin.cn/post/7686174631263404073 |
| 12 | [一份 KDMS 评估报告，怎样排出迁移先后顺序](https://juejin.cn/post/7686361321610035246) | 一只牛博 | 赞0/藏0/阅624 | 人大金仓迁移：总兼容度只能看方向，排期要回到对象明细和工作量。评估报告当后续基准，不要开完会就归档。无 AI 增量。 | https://juejin.cn/post/7686361321610035246 |

#### 收藏热榜

本槽无新增。

### 前端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 5 | [2026 年了，十万级表格还只会「虚拟滚动」？](https://juejin.cn/post/7686043275371708450) | 秋天的一阵风 | 赞7/藏13/阅1332 | 虚拟滚动只减 DOM；搜索/排序/全选卡在主线程全量计算和勾选状态设计。面试向，给交互层瓶颈，不是又一篇虚拟列表入门。 | https://juejin.cn/post/7686043275371708450 |
| 8 | [AI写代码越跑越快，项目组件却越来越乱？](https://juejin.cn/post/7685970177332592655) | 秋天的一阵风 | 赞3/藏4/阅1264 | AI 看不见存量组件就会现编。主张写前清单、写时按项目 API、合入前复用校验。关键词搜拦不住换皮/异形重复。 | https://juejin.cn/post/7685970177332592655 |

#### 收藏热榜

本槽无新增。

### 人工智能

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 6 | [Codex 最新焚决发布，快！](https://juejin.cn/post/7686029820083929097) | 沉默王二 | 赞16/藏13/阅845 | 把 OpenAI 9/11《Rethinking skills and prompts for GPT-6 Astra》落成两段审查 prompt：先找过宽 Skill / 强制读文档 / 冲突规则，再最小改 AGENTS.md。原文不回填。 | https://juejin.cn/post/7686029820083929097 |
| 12 | [民间AI排行榜单新鲜出炉，Fable 5.1仅排第三](https://juejin.cn/post/7686044352167575604) | 石小石Orz | 赞9/藏3/阅446 | 转述 B 站「整活」竞技场：Astra 第一、Fable 5.1 第三。用来讨论 Benchmark ≠ 真实任务，不是官方榜。 | https://juejin.cn/post/7686044352167575604 |
| 13 | [个人提效，攒不成组织提效：货拉拉 AI Coding 落地实践](https://juejin.cn/post/7685936943796977718) | 货拉拉技术 | 赞7/藏10/阅499 | 统一工作台、spec 驱动、三层签名度量、FPY 盲区、对抗性审查。1000+ 工程师规模下个人配置撑不住。 | https://juejin.cn/post/7685936943796977718 |

#### 收藏热榜

本槽无新增。

### 开发工具

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 10 | [BrowserAct，给AI Agent配一个真实浏览器](https://juejin.cn/post/7685691414155935790) | 狂师 | 赞2/藏0/阅61 | 开源 CLI + Skill：云端写一句话出爬虫，本地装进 Claude Code/Cursor/Codex，复用真 Chrome 登录态，带验证码和远程接管。forge 把探路沉淀成 SKILL.md。 | https://juejin.cn/post/7685691414155935790 |
| 11 | [价值200的AI订阅实测](https://juejin.cn/post/7685966048847380514) | 程序员老刘 | 赞1/藏0/阅73 | token plan：5 小时 1 万 AFP ≈ GLM5.3 两千万 token，一个列表分类页没改完就烧光。账本向，套餐名未写死官方产品。 | https://juejin.cn/post/7685966048847380514 |
| 12 | [Flutter 本地大模型实战：做一个自然语言记账工具](https://juejin.cn/post/7685559463386464262) | Crazy_MT | 赞0/藏2/阅91 | 本地模型只做意图和抽字段，Dart 校验后 Floor 写 SQLite。模型没有直接写库权限。适合隐私记账 demo。 | https://juejin.cn/post/7685559463386464262 |
| 15 | [基于“行为评估”准则评估智能体(一)](https://juejin.cn/post/7686010356546011199) | MobotStone | 赞1/藏1/阅65 | 对照 Google Harness Engineering：改 Prompt/Tool 后分数掉了，要查工具选没选对、测没测、流程偏没偏。只看 PASS/FAIL 定位不了回归。 | https://juejin.cn/post/7686010356546011199 |

#### 收藏热榜

本槽无新增。


### 跨榜重复与去重说明

- 本轮新摘要 URL 数：11
- 因 `seen_urls` 跳过：109（只给数量；不要把已见文再展开成表行）
- 同文多标签/双榜出现：无

### 来源清单

- 快照日：2026-09-18（Asia/Shanghai）
- 页面：https://juejin.cn/hot/articles 、 https://juejin.cn/hot/collected-articles
- 抓取：`tools/juejin_hot_fetch.py` → `_staging_latest.json`

| 标签 | 榜单 | 标题 | 链接 |
| --- | --- | --- | --- |
| 后端 | 文章热榜 | JDK27正式发布，人麻了! | https://juejin.cn/post/7686174631263404073 |
| 后端 | 文章热榜 | 一份 KDMS 评估报告，怎样排出迁移先后顺序 | https://juejin.cn/post/7686361321610035246 |
| 前端 | 文章热榜 | 十万级表格还只会虚拟滚动？ | https://juejin.cn/post/7686043275371708450 |
| 前端 | 文章热榜 | AI写代码越跑越快，项目组件却越来越乱 | https://juejin.cn/post/7685970177332592655 |
| 人工智能 | 文章热榜 | Codex 最新焚决发布，快！ | https://juejin.cn/post/7686029820083929097 |
| 人工智能 | 文章热榜 | 民间AI排行榜单新鲜出炉 | https://juejin.cn/post/7686044352167575604 |
| 人工智能 | 文章热榜 | 货拉拉 AI Coding 落地实践 | https://juejin.cn/post/7685936943796977718 |
| 开发工具 | 文章热榜 | BrowserAct | https://juejin.cn/post/7685691414155935790 |
| 开发工具 | 文章热榜 | 价值200的AI订阅实测 | https://juejin.cn/post/7685966048847380514 |
| 开发工具 | 文章热榜 | Flutter 本地大模型记账 | https://juejin.cn/post/7685559463386464262 |
| 开发工具 | 文章热榜 | 基于行为评估准则评估智能体 | https://juejin.cn/post/7686010356546011199 |

## 2026-09-17

### 今日总览

**一句话结论**：`2026-09-17` 新 URL 主线是 **Agent 长期记忆 / 浏览器上下文** 与 **前端矢量 PDF**，开发工具槽出现 Codex 本地代理和统一 Agent Rules。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 文章热榜 + 收藏热榜 × 后端/前端/人工智能/开发工具 |
| 榜单规模 | 每槽最多 15 条；列表总条数 120；去重后新 URL **20**；跳过已见 **100**；详情成功 20 / 失败 0 |
| 核心趋势 | 1）团队在补 Agent 读得懂的仓库记忆，而不是再写给人看的 Wiki；2）前端热文回到渲染/转码基本功；3）收藏榜本轮仅 1 条系列文 |
| 可直接关注 | [OpenWiki](https://juejin.cn/post/7685591822258585626)；[OpenSider](https://juejin.cn/post/7685651354878754825)；[AgentLoop](https://juejin.cn/post/7684795356321775626)；[dompdf.js](https://juejin.cn/post/7685644889096011827) |

### 后端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 8 | [ChatGPT 开启无限 token](https://juejin.cn/post/7685770509585629190) | cxuanAI | 赞20/藏10/阅955 | 讲 Plus 额度用尽后，把活挪到不消耗 Work/Codex 额度的 Chat，再接 MCP。作者自己写「不推荐、有风险、别用主号」。灰区绕过，不当官方能力。 | https://juejin.cn/post/7685770509585629190 |
| 12 | [AI会让程序员失业吗？200年前的手工织工已经给出了答案](https://juejin.cn/post/7685276242113019938) | shengjk1 | 赞7/藏6/阅336 | 用卢德运动类比：机器先让熟练降价，不是一夜失业。观点文，适合当岗位讨论，无实现增量。 | https://juejin.cn/post/7685276242113019938 |
| 15 | [为什么越来越多人用OpenWiki？](https://juejin.cn/post/7685591822258585626) | 苏三说技术 | 赞4/藏7/阅325 | LangChain 2026-07 开源：扫描仓库，用 Deep Agents 生成给 Agent 读的 Markdown Wiki，事实进 `openwiki/.claims/`。解决「每次任务都失忆」。 | https://juejin.cn/post/7685591822258585626 |

#### 收藏热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 15 | [16｜（前端转全栈）前端人排查后端问题](https://juejin.cn/post/7669696162708570166) | swipe | 赞25/藏60/阅1375 | 系列第 16 篇：用 curl、traceId、日志、MySQL、Redis 对照前端 DevTools 习惯查后端。配套 fullstack-mall。8 月原文，本轮收藏榜新 URL。 | https://juejin.cn/post/7669696162708570166 |

### 前端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 2 | [前端2秒生成500页矢量PDF，rust真的强到没朋友](https://juejin.cn/post/7685644889096011827) | 刘发财 | 赞23/藏29/阅2874 | `dompdf.js` 用 Rust/WASM 读 DOM 几何直出矢量 PDF，不再走 html2canvas 截图。作者正在拆掉 jsPDF 依赖。适合长文档导出。 | https://juejin.cn/post/7685644889096011827 |
| 11 | [前端转型全栈 00：AI 时代该学哪些，不该学哪些](https://juejin.cn/post/7685561582916304906) | LEE | 赞9/藏11/阅493 | 主张别先背一门后端语法；先补持久化、幂等、权限、迁移。美团/京东编制调整作背景，属报道转述。 | https://juejin.cn/post/7685561582916304906 |
| 12 | [PNG/JPG 如何变成 WebP？真相不是改后缀！](https://juejin.cn/post/7684900473053970478) | 不一样的少年_ | 赞10/藏9/阅449 | 格式转换=解码成像素再按目标编码器重打包。用 libvips 讲 PNG/JPG/WebP。无 AI 增量。 | https://juejin.cn/post/7684900473053970478 |
| 13 | [AgentLoop: 从 while(true) 到生产级循环](https://juejin.cn/post/7684795356321775626) | 掰头战士 | 赞16/藏6/阅315 | 6 行最小 loop 会在上下文爆炸、死循环、429、无流式、账单、截断上崩。生产差距在每轮额外做的压缩/检测/进度。 | https://juejin.cn/post/7684795356321775626 |
| 14 | [AI发展下的后编程时代思考](https://juejin.cn/post/7684657593500205110) | 林冠宏_指尖下的幽灵 | 赞4/藏3/阅540 | 对比几年前掘金分享热度，讨论 AI 之后写代码与写文章的动机变化。随笔，技术增量有限。 | https://juejin.cn/post/7684657593500205110 |
| 15 | [从调研到闭环，我用 GPT-Image-2.5 和 GPT-6 Astra 把智慧厂房 3D 大屏这条链路走完了](https://juejin.cn/post/7684759404726321203) | 柳杉 | 赞8/藏2/阅326 | 先写工程 Brief，再用 GPT-Image-2.5 出图、Astra + Blender MCP 建模，把调研到代码还原串成一条线。案例文。 | https://juejin.cn/post/7684759404726321203 |

#### 收藏热榜

本槽无新增。

### 人工智能

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 10 | [全球最聪明的几个人，本周突然一起说“别卷了”](https://juejin.cn/post/7685267114438115366) | 码事漫谈 | 赞7/藏5/阅507 | 转述 Amodei《Pace the Frontier》与 Altman/Musk 表态，并对照融资与专利仍在加速。时政向，重大数字回官方原文。 | https://juejin.cn/post/7685267114438115366 |
| 12 | [WorkBuddy + 飞书的 8 种神仙用法](https://juejin.cn/post/7685215742590451763) | 苍何 | 赞7/藏4/阅341 | 官方飞书连接器：读群/知识库/日程/多维表，再建文档和约会。知识库 9/14 已写过同文，本轮热榜新 URL。 | https://juejin.cn/post/7685215742590451763 |
| 13 | [GPT‑6 Astra真正的变化：AI开始直接操作工作软件](https://juejin.cn/post/7683803827217350675) | 蜗牛聊AI | 赞5/藏2/阅342 | 把 Astra 读成「在权限约束下跑可验收流程」，而不是更高分聊天。引用 9/9 官方页，热榜传播窗口。 | https://juejin.cn/post/7683803827217350675 |
| 14 | [一天一个开源项目（第214篇）：AstronRPA](https://juejin.cn/post/7684019326370611263) | 冬奇Lab | 赞4/藏6/阅379 | 讯飞开源桌面 RPA：300+ 组件，经 MCP 给 Astron Agent 当「手」，覆盖没 API 的金蝶/用友界面。 | https://juejin.cn/post/7684019326370611263 |
| 15 | [OpenSider：让浏览器驱动 Agent](https://juejin.cn/post/7685651354878754825) | parksben | 赞4/藏2/阅302 | 浏览器当客户端、本机 CLI Agent 当执行器：侧边栏看到当前标签页，不必 Playwright 另起干净浏览器丢登录态。 | https://juejin.cn/post/7685651354878754825 |

#### 收藏热榜

本槽无新增。

### 开发工具

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 11 | [找不到好用的 Mac 便签，我干脆自己做了一个](https://juejin.cn/post/7685559824034316339) | 柯腾呐 | 赞0/藏0/阅105 | DSticky：Tauri v2 + React + Rust，独立窗口便签，本机保存、跨 Space、全屏置顶。无账号。个人工具。 | https://juejin.cn/post/7685559824034316339 |
| 12 | [AI 让我的独门小工具焕发第二春](https://juejin.cn/post/7685206698757619712) | 烽火戏诸诸诸侯 | 赞1/藏0/阅81 | 两年前后用 Agent 重画同一套 Java Swing 端口检测工具的 UI。案例向，框架没变。 | https://juejin.cn/post/7685206698757619712 |
| 13 | [我把 Codex 变成了一个本地 API：Codex Proxy 配置实战](https://juejin.cn/post/7684602434082570282) | 凭君语未可 | 赞0/藏1/阅89 | 用第三方 `codex-proxy` 把本机 Codex 登录态转成 `127.0.0.1:6769/v1`。额度照旧，作者强调只本机、非官方网关。 | https://juejin.cn/post/7684602434082570282 |
| 14 | [AI 编程工具链碎片化？基于多端兼容的统一 Agent Rules 架构实践](https://juejin.cn/post/7684484529649975348) | 程序员2007 | 赞0/藏1/阅63 | 只维护一份 `AGENTS.md`，脚本同步到 Cursor / Claude Code / Copilot。解决三套规则漂移。 | https://juejin.cn/post/7684484529649975348 |
| 15 | [120+ 个 Agent Skill 管不过来？我造了套「包管理器」](https://juejin.cn/post/7684228650582278150) | 王若风 | 赞0/藏2/阅81 | skillctl：仓库当源、软链接安装、doctor 修断链。立场是「宁要链接复杂性，不要副本不一致」。 | https://juejin.cn/post/7684228650582278150 |

#### 收藏热榜

本槽无新增。


### 跨榜重复与去重说明

- 本轮新摘要 URL 数：20
- 因 `seen_urls` 跳过：100（只给数量；不要把已见文再展开成表行）
- 同文多标签/双榜出现：无

### 来源清单

- 快照日：2026-09-17（Asia/Shanghai）
- 页面：https://juejin.cn/hot/articles 、 https://juejin.cn/hot/collected-articles
- 抓取：`tools/juejin_hot_fetch.py` → `_staging_latest.json`

| 标签 | 榜单 | 标题 | 链接 |
| --- | --- | --- | --- |
| 后端 | 文章热榜 | ChatGPT 开启无限 token | https://juejin.cn/post/7685770509585629190 |
| 后端 | 文章热榜 | AI会让程序员失业吗？200年前的手工织工已经给出了答案 | https://juejin.cn/post/7685276242113019938 |
| 后端 | 文章热榜 | 为什么越来越多人用OpenWiki？ | https://juejin.cn/post/7685591822258585626 |
| 后端 | 收藏热榜 | 16｜（前端转全栈）前端人排查后端问题 | https://juejin.cn/post/7669696162708570166 |
| 前端 | 文章热榜 | 前端2秒生成500页矢量PDF | https://juejin.cn/post/7685644889096011827 |
| 前端 | 文章热榜 | 前端转型全栈 00 | https://juejin.cn/post/7685561582916304906 |
| 前端 | 文章热榜 | PNG/JPG 如何变成 WebP？ | https://juejin.cn/post/7684900473053970478 |
| 前端 | 文章热榜 | AgentLoop: 从 while(true) 到生产级循环 | https://juejin.cn/post/7684795356321775626 |
| 前端 | 文章热榜 | AI发展下的后编程时代思考 | https://juejin.cn/post/7684657593500205110 |
| 前端 | 文章热榜 | 智慧厂房 3D 大屏闭环 | https://juejin.cn/post/7684759404726321203 |
| 人工智能 | 文章热榜 | 全球最聪明的几个人，本周突然一起说“别卷了” | https://juejin.cn/post/7685267114438115366 |
| 人工智能 | 文章热榜 | WorkBuddy + 飞书的 8 种神仙用法 | https://juejin.cn/post/7685215742590451763 |
| 人工智能 | 文章热榜 | GPT‑6 Astra真正的变化 | https://juejin.cn/post/7683803827217350675 |
| 人工智能 | 文章热榜 | AstronRPA | https://juejin.cn/post/7684019326370611263 |
| 人工智能 | 文章热榜 | OpenSider：让浏览器驱动 Agent | https://juejin.cn/post/7685651354878754825 |
| 开发工具 | 文章热榜 | DSticky Mac 便签 | https://juejin.cn/post/7685559824034316339 |
| 开发工具 | 文章热榜 | AI 让我的独门小工具焕发第二春 | https://juejin.cn/post/7685206698757619712 |
| 开发工具 | 文章热榜 | Codex Proxy 配置实战 | https://juejin.cn/post/7684602434082570282 |
| 开发工具 | 文章热榜 | 统一 Agent Rules | https://juejin.cn/post/7684484529649975348 |
| 开发工具 | 文章热榜 | skill 包管理器 | https://juejin.cn/post/7684228650582278150 |

## 2026-09-16

### 今日总览

**一句话结论**：`2026-09-16` 新 URL 主线是 **Android Studio 把 Agent Skills 预装进 IDE** 与 **折叠屏双栏路由**，后端热文回到校验/直播高并发，AI 槽继续消化减速舆论和 FDE 岗位。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 文章热榜 + 收藏热榜 × 后端/前端/人工智能/开发工具 |
| 榜单规模 | 每槽最多 15 条；列表总条数 120；去重后新 URL **17**；跳过已见 **103**；详情成功 17 / 失败 0 |
| 核心趋势 | 1）IDE/前端开始用 skill 和验收模板接住 AI 写代码的速度；2）后端热文偏基础组件与吐槽文；3）收藏槽全是已见文 |
| 可直接关注 | [AS Quail 4](https://juejin.cn/post/7685597597233905716)；[vue-split-screen](https://juejin.cn/post/7683846471340032051)；[AI 验收](https://juejin.cn/post/7684102772083130422)；[FDE](https://juejin.cn/post/7684795356343336998) |

### 后端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 1 | [ValidX时间段验证详解：ISO 8601标准与简化格式](https://juejin.cn/post/7684649314159312930) | vipxieliang | 赞2/藏2/阅10916 | 讲时间段与时间点的差别，以及 ValidX 对 ISO 8601 `P[nY][nM][nD]T…` 和简化「数字+单位」两种写法的约束。适合做预约/账单区间校验。无 AI 增量。 | https://juejin.cn/post/7684649314159312930 |
| 10 | [“这需求用 AI 也就十分钟吧？”——周五深夜十一点，我在工位给 Cursor 擦屁股](https://juejin.cn/post/7684460980934164495) | 程序员2007 | 赞4/藏5/阅331 | 吐槽「积分到期横幅」被当成十分钟 AI 活，夜里给 Cursor/Claude Code 擦边界和灰度。观点文：省的是打字，不是验收和回滚。 | https://juejin.cn/post/7684460980934164495 |
| 12 | [一个Docker命令，40万首古诗词API开箱即用](https://juejin.cn/post/7683820796637872154) | SimonKing | 赞6/藏5/阅273 | 介绍 Go 服务「诗泉」：基于 chinese-poetry 数据集，Docker 拉起近 40 万首诗词检索 API。适合国风小程序先别自建库。 | https://juejin.cn/post/7683820796637872154 |
| 13 | [GPT-6 Astra 的提示词泄露了，里面居然藏着个保安？](https://juejin.cn/post/7685215742590517299) | cxuanAI | 赞6/藏5/阅270 | 拆 Codex Desktop 收集型提示词里的 Guardian V2：异步审电脑/浏览器动作。**泄露仓，事实以官方为准**。热榜新 URL，知识库 9/14 已写过同文。 | https://juejin.cn/post/7685215742590517299 |
| 15 | [手搓一套直播高并发环境！一个后端小白从 0 到 1 的搭建笔记](https://juejin.cn/post/7684154085232001059) | 码外生活 | 赞3/藏5/阅224 | 用 Spring Cloud / Dubbo / Redis / RabbitMQ / Netty / K8s 搭直播练习环境。学习向选型笔记，不是生产压测报告。 | https://juejin.cn/post/7684154085232001059 |

#### 收藏热榜

本槽无新增。

### 前端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 10 | [iPhone Duo 发布后，一个 Vue 组件让 Web 应用低成本适配折叠屏](https://juejin.cn/post/7683846471340032051) | huali | 赞8/藏18/阅848 | `vue-split-screen` 用一条导航轨迹驱动双栏：只维护一套 Vue Router，轨迹写入 `history.state`，从哪个面板点就从哪个节点 push/replace。适合列表+详情上折叠屏。 | https://juejin.cn/post/7683846471340032051 |
| 12 | [你的 Vue3 项目也能有钉钉同款审批流设计器](https://juejin.cn/post/7683434989240795162) | mldong | 赞14/藏22/阅567 | npm 装 `mldong-flow-designer-dingtalk`，10 分钟画出审批链，JSON 交给 jeeflow。避开画布类设计器对业务用户过重的问题。 | https://juejin.cn/post/7683434989240795162 |
| 13 | [我用 AI 写完一个需求后才发现，最难的不是 prompt，而是验收](https://juejin.cn/post/7684102772083130422) | kyriewen | 赞8/藏6/阅560 | 把时间账从「八分写两分验」翻过来；给 5 个必验项和验收 prompt 模板。适合把 Claude Code 产出挡在提交前。 | https://juejin.cn/post/7684102772083130422 |
| 14 | [面试官问我：AI 都能写代码了，前端凭什么还值 25K](https://juejin.cn/post/7683348233489924102) | kyriewen | 赞5/藏6/阅551 | 论点是 25K 买的是不确定条件下的交付，不是 JSX 产量。标题是拟访谈，不是某一场真实面试实录。 | https://juejin.cn/post/7683348233489924102 |
| 15 | [程序员都开始懂业务了，产品经理还剩下什么价值？](https://juejin.cn/post/7684690252645515298) | 勇宝趣学前端 | 赞3/藏1/阅462 | 把 PM 价值从写文档改到工作流设计：哪些判断给模型、哪些必须人审。观点文；知识库 9/14 已写过同文。 | https://juejin.cn/post/7684690252645515298 |

#### 收藏热榜

本槽无新增。

### 人工智能

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 4 | [黄仁勋台上接特朗普电话开免提，全场听到一句话：AI 不会减速](https://juejin.cn/post/7685320540698361899) | 计算机魔术师 | 赞12/藏2/阅1400 | 转述 9/14 All-In Summit：黄仁勋免接特朗普电话，对位 Anthropic「限速」。时政/传播向，不当技术结论。 | https://juejin.cn/post/7685320540698361899 |
| 6 | [2026年古法编程的末法时代，如何评估自己完成迅速转行](https://juejin.cn/post/7684615074136801320) | Sumoon | 赞15/藏14/阅681 | 用「React/API/Agent」栈自评转行，并提醒先补基础再谈 Agent。职业规划文，技术增量有限。 | https://juejin.cn/post/7684615074136801320 |
| 12 | [AI 越来越强，为什么打工人反而越来越累、越来越内耗了？](https://juejin.cn/post/7684573646438629386) | 程序员海军 | 赞6/藏4/阅467 | 访谈体：能干的活多了，上下文切换和验收没少。情绪向，可当现象记录。 | https://juejin.cn/post/7684573646438629386 |
| 14 | [最近火爆出圈的，FDE 到底是个什么岗位？](https://juejin.cn/post/7684795356343336998) | 狂师 | 赞6/藏4/阅442 | 拆 Forward Deployment Engineer：现场把模型嵌进客户流程，考应用开发/工程化/业务沟通，不是售前也不是调 API。 | https://juejin.cn/post/7684795356343336998 |

#### 收藏热榜

本槽无新增。

### 开发工具

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 8 | [Android Studio Quail 4发布，看日志我以为谷歌放弃Flutter了](https://juejin.cn/post/7685597597233905716) | 程序员老刘 | 赞2/藏3/阅199 | Quail 4 收官：23 项 Android Skills、Gemma 4 本地、并行 Agent 状态条。Flutter「迁回原生」在下一版 Rabbit 1 Canary，作者后文也说 Flutter 线还在发版。细节回 developer.android.com。 | https://juejin.cn/post/7685597597233905716 |
| 13 | [2026 性能测试工具大盘点：13 款主流压测工具](https://juejin.cn/post/7685282635451531273) | 狂师 | 赞2/藏5/阅68 | 先警告压测机先挂会测出假上限；对照 JMeter、k6、Locust、wrk。清单文。 | https://juejin.cn/post/7685282635451531273 |
| 15 | [2026年做数据库开发，国产数据库已经是绕不开的选项了](https://juejin.cn/post/7683348233489596422) | 这个DBA有点耶 | 赞0/藏1/阅113 | 新手路径：先关系库再谈国产选型，作者用 Mongo 错选的迁移故事开场。入门向。 | https://juejin.cn/post/7683348233489596422 |

#### 收藏热榜

本槽无新增。


### 跨榜重复与去重说明

- 本轮新摘要 URL 数：17
- 因 `seen_urls` 跳过：103（只给数量；不要把已见文再展开成表行）
- 同文多标签/双榜出现：无

### 来源清单

- 快照日：2026-09-16（Asia/Shanghai）
- 页面：https://juejin.cn/hot/articles 、 https://juejin.cn/hot/collected-articles
- 抓取：`tools/juejin_hot_fetch.py` → `_staging_latest.json`

| 标签 | 榜单 | 标题 | 链接 |
| --- | --- | --- | --- |
| 后端 | 文章热榜 | ValidX时间段验证详解：ISO 8601标准与简化格式 | https://juejin.cn/post/7684649314159312930 |
| 后端 | 文章热榜 | “这需求用 AI 也就十分钟吧？” | https://juejin.cn/post/7684460980934164495 |
| 后端 | 文章热榜 | 一个Docker命令，40万首古诗词API开箱即用 | https://juejin.cn/post/7683820796637872154 |
| 后端 | 文章热榜 | GPT-6 Astra 的提示词泄露了，里面居然藏着个保安？ | https://juejin.cn/post/7685215742590517299 |
| 后端 | 文章热榜 | 手搓一套直播高并发环境 | https://juejin.cn/post/7684154085232001059 |
| 前端 | 文章热榜 | iPhone Duo 发布后，一个 Vue 组件让 Web 应用低成本适配折叠屏 | https://juejin.cn/post/7683846471340032051 |
| 前端 | 文章热榜 | 你的 Vue3 项目也能有钉钉同款审批流设计器 | https://juejin.cn/post/7683434989240795162 |
| 前端 | 文章热榜 | 我用 AI 写完一个需求后才发现，最难的不是 prompt，而是验收 | https://juejin.cn/post/7684102772083130422 |
| 前端 | 文章热榜 | 面试官问我：AI 都能写代码了，前端凭什么还值 25K | https://juejin.cn/post/7683348233489924102 |
| 前端 | 文章热榜 | 程序员都开始懂业务了，产品经理还剩下什么价值？ | https://juejin.cn/post/7684690252645515298 |
| 人工智能 | 文章热榜 | 黄仁勋台上接特朗普电话开免提 | https://juejin.cn/post/7685320540698361899 |
| 人工智能 | 文章热榜 | 2026年古法编程的末法时代 | https://juejin.cn/post/7684615074136801320 |
| 人工智能 | 文章热榜 | AI 越来越强，为什么打工人反而越来越累 | https://juejin.cn/post/7684573646438629386 |
| 人工智能 | 文章热榜 | 最近火爆出圈的，FDE 到底是个什么岗位？ | https://juejin.cn/post/7684795356343336998 |
| 开发工具 | 文章热榜 | Android Studio Quail 4发布 | https://juejin.cn/post/7685597597233905716 |
| 开发工具 | 文章热榜 | 2026 性能测试工具大盘点 | https://juejin.cn/post/7685282635451531273 |
| 开发工具 | 文章热榜 | 2026年做数据库开发，国产数据库已经是绕不开的选项了 | https://juejin.cn/post/7683348233489596422 |

## 2026-09-15

### 今日总览

**一句话结论**：`2026-09-15` 新 URL 主线是 **DeepSeek Harness 桌面端/插件架构** 与 **JWT vs 大站 Session**，AI 槽继续消化降价机制和递归自改进舆论。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 文章热榜 + 收藏热榜 × 后端/前端/人工智能/开发工具 |
| 榜单规模 | 每槽最多 15 条；列表总条数 120；去重后新 URL **11**；跳过已见 **109**；详情成功 11 / 失败 0 |
| 核心趋势 | 1）DeepSeek Harness 从 WebUI 叙事转到仓库里的 desktop + plugin；2）后端热文回到认证/备份/消息总线基本功；3）收藏槽全是已见文 |
| 可直接关注 | [主流站不用 JWT](https://juejin.cn/post/7684261460002701338)；[Harness 桌面端](https://juejin.cn/post/7685188623412133898)；[Harness 架构](https://juejin.cn/post/7684759404727320627)；[Kafka 当 Agent 总线](https://juejin.cn/post/7684573646439317514) |

### 后端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 8 | [被吹上天的 JWT，为什么主流网站一个都不用](https://juejin.cn/post/7684261460002701338) | 减瓦 | 赞22/藏18/阅1299 | 减瓦对照 GitHub/Google/Amazon/Netflix 登录 Cookie：主流站点用服务端 session，不是浏览器 JWT。JWT 出镜率高来自教程和脚手架，不是大站实践。适合面试和网关选型时把「无状态」和「可吊销」分开。 | https://juejin.cn/post/7684261460002701338 |
| 12 | [只备份一个 schema，别把整库都搬走](https://juejin.cn/post/7685224902321848358) | 一只牛博 | 赞0/藏0/阅753 | 牛博讲只备份单个 schema：用 sys_dump `-n` 锁范围，避免整库 dump 带出审计/他人业务表。先 `help` 确认当前版本认不认该参数。适合多 schema 共库的迁移/外发。 | https://juejin.cn/post/7685224902321848358 |
| 13 | [Kafka已正式接入AI](https://juejin.cn/post/7684573646439317514) | 苏三说技术 | 赞9/藏10/阅493 | 苏三主张 Multi-Agent 别用同步 HTTP 串：改 Kafka 当 Agent 总线（Topic 异步、挂了不丢中间态）。并提到 Kafka 在 MCP/A2A/实时上下文上的布局。架构观点文，落地要自补幂等和 schema。 | https://juejin.cn/post/7684573646439317514 |

#### 收藏热榜

本槽无新增。

### 前端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 12 | [DeepSeek 官方仓库惊现 DeepSeek Harness 桌面端！](https://juejin.cn/post/7685188623412133898) | ikoala | 赞20/藏12/阅866 | ikoala 翻 DeepSeek Harness 官方仓 `apps/desktop`：8/28 起有 Electron 打包，现 0.1.5 rc.2；截至 9/13 仍是 Developer Preview，Releases 无安装包。桌面端不走本地 Web 服务。以仓库为准。 | https://juejin.cn/post/7685188623412133898 |
| 15 | [倒反天罡！押注 React Native 6 年后，Shopify 又回到了原生开发](https://juejin.cn/post/7683784267847925787) | parade岁月 | 赞7/藏7/阅667 | parade岁月转述 Shopify 9/10 工程博文：押注 RN 六年后回到 Swift/Kotlin Native，背景之一是 AI Coding Agent 更吃原生工具链。热榜传播窗口，细节回 Shopify Engineering 原文。 | https://juejin.cn/post/7683784267847925787 |

#### 收藏热榜

本槽无新增。

### 人工智能

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 10 | [代码80%是AI写的，这家AI公司呼吁暂停AI开发](https://juejin.cn/post/7684228650583375878) | 计算机魔术师 | 赞4/藏2/阅529 | 计算机魔术师复述 Anthropic《当 AI 构建自身》：内部超 80% 合入代码由 Claude 写，同时警告递归自改进。观点/转述，重大数字回官方署名文，不当成 9/15 新数据。 | https://juejin.cn/post/7684228650583375878 |
| 11 | [DeepSeek 这波操作很凶](https://juejin.cn/post/7684154085232017443) | 码事漫谈 | 赞7/藏5/阅425 | 码事漫谈把 DeepSeek 9/10 降价解释成「KV Cache 工作记忆砍掉约 3/4」的结果，而不只是促销。Agent 长上下文账单的关键是草稿纸厚度。机制向解读，以官方价目和技术报告为准。 | https://juejin.cn/post/7684154085232017443 |
| 12 | [5000亿估值冲刺科创板，DeepSeek 为何急着上市？](https://juejin.cn/post/7684102772083195958) | 计算机魔术师 | 赞7/藏5/阅389 | 计算机魔术师转述路透：DeepSeek 接洽中信证券筹备科创板，5000 亿估值融资后不到三月。尚未见辅导备案。财经向，不当技术结论。 | https://juejin.cn/post/7684102772083195958 |
| 13 | [Deepseek Harness 架构解析和应用](https://juejin.cn/post/7684759404727320627) | 古茗前端团队 | 赞7/藏6/阅344 | 古茗前端拆 DeepSeek Harness：Everything is a plugin，底层 Cordis；`npx @deepseek-ai/dsh web` 或源码启动。解释为何短时间高 star。适合对照 Claude Code/Codex 的 skill/plugin 模型。 | https://juejin.cn/post/7684759404727320627 |

#### 收藏热榜

本槽无新增。

### 开发工具

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 14 | [Docker 多阶段构建实践指南](https://juejin.cn/post/7682977354633609243) | 鸿观工坊 | 赞0/藏1/阅104 | 鸿观工坊用 Spring Boot 3 演示 Docker 多阶段构建：builder 阶段 Maven 打包，运行镜像只留产物；先拷 pom 吃缓存。适合个人/中小团队当简易 CI，无 AI 增量。 | https://juejin.cn/post/7682977354633609243 |
| 15 | [受够微信偷偷更新，我做了一个 Windows 微信更新屏蔽工具](https://juejin.cn/post/7685317187398664238) | 张海潮 | 赞1/藏0/阅47 | 张海潮开源 wechat-update-blocker：屏蔽 Windows 微信 4.x / xwechat 自动更新。禁止单个更新 EXE 不够，更新通道比设置开关更深。个人工具，注意安全与条款。 | https://juejin.cn/post/7685317187398664238 |

#### 收藏热榜

本槽无新增。


### 跨榜重复与去重说明

- 本轮新摘要 URL 数：11
- 因 `seen_urls` 跳过：109（只给数量；不要把已见文再展开成表行）
- 同文多标签/双榜出现：无

### 来源清单

- 快照日：2026-09-15（Asia/Shanghai）
- 页面：https://juejin.cn/hot/articles 、 https://juejin.cn/hot/collected-articles
- 抓取：`tools/juejin_hot_fetch.py` → `_staging_latest.json`

| 标签 | 榜单 | 标题 | 链接 |
| --- | --- | --- | --- |
| 后端 | 文章热榜 | 被吹上天的 JWT，为什么主流网站一个都不用 | https://juejin.cn/post/7684261460002701338 |
| 后端 | 文章热榜 | 只备份一个 schema，别把整库都搬走 | https://juejin.cn/post/7685224902321848358 |
| 后端 | 文章热榜 | Kafka已正式接入AI | https://juejin.cn/post/7684573646439317514 |
| 前端 | 文章热榜 | DeepSeek 官方仓库惊现 DeepSeek Harness 桌面端！ | https://juejin.cn/post/7685188623412133898 |
| 前端 | 文章热榜 | 倒反天罡！押注 React Native 6 年后，Shopify 又回到了原生开发 | https://juejin.cn/post/7683784267847925787 |
| 人工智能 | 文章热榜 | 代码80%是AI写的，这家AI公司呼吁暂停AI开发 | https://juejin.cn/post/7684228650583375878 |
| 人工智能 | 文章热榜 | DeepSeek 这波操作很凶 | https://juejin.cn/post/7684154085232017443 |
| 人工智能 | 文章热榜 | 5000亿估值冲刺科创板，DeepSeek 为何急着上市？ | https://juejin.cn/post/7684102772083195958 |
| 人工智能 | 文章热榜 | Deepseek Harness 架构解析和应用 | https://juejin.cn/post/7684759404727320627 |
| 开发工具 | 文章热榜 | Docker 多阶段构建实践指南 | https://juejin.cn/post/7682977354633609243 |
| 开发工具 | 文章热榜 | 受够微信偷偷更新，我做了一个 Windows 微信更新屏蔽工具 | https://juejin.cn/post/7685317187398664238 |

## 2026-09-14

### 今日总览

**一句话结论**：`2026-09-14` 新 URL 主线是 **DeepSeek Harness/V4.1 Flash + WorkBuddy/Skills 产品化**，工程向关注 **先盘工作流再选模型、Dart Skills CLI、浏览器自动化坑**。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 文章热榜 + 收藏热榜 × 后端/前端/人工智能/开发工具 |
| 榜单规模 | 每槽最多 15 条；列表总条数 120；去重后新 URL **25**；跳过已见 **95**；详情成功 25 / 失败 0 |
| 核心趋势 | 1）AI/工具槽继续消化 DeepSeek Flash 与国产 Agent 工作台；2）前端热文偏情绪与小程序账本；3）收藏榜补 Agent 概念面经和浏览器自动化 |
| 可直接关注 | [不要先问用哪个 AI](https://juejin.cn/post/7683020866855632906)；[Dart Skills CLI 1.0](https://juejin.cn/post/7684080641566867471)；[WorkBuddy 技术拆解](https://juejin.cn/post/7684313635775004712)；[DeepSeek 桌面端 vs WebUI](https://juejin.cn/post/7683816340574945343) |

### 后端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 2 | [SQL Server数据库迁移：V9R4C019 如何接住存量 T-SQL 批处理](https://juejin.cn/post/7683830679906287643) | 一只牛博 | 赞1/藏1/阅3700 | 牛博把 SQL Server 迁移看成「语义对位」：先保住 MERGE / DML OUTPUT / 窗口函数 / PIVOT / LIKE，而不是按文件数估工期。V9R4C019 补这些高频 T-SQL，存量批处理才有少改业务语义的条件。适合做异构库迁移的人。 | https://juejin.cn/post/7683830679906287643 |
| 6 | [跟 WebUI 说再见了，最强 DeepSeek 桌面端来了！](https://juejin.cn/post/7683816340574945343) | cxuanAI | 赞12/藏10/阅2110 | cxuanAI 认为 DeepSeek Harness 的 WebUI 不适合当日常 Agent：浏览器管不好长期会话。对比 CLI 编排与桌面端「项目/会话/进程」收口。观点文，产品形态选择参考，不是官方发版说明。 | https://juejin.cn/post/7683816340574945343 |
| 11 | [10 MB 的 Postman 替代品，启动不到 1 秒](https://juejin.cn/post/7683086663756693554) | 小奏技术 | 赞2/藏4/阅291 | 小奏介绍 RustFox：Rust+Tauri 2+Vue 的本地优先 API 客户端，安装包约 10MB、启动亚秒级，对标 Postman 的体积和启动成本。适合本地调试，先看 Collection 兼容再替换团队流程。 | https://juejin.cn/post/7683086663756693554 |
| 13 | [DeepSeek V4.1 Flash 正式发布！](https://juejin.cn/post/7683784267848122395) | cxuanAI | 赞3/藏0/阅317 | cxuanAI 解读 DeepSeek V4.1 Flash 正式版：官方跑分对标 Opus 5 / GPT-5.6 Sol；552B MoE，输入激活 8B / 输出 16B，另有 196B Engram 条件记忆；原生多模态。数字以官方技术报告为准。 | https://juejin.cn/post/7683784267848122395 |
| 14 | [Go 还是 Golang？可能你一直都搞错了！](https://juejin.cn/post/7683700156294873134) | 江湖十年 | 赞5/藏1/阅224 | 江湖十年考证 Go vs Golang：语言官方名是 Go，Golang 来自域名/搜索妥协。严肃但无工程增量，扫一眼即可。 | https://juejin.cn/post/7683700156294873134 |

#### 收藏热榜

本槽无新增。

### 前端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 9 | [2025，记住这一年！它是古法编程的最后一年。](https://juejin.cn/post/7683846471338885171) | 阳火锅 | 赞25/藏8/阅1024 | 阳火锅随笔：自称 2025 年后不再手写前端，只审 AI 补丁。情绪向「古法编程最后一年」，技术增量有限，略读。 | https://juejin.cn/post/7683846471338885171 |
| 11 | [一个人 + AI 做的小程序，一个月赚了 36 块](https://juejin.cn/post/7683443642279723023) | 好市民_ | 赞8/藏11/阅1087 | 好市民复盘「签小签」小程序满月：31 天自然流量收入 36.21 元，年成本约 144 元。账算得很清楚，适合看流量主现实，不是增长范文。 | https://juejin.cn/post/7683443642279723023 |
| 13 | [从codex转战workbuddy使用一周的感受](https://juejin.cn/post/7684460980934049807) | wing98 | 赞18/藏6/阅762 | wing98 从 Codex 中转站被封切到 WorkBuddy 一周：积分消耗体感偏贵，GLM 5.3 修小 bug 可用。非评测，是账号稳定性驱动的搬家记录。 | https://juejin.cn/post/7684460980934049807 |
| 14 | [DeepSeek V4.1 Flash 来了，明天中午 Flash 降价 60%](https://juejin.cn/post/7683375934587502643) | 乘风gg | 赞3/藏2/阅1011 | 乘风gg 转述 DeepSeek 用量页：V4.1 Flash 上线后、V4.1 Pro 之前，V4 Pro 请求路由到 Flash 并按 Flash 计价。过渡期成本自动下降，对比测试要分开「你点的模型和实际跑的模型」。 | https://juejin.cn/post/7683375934587502643 |
| 15 | [2026 年，你可以从项目中删掉这 5 个 npm 包了](https://juejin.cn/post/7683724457530376198) | 涛涛ing | 赞11/藏12/阅650 | 涛涛ing 主张 2026 可删 5 类 npm：原生 Signals 替状态库、浏览器 API 吞日期/工具/动画等。要按目标浏览器基线验证，不要无脑卸 lodash/dayjs。 | https://juejin.cn/post/7683724457530376198 |

#### 收藏热榜

本槽无新增。

### 人工智能

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 6 | [为什么现在越来越多的开源模型，都“毕业“于 Qwen？](https://juejin.cn/post/7682499191234707497) | 吴佳浩Alben | 赞4/藏7/阅560 | 吴佳浩指出大量「新开源模型」Model Card 写着 Base Model: Qwen。信息传播快过技术理解；评模型先看底座和增量训练，别被标题带跑。 | https://juejin.cn/post/7682499191234707497 |
| 8 | [我用 WorkBuddy 做了一次三巨头年报横向财务分析：从 276 页 PDF 到一张可核验的比较表](https://juejin.cn/post/7683438420874461247) | 倔强的石头_ | 赞2/藏3/阅540 | 石头用 WorkBuddy+GLM 5.1 把三份家电年报做成可核验横向表：记录第一次失败、改配置、验收口径。重点是过程门禁，不是「AI 很厉害」。 | https://juejin.cn/post/7683438420874461247 |
| 10 | [用 AI 做短剧出海，赚麻了！（附 Skill 及教程）](https://juejin.cn/post/7684069447021035562) | 苍何 | 赞4/藏6/阅450 | 苍何讲 AI 短剧出海与 Skill 流水线。偏营销增长，数字多转述媒体；当案例扫，不当市场规模结论。 | https://juejin.cn/post/7684069447021035562 |
| 11 | [迷茫焦虑期，我做了一个带支付带官网的 AI 聊天虚拟恋人 App](https://juejin.cn/post/7683400830063444006) | 北岛贰 | 赞4/藏6/阅245 | 北岛贰记录焦虑期做带支付的虚拟恋人 App。个人项目叙事，技术细节少。 | https://juejin.cn/post/7683400830063444006 |
| 12 | [不要先问“用哪个 AI”，先盘点你的开发工作流](https://juejin.cn/post/7683020866855632906) | 全栈弄潮儿 | 赞9/藏5/阅282 | 全栈弄潮儿：先盘开发工作流再选模型。AI 应进需求澄清/读旧代码/排障，而不只写代码；每次对话留下可复用清单。比工具横评更有复用价值。 | https://juejin.cn/post/7683020866855632906 |
| 13 | [我把苹果发布会里的折叠屏，真的用网页做出来了](https://juejin.cn/post/7684463933702291466) | 雨夜寻晴天 | 赞4/藏2/阅254 | 雨夜用 React+CSS 3D+GSAP 在网页复刻折叠屏展开，无 WebGL。AI 只帮规划。适合前端动效练习。 | https://juejin.cn/post/7684463933702291466 |
| 14 | [什么是 RAG？如何用 RAG 实现一个用户记忆？](https://juejin.cn/post/7683339702867542058) | 2分钟速写快排 | 赞4/藏4/阅208 | 2分钟速写快排用 RAG 做跨对话用户记忆：检索资料库再生成，避免每轮重读全对话。Vibe Coding 场景下把技术栈/布局约定写成可检索记忆。入门向。 | https://juejin.cn/post/7683339702867542058 |
| 15 | [Anthropic一次性锁死十年算力，5170亿美元买什么](https://juejin.cn/post/7682593227544936454) | 计算机魔术师 | 赞4/藏3/阅313 | 计算机魔术师复盘 Anthropic 长期算力租赁叙事（Claude Code/Cowork 拉高 token）。媒体向算力财经文，数字需回官方 Economic Index，不当采购依据。 | https://juejin.cn/post/7682593227544936454 |

#### 收藏热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 14 | [腾讯面试官：“你说你做了一个终端Agent，那说说 LLM 和 Agent的区别，ReAct、MCP、Tool、Memory、Skills？”我信誓旦旦开始背了](https://juejin.cn/post/7667008177453252659) | 沉默王二 | 赞35/藏82/阅2636 | 沉默王二面经体：LLM vs Agent，以及 ReAct/MCP/Tool/Memory/Skills 边界。收藏榜长文，适合面试备课，不是新框架发布。 | https://juejin.cn/post/7667008177453252659 |

### 开发工具

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 1 | [2026年AI编程工具大全，33个主流工具一次看懂](https://juejin.cn/post/7683784267847794715) | 狂师 | 赞5/藏11/阅430 | 狂师盘点 33 个 AI 编程工具（含 TraeWork/豆包工作）。清单体，用来定位官网/仓库，不要当评测。 | https://juejin.cn/post/7683784267847794715 |
| 8 | [WorkBuddy 技术解析：核心并不神秘，真正壁垒在产品化、生态与规模工程](https://juejin.cn/post/7684313635775004712) | MobotStone | 赞3/藏1/阅124 | MobotStone 拆 WorkBuddy：技术上是成熟 harness+MCP+Skills+沙箱的产品化，壁垒在办公场景与规模工程，不在发明新 Agent 架构。可与 Codex 对照产品形态。 | https://juejin.cn/post/7684313635775004712 |
| 12 | [Dart Skills CLI 1.0发布，老刘年初的预言兑现了](https://juejin.cn/post/7684080641566867471) | 程序员老刘 | 赞0/藏0/阅148 | 老刘报道 Dart Skills CLI 1.0：官方博客称可为 package 打包分发 Agent Skills。印证「官方 Skill 会像官方文档一样成为标配」。以 Dart 官方博文为准。 | https://juejin.cn/post/7684080641566867471 |
| 13 | [从产品角度：拆解WorkBuddy 功能](https://juejin.cn/post/7684615074137718824) | MobotStone | 赞4/藏2/阅56 | MobotStone 从产品拆 WorkBuddy：连接器=接工具，技能=教方法，专家=定角色，专家团=协作，灵感=抄方案。适合第一次打开产品的人。 | https://juejin.cn/post/7684615074137718824 |
| 14 | [5个Skills，一个人干一个团队的活](https://juejin.cn/post/7683384640531841059) | 周一同学Zelina | 赞0/藏0/阅119 | 周一同学用秒哒 5 个 Skill 对应资料/客户/数据/PPT/视觉。演示「一人多角色 + Skill」，偏产品测评。 | https://juejin.cn/post/7683384640531841059 |

#### 收藏热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 14 | [比 Playwright 更给力，推荐一个AI Agent的浏览器自动化开源项目！](https://juejin.cn/post/7657076812560367626) | 狂师 | 赞10/藏15/阅426 | 狂师推荐比 Playwright 更贴 Agent 的浏览器自动化开源项目：针对登录态、验证码、反爬。Agent 用干净浏览器会被拦。先核项目活跃度再接入。 | https://juejin.cn/post/7657076812560367626 |


### 跨榜重复与去重说明

- 本轮新摘要 URL 数：25
- 因 `seen_urls` 跳过：95（只给数量；不要把已见文再展开成表行）
- 同文多标签/双榜出现：无

### 来源清单

- 快照日：2026-09-14（Asia/Shanghai）
- 页面：https://juejin.cn/hot/articles 、 https://juejin.cn/hot/collected-articles
- 抓取：`tools/juejin_hot_fetch.py` → `_staging_latest.json`

| 标签 | 榜单 | 标题 | 链接 |
| --- | --- | --- | --- |
| 后端 | 文章热榜 | SQL Server数据库迁移：V9R4C019 如何接住存量 T-SQL 批处理 | https://juejin.cn/post/7683830679906287643 |
| 后端 | 文章热榜 | 跟 WebUI 说再见了，最强 DeepSeek 桌面端来了！ | https://juejin.cn/post/7683816340574945343 |
| 后端 | 文章热榜 | 10 MB 的 Postman 替代品，启动不到 1 秒 | https://juejin.cn/post/7683086663756693554 |
| 后端 | 文章热榜 | DeepSeek V4.1 Flash 正式发布！ | https://juejin.cn/post/7683784267848122395 |
| 后端 | 文章热榜 | Go 还是 Golang？可能你一直都搞错了！ | https://juejin.cn/post/7683700156294873134 |
| 前端 | 文章热榜 | 2025，记住这一年！它是古法编程的最后一年。 | https://juejin.cn/post/7683846471338885171 |
| 前端 | 文章热榜 | 一个人 + AI 做的小程序，一个月赚了 36 块 | https://juejin.cn/post/7683443642279723023 |
| 前端 | 文章热榜 | 从codex转战workbuddy使用一周的感受 | https://juejin.cn/post/7684460980934049807 |
| 前端 | 文章热榜 | DeepSeek V4.1 Flash 来了，明天中午 Flash 降价 60% | https://juejin.cn/post/7683375934587502643 |
| 前端 | 文章热榜 | 2026 年，你可以从项目中删掉这 5 个 npm 包了 | https://juejin.cn/post/7683724457530376198 |
| 人工智能 | 文章热榜 | 为什么现在越来越多的开源模型，都“毕业“于 Qwen？ | https://juejin.cn/post/7682499191234707497 |
| 人工智能 | 文章热榜 | 我用 WorkBuddy 做了一次三巨头年报横向财务分析：从 276 页 PDF 到一张可核验的比较表 | https://juejin.cn/post/7683438420874461247 |
| 人工智能 | 文章热榜 | 用 AI 做短剧出海，赚麻了！（附 Skill 及教程） | https://juejin.cn/post/7684069447021035562 |
| 人工智能 | 文章热榜 | 迷茫焦虑期，我做了一个带支付带官网的 AI 聊天虚拟恋人 App | https://juejin.cn/post/7683400830063444006 |
| 人工智能 | 文章热榜 | 不要先问“用哪个 AI”，先盘点你的开发工作流 | https://juejin.cn/post/7683020866855632906 |
| 人工智能 | 文章热榜 | 我把苹果发布会里的折叠屏，真的用网页做出来了 | https://juejin.cn/post/7684463933702291466 |
| 人工智能 | 文章热榜 | 什么是 RAG？如何用 RAG 实现一个用户记忆？ | https://juejin.cn/post/7683339702867542058 |
| 人工智能 | 文章热榜 | Anthropic一次性锁死十年算力，5170亿美元买什么 | https://juejin.cn/post/7682593227544936454 |
| 开发工具 | 文章热榜 | 2026年AI编程工具大全，33个主流工具一次看懂 | https://juejin.cn/post/7683784267847794715 |
| 开发工具 | 文章热榜 | WorkBuddy 技术解析：核心并不神秘，真正壁垒在产品化、生态与规模工程 | https://juejin.cn/post/7684313635775004712 |
| 开发工具 | 文章热榜 | Dart Skills CLI 1.0发布，老刘年初的预言兑现了 | https://juejin.cn/post/7684080641566867471 |
| 开发工具 | 文章热榜 | 从产品角度：拆解WorkBuddy 功能 | https://juejin.cn/post/7684615074137718824 |
| 开发工具 | 文章热榜 | 5个Skills，一个人干一个团队的活 | https://juejin.cn/post/7683384640531841059 |
| 人工智能 | 收藏热榜 | 腾讯面试官：“你说你做了一个终端Agent，那说说 LLM 和 Agent的区别，ReAct、MCP、Tool、Memory、Skills？”我信誓旦旦开始背了 | https://juejin.cn/post/7667008177453252659 |
| 开发工具 | 收藏热榜 | 比 Playwright 更给力，推荐一个AI Agent的浏览器自动化开源项目！ | https://juejin.cn/post/7657076812560367626 |

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

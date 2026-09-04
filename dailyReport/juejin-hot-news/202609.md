# Juejin Hot Digest

按 Asia/Shanghai 时区汇总掘金文章热榜与收藏热榜（后端 / 前端 / 人工智能 / 开发工具），按文章链接去重并归纳正文。

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

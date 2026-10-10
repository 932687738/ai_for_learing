# Juejin Hot Digest

按 Asia/Shanghai 时区汇总掘金文章热榜与收藏热榜（后端 / 前端 / 人工智能 / 开发工具），按文章链接去重并归纳正文。

## 2026-10-10

### 今日总览

**一句话结论**：10 月 10 日新文不多，主线是 **图片和配置怎么进后端、沙箱是什么，以及几篇 GitHub 速报**；收藏热榜没有未收录链接。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 文章热榜 + 收藏热榜 × 后端/前端/人工智能/开发工具 |
| 榜单规模 | 列表 120；新 URL **34**；跳过已见 **86**；详情成功 34 / 失败 0 |
| 核心趋势 | 1）前端新文落在全栈边界、图片内存和 Nacos 配置；2）人工智能槽在解释沙箱和 Harness 桌面端；3）开发工具槽仍有日榜转载 |
| 可直接关注 | [5MB 图片与内存](https://juejin.cn/post/7693579496969486382)；[nacos-web-config](https://juejin.cn/post/7693757919828901923)；[Agent 沙箱](https://juejin.cn/post/7693805723601764362) |

### 后端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 2 | [🤔同事突然问我：Spring的注解 @Component 和 @Service 有何不同？](https://juejin.cn/post/7694480295002128410) | bug菌 | 赞1/藏1/阅1195 | 面试向整理：@Component 与 @Service 在 Spring 里都是组件扫描的标记，@Service 多一层语义，方便按层识别。作者从源码习惯讲差别，没有新的框架行为。 | https://juejin.cn/post/7694480295002128410 |
| 3 | [AI时代建议学点自己真正感兴趣的！](https://juejin.cn/post/7694299604674297891) | 程序员飞鱼 | 赞30/藏1/阅383 | 随笔，谈 AI 写代码已经让在职程序员感到岗位压力。没有方法或数据，适合当情绪记录，不适合当技术结论。 | https://juejin.cn/post/7694299604674297891 |
| 6 | [GROUP BY 先别想当然，查汇总前把规则跑清楚](https://juejin.cn/post/7694121230733246499) | 一只牛博 | 赞0/藏0/阅814 | 统计 SQL 能跑完也会错。文章要求在写 GROUP BY 之前先把分组键、过滤时机和汇总口径跑清楚。是 SQL 习惯，不是某个数据库的新版本。 | https://juejin.cn/post/7694121230733246499 |
| 8 | [我写了一个“自动写周报”的脚本，结果被领导表扬了](https://juejin.cn/post/7693915625802907689) | 郭伟豪豪豪彡 | 赞5/藏5/阅422 | 作者用脚本从既有工作记录拼周五周报，并称因此少写重复段落。格式绑在他自己的公司模板上，不能当成通用周报产品。 | https://juejin.cn/post/7693915625802907689 |
| 10 | [我的 QQ 机器人被腾讯反复踢下线，折腾了半个月才搞明白](https://juejin.cn/post/7693049513120186414) | 碎觉崽 | 赞3/藏4/阅350 | 用 NapCat 把 QQ 接进自动化后反复掉线。作者结论是守护脚本在重启，不是腾讯风控。这是个人环境的排查记录。 | https://juejin.cn/post/7693049513120186414 |
| 14 | [线程本地存储 ThreadLocal](https://juejin.cn/post/7692977150127603775) | 斑鸠喳喳 | 赞3/藏5/阅187 | 从用法讲到 ThreadLocal、ThreadLocalMap 和 Entry，并提到线程特有存储。是 Java 源码笔记，提醒用完要移除，避免线程池里残留。 | https://juejin.cn/post/7692977150127603775 |
| 15 | [实战｜用 DeepSeek + SQLite 从零搭建轻量 Text2SQL 查询助手](https://juejin.cn/post/7693414422438248490) | YIAN | 赞4/藏10/阅188 | 用 DeepSeek 加 SQLite 做 Text2SQL：自然语言生成 SQL 再执行。适合看一条轻量链路怎么接，生成 SQL 仍要限制可执行语句。 | https://juejin.cn/post/7693414422438248490 |

#### 收藏热榜

本槽无新增。

### 前端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 1 | [做全栈是前端骗局还是出路？](https://juejin.cn/post/7694107051320311827) | ErpanOmer | 赞23/藏42/阅1986 | 讨论前端是否该借 Serverless 做全栈，方案集中在 Cloudflare Workers、Hono 和 Drizzle。投入产出是作者判断，适合看这条技术栈的边界。 | https://juejin.cn/post/7694107051320311827 |
| 2 | [别用前端思维写后端：一张 5MB 图片，为什么能撑爆内存？](https://juejin.cn/post/7693579496969486382) | 不一样的少年_ | 赞17/藏19/阅1099 | 从前端转到 Go 后，一张 5MB 图片在解码、并发排队和原生内存上把进程撑大。文中给了准入、流式落盘和大图独占。适合处理上传的人，数字要按自己的解码库重测。 | https://juejin.cn/post/7693579496969486382 |
| 3 | [🚀 nacos-web-config：运营半夜改条配置，网页秒更新 —— 不用发版、不用轮询，我把它开源了](https://juejin.cn/post/7693757919828901923) | 秋天的一阵风 | 赞8/藏12/阅1172 | nacos-web-config 让页面直接吃 Nacos 配置，改配置后不用发版、也不轮询。作者已开源。适合运营改文案，密钥和权限不要放进前端可读的配置。 | https://juejin.cn/post/7693757919828901923 |
| 4 | [一个全程 AI 写的小程序「厨菜记」，上线 20 天跑通流量主，收入几块钱，开心得不行](https://juejin.cn/post/7693805723602157578) | 好市民_ | 赞5/藏3/阅784 | 复盘一个全程由 AI 写成的菜谱小程序：上线约 20 天、独立访客和流量主收入都很小。收入是作者自己的数，重点是反馈处理而不是增长方法。 | https://juejin.cn/post/7693805723602157578 |
| 6 | [Blender 建模 + Three.js 展示：和 AI 一起做一个光储充超充站数字孪生大屏](https://juejin.cn/post/7693351700208140288) | 纸片人 | 赞17/藏19/阅481 | 用 Blender 建模、Three.js 在大屏上展示光储充站点。做法是先出模型再在网页里演。适合要赶一版可视化的人，不是数字孪生平台。 | https://juejin.cn/post/7693351700208140288 |
| 8 | [🧐 为什么大厂 RAG 从不用纯向量检索？](https://juejin.cn/post/7694205589761441807) | 秋天的一阵风 | 赞5/藏4/阅657 | 作者认为纯向量检索会漏掉型号和代码关键字，大厂 RAG 会混上关键词。是经验文，没有给出可复现的对照实验。 | https://juejin.cn/post/7694205589761441807 |
| 9 | [后台管理框架存活率大调查（2026版）](https://juejin.cn/post/7694016286322556969) | Hooray | 赞10/藏12/阅504 | 筛了一遍 2026 年还在维护的后台管理框架，看高 star 项目是否还更新。名单会过时，存活与否要以各仓库最近提交为准。 | https://juejin.cn/post/7694016286322556969 |
| 13 | [GraphQL 在国内为什么水土不服？](https://juejin.cn/post/7694187254181494820) | ErpanOmer | 赞6/藏3/阅354 | 认为 GraphQL 要重建缓存、处理 N+1 并推动后端改造，国内团队往往用 REST 加 BFF 更省。是取舍说明，不是 GraphQL 不能用。 | https://juejin.cn/post/7694187254181494820 |
| 14 | [只用 three.js + OpenStreetMap，手搓一个「成都城市 3D」数据大屏](https://juejin.cn/post/7693165008605396992) | 纸片人 | 赞7/藏9/阅342 | 不用地图 SDK，把 OpenStreetMap 预处理成静态 JSON，再用 three.js 生成成都三维，Vue 只画面板。适合看离线数据怎么进网页，城市范围是作者这份数据。 | https://juejin.cn/post/7693165008605396992 |
| 15 | [SVG和Canvas，前端里的两支“画笔”，用的时候怎么选择？](https://juejin.cn/post/7693160537133203471) | 银岭峰爽捞牛牛的大平原火鸡 | 赞4/藏5/阅376 | 比较 SVG 和 Canvas：界面和图标偏 SVG，大量粒子和游戏画面偏 Canvas。是选择标准，没有新的绘图库。 | https://juejin.cn/post/7693160537133203471 |

#### 收藏热榜

本槽无新增。

### 人工智能

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 2 | [国庆七天，AI圈没一天消停](https://juejin.cn/post/7694124645507940379) | 码事漫谈 | 赞26/藏14/阅3152 | 按时间线回顾国庆那几天的模型发布，并提到 10 月 3 日的一封辞职信。是二手综述，具体发布日要回各公司原文，不能替代 AI 日报。 | https://juejin.cn/post/7694124645507940379 |
| 3 | [9、古代没有程序员，但蒲松龄们早就被"裁员"过了](https://juejin.cn/post/7693144953569493043) | 六神啊六神 | 赞20/藏6/阅1127 | 用历史类比谈程序员被替代的焦虑，并提到年龄限制和裁员新闻。是评论，没有技术做法。 | https://juejin.cn/post/7693144953569493043 |
| 5 | [AI 帮我投资 85 天，最多赚到 3733 元](https://juejin.cn/post/7693414422438723626) | 过客12345 | 赞4/藏6/阅1173 | 一套不选股、不预测、不下单的系统跑了 85 天，作者账户浮盈最高约 3733 元，并说明钱不是系统赚的。适合看它实际做了哪些记录，不能当成收益承诺。 | https://juejin.cn/post/7693414422438723626 |
| 6 | [C盘爆红别乱删！我用 Codex 查出 AppData 占了 87.81GB](https://juejin.cn/post/7693225151681560586) | niaonao | 赞12/藏10/阅786 | 作者让 Codex 装一个磁盘统计技能，8 分钟后指出 AppData 约占 87.81GB。路径和体积是他这台机器的，清理前仍要自己确认。 | https://juejin.cn/post/7693225151681560586 |
| 7 | [DeepSeek Harness 桌面端来啦！更便捷更安全的选择](https://juejin.cn/post/7693712140221792271) | 大模型真好玩 | 赞6/藏3/阅788 | 介绍 DeepSeek Harness 桌面端：免装环境、与 Web 数据互通、不另开本地端口。功能以作者看到的客户端为准，架构细节他说会放在后续篇。 | https://juejin.cn/post/7693712140221792271 |
| 10 | [Agent 天天挂在嘴边的沙箱，到底是个啥？](https://juejin.cn/post/7693805723601764362) | 狂师 | 赞6/藏3/阅618 | 解释 Claude Code、Codex 文档里的沙箱是在限制工具能碰的文件和网络。概念说明，具体策略要看各产品当前文档。 | https://juejin.cn/post/7693805723601764362 |
| 11 | [WorkBuddy悄悄干了件大事，下一代Office真来了！](https://juejin.cn/post/7694131662615117851) | AI袋鼠帝 | 赞4/藏0/阅666 | 从本机文件数量谈到 WorkBuddy 把 Markdown 当成办公载体。产品能力是作者观察，不是 WorkBuddy 的发布说明。 | https://juejin.cn/post/7694131662615117851 |
| 12 | [workbuddy-to-dsh使用教程](https://juejin.cn/post/7692614083904274486) | ianzh | 赞5/藏4/阅585 | workbuddy-to-dsh 用无依赖的 Node 脚本把 WorkBuddy 模型转到 DeepSeek Harness，并带用量、签到和对话测试。适合看中转插件怎么接，密钥不要写进仓库。 | https://juejin.cn/post/7692614083904274486 |
| 15 | [A 社为什么反超了](https://juejin.cn/post/7693481478181584932) | stormzhangV | 赞3/藏2/阅493 | 评论 Anthropic 为何在作者看来追上 Google 和 OpenAI。是观点，没有新的评测表。 | https://juejin.cn/post/7693481478181584932 |

#### 收藏热榜

本槽无新增。

### 开发工具

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 1 | [有了 Parallels Desktop，我终于不用问别人借Windows电脑用了](https://juejin.cn/post/7694490288811376680) | 一只牛博 | 赞0/藏0/阅805 | 作者用 Parallels 在 Mac 上跑 Windows 插件，避免再借一台电脑。偏营销使用体验，略读。 | https://juejin.cn/post/7694490288811376680 |
| 3 | [Flet 1.0 思路很好，可惜来晚了](https://juejin.cn/post/7694481800701542446) | 程序员老刘 | 赞6/藏3/阅240 | Flet 1.0 用 Python 写 Flutter 界面，多端一致。作者认为在模型已经能直接写 Flutter 之后，这个痛点变小了。发布事实要以 Flet 仓库为准。 | https://juejin.cn/post/7694481800701542446 |
| 7 | [GitHub 日榜趋势速报 / 2026-10-08](https://juejin.cn/post/7693579496968978478) | miofly | 赞1/藏1/阅191 | GitHub 日榜转载，日期写的是 2026-10-08。偏聚合，略读。 | https://juejin.cn/post/7693579496968978478 |
| 9 | [GitHub 日榜趋势速报 / 2026-10-09](https://juejin.cn/post/7694124254145724467) | miofly | 赞0/藏0/阅153 | GitHub 日榜转载，日期写的是 2026-10-09。偏聚合，略读。 | https://juejin.cn/post/7694124254145724467 |
| 10 | [Codex插件推荐：Local Figma Agent MCP，不购买付费套餐，也能让 Agent 读懂并修改Figma设计稿](https://juejin.cn/post/7693887055508275234) | Febrie | 赞4/藏1/阅90 | 推荐一个本地 Figma Agent MCP，让 Codex 读和改设计稿而不用付费套餐额度。能力边界以该插件实际暴露的工具为准。 | https://juejin.cn/post/7693887055508275234 |
| 11 | [ChatGPT 账号用户可免费使用 Auto-review 双智能体审查功能](https://juejin.cn/post/7693384474742685746) | miofly | 赞2/藏1/阅87 | 转述 ChatGPT 账号可免费使用 Auto-review：第二个智能体检查主智能体的高风险操作，且不占套餐用量。是否免费要以产品内说明为准，这篇是转载。 | https://juejin.cn/post/7693384474742685746 |
| 13 | [GitHub 今日推荐｜lightcraft：纯 Rust 重写的 RAW 照片开发工具](https://juejin.cn/post/7693383473919361075) | miofly | 赞0/藏0/阅150 | 推荐 lightcraft：用 Rust 重写的 RAW 照片工具，对标 Lightroom 的一部分能力。是项目介绍，不是评测。 | https://juejin.cn/post/7693383473919361075 |
| 15 | [EmbeddingGemma 2：740M 参数的多模态嵌入模型，支持本地推理](https://juejin.cn/post/7693383473919508531) | miofly | 赞1/藏0/阅90 | 转述 EmbeddingGemma 2：约 7.4 亿参数的多模态嵌入，可本地推理。发布细节要回 Google 原文，这篇是项目速报。 | https://juejin.cn/post/7693383473919508531 |

#### 收藏热榜

本槽无新增。

### 跨榜重复与去重说明

- 本轮新摘要 URL 数：34
- 因 `seen_urls` 跳过：86
- 同文多标签/双榜出现：无。34 条新 URL 都只出现在对应标签的文章热榜

### 来源清单

- 快照日：2026-10-10（Asia/Shanghai）
- 页面：https://juejin.cn/hot/articles 、 https://juejin.cn/hot/collected-articles
- 抓取：`tools/juejin_hot_fetch.py` → `_staging_latest.json`

| 标签 | 榜单 | 标题 | 链接 |
| --- | --- | --- | --- |
| 后端 | 文章热榜 | 🤔同事突然问我：Spring的注解 @Component 和 @Service 有何不同？ | https://juejin.cn/post/7694480295002128410 |
| 后端 | 文章热榜 | AI时代建议学点自己真正感兴趣的！ | https://juejin.cn/post/7694299604674297891 |
| 后端 | 文章热榜 | GROUP BY 先别想当然，查汇总前把规则跑清楚 | https://juejin.cn/post/7694121230733246499 |
| 后端 | 文章热榜 | 我写了一个“自动写周报”的脚本，结果被领导表扬了 | https://juejin.cn/post/7693915625802907689 |
| 后端 | 文章热榜 | 我的 QQ 机器人被腾讯反复踢下线，折腾了半个月才搞明白 | https://juejin.cn/post/7693049513120186414 |
| 后端 | 文章热榜 | 线程本地存储 ThreadLocal | https://juejin.cn/post/7692977150127603775 |
| 后端 | 文章热榜 | 实战｜用 DeepSeek + SQLite 从零搭建轻量 Text2SQL 查询助手 | https://juejin.cn/post/7693414422438248490 |
| 前端 | 文章热榜 | 做全栈是前端骗局还是出路？ | https://juejin.cn/post/7694107051320311827 |
| 前端 | 文章热榜 | 别用前端思维写后端：一张 5MB 图片，为什么能撑爆内存？ | https://juejin.cn/post/7693579496969486382 |
| 前端 | 文章热榜 | 🚀 nacos-web-config：运营半夜改条配置，网页秒更新 —— 不用发版、不用轮询，我把它开源了 | https://juejin.cn/post/7693757919828901923 |
| 前端 | 文章热榜 | 一个全程 AI 写的小程序「厨菜记」，上线 20 天跑通流量主，收入几块钱，开心得不行 | https://juejin.cn/post/7693805723602157578 |
| 前端 | 文章热榜 | Blender 建模 + Three.js 展示：和 AI 一起做一个光储充超充站数字孪生大屏 | https://juejin.cn/post/7693351700208140288 |
| 前端 | 文章热榜 | 🧐 为什么大厂 RAG 从不用纯向量检索？ | https://juejin.cn/post/7694205589761441807 |
| 前端 | 文章热榜 | 后台管理框架存活率大调查（2026版） | https://juejin.cn/post/7694016286322556969 |
| 前端 | 文章热榜 | GraphQL 在国内为什么水土不服？ | https://juejin.cn/post/7694187254181494820 |
| 前端 | 文章热榜 | 只用 three.js + OpenStreetMap，手搓一个「成都城市 3D」数据大屏 | https://juejin.cn/post/7693165008605396992 |
| 前端 | 文章热榜 | SVG和Canvas，前端里的两支“画笔”，用的时候怎么选择？ | https://juejin.cn/post/7693160537133203471 |
| 人工智能 | 文章热榜 | 国庆七天，AI圈没一天消停 | https://juejin.cn/post/7694124645507940379 |
| 人工智能 | 文章热榜 | 9、古代没有程序员，但蒲松龄们早就被"裁员"过了 | https://juejin.cn/post/7693144953569493043 |
| 人工智能 | 文章热榜 | AI 帮我投资 85 天，最多赚到 3733 元 | https://juejin.cn/post/7693414422438723626 |
| 人工智能 | 文章热榜 | C盘爆红别乱删！我用 Codex 查出 AppData 占了 87.81GB | https://juejin.cn/post/7693225151681560586 |
| 人工智能 | 文章热榜 | DeepSeek Harness 桌面端来啦！更便捷更安全的选择 | https://juejin.cn/post/7693712140221792271 |
| 人工智能 | 文章热榜 | Agent 天天挂在嘴边的沙箱，到底是个啥？ | https://juejin.cn/post/7693805723601764362 |
| 人工智能 | 文章热榜 | WorkBuddy悄悄干了件大事，下一代Office真来了！ | https://juejin.cn/post/7694131662615117851 |
| 人工智能 | 文章热榜 | workbuddy-to-dsh使用教程 | https://juejin.cn/post/7692614083904274486 |
| 人工智能 | 文章热榜 | A 社为什么反超了 | https://juejin.cn/post/7693481478181584932 |
| 开发工具 | 文章热榜 | 有了 Parallels Desktop，我终于不用问别人借Windows电脑用了 | https://juejin.cn/post/7694490288811376680 |
| 开发工具 | 文章热榜 | Flet 1.0 思路很好，可惜来晚了 | https://juejin.cn/post/7694481800701542446 |
| 开发工具 | 文章热榜 | GitHub 日榜趋势速报 / 2026-10-08 | https://juejin.cn/post/7693579496968978478 |
| 开发工具 | 文章热榜 | GitHub 日榜趋势速报 / 2026-10-09 | https://juejin.cn/post/7694124254145724467 |
| 开发工具 | 文章热榜 | Codex插件推荐：Local Figma Agent MCP，不购买付费套餐，也能让 Agent 读懂并修改Figma设计稿 | https://juejin.cn/post/7693887055508275234 |
| 开发工具 | 文章热榜 | ChatGPT 账号用户可免费使用 Auto-review 双智能体审查功能 | https://juejin.cn/post/7693384474742685746 |
| 开发工具 | 文章热榜 | GitHub 今日推荐｜lightcraft：纯 Rust 重写的 RAW 照片开发工具 | https://juejin.cn/post/7693383473919361075 |
| 开发工具 | 文章热榜 | EmbeddingGemma 2：740M 参数的多模态嵌入模型，支持本地推理 | https://juejin.cn/post/7693383473919508531 |

## 2026-10-08

### 今日总览

**一句话结论**：10 月 8 日四榜新文主要在文章热榜，主线是 **Java Agent 运行时、技能/插件和本机调试**；收藏热榜没有未收录的新链接。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 文章热榜 + 收藏热榜 × 后端/前端/人工智能/开发工具 |
| 榜单规模 | 列表 120；新 URL **60**；跳过已见 **60**；详情成功 60 / 失败 0 |
| 核心趋势 | 1）后端在核对 Spring AI Alibaba 是否停更，并写 Go/Rust 边界；2）人工智能槽集中在 Java Agent、MCP 和 Claude Code Mods；3）开发工具槽有大量 GitHub 日榜转载，另有 vConsole MCP 和本地代码搜索 |
| 可直接关注 | [Spring AI Alibaba 停更传闻](https://juejin.cn/post/7693821701955567670)；[Claude Code Mods](https://juejin.cn/post/7691498553260884008)；[dowse / tgrep](https://juejin.cn/post/7691151105851195430)；[vConsole MCP](https://juejin.cn/post/7691270105432784931) |

### 后端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 1 | [Spring AI Alibaba已停更了，Java还有希望吗？](https://juejin.cn/post/7693821701955567670) | 苏三说技术 | 赞16/藏8/阅952 | 作者核对了 spring-ai-alibaba 的 Release：正式版仍停在 2026-03-10 的 v1.1.2.2，并据此反驳「已停更」。结论是仓库在换内核而不是弃坑。Star 数和「换心脏」是作者判断，要以仓库提交记录为准。 | https://juejin.cn/post/7693821701955567670 |
| 2 | [我埋了 8 个假文件，看谁会上钩：12 天 502 次扫描实录](https://juejin.cn/post/7692743066844135433) | 变量探索SEQVEC | 赞1/藏4/阅404 | 作者放了 8 个假敏感文件，12 天收到 502 次访问、119 个独立 IP，扫描最集中的是 .env。来源里有泄露扫描平台和伪装成常见设备的自动化请求。这是个人蜜罐记录，不能外推成全网比例。 | https://juejin.cn/post/7692743066844135433 |
| 3 | [2026年后端开发进化：告别CRUD内卷，拥抱AI原生架构与服务编排新时代](https://juejin.cn/post/7691917465479446591) | ZhenYuChen2000 | 赞4/藏4/阅321 | 文章认为 2026 年的后端价值在服务编排、高可用和把 AI 放进架构，而不是继续堆 CRUD。没有给出可复现的系统或指标，适合当作岗位能力清单，不适合当作架构决策。 | https://juejin.cn/post/7691917465479446591 |
| 4 | [Go 写业务，Rust 扛底盘：一套可落地的混合架构](https://juejin.cn/post/7691152001448820746) | 喵个咪 | 赞5/藏3/阅279 | 用「变化频率 × 延迟敏感度」划分 Go 业务和 Rust 底盘，并比较进程、sidecar、FFI、WASM 四种接法。样本是作者的 RushWind Admin 与 Go 服务共享 proto。成本数字需要在自己的系统里重测。 | https://juejin.cn/post/7691152001448820746 |
| 5 | [给页面加一个 JSON 编辑器：jsoneditor 的功能、配置和接入注意事项](https://juejin.cn/post/7691155417934594074) | 羲云 | 赞5/藏7/阅215 | 介绍轻量 jsoneditor：一个脚本提供结构、思维导图和文本三种视图，并有 Vue 3 与 React 18 适配。作者声明没有做大数据性能和生产长期验证，行为以他看到的源码为准。 | https://juejin.cn/post/7691155417934594074 |
| 6 | [Loop Engineering 保姆级教程 + 项目实战](https://juejin.cn/post/7692336657548279842) | hsfxuebao | 赞2/藏1/阅276 | 用 Claude Code 与 OpenClaw 创始人的公开说法引出 Loop Engineering，再写成保姆级实战。适合了解「人写循环、循环去提示模型」这一句，具体命令要以官方文档为准。 | https://juejin.cn/post/7692336657548279842 |
| 7 | [DuckDB：一个正在改变数据分析方式的数据库](https://juejin.cn/post/7691498553260851240) | 前端小小栈 | 赞1/藏4/阅298 | 把 DuckDB 定义成嵌在进程里的分析库，用 SQL 直接查 CSV、Parquet 或 DataFrame，不必先起一台数据库。适合轻量探查和 AI 侧的本地分析，不是要替换线上 OLTP。 | https://juejin.cn/post/7691498553260851240 |
| 8 | [用 Codex 加速 Java 开发：从代码生成到测试覆盖的完整实战](https://juejin.cn/post/7692058641252237322) | 要努力啊469 | 赞3/藏5/阅205 | 个人经验：用 Codex 写 Spring 模板、补测试，作者称同类功能从 30–40 小时降到 15–20 小时。没有对照实验，时间不能外推；文中仍把 GPT-4 和 Codex 放在一起说。 | https://juejin.cn/post/7692058641252237322 |
| 9 | [Redis 分布式锁：从 2.8 之前到 2.8+，一篇讲透](https://juejin.cn/post/7691898006993010698) | 用户622288404819 | 赞3/藏4/阅198 | 按 Redis 2.8 前后讲分布式锁：早期 SETNX 加 EXPIRE 有两步窗口，2.8 起用 SET NX PX。后半写释放、续期和主从边界，是面试向整理，不是新版本发布。 | https://juejin.cn/post/7691898006993010698 |
| 10 | [百万级数据导出OOM：POI的坑与EasyExcel的流式写入实战（附内存对比）](https://juejin.cn/post/7691585964053512238) | 知守观 | 赞4/藏4/阅183 | 百万行导出时 POI 全量装入内存会 OOM，作者改成 EasyExcel 流式写加分页查询，并提到 CellStyle 数量上限。案例来自作者自己的评估平台，内存对比要以文中实验条件阅读。 | https://juejin.cn/post/7691585964053512238 |
| 11 | [多环境配置治理：开发、测试、生产连接信息如何隔离](https://juejin.cn/post/7691326130512265254) | 倔强的石头_ | 赞0/藏1/阅247 | 围绕金仓数据库，说明开发、测试、生产的连接信息要分开，避免连错库和把密码提交进仓库。做法是环境隔离，不涉及金仓内核。 | https://juejin.cn/post/7691326130512265254 |
| 12 | [只会 Vibe Coding 的程序员，为什么可能会被淘汰？](https://juejin.cn/post/7691234322111660067) | 前端小小栈 | 赞2/藏1/阅146 | 文章认为只会逐条提示模型会碰到上限，提效来自一个人同时看管多个 Agent，并给它们可检查的完成条件。没有实验数据，是观点文。 | https://juejin.cn/post/7691234322111660067 |
| 13 | [DeepSeek Harness 插件开发新手教程](https://juejin.cn/post/7691149921396834354) | 章鱼哥1971 | 赞2/藏3/阅180 | 用一个余额胶囊插件带新手看 DeepSeek Harness、插件和 cordis 的关系，并对照本机目录里的命令。适合第一次写 dsh 插件，路径是作者机器上的。 | https://juejin.cn/post/7691149921396834354 |
| 14 | [Rust/Go/Java/Python/PHP 大比拼：负载下后端框架到底差多少？](https://juejin.cn/post/7693160537133629455) | 狼爷 | 赞4/藏2/阅135 | 汇总 TechEmpower 等公开基准，强调空闲内存不能代表负载下的吞吐和 P99。文中提醒基准是受控环境，选型仍要看自己的并发和延迟。 | https://juejin.cn/post/7693160537133629455 |
| 15 | [Spring Boot 2.1 → 3.5 迁移推演：这个 2018 年的项目会炸在哪](https://juejin.cn/post/7692739051067342857) | 知守观 | 赞2/藏3/阅133 | 用一套 2018 年的 Spring Boot 2.1 源码推演升到 3.5：javax 包名、Springfox、Druid 和 MyBatis-Plus 的改名点。这是推演不是已完成的迁移记录。 | https://juejin.cn/post/7692739051067342857 |

#### 收藏热榜

本槽无新增。

### 前端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 1 | [Node.js 50个优势场景盘点：一个人单干，为啥我多数时候只用它](https://juejin.cn/post/7691227873459028006) | iDao技术魔方 | 赞6/藏19/阅631 | 把 Node.js 的适用面收成 API、胶水层等几类，并写明什么时候不要用。偏选型清单，附作者认为可抄的代码，不是基准测试。 | https://juejin.cn/post/7691227873459028006 |
| 2 | [Vue3 UIKit 实战：把聊天、会话、主题和移动端适配全部封装好](https://juejin.cn/post/7691345821564174363) | codeGoogle | 赞6/藏13/阅621 | 在 Vue 3 里封装聊天 UI：会话未读、置顶、草稿和消息区，而不只是把 IM SDK 接上。适合要做会话列表的人，组件边界以作者这套 UIKit 为准。 | https://juejin.cn/post/7691345821564174363 |
| 3 | [前端转全栈笔记：讲框架之前，先把 TypeScript 这关过了](https://juejin.cn/post/7691835382221389824) | Timmy | 赞7/藏15/阅496 | 前端转全栈时，作者卡在 NestJS 的装饰器和依赖注入，因此先补 TypeScript。是学习笔记，不是框架发布说明。 | https://juejin.cn/post/7691835382221389824 |
| 4 | [ai agent --- mem0 外挂记忆系统](https://juejin.cn/post/7691517675236556854) | snow来了 | 赞4/藏3/阅366 | 介绍 mem0 的三层范围：用户、Agent、单次运行，以及从对话里抽事实。适合给 Agent 外挂记忆时看作用域怎么分，生产写入策略文中没有展开。 | https://juejin.cn/post/7691517675236556854 |
| 5 | [2026-09-27-Qwen-Image-2.1-1660Ti本地部署实战](https://juejin.cn/post/7692143474695569458) | 用户337409692426 | 赞3/藏4/阅411 | 在 6GB 的 1660 Ti 上用 GGUF Q4 跑 Qwen-Image-2.1，再用 int8 权重做加速，作者给出约 2.28 倍。标题日期是 9 月 27 日，这篇是低显存实录，硬件结果不能直接照搬。 | https://juejin.cn/post/7692143474695569458 |
| 6 | [ai agent --- redis 缓存](https://juejin.cn/post/7691450666426286134) | snow来了 | 赞3/藏4/阅372 | 用 Redis 做 Agent 侧缓存，并复述内存、单线程和 epoll。是入门说明，标题里的拼写错误不影响主题，但不要把它当成缓存架构设计。 | https://juejin.cn/post/7691450666426286134 |
| 7 | [pnpm 12 升级实测](https://juejin.cn/post/7691498553261342760) | 独立开发阿平 | 赞1/藏2/阅368 | 作者在同一台机器上比较 pnpm 11.2.2 和 12.8.1，称四项契约没变、迁移成本低。只是一次实测，锁文件和依赖集不同时要自己再跑。 | https://juejin.cn/post/7691498553261342760 |
| 8 | [diff 算法（虚拟 DOM Reconciliation）](https://juejin.cn/post/7692296625806229544) | 前端阿凡 | 赞2/藏4/阅332 | 讲虚拟 DOM 的 diff：在新旧树上找一组增删移，并说明最少操作在理论上很难。是算法笔记，没有绑定某一个框架版本的补丁。 | https://juejin.cn/post/7692296625806229544 |
| 9 | [给 Vue 页面加个 Markdown 编辑器：ME.js 的接入、图片粘贴与音视频](https://juejin.cn/post/7692127219867877414) | 羲云 | 赞6/藏10/阅260 | 在 Vue 页面接入 ME.js，覆盖排版、粘贴图片和音视频，内容以 Markdown 存储。适合后台文章框，不是富文本编辑器的全面评测。 | https://juejin.cn/post/7692127219867877414 |
| 10 | [前端转 NestJS 全栈实践：从表单页面到微信业务系统](https://juejin.cn/post/7691774360802164751) | 花旗蜕变 | 赞4/藏6/阅261 | 后端只有两人时，作者用 NestJS 从表单做到微信侧业务，写了字段联动、服务端校验和支付幂等。是个人全栈实践，幂等细节要按支付渠道再核对。 | https://juejin.cn/post/7691774360802164751 |
| 11 | [Nuxt 中使用 useHead 优化 SEO 与 GEO](https://juejin.cn/post/7692387846459654178) | excel | 赞5/藏4/阅213 | 用 Nuxt 的 useHead 写规范链接和 JSON-LD，让搜索引擎和生成式回答更容易读懂页面。适合做 SEO/GEO 的基础标签，不保证排名。 | https://juejin.cn/post/7692387846459654178 |
| 12 | [后端零改动，给若依换一套现代化前端](https://juejin.cn/post/7692369572608786467) | niyongsheng | 赞2/藏5/阅277 | ruoyi-vue-nys 用 Vue 3.5、Vite 和 TypeScript 重写若依前端，并声明后端 API 不用改。适合要换皮的若依项目，接口兼容要以作者仓库的适配清单为准。 | https://juejin.cn/post/7692369572608786467 |
| 13 | [ai agent --- 文件存储](https://juejin.cn/post/7692274273326579748) | snow来了 | 赞1/藏3/阅280 | 会话里的图片和文档在历史记录中要能再打开，作者把它们放到对象存储。讲的是文件落点，不是对象存储产品对比。 | https://juejin.cn/post/7692274273326579748 |
| 14 | [组合式 API（Composition API）](https://juejin.cn/post/7692042894160511011) | 前端阿凡 | 赞1/藏5/阅245 | 说明 Options API 在组件变大后按选项拆开会散，再转向组合式 API。是 Vue 概念笔记，没有新的框架发布。 | https://juejin.cn/post/7692042894160511011 |
| 15 | [我给 DeepSeek 的编程智能体写了三个插件:余额胶囊、任务面板、番茄钟](https://juejin.cn/post/7692059206256394249) | 章鱼哥1971 | 赞2/藏3/阅212 | 作者给 DeepSeek Harness 写了余额胶囊、任务面板和番茄钟三个插件，用来演示插件由浅到深。适合对照着写，不是 Harness 官方教程。 | https://juejin.cn/post/7692059206256394249 |

#### 收藏热榜

本槽无新增。

### 人工智能

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 1 | [31岁罗福莉，晋升小米最高职级22级](https://juejin.cn/post/7691227873460125734) | 沉默王二 | 赞20/藏6/阅1617 | 梳理小米 MiMo 从 7B 到 V2.6 的迭代、V2.6 的强化学习，以及作者所写的 HySparse2、MiMo Code 和 Desktop。人物职级是标题信息，技术部分要回小米原文核对。 | https://juejin.cn/post/7691227873460125734 |
| 2 | [副业搞起来，小说，漫画，漫剧的成本优化思路](https://juejin.cn/post/7692440533922971667) | 小呆呆666 | 赞13/藏15/阅1361 | 讨论小说、漫画、漫剧的成本，并给出一个 novel_to_comic 技能仓库。偏副业流程，成本数字是作者自己的算法。 | https://juejin.cn/post/7692440533922971667 |
| 3 | [千问偷偷进村修改 token plan 重置周期这个事大家都知道了吧？](https://juejin.cn/post/7691284233897656383) | math4mads | 赞6/藏1/阅478 | 作者称 9 月 28 日晚看到通义千问个人中心的 token plan 重置周期变了，并保留当时剩余额度的截图式描述。这是用户观察，不是阿里云公告。 | https://juejin.cn/post/7691284233897656383 |
| 4 | [Muse 登顶 App Store 第一，SDK 直接开源：AI Agent 开始进入下一个阶段](https://juejin.cn/post/7692296625806508072) | 前端小小栈 | 赞6/藏7/阅666 | 从 Muse 登上 App Store 榜首并开源 SDK 推论 Agent 会从单个 App 走到开发者生态和硬件。榜单名次会变，SDK 能力要以仓库为准。 | https://juejin.cn/post/7692296625806508072 |
| 5 | [LLM 面试必问的 8 个问题，答不上来直接淘汰](https://juejin.cn/post/7691530846752538639) | 怕浪猫 | 赞7/藏14/阅611 | 把 LLM 面试收成推理、工具、记忆等题，面向做 Agent 的人。是题库不是论文，答案需要自己用官方文档校验。 | https://juejin.cn/post/7691530846752538639 |
| 6 | [Space-Bunny 匿名模型观察：0.03 倍积分、1M 上下文，以及模型选型的算术题](https://juejin.cn/post/7691876916195016719) | 小虎AI生活 | 赞5/藏1/阅487 | 观察 WorkBuddy 面板里的匿名模型 Space-Bunny：作者写倍率 0.03、限时折扣和调用榜，并讨论选型时怎么算账。匿名模型的供应方未知，价格以面板当时显示为准。 | https://juejin.cn/post/7691876916195016719 |
| 7 | [云端部署阿里 Qwen-Image-2.1 保姆级教程](https://juejin.cn/post/7691823753387376649) | Cosolar | 赞6/藏3/阅389 | 在云 GPU 上部署 Qwen-Image-2.1，逐步给命令，并标出系统盘写满、显存不够和忘了关机继续扣费。面向没管过 Linux 的人，账单仍取决于所选实例。 | https://juejin.cn/post/7691823753387376649 |
| 8 | [LangSmith：从链路追踪到 RAG 自动化评估](https://juejin.cn/post/7691774360802246671) | 东风破_ | 赞9/藏9/阅298 | 用 LangSmith 看 LangGraph 或 RAG 的节点、检索结果和真正送进模型的提示，并接到自动化评估。讲的是 LangSmith，不是 Langfuse。 | https://juejin.cn/post/7691774360802246671 |
| 9 | [LangChain4j 新手入门实战教程（Java版）](https://juejin.cn/post/7692127219867123750) | dora | 赞7/藏4/阅275 | Java 新手向的 LangChain4j 教程，作者声明接触 Agent 不久。适合看 Java 侧怎么起一个链，错误要以库文档校正。 | https://juejin.cn/post/7692127219867123750 |
| 10 | [MCP 技术分享：从协议握手到 LangGraph 多 Server 调用](https://juejin.cn/post/7691835382220111872) | 码农悟道 | 赞3/藏3/阅300 | 从 MCP 握手写到自己做工具，再用 LangGraph 聚合多个 Server，并比较传输方式。文中有可运行的 Python 示例，生产鉴权要另补。 | https://juejin.cn/post/7691835382220111872 |
| 11 | [2026 年 AI Agent 面试到底考什么？这套题库覆盖了 90% 的高频考点](https://juejin.cn/post/7691231137718353920) | 怕浪猫 | 赞3/藏7/阅317 | 整理 Agent 面试题，从定义写到架构，并称覆盖大部分高频点。是题库，覆盖率是作者估计。 | https://juejin.cn/post/7691231137718353920 |
| 12 | [从零用 Java 构建 AI Agent 框架：JavaManus 设计与实现深度解析](https://juejin.cn/post/7692742889198387200) | 狼爷 | 赞4/藏3/阅218 | 用自建项目 JavaManus 拆 ReAct 循环、工具编排和记忆。适合看一个 Java Agent 的模块边界，不是 Spring AI 官方框架。 | https://juejin.cn/post/7692742889198387200 |
| 13 | [用纯 Java 做一个企业级 Agent Harness 平台：BizBuddy 的设计与取舍](https://juejin.cn/post/7692084224499367971) | 长弓三石 | 赞3/藏4/阅238 | BizBuddy 用 AgentScope 2.0.3 做内核、若依做业务底座，做入口智能体和专家路由。版本号以作者所写为准，企业级是项目自称。 | https://juejin.cn/post/7692084224499367971 |
| 14 | [Personal Agent 火了，新酿还是旧酒？](https://juejin.cn/post/7691717198448148518) | 飞哥数智谈 | 赞3/藏4/阅207 | 认为个人 Agent 的长期记忆和主动执行并不新，变化在产品形态，并从 OpenClaw、Work 谈到 Muse。是评论，不是产品发布说明。 | https://juejin.cn/post/7691717198448148518 |
| 15 | [Claude Code Mods 是什么：给 Claude 加工具、在终端画界面](https://juejin.cn/post/7691498553260884008) | ZzT | 赞3/藏1/阅218 | 说明 Claude Code 2.1.287 的 Mods 能注册工具并在终端画界面，这是钩子做不到的，并用一个防误删插件演示。版本能力与 AI 日报里的 v2.1.287 一致，演示是作者插件。 | https://juejin.cn/post/7691498553260884008 |

#### 收藏热榜

本槽无新增。

### 开发工具

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 1 | [GitHub 周榜趋势速报 / 2026-10-02](https://juejin.cn/post/7691399863522918438) | miofly | 赞2/藏1/阅209 | GitHub 周榜转载，列出 2026-10-02 这一周 Star 增速靠前的仓库。偏聚合，略读；具体项目要回 GitHub 看。 | https://juejin.cn/post/7691399863522918438 |
| 2 | [「vConsole MCP🛠️」我让 AI 直接看见任何 H5 的日志和请求帮你 debug](https://juejin.cn/post/7691270105432784931) | JustHappy | 赞3/藏2/阅199 | 作者做了 vConsole MCP，让模型读到手机 H5 的日志和请求，用来补跨端调试。适合在真机页面上排错，权限范围要看这个 MCP 实际暴露了什么。 | https://juejin.cn/post/7691270105432784931 |
| 3 | [GitHub 日榜趋势速报 / 2026-10-07](https://juejin.cn/post/7693049513120661550) | miofly | 赞3/藏3/阅138 | GitHub 日榜转载，日期写的是 2026-10-07。偏聚合，略读。 | https://juejin.cn/post/7693049513120661550 |
| 4 | [单片机底层系列：C 库运行时——从 libspace 到多任务与中断安全](https://juejin.cn/post/7692881705649193001) | oku62089 | 赞0/藏0/阅203 | 从 libspace 比较 ARM C 库和 Newlib，用错误码、堆损坏和 HardFault 实验说明多任务和中断里的 C 库安全。面向单片机，不是主机端工具链新闻。 | https://juejin.cn/post/7692881705649193001 |
| 5 | [Agent 开发框架深度对比——LangGraph、AutoGen、CrewAI 与 Microsoft Agent Framework 该选谁](https://juejin.cn/post/7692612898275967002) | 为你学会写情书 | 赞3/藏2/阅146 | 比较 LangGraph、AutoGen、CrewAI 和 Microsoft Agent Framework 的选型。作者把时间定在 2026 年，结论会随各框架版本变，要用当前文档复核。 | https://juejin.cn/post/7692612898275967002 |
| 6 | [GitHub 今日推荐｜archify：AI 代理自动生成可交互架构图的技能模块](https://juejin.cn/post/7691231869480566830) | miofly | 赞2/藏1/阅161 | 推荐 archify：给编码代理用的技能，把系统描述或仓库收成一份自包含的 HTML 架构图。是 GitHub 项目推荐，图的正确性取决于仓库解析。 | https://juejin.cn/post/7691231869480566830 |
| 7 | [GitHub 日榜趋势速报 / 2026-10-02](https://juejin.cn/post/7691231869480288302) | miofly | 赞1/藏1/阅195 | GitHub 日榜转载，日期写的是 2026-10-02。偏聚合，略读。 | https://juejin.cn/post/7691231869480288302 |
| 8 | [万物皆插件：DeepSeek Harness 底层揭秘，脚手架如何蜕变为产品](https://juejin.cn/post/7693225151681396746) | MobotStone | 赞2/藏1/阅116 | 把 DeepSeek Harness 解释成「运行框架才是产品」，并写到 8 月 13 日的开源和 MIT 许可。日期是作者叙述，插件模型要回官方仓库。 | https://juejin.cn/post/7693225151681396746 |
| 9 | [GitHub 今日推荐｜lipflow：无麦克风唇读文字输入工具](https://juejin.cn/post/7692059206256738313) | miofly | 赞3/藏1/阅118 | 推荐 lipflow：本地用摄像头做唇读输入，不依赖麦克风。是项目推荐，识别效果要以仓库说明为准。 | https://juejin.cn/post/7692059206256738313 |
| 10 | [GitHub 日榜趋势速报 / 2026-10-03](https://juejin.cn/post/7691479433083142171) | miofly | 赞0/藏0/阅150 | GitHub 日榜转载，日期写的是 2026-10-03。偏聚合，略读。 | https://juejin.cn/post/7691479433083142171 |
| 11 | [GitHub 日榜趋势速报 / 2026-10-06](https://juejin.cn/post/7692863129294716966) | miofly | 赞2/藏2/阅102 | GitHub 日榜转载，日期写的是 2026-10-06。偏聚合，略读。 | https://juejin.cn/post/7692863129294716966 |
| 12 | [一部手机开发安卓 App：让写代码和看效果都舒服起来](https://juejin.cn/post/7692440533922693139) | 编码生活禅意录 | 赞1/藏0/阅42 | 只用安卓手机开发 App：构建和测试放在服务器，手机上看入口和结果，并配合终端与 Agent。是一条工作流，不是新的 IDE 发布。 | https://juejin.cn/post/7692440533922693139 |
| 13 | [GitHub 日榜趋势速报 / 2026-10-04](https://juejin.cn/post/7692229946185531442) | miofly | 赞0/藏0/阅105 | GitHub 日榜转载，日期写的是 2026-10-04。偏聚合，略读。 | https://juejin.cn/post/7692229946185531442 |
| 14 | [GitHub 今日推荐｜REDox：64 位 token 表示结构化数据，内存占用降 70% 支持多格式互转](https://juejin.cn/post/7691766112886816819) | miofly | 赞0/藏0/阅101 | 推荐 REDox：用 64 位 token 表示结构化数据，作者称内存占用下降约 70%，并做多格式读写。数字来自项目说明，要在自己的数据上复测。 | https://juejin.cn/post/7691766112886816819 |
| 15 | [我把微软开源的 tgrep 做成了本地版 GitHub Code Search：45,629 个文件里搜一次 10ms](https://juejin.cn/post/7691151105851195430) | 张宏宇 | 赞0/藏2/阅104 | dowse 用微软开源的 tgrep 做本地跨仓库搜索，作者在 45629 个文件的一次查询里只读了 73 个文件、约 10 毫秒，并支持 GitHub Code Search 语法。这是本地索引，不是 GitHub 托管搜索，也不是代码知识图谱。 | https://juejin.cn/post/7691151105851195430 |

#### 收藏热榜

本槽无新增。

### 跨榜重复与去重说明

- 本轮新摘要 URL 数：60
- 因 `seen_urls` 跳过：60（只计数量）
- 同文多标签/双榜出现：无。60 条新 URL 都只出现在对应标签的文章热榜

### 来源清单

- 快照日：2026-10-08（Asia/Shanghai）
- 页面：https://juejin.cn/hot/articles 、 https://juejin.cn/hot/collected-articles
- 抓取：`tools/juejin_hot_fetch.py` → `_staging_latest.json`

| 标签 | 榜单 | 标题 | 链接 |
| --- | --- | --- | --- |
| 后端 | 文章热榜 | Spring AI Alibaba已停更了，Java还有希望吗？ | https://juejin.cn/post/7693821701955567670 |
| 后端 | 文章热榜 | 我埋了 8 个假文件，看谁会上钩：12 天 502 次扫描实录 | https://juejin.cn/post/7692743066844135433 |
| 后端 | 文章热榜 | 2026年后端开发进化：告别CRUD内卷，拥抱AI原生架构与服务编排新时代 | https://juejin.cn/post/7691917465479446591 |
| 后端 | 文章热榜 | Go 写业务，Rust 扛底盘：一套可落地的混合架构 | https://juejin.cn/post/7691152001448820746 |
| 后端 | 文章热榜 | 给页面加一个 JSON 编辑器：jsoneditor 的功能、配置和接入注意事项 | https://juejin.cn/post/7691155417934594074 |
| 后端 | 文章热榜 | Loop Engineering 保姆级教程 + 项目实战 | https://juejin.cn/post/7692336657548279842 |
| 后端 | 文章热榜 | DuckDB：一个正在改变数据分析方式的数据库 | https://juejin.cn/post/7691498553260851240 |
| 后端 | 文章热榜 | 用 Codex 加速 Java 开发：从代码生成到测试覆盖的完整实战 | https://juejin.cn/post/7692058641252237322 |
| 后端 | 文章热榜 | Redis 分布式锁：从 2.8 之前到 2.8+，一篇讲透 | https://juejin.cn/post/7691898006993010698 |
| 后端 | 文章热榜 | 百万级数据导出OOM：POI的坑与EasyExcel的流式写入实战（附内存对比） | https://juejin.cn/post/7691585964053512238 |
| 后端 | 文章热榜 | 多环境配置治理：开发、测试、生产连接信息如何隔离 | https://juejin.cn/post/7691326130512265254 |
| 后端 | 文章热榜 | 只会 Vibe Coding 的程序员，为什么可能会被淘汰？ | https://juejin.cn/post/7691234322111660067 |
| 后端 | 文章热榜 | DeepSeek Harness 插件开发新手教程 | https://juejin.cn/post/7691149921396834354 |
| 后端 | 文章热榜 | Rust/Go/Java/Python/PHP 大比拼：负载下后端框架到底差多少？ | https://juejin.cn/post/7693160537133629455 |
| 后端 | 文章热榜 | Spring Boot 2.1 → 3.5 迁移推演：这个 2018 年的项目会炸在哪 | https://juejin.cn/post/7692739051067342857 |
| 前端 | 文章热榜 | Node.js 50个优势场景盘点：一个人单干，为啥我多数时候只用它 | https://juejin.cn/post/7691227873459028006 |
| 前端 | 文章热榜 | Vue3 UIKit 实战：把聊天、会话、主题和移动端适配全部封装好 | https://juejin.cn/post/7691345821564174363 |
| 前端 | 文章热榜 | 前端转全栈笔记：讲框架之前，先把 TypeScript 这关过了 | https://juejin.cn/post/7691835382221389824 |
| 前端 | 文章热榜 | ai agent --- mem0 外挂记忆系统 | https://juejin.cn/post/7691517675236556854 |
| 前端 | 文章热榜 | 2026-09-27-Qwen-Image-2.1-1660Ti本地部署实战 | https://juejin.cn/post/7692143474695569458 |
| 前端 | 文章热榜 | ai agent --- redis 缓存 | https://juejin.cn/post/7691450666426286134 |
| 前端 | 文章热榜 | pnpm 12 升级实测 | https://juejin.cn/post/7691498553261342760 |
| 前端 | 文章热榜 | diff 算法（虚拟 DOM Reconciliation） | https://juejin.cn/post/7692296625806229544 |
| 前端 | 文章热榜 | 给 Vue 页面加个 Markdown 编辑器：ME.js 的接入、图片粘贴与音视频 | https://juejin.cn/post/7692127219867877414 |
| 前端 | 文章热榜 | 前端转 NestJS 全栈实践：从表单页面到微信业务系统 | https://juejin.cn/post/7691774360802164751 |
| 前端 | 文章热榜 | Nuxt 中使用 useHead 优化 SEO 与 GEO | https://juejin.cn/post/7692387846459654178 |
| 前端 | 文章热榜 | 后端零改动，给若依换一套现代化前端 | https://juejin.cn/post/7692369572608786467 |
| 前端 | 文章热榜 | ai agent --- 文件存储 | https://juejin.cn/post/7692274273326579748 |
| 前端 | 文章热榜 | 组合式 API（Composition API） | https://juejin.cn/post/7692042894160511011 |
| 前端 | 文章热榜 | 我给 DeepSeek 的编程智能体写了三个插件:余额胶囊、任务面板、番茄钟 | https://juejin.cn/post/7692059206256394249 |
| 人工智能 | 文章热榜 | 31岁罗福莉，晋升小米最高职级22级 | https://juejin.cn/post/7691227873460125734 |
| 人工智能 | 文章热榜 | 副业搞起来，小说，漫画，漫剧的成本优化思路 | https://juejin.cn/post/7692440533922971667 |
| 人工智能 | 文章热榜 | 千问偷偷进村修改 token plan 重置周期这个事大家都知道了吧？ | https://juejin.cn/post/7691284233897656383 |
| 人工智能 | 文章热榜 | Muse 登顶 App Store 第一，SDK 直接开源：AI Agent 开始进入下一个阶段 | https://juejin.cn/post/7692296625806508072 |
| 人工智能 | 文章热榜 | LLM 面试必问的 8 个问题，答不上来直接淘汰 | https://juejin.cn/post/7691530846752538639 |
| 人工智能 | 文章热榜 | Space-Bunny 匿名模型观察：0.03 倍积分、1M 上下文，以及模型选型的算术题 | https://juejin.cn/post/7691876916195016719 |
| 人工智能 | 文章热榜 | 云端部署阿里 Qwen-Image-2.1 保姆级教程 | https://juejin.cn/post/7691823753387376649 |
| 人工智能 | 文章热榜 | LangSmith：从链路追踪到 RAG 自动化评估 | https://juejin.cn/post/7691774360802246671 |
| 人工智能 | 文章热榜 | LangChain4j 新手入门实战教程（Java版） | https://juejin.cn/post/7692127219867123750 |
| 人工智能 | 文章热榜 | MCP 技术分享：从协议握手到 LangGraph 多 Server 调用 | https://juejin.cn/post/7691835382220111872 |
| 人工智能 | 文章热榜 | 2026 年 AI Agent 面试到底考什么？这套题库覆盖了 90% 的高频考点 | https://juejin.cn/post/7691231137718353920 |
| 人工智能 | 文章热榜 | 从零用 Java 构建 AI Agent 框架：JavaManus 设计与实现深度解析 | https://juejin.cn/post/7692742889198387200 |
| 人工智能 | 文章热榜 | 用纯 Java 做一个企业级 Agent Harness 平台：BizBuddy 的设计与取舍 | https://juejin.cn/post/7692084224499367971 |
| 人工智能 | 文章热榜 | Personal Agent 火了，新酿还是旧酒？ | https://juejin.cn/post/7691717198448148518 |
| 人工智能 | 文章热榜 | Claude Code Mods 是什么：给 Claude 加工具、在终端画界面 | https://juejin.cn/post/7691498553260884008 |
| 开发工具 | 文章热榜 | GitHub 周榜趋势速报 / 2026-10-02 | https://juejin.cn/post/7691399863522918438 |
| 开发工具 | 文章热榜 | 「vConsole MCP🛠️」我让 AI 直接看见任何 H5 的日志和请求帮你 debug | https://juejin.cn/post/7691270105432784931 |
| 开发工具 | 文章热榜 | GitHub 日榜趋势速报 / 2026-10-07 | https://juejin.cn/post/7693049513120661550 |
| 开发工具 | 文章热榜 | 单片机底层系列：C 库运行时——从 libspace 到多任务与中断安全 | https://juejin.cn/post/7692881705649193001 |
| 开发工具 | 文章热榜 | Agent 开发框架深度对比——LangGraph、AutoGen、CrewAI 与 Microsoft Agent Framework 该选谁 | https://juejin.cn/post/7692612898275967002 |
| 开发工具 | 文章热榜 | GitHub 今日推荐｜archify：AI 代理自动生成可交互架构图的技能模块 | https://juejin.cn/post/7691231869480566830 |
| 开发工具 | 文章热榜 | GitHub 日榜趋势速报 / 2026-10-02 | https://juejin.cn/post/7691231869480288302 |
| 开发工具 | 文章热榜 | 万物皆插件：DeepSeek Harness 底层揭秘，脚手架如何蜕变为产品 | https://juejin.cn/post/7693225151681396746 |
| 开发工具 | 文章热榜 | GitHub 今日推荐｜lipflow：无麦克风唇读文字输入工具 | https://juejin.cn/post/7692059206256738313 |
| 开发工具 | 文章热榜 | GitHub 日榜趋势速报 / 2026-10-03 | https://juejin.cn/post/7691479433083142171 |
| 开发工具 | 文章热榜 | GitHub 日榜趋势速报 / 2026-10-06 | https://juejin.cn/post/7692863129294716966 |
| 开发工具 | 文章热榜 | 一部手机开发安卓 App：让写代码和看效果都舒服起来 | https://juejin.cn/post/7692440533922693139 |
| 开发工具 | 文章热榜 | GitHub 日榜趋势速报 / 2026-10-04 | https://juejin.cn/post/7692229946185531442 |
| 开发工具 | 文章热榜 | GitHub 今日推荐｜REDox：64 位 token 表示结构化数据，内存占用降 70% 支持多格式互转 | https://juejin.cn/post/7691766112886816819 |
| 开发工具 | 文章热榜 | 我把微软开源的 tgrep 做成了本地版 GitHub Code Search：45,629 个文件里搜一次 10ms | https://juejin.cn/post/7691151105851195430 |

## 2026-10-02

### 今日总览

**一句话结论**：10 月 2 日新 URL 不多，主线是 **聚合边界、内网 Agent 和本地 Excel MCP**；开发工具槽仍有 GitHub 日榜转载。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 文章热榜 + 收藏热榜 × 后端/前端/人工智能/开发工具 |
| 榜单规模 | 列表 120；新 URL **13**；跳过已见 **107**；详情成功 13 / 失败 0 |
| 核心趋势 | 1）后端新文落在 DDD 仓储和 Go 锁，而不是新框架；2）人工智能槽写隔离内网和云端签到；3）收藏榜只新增一篇 WorkBuddy 蓝皮书 |
| 可直接关注 | [ProcessTask 的仓储边界](https://juejin.cn/post/7689030783366103066)；[隔离内网 Agent](https://juejin.cn/post/7690505279806373931)；[smart-excel-mcp](https://juejin.cn/post/7688929298951864335) |

### 后端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- | --- |
| 11 | [甲骨文裁3万、DeepSeek却招150人：后端程序员往哪走，我把这批JD拆了一遍](https://juejin.cn/post/7690440622159560739) | 王中阳讲AI | 赞2/藏2/阅162 | 用裁员和招聘数字对照后端 JD，再翻译成 Agent 技能，并给一个 Go 最小例子。人数是作者整理的，要以公司公告为准。 | https://juejin.cn/post/7690440622159560739 |
| 12 | [3 个 AI Agent 交付一个企业项目：4 人团队 2 个月，我 3 周做完](https://juejin.cn/post/7690841638806421538) | 王中阳讲AI | 赞1/藏1/阅156 | 个人案例：3 个 Agent、3 周、报价 12 万，对照原计划的 4 人 2 个月。没有对照实验，周期不能外推。 | https://juejin.cn/post/7690841638806421538 |
| 14 | [Go语言第十三章(互斥锁，读写锁)](https://juejin.cn/post/7689038880545587215) | 小满zs | 赞2/藏2/阅123 | 协程要改同一块内存时，用 sync 的互斥锁和读写锁，而不是只靠 channel。入门教程。 | https://juejin.cn/post/7689038880545587215 |
| 15 | [聚合边界：为什么 ProcessTask 没有自己的 Repository](https://juejin.cn/post/7689030783366103066) | mldong | 赞3/藏6/阅125 | 仓储数量跟着聚合走，不跟表或类走。引擎接口里虽有 saveTask，并不表示 ProcessTask 是独立聚合。 | https://juejin.cn/post/7689030783366103066 |

#### 收藏热榜

本槽无新增。

### 前端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- | --- |
| 10 | [前端已死？别急，这可能只是所有行业的开始](https://juejin.cn/post/7690545232068870153) | 前端小小栈 | 赞3/藏1/阅318 | 观点文：被改写的是重复任务，不是职业名称。没有新的工具或数据。 | https://juejin.cn/post/7690545232068870153 |
| 13 | [从零实现一个带虚拟滚动的 Select](https://juejin.cn/post/7689656350306959406) | 再吃一根胡萝卜 | 赞2/藏1/阅280 | 下拉要装成千上万条时不要全量渲染。作者从零做虚拟滚动，并对照 el-select-v2 的踩坑。 | https://juejin.cn/post/7689656350306959406 |
| 14 | [WEB 项目如何禁用 F12 等功能](https://juejin.cn/post/7689431365684772904) | farerboy | 赞2/藏4/阅304 | 上线后禁用开发者工具只能提高随意查看的成本，挡不住会绕过的人。适合知道边界再决定要不要做。 | https://juejin.cn/post/7689431365684772904 |
| 15 | [开发自己的第一个MCP--用 AI 智能重构 Excel 处理工作流](https://juejin.cn/post/7688929298951864335) | 去伪存真 | 赞0/藏3/阅330 | 本地 MCP 服务 smart-excel-mcp：扫目录、洗列、按时间戳归档，邮件发送前做预览。适合表格还在人手里传的流程。 | https://juejin.cn/post/7688929298951864335 |

#### 收藏热榜

本槽无新增。

### 人工智能

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- | --- |
| 14 | [隔离内网下 AI Agent 工程实战](https://juejin.cn/post/7690505279806373931) | SFLYQ | 赞6/藏2/阅268 | 国庆整理的内网 Agent 工程笔记，重点是不能随意出网时模型、工具和数据怎么放。细节以正文架构为准。 | https://juejin.cn/post/7690505279806373931 |
| 15 | [把 WorkBuddy 每日签到搬上云端](https://juejin.cn/post/7690056198372376627) | hoLzwEge | 赞1/藏1/阅320 | 把每日签到和派猫猫旅行放到云端定时，大约 00:05 跑，本机关机也能执行。个人自动化，接口变更会失效。 | https://juejin.cn/post/7690056198372376627 |

#### 收藏热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- | --- |
| 15 | [耗时 7 天，我们开源了腾讯 WorkBuddy 实战蓝皮书（建议收藏）](https://juejin.cn/post/7661324464743858219) | 苍何 | 赞48/藏83/阅5463 | 介绍一份开源的 WorkBuddy 实战蓝皮书，并顺带评论 Codex 与 ChatGPT 合并。资料汇总，产品判断要回官方说明。 | https://juejin.cn/post/7661324464743858219 |

### 开发工具

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- | --- |
| 7 | [GitHub 今日推荐｜DiPlay：让 iPhone CarPlay 直连 BYD 车机，无需硬件适配器](https://juejin.cn/post/7691151105850310694) | miofly | 赞1/藏0/阅122 | DiPlay 跑在比亚迪 DiLink 上，用软件完成握手和 AirPlay，支持 USB 与 Wi-Fi。项目介绍，兼容范围要看仓库。 | https://juejin.cn/post/7691151105850310694 |
| 12 | [GitHub 日榜趋势速报 \| 2026-10-01](https://juejin.cn/post/7691156905345679398) | miofly | 赞2/藏3/阅76 | 2026-10-01 的 Star 增速清单，点名 Strata、AIHOT、DiPlay。榜单聚合，略读。 | https://juejin.cn/post/7691156905345679398 |

#### 收藏热榜

本槽无新增。

### 跨榜重复与去重说明

- 本轮新摘要 URL 数：13
- 因 `seen_urls` 跳过：107（只计数量）
- 详情失败：0
- 同文多标签/双榜出现：本轮新 URL 没有跨槽重复

### 来源清单

- 快照日：2026-10-02（Asia/Shanghai）
- 页面：https://juejin.cn/hot/articles 、 https://juejin.cn/hot/collected-articles
- 抓取：`tools/juejin_hot_fetch.py` → `_staging_latest.json`

| 标签 | 榜单 | 标题 | 链接 |
| --- | --- | --- | --- |
| 后端 | 文章热榜 | 甲骨文裁3万、DeepSeek却招150人：后端程序员往哪走，我把这批JD拆了一遍 | https://juejin.cn/post/7690440622159560739 |
| 后端 | 文章热榜 | 3 个 AI Agent 交付一个企业项目：4 人团队 2 个月，我 3 周做完 | https://juejin.cn/post/7690841638806421538 |
| 后端 | 文章热榜 | Go语言第十三章(互斥锁，读写锁) | https://juejin.cn/post/7689038880545587215 |
| 后端 | 文章热榜 | 聚合边界：为什么 ProcessTask 没有自己的 Repository | https://juejin.cn/post/7689030783366103066 |
| 前端 | 文章热榜 | 前端已死？别急，这可能只是所有行业的开始 | https://juejin.cn/post/7690545232068870153 |
| 前端 | 文章热榜 | 从零实现一个带虚拟滚动的 Select | https://juejin.cn/post/7689656350306959406 |
| 前端 | 文章热榜 | WEB 项目如何禁用 F12 等功能 | https://juejin.cn/post/7689431365684772904 |
| 前端 | 文章热榜 | 开发自己的第一个MCP--用 AI 智能重构 Excel 处理工作流 | https://juejin.cn/post/7688929298951864335 |
| 人工智能 | 文章热榜 | 隔离内网下 AI Agent 工程实战 | https://juejin.cn/post/7690505279806373931 |
| 人工智能 | 文章热榜 | 把 WorkBuddy 每日签到搬上云端 | https://juejin.cn/post/7690056198372376627 |
| 人工智能 | 收藏热榜 | 耗时 7 天，我们开源了腾讯 WorkBuddy 实战蓝皮书（建议收藏） | https://juejin.cn/post/7661324464743858219 |
| 开发工具 | 文章热榜 | GitHub 今日推荐｜DiPlay：让 iPhone CarPlay 直连 BYD 车机，无需硬件适配器 | https://juejin.cn/post/7691151105850310694 |
| 开发工具 | 文章热榜 | GitHub 日榜趋势速报 \| 2026-10-01 | https://juejin.cn/post/7691156905345679398 |

## 2026-10-01

### 今日总览

**一句话结论**：10 月 1 日新 URL 的主线是 **Harness 桌面端被拆开、LangGraph 分支被写成图、以及测试/评审用的 Skill 口径**；开发工具槽里有一批 GitHub 日榜转载，阅读价值低于实作文。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 文章热榜 + 收藏热榜 × 后端/前端/人工智能/开发工具 |
| 榜单规模 | 列表 120；新 URL **64**；跳过已见 **56**；详情成功 64 / 失败 0 |
| 核心趋势 | 1）DeepSeek Harness 与 Pi 的对照继续占热榜；2）LangGraph 从简历工作台写到分支汇合；3）日榜和工具类教程稀释了开发工具槽 |
| 可直接关注 | [LangGraph 分支](https://juejin.cn/post/7690468159975637038)；[Harness 与 Pi](https://juejin.cn/post/7688805244534325263)；[打回 AI 的 PR](https://juejin.cn/post/7689029662157668390)；[禁 JOIN](https://juejin.cn/post/7689077368330190899) |

### 后端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 1 | [为什么越来越多人用 OnlyOffice？](https://juejin.cn/post/7689599510955278336) | 苏三说技术 | 赞37/藏35/阅3367 | OnlyOffice 社区版从 9.4.0 起强制轻量模式，原标准模式不再提供。选型时要确认宏、插件和并发是否被轻量档砍掉。 | https://juejin.cn/post/7689599510955278336 |
| 2 | [DeepSeek Harness 出了桌面端？我把它扒了一遍](https://juejin.cn/post/7690197651808616502) | cxuanAI | 赞7/藏8/阅764 | DeepSeek Harness 桌面端在官方声明前被拆出，随后又连夜改版。文中界面以作者截取时的构建为准，不要当成稳定 API。 | https://juejin.cn/post/7690197651808616502 |
| 3 | [读懂LangGraph 的分支执行逻辑](https://juejin.cn/post/7690468159975637038) | Dragon_xjy | 赞3/藏4/阅869 | 同一输入要分叉再汇合时，LangGraph 把分支写成可运行的图，而不是一串 if。适合要看清并行与汇合点的后端编排。 | https://juejin.cn/post/7690468159975637038 |
| 4 | [管理后台数据国际化：不建翻译表、一列 JSON、后端零改动](https://juejin.cn/post/7688579804614361138) | mldong | 赞3/藏7/阅354 | 后台文案放数据库时，语言包帮不上。作者比较翻译表、每语言一列和 JSON 扩展键，选第三种是为了加语言不改表。 | https://juejin.cn/post/7688579804614361138 |
| 5 | [王者荣耀日志组件BqLog为什么这么快之1——高性能实时压缩日志](https://juejin.cn/post/7690401920711655467) | pippocao | 赞5/藏7/阅225 | 手游日志卡在少写、能追、包体小之间。文里把「少打点」和「出事能还原」拆开谈，而不是只压日志级别。 | https://juejin.cn/post/7690401920711655467 |
| 6 | [ Redis 常见的数据类型及底层结构](https://juejin.cn/post/7688910933353054244) | xyLJ | 赞4/藏4/阅235 | 从 SDS、quicklist 到 Set 三态、ZSet 跳表加哈希、Hash 渐进 rehash，按结构讲 Redis 五种类型的内存形态。适合补存储原理，不是运维手册。 | https://juejin.cn/post/7688910933353054244 |
| 7 | [面试官问"你怎么证明它有效"，200个转AI的后端没几个答得上来](https://juejin.cn/post/7690490009979928576) | 王中阳讲AI | 赞3/藏4/阅226 | 用一场模拟面试追问「RAG 准确率提升 30%」的测量口径。重点是离线集、标注和上线对照，而不是简历句式。 | https://juejin.cn/post/7690490009979928576 |
| 8 | [干了 6 年前端，我是怎么一步步转型到 AI 的？](https://juejin.cn/post/7690468159976701998) | 前端小小栈 | 赞3/藏2/阅220 | 作者复盘从前端、Node 基建、数据分析走到企业 Agent 的路径。是个人转型记录，工程步骤不完整。 | https://juejin.cn/post/7690468159976701998 |
| 9 | [为什么 Spring Boot 自动配置了 Redis，还要自己写 RedisTemplate？](https://juejin.cn/post/7690497906533138482) | xyLJ | 赞4/藏4/阅160 | 解释 Spring Boot 已经自动配置 Redis 时，为什么业务仍要自己声明 RedisTemplate，以及自定义 Bean 如何盖掉自动配置。 | https://juejin.cn/post/7690497906533138482 |
| 10 | [秒懂 Rust 的 7 个核心概念](https://juejin.cn/post/7688603862199205930) | RockByte | 赞1/藏5/阅249 | 讨论 Rust 在调查里长期受喜爱、但很多人被编译器劝退的原因。偏学习体验，没有新的语言特性发布。 | https://juejin.cn/post/7688603862199205930 |
| 11 | [idea 插件-把数据库的表画出来](https://juejin.cn/post/7690942973639475200) | 签收日落 | 赞4/藏4/阅167 | 作者谈 AI 问答普及后，自己为什么还写技术博客。观点文，没有可复用的实现。 | https://juejin.cn/post/7690942973639475200 |
| 12 | [同一个审批流引擎，我写了两次：一次 11226 行，一次 7036 行](https://juejin.cn/post/7689030470209896498) | mldong | 赞3/藏6/阅174 | 同一套审批语义写了两遍：内置模块约 1.1 万行，独立引擎约 7 千行。用行数差说明贫血模型和充血模型各自多出来的职责。 | https://juejin.cn/post/7689030470209896498 |
| 13 | [数据平台到底是什么？一篇文章搞懂数据平台开发](https://juejin.cn/post/7689299210249044019) | 前端小小栈 | 赞2/藏3/阅163 | 从业务库出发，串起采集、传输、仓与湖。是数据平台地图，深度停在概念层。 | https://juejin.cn/post/7689299210249044019 |
| 14 | [「一切皆插件」不是口号：手写一个敢上生产的治理管道过滤器](https://juejin.cn/post/7690460679959035947) | 后端LV | 赞4/藏4/阅100 | 把「一切皆插件」落到 FilterContext：顺序契约、短路、异常隔离和数据边界。后半用两个过滤器拼等保审计，强调能跑和敢上线不是一回事。 | https://juejin.cn/post/7690460679959035947 |
| 15 | [大厂禁 JOIN 的真正原因，拆到第四层才清楚](https://juejin.cn/post/7689077368330190899) | 晚安日记wanna | 赞1/藏2/阅146 | 禁 JOIN 的理由不是单条 SQL 慢，而是 join buffer 和分库之后跨库语法不成立。适合正在做分库分表的人。 | https://juejin.cn/post/7689077368330190899 |

#### 收藏热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 15 | [为什么Spring要“抛弃”Feign？](https://juejin.cn/post/7664407325864558628) | 苏三说技术 | 赞66/藏64/阅7173 | 对照 Spring 的 @HttpExchange 和仍在用的 Feign：声明方式接近，但客户端、拦截器和负载均衡不一定原样搬过来。 | https://juejin.cn/post/7664407325864558628 |

### 前端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 1 | [同样叫 Harness，DeepSeek Harness 和 Pi 根本不在同一层](https://juejin.cn/post/7688805244534325263) | ikoala | 赞27/藏30/阅1964 | 对照 DeepSeek Harness 和 Pi 的源码调用链：表面都能调模型和工具，扩展点挂的位置不同。看架构不要只看 README。 | https://juejin.cn/post/7688805244534325263 |
| 2 | [用 GPT-6 Astra 和 Tripo3D 做智慧农业 3D 大屏：从调研到可巡检园区全流程实录](https://juejin.cn/post/7690497704220196883) | 柳杉 | 赞19/藏15/阅902 | 把上一篇智慧厂房的调研到网页化链路换到农业园区，对象改成地块、作物、墒情和水肥。验证的是链路能不能换场景，不是新引擎。 | https://juejin.cn/post/7690497704220196883 |
| 3 | [用 AI 迁项目有多爽？我把 Webpack 迁 Vite 的全过程记下来了](https://juejin.cn/post/7689096640691683343) | CopyCode | 赞8/藏14/阅1054 | 记录用 AI 把 Webpack 迁到 Vite 的过程，重点是保存到编译完成的等待和反复刷新。迁移清单要自己核对，文中时长是作者机器上的体感。 | https://juejin.cn/post/7689096640691683343 |
| 4 | [我重写了整个项目，但没人感谢我！](https://juejin.cn/post/7690869176362270729) | ErpanOmer | 赞13/藏4/阅768 | 大型前端基建迁移做完，绩效仍只是达标。作者认为因果链太长，技术语言没有提前换成业务代价。 | https://juejin.cn/post/7690869176362270729 |
| 5 | [2026年，你终于可以在 `<textarea>` 里定位任意字符了](https://juejin.cn/post/7690190550998007827) | 涛涛ing | 赞11/藏15/阅725 | 自动补全要贴着输入光标，但 input/textarea 拿不到光标坐标。文里拆这个黑盒该在哪一层补测量。 | https://juejin.cn/post/7690190550998007827 |
| 6 | [VibeCoding 一套 Admin 系统，五种技术栈实现](https://juejin.cn/post/7688739949714997288) | 白雾茫茫丶 | 赞7/藏8/阅699 | 一个多栈同构后台：先锁约定，再划清跨端对齐的层，以及 Agent 负责哪一段。附带可抄的 Vibe Coding 配置，但是项目约定不是通用框架。 | https://juejin.cn/post/7688739949714997288 |
| 7 | [同样用 Element Plus，为什么你的后台总有一股“模板味”？](https://juejin.cn/post/7690405198255325234) | Liora_Yvonne | 赞5/藏9/阅671 | 后台功能齐了仍显乱，因为查询、新增、行操作都是主按钮。讲的是层级和信息密度，不是组件库替换。 | https://juejin.cn/post/7690405198255325234 |
| 8 | [我排查了一下午，发现项目打包体积翻倍的元凶是它](https://juejin.cn/post/7690614916369252387) | CopyCode | 赞6/藏4/阅638 | React 18 + Vite 的 H5 生产 JS 约 2MB，路由和 vendor 已拆过。后面讨论继续减肥时该动哪一块，而不是再拆一次路由。 | https://juejin.cn/post/7690614916369252387 |
| 9 | [栗子前端技术周刊第 148 期 - Turborepo 2.11、Chrome 154 iframe、Node.js 26...](https://juejin.cn/post/7689866047096602666) | 晓得迷路了 | 赞6/藏1/阅384 | 前端周刊第 148 期，覆盖 9 月 21 日到 27 日，其中提到 Turborepo 2.11。周刊体，具体变更要回链到上游。 | https://juejin.cn/post/7689866047096602666 |
| 10 | [Flutter 获取 iPhone Duo 预留区位置](https://juejin.cn/post/7688917667420717091) | zeqinjie | 赞8/藏6/阅352 | 把 iOS 当前遮挡区换成 Flutter 窗口坐标里的 Rect，给自定义界面避开摄像头一类局部遮挡。只适用于这个 Duo 预留区问题。 | https://juejin.cn/post/7688917667420717091 |
| 11 | [Next.js+LangGraph.js+ 简历工具AI Agent完整落地](https://juejin.cn/post/7690205250238103567) | 码农悟道 | 赞2/藏5/阅347 | 用 Next.js 和 LangGraph 做简历优化工作台，把可迭代工作流拆开。适合想在前端仓库里接 Agent 的人，后端编排深度有限。 | https://juejin.cn/post/7690205250238103567 |
| 12 | [耗时两周从零搭建私有化企业 RAG 知识库，完整架构与踩坑总结](https://juejin.cn/post/7689030315844419630) | 码农悟道 | 赞5/藏9/阅314 | 用 FastAPI、LangGraph 和 PGVector 做可溯源的私有知识库，写架构选择和第一期踩坑。检索效果数字没有独立评测，不要直接当生产方案。 | https://juejin.cn/post/7689030315844419630 |
| 13 | [ vtable-guild 被收录进 vuejs/awesome-vue 了 🎉](https://juejin.cn/post/7689299285138374692) | parade岁月 | 赞3/藏3/阅212 | 个人 Vue 组件进入 awesome-vue 清单。是发布记录，没有新的组件实现细节。 | https://juejin.cn/post/7689299285138374692 |
| 14 | [AI Native 团队完整开发落地手册](https://juejin.cn/post/7690779187615563776) | tingke | 赞6/藏6/阅225 | 解读 Anthropic 的 AI-native SDLC 手册：问题不是模型能写多少行，而是几小时内生成的代码如何进入现有交付。手册日期是 2026 年 8 月，本文是转述。 | https://juejin.cn/post/7690779187615563776 |
| 15 | [自从有了 AI，我就再也不想拼 UI 了……](https://juejin.cn/post/7690468159975768110) | 亿元程序员 | 赞2/藏2/阅318 | 续写用 Codex 从界面说明生成 PSD 的提示词经验，作者来自游戏主程。偏工作流手记。 | https://juejin.cn/post/7690468159975768110 |

#### 收藏热榜

本槽无新增。

### 人工智能

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 1 | [突发！字节内部大调整，QA直接转研发了？](https://juejin.cn/post/7689818941397778478) | 狂师 | 赞38/藏9/阅6156 | 转述字节部分测试团队把 QA 和研发序列合并、分批转型。组织消息，没有公开的职级制度原文。 | https://juejin.cn/post/7689818941397778478 |
| 2 | [漫话大模型：7 家中国公司被点名「蒸馏」，他们到底偷走了什么？](https://juejin.cn/post/7690769804492341298) | 程序员于老七 | 赞23/藏10/阅1591 | 转述 Anthropic 9 月报告点名七家中国公司蒸馏 Claude。以公司原文为准，这篇是社区复述。 | https://juejin.cn/post/7690769804492341298 |
| 3 | [顶级模型一句话，AI 写出了能玩的 QQ飞车](https://juejin.cn/post/7689377403413430307) | 怕浪猫 | 赞8/藏12/阅982 | 用一句话让模型做出可玩的网页小游戏，再换词做另外两个。展示的是生成幅度，不是可维护的游戏架构。 | https://juejin.cn/post/7689377403413430307 |
| 4 | [非游戏开发者用 AI 做微信小游戏的完整实录：聊天出 MVP、备案 27 天、踩坑](https://juejin.cn/post/7690435049426681898) | 尾巴斯斯 | 赞6/藏7/阅842 | 非游戏开发者用免费额度把微信小游戏从聊天 MVP 做到备案，周期约 27 天。流程记录，不代表审核时长可复制。 | https://juejin.cn/post/7690435049426681898 |
| 5 | [再见了 WebUI，DeepSeek 桌面版真不错。](https://juejin.cn/post/7690490511467544602) | 沉默王二 | 赞6/藏5/阅751 | 实测 DeepSeek Harness 桌面版和 WebUI 的差别、自动更新和登录，并拆插件机制。插件推荐以作者环境为准。 | https://juejin.cn/post/7690490511467544602 |
| 6 | [ZCode 可以自己看微信小程序了](https://juejin.cn/post/7690010257952178218) | 飞哥数智谈 | 赞9/藏14/阅464 | 用 ZCode 改微信小程序时，发现它能驱动开发者工具做运行、截图和再改。重点是 Agent 进入封闭工具链，不是模型榜。 | https://juejin.cn/post/7690010257952178218 |
| 7 | [DHH 震撼发声：手写代码时代落幕，Agent 正重塑软件工程](https://juejin.cn/post/7689061402817265710) | 王若风 | 赞4/藏4/阅587 | 转述 DHH 称 37signals 让 Agent 成为默认写码者。观点转述，没有该公司工程制度的原文链接核验。 | https://juejin.cn/post/7689061402817265710 |
| 8 | [多智能体系统的通信风暴与死锁治理：生产级降级与容灾方案](https://juejin.cn/post/7688585710283014184) | 吴佳浩Alben | 赞10/藏8/阅419 | 谈多智能体的通信风暴和死锁，以及生产里的降级与容灾。系列文章，本篇给出的是治理方向而不是完整代码。 | https://juejin.cn/post/7688585710283014184 |
| 9 | [画 AI 漫画，别只会写“日漫风”：10 种画风、适用故事和可复制提示词](https://juejin.cn/post/7690197651807633462) | 小酒星小杜 | 赞9/藏8/阅397 | 单句提示可以出好看的图，漫画还要交代等待的原因和下一格。讲分镜约束，不是图像模型发布。 | https://juejin.cn/post/7690197651807633462 |
| 10 | [AI 测试 Skill 大全，我日常在用的 25 个，夯爆了！](https://juejin.cn/post/7690414588748464138) | 狂师 | 赞8/藏13/阅418 | 作者把自己的 25 个测试 Skill 按需求到报告串起来。技能是个人仓库资产，换团队要重写入口条件。 | https://juejin.cn/post/7690414588748464138 |
| 11 | [AI时代最大的红利：个人做量化，也能开发出一套适合你的策略](https://juejin.cn/post/7690110881577304079) | 代码北人生 | 赞7/藏15/阅408 | 量化研究背景里使用 AI 时，提醒未来函数、幸存者偏差和手续费漏算。领域经验，不是通用 Agent 教程。 | https://juejin.cn/post/7690110881577304079 |
| 12 | [分享一个做视频的skill，这条白板视频，每一笔都是代码画的](https://juejin.cn/post/7690026779798208547) | 怕浪猫 | 赞7/藏9/阅384 | 一句话交出白板视频技能 whiteboard-video，产物是成片结构而不是文案。技能仓库地址在文中，使用前看输入假设。 | https://juejin.cn/post/7690026779798208547 |
| 13 | [一天一个开源项目（第 227 篇）：Strands Agents Harness SDK —— 从「手写 Agent 循环」到「一行代码拿到生产级 Agent」](https://juejin.cn/post/7689299285138128932) | 冬奇Lab | 赞4/藏9/阅379 | 介绍 Strands Agents（harness-sdk）这一期开源项目，目标是把 Agent 真正跑起来。项目卡片体，细节要回仓库。 | https://juejin.cn/post/7689299285138128932 |
| 14 | [基于Jev的浏览器Agent插件狂揽 21k star，3分钟教你解放双手](https://juejin.cn/post/7690762523469479977) | ServBay | 赞3/藏5/阅341 | 把 Jev 说成离散动作上的判断模型，用来降低浏览器代理的等待。判断模型和生成模型职责不同，延迟数字以厂商说明为准。 | https://juejin.cn/post/7690762523469479977 |
| 15 | [我打回了 AI 写的 PR：新立 3 条规矩，第 1 条就有争议](https://juejin.cn/post/7689029662157668390) | kyriewen | 赞6/藏6/阅296 | 打回 AI 的 PR 看三态是否齐、需求理解有没有随 PR 提交、任务外改动是否零容忍。附打回评论模板，适合做评审口径。 | https://juejin.cn/post/7689029662157668390 |

#### 收藏热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 13 | [Kimi K3太牛了！但老板说API太贵，让我本地化部署，我算完成本，他涨红脸沉默不语了！其实成本不高，三千万足矣。](https://juejin.cn/post/7666482995197722630) | 李剑一 | 赞117/藏84/阅24307 | 以账单和老板反应串起的叙事。偏故事，技术增量弱，略读。 | https://juejin.cn/post/7666482995197722630 |
| 15 | [三年了，为什么 AI 应用还没爆发？](https://juejin.cn/post/7659709059810705462) | 写代码像蔡徐抻 | 赞159/藏81/阅23272 | 从「算力过剩」的市场说法谈到应用何时出现。评论体，没有新的产能或模型数据。 | https://juejin.cn/post/7659709059810705462 |

### 开发工具

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 1 | [《HelloGitHub》第 126 期](https://juejin.cn/post/7689599510956507136) | HelloGitHub | 赞5/藏4/阅487 | HelloGitHub 式的项目清单，覆盖多语言入门仓库。榜单体，略读后按兴趣点进仓库。 | https://juejin.cn/post/7689599510956507136 |
| 2 | [Trae 每天自动签到：Serverless 定时任务完整复盘](https://juejin.cn/post/7688669403517960202) | 夏天要喝冰可乐 | 赞4/藏3/阅364 | 复盘一个只用标准库的 Serverless 定时任务：接口逆向、误导性错误码、失败告警和配额竞争。适合看无人值守任务怎么失败。 | https://juejin.cn/post/7688669403517960202 |
| 3 | [Web自动化测试全景图：20个主流AI自动化工具如何选？（强烈安利）](https://juejin.cn/post/7690869043603292206) | 狂师 | 赞5/藏5/阅154 | Web 自动化不再只是 Playwright 和 Selenium，清单里一半带 AI。作者比较的是选择成本，不是新跑分。 | https://juejin.cn/post/7690869043603292206 |
| 4 | [ 一张图三句需求，我用 Trae Work 做了一块能看日出日落和月相的天文机械表](https://juejin.cn/post/7690504159464505386) | 汉堡大王9527 | 赞3/藏0/阅133 | 在 Trae 里丢一张天文表图片和一句需求，让它做出时分秒、月相和扫秒。是图像到界面的一次试做。 | https://juejin.cn/post/7690504159464505386 |
| 5 | [GitHub 日榜趋势速报 \| 2026-09-29](https://juejin.cn/post/7690415131084406822) | miofly | 赞1/藏1/阅169 | GitHub 日榜转载，日期写 2026-09-29。榜单聚合，略读。 | https://juejin.cn/post/7690415131084406822 |
| 6 | [GitHub 日榜趋势速报 \| 2026-09-30](https://juejin.cn/post/7690839722769563657) | miofly | 赞2/藏0/阅135 | GitHub 日榜转载，日期写 2026-09-30。榜单聚合，略读。 | https://juejin.cn/post/7690839722769563657 |
| 7 | [Hutool之RandomUtil：随机数生成的终极利器](https://juejin.cn/post/7689654965350137899) | 独泪了无痕 | 赞3/藏0/阅90 | 用 Hutool 生成验证码、临时密码一类随机串。工具类用法，没有安全随机数的边界讨论。 | https://juejin.cn/post/7689654965350137899 |
| 8 | [GitHub 日榜趋势速报 \| 2026-09-27](https://juejin.cn/post/7689314158994669614) | miofly | 赞2/藏1/阅101 | GitHub 日榜转载，日期写 2026-09-27。榜单聚合，略读。 | https://juejin.cn/post/7689314158994669614 |
| 9 | [GitHub 日榜趋势速报 \| 2026-09-25](https://juejin.cn/post/7689029662158651430) | miofly | 赞0/藏1/阅155 | GitHub 日榜转载，日期写 2026-09-25，提到 jev-chat-jarvis。榜单聚合，略读。 | https://juejin.cn/post/7689029662158651430 |
| 10 | [GitHub 日榜趋势速报 \| 2026-09-28](https://juejin.cn/post/7689771186259836955) | miofly | 赞0/藏1/阅123 | GitHub 日榜转载，日期写 2026-09-28。榜单聚合，略读。 | https://juejin.cn/post/7689771186259836955 |
| 11 | [开发利器Hutool之MapUtil的使用](https://juejin.cn/post/7689091429970952227) | 独泪了无痕 | 赞1/藏0/阅111 | Hutool MapUtil 对 Map 的创建、过滤、合并做静态封装。API 速查，不是新库发布。 | https://juejin.cn/post/7689091429970952227 |
| 12 | [一个轻量级 AI 代理工具箱，与coding plan 推荐](https://juejin.cn/post/7689314158994964526) | 码头的薯条 | 赞2/藏3/阅96 | 介绍一个对接 coding plan 的轻量代理，用来分发多家模型接口。动机是 token 花费，缺少限额和审计设计。 | https://juejin.cn/post/7689314158994964526 |
| 13 | [【AI】iPhone18抢不到？我用 Codex 做了个苹果库存监控工具](https://juejin.cn/post/7690551361394851882) | JavaDog程序狗 | 赞1/藏0/阅80 | 让 Codex 做苹果库存监控：认接口、辨真假库存、处理 HTTP 541，再包成可双击的程序。是一次个人自动化，库存接口可能变更。 | https://juejin.cn/post/7690551361394851882 |
| 14 | [把 ADB 装进 macOS app    ](https://juejin.cn/post/7689030281899622438) | tangzzzfan | 赞1/藏3/阅81 | 验证 macOS 应用用 Rust sidecar 做 Android 无线调试，避免用户自己装 ADB。还是技术验证，不是成品分布。 | https://juejin.cn/post/7689030281899622438 |
| 15 | [再也不怕手滑丢代码！给 git 高危操作加一层安全校验](https://juejin.cn/post/7689030185367486510) | 用户7330964612309 | 赞1/藏1/阅61 | 讨论 checkout 和 reset --hard 之后如何留退路。面向日常 Git 误操作，不是新的版本控制模型。 | https://juejin.cn/post/7689030185367486510 |

#### 收藏热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 15 | [《HelloGitHub》第 124 期](https://juejin.cn/post/7667084999975862323) | HelloGitHub | 赞24/藏17/阅1224 | 另一期 HelloGitHub 项目清单。榜单体，略读。 | https://juejin.cn/post/7667084999975862323 |

### 跨榜重复与去重说明

- 本轮新摘要 URL 数：64
- 因 `seen_urls` 跳过：56（只计数量）
- 详情失败：0
- 同文多标签/双榜出现：本轮新 URL 没有跨槽重复

### 来源清单

- 快照日：2026-10-01（Asia/Shanghai）
- 页面：https://juejin.cn/hot/articles 、 https://juejin.cn/hot/collected-articles
- 抓取：`tools/juejin_hot_fetch.py` → `_staging_latest.json`

| 标签 | 榜单 | 标题 | 链接 |
| --- | --- | --- | --- |
| 后端 | 文章热榜 | 为什么越来越多人用 OnlyOffice？ | https://juejin.cn/post/7689599510955278336 |
| 后端 | 文章热榜 | DeepSeek Harness 出了桌面端？我把它扒了一遍 | https://juejin.cn/post/7690197651808616502 |
| 后端 | 文章热榜 | 读懂LangGraph 的分支执行逻辑 | https://juejin.cn/post/7690468159975637038 |
| 后端 | 文章热榜 | 管理后台数据国际化：不建翻译表、一列 JSON、后端零改动 | https://juejin.cn/post/7688579804614361138 |
| 后端 | 文章热榜 | 王者荣耀日志组件BqLog为什么这么快之1——高性能实时压缩日志 | https://juejin.cn/post/7690401920711655467 |
| 后端 | 文章热榜 |  Redis 常见的数据类型及底层结构 | https://juejin.cn/post/7688910933353054244 |
| 后端 | 文章热榜 | 面试官问"你怎么证明它有效"，200个转AI的后端没几个答得上来 | https://juejin.cn/post/7690490009979928576 |
| 后端 | 文章热榜 | 干了 6 年前端，我是怎么一步步转型到 AI 的？ | https://juejin.cn/post/7690468159976701998 |
| 后端 | 文章热榜 | 为什么 Spring Boot 自动配置了 Redis，还要自己写 RedisTemplate？ | https://juejin.cn/post/7690497906533138482 |
| 后端 | 文章热榜 | 秒懂 Rust 的 7 个核心概念 | https://juejin.cn/post/7688603862199205930 |
| 后端 | 文章热榜 | idea 插件-把数据库的表画出来 | https://juejin.cn/post/7690942973639475200 |
| 后端 | 文章热榜 | 同一个审批流引擎，我写了两次：一次 11226 行，一次 7036 行 | https://juejin.cn/post/7689030470209896498 |
| 后端 | 文章热榜 | 数据平台到底是什么？一篇文章搞懂数据平台开发 | https://juejin.cn/post/7689299210249044019 |
| 后端 | 文章热榜 | 「一切皆插件」不是口号：手写一个敢上生产的治理管道过滤器 | https://juejin.cn/post/7690460679959035947 |
| 后端 | 文章热榜 | 大厂禁 JOIN 的真正原因，拆到第四层才清楚 | https://juejin.cn/post/7689077368330190899 |
| 后端 | 收藏热榜 | 为什么Spring要“抛弃”Feign？ | https://juejin.cn/post/7664407325864558628 |
| 前端 | 文章热榜 | 同样叫 Harness，DeepSeek Harness 和 Pi 根本不在同一层 | https://juejin.cn/post/7688805244534325263 |
| 前端 | 文章热榜 | 用 GPT-6 Astra 和 Tripo3D 做智慧农业 3D 大屏：从调研到可巡检园区全流程实录 | https://juejin.cn/post/7690497704220196883 |
| 前端 | 文章热榜 | 用 AI 迁项目有多爽？我把 Webpack 迁 Vite 的全过程记下来了 | https://juejin.cn/post/7689096640691683343 |
| 前端 | 文章热榜 | 我重写了整个项目，但没人感谢我！ | https://juejin.cn/post/7690869176362270729 |
| 前端 | 文章热榜 | 2026年，你终于可以在 `<textarea>` 里定位任意字符了 | https://juejin.cn/post/7690190550998007827 |
| 前端 | 文章热榜 | VibeCoding 一套 Admin 系统，五种技术栈实现 | https://juejin.cn/post/7688739949714997288 |
| 前端 | 文章热榜 | 同样用 Element Plus，为什么你的后台总有一股“模板味”？ | https://juejin.cn/post/7690405198255325234 |
| 前端 | 文章热榜 | 我排查了一下午，发现项目打包体积翻倍的元凶是它 | https://juejin.cn/post/7690614916369252387 |
| 前端 | 文章热榜 | 栗子前端技术周刊第 148 期 - Turborepo 2.11、Chrome 154 iframe、Node.js 26... | https://juejin.cn/post/7689866047096602666 |
| 前端 | 文章热榜 | Flutter 获取 iPhone Duo 预留区位置 | https://juejin.cn/post/7688917667420717091 |
| 前端 | 文章热榜 | Next.js+LangGraph.js+ 简历工具AI Agent完整落地 | https://juejin.cn/post/7690205250238103567 |
| 前端 | 文章热榜 | 耗时两周从零搭建私有化企业 RAG 知识库，完整架构与踩坑总结 | https://juejin.cn/post/7689030315844419630 |
| 前端 | 文章热榜 |  vtable-guild 被收录进 vuejs/awesome-vue 了 🎉 | https://juejin.cn/post/7689299285138374692 |
| 前端 | 文章热榜 | AI Native 团队完整开发落地手册 | https://juejin.cn/post/7690779187615563776 |
| 前端 | 文章热榜 | 自从有了 AI，我就再也不想拼 UI 了…… | https://juejin.cn/post/7690468159975768110 |
| 人工智能 | 文章热榜 | 突发！字节内部大调整，QA直接转研发了？ | https://juejin.cn/post/7689818941397778478 |
| 人工智能 | 文章热榜 | 漫话大模型：7 家中国公司被点名「蒸馏」，他们到底偷走了什么？ | https://juejin.cn/post/7690769804492341298 |
| 人工智能 | 文章热榜 | 顶级模型一句话，AI 写出了能玩的 QQ飞车 | https://juejin.cn/post/7689377403413430307 |
| 人工智能 | 文章热榜 | 非游戏开发者用 AI 做微信小游戏的完整实录：聊天出 MVP、备案 27 天、踩坑 | https://juejin.cn/post/7690435049426681898 |
| 人工智能 | 文章热榜 | 再见了 WebUI，DeepSeek 桌面版真不错。 | https://juejin.cn/post/7690490511467544602 |
| 人工智能 | 文章热榜 | ZCode 可以自己看微信小程序了 | https://juejin.cn/post/7690010257952178218 |
| 人工智能 | 文章热榜 | DHH 震撼发声：手写代码时代落幕，Agent 正重塑软件工程 | https://juejin.cn/post/7689061402817265710 |
| 人工智能 | 文章热榜 | 多智能体系统的通信风暴与死锁治理：生产级降级与容灾方案 | https://juejin.cn/post/7688585710283014184 |
| 人工智能 | 文章热榜 | 画 AI 漫画，别只会写“日漫风”：10 种画风、适用故事和可复制提示词 | https://juejin.cn/post/7690197651807633462 |
| 人工智能 | 文章热榜 | AI 测试 Skill 大全，我日常在用的 25 个，夯爆了！ | https://juejin.cn/post/7690414588748464138 |
| 人工智能 | 文章热榜 | AI时代最大的红利：个人做量化，也能开发出一套适合你的策略 | https://juejin.cn/post/7690110881577304079 |
| 人工智能 | 文章热榜 | 分享一个做视频的skill，这条白板视频，每一笔都是代码画的 | https://juejin.cn/post/7690026779798208547 |
| 人工智能 | 文章热榜 | 一天一个开源项目（第 227 篇）：Strands Agents Harness SDK —— 从「手写 Agent 循环」到「一行代码拿到生产级 Agent」 | https://juejin.cn/post/7689299285138128932 |
| 人工智能 | 文章热榜 | 基于Jev的浏览器Agent插件狂揽 21k star，3分钟教你解放双手 | https://juejin.cn/post/7690762523469479977 |
| 人工智能 | 文章热榜 | 我打回了 AI 写的 PR：新立 3 条规矩，第 1 条就有争议 | https://juejin.cn/post/7689029662157668390 |
| 人工智能 | 收藏热榜 | Kimi K3太牛了！但老板说API太贵，让我本地化部署，我算完成本，他涨红脸沉默不语了！其实成本不高，三千万足矣。 | https://juejin.cn/post/7666482995197722630 |
| 人工智能 | 收藏热榜 | 三年了，为什么 AI 应用还没爆发？ | https://juejin.cn/post/7659709059810705462 |
| 开发工具 | 文章热榜 | 《HelloGitHub》第 126 期 | https://juejin.cn/post/7689599510956507136 |
| 开发工具 | 文章热榜 | Trae 每天自动签到：Serverless 定时任务完整复盘 | https://juejin.cn/post/7688669403517960202 |
| 开发工具 | 文章热榜 | Web自动化测试全景图：20个主流AI自动化工具如何选？（强烈安利） | https://juejin.cn/post/7690869043603292206 |
| 开发工具 | 文章热榜 |  一张图三句需求，我用 Trae Work 做了一块能看日出日落和月相的天文机械表 | https://juejin.cn/post/7690504159464505386 |
| 开发工具 | 文章热榜 | GitHub 日榜趋势速报 \| 2026-09-29 | https://juejin.cn/post/7690415131084406822 |
| 开发工具 | 文章热榜 | GitHub 日榜趋势速报 \| 2026-09-30 | https://juejin.cn/post/7690839722769563657 |
| 开发工具 | 文章热榜 | Hutool之RandomUtil：随机数生成的终极利器 | https://juejin.cn/post/7689654965350137899 |
| 开发工具 | 文章热榜 | GitHub 日榜趋势速报 \| 2026-09-27 | https://juejin.cn/post/7689314158994669614 |
| 开发工具 | 文章热榜 | GitHub 日榜趋势速报 \| 2026-09-25 | https://juejin.cn/post/7689029662158651430 |
| 开发工具 | 文章热榜 | GitHub 日榜趋势速报 \| 2026-09-28 | https://juejin.cn/post/7689771186259836955 |
| 开发工具 | 文章热榜 | 开发利器Hutool之MapUtil的使用 | https://juejin.cn/post/7689091429970952227 |
| 开发工具 | 文章热榜 | 一个轻量级 AI 代理工具箱，与coding plan 推荐 | https://juejin.cn/post/7689314158994964526 |
| 开发工具 | 文章热榜 | 【AI】iPhone18抢不到？我用 Codex 做了个苹果库存监控工具 | https://juejin.cn/post/7690551361394851882 |
| 开发工具 | 文章热榜 | 把 ADB 装进 macOS app     | https://juejin.cn/post/7689030281899622438 |
| 开发工具 | 文章热榜 | 再也不怕手滑丢代码！给 git 高危操作加一层安全校验 | https://juejin.cn/post/7689030185367486510 |
| 开发工具 | 收藏热榜 | 《HelloGitHub》第 124 期 | https://juejin.cn/post/7667084999975862323 |

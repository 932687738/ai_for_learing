---
name: juejin-hot-digest
description: Generates a Chinese digest from Juejin hot boards (文章热榜 + 收藏热榜) for 后端/前端/人工智能/开发工具. Fetches list + article body, classifies and summarizes real content with canonical links, and deduplicates by article URL via persistent seen_urls. Use when the user says 拉取掘金热榜, 掘金热文, 更新掘金热榜, 掘金收藏榜, or requests juejin hot digest / force=true. Also runs as the third step when dual-digest-on-pull triggers on 拉取 / 拉取日报 (after ai-daily-digest and knowledge-base-digest), sharing the same date/force choice.
---

# Juejin Hot Digest（掘金热榜摘要）

## 使用场景

当用户提到以下任意意图时使用本 Skill：

- 拉取掘金热榜
- 掘金热文 / 掘金收藏榜
- 更新掘金热榜
- 生成掘金热榜摘要
- 带 `force=true` 的掘金热榜刷新
- **统一「拉取」**：用户说 `拉取` / `拉取一下` / `拉取日报` 等（非 Git）时，由 [`.cursor/rules/dual-digest-on-pull.mdc`](../../rules/dual-digest-on-pull.mdc) 在 AI 日报与知识库之后**同步触发本 Skill**；日期/`force` 与另外两路**共用同一次用户选择**，不要再单独提问

目标：按 Asia/Shanghai 时区，从掘金两个热榜页面拉取指定分类文章，**阅读正文后做分类归纳总结**，写入本地 Markdown，并用状态文件按**文章真实链接**去重，避免对同一地址重复拉取与重复摘要。

## 固定来源（只允许这两页 × 四个标签）

| 榜单 | 页面 | API `type` |
| --- | --- | --- |
| 文章热榜 | https://juejin.cn/hot/articles | `hot` |
| 收藏热榜 | https://juejin.cn/hot/collected-articles | `collect` |

| 标签 | `cate_id` |
| --- | --- |
| 后端 | `6809637769959178254` |
| 前端 | `6809637767543259144` |
| 人工智能 | `6809637773935378440` |
| 开发工具 | `6809637771511070734` |

共 **2 × 4 = 8** 个列表槽位。不要扩展到其他分类或其他站点（除非用户明确要求）。

## 触发后的日期选择

若本次由 **dual-digest-on-pull（统一「拉取」）** 触发：不要单独提问；直接使用用户已给出的 `1` / `2`+日期 / `force=true`（与 AI 日报、知识库相同）。

若用户**仅**请求掘金热榜：除非已明确提供 `force=true` 或已带 `1`/`2`/日期，否则先出示选项并等待选择：

```text
请选择拉取方式：
1. 不指定日期，按增量逻辑拉取（快照日期 = 今天 Asia/Shanghai）
2. 指定日期，仅将该次快照记到某一天章节
```

选择规则：

- 用户回复 `1`：走非 force 增量逻辑（见「日期计算」）。
- 用户回复 `2`：要求 `YYYY-MM-DD`；同一句已带日期可直接用。
- 指定日期模式：快照仍取**当前热榜实时内容**，但写入章节标题为用户指定日；若该日已在 `processed_dates` 或归档/滚动文件已有 `## YYYY-MM-DD`，输出 `该日期已处理，跳过：YYYY-MM-DD`，不抓取、不写入、不更新状态。
- 日期格式无效时要求重填，不要猜测。

## 固定路径

（相对仓库根目录。）

- 目录：`dailyReport/juejin-hot-news`
- 状态文件：`dailyReport/juejin-hot-news/juejin-hot-state.json`
- 滚动入口（仅当前自然月）：`dailyReport/juejin-hot-news/juejin-hot-digest.md`
- 月归档：`dailyReport/juejin-hot-news/YYYYMM.md`
- 抓取暂存（可覆盖，勿当历史归档）：`dailyReport/juejin-hot-news/_staging_latest.json`
- 抓取脚本：`tools/juejin_hot_fetch.py`

目录不存在时先创建。

## 状态文件格式

```json
{
  "last_end_date": "YYYY-MM-DD",
  "last_sync_ymd": "YYYY-MM-DD",
  "processed_dates": ["YYYY-MM-DD"],
  "seen_urls": ["https://juejin.cn/post/ARTICLE_ID"]
}
```

字段规则：

- `last_end_date` / `last_sync_ymd` / `processed_dates`：与 `ai-daily-digest` 同语义（按快照日）。
- **`seen_urls`（特殊逻辑，必须遵守）**：
  - 存文章**真实规范链接**：`https://juejin.cn/post/{article_id}`（去掉 query/hash；统一 https；小写 host）。
  - 跨日期、跨榜单、跨标签**全局去重**。
  - 已在 `seen_urls` 中的链接：**禁止再次请求正文详情、禁止再次写入摘要正文**；可在「跳过已见」统计中记一笔。
  - 仅当某 URL 在本次成功写入 digest 后，才并入 `seen_urls`。
  - `force=true` 时允许重新抓取并覆盖当日章节中对应条目，但仍须用正文重写摘要；写入后 `seen_urls` 保持并集。

## 日期计算

所有日期按 Asia/Shanghai。

热榜是**实时榜**，没有「昨天的榜」归档接口；因此：

1. 设 `today_ymd` 为当前运行日；默认快照日 `snap_ymd = today_ymd`。
2. 非 force 增量：
   - 若状态无 `last_end_date`：处理 `snap_ymd`，并设 `last_sync_ymd = snap_ymd`。
   - 若 `snap_ymd` 已在 `processed_dates`，或月归档/滚动入口已有 `## snap_ymd`：输出 `本次无新资讯`（或指定日跳过文案），**仍可**说明榜上全是已见 URL；不要空跑写章节。
   - 否则处理 `snap_ymd`。
3. 指定日期模式：章节日 = 用户日；去重仍看 `seen_urls`。
4. `force=true`：强制处理最近 1 个快照日（`today_ymd`），或用户指定的单日；允许覆盖该日 Markdown 章节；抓取时对脚本加 `--include-seen` **仅当**需要强制重摘要已见文（默认 force 也优先只拉未见文；若当日无新 URL，可对榜上 Top 条目强制重拉正文以刷新章节）。
5. 非 force 且无新日期 / 无新 URL 可写：

```text
本次无新资讯
```

若无新日期则不要改 Markdown/状态；若有日期但 `new_articles` 为空（全被 seen 过滤），仍可写入极简「今日总览 + 跳过统计」章节并更新 `processed_dates`（**不**重复展开旧文）。

## 推荐执行步骤（必须按序）

1. **读状态**：`dailyReport/juejin-hot-news/juejin-hot-state.json`（不存在则按空状态创建目录后继续）。
2. **跑抓取脚本**（页面为 SPA，`WebFetch` 页面通常无列表；必须以 API 脚本为准）：

```bash
python tools/juejin_hot_fetch.py --limit 15
```

指定快照日时加 `--date YYYY-MM-DD`。`force` 且需重拉已见文时加 `--include-seen`。

3. **读暂存**：打开 `dailyReport/juejin-hot-news/_staging_latest.json`。
4. **只处理 `new_articles`**（特殊去重）：
   - 每条必须有真实 `url`（`https://juejin.cn/post/...`）。
   - 优先用 `detail.mark_content` / `detail.brief` **归纳正文实际内容**，禁止只复述标题。
   - `detail` 为空时：可用 `WebFetch` 打开 `url` 补读；仍失败则标注「正文未取到」并降级为标题+brief，不得编造。
5. **分类与归纳**：
   - 一级分类固定为四个标签：后端 / 前端 / 人工智能 / 开发工具。
   - 二级按榜单：文章热榜 / 收藏热榜；同一 URL 出现在多榜/多标签时，**只写一条正文摘要**，在「出现位置」列出全部 `(标签, 榜单, 排名)`。
   - 可在标签内再按主题小聚类（如「Agent/Skills」「工程效能」「框架实战」），但链接必须真实可点。
6. **写 Markdown**（见模板与写入规则）。
7. **更新状态**：合并本次成功摘要的 URL 到 `seen_urls`（去重升序或稳定追加均可，推荐排序去重）；更新 `processed_dates` / `last_end_date` / `last_sync_ymd`。
8. **收尾**：告知处理日期、写入路径、新增条数、因去重跳过条数。

## 摘要质量要求

- 每篇新文章写 **2–5 句中文**，覆盖：解决什么问题、关键做法/技术点、适用读者、注意点（若有）。
- 必须附带真实链接：`[标题](https://juejin.cn/post/...)`。
- 过滤明显广告软文时可标注「偏营销，略读」仍给链接，或跳过但计入统计。
- 不要输出整篇原文粘贴；不要伪造阅读量/排名。

## 日期章节模板

```markdown
## YYYY-MM-DD

### 今日总览

**一句话结论**：[融合当日四标签×双榜的主线]

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 文章热榜 + 收藏热榜 × 后端/前端/人工智能/开发工具 |
| 榜单规模 | 每槽最多 N 条；列表总条数 / 去重后新 URL 数 / 跳过已见数 |
| 核心趋势 | [2–4 个跨文归纳，不逐 URL 流水账] |
| 可直接关注 | [3–5 个最值得点开的方向，可带链接] |

### 后端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 1 | [标题](URL) | 作者 | 赞/藏/阅 | [2–5 句正文归纳；若为本轮跳过已见则写「已收录，跳过」] | URL |

#### 收藏热榜

（同上表结构）

### 前端

（同后端结构：文章热榜 + 收藏热榜）

### 人工智能

（同上）

### 开发工具

（同上）

### 跨榜重复与去重说明

- 本轮新摘要 URL 数：N
- 因 `seen_urls` 跳过：M（可列 Top 若干标题+链接，或只给数量）
- 同文多标签/双榜出现：列出 `URL → 出现位置`

### 来源清单

- 快照日：YYYY-MM-DD（Asia/Shanghai）
- 页面：https://juejin.cn/hot/articles 、 https://juejin.cn/hot/collected-articles
- 抓取：`tools/juejin_hot_fetch.py` → `_staging_latest.json`

| 标签 | 榜单 | 标题 | 链接 |
| --- | --- | --- | --- |
| 后端 | 文章热榜 | xxx | https://juejin.cn/post/... |
```

表格中「链接」列可与标题列合并为 Markdown 链接；来源清单必须能回溯全部**新摘要**文章。

若 `new_articles` 为空但仍需记日：

```markdown
## YYYY-MM-DD

### 今日总览

**一句话结论**：四标签×双榜已扫描，本轮无未见于 `seen_urls` 的新文章链接。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 文章热榜 + 收藏热榜 × 后端/前端/人工智能/开发工具 |
| 榜单规模 | 列表总条数 X；新 URL 0；跳过已见 X |
| 核心趋势 | 热榜内容与历史已收录集合高度重叠 |
| 可直接关注 | 无新增；可 force=true 强制重摘要 |

### 跨榜重复与去重说明

- 本轮新摘要 URL 数：0
- 因 `seen_urls` 跳过：M

### 来源清单

- 快照日：YYYY-MM-DD
- 页面：https://juejin.cn/hot/articles 、 https://juejin.cn/hot/collected-articles
```

## Markdown 写入规则

对成功处理的快照日 `YYYY-MM-DD`：

1. `YYYYMM` = 日期前 6 位数字。
2. 双写：`dailyReport/juejin-hot-news/{YYYYMM}.md` 与 `juejin-hot-digest.md`。
3. 文件头（新建时）：

```markdown
# Juejin Hot Digest

按 Asia/Shanghai 时区汇总掘金文章热榜与收藏热榜（后端 / 前端 / 人工智能 / 开发工具），按文章链接去重并归纳正文。
```

4. 章节标题精确为 `## YYYY-MM-DD`；文件内日期**倒序**。
5. 已存在则覆盖该日章节（force 或同日重跑）；否则插入到倒序正确位置。
6. 修剪滚动入口：只保留当前自然月章节。
7. 不要删除文件头说明段。
8. `_staging_latest.json` 可不入库；不要把整篇 `mark_content` 粘进 digest。

## 状态更新规则

仅在当日章节成功写入后更新状态：

- `processed_dates` 并入快照日，去重升序。
- `last_end_date` = max(原值, 快照日)。
- `last_sync_ymd` 更新为本次快照日（首次或本次）。
- 将本次**实际写入摘要**的规范 URL 并入 `seen_urls`（去重；建议按字符串排序）。
- 仅出现在 `skipped_seen`、未写摘要的 URL：**不要**重复追加（应已在集合中）。

## 输出要求

完成后简要告知：

- 处理的快照日期。
- 写入路径：月归档 `YYYYMM.md` + 滚动 `juejin-hot-digest.md` + 状态文件。
- 新摘要篇数、因链接去重跳过篇数、详情失败篇数（如有）。

指定日期重复时唯一输出：

```text
该日期已处理，跳过：YYYY-MM-DD
```

非 force 且无新日期时唯一输出：

```text
本次无新资讯
```

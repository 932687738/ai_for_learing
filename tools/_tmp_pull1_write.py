# -*- coding: utf-8 -*-
"""Incremental digest pull: AI/KB 2026-08-24 + Juejin 2026-08-25."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

AI_SEC = """## 2026-08-24

### 今日总览

**一句话结论**：8 月 24 日主线是 **Langfuse `v4.17.0` 把 8/22 评测改版落到发行版**，以及 **Codex `0.149.1` 补丁**：前者从 trace/event 表建标注队列、评测 UX 进主线，Assistant（OSS）接上 Anthropic Messages；后者无独立 What's New，只给 compare。Claude Code 当日中国时间窗口无新 tag（`v2.1.243` 落在 UTC 晚间，中国时间为 8/25）。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 官方厂商、安全治理、Claude Code/Codex/OpenClaw/Hermes、Spring AI/Alibaba AI、Langfuse、LangChain/LangGraph、Code Graph、Loop Engineering、skills、论文与政策 |
| 核心趋势 | 1）可观测性从「改 changelog」变成「可升级的 v4 发行」；2）编程 CLI 进入补丁日；3）无新模型 |
| 可直接关注 | 标注队列可从 trace/event 表一键建；evaluator 可按模型过滤；Claude Code `/usage` Loops 拆解记到 8/25 |
| 专项检索结论 | Langfuse：`v4.17.0`（Published 2026-08-24T13:14:03Z，中国时间 21:14）。Codex：`0.149.1`（Published 2026-08-24T00:28:28Z，中国时间 08:28）。Claude Code / OpenClaw / Hermes / Spring AI / Spring Alibaba AI / LangChain·LangGraph / Code Graph / Loop Engineering / skills：未发现可核验的 8/24 重大官方更新。 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| LLM 可观测性 | [Langfuse v4.17.0](https://github.com/langfuse/langfuse/releases/tag/v4.17.0) | 2026-08-24 | 开源发布 | 新 evaluation UX 合入主线；从 trace/event 表建 annotation queue；evaluator 可展示/过滤模型；Assistant（OSS）支持 Anthropic Messages；v4 双写默认露出迁移 UI |
| 编程 CLI | [Codex 0.149.1](https://github.com/openai/codex/releases/tag/rust-v0.149.1) | 2026-08-24 | 开源发布 | 补丁发布，页面无功能条目，变更见 [0.149.0...0.149.1](https://github.com/openai/codex/compare/rust-v0.149.0...rust-v0.149.1) |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| 评测上线 | [Langfuse v4.17.0](https://github.com/langfuse/langfuse/releases/tag/v4.17.0) | 8/22 changelog 的 evaluator/rule 体验进发行版；code evaluator 与 score 关联修复 | 自托管 / 要升 v4 的人 |
| Codex 补丁 | [0.149.1 compare](https://github.com/openai/codex/compare/rust-v0.149.0...rust-v0.149.1) | 无独立 release notes，以 diff 为准 | 已跟 0.149.0、要锁补丁的人 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：框架侧当日 GA 在 Langfuse 发行版；编排框架无新 release。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| Langfuse | v4.17.0：评测 UX + 标注队列 + Anthropic Messages | 从线上 trace 直接建队列，少复制粘贴到评测集 |
| Codex | 0.149.1 补丁 | 功能仍以 0.149.0 的 agents/queue 为准 |
| Claude Code | 中国时间窗口无新 tag | `v2.1.243`（UTC 8/24 23:40）记到 8/25：`/usage` Loops、`modelPicker`、`promptCacheTtl` |
| 其余专项 | 未发现 8/24 可核验重大更新 | 继续消化 8/22 评测改版 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 推荐 | [Langfuse v4.17.0](https://github.com/langfuse/langfuse/releases/tag/v4.17.0) | 当日唯一带完整功能列表的框架发行 |
| 延伸 | [Codex 0.149.1](https://github.com/openai/codex/releases/tag/rust-v0.149.1) | 确认补丁日、对照 compare |

### 来源清单

- 检索范围：2026-08-24 00:00:00 到 2026-08-24 23:59:59（Asia/Shanghai）
- 引用域名：github.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 开源发布 | Langfuse v4.17.0 | 2026-08-24 | https://github.com/langfuse/langfuse/releases/tag/v4.17.0 |
| 开源发布 | Codex 0.149.1 | 2026-08-24 | https://github.com/openai/codex/releases/tag/rust-v0.149.1 |

"""

KB_SEC = """## 2026-08-24

### 今日总览

**一句话结论**：固定大厂门户 8 月 24 日无新长文；掘金同日可核验工程文是 **浏览器内 CAD diff**，另有金仓/蓝耘/ServBay 偏营销文。五个专项无官方新 GA。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 阿里/腾讯/字节/百度/美团/京东/滴滴/网易/360/有赞 + 掘金；专项 Langfuse/LangChain/Code Graph/Spring Alibaba AI/Loop Engineering |
| 核心趋势 | 图纸评审想做成「类 git diff」；向量库厂商继续讲融合库 |
| 可直接关注 | CAD 对比在客户端完成、不上传服务器；得物 EP-Harness 文属 8/20，不记本日 |
| 专项检索结论 | Langfuse / LangChain·LangGraph / Code Graph / Spring Alibaba AI / Loop Engineering：固定来源内未发现可核验的 8/24 新文。 |
| 未发现更新 | 阿里技术/中间件/语雀干货、腾讯 TEG/AlloyTeam/大讲堂、字节技术博客、百度 FEX/EFE、美团技术团队、京东/凹凸、滴滴、网易、360、有赞 |

### 重要文章与更新

| 主题 | 标题 | 日期 | 来源 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| CAD 工程 | [在浏览器里对比 DWG/DXF 图纸](https://juejin.cn/post/7677109639176749090) | 2026-08-24 | 掘金 | `@mlightcad/cad-diff-viewer`：左右分屏/叠加，客户端完成，不必上 AutoCAD。图纸 diff 难在句柄、图层、浮点，不是文本行对齐 |
| 多模库（偏营销） | [向量数据库不该成为新孤岛：KingbaseES](https://juejin.cn/post/7677418026090528794) | 2026-08-24 | 掘金 | 讲权限/正文/向量不同步。产品文，对照金仓文档再评估 |
| 热榜工具（偏营销） | [用蓝耘元生代做 GitHub 热榜解读](https://juejin.cn/post/7677428850284675082) | 2026-08-24 | 掘金 | Dify Chatflow + DeepSeek-V3.2 整理 Trending。带推广码，流程可学、平台勿当中立评测 |

### 技术文档与实践

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| 图纸评审 | [cad-diff-viewer](https://juejin.cn/post/7677109639176749090) | 几何/句柄/图层对齐；纯前端、无转换后端 | 要做图纸 CR 的前端/工具链 |

### 工程实践归纳

**总体判断**：五个专项在固定来源内均未发现可核验更新；工程信号在「领域 diff ≠ 文本 diff」。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 专项五题 | 无新文 | Langfuse v4.17.0 见 AI 日报，不在固定中文门户 |
| 图纸工具 | 浏览器 CAD diff | 先定义对齐键（句柄/图层），再谈可视化 |
| 向量库 | 金仓融合叙事 | 权限与索引不同步是真问题，方案须回官方 |

### 值得深入阅读的资料

- 本日门户无推荐；CAD 文可作工具样本。得物 [EP-Harness](https://juejin.cn/post/7675676910077329414) 发布于 8/20，可回看不记本日。

### 来源清单

- 检索范围：2026-08-24 00:00:00 到 2026-08-24 23:59:59（Asia/Shanghai）
- 固定来源覆盖：已覆盖清单中的公司/组织维度
- 来源清单表格：

| 公司/组织 | 来源 | 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- | --- | --- |
| 字节跳动（社区） | 掘金 | 开源工具 | 在浏览器里对比 DWG/DXF | 2026-08-24 | https://juejin.cn/post/7677109639176749090 |
| 字节跳动（社区） | 掘金 | 社区转述（偏营销） | KingbaseES 多模融合 | 2026-08-24 | https://juejin.cn/post/7677418026090528794 |
| 字节跳动（社区） | 掘金 | 社区转述（偏营销） | 蓝耘元生代 GitHub 热榜解读 | 2026-08-24 | https://juejin.cn/post/7677428850284675082 |

"""

JJ_SEC = """## 2026-08-25

### 今日总览

**一句话结论**：`2026-08-25` 新 URL 主线是 **得物 EP-Harness 团队化、沙箱概念、前端价值/CSS、CAD diff**；收藏榜补前端转 Agent 日记与「白嫖 V4 Pro」旧文。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 文章热榜 + 收藏热榜 × 后端/前端/人工智能/开发工具 |
| 榜单规模 | 每槽最多 15 条；列表总条数 120；去重后新 URL **16**；跳过已见 **104**；详情成功 16 / 失败 0 |
| 核心趋势 | 1）个人 AI Coding 的缺口被写成平台（prompt 评审、可见性、闭环）；2）前端在谈「教程会的都贬值」；3）工具向落到 Flutter 9 月大限与数据库 GUI |
| 可直接关注 | [EP-Harness｜得物技术](https://juejin.cn/post/7675676910077329414)；[Sandbox 到底是什么](https://juejin.cn/post/7676165309280796698)；[AI 时代写给前端同行](https://juejin.cn/post/7676369124041654307)；[CAD diff-viewer](https://juejin.cn/post/7677109639176749090) |

### 后端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 14 | [用蓝耘元生代做 GitHub 热榜解读](https://juejin.cn/post/7677428850284675082) | 一只牛博 | 赞0/藏1/阅616 | Dify Chatflow + DeepSeek-V3.2 收拢 Trending/README/目录再整理。偏营销（推广码）；流程可学。 | https://juejin.cn/post/7677428850284675082 |
| 15 | [向量数据库不该成为新孤岛：KingbaseES](https://juejin.cn/post/7677418026090528794) | 一只牛博 | 赞0/藏1/阅611 | 权限、正文、向量分三套导致不同步。金仓融合库叙事，偏营销，对照官方文档。 | https://juejin.cn/post/7677418026090528794 |

#### 收藏热榜

本槽无新增。

### 前端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 8 | [在浏览器里对比 DWG/DXF 图纸](https://juejin.cn/post/7677109639176749090) | mlightcad | 赞1/藏4/阅1324 | `cad-diff-viewer`：左右分屏/叠加，客户端完成，不上 AutoCAD。适合要做图纸评审的人。 | https://juejin.cn/post/7677109639176749090 |
| 10 | [AI 时代写给前端同行：什么在贬值，什么在涨价](https://juejin.cn/post/7676369124041654307) | 书源 | 赞19/藏14/阅773 | 教程能学会的被 AI 吃掉；涨价的是产品判断、性能、协作。观点文，含 AI 辅助生成声明。 | https://juejin.cn/post/7676369124041654307 |
| 13 | [一行 CSS 新特性干掉 20 行 JavaScript](https://juejin.cn/post/7677254638324350986) | ErpanOmer | 赞16/藏19/阅554 | 视差、组件级响应式、气泡定位等可用新 CSS 少写 JS。盘点文，兼容性须自测。 | https://juejin.cn/post/7677254638324350986 |
| 14 | [客户只想看个页面，我却做了一个静态演示发布系统](https://juejin.cn/post/7676301268526841856) | 勇宝趣学前端 | 赞5/藏9/阅745 | 不想把演示丢给带广告的第三方托管，自建上传/过期/下线。适合演示多、要管权限的人。 | https://juejin.cn/post/7676301268526841856 |
| 15 | [Three.js 3D地图开发实录](https://juejin.cn/post/7675920155117092873) | 漏刻有时 | 赞5/藏12/阅504 | LockScope：纯前端 SPA，GeoJSON 到流光飞线，记 12 个坑。Three.js r128，无构建。适合要定制大屏地图的人。 | https://juejin.cn/post/7675920155117092873 |

#### 收藏热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 14 | [从零开始:前端转型AI agent直到就业](https://juejin.cn/post/7644135664519741449) | 渣渣xiong | 赞75/藏96/阅6242 | 34 岁前端裁员后转 Agent 的第 18–56 天：项目、时间分配、求职。旧文新上收藏榜；路径是个人样本。 | https://juejin.cn/post/7644135664519741449 |

### 人工智能

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 7 | [Sandbox（沙箱）到底是什么](https://juejin.cn/post/7676165309280796698) | 陆枫Larry | 赞13/藏15/阅504 | 从 OpenClaw 文档出发：沙箱 ≠ VM/Docker/venv，是划定的受限执行区。适合刚碰 Agent 权限的人。 | https://juejin.cn/post/7676165309280796698 |
| 13 | [EP-Harness：从个人 AI Coding 到团队级 Agent 工作流｜得物技术](https://juejin.cn/post/7675676910077329414) | 得物技术 | 赞7/藏5/阅347 | Prompt 无评审、经验沉不下来、过程不可见、写完代码接不上 CR/部署。EP-Harness 把这些做成平台能力。大厂实践，细节以原文架构为准。 | https://juejin.cn/post/7675676910077329414 |
| 14 | [智谱GLM-5.3+ZCode Agent，真实项目第一手实测](https://juejin.cn/post/7675615031892656174) | 狂师 | 赞6/藏2/阅368 | 主张原生模型配原生 Agent（ZCode），少一层协议转换。8/13–14 发布后的实测，数字回作者环境。 | https://juejin.cn/post/7675615031892656174 |
| 15 | [为啥Agent在coding表现这么好，但是在别的领域就是差的不少](https://juejin.cn/post/7676901441995391014) | 姆斯李 | 赞8/藏6/阅281 | 从可形式化、反馈闭环推 coding 为何好用、业务 Agent 为何留存低。个人推演，不是评测。 | https://juejin.cn/post/7676901441995391014 |

#### 收藏热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 15 | [白嫖DeepSeek V4 Pro！免费无限用，还能接入Claude-Code](https://juejin.cn/post/7650882103059939337) | 神奇小汤圆 | 赞58/藏90/阅21408 | 旧文：把免费额度接到本地/Claude Code。额度与条款会变，以官方为准；标题党，按步骤核权限。 | https://juejin.cn/post/7650882103059939337 |

### 开发工具

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 8 | [2026 年值得关注的 8 款 AI 智能体工具](https://juejin.cn/post/7677418026090233882) | ServBay | 赞2/藏5/阅190 | 盘本地环境/多模型调度/会话可视化。偏产品清单，对照各仓库再装。 | https://juejin.cn/post/7677418026090233882 |
| 11 | [Flutter版本选择指南：3.47压哨发布，9月大限只剩一周](https://juejin.cn/post/7677227641012666383) | 程序员老刘 | 赞1/藏2/阅156 | Flutter 3.47 + Dart 3.13；Material/Cupertino 拆包，11 月 SDK 内置库走向。赶 9 月 UIKit 迁移窗口。 | https://juejin.cn/post/7677227641012666383 |
| 15 | [2026 年 4 款数据库管理工具推荐](https://juejin.cn/post/7675324884412334121) | ClouGence | 赞0/藏2/阅165 | Navicat / CloudDM / DataGrip / DBeaver。偏选型安利，国产库与审批场景须自测。 | https://juejin.cn/post/7675324884412334121 |

#### 收藏热榜

本槽无新增。

### 跨榜重复与去重说明

- 本轮新摘要 URL 数：16
- 因 `seen_urls` 跳过：104（只给数量；不要把已见文再展开成表行）
- 同文多标签/双榜出现：无（16 条均只出现在单一槽位）

### 来源清单

- 快照日：2026-08-25（Asia/Shanghai）
- 页面：https://juejin.cn/hot/articles 、 https://juejin.cn/hot/collected-articles
- 抓取：`tools/juejin_hot_fetch.py` → `_staging_latest.json`

| 标签 | 榜单 | 标题 | 链接 |
| --- | --- | --- | --- |
| 后端 | 文章热榜 | 用蓝耘元生代做 GitHub 热榜解读 | https://juejin.cn/post/7677428850284675082 |
| 后端 | 文章热榜 | KingbaseES 多模融合 | https://juejin.cn/post/7677418026090528794 |
| 前端 | 文章热榜 | 浏览器里对比 DWG/DXF | https://juejin.cn/post/7677109639176749090 |
| 前端 | 文章热榜 | AI 时代写给前端同行 | https://juejin.cn/post/7676369124041654307 |
| 前端 | 文章热榜 | 一行 CSS 干掉 20 行 JS | https://juejin.cn/post/7677254638324350986 |
| 前端 | 文章热榜 | 静态演示发布系统 | https://juejin.cn/post/7676301268526841856 |
| 前端 | 文章热榜 | Three.js 3D 地图实录 | https://juejin.cn/post/7675920155117092873 |
| 前端 | 收藏热榜 | 前端转型 AI agent 日记 | https://juejin.cn/post/7644135664519741449 |
| 人工智能 | 文章热榜 | Sandbox 到底是什么 | https://juejin.cn/post/7676165309280796698 |
| 人工智能 | 文章热榜 | EP-Harness｜得物技术 | https://juejin.cn/post/7675676910077329414 |
| 人工智能 | 文章热榜 | GLM-5.3 + ZCode 实测 | https://juejin.cn/post/7675615031892656174 |
| 人工智能 | 文章热榜 | Agent 为何 coding 强、业务弱 | https://juejin.cn/post/7676901441995391014 |
| 人工智能 | 收藏热榜 | 白嫖 DeepSeek V4 Pro | https://juejin.cn/post/7650882103059939337 |
| 开发工具 | 文章热榜 | 8 款 AI 智能体工具 | https://juejin.cn/post/7677418026090233882 |
| 开发工具 | 文章热榜 | Flutter 3.47 / 9 月大限 | https://juejin.cn/post/7677227641012666383 |
| 开发工具 | 文章热榜 | 4 款数据库管理工具 | https://juejin.cn/post/7675324884412334121 |

"""


def insert_section(path: Path, section: str, heading: str) -> None:
    text = path.read_text(encoding="utf-8")
    marker = f"## {heading}\n"
    if text.startswith(marker) or f"\n{marker}" in text:
        raise SystemExit(f"section already exists in {path}: {heading}")
    lines = text.splitlines(keepends=True)
    insert_at = 0
    for i, line in enumerate(lines):
        if line.startswith("# "):
            insert_at = i + 1
            while insert_at < len(lines) and lines[insert_at].strip() == "":
                insert_at += 1
            while insert_at < len(lines) and not lines[insert_at].startswith("## "):
                insert_at += 1
            break
    path.write_text("".join(lines[:insert_at]) + section + "".join(lines[insert_at:]), encoding="utf-8")
    print("updated", path, heading)


def update_state(path: Path, date: str, extra: dict | None = None) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    dates = set(data.get("processed_dates") or [])
    dates.add(date)
    data["processed_dates"] = sorted(dates)
    data["last_end_date"] = max(data.get("last_end_date") or date, date)
    data["last_sync_ymd"] = data["last_end_date"]
    if extra:
        data.update(extra)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("state", path, date)


def merge_juejin_seen(state_path: Path, staging_path: Path, snap: str) -> None:
    staging = json.loads(staging_path.read_text(encoding="utf-8"))
    new_urls = [a["url"] for a in staging.get("new_articles") or [] if a.get("url")]
    data = json.loads(state_path.read_text(encoding="utf-8"))
    seen = set(data.get("seen_urls") or [])
    seen.update(new_urls)
    update_state(state_path, snap, {"seen_urls": sorted(seen)})


def main() -> None:
    insert_section(ROOT / "dailyReport/ai-daily-news/ai-daily-digest.md", AI_SEC, "2026-08-24")
    insert_section(ROOT / "dailyReport/ai-daily-news/202608.md", AI_SEC, "2026-08-24")
    insert_section(ROOT / "dailyReport/knowledge-base-news/knowledge-base-digest.md", KB_SEC, "2026-08-24")
    insert_section(ROOT / "dailyReport/knowledge-base-news/202608.md", KB_SEC, "2026-08-24")
    insert_section(ROOT / "dailyReport/juejin-hot-news/juejin-hot-digest.md", JJ_SEC, "2026-08-25")
    insert_section(ROOT / "dailyReport/juejin-hot-news/202608.md", JJ_SEC, "2026-08-25")
    update_state(ROOT / "dailyReport/ai-daily-news/ai-daily-state.json", "2026-08-24")
    update_state(ROOT / "dailyReport/knowledge-base-news/knowledge-base-state.json", "2026-08-24")
    merge_juejin_seen(
        ROOT / "dailyReport/juejin-hot-news/juejin-hot-state.json",
        ROOT / "dailyReport/juejin-hot-news/_staging_latest.json",
        "2026-08-25",
    )


if __name__ == "__main__":
    main()

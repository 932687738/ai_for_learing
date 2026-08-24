# -*- coding: utf-8 -*-
"""Incremental digest pull: AI/KB 2026-08-21..23 + Juejin 2026-08-24."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

AI_21 = """## 2026-08-21

### 今日总览

**一句话结论**：8 月 21 日主线是 **Codex 稳定版 `0.149.0` 进入中国时间窗口** 与 **Claude Code `v2.1.238`**：前者补上 `codex agents` 仪表盘、`codex queue` 和 `/cd`；后者给 marketplace `headersHelper`、自托管 runner 延迟关机与 readline 键位。OpenAI「Codex as a platform」与 Apple Messages 插件属 8/19–8/20 官方口径，中文窗口继续传播。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 官方厂商、安全治理、Claude Code/Codex/OpenClaw/Hermes、Spring AI/Alibaba AI、Langfuse、LangChain/LangGraph、Code Graph、Loop Engineering、skills、论文与政策 |
| 核心趋势 | 1）编程 Agent 把「会话/任务」做成可搜索、可排队的产品面；2）企业网关/自托管 runner 继续补鉴权与关机语义；3）桌面插件把 Messages 当任务入口 |
| 可直接关注 | `codex agents` / `codex queue`；`keybindingFlavor: readline`；marketplace `headersHelper` 安装时才跑且要确认 |
| 专项检索结论 | Codex：`0.149.0`（Published 2026-08-20T21:04:55Z，中国时间 8/21 05:04）。Claude Code：`v2.1.238`（Published 2026-08-20T20:33:51Z，中国时间 8/21 04:33）。OpenClaw / Hermes / Spring AI / Spring Alibaba AI / Langfuse / LangChain·LangGraph / Code Graph / Loop Engineering / skills：未发现可核验的 8/21 重大官方更新。 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| 编程 CLI | [Codex 0.149.0](https://github.com/openai/codex/releases/tag/rust-v0.149.0) | 2026-08-21（UTC 20 日晚；中国时间凌晨） | 开源发布 | 交互式 `codex agents`；`/cd` `/pwd` `/cwd`；`codex queue` 给已有会话投消息；`codex doctor` 扩到端点防护/代理/桌面状态；SDK 可传精确 CLI 覆盖与 `max`/`ultra` reasoning |
| 编程 CLI | [Claude Code v2.1.238](https://github.com/anthropics/claude-code/releases/tag/v2.1.238) | 2026-08-21（UTC 20 日晚；中国时间凌晨） | 开源发布 | `keybindingFlavor=readline`；插件市场 `headersHelper` 现用现签；`self-hosted-runner --defer-shutdown-max-min`；修长会话内存与 Remote Control 断线 |
| Harness 叙事 | [Codex as a platform](https://developers.openai.com/blog/codex-as-a-platform) | 相邻日期/中国时间窗口传播（中文媒体 8/21 集中转述） | 官方开发者博文 | `codex exec` / SDK / `app-server` 三层；ARC-AGI-3 上 Sol 从 13.3% 到 38.3%、输出 token 约 1/6；示例应用 Relay |
| 桌面插件 | [Apple Messages plugin / Release Notes](https://openai.com/products/release-notes/) | 2026-08-20（相邻日期；中文/安全媒体 8/21 起传播） | 官方产品更新 | Apple silicon Mac 上 Work/Codex 可读 iMessage/SMS/RCS 并经批准发送；需 Full Disk Access，权限面大于聊天记录 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| Codex 会话编排 | [0.149.0 release](https://github.com/openai/codex/releases/tag/rust-v0.149.0) | 恢复/fork 线程要带回权限档案；排队消息要能叫醒空闲会话 | 多会话/远程 Codex |
| Claude Code 企业网关 | [v2.1.238 release](https://github.com/anthropics/claude-code/releases/tag/v2.1.238) | `headersHelper` 不继承凭证环境变量；项目 MCP helper 要先过 trust dialog | 自建市场/代理出网 |
| 嵌入式 harness | [Codex as a platform](https://developers.openai.com/blog/codex-as-a-platform) | 应用拥有界面/审批/MCP，harness 只管 loop | 要把 Agent 嵌进已有后台的人 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：框架侧无新 GA；可落地增量在 Codex 任务仪表盘与 Claude Code 插件鉴权。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| Codex | 0.149.0：agents 仪表盘 + queue + cwd 命令 | 长任务要能被找到、被投递，而不是只开新会话 |
| Claude Code | v2.1.238：headersHelper / runner 延迟关机 | 短期 token 现用现签；SIGTERM 先停新活再退 |
| OpenAI 平台叙事 | exec / SDK / app-server | 别把 CLI 壳再包一层当产品 |
| Langfuse / LangGraph / Code Graph / Loop / Spring AI | 未发现 8/21 可核验重大更新 | Langfuse 官方 changelog 落在 8/22 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 推荐 | [Codex 0.149.0](https://github.com/openai/codex/releases/tag/rust-v0.149.0) | 当日 Codex 唯一可核验的稳定 changelog |
| 推荐 | [Claude Code v2.1.238](https://github.com/anthropics/claude-code/releases/tag/v2.1.238) | 企业网关与自托管 runner 相关条目集中 |
| 延伸 | [Codex as a platform](https://developers.openai.com/blog/codex-as-a-platform) | 把 harness 讲成嵌入面，数字须回原文 |

### 来源清单

- 检索范围：2026-08-21 00:00:00 到 2026-08-21 23:59:59（Asia/Shanghai）
- 引用域名：github.com, developers.openai.com, openai.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 开源发布 | Codex 0.149.0 | 2026-08-21（中国时间窗口） | https://github.com/openai/codex/releases/tag/rust-v0.149.0 |
| 开源发布 | Claude Code v2.1.238 | 2026-08-21（中国时间窗口） | https://github.com/anthropics/claude-code/releases/tag/v2.1.238 |
| 官方博文 | Codex as a platform | 相邻日期/中国时间窗口传播 | https://developers.openai.com/blog/codex-as-a-platform |
| 官方产品 | Apple Messages plugin | 2026-08-20（相邻日期） | https://openai.com/products/release-notes/ |

"""

AI_22 = """## 2026-08-22

### 今日总览

**一句话结论**：8 月 22 日主线是 **Langfuse 重做生产评测工作流** 与 **Claude Code `v2.1.239`/`v2.1.240`**：评测侧把 evaluator 与 rule 拆开，可在真实 observation 上试跑并估算近 7 日成本；Claude Code 把 1.1× 美国专属推理溢价写进 `/cost`，并修 Bedrock 代理下静默双计费。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 官方厂商、安全治理、Claude Code/Codex/OpenClaw/Hermes、Spring AI/Alibaba AI、Langfuse、LangChain/LangGraph、Code Graph、Loop Engineering、skills、论文与政策 |
| 核心趋势 | 1）评测从「写 JSONPath 上线」转到「对着真实 trace 试跑再采样」；2）编程 CLI 继续修云会话/代理/OTel；3）Codex 仅见 alpha 流水，无新 GA |
| 可直接关注 | evaluator 与 rule 分离；上线前看过去 7 日匹配量；Bedrock 代理剥 Content-Type 会导致整轮非流式重跑 |
| 专项检索结论 | Langfuse：[Reusable evaluators and rules](https://langfuse.com/changelog/2026-08-22-reusable-evaluators-and-rules)（2026-08-22）。Claude Code：`v2.1.239`（Published 2026-08-21T19:54:23Z，中国时间 8/22 03:54）；`v2.1.240`（Published 2026-08-22T14:45:30Z，中国时间 22:45，仅 bugfix）。Codex / OpenClaw / Hermes / Spring AI / Spring Alibaba AI / LangChain·LangGraph / Code Graph / Loop Engineering / skills：未发现可核验的 8/22 重大官方更新。 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| LLM 评测 | [Set up production evaluations with ease](https://langfuse.com/changelog/2026-08-22-reusable-evaluators-and-rules) | 2026-08-22 | 官方 changelog | Evaluator 定义怎么打分，Rule 定义评哪些 observation；可复用过滤/采样；用真实数据试跑；变量映射可点选，JSONPath 仍留高级路径；上线前估近 7 日量与 judge 成本 |
| 编程 CLI | [Claude Code v2.1.239](https://github.com/anthropics/claude-code/releases/tag/v2.1.239) | 2026-08-22（UTC 21 日晚；中国时间凌晨） | 开源发布 | `/cost` 计入 1.1× US-only 溢价；`/claude-api upgrade` 迁 Python SDK 0.x→1.x；修 Bedrock 代理双计费、HTTPS_PROXY + SSO 启动挂起、OTel 被 PreToolUse 打断；`/goal` check-in 改为 30min→1h→2h |
| 编程 CLI | [Claude Code v2.1.240](https://github.com/anthropics/claude-code/releases/tag/v2.1.240) | 2026-08-22 | 开源发布 | 仅「Bug fixes and reliability improvements」，无新功能条目 |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| 生产评测 | [Langfuse changelog](https://langfuse.com/changelog/2026-08-22-reusable-evaluators-and-rules) | observation 级已自动升级；trace 级须走迁移 FAQ | 已有 Langfuse judge 的人 |
| Claude Code 账单 | [v2.1.239 release](https://github.com/anthropics/claude-code/releases/tag/v2.1.239) | 数据驻留工作区的 1.1× 要进预算；代理剥 Content-Type 会双计费 | Bedrock/Vertex 走企业代理的人 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：当日唯一框架级 GA 是 Langfuse 评测体验；编排框架无新 release。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| Langfuse | evaluator / rule 分离 + 真实数据试跑 | 先估匹配量再开线上 judge，别一上来全量 LLM 打分 |
| Claude Code | v2.1.239 成本与代理修复；v2.1.240 纯修复 | `/goal` 长任务降频 check-in，减少打扰 |
| Codex / LangGraph / Code Graph / Loop / Spring AI | 未发现 8/22 可核验重大更新 | Codex `0.149.1` 落在 8/24 UTC，不记入本日 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 推荐 | [Langfuse / reusable evaluators](https://langfuse.com/changelog/2026-08-22-reusable-evaluators-and-rules) | 当日框架专项唯一可核验官方更新 |
| 推荐 | [Claude Code v2.1.239](https://github.com/anthropics/claude-code/releases/tag/v2.1.239) | 成本、代理、OTel、`/goal` 条目集中 |

### 来源清单

- 检索范围：2026-08-22 00:00:00 到 2026-08-22 23:59:59（Asia/Shanghai）
- 引用域名：langfuse.com, github.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 官方 changelog | Langfuse reusable evaluators and rules | 2026-08-22 | https://langfuse.com/changelog/2026-08-22-reusable-evaluators-and-rules |
| 开源发布 | Claude Code v2.1.239 | 2026-08-22（中国时间窗口） | https://github.com/anthropics/claude-code/releases/tag/v2.1.239 |
| 开源发布 | Claude Code v2.1.240 | 2026-08-22 | https://github.com/anthropics/claude-code/releases/tag/v2.1.240 |

"""

AI_23 = """## 2026-08-23

### 今日总览

**一句话结论**：8 月 23 日可核验增量偏瘦：**Claude Code `v2.1.241` 仅 bugfix**；安全/消费媒体继续复述 8/20 的 Apple Messages 插件与 Full Disk Access 面。Codex 稳定版无新 tag（`0.149.1` 落在 8/24 UTC）。五个框架专项无新 GA。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 官方厂商、安全治理、Claude Code/Codex/OpenClaw/Hermes、Spring AI/Alibaba AI、Langfuse、LangChain/LangGraph、Code Graph、Loop Engineering、skills、论文与政策 |
| 核心趋势 | 1）编程 CLI 进入连续小修日；2）桌面 Agent 权限争议从「能不能发 iMessage」转到「FDA 打开了哪些盘」；3）框架侧消化 8/22 Langfuse 评测改版 |
| 可直接关注 | Messages 插件默认要批准正文和收件人；关闭持久批准与任务免批准的已知问题见官方 release notes |
| 专项检索结论 | Claude Code：`v2.1.241`（Published 2026-08-23T00:52:16Z，中国时间 08:52，仅 bugfix）。Codex / OpenClaw / Hermes / Spring AI / Spring Alibaba AI / Langfuse / LangChain·LangGraph / Code Graph / Loop Engineering / skills：未发现可核验的 8/23 重大官方更新。 |

### 重要事件与发布

| 主题 | 标题 | 日期 | 类型 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| 编程 CLI | [Claude Code v2.1.241](https://github.com/anthropics/claude-code/releases/tag/v2.1.241) | 2026-08-23 | 开源发布 | 仅「Bug fixes and reliability improvements」，无新功能条目 |
| 桌面插件（传播） | [ChatGPT Work and Codex Can Now Use Apple Messages](https://winbuzzer.com/2026/08/23/openai-lets-chatgpt-search-apple-messages-and-send-replies-o-xcxwbn/) | 2026-08-23（报道；官方属 8/20） | 技术媒体 | 复述 Apple silicon + Work/Codex 才能用；安装、系统权限、发送批准三步分离。权限细节须回 [OpenAI Release Notes](https://openai.com/products/release-notes/) |

### 技术文档与教程

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| Claude Code | [v2.1.241 release](https://github.com/anthropics/claude-code/releases/tag/v2.1.241) | 连续修复日，升级即可 | 已跟 2.1.239 的人 |
| Messages 权限 | [OpenAI product release notes](https://openai.com/products/release-notes/) | FDA、联系人、自动化分权；默认发送前批准 | Mac 桌面 Agent 管理员 |

### LangChain / Agent / LLM 工程相关进展

**总体判断**：无新框架 GA；继续消化 8/21 Codex 仪表盘与 8/22 Langfuse 评测。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| Claude Code | v2.1.241 纯修复 | 不必为「新能力」升级，修稳定性可升 |
| Messages 插件 | 媒体二次传播 + FDA 争议 | 桌面 Agent 的权限边界要写进安全评审，不能只看功能 demo |
| 其余专项 | 未发现 8/23 可核验重大更新 | Codex `0.149.1` 记到下一中国日 |

### 值得深入阅读的资料

| 推荐级别 | 资料 | 为什么值得读 |
| --- | --- | --- |
| 延伸 | [OpenAI Release Notes / Apple Messages](https://openai.com/products/release-notes/) | 官方口径比媒体短，含撤销与已知问题 |
| 延伸 | [Claude Code v2.1.241](https://github.com/anthropics/claude-code/releases/tag/v2.1.241) | 确认当日无功能增量 |

### 来源清单

- 检索范围：2026-08-23 00:00:00 到 2026-08-23 23:59:59（Asia/Shanghai）
- 引用域名：github.com, openai.com, winbuzzer.com
- 来源清单表格：

| 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- |
| 开源发布 | Claude Code v2.1.241 | 2026-08-23 | https://github.com/anthropics/claude-code/releases/tag/v2.1.241 |
| 技术媒体 | ChatGPT / Codex Apple Messages | 2026-08-23（报道；官方属 8/20） | https://winbuzzer.com/2026/08/23/openai-lets-chatgpt-search-apple-messages-and-send-replies-o-xcxwbn/ |

"""

KB_21 = """## 2026-08-21

### 今日总览

**一句话结论**：固定大厂门户 8 月 21 日缺少可复现的新长文；掘金可见 **WorkBuddy + 腾讯云 OCR 合同审查** 实操记录。五个专项无官方新 GA。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 阿里/腾讯/字节/百度/美团/京东/滴滴/网易/360/有赞 + 掘金；专项 Langfuse/LangChain/Code Graph/Spring Alibaba AI/Loop Engineering |
| 核心趋势 | 社区仍在消化 DSH / Codex harness，固定门户当日无新架构文 |
| 可直接关注 | 合同审查要「报告能回到原文」；扫描件先过 OCR 再抽条款 |
| 专项检索结论 | Langfuse / LangChain·LangGraph / Code Graph / Spring Alibaba AI / Loop Engineering：固定来源内未发现可核验的 8/21 新文。 |
| 未发现更新 | 阿里技术/中间件/语雀干货、腾讯 TEG/AlloyTeam/大讲堂、字节技术博客、百度 FEX/EFE、美团技术团队、京东/凹凸、滴滴、网易、360、有赞 |

### 重要文章与更新

| 主题 | 标题 | 日期 | 来源 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| OCR + Skill | [从零封装一个合同审查助手](https://juejin.cn/post/7676162994423119918) | 2026-08-21（文内录屏时间戳） | 掘金 | WorkBuddy + 腾讯云 OCR 吃 Word/PDF/扫描件，输出要素表、风险清单、修改建议；强调条款要能回溯原文。偏个人封装，密钥与技能开通以腾讯云为准 |

### 技术文档与实践

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| 文档 Agent | [合同审查助手](https://juejin.cn/post/7676162994423119918) | 格式归一 → OCR → 结构化抽取 → 风险回原文 | 采购/法务对接的工程同学 |

### 工程实践归纳

**总体判断**：五个专项在固定来源内均未发现可核验更新；工程信号落在「文档 Agent 要可回溯」。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 专项五题 | 无新文 | 不把 8/13 DSH 旧文当天 changelog |
| 文档抽取 | 掘金实操 | 漏看自动续约比慢更贵；报告必须锚回原文 |

### 值得深入阅读的资料

- 本日门户无推荐长文；可回看 8/18 [别让模型填写 user_id](https://developer.aliyun.com/article/1756572)。

### 来源清单

- 检索范围：2026-08-21 00:00:00 到 2026-08-21 23:59:59（Asia/Shanghai）
- 固定来源覆盖：已覆盖清单中的公司/组织维度
- 来源清单表格：

| 公司/组织 | 来源 | 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- | --- | --- |
| 字节跳动（社区） | 掘金 | 社区实操 | 从零封装一个合同审查助手 | 2026-08-21 | https://juejin.cn/post/7676162994423119918 |

"""

KB_22 = """## 2026-08-22

### 今日总览

**一句话结论**：固定来源内 8 月 22 日未发现可核验的大厂新长文；Langfuse 官方评测改版在国际 changelog，不计入本路固定站点。五个专项无中文门户新文。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 阿里/腾讯/字节/百度/美团/京东/滴滴/网易/360/有赞 + 掘金；专项 Langfuse/LangChain/Code Graph/Spring Alibaba AI/Loop Engineering |
| 核心趋势 | 社区热文仍是 DSH 安装/命令手册，不是门户当日发布 |
| 可直接关注 | 国际侧 Langfuse 8/22 评测改版见 AI 日报；本路不把 langfuse.com 当固定来源 |
| 专项检索结论 | Langfuse / LangChain·LangGraph / Code Graph / Spring Alibaba AI / Loop Engineering：固定来源内未发现可核验的 8/22 新文。 |
| 未发现更新 | 阿里技术/中间件/语雀干货、腾讯 TEG/AlloyTeam/大讲堂、字节技术博客、百度 FEX/EFE、美团技术团队、京东/凹凸、滴滴、网易、360、有赞 |

### 重要文章与更新

- 未发现值得单独列表的固定来源新文。

### 技术文档与实践

- 未发现值得单独精读的新固定来源长文。

### 工程实践归纳

**总体判断**：五个专项在固定来源内均未发现可核验更新。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 专项五题 | 无新文 | 不把搜索到的旧 Langfuse 教程当天 changelog |
| Agent 接入 | 无新文 | 继续按 8/18：身份不进模型参数 |

### 值得深入阅读的资料

- 本日暂无推荐。

### 来源清单

- 检索范围：2026-08-22 00:00:00 到 2026-08-22 23:59:59（Asia/Shanghai）
- 固定来源覆盖：已覆盖清单中的公司/组织维度
- 来源清单表格：本日无新增固定来源条目。

"""

KB_23 = """## 2026-08-23

### 今日总览

**一句话结论**：固定大厂门户 8 月 23 日仍无新长文；掘金出现 **GitHub 月榜/周榜 Agent Skills 盘点**（抓取基准写明 2026-08-23）。五个专项无官方新 GA。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 阿里/腾讯/字节/百度/美团/京东/滴滴/网易/360/有赞 + 掘金；专项 Langfuse/LangChain/Code Graph/Spring Alibaba AI/Loop Engineering |
| 核心趋势 | 社区把 8 月开源热度读成「Agent 基建军备赛」，数字是抓取时点 |
| 可直接关注 | 月榜 Top 里 Skills/记忆/路由占比高；`@claude`/`@codex` 出现在 Built by 列表，勿当官方贡献统计 |
| 专项检索结论 | Langfuse / LangChain·LangGraph / Code Graph / Spring Alibaba AI / Loop Engineering：固定来源内未发现可核验的 8/23 新文。 |
| 未发现更新 | 阿里技术/中间件/语雀干货、腾讯 TEG/AlloyTeam/大讲堂、字节技术博客、百度 FEX/EFE、美团技术团队、京东/凹凸、滴滴、网易、360、有赞 |

### 重要文章与更新

| 主题 | 标题 | 日期 | 来源 | 研发/学习价值 |
| --- | --- | --- | --- | --- |
| 开源盘点 | [2026年8月GitHub热榜深度拆解：Agent Skills席卷开源圈](https://juejin.cn/post/7676748940241633307) | 2026-08-23（文内抓取基准） | 掘金 | 月度热榜约 19 项里 13 项沾 Agent/Skills/记忆/路由。社区解读，星数以 GitHub 当时快照为准 |

### 技术文档与实践

| 方向 | 推荐资料 | 核心技术点 | 适合谁看 |
| --- | --- | --- | --- |
| 开源雷达 | [8 月 GitHub 热榜拆解](https://juejin.cn/post/7676748940241633307) | 先看全景再下钻五个项目；注意时点数据 | 要补 Skills/记忆仓库样本的人 |

### 工程实践归纳

**总体判断**：五个专项在固定来源内均未发现可核验更新；盘点文不能替代 changelog。

| 主题 | 进展 | 工程启发 |
| --- | --- | --- |
| 专项五题 | 无新文 | 热榜 ≠ 当日官方发布 |
| Agent Skills | 掘金月榜解读 | 技能包星数涨得快，先看权限与维护者 |

### 值得深入阅读的资料

- 本日门户无推荐；可对照本仓库 `dailyReport/github-topz.md` 的 Trending 表，不要混用两套口径。

### 来源清单

- 检索范围：2026-08-23 00:00:00 到 2026-08-23 23:59:59（Asia/Shanghai）
- 固定来源覆盖：已覆盖清单中的公司/组织维度
- 来源清单表格：

| 公司/组织 | 来源 | 类型 | 标题 | 日期 | 链接 |
| --- | --- | --- | --- | --- | --- |
| 字节跳动（社区） | 掘金 | 社区盘点 | 2026年8月GitHub热榜深度拆解 | 2026-08-23 | https://juejin.cn/post/7676748940241633307 |

"""

JJ_SEC = """## 2026-08-24

### 今日总览

**一句话结论**：`2026-08-24` 新 URL 主线是 **DSH 安装/命令/源码对比、Codex 变慢、本地 Qwen 省 token、合同/备份工程文**；收藏榜只补一篇 AI 做微信小游戏旧文。

| 维度 | 本日结论 |
| --- | --- |
| 检索范围 | 文章热榜 + 收藏热榜 × 后端/前端/人工智能/开发工具 |
| 榜单规模 | 每槽最多 15 条；列表总条数 120；去重后新 URL **29**；跳过已见 **91**；详情成功 29 / 失败 0 |
| 核心趋势 | 1）Harness 热文从「值不值得装」转到命令手册、插件清单和 `.agents/`；2）有人开始写 Codex「变慢」是工作方式变了；3）工具向落到备份验库、Git 规范、Docker |
| 可直接关注 | [Codex 怎么突然变慢了](https://juejin.cn/post/7675676910077345798)；[我把 DSH 跑了一遍，终于知道它和 Codex 差在哪](https://juejin.cn/post/7675538244907221001)；[备份完不算完](https://juejin.cn/post/7676421042796412968)；[合同审查助手](https://juejin.cn/post/7676162994423119918) |

### 后端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 3 | [「速通Shell」Shell 数组、关联数组与 mapfile](https://juejin.cn/post/7675181079705649206) | 柒号华仔 | 赞1/藏3/阅2026 | 系列从单条数据处理转到成组数据：普通数组、关联数组、`mapfile`。强调运维/CI 里 bash 数组够覆盖约 80% 场景。适合补 shell，不是新框架。 | https://juejin.cn/post/7675181079705649206 |
| 5 | [备份完不算完，先还原到临时库验一遍](https://juejin.cn/post/7676421042796412968) | 一只牛博 | 赞3/藏2/阅1670 | 「备份成功」≠「能还原」。把 custom 备份还原到临时库，验数据、对象、约束和业务查询。演示用 `system` 建删库。适合 DBA/会写备份脚本的人。 | https://juejin.cn/post/7676421042796412968 |
| 6 | [DeepSeek Harness 这波，搞得全世界都在安装 Node.js](https://juejin.cn/post/7675899462443122726) | 神奇小汤圆 | 赞6/藏8/阅1192 | DSH 默认 Web UI（`127.0.0.1:3080`），入口是 `npx @deepseek-ai/dsh web`，逼着一批非前端装 Node。适合还没跑起来的人；版本以官方为准。 | https://juejin.cn/post/7675899462443122726 |
| 9 | [DeepSeek Harness 命令大全](https://juejin.cn/post/7675947280080240691) | 苏三说技术 | 赞8/藏10/阅630 | 把 `dsh` 当 profile 启动器，整理 `--profile`/`--patch`/`--dump-config` 与插件安装。速查手册，参数以当时官方文档为准。 | https://juejin.cn/post/7675947280080240691 |
| 11 | [DeepSeek Harness 必装的插件公布了](https://juejin.cn/post/7675308265186983978) | cxuanAI | 赞5/藏18/阅516 | 盘 Cordis 插件：better-sidebar 等有用，也点名桌宠类没卵用。适合刚装完毛坯房；先看权限。 | https://juejin.cn/post/7675308265186983978 |
| 12 | [为什么越来越多人用 kkFileView](https://juejin.cn/post/7676641074035605550) | 苏三说技术 | 赞8/藏18/阅387 | 浏览器预览 Word/Excel/CAD/PDF，半小时部署。称 9.9k+ Star。适合 Java OA 要在线预览的人；安全与格式支持须自测。 | https://juejin.cn/post/7676641074035605550 |
| 13 | [Codex 怎么突然变慢了](https://juejin.cn/post/7675676910077345798) | 掘金者阿豪 | 赞5/藏6/阅357 | 同一类需求从「几分钟改完」变成几十分钟。作者判断是工作方式变了（更多读项目/规划），不是单纯卡顿。偏体验，对照你自己的会话设置。 | https://juejin.cn/post/7675676910077345798 |
| 14 | [给 AI 时代找工作的同学一些实用建议](https://juejin.cn/post/7676277362519113763) | 逻辑帧 | 赞6/藏9/阅324 | 转公众号：大模型研发是小工种，学历/微调焦虑常见。建议死皮赖脸投、把做过的 RAG/MCP 项目讲清楚。职场文，不是技术手册。 | https://juejin.cn/post/7676277362519113763 |
| 15 | [Go 1.27 升了一波，泛型方法和 JSON v2 真香但有个坑](https://juejin.cn/post/7675914752422805514) | Flynt | 赞1/藏3/阅375 | 从 1.25 升到 1.27：泛型方法少写包级万能函数；`encoding/json/v2` 踩坑。适合要升级的 Go 服务；changelog 回官方博客。 | https://juejin.cn/post/7675914752422805514 |

#### 收藏热榜

本槽无新增。

### 前端

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 10 | [高级前端如何优雅地拒绝不合理的产品需求](https://juejin.cn/post/7675261669513953290) | ErpanOmer | 赞12/藏13/阅601 | 别只说「有点难」：用性能/端能力把风险讲清楚，避免接不可能任务再被甩锅。职场沟通文。 | https://juejin.cn/post/7675261669513953290 |
| 11 | [ECharts 太平面？试试这款 Vue 3D 图表库](https://juejin.cn/post/7674878323556237355) | RayChart | 赞8/藏7/阅501 | 大屏要「立体一点」时，作者不想从零写 Three.js 柱状图。偏库安利，选型先看许可与包体积。 | https://juejin.cn/post/7674878323556237355 |
| 12 | [虚拟滚动真的比普通滚动性能更好吗](https://juejin.cn/post/7676091857219272742) | Mh | 赞5/藏13/阅725 | 从零写固定高度虚拟列表，再对比「是不是一定更快」。短列表可能更差。适合要做长列表的人。 | https://juejin.cn/post/7676091857219272742 |
| 14 | [面试官说"打开你的AI工具"](https://juejin.cn/post/7674817329578606619) | kyriewen | 赞6/藏7/阅546 | 现场看你怎么用 Claude Code/Cursor，不是默写八股。引用 LeadDev「默认候选人买得起 Max」。面试观察文。 | https://juejin.cn/post/7674817329578606619 |
| 15 | [DeepSeek Harness 发布后，我没急着跑 Demo，先把 `.agents/` 翻了一遍](https://juejin.cn/post/7674828652658425896) | 小u | 赞5/藏8/阅586 | 根目录 `.agents/` 里 11 个 Skill、684 份 Agent Note。作者认为 DSH 把「怎么改这个仓库」写成规则和历史决策。适合要读源码仓的人。 | https://juejin.cn/post/7674828652658425896 |

#### 收藏热榜

本槽无新增。

### 人工智能

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 5 | [这个本地模型，让我 token 自由了](https://juejin.cn/post/7676709710489419786) | stormzhangV | 赞14/藏10/阅804 | 写 Qwen3.8-27B 本地跑、叫板 Opus 4.6、HF/Cline 热度。数字是作者转述，须回阿里/HF。适合 token 账单焦虑、能上本地卡的人。 | https://juejin.cn/post/7676709710489419786 |
| 6 | [我把 DeepSeek Harness 跑了一遍，终于知道它和 Codex 差在哪了](https://juejin.cn/post/7675538244907221001) | 子昕AI编程 | 赞9/藏8/阅891 | 金句：Codex 把组装好的 Agent 交给你，DSH 把组装方式交给你。劝新手别从架构页起步。对比文，选型对照官方仓库。 | https://juejin.cn/post/7675538244907221001 |
| 8 | [从失业到出书：我一个人靠 AI 搭起了一家小公司](https://juejin.cn/post/7675947280080879667) | 后端小肥肠 | 赞13/藏5/阅710 | 创业一年半：出书、训练营、视频 IP。经历向，不是 Agent 教程。 | https://juejin.cn/post/7675947280080879667 |
| 11 | [国产模型越来越强了：DeepSeek V4、Kimi K3 与 GLM](https://juejin.cn/post/7675272903248920595) | Shepherd | 赞5/藏3/阅530 | 专栏铺垫：V4 Flash/Pro、Kimi K3、GLM Coding Plan。资讯盘点，日期回各家公告。 | https://juejin.cn/post/7675272903248920595 |
| 12 | [没想到吧！Skill 也可以测试](https://juejin.cn/post/7675447922213568558) | RockByte | 赞3/藏4/阅415 | 系列续篇：给上一篇 Skill 写可重复跑的检查脚本，改完回归。适合已经在写 Skill 的人。 | https://juejin.cn/post/7675447922213568558 |
| 13 | [DeepSeek Harness 强是真的强，普通用户可以再等等](https://juejin.cn/post/7675614776635670582) | 深小乐 | 赞4/藏6/阅374 | 认可 Everything is a Plugin，但认为当前预览不适合普通用户。体验判断，对照你的受众。 | https://juejin.cn/post/7675614776635670582 |
| 14 | [从 0 到 1，DeepSeek Harness 保姆级安装与使用教程](https://juejin.cn/post/7675266921491267611) | 狂师 | 赞5/藏9/阅345 | 补 8/13 之后的安装路径，作者自称不追热点。步骤文，命令以当时官方为准。 | https://juejin.cn/post/7675266921491267611 |
| 15 | [RAG检索优化实战：从67%到92%](https://juejin.cn/post/7674794074012893238) | 神奇小汤圆 | 赞5/藏9/阅348 | 先建 Hit Rate@5 / MRR / Context Relevance，再调四步。67%→92% 是作者样本。适合已经上线在盲调 prompt 的人。 | https://juejin.cn/post/7674794074012893238 |

#### 收藏热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 15 | [我全程用 AI开发了一款微信小游戏，上线了](https://juejin.cn/post/7669058712007147539) | 程序员码歌 | 赞65/藏94/阅7621 | 复盘《箭头快跑呀》：选型、美术、审核、广告。旧文新上收藏榜；变现数字以作者自述为准。 | https://juejin.cn/post/7669058712007147539 |

### 开发工具

#### 文章热榜

| 排名 | 标题 | 作者 | 热度/互动 | 内容摘要 | 链接 |
| --- | ---:| --- | --- | --- | --- |
| 2 | [从零封装一个合同审查助手](https://juejin.cn/post/7676162994423119918) | 倔强的石头_ | 赞5/藏5/阅823 | WorkBuddy + 腾讯云 OCR 吃 5 种格式合同，要要素表、风险清单且能回原文。个人封装，含翻车记录。 | https://juejin.cn/post/7676162994423119918 |
| 10 | [GitHub 本周热门开源项目：Agent Infra与端侧 AI｜8.17–8.23](https://juejin.cn/post/7676110932394098731) | IvanCodes | 赞2/藏1/阅173 | 周五周报：diagram-design 一周 +1.1 万星等。时点数据，适合扫仓库。 | https://juejin.cn/post/7676110932394098731 |
| 11 | [【规范】这套 Git 规范，救了整个团队](https://juejin.cn/post/7675677773995999259) | JavaDog程序狗 | 赞2/藏3/阅164 | 用 force push 血案引出分支/评审规范。超过 3 人的团队可当检查清单，不是新工具。 | https://juejin.cn/post/7675677773995999259 |
| 12 | [Docker 部署禅道 ZenTao](https://juejin.cn/post/7675671057673256975) | 程序员老赵 | 赞2/藏5/阅122 | `easysoft/zentao:22.4` + MariaDB，数据留内网。适合不想上 SaaS Jira 的小团队。 | https://juejin.cn/post/7675671057673256975 |
| 14 | [2026年8月GitHub热榜深度拆解：Agent Skills席卷开源圈](https://juejin.cn/post/7676748940241633307) | 怪侠说不说 | 赞1/藏2/阅126 | 抓取基准 8/23：月榜多项是 Skills/记忆/路由。长文盘点，星数会变。 | https://juejin.cn/post/7676748940241633307 |
| 15 | [Docker 实战：使用 Nginx 作为容器入口代理 Node 服务](https://juejin.cn/post/7676375370355441691) | 东风破_ | 赞3/藏1/阅85 | 系列第二篇：多容器 + Nginx 反代 Express。入门拓扑，不是生产硬化。 | https://juejin.cn/post/7676375370355441691 |

#### 收藏热榜

本槽无新增。

### 跨榜重复与去重说明

- 本轮新摘要 URL 数：29
- 因 `seen_urls` 跳过：91（只给数量；不要把已见文再展开成表行）
- 同文多标签/双榜出现：无（29 条均只出现在单一槽位）

### 来源清单

- 快照日：2026-08-24（Asia/Shanghai）
- 页面：https://juejin.cn/hot/articles 、 https://juejin.cn/hot/collected-articles
- 抓取：`tools/juejin_hot_fetch.py` → `_staging_latest.json`

| 标签 | 榜单 | 标题 | 链接 |
| --- | --- | --- | --- |
| 后端 | 文章热榜 | 「速通Shell」数组与 mapfile | https://juejin.cn/post/7675181079705649206 |
| 后端 | 文章热榜 | 备份完不算完，先还原到临时库 | https://juejin.cn/post/7676421042796412968 |
| 后端 | 文章热榜 | DSH 搞得全世界都在安装 Node.js | https://juejin.cn/post/7675899462443122726 |
| 后端 | 文章热榜 | DeepSeek Harness 命令大全 | https://juejin.cn/post/7675947280080240691 |
| 后端 | 文章热榜 | DSH 必装插件 | https://juejin.cn/post/7675308265186983978 |
| 后端 | 文章热榜 | 为什么越来越多人用 kkFileView | https://juejin.cn/post/7676641074035605550 |
| 后端 | 文章热榜 | Codex 怎么突然变慢了 | https://juejin.cn/post/7675676910077345798 |
| 后端 | 文章热榜 | 给 AI 时代找工作的建议 | https://juejin.cn/post/7676277362519113763 |
| 后端 | 文章热榜 | Go 1.27 泛型方法与 JSON v2 | https://juejin.cn/post/7675914752422805514 |
| 前端 | 文章热榜 | 高级前端如何拒绝不合理需求 | https://juejin.cn/post/7675261669513953290 |
| 前端 | 文章热榜 | Vue 3D 图表库 | https://juejin.cn/post/7674878323556237355 |
| 前端 | 文章热榜 | 虚拟滚动真的更快吗 | https://juejin.cn/post/7676091857219272742 |
| 前端 | 文章热榜 | 面试官说打开你的 AI 工具 | https://juejin.cn/post/7674817329578606619 |
| 前端 | 文章热榜 | 先翻 DSH 的 .agents/ | https://juejin.cn/post/7674828652658425896 |
| 人工智能 | 文章热榜 | 这个本地模型让我 token 自由了 | https://juejin.cn/post/7676709710489419786 |
| 人工智能 | 文章热榜 | DSH 和 Codex 差在哪 | https://juejin.cn/post/7675538244907221001 |
| 人工智能 | 文章热榜 | 从失业到出书 | https://juejin.cn/post/7675947280080879667 |
| 人工智能 | 文章热榜 | 国产模型 DeepSeek / Kimi / GLM | https://juejin.cn/post/7675272903248920595 |
| 人工智能 | 文章热榜 | Skill 也可以测试 | https://juejin.cn/post/7675447922213568558 |
| 人工智能 | 文章热榜 | DSH 强，普通用户再等等 | https://juejin.cn/post/7675614776635670582 |
| 人工智能 | 文章热榜 | DSH 保姆级安装 | https://juejin.cn/post/7675266921491267611 |
| 人工智能 | 文章热榜 | RAG 检索从 67% 到 92% | https://juejin.cn/post/7674794074012893238 |
| 人工智能 | 收藏热榜 | 全程用 AI 开发微信小游戏 | https://juejin.cn/post/7669058712007147539 |
| 开发工具 | 文章热榜 | 合同审查助手 | https://juejin.cn/post/7676162994423119918 |
| 开发工具 | 文章热榜 | GitHub 本周热门 8.17–8.23 | https://juejin.cn/post/7676110932394098731 |
| 开发工具 | 文章热榜 | 这套 Git 规范救了整个团队 | https://juejin.cn/post/7675677773995999259 |
| 开发工具 | 文章热榜 | Docker 部署禅道 | https://juejin.cn/post/7675671057673256975 |
| 开发工具 | 文章热榜 | 8 月 GitHub 热榜深度拆解 | https://juejin.cn/post/7676748940241633307 |
| 开发工具 | 文章热榜 | Nginx 代理 Node 容器 | https://juejin.cn/post/7676375370355441691 |

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
    pairs = [
        (ROOT / "dailyReport/ai-daily-news/ai-daily-digest.md", [(AI_21, "2026-08-21"), (AI_22, "2026-08-22"), (AI_23, "2026-08-23")]),
        (ROOT / "dailyReport/ai-daily-news/202608.md", [(AI_21, "2026-08-21"), (AI_22, "2026-08-22"), (AI_23, "2026-08-23")]),
        (ROOT / "dailyReport/knowledge-base-news/knowledge-base-digest.md", [(KB_21, "2026-08-21"), (KB_22, "2026-08-22"), (KB_23, "2026-08-23")]),
        (ROOT / "dailyReport/knowledge-base-news/202608.md", [(KB_21, "2026-08-21"), (KB_22, "2026-08-22"), (KB_23, "2026-08-23")]),
    ]
    for path, secs in pairs:
        for section, heading in secs:
            insert_section(path, section, heading)
    insert_section(ROOT / "dailyReport/juejin-hot-news/juejin-hot-digest.md", JJ_SEC, "2026-08-24")
    insert_section(ROOT / "dailyReport/juejin-hot-news/202608.md", JJ_SEC, "2026-08-24")
    for d in ("2026-08-21", "2026-08-22", "2026-08-23"):
        update_state(ROOT / "dailyReport/ai-daily-news/ai-daily-state.json", d)
        update_state(ROOT / "dailyReport/knowledge-base-news/knowledge-base-state.json", d)
    merge_juejin_seen(
        ROOT / "dailyReport/juejin-hot-news/juejin-hot-state.json",
        ROOT / "dailyReport/juejin-hot-news/_staging_latest.json",
        "2026-08-24",
    )


if __name__ == "__main__":
    main()

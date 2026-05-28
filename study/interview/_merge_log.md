# Markdown 问答分类合并日志

## 2026-05-28（Transform / Advisor / ReAct 专题）

**源文件**：`study/interview/original/template.md`（Spring AI 核心概念与 ReAct/Transformer 辨析，109 行）

**操作**：提炼 5 条问答，合并至 3 个分类文件；无 `.bak` 备份。

| 分类文件 | 操作 | 条数变化 |
|----------|------|----------|
| Spring AI基础问答.md | 新增 + 合并增强 | +2 新增，1 条 Advisor 扩展替换（净 +3） |
| 文档与分块问答.md | 新增 | +1（ETL Transform 流水线） |
| Agent与对话问答.md | 新增 | +1（ReAct vs Transformer） |

**新增/扩展条目**：Transform 结构化输出、Advisor 机制（内置表+自定义）、Transformer vs Advisor、ETL Transform、ReAct vs Transformer 架构

**合计**：3 个文件更新，净增 5 条；语义去重合并 1 条（原 Advisor 条目）；失败 0 条。

## 2026-05-28（Ragas 专题合并）

**源文件**：`study/interview/original/template.md`（Ragas 框架简介，含指标与 Python 代码）

**操作**：提炼 6 条 Ragas 问答，合并至 `可观测与评估问答.md`；原 1 条 Ragas CI 条目扩展为 6 条；无 `.bak` 备份。

| 分类文件 | 操作 | 条数变化 |
|----------|------|----------|
| 可观测与评估问答.md | 合并增强 | 1 条替换扩展为 6 条（+5 净增） |

**新增/扩展条目**：Ragas 是什么、评估指标体系、快速上手、结果分析、进阶功能、Spring AI CI 集成

**合计**：1 个文件更新，净增 5 条（该文件共 9 条）；语义去重合并 1 条；失败 0 条。

## 2026-05-28（HyDE 专题合并）

**源文件**：`study/interview/original/template.md`（HyDE 总结技术文章，含 LangChain 代码与衍生方案）

**操作**：提炼 6 条 HyDE 问答，合并至 `RAG检索增强问答.md`；原 3 条 HyDE 条目扩展/替换为 6 条；无 `.bak` 备份。

| 分类文件 | 操作 | 条数变化 |
|----------|------|----------|
| RAG检索增强问答.md | 合并增强 | 3 条替换扩展为 6 条（+3 净增） |

**新增/扩展条目**：HyDE 是什么、为什么有效、优缺点、Spring AI 实现、LangChain 实现、衍生方案（HyPE/HyQE/SL-HyDE）

**合计**：1 个文件更新，净增 3 条（该文件共 20 条）；语义去重合并 3 条；失败 0 条。

## 2026-05-28（多路径检索与监控）

**源文件**：`study/interview/original/template.md`（Spring AI RAG 多路径检索与监控最佳实践，5 个技术点）

**操作**：提炼 5 条问答，合并至 4 个分类文件；无 `.bak` 备份。

| 分类文件 | 操作 | 条数变化 |
|----------|------|----------|
| Spring AI基础问答.md | 新增 | +1（Query 对象） |
| RAG检索增强问答.md | 新增 | +2（三路检索、MultiQueryExpander） |
| 可观测与评估问答.md | 新增 | +1（joined/reranked 埋点） |
| 文档与分块问答.md | 合并增强 | 1 条扩展（content vs metadata） |

**合计**：4 个文件更新，净增 4 条；语义去重合并 1 条；失败 0 条。

## 2026-05-28（RRF 专题合并）

**源文件**：`study/interview/original/template.md`（RRF 详解技术文章，非标准问答格式）

**操作**：从文章提炼 7 条问答，合并至 `RAG检索增强问答.md`；原「RRF 多路召回融合」单条扩展替换为 7 条完整条目；无 `.bak` 备份。

| 分类文件 | 操作 | 新增/更新条数 |
|----------|------|---------------|
| RAG检索增强问答.md | 更新 | +6 新增，1 条替换扩展 |

**合计**：1 个文件更新，净增 6 条（该文件共 15 条）；语义去重合并 1 条（原 RRF 伪代码并入「RRF 公式与融合计算」）；失败 0 条。

## 2026-05-28（修订）

**源文件**：`study/interview/original/template.md`（Spring AI RAG 技术面试全记录，34 条问答）

**操作**：按新规则重新生成全部 9 个分类文件（可读性 + 保留代码示例），无 `.bak` 备份。

**规则变更**：
- 答须分段/要点列表，提升可读性
- 源文件代码示例须保留并规范为 fenced code block

| 分类文件 | 操作 | 条数 |
|----------|------|------|
| Spring AI基础问答.md | 重写 | 3 |
| 文档与分块问答.md | 重写 | 6 |
| 向量与嵌入问答.md | 重写 | 3 |
| 索引与存储问答.md | 重写 | 4 |
| RAG Advisor问答.md | 重写 | 2 |
| RAG检索增强问答.md | 重写 | 9 |
| 可观测与评估问答.md | 重写 | 3 |
| 性能与高可用问答.md | 重写 | 2 |
| Agent与对话问答.md | 重写 | 2 |

**合计**：9 个分类文件，34 条问答；语义去重 0 条；失败 0 条。

## 2026-05-28（初版）

**源文件**：`study/interview/original/template.md`

**操作**：首次直写分类文件，无 `.bak` 备份。初版未保留代码块，已由修订版覆盖。

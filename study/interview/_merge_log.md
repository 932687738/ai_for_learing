# Markdown 问答分类合并日志

## 2026-05-28（Cursor 多智能体协同编码指南）

**源文件**：`study/interview/original/template.md`（Cursor Rules 分角色、五阶段顺序协同、Git/Composer 跨栈、最佳实践，290 行）

**说明**：源文件为 IDE 实践指南（非 Spring AI 问答体），按知识点相关性路由；Cursor 专属实践归入 `其他.md`。

| 模块文件 | 操作 | 条数变化 |
|----------|------|----------|
| Agent架构与协同.md | 新增 | +1（基于 Cursor Rules 的领域角色智能体） |
| Agent工作流模式.md | 新增 | +1（IDE 分阶段顺序多智能体协同） |
| 其他.md | 新建 | +1（Cursor 多智能体开发最佳实践） |

**路由备注**：与 Spring AI Agent 概念对照写入条目；无 `.bak`；失败 0 条。

**合计**：3 个文件更新/新建，净增 3 条；全库 76 条。

## 2026-05-28（知识点体系重构）

**操作**：将 9 个 `*问答.md`（73 条）迁移为 `study/interview/knowledge/` 标准知识点模块；删除旧问答文件；落地分类规范。

**规范文件**：

| 文件 | 用途 |
|------|------|
| `.cursor/knowledge-taxonomy.md` | 模块定义、路由关键词、条目格式（权威） |
| `.cursor/agents/markdown-qa-classify-merge.md` | Agent 流程 |
| `.cursor/skills/markdown-qa-classify-merge/SKILL.md` | Skill 触发与路径 |
| `.cursor/rules/markdown-qa-classify-merge.mdc` | Cursor Rule |
| `tools/migrate_qa_to_knowledge.py` | 旧问答 → 知识点批量迁移脚本 |

**知识点模块**（14 文件 + `索引.md`，73 条，中文文件名）：

| 模块文件 | 知识点数 |
|----------|------:|
| Spring AI核心组件.md | 7 |
| 文档ETL与分块.md | 7 |
| 向量与嵌入.md | 3 |
| 索引与存储.md | 7 |
| RAG Advisor.md | 3 |
| RAG检索策略.md | 7 |
| HyDE假设文档嵌入.md | 7 |
| RRF混合检索融合.md | 7 |
| RAG长期记忆.md | 1 |
| Agent记忆体系.md | 3 |
| Agent架构与协同.md | 4 |
| Agent工作流模式.md | 5 |
| 可观测与评估.md | 9 |
| 性能与高可用.md | 3 |

**路由调整**：`检索 Query 对象` → RAG检索策略；`记忆类型对比` → Agent记忆体系；RAG/Agent 大主题按子主题拆分。

**2026-05-28 补充**：知识点文件命名统一为**中文**（如 `Spring AI核心组件.md`）；索引文件为 `knowledge/索引.md`；规范见 `.cursor/knowledge-taxonomy.md`。

**合计**：14 模块 + `索引.md`；旧 `*问答.md` 已删除；文件名统一中文；失败 0 条。

## 2026-05-28（Spring AI 核心技术与实践指南）

**源文件**：`study/interview/original/template.md`（Transformer/Advisor、检索优化、提示词、回答检测、文本补全、问题转换、多 Agent、CoT/ToT、工作流模式，382 行）

**操作**：从实践指南提炼 11 条问答，按主题写入 6 个分类文件；语义去重合并增强 3 条既有问答；无 `.bak` 备份。

| 分类文件 | 操作 | 条数变化 |
|----------|------|----------|
| Spring AI基础问答.md | 合并增强 + 新增 | 1 条 Advisor 扩展（+ResponseValidationAdvisor），+2（PromptTemplate、ChatClient 补全模式） |
| RAG Advisor问答.md | 新增 | +1（ResponseValidationAdvisor 回答质量检测） |
| RAG检索增强问答.md | 合并增强 | 1 条扩展（查询改写 + QueryRewriteAdvisor CallAdvisor） |
| 索引与存储问答.md | 合并增强 + 新增 | 1 条 HNSW 扩展（+IVF/DiskANN），+2（ES 分片副本、routing 路由） |
| 性能与高可用问答.md | 新增 | +1（ChatClient @Cacheable 缓存） |
| Agent与对话问答.md | 新增 | +5（Sequential/Loop、共享记忆、Orchestrator/CoT/ToT、工作流模式、Handoff） |

**新增/扩展条目**：PromptTemplate 设计、ChatClient 同步/结构化/流式/参数调优、回答检测三方案、QueryRewriteAdvisor、ES 分片与 routing、AI 响应缓存、SequentialAgent/LoopAgent、CoT/ToT、五种工作流模式、多 Agent 交接

**合计**：6 个文件更新，净增 11 条（含 3 条语义合并增强）；失败 0 条。

## 2026-05-28（Spring AI 智能体操作数据库：组件顺序）

**源文件**：`study/interview/original/template.md`（组件定义表、匹配顺序、五步流程、餐厅类比，63 行）

**操作**：语义去重后合并增强 2 条既有问答；无 `.bak` 备份。

| 分类文件 | 操作 | 条数变化 |
|----------|------|----------|
| Agent与对话问答.md | 合并增强 | 1 条（+Spring AI 数据库场景、组件定位表、execute_sql 示例） |
| RAG检索增强问答.md | 合并增强 | 1 条（+Schema/查询模板、数据库场景价值说明） |

**合计**：2 个文件更新，净增 0 条；语义去重合并 2 条；失败 0 条。

## 2026-05-28（Skills / Tools / MCP / RAG 协同流程）

**源文件**：`study/interview/original/template.md`（五步流程、Mermaid 片段、餐厅类比，41 行）

**操作**：提炼 2 条问答，按主题写入 2 个分类文件；补全源文件残缺流程图为完整 Mermaid；无 `.bak` 备份。

| 分类文件 | 操作 | 条数变化 |
|----------|------|----------|
| Agent与对话问答.md | 新增 | +1（Skills/Tools/MCP/知识库五步协同） |
| RAG检索增强问答.md | 新增 | +1（Agent 流水线并行知识库检索） |

**新增条目**：Skills+Tools+MCP 协同流程与类比表、并行 RAG 子流程（查询重写→向量检索→上下文增强）

**合计**：2 个文件更新，净增 2 条；失败 0 条。

## 2026-05-28（Spring AI 记忆存储专题）

**源文件**：`study/interview/original/template.md`（短期/长期/永久记忆与代码示例，171 行）

**操作**：提炼 4 条问答，按主题写入 3 个分类文件；扩展合并 `Agent与对话` 既有短期记忆条目；无 `.bak` 备份。

| 分类文件 | 操作 | 条数变化 |
|----------|------|----------|
| Agent与对话问答.md | 合并增强 + 新增 | 1 条扩展（短期记忆），+1（AutoMemoryTools） |
| RAG检索增强问答.md | 新增 | +1（向量库跨会话长期记忆） |
| Spring AI基础问答.md | 新增 | +1（记忆类型对比与选型） |

**新增/扩展条目**：短期 ChatMemory 配置与用法、AutoMemoryTools、向量库长期记忆 RAG 注入、三种记忆对比选型表

**合计**：3 个文件更新，净增 3 条（含 1 条语义合并增强）；失败 0 条。

## 2026-05-28（similaritySearch vs similarityThreshold 扩展）

**源文件**：`study/interview/original/template.md`（检索方法对比全文，61 行）

**操作**：合并增强 `索引与存储问答.md` 中已有相似度阈值条目；无 `.bak` 备份。

| 分类文件 | 操作 | 条数变化 |
|----------|------|----------|
| 索引与存储问答.md | 合并增强 | 1 条扩展（+对比表、举例、SIMILARITY_THRESHOLD_ACCEPT_ALL、补充说明） |

**合计**：1 个文件更新，净增 0 条；语义去重合并 1 条；失败 0 条。

## 2026-05-28（相似度阈值检索策略）

**源文件**：`study/interview/original/template.md`（similaritySearch 与阈值过滤实践，17 行）

**操作**：提炼 1 条问答，合并至 `索引与存储问答.md`；无 `.bak` 备份。

| 分类文件 | 操作 | 条数变化 |
|----------|------|----------|
| 索引与存储问答.md | 新增 | +1（similaritySearch 与相似度阈值策略） |

**合计**：1 个文件更新，净增 1 条（该文件共 5 条）；失败 0 条。

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

# Spring AI 面试知识点分类体系

> 本文件为 `@markdown-qa-classify-merge` 的**知识点路由与文件格式**权威定义。Agent、Skill、Rule 均引用此处。

## 目标目录

```
study/interview/
├── knowledge/                    # 标准知识点文件（产出目录，中文文件名）
│   ├── 索引.md                   # 模块索引
│   ├── Spring AI核心组件.md
│   ├── 文档ETL与分块.md
│   ├── 向量与嵌入.md
│   ├── 索引与存储.md
│   ├── RAG Advisor.md
│   ├── RAG检索策略.md
│   ├── HyDE假设文档嵌入.md
│   ├── RRF混合检索融合.md
│   ├── RAG长期记忆.md
│   ├── Agent记忆体系.md
│   ├── Agent架构与协同.md
│   ├── Agent工作流模式.md
│   ├── 可观测与评估.md
│   ├── 性能与高可用.md
│   └── 其他.md                   # 无法归类时
├── original/                     # 原始待处理 Markdown
├── _merge_log.md
└── （禁止再新建 *问答.md）
```

## 分类原则（按知识点相关性）

1. **先识别知识点主题**，再映射到模块文件；一条源内容可拆入多个模块，但**同一知识点只保留一处**（语义去重后写入最相关模块）。
2. **禁止**按源文件名或文档总标题整包写入单一文件。
3. **大模块再按子主题拆分**（例如 RAG 检索拆为检索策略 / HyDE / RRF，Agent 拆为记忆 / 架构 / 工作流）。
4. 边界模糊时选**最接近下游使用场景**的模块，并在 `_merge_log.md` 注明。
5. **文件名一律使用中文**（见下表）；内部路由仍可用 `module_id` 标识，落盘时必须映射为中文文件名。

## 模块定义与路由

| module_id | 中文文件名 | 涵盖知识点 |
| :--- | :--- | :--- |
| `spring-ai-core` | `Spring AI核心组件.md` | ChatClient/ChatModel、Prompt/UserMessage、PromptTemplate、Transform 结构化输出、Advisor 机制、Transformer vs Advisor、Query 对象、记忆类型概览、文本补全模式 |
| `document-etl-chunking` | `文档ETL与分块.md` | DocumentReader、Tika、TokenTextSplitter、content/metadata、Enricher、ETL Transform 流水线 |
| `embedding-vectorstore` | `向量与嵌入.md` | EmbeddingModel、VectorStore.add、similaritySearch 调用链 |
| `index-storage` | `索引与存储.md` | 相似度阈值、元数据过滤、HNSW/IVF/DiskANN、多租户隔离、PgVector、ES 分片/routing |
| `rag-advisor` | `RAG Advisor.md` | QuestionAnswerAdvisor 流程与缓存、ResponseValidationAdvisor、回答质量检测 |
| `rag-retrieval-strategies` | `RAG检索策略.md` | 多路径召回、MultiQueryExpander、BM25 混合、Rerank、查询改写、metadata 关键词混合检索 |
| `rag-retrieval-hyde` | `HyDE假设文档嵌入.md` | HyDE 原理/实现/衍生、智能路由是否走 HyDE |
| `rag-retrieval-rrf` | `RRF混合检索融合.md` | RRF 公式、混合检索融合、各存储 RRF 配置、与其他融合方法对比 |
| `rag-memory` | `RAG长期记忆.md` | 向量库跨会话长期记忆、MemoryAdvisor 注入 |
| `agent-memory` | `Agent记忆体系.md` | ChatMemory 短期记忆、AutoMemoryTools、会话窗口与持久化 |
| `agent-architecture` | `Agent架构与协同.md` | ReAct、@Tool 动态 RAG、Skills/Tools/MCP 协同、Agent 流水线并行 RAG |
| `agent-workflow` | `Agent工作流模式.md` | SequentialAgent、LoopAgent、共享 ChatMemory 协作、Orchestrator/CoT/ToT、链式/路由/并行/评估器工作流、Handoff |
| `observability-evaluation` | `可观测与评估.md` | Micrometer 埋点、Tracing、Ragas、Prometheus/Grafana |
| `performance-reliability` | `性能与高可用.md` | 并行检索、CompletableFuture 超时、@Cacheable 缓存 |
| `other` | `其他.md` | 无法归类 |

### 标题关键词路由（RAG 检索增强类优先匹配）

| 关键词（标题或问句） | 目标 module_id → 中文文件 |
| :--- | :--- |
| HyDE、HyPE、HyQE、SL-HyDE、假设文档、智能路由判断是否 | `rag-retrieval-hyde` → `HyDE假设文档嵌入.md` |
| RRF、倒数排名、Reciprocal Rank | `rag-retrieval-rrf` → `RRF混合检索融合.md` |
| 跨会话长期记忆、MemoryAdvisor、向量库.*记忆 | `rag-memory` → `RAG长期记忆.md` |
| Agent 流水线.*RAG、Skills.*MCP | `agent-architecture` → `Agent架构与协同.md` |
| AutoMemoryTools、短期记忆、记忆类型对比 | `agent-memory` → `Agent记忆体系.md`（优先于 architecture 匹配） |
| 多路径、MultiQuery、BM25、Rerank、查询改写、metadata keywords | `rag-retrieval-strategies` → `RAG检索策略.md` |

## 标准知识点条目格式

模块文件结构：

```markdown
<!-- 模块：{模块中文名} | 最后更新于 YYYY-MM-DD -->

# {模块中文名}

> {一句话模块说明}

## 目录

- [知识点标题](#anchor)
...

---

## 知识点标题

> **模块**：{模块中文名} | **标签**：tag1, tag2 | **更新**：YYYY-MM-DD

### 核心概念

{1–3 句概括，来自答的提炼，非原文照搬}

### 要点

{答的正文：列表、表格、分步说明}

### 代码示例

\`\`\`java
...
\`\`\`

### 面试常问

**问**：{原问或等价面试题}

**答**：{精简可口述版，可与要点重复但须更短}

### 关联知识点

- [{关联标题}]({中文文件名}.md)

---
```

## 合并规则

1. 新知识点写入前：读目标模块全文，**语义去重**；已有则合并为更完整条目（更新要点/代码/面试常问）。
2. 同一知识点跨模块只保留主模块一份；次模块用「关联知识点」链接（**链接目标须为中文文件名**），不重复全文。
3. 更新模块文件头 `<!-- 模块：... | 最后更新于 ... -->`、刷新 `knowledge/索引.md` 与 `_merge_log.md`。
4. **禁止** `.bak.md`；**禁止**回写 `*问答.md` 旧格式；**禁止**新建英文 slug 文件名（如 `spring-ai-core.md`）。

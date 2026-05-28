# Spring AI RAG 技术面试全记录

> 面试官：Spring AI 与 RAG 技术专家  
> 候选人：开发者  
> 日期：2026-05-25 至 2026-05-28

---

## 1. DocumentReader 与 TikaDocumentReader

**问**：请解释 `DocumentReader` 在 Spring AI RAG 管道中的核心职责，并说明 `TikaDocumentReader` 相比其他 `DocumentReader` 实现的主要优势。

**答**：不清楚。

**参考答案**：
- `DocumentReader` 负责从不同数据源读取原始文档，生成 `Document` 对象（包含文本内容 `content` 和元数据 `metadata`）。
- `TikaDocumentReader` 基于 Apache Tika，能自动检测并解析多种格式（PDF、DOCX、XLSX、PPTX、HTML、XML、TXT 等）。优势：统一处理多格式，无需手动判断 MIME 类型或配置不同解析器。

---

## 2. TokenTextSplitter 与普通 TextSplitter

**问**：在 RAG 的 ETL 流程中，`TokenTextSplitter` 与普通 `TextSplitter` 在分块依据上有什么本质区别？为什么推荐使用 `TokenTextSplitter`？

**答**：不知道。

**参考答案**：
- 普通 `TextSplitter` 按字符数或段落等表面规则分块，不感知 LLM 的 token 限制。
- `TokenTextSplitter` 按 token 数量分块，能精确保证每块长度在模型上下文窗口内。
- 推荐原因：与 LLM 对齐（计费/限制按 token）、避免截断浪费、跨语言友好。

---

## 3. EmbeddingModel 与本地 ONNX 模型

**问**：在 Spring AI 中，`EmbeddingModel` 接口的 `embed(Document)` 方法返回值类型是什么？如果要使用本地的 ONNX 嵌入模型（例如 all-MiniLM-L6-v2），应该引入哪个具体实现类？

**答**：不知道。

**参考答案**：
- 返回值类型：`EmbeddingResponse`，封装了 `List<Embedding>`，每个 `Embedding` 包含浮点数向量。
- 本地 ONNX 模型实现类：`OnnxEmbeddingModel`（来自 `spring-ai-transformers` 依赖）。

---

## 4. VectorStore 相似度搜索与元数据过滤

**问**：Spring AI 中 `VectorStore` 接口的 `similaritySearch(SearchRequest)` 方法如何结合元数据过滤（`Filter.Expression`）？请写出一个代码示例，要求：筛选出 `category` 等于 `"technology"` 且 `score > 0.7` 的 Top-5 结果。

**答**：不知道。

**参考答案**：
```java
Filter.Expression filter = Filter.Expression.and(
    Filter.Expression.eq("category", "technology"),
    Filter.Expression.gt("score", 0.7)
);
SearchRequest searchRequest = SearchRequest.query("人工智能")
    .withTopK(5)
    .withFilterExpression(filter);
List<Document> results = vectorStore.similaritySearch(searchRequest);
5. QuestionAnswerAdvisor 缓存
问：在 Spring AI 生产级 RAG 应用中，QuestionAnswerAdvisor 默认每次请求同步调用向量存储。如何为检索结果引入缓存层，既能缓存相同或相似问题的检索结果，又能避免缓存污染？请给出基于 Spring Cache 或自定义 CacheManager 的配置思路。

答：不会。

参考答案：

缓存 Key 设计：归一化查询文本的 MD5，或查询向量的哈希。

避免污染：设置合理 TTL（如 5~30 分钟）；对实时性查询（含“今天”“昨天”）动态禁用缓存；使用条件注解 @CacheCondition。

示例：

java
@Cacheable(value = "ragResults", key = "#query.normalized()", condition = "#query.isCacheable()")
public List<Document> retrieve(String query, int topK) {
    return vectorStore.similaritySearch(SearchRequest.query(query).withTopK(topK));
}
6. 多路召回（向量 + BM25）
问：如何通过多路召回（例如结合关键词搜索 BM25 和向量搜索）来提升召回率？请简述在 Spring AI 中集成 ElasticsearchVectorStore 并实现混合检索的思路。

答：不会。

参考答案：

使用 ElasticsearchVectorStore 的混合检索配置：withHybridSearch(true)，设置向量权重和关键词权重。

若数据库不支持原生混合，可自行实现：分别调用 VectorStore 和 ElasticsearchRestTemplate，合并去重后送入 ReRanker。

7. 重排序（Rerank）集成
问：多路召回后，如何集成重排序模型（如 CrossEncoder）？请简要说明在 RetrievalAugmentationAdvisor 中添加 reranker 的步骤。

答：不会。

参考答案：

推荐使用 Spring AI Alibaba 的 RetrievalRerankAdvisor。

步骤：

添加依赖 spring-ai-alibaba-starter。
配置重排序模型（如 dashscope 的 gte-rerank-hybrid）。
在 ChatClient 构建时通过 .defaultAdvisors(new RetrievalRerankAdvisor(vectorStore, rerankModel)) 注入。
工作原理：检索 → 重排序（联合打分）→ 过滤排序 → 生成答案。

8. 查询改写（Query Rewriting）
问：如何通过查询改写缓解因用户表述不清而导致的检索失败？请给出 Spring AI 中的实现思路。

答：继续（追问后给出答案）。

参考答案：

使用内置组件：RewriteQueryTransformer（重写）、MultiQueryExpander（多查询扩展）、CompressionQueryTransformer（对话压缩）。

通过 RetrievalAugmentationAdvisor.builder().queryTransformers(...) 配置。

进阶：上下文感知改写、实体标准化、HyDE。

9. 可观测性（Metrics & Tracing）
问：生产环境如何对 RAG 各环节进行可观测性埋点？请说明 Micrometer Tracing 和核心指标。

答：不会。

参考答案：

使用 Micrometer Tracing 创建 Span 进行链路追踪。

核心指标：检索延迟（Timer）、Top-K 命中率（Counter）、重排序精度提升（Gauge）、缓存命中率、Token 消耗。

示例：

java
Timer.Sample sample = Timer.start(registry);
// 检索...
sample.stop(Timer.builder("vectorstore.search.duration").register(registry));
10. Ragas 评估集成
问：如何在 Spring AI 应用中集成 Ragas 评估框架？请给出 CI 流水线设计思路。

答：不会。

参考答案：

推荐独立 Python 评估服务（Docker 化），通过 HTTP 异步调用。

CI 流程：启动测试环境 → 部署 Spring AI 应用 → 测试运行器遍历数据集 → 调用 Ragas 服务 → 评估指标 → 质量门禁（如 context_recall >= 0.85）。

Java 侧替代：Dokimos 等框架进行单元测试式评估。

11. 向量索引优化（HNSW vs IVFFlat）
问：如何利用索引类型选择（HNSW、IVF_FLAT）以及分区/分片策略优化检索性能？请结合 Milvus、PgVector 或 Redis 给出配置建议。

答：不会。

参考答案：

HNSW：查询快、内存高、召回率高；IVFFlat：构建快、内存低、需训练。

PgVector 配置：index-type: HNSW，可调 m、ef_construction。

Milvus：支持多种索引，通过 MilvusVectorStoreConfig 配置。

Redis：支持 FLAT/HNSW，通过 builder 设置 hnswM、hnswEfRuntime。

分区策略：PgVector 分区表、Milvus 分区、Redis Key 前缀。

12. 可观测性大盘（Prometheus + Grafana）
问：在 Spring AI 中如何基于 Micrometer 为 RAG 链路建立性能基准和监控大盘？

答：不会。

参考答案：

添加 micrometer-registry-prometheus 依赖，暴露 /actuator/prometheus 端点。

关键指标：gen_ai_client_operation_seconds、db_vector_client_operation_seconds、ai.rag.relevancy.score。

部署 Prometheus + Grafana，导入仪表盘。

建立告警规则（如 LLM p99 延迟 >5s，Token 消耗突增）。

13. 异步并行检索与超时控制
问：如何通过异步并行检索和结果流式处理优化端到端延迟？结合 CompletableFuture 给出设计思路。

答：不会。

参考答案：

使用 @Async 和 CompletableFuture 并行查询多个向量存储或分区。

超时控制：.orTimeout(2, TimeUnit.SECONDS) + .exceptionally(ex -> Collections.emptyList())。

合并去重后送入重排序。

14. HyDE 实现
问：在 Spring AI 中实现 HyDE 的具体步骤是什么？请写出核心代码。

答：不会。

参考答案：

java
@Service
public class HyDEQueryTransformer {
    public String generateHypotheticalDocument(String query) {
        return chatClient.prompt()
            .user("请直接生成一篇详实的答案：\n" + query)
            .call()
            .content();
    }
}
然后实现 QueryTransformer 接口，在 transform 中调用生成方法，返回假设文档作为检索查询。

15. 多租户数据隔离
问：如何利用元数据过滤实现租户级别的数据隔离？请给出插入和检索时的代码示例。

答：不会。

参考答案：

插入时强制注入 tenant_id 到 metadata。

检索时构造 Filter.Expression.eq("tenant_id", tenantId)。

可选策略：单集合+过滤、每租户独立集合、每租户独立数据库、分区键。

16. Agent 与 RAG 协同（@Tool 注册与动态加载）
问：如何让 Agent 动态决定是否调用 RAG 检索？请给出使用 @Tool 注解并动态加载工具的设计。

答：提出思路：针对本地知识库增加方法，使用 @Tool 注解并包含名称和描述，agent 通过 tools 方法加载所有可用工具，如果没有则使用 LLM 能力进行外部检索。

评价与补充：

该思路是生产级 Agent 的核心模式。

实现步骤：

为每个知识库定义带 @Tool 的类，提供清晰的 name 和 description。
使用 KnowledgeToolRegistry 自动扫描并注册所有工具。
在 ChatClient 构建时通过 .defaultTools(allTools) 注册。
当工具数量过多时，可升级为动态工具发现（向量搜索工具定义）。
降级策略：本地无结果时调用 web_search 工具或 LLM 自身知识。
17. 多轮对话记忆管理
问：如何在多轮对话中让 Agent 记住上下文，并避免记忆膨胀？请说明 ChatMemory 与 ToolContext 的配合。

答：使用唯一 ID + ChatMemory + HashMap 做短期记忆，超过数量时压缩历史，提取重点进入下一轮；必要时用 ES/PgVector 做长期记忆。

评价：完全正确，符合生产实践。

短期记忆：MessageChatMemoryAdvisor + MessageWindowChatMemory 管理窗口。

长期记忆：JdbcChatMemoryRepository 或向量库存储摘要。

18. 基础巩固：ChatClient vs ChatModel
问：ChatClient 和 ChatModel 有什么区别？

答：Client 是对 Model 的封装。

评价：基本正确，补充：

ChatModel：底层接口，直接与具体模型 API 通信。

ChatClient：高层门面，提供流式、Advisor、Tool 调用、Prompt 模板等。

使用原则：默认用 Client，特殊场景（极简调用、底层调试）才用 Model。

19. Prompt 与 UserMessage 的关系
问：Prompt 和 UserMessage 分别代表什么？关系是什么？

答：Prompt 是提示词，分为系统提示词和用户提示词以及工具封装；UserMessage 是 Prompt 中的一个用户提示词组件。

评价：正确。Prompt 是消息列表容器，UserMessage 是其中代表用户的组件。

20. Advisor 的作用与位置
问：Advisor 接口的作用是什么？它的 around 方法在执行链路中处于什么位置？

答：Advisor 是切面，用于 Client 调用前后或失败的处理，调用大模型前后。

评价：正确。around 方法包裹 ChatClient 调用 ChatModel 的整个过程，支持链式执行和中断。

21. Document 的 content 与 metadata
问：Document 对象的 content 和 metadata 分别存储什么？请各举两个例子。

答：content 是实际内容，metadata 用于数据或权限隔离，可在 metadata 中进行筛选。

评价：完全正确。

content：文档正文、代码片段等。

metadata：tenant_id、source、page、created_at 等。

22. TokenTextSplitter 参数详解
问：chunkSize 和 chunkOverlap 分别控制什么？若 chunkSize=500, chunkOverlap=50，第二个块包含哪些 tokens？

答：不知道。

参考答案：

chunkSize：每个块的最大 token 数。

chunkOverlap：相邻块重叠的 token 数。

示例：块1 = 1-500，块2 = 451-950（从 451 开始，因为重叠 50）。

23. 其他分块工具
问：除了 TokenTextSplitter，还有没有类似的分块工具？

答：不知道（追问后回答）。

参考答案：

SentenceSplitter（Alibaba）：基于模型识别句子边界，中文友好。

RecursiveCharacterTextSplitter（Alibaba）：按分隔符优先级递归切割。

选择建议：中文优先用 SentenceSplitter 或 RecursiveCharacterTextSplitter。

24. VectorStore.add() 的两个职责
问：VectorStore.add(List<Document>) 内部通常会做哪两件事？

答：不知道（追问后回答）。

参考答案：

调用 EmbeddingModel 将每个 Document 的 content 转换为向量。

将 content、metadata 和向量存入数据库。

默认不做去重（SimpleVectorStore 按 id 覆盖，其他数据库按主键 upsert）。

25. 关键词/摘要存储位置
问：KeywordMetadataEnricher 和 SummaryMetadataEnricher 生成的关键词和摘要最终存储在哪里？

答：vector 的 metadata 中。

评价：正确。它们会写入 Document.metadata 的 keywords 和 summary 字段。

26. 元数据过滤中的 eq vs in
问：如何利用 metadata 中的 keywords 字段提升召回率？写出混合检索代码示例。

答：filter 中的 equals。

评价：正确，但数组字段应用 in 而非 eq。

java
Filter.Expression.in("keywords", "VectorStore")
27. SimpleVectorStore vs PgVector
问：SimpleVectorStore 和 PgVector 的主要区别？开发和生产环境分别选择哪个？

答：不知道。

参考答案：

SimpleVectorStore：内存存储，数据易失，适合开发测试。

PgVector：PostgreSQL + pgvector 扩展，持久化，适合生产。

28. QuestionAnswerAdvisor 工作流程
问：QuestionAnswerAdvisor 接收到用户问题后，会执行哪两个主要步骤？将什么内容传递给大模型？

答：拦截 PgVector，before 拆解文本转换向量，返回时组装对象，将向量传给大模型。

评价：部分错误。修正：

Before 阶段：调用 VectorStore.similaritySearch 检索相关文档。

调用大模型前：将检索到的 Document.content（文本）拼接到 Prompt 中，不是向量。

29. VectorStore 内部调用链
问：VectorStore.similaritySearch() 内部如何将用户问题转换成向量并进行检索？

答：不会。

参考答案：

调用 EmbeddingModel.embed(query) 生成查询向量。

执行数据库的 ANN 搜索（如 PgVector 的 <=> 操作符）。

将结果封装为 Document 列表返回。

30. HyDE 核心思路
问：简述 HyDE 的核心思路，与传统 Query2Vec 有何本质不同？

答：先将用户模糊的问题转为更精准详细的意图，再进行向量查询，避免歧义。

评价：接近，但本质是：生成一篇假设性的答案文档，用答案的向量去检索，而不是改写问题。

31. HyDE 不适用场景
问：什么场景下 HyDE 的召回提升不值得额外代价？

答：专有名词的查询，问题本身已经很规范。

评价：完全正确。

32. 智能路由（名词库）
问：如何自动判断问题是否需要 HyDE？

答：有一个专门的名词库，符合的走直通车，不符合的走 HyDE。

评价：优秀的设计思路。

33. RRF 多路召回融合
问：如何实现多路召回的结果融合？请给出 RRF 伪代码。

答：不清楚。

参考答案：

java
RRF_score(doc) = Σ 1 / (K + rank_i(doc))  // K=60
伪代码实现：

java
Map<String, Double> rrfScores = new HashMap<>();
for (List<Document> list : rankedLists) {
    for (int i=0; i<list.size(); i++) {
        double contribution = 1.0 / (K + i + 1);
        rrfScores.merge(list.get(i).getId(), contribution, Double::sum);
    }
}
34. 超时控制
问：如何用 CompletableFuture 设置超时，防止慢召回拖垮请求？

答：不会。

参考答案：

java
CompletableFuture.supplyAsync(() -> vectorSearch(query))
    .orTimeout(2, TimeUnit.SECONDS)
    .exceptionally(ex -> Collections.emptyList());
# Spring AI RAG 技术面试全记录（含完整代码）

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

**代码示例**：
```java
Resource pdfResource = new FileSystemResource("doc.pdf");
TikaDocumentReader reader = new TikaDocumentReader(pdfResource);
List<Document> docs = reader.read();
2. TokenTextSplitter 与普通 TextSplitter
问：在 RAG 的 ETL 流程中，TokenTextSplitter 与普通 TextSplitter 在分块依据上有什么本质区别？为什么推荐使用 TokenTextSplitter？

答：不知道。

参考答案：

普通 TextSplitter 按字符数或段落等表面规则分块，不感知 LLM 的 token 限制。

TokenTextSplitter 按 token 数量分块，能精确保证每块长度在模型上下文窗口内。

推荐原因：与 LLM 对齐（计费/限制按 token）、避免截断浪费、跨语言友好。

代码示例：

java
TokenTextSplitter splitter = new TokenTextSplitter(
    500,   // chunkSize (tokens)
    50,    // chunkOverlap (tokens)
    "cl100k_base" // tokenizer name
);
List<Document> chunks = splitter.split(documents);
3. EmbeddingModel 与本地 ONNX 模型
问：在 Spring AI 中，EmbeddingModel 接口的 embed(Document) 方法返回值类型是什么？如果要使用本地的 ONNX 嵌入模型（例如 all-MiniLM-L6-v2），应该引入哪个具体实现类？

答：不知道。

参考答案：

返回值类型：EmbeddingResponse，封装了 List<Embedding>，每个 Embedding 包含浮点数向量。

本地 ONNX 模型实现类：OnnxEmbeddingModel（来自 spring-ai-transformers 依赖）。

代码示例：

java
OnnxEmbeddingModelConfig config = new OnnxEmbeddingModelConfig(
    "path/to/all-MiniLM-L6-v2/",  // 模型目录
    "cpu"
);
EmbeddingModel embeddingModel = new OnnxEmbeddingModel(config);
4. VectorStore 相似度搜索与元数据过滤
问：Spring AI 中 VectorStore 接口的 similaritySearch(SearchRequest) 方法如何结合元数据过滤（Filter.Expression）？请写出一个代码示例，要求：筛选出 category 等于 "technology" 且 score > 0.7 的 Top-5 结果。

答：不知道。

参考答案：

java
Filter.Expression filter = Filter.Expression.and(
    Filter.Expression.eq("category", "technology"),
    Filter.Expression.gt("score", 0.7)
);

SearchRequest searchRequest = SearchRequest.query("人工智能")
    .withTopK(5)
    .withSimilarityThreshold(0.5)
    .withFilterExpression(filter);

List<Document> results = vectorStore.similaritySearch(searchRequest);
5. QuestionAnswerAdvisor 缓存
问：在 Spring AI 生产级 RAG 应用中，QuestionAnswerAdvisor 默认每次请求同步调用向量存储。如何为检索结果引入缓存层，既能缓存相同或相似问题的检索结果，又能避免缓存污染？请给出基于 Spring Cache 或自定义 CacheManager 的配置思路。

答：不会。

参考答案：

缓存 Key 设计：归一化查询文本的 MD5，或查询向量的哈希。

避免污染：设置合理 TTL（如 5~30 分钟）；对实时性查询（含“今天”“昨天”）动态禁用缓存；使用条件注解 @CacheCondition。

代码示例：

java
@Service
public class RAGService {
    @Cacheable(value = "ragResults", key = "#query.normalized()", condition = "#query.isCacheable()")
    public List<Document> retrieve(String query, int topK) {
        return vectorStore.similaritySearch(SearchRequest.query(query).withTopK(topK));
    }
}

public static String normalized(String raw) {
    return raw.toLowerCase().replaceAll("[\\p{Punct}]", "").trim();
}
6. 多路召回（向量 + BM25）
问：如何通过多路召回（例如结合关键词搜索 BM25 和向量搜索）来提升召回率？请简述在 Spring AI 中集成 ElasticsearchVectorStore 并实现混合检索的思路。

答：不会。

参考答案：

使用 ElasticsearchVectorStore 的混合检索配置：withHybridSearch(true)，设置向量权重和关键词权重。

若数据库不支持原生混合，可自行实现：分别调用 VectorStore 和 ElasticsearchRestTemplate，合并去重后送入 ReRanker。

代码示例：

java
ElasticsearchVectorStoreConfig config = ElasticsearchVectorStoreConfig.builder()
    .withIndexName("rag_docs")
    .withHybridSearch(true)
    .withHybridSearchAlpha(0.7)
    .build();
ElasticsearchVectorStore vectorStore = new ElasticsearchVectorStore(restClient, embeddingModel, config);

List<Document> results = vectorStore.similaritySearch(SearchRequest.query("我的问题").withTopK(10));
7. 重排序（Rerank）集成
问：多路召回后，如何集成重排序模型（如 CrossEncoder）？请简要说明在 RetrievalAugmentationAdvisor 中添加 reranker 的步骤。

答：不会。

参考答案：

推荐使用 Spring AI Alibaba 的 RetrievalRerankAdvisor。

步骤：

添加依赖 spring-ai-alibaba-starter。
配置重排序模型（如 dashscope 的 gte-rerank-hybrid）。
在 ChatClient 构建时通过 .defaultAdvisors(new RetrievalRerankAdvisor(vectorStore, rerankModel)) 注入。
代码示例：

java
@Configuration
public class RerankConfig {
    @Bean
    public ChatClient chatClient(ChatClient.Builder builder, VectorStore vectorStore, RerankModel rerankModel) {
        return builder
                .defaultAdvisors(new RetrievalRerankAdvisor(vectorStore, rerankModel))
                .build();
    }
}
8. 查询改写（Query Rewriting）
问：如何通过查询改写缓解因用户表述不清而导致的检索失败？请给出 Spring AI 中的实现思路。

答：继续（追问后给出答案）。

参考答案：

使用内置组件：RewriteQueryTransformer（重写）、MultiQueryExpander（多查询扩展）、CompressionQueryTransformer（对话压缩）。

通过 RetrievalAugmentationAdvisor.builder().queryTransformers(...) 配置。

代码示例：

java
ChatClient chatClient = ChatClient.builder(chatModel)
    .defaultAdvisors(
        RetrievalAugmentationAdvisor.builder()
            .queryTransformers(
                new RewriteQueryTransformer(chatClientBuilder, 
                    new PromptTemplate("请将以下用户问题重写为更清晰、更适合检索的查询：{query}"),
                    "vector-store"),
                MultiQueryExpander.builder()
                    .chatClientBuilder(chatClientBuilder)
                    .numberOfQueries(3)
                    .includeOriginal(true)
                    .build()
            )
            .documentRetriever(vectorStoreDocumentRetriever)
            .build()
    )
    .build();
9. 可观测性（Metrics & Tracing）
问：生产环境如何对 RAG 各环节进行可观测性埋点？请说明 Micrometer Tracing 和核心指标。

答：不会。

参考答案：

使用 Micrometer Tracing 创建 Span 进行链路追踪。

核心指标：检索延迟（Timer）、Top-K 命中率（Counter）、重排序精度提升（Gauge）、缓存命中率、Token 消耗。

代码示例：

java
@Autowired
private Tracer tracer;

public List<Document> retrieveWithTrace(String query) {
    Span span = tracer.nextSpan().name("vectorstore.similaritySearch").start();
    try (Tracer.SpanInScope ws = tracer.withSpanInScope(span)) {
        span.tag("query", query);
        span.tag("topK", String.valueOf(topK));
        return vectorStore.similaritySearch(SearchRequest.query(query).withTopK(topK));
    } catch (Exception e) {
        span.error(e);
        throw e;
    } finally {
        span.end();
    }
}
10. Ragas 评估集成
问：如何在 Spring AI 应用中集成 Ragas 评估框架？请给出 CI 流水线设计思路。

答：不会。

参考答案：

推荐独立 Python 评估服务（Docker 化），通过 HTTP 异步调用。

CI 流程：启动测试环境 → 部署 Spring AI 应用 → 测试运行器遍历数据集 → 调用 Ragas 服务 → 评估指标 → 质量门禁（如 context_recall >= 0.85）。

代码示例（Python 评估脚本）：

python
# ragas_evaluator.py
def evaluate_and_check():
    result = evaluate(test_dataset, metrics=[context_recall])
    assert result["context_recall"] >= 0.85, "召回率过低！"
11. 向量索引优化（HNSW vs IVFFlat）
问：如何利用索引类型选择（HNSW、IVF_FLAT）以及分区/分片策略优化检索性能？请结合 Milvus、PgVector 或 Redis 给出配置建议。

答：不会。

参考答案：

HNSW：查询快、内存高、召回率高；IVFFlat：构建快、内存低、需训练。

PgVector 配置：index-type: HNSW，可调 m、ef_construction。

代码示例（PgVector YAML 配置）：

yaml
spring:
  ai:
    vectorstore:
      pgvector:
        index-type: HNSW
        distance-type: COSINE_DISTANCE
        dimensions: 1536
Redis 配置：

java
RedisVectorStore vectorStore = RedisVectorStore.builder(jedisPooled, embeddingModel)
    .indexName("my_vector_index")
    .vectorAlgorithm(Algorithm.HNSW)
    .hnswM(32)
    .hnswEfConstruction(200)
    .build();
12. 可观测性大盘（Prometheus + Grafana）
问：在 Spring AI 中如何基于 Micrometer 为 RAG 链路建立性能基准和监控大盘？

答：不会。

参考答案：

添加 micrometer-registry-prometheus 依赖，暴露 /actuator/prometheus 端点。

关键指标：gen_ai_client_operation_seconds、db_vector_client_operation_seconds、ai.rag.relevancy.score。

代码示例（指标定义）：

java
@Bean
public MeterRegistryCustomizer<MeterRegistry> metricsConfig() {
    return registry -> registry.config().commonTags("application", "rag-service");
}

// 在检索方法中
Timer.Sample sample = Timer.start(registry);
// 执行检索...
sample.stop(Timer.builder("vectorstore.search.duration")
    .publishPercentiles(0.99, 0.95)
    .register(registry));
13. 异步并行检索与超时控制
问：如何通过异步并行检索和结果流式处理优化端到端延迟？结合 CompletableFuture 给出设计思路。

答：不会。

参考答案：

使用 @Async 和 CompletableFuture 并行查询多个向量存储或分区。

超时控制：.orTimeout(2, TimeUnit.SECONDS) + .exceptionally(ex -> Collections.emptyList())。

代码示例：

java
@Service
public class ParallelRetrievalService {
    @Async("vectorSearchExecutor")
    public CompletableFuture<List<Document>> searchFromStore1(String query, int topK) {
        List<Document> docs = vectorStore1.similaritySearch(
            SearchRequest.query(query).withTopK(topK)
        );
        return CompletableFuture.completedFuture(docs);
    }
}

// 合并与超时
CompletableFuture<List<Document>> future1 = parallelService.searchFromStore1(query, 20);
CompletableFuture.allOf(future1, future2, future3).orTimeout(2, TimeUnit.SECONDS).join();
14. HyDE 实现
问：在 Spring AI 中实现 HyDE 的具体步骤是什么？请写出核心代码。

答：不会。

参考答案：

java
@Service
public class HyDEQueryTransformer {
    @Autowired
    private ChatClient chatClient;

    public String generateHypotheticalDocument(String userQuery) {
        String prompt = """
            你是一个信息检索助手。请根据以下用户问题，直接生成一篇内容详实、信息准确的理想答案。
            用户问题：%s
            """.formatted(userQuery);
        return chatClient.prompt().user(prompt).call().content();
    }
}

@Component
public class HyDEQueryTransformer implements QueryTransformer {
    @Autowired
    private HyDEQueryTransformer hydeGenerator;

    @Override
    public String transform(String query) {
        return hydeGenerator.generateHypotheticalDocument(query);
    }
}
15. 多租户数据隔离
问：如何利用元数据过滤实现租户级别的数据隔离？请给出插入和检索时的代码示例。

答：不会。

参考答案：

java
// 插入时强制注入 tenant_id
public void addDocument(String content, Map<String, Object> extraMetadata) {
    String tenantId = tenantSecurityUtil.getCurrentTenantId();
    Map<String, Object> metadata = new HashMap<>(extraMetadata);
    metadata.put("tenant_id", tenantId);
    Document doc = new Document(content, metadata);
    vectorStore.add(List.of(doc));
}

// 检索时动态过滤
public List<Document> searchByTenant(String query, int topK) {
    String tenantId = tenantSecurityUtil.getCurrentTenantId();
    Filter.Expression tenantFilter = Filter.ExpressionBuilder.eq("tenant_id", tenantId);
    SearchRequest searchRequest = SearchRequest.query(query)
            .withTopK(topK)
            .withFilterExpression(tenantFilter);
    return vectorStore.similaritySearch(searchRequest);
}
16. Agent 与 RAG 协同（@Tool 注册与动态加载）
问：如何让 Agent 动态决定是否调用 RAG 检索？请给出使用 @Tool 注解并动态加载工具的设计。

答：针对本地知识库增加方法，使用 @Tool 注解并包含名称和描述，agent 通过 tools 方法加载所有可用工具，如果没有则使用 LLM 能力进行外部检索。

参考答案：

java
@Component
public class ProductDocumentTool {
    @Tool(name = "query_product_docs", 
         description = "查询产品功能、配置、API使用方法的官方文档知识库。")
    public String queryProductDocs(@ToolParam(description = "用户关于产品的具体问题") String query) {
        List<Document> docs = vectorStore.similaritySearch(SearchRequest.query(query).withTopK(3));
        return docs.stream().map(Document::getContent).collect(Collectors.joining("\n---\n"));
    }
}

@Service
public class KnowledgeToolRegistry {
    @Autowired
    private List<Object> allTools;
    private Map<String, Object> toolMap = new ConcurrentHashMap<>();
    
    @PostConstruct
    public void init() {
        for (Object tool : allTools) {
            // 通过反射获取 @Tool 注解的方法名注册
            toolMap.put(tool.getClass().getSimpleName(), tool);
        }
    }
    
    public Object[] getAllToolInstances() {
        return toolMap.values().toArray();
    }
}

// 配置 ChatClient
@Bean
public ChatClient agentChatClient(ChatClient.Builder builder) {
    return builder
        .defaultSystem("你是一个智能助手，优先使用知识库工具回答问题。")
        .defaultTools(toolRegistry.getAllToolInstances())
        .build();
}
17. 多轮对话记忆管理
问：如何在多轮对话中让 Agent 记住上下文，并避免记忆膨胀？请说明 ChatMemory 与 ToolContext 的配合。

答：使用唯一 ID + ChatMemory + HashMap 做短期记忆，超过数量时压缩历史，提取重点进入下一轮；必要时用 ES/PgVector 做长期记忆。

参考答案（短期记忆配置）：

java
@Bean
public ChatMemory chatMemory() {
    return new MessageWindowChatMemory(10); // 保留最近10条消息
}

@Bean
public ChatClient chatClient(ChatClient.Builder builder, ChatMemory chatMemory) {
    return builder
        .defaultAdvisors(new MessageChatMemoryAdvisor(chatMemory))
        .build();
}
18. 基础巩固：ChatClient vs ChatModel
问：ChatClient 和 ChatModel 有什么区别？

答：Client 是对 Model 的封装。

参考答案：

ChatModel：底层接口，直接与具体模型 API 通信。

ChatClient：高层门面，提供流式、Advisor、Tool 调用、Prompt 模板等。

代码对比：

java
// 底层 ChatModel
ChatResponse response = chatModel.call(new Prompt("你好"));

// 高层 ChatClient
String answer = chatClient.prompt()
    .user("你好")
    .advisors(new QuestionAnswerAdvisor(vectorStore))
    .call()
    .content();
19. Prompt 与 UserMessage 的关系
问：Prompt 和 UserMessage 分别代表什么？关系是什么？

答：Prompt 是提示词，分为系统提示词和用户提示词以及工具封装；UserMessage 是 Prompt 中的一个用户提示词组件。

代码示例：

java
Prompt prompt = new Prompt(
    List.of(
        new SystemMessage("你是一个Spring技术专家"),
        new UserMessage("RAG中的Advisor是什么？")
    )
);
20. Advisor 的作用与位置
问：Advisor 接口的作用是什么？它的 around 方法在执行链路中处于什么位置？

答：Advisor 是切面，用于 Client 调用前后或失败的处理，调用大模型前后。

代码示例：

java
@Component
public class LoggingAdvisor implements CallAroundAdvisor {
    @Override
    public AdvisedResponse around(AdvisedRequest request, AdvisorChain chain) {
        long start = System.currentTimeMillis();
        System.out.println("【前置】用户问题: " + request.userText());
        AdvisedResponse response = chain.next(request);
        System.out.println("【后置】耗时: " + (System.currentTimeMillis() - start) + "ms");
        return response;
    }
}
21. Document 的 content 与 metadata
问：Document 对象的 content 和 metadata 分别存储什么？请各举两个例子。

答：content 是实际内容，metadata 用于数据或权限隔离，可在 metadata 中进行筛选。

代码示例：

java
Document doc = new Document(
    "Spring AI 中的 RAG 通过 VectorStore 实现检索增强生成",
    Map.of("tenant_id", "company_a", "source", "api_docs.pdf", "page", 42)
);
22. TokenTextSplitter 参数详解
问：chunkSize 和 chunkOverlap 分别控制什么？若 chunkSize=500, chunkOverlap=50，第二个块包含哪些 tokens？

答：不知道。

参考答案：

chunkSize：每个块的最大 token 数。

chunkOverlap：相邻块重叠的 token 数。

示例：块1 = 1-500，块2 = 451-950（从 451 开始，因为重叠 50）。

23. 其他分块工具
问：除了 TokenTextSplitter，还有没有类似的分块工具？

答：不知道。

参考答案：

SentenceSplitter（Alibaba）：基于模型识别句子边界，中文友好。

RecursiveCharacterTextSplitter（Alibaba）：按分隔符优先级递归切割。

代码示例：

java
SentenceSplitter splitter = new SentenceSplitter(100);  // 最大100 token
List<Document> newDocuments = splitter.split(documents);

RecursiveCharacterTextSplitter splitter2 = new RecursiveCharacterTextSplitter();
List<Document> newDocs = splitter2.split(documents);
24. VectorStore.add() 的两个职责
问：VectorStore.add(List<Document>) 内部通常会做哪两件事？

答：不知道。

参考答案：

调用 EmbeddingModel 将每个 Document 的 content 转换为向量。

将 content、metadata 和向量存入数据库。

25. 关键词/摘要存储位置
问：KeywordMetadataEnricher 和 SummaryMetadataEnricher 生成的关键词和摘要最终存储在哪里？

答：vector 的 metadata 中。

代码示例：

java
KeywordMetadataEnricher enricher = new KeywordMetadataEnricher(chatModel, 5);
List<Document> enriched = enricher.apply(List.of(doc));
// doc.getMetadata().get("keywords") -> ["Spring AI", "VectorStore"]
26. 元数据过滤中的 eq vs in
问：如何利用 metadata 中的 keywords 字段提升召回率？写出混合检索代码示例。

答：filter 中的 equals。

补充：对于数组字段应使用 in 操作符。

java
Filter.Expression keywordFilter = Filter.ExpressionBuilder.in("keywords", "VectorStore");
SearchRequest request = SearchRequest.query("")
    .withFilterExpression(keywordFilter)
    .withTopK(5);
27. SimpleVectorStore vs PgVector
问：SimpleVectorStore 和 PgVector 的主要区别？开发和生产环境分别选择哪个？

答：不知道。

参考答案：

SimpleVectorStore：内存存储，数据易失，适合开发测试。

PgVector：PostgreSQL + pgvector 扩展，持久化，适合生产。

配置示例：

yaml
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/postgres
  ai:
    vectorstore:
      pgvector:
        index-type: HNSW
        distance-type: COSINE_DISTANCE
28. QuestionAnswerAdvisor 工作流程
问：QuestionAnswerAdvisor 接收到用户问题后，会执行哪两个主要步骤？将什么内容传递给大模型？

答：拦截 PgVector，before 拆解文本转换向量，返回时组装对象，将向量传给大模型。

纠正：

Before 阶段：调用 VectorStore.similaritySearch 检索相关文档。

调用大模型前：将检索到的 Document.content（文本）拼接到 Prompt 中，不是向量。

29. VectorStore 内部调用链
问：VectorStore.similaritySearch() 内部如何将用户问题转换成向量并进行检索？

答：不会。

参考答案：

java
// 伪代码
public List<Document> similaritySearch(SearchRequest request) {
    List<Double> queryVector = embeddingModel.embed(request.getQuery());
    // 执行 SQL: SELECT * FROM vectors ORDER BY embedding <=> queryVector LIMIT topK
    return database.search(queryVector, request.getTopK());
}
30. HyDE 核心思路
问：简述 HyDE 的核心思路，与传统 Query2Vec 有何本质不同？

答：先将用户模糊的问题转为更精准详细的意图，再进行向量查询，避免歧义。

纠正：本质是生成假设性答案，用答案的向量去检索。

31. HyDE 不适用场景
问：什么场景下 HyDE 的召回提升不值得额外代价？

答：专有名词的查询，问题本身已经很规范。

正确。

32. 智能路由（名词库）
问：如何自动判断问题是否需要 HyDE？

答：有一个专门的名词库，符合的走直通车，不符合的走 HyDE。

代码示例：

java
@Component
public class SmartRoutingAdvisor implements CallAroundAdvisor {
    @Autowired
    private TerminologyRegistry terminologyRegistry;
    
    @Override
    public AdvisedResponse around(AdvisedRequest request, AdvisorChain chain) {
        if (terminologyRegistry.containsTechnicalTerm(request.userText())) {
            // 直通车检索
        } else {
            // HyDE 检索
        }
    }
}
33. RRF 多路召回融合
问：如何实现多路召回的结果融合？请给出 RRF 伪代码。

答：不清楚。

参考答案：

java
public class RRFMerger {
    private static final int K = 60;
    
    public List<Document> merge(List<List<Document>> rankedLists) {
        Map<String, Double> rrfScores = new HashMap<>();
        for (List<Document> list : rankedLists) {
            for (int i = 0; i < list.size(); i++) {
                double contribution = 1.0 / (K + i + 1);
                rrfScores.merge(list.get(i).getId(), contribution, Double::sum);
            }
        }
        // 按分数降序排序返回
        return sortByScore(rrfScores);
    }
}
34. 超时控制
问：如何用 CompletableFuture 设置超时，防止慢召回拖垮请求？

答：不会。

参考答案：

java
CompletableFuture<List<Document>> future = CompletableFuture
    .supplyAsync(() -> vectorSearch(query))
    .orTimeout(2, TimeUnit.SECONDS)
    .exceptionally(ex -> {
        log.warn("检索超时", ex);
        return Collections.emptyList();
    });
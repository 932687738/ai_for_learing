<!-- 最后更新于 2026-05-28 -->

## 多路召回向量与 BM25

**问**：如何通过多路召回（例如结合关键词搜索 BM25 和向量搜索）来提升召回率？请简述在 Spring AI 中集成 ElasticsearchVectorStore 并实现混合检索的思路。

**答**：

- **原生混合**：ElasticsearchVectorStore 配置 `withHybridSearch(true)`，用 `withHybridSearchAlpha` 调节向量/关键词权重。
- **自行实现**：分别调用 VectorStore 与 ElasticsearchRestTemplate，合并去重后可选 ReRanker 精排。

**代码示例**：

```java
ElasticsearchVectorStoreConfig config = ElasticsearchVectorStoreConfig.builder()
    .withIndexName("rag_docs")
    .withHybridSearch(true)
    .withHybridSearchAlpha(0.7)
    .build();
ElasticsearchVectorStore vectorStore = new ElasticsearchVectorStore(restClient, embeddingModel, config);

List<Document> results = vectorStore.similaritySearch(SearchRequest.query("我的问题").withTopK(10));
```

分类标签：RAG检索增强 | 更新日期：2026-05-28

---

## 重排序 Rerank 集成

**问**：多路召回后，如何集成重排序模型（如 CrossEncoder）？请简要说明在 RetrievalAugmentationAdvisor 中添加 reranker 的步骤。

**答**：

1. 添加依赖 `spring-ai-alibaba-starter`。
2. 配置重排序模型（如 dashscope 的 `gte-rerank-hybrid`）。
3. 在 ChatClient 构建时通过 `.defaultAdvisors(new RetrievalRerankAdvisor(vectorStore, rerankModel))` 注入。

**代码示例**：

```java
@Configuration
public class RerankConfig {
    @Bean
    public ChatClient chatClient(ChatClient.Builder builder, VectorStore vectorStore, RerankModel rerankModel) {
        return builder
                .defaultAdvisors(new RetrievalRerankAdvisor(vectorStore, rerankModel))
                .build();
    }
}
```

分类标签：RAG检索增强 | 更新日期：2026-05-28

---

## 查询改写 Query Rewriting

**问**：如何通过查询改写缓解因用户表述不清而导致的检索失败？请给出 Spring AI 中的实现思路。

**答**：

- **RewriteQueryTransformer**：将口语化问题重写为检索友好查询。
- **MultiQueryExpander**：生成多条扩展查询并行召回。
- **CompressionQueryTransformer**：压缩多轮对话为单条检索 query。
- 通过 `RetrievalAugmentationAdvisor.builder().queryTransformers(...)` 配置。

**代码示例**：

```java
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
```

分类标签：RAG检索增强 | 更新日期：2026-05-28

---

## HyDE 实现步骤

**问**：在 Spring AI 中实现 HyDE 的具体步骤是什么？请写出核心代码。

**答**：

1. 用 ChatClient 根据用户问题生成「假设性理想答案」文档。
2. 对该文本做 embed 并 similaritySearch，而非直接对原始短问句向量化。
3. 封装为 `QueryTransformer` 接入 `RetrievalAugmentationAdvisor`。

**代码示例**：

```java
@Service
public class HyDEQueryGenerator {
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
    private HyDEQueryGenerator hydeGenerator;

    @Override
    public String transform(String query) {
        return hydeGenerator.generateHypotheticalDocument(query);
    }
}
```

分类标签：RAG检索增强 | 更新日期：2026-05-28

---

## HyDE 核心思路与 Query2Vec 区别

**问**：简述 HyDE 的核心思路，与传统 Query2Vec 有何本质不同？

**答**：

- **HyDE**：先让 LLM 生成假设性答案，用**答案向量**检索，语义更丰满。
- **Query2Vec**：直接对用户短问句 embed，易因表述模糊导致向量偏离。
- **本质区别**：检索用的文本由 LLM 扩写生成，而非原始 query。

分类标签：RAG检索增强 | 更新日期：2026-05-28

---

## HyDE 不适用场景

**问**：什么场景下 HyDE 的召回提升不值得额外代价？

**答**：

专有名词、SKU、错误码等已高度规范且简短的查询，或问题本身已足够精确时，直接 Query2Vec 即可；HyDE 额外 LLM 调用的延迟与成本不划算。

分类标签：RAG检索增强 | 更新日期：2026-05-28

---

## 智能路由判断是否使用 HyDE

**问**：如何自动判断问题是否需要 HyDE？

**答**：

维护术语/名词库（TerminologyRegistry），命中规范术语时走直通向量检索，否则走 HyDE。可在自定义 `CallAroundAdvisor` 中根据 `userText` 路由不同检索策略。

**代码示例**：

```java
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
```

分类标签：RAG检索增强 | 更新日期：2026-05-28

---

## metadata keywords 与混合检索

**问**：如何利用 metadata 中的 keywords 字段提升召回率？写出混合检索代码示例。

**答**：

对数组型 metadata 字段应使用 **`in`** 操作符，而非 `eq`。可将关键词过滤与向量 similaritySearch 组合使用。

**代码示例**：

```java
Filter.Expression keywordFilter = Filter.ExpressionBuilder.in("keywords", "VectorStore");
SearchRequest request = SearchRequest.query("")
    .withFilterExpression(keywordFilter)
    .withTopK(5);
```

分类标签：RAG检索增强 | 更新日期：2026-05-28

---

## RRF 多路召回融合

**问**：如何实现多路召回的结果融合？请给出 RRF 伪代码。

**答**：

Reciprocal Rank Fusion：对每路排序列表中第 i 名文档贡献 `1/(K+i+1)`（K 常取 60），同一文档 ID 分数累加，最后按 RRF 分降序合并。

**代码示例**：

```java
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
```

分类标签：RAG检索增强 | 更新日期：2026-05-28

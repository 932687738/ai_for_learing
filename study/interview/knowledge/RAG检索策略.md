<!-- 模块：RAG 检索策略 | 最后更新于 2026-05-28（Re-Ranker 手动集成） -->

# RAG 检索策略

> 多路召回、查询扩展/改写、混合检索与 Rerank。

## 目录

- [多路径检索三种召回策略](#多路径检索三种召回策略)
- [MultiQueryExpander.expand 的作用](#multiqueryexpanderexpand-的作用)
- [多路召回向量与 BM25](#多路召回向量与-bm25)
- [重排序 Rerank 集成](#重排序-rerank-集成)
- [查询改写 Query Rewriting](#查询改写-query-rewriting)
- [metadata keywords 与混合检索](#metadata-keywords-与混合检索)
- [检索 Query 对象 vs 直接传字符串](#检索-query-对象-vs-直接传字符串)
- [召回率 Recall 与提升手段](#召回率-recall-与提升手段)
- [Elasticsearch 混合检索 DSL 示例](#elasticsearch-混合检索-dsl-示例)

---
## 多路径检索三种召回策略

> **模块**：RAG 检索策略 | **标签**：RAG检索增强 | **更新**：2026-05-28

### 核心概念

生产级 RAG 中「原始语义 + MultiQueryExpander + 关键词扩展」三路检索有何区别？为什么要合并？

### 要点

| 维度 | 路径1（原始） | 路径2（语义扩展） | 路径3（关键词扩展） |
| :--- | :--- | :--- | :--- |
| 输入形式 | 用户原问题 | 多个自然语言变体 | 关键词组合/布尔查询 |
| 转换方式 | 无 | LLM 生成 | 规则/词典/模型扩展 |
| 检索原理 | 语义相似度 | 多角度语义覆盖 | 关键词匹配 + 语义 |
| LLM 依赖 | 无 | 需要 | 可能不需要 |
| 计算成本 | 低（1 次） | 高（K 次） | 中（1 次） |
| 召回类型 | 直接相关 | 间接相关、不同表述 | 含关键词但语义可能偏离 |

**合并原因**：路径 1 保精准度，路径 2 提召回率，路径 3 弥补语义检索遗漏的关键词匹配；合并常用 **RRF** 或加权平均。

### 代码示例

```java
// 路径1：原始问题直出 embedding
List<Document> originalDocs = searchKnowledgeDocuments(originalQuery.text(), perPathK);

// 路径2：MultiQueryExpander 扩展查询（不含原问）
MultiQueryExpander expander = MultiQueryExpander.builder()
    .numberOfQueries(3)
    .includeOriginal(false)
    .build();
List<Query> expandedQueries = expander.expand(originalQuery);

// 路径3：关键词扩展检索
Query keywordQuery = keywordExpansionQueryTransformer.transform(originalQuery);
List<Document> keywordDocs = searchKnowledgeDocuments(keywordQuery.text(), perPathK);
```

### 面试常问

**问**：生产级 RAG 中「原始语义 + MultiQueryExpander + 关键词扩展」三路检索有何区别？为什么要合并？

**答**：路径1（原始） 路径3（关键词扩展） :--- :--- 用户原问题 关键词组合/布尔查询 转换方式 LLM 生成 语义相似度 关键词匹配 + 语义 LLM 依赖 需要 低（1 次） 中（1 次） 召回类型 间接相关、不同表述 **合并原因**：路径 1 保精准度，路径 2 提召回率，路径 3 弥补语义检索遗漏的关键词匹配；合并常用 **RRF** 或加权平均。

### 关联知识点

- [HyDE 假设文档嵌入](HyDE假设文档嵌入.md)
- [RRF 混合检索融合](RRF混合检索融合.md)

---
## MultiQueryExpander.expand 的作用

> **模块**：RAG 检索策略 | **标签**：RAG检索增强 | **更新**：2026-05-28

### 核心概念

核心功能：利用 LLM 将一个用户查询扩展为多个语义不同但相关的查询变体，提高召回率，避免因用户措辞差异遗漏文档。

### 要点

- **核心功能**：利用 LLM 将一个用户查询扩展为多个语义不同但相关的查询变体，提高召回率，避免因用户措辞差异遗漏文档。
- **工作流程**：接收 `originalQuery` → 调用 ChatClient 按提示词模板生成变体 → 返回 `List<Query>`。
- **关键参数**：
  - `numberOfQueries`：生成变体数量。
  - `includeOriginal`：是否包含原始查询（多路径场景常设 `false`，避免与路径 1 重复）。

### 代码示例

```java
List<Query> expandedQueries = queryExpander.expand(originalQuery);
```

### 面试常问

**问**：`MultiQueryExpander.expand()` 的核心功能是什么？关键配置参数有哪些？

**答**：核心功能**：利用 LLM 将一个用户查询扩展为多个语义不同但相关的查询变体，提高召回率，避免因用户措辞差异遗漏文档。；工作流程**：接收 `originalQuery` → 调用 ChatClient 按提示词模板生成变体 → 返回 `List<Query>`。；关键参数**：；`numberOfQueries`：生成变体数量。。

### 关联知识点

- [HyDE 假设文档嵌入](HyDE假设文档嵌入.md)
- [RRF 混合检索融合](RRF混合检索融合.md)

---
## 多路召回向量与 BM25

> **模块**：RAG 检索策略 | **标签**：RAG检索增强 | **更新**：2026-05-28

### 核心概念

原生混合：ElasticsearchVectorStore 配置 `withHybridSearch(true)`，用 `withHybridSearchAlpha` 调节向量/关键词权重。

### 要点

- **原生混合**：ElasticsearchVectorStore 配置 `withHybridSearch(true)`，用 `withHybridSearchAlpha` 调节向量/关键词权重。
- **自行实现**：分别调用 VectorStore 与 ElasticsearchRestTemplate，合并去重后可选 ReRanker 精排。

### 代码示例

```java
ElasticsearchVectorStoreConfig config = ElasticsearchVectorStoreConfig.builder()
    .withIndexName("rag_docs")
    .withHybridSearch(true)
    .withHybridSearchAlpha(0.7)
    .build();
ElasticsearchVectorStore vectorStore = new ElasticsearchVectorStore(restClient, embeddingModel, config);

List<Document> results = vectorStore.similaritySearch(SearchRequest.query("我的问题").withTopK(10));
```

### 面试常问

**问**：如何通过多路召回（例如结合关键词搜索 BM25 和向量搜索）来提升召回率？请简述在 Spring AI 中集成 ElasticsearchVectorStore 并实现混合检索的思路。

**答**：原生混合**：ElasticsearchVectorStore 配置 `withHybridSearch(true)`，用 `withHybridSearchAlpha` 调节向量/关键词权重。；自行实现**：分别调用 VectorStore 与 ElasticsearchRestTemplate，合并去重后可选 ReRanker 精排。。

### 关联知识点

- [HyDE 假设文档嵌入](HyDE假设文档嵌入.md)
- [RRF 混合检索融合](RRF混合检索融合.md)

---
## 重排序 Rerank 集成

> **模块**：RAG 检索策略 | **标签**：RAG检索增强 | **更新**：2026-05-28

### 核心概念

多路召回后可用 CrossEncoder 类重排序模型精排；Spring AI 提供开箱即用的 `RetrievalRerankAdvisor`，也可通过 `DocumentPostProcessor` 手动接入任意 Rerank API。

### 要点

**开箱即用（RetrievalRerankAdvisor）**

1. 添加依赖（如 `spring-ai-alibaba-starter`）。
2. 配置 `RerankModel`（如 dashscope 的 `gte-rerank-hybrid`）。
3. ChatClient 构建时 `.defaultAdvisors(new RetrievalRerankAdvisor(vectorStore, rerankModel))`。

**手动集成（DocumentPostProcessor）**

- 实现 `DocumentPostProcessor`，在 `process(List<Document>)` 中调用重排序 API 对文档评分并排序。
- 适合自定义 Rerank 服务或非 Alibaba 生态模型。

### 代码示例

```java
@Configuration
public class RerankConfig {
    @Bean
    public ChatClient chatClient(ChatClient.Builder builder,
                                 VectorStore vectorStore,
                                 RerankModel rerankModel) {
        return builder
            .defaultAdvisors(new RetrievalRerankAdvisor(vectorStore, rerankModel))
            .build();
    }
}
```

```java
@Component
public class MyRerankProcessor implements DocumentPostProcessor {
    @Override
    public List<Document> process(List<Document> documents) {
        // 调用重排序 API 对文档评分并排序
        return rerankService.rerank(documents);
    }
}
```

### 面试常问

**问**：Spring AI 中如何实现 Re-Ranker？Advisor 与 PostProcessor 两种方式有何区别？

**答**：Advisor 方式用 `RetrievalRerankAdvisor` 与 VectorStore、RerankModel 一键集成；PostProcessor 方式实现 `DocumentPostProcessor` 在检索链路中自定义调用任意 Rerank API，灵活性更高。

### 关联知识点

- [多路召回向量与 BM25](#多路召回向量与-bm25)
- [RRF 混合检索融合](RRF混合检索融合.md)

---
## 查询改写 Query Rewriting

> **模块**：RAG 检索策略 | **标签**：RAG检索增强 | **更新**：2026-05-28

### 核心概念

RewriteQueryTransformer：将口语化问题重写为检索友好查询。

### 要点

- **RewriteQueryTransformer**：将口语化问题重写为检索友好查询。
- **MultiQueryExpander**：生成多条扩展查询并行召回。
- **CompressionQueryTransformer**：压缩多轮对话为单条检索 query。
- 通过 `RetrievalAugmentationAdvisor.builder().queryTransformers(...)` 配置。

### 代码示例

```java
@Component
public class QueryRewriteAdvisor implements CallAdvisor {
    private final ChatClient rewriteClient;

    public QueryRewriteAdvisor(ChatClient.Builder builder) {
        this.rewriteClient = builder
            .defaultSystem("Rewrite the user query into a clear, precise form. Output only the rewritten query.")
            .build();
    }

    @Override
    public AdvisedResponse adviseCall(AdvisedRequest request, CallAdvisorChain chain) {
        String rewritten = rewriteClient.prompt()
            .user("Original: " + request.userText())
            .call()
            .content();
        AdvisedRequest newRequest = AdvisedRequest.from(request).withUserText(rewritten).build();
        return chain.nextCall(newRequest);
    }

    @Override
    public int getOrder() { return 1; }
}

// 多查询变体并行检索
List<String> variants = List.of(
    "How to optimize retrieval in Spring AI",
    "Spring AI retrieval performance tuning",
    "Boost query speed in Spring AI"
);
// 并行检索后合并结果
```

### 面试常问

**问**：如何通过查询改写缓解因用户表述不清而导致的检索失败？请给出 Spring AI 中的实现思路。

**答**：RewriteQueryTransformer**：将口语化问题重写为检索友好查询。；MultiQueryExpander**：生成多条扩展查询并行召回。；CompressionQueryTransformer**：压缩多轮对话为单条检索 query。；通过 `RetrievalAugmentationAdvisor.builder().queryTransformers(...)` 配置。。

### 关联知识点

- [HyDE 假设文档嵌入](HyDE假设文档嵌入.md)
- [RRF 混合检索融合](RRF混合检索融合.md)

---
## metadata keywords 与混合检索

> **模块**：RAG 检索策略 | **标签**：RAG检索增强 | **更新**：2026-05-28

### 核心概念

对数组型 metadata 字段应使用 **`in`** 操作符，而非 `eq`。可将关键词过滤与向量 similaritySearch 组合使用。

### 要点

对数组型 metadata 字段应使用 **`in`** 操作符，而非 `eq`。可将关键词过滤与向量 similaritySearch 组合使用。

### 代码示例

```java
Filter.Expression keywordFilter = Filter.ExpressionBuilder.in("keywords", "VectorStore");
SearchRequest request = SearchRequest.query("")
    .withFilterExpression(keywordFilter)
    .withTopK(5);
```

### 面试常问

**问**：如何利用 metadata 中的 keywords 字段提升召回率？写出混合检索代码示例。

**答**：对数组型 metadata 字段应使用 **`in`** 操作符，而非 `eq`。可将关键词过滤与向量 similaritySearch 组合使用。

### 关联知识点

- [HyDE 假设文档嵌入](HyDE假设文档嵌入.md)
- [RRF 混合检索融合](RRF混合检索融合.md)

---
## 检索 Query 对象 vs 直接传字符串

> **模块**：RAG 检索策略 | **标签**：Spring AI基础 | **更新**：2026-05-28

### 核心概念

Query 作用：封装用户问题为标准检索对象，为后续扩展 TopK、相似度阈值、过滤表达式、元数据等参数预留空间。

### 要点

- **Query 作用**：封装用户问题为标准检索对象，为后续扩展 TopK、相似度阈值、过滤表达式、元数据等参数预留空间。
- **对比直接传字符串**：

| 直接传字符串 | 使用 Query 对象 |
| :--- | :--- |
| 无法携带额外参数 | 可携带阈值、过滤、用户标识等 |
| 接口变更成本高 | 扩展时无需修改方法签名 |
| 语义不明确 | 明确表达这是检索查询 |
| 不利于统一日志/监控 | 可嵌入检索类型、时间戳等元数据 |

### 代码示例

```java
Query originalQuery = Query.builder().text(question.trim()).build();
List<Document> originalDocs = searchKnowledgeDocuments(originalQuery.text(), perPathK);

// 可扩展的 Query 构建
Query query = Query.builder()
    .text(question.trim())
    .withTopK(5)
    .withSimilarityThreshold(0.7)
    .withFilterExpression("tenant_id == '123'")
    .build();
```

### 面试常问

**问**：Spring AI RAG 检索中为什么使用 `Query` 对象而不是直接传 `question.trim()` 字符串？

**答**：Query 作用**：封装用户问题为标准检索对象，为后续扩展 TopK、相似度阈值、过滤表达式、元数据等参数预留空间。；对比直接传字符串**：。

### 关联知识点

- [HyDE 假设文档嵌入](HyDE假设文档嵌入.md)
- [RRF 混合检索融合](RRF混合检索融合.md)

---
## 召回率 Recall 与提升手段

> **模块**：RAG 检索策略 | **标签**：RAG检索增强, 召回率 | **更新**：2026-05-28

### 核心概念

召回率衡量检索「查全」能力：**Recall = 检索到的相关文档数 / 总相关文档数**。RAG 生产优化常围绕提升召回再精排。

### 要点

| 手段 | 说明 |
| :--- | :--- |
| 混合检索 | 向量 + BM25 关键词取并集，互补语义与精确匹配 |
| 增大 Top-K + Rerank | 先放宽召回（如 10→100），再用 CrossEncoder 精排 |
| 查询扩展 | LLM 生成同义问句，或 HyDE 假设文档嵌入 |
| 多路召回 | 不同 embedding 模型分别检索后合并（常配合 RRF） |

- 召回与精度常需权衡：先保召回，再用阈值/Rerank 控噪声。
- HyDE、MultiQuery、RRF 等细节见各专项模块，此处强调组合思路。

### 面试常问

**问**：RAG 系统中召回率如何定义？有哪些常见提升手段？

**答**：Recall = 命中相关文档数 / 全部相关文档数。可混合向量与 BM25、扩大 Top-K 后 Rerank、做查询扩展（含 HyDE）或多 embedding 多路召回再融合。

### 关联知识点

- [HyDE 假设文档嵌入](HyDE假设文档嵌入.md)
- [RRF 混合检索融合](RRF混合检索融合.md)
- [重排序 Rerank 集成](#重排序-rerank-集成)

---
## Elasticsearch 混合检索 DSL 示例

> **模块**：RAG 检索策略 | **标签**：Elasticsearch, 混合检索 | **更新**：2026-05-28

### 核心概念

在 Elasticsearch 中可用 `bool.should` 并行组合**关键词 match** 与 **script_score 向量相似度**，实现原生混合检索。

### 要点

- `match` 分支负责 BM25 关键词召回。
- `script_score` + `cosineSimilarity` 负责向量语义召回。
- 两路结果由 ES 统一打分排序；多路独立召回场景可改用 RRF 融合（见 RRF 模块）。

### 代码示例

```json
{
  "query": {
    "bool": {
      "should": [
        { "match": { "content": "用户查询关键词" } },
        {
          "script_score": {
            "query": { "match_all": {} },
            "script": {
              "source": "cosineSimilarity(params.query_vector, 'vector_field') + 1.0",
              "params": { "query_vector": [0.1, 0.2] }
            }
          }
        }
      ]
    }
  }
}
```

### 面试常问

**问**：不用 Spring AI 封装时，Elasticsearch 如何实现向量+关键词混合检索？

**答**：在 `bool.should` 中并列 `match`（BM25）与 `script_score`（cosineSimilarity 向量分），由 ES 合并打分；若多路独立列表需更稳健融合，可后接 RRF。

### 关联知识点

- [多路召回向量与 BM25](#多路召回向量与-bm25)
- [RRF 混合检索融合](RRF混合检索融合.md)

---
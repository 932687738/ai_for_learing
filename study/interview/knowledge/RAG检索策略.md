<!-- 模块：RAG 检索策略 | 最后更新于 2026-06-06（CRAG 与子查询）） -->

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

- [CRAG 纠错检索增强生成](#crag-纠错检索增强生成)
- [子查询 Sub-Query 模式](#子查询-sub-query-模式)
- [DIN-SQL 与子查询模式对比](#din-sql-与子查询模式对比)
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

## CRAG 纠错检索增强生成

> **模块**：RAG 检索策略 | **标签**：CRAG, 检索评估, 纠错 | **更新**：2026-06-06

### 核心概念

CRAG（Corrective RAG）在生成前对检索结果做质量评估与分流：高置信精炼内部知识，低置信丢弃并走网络搜索，模糊时双源协同，降低噪声误导 LLM。

### 要点

- **三大检索问题**：主题相似但未答题、内容过时、知识库污染。
- **流程**：检索 → 评估器打分 → 分流（Correct/Incorrect/Ambiguous）→ 知识精炼 k_in / 网络搜索 k_ex → 整合后生成。
- **阈值**：置信度建议从 0.5–0.7 调优；评估结果可缓存减 LLM 调用。
- **局限**：延迟与复杂度上升、依赖外部搜索质量、评估器精度是瓶颈。
- **实现**：LangGraph/LlamaIndex `corrective-rag` 等即插即用模块。

### 面试常问

**问**：CRAG 是什么？解决什么问题？

**答**：纠正性 RAG，在生成前评估检索质量并纠错——好结果精炼、差结果换外部搜索、模糊时双源合并，避免脏文档直接喂给 LLM。

### 关联知识点

- [多路径检索三种召回策略](#多路径检索三种召回策略)
- [HyDE 假设文档嵌入](HyDE假设文档嵌入.md)

---
## 子查询 Sub-Query 模式

> **模块**：RAG 检索策略 | **标签**：Sub-Query, 多跳问答, 问题分解 | **更新**：2026-06-06

### 核心概念

子查询模式将复杂问题拆为多个可独立回答的子问题，分别检索/求解后聚合，降低单步难度并提升多跳问答可解释性。

### 要点

- **流程**：分解 → 并行/串行执行子问题 → 答案融合。
- **示例**：「《流浪地球》导演的第一部电影？」→ Q1 导演是谁 → Q2 该导演首作。
- **与 Multi-hop**：子查询是显式分解策略；CoT 侧重推理链而非独立问答。
- **优点**：准确性高、可展示中间步骤、子问题可并行。
- **挑战**：分解质量依赖 LLM、误差累积、多次调用成本。
- **实现**：LangChain MultiQuery/自定义分解链；Spring AI Alibaba Graph 分解+检索+聚合节点。

### 面试常问

**问**：子查询模式如何工作？适用场景？

**答**：复杂问题拆成子问题分别查知识库或调工具，再合并答案。适合跨文档多跳问答；分解错误会传导，需配合 Observation 自修复或人工校验。

### 关联知识点

- [DIN-SQL 与子查询模式对比](#din-sql-与子查询模式对比)
- [Text2SQL 核心流程与高级技术](Agent架构与协同.md)

---
## DIN-SQL 与子查询模式对比

> **模块**：RAG 检索策略 | **标签**：DIN-SQL, Sub-Query, 查询分解 | **更新**：2026-06-06

### 核心概念

两者都「分而治之」，但子查询在问题级拆独立子问答，DIN-SQL 在 SQL 结构级拆 SELECT/JOIN/WHERE 等子句并串行组合为单条 SQL。

### 要点

| 维度 | 子查询模式 | DIN-SQL |
| :--- | :--- | :--- |
| 分解粒度 | 问题级（可跨数据源） | SQL 子句级 |
| 输出 | 多个子答案再合并 | 单条完整 SQL |
| 依赖 | 子问题可并行 | 严格串行，前步错则全错 |
| 场景 | 多跳问答、多源整合 | 单库复杂 SQL（JOIN/嵌套/聚合） |
| Schema | 不一定需要 | 必须 |

- 可嵌套：子查询中的某一子问题若需复杂 SQL，可用 DIN-SQL 生成；DIN-SQL 的嵌套 SELECT 也可视为子任务。
- 长尾/冷启动：两者结合动态 Few-shot 与 Observation 自修复效果更好。

### 面试常问

**问**：DIN-SQL 和子查询模式有什么区别？

**答**：子查询拆成多个独立问题分别回答再合并；DIN-SQL 把生成一条复杂 SQL 的过程拆成链接 schema、写 JOIN、写 WHERE 等步骤。前者偏问答编排，后者偏 SQL 生成。

### 关联知识点

- [子查询 Sub-Query 模式](#子查询-sub-query-模式)
- [Text2SQL 核心流程与高级技术](Agent架构与协同.md)

---


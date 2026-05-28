<!-- 最后更新于 2026-05-28 -->

## 多路径检索三种召回策略

**问**：生产级 RAG 中「原始语义 + MultiQueryExpander + 关键词扩展」三路检索有何区别？为什么要合并？

**答**：

| 维度 | 路径1（原始） | 路径2（语义扩展） | 路径3（关键词扩展） |
| :--- | :--- | :--- | :--- |
| 输入形式 | 用户原问题 | 多个自然语言变体 | 关键词组合/布尔查询 |
| 转换方式 | 无 | LLM 生成 | 规则/词典/模型扩展 |
| 检索原理 | 语义相似度 | 多角度语义覆盖 | 关键词匹配 + 语义 |
| LLM 依赖 | 无 | 需要 | 可能不需要 |
| 计算成本 | 低（1 次） | 高（K 次） | 中（1 次） |
| 召回类型 | 直接相关 | 间接相关、不同表述 | 含关键词但语义可能偏离 |

**合并原因**：路径 1 保精准度，路径 2 提召回率，路径 3 弥补语义检索遗漏的关键词匹配；合并常用 **RRF** 或加权平均。

**代码示例**：

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

分类标签：RAG检索增强 | 更新日期：2026-05-28

---

## MultiQueryExpander.expand 的作用

**问**：`MultiQueryExpander.expand()` 的核心功能是什么？关键配置参数有哪些？

**答**：

- **核心功能**：利用 LLM 将一个用户查询扩展为多个语义不同但相关的查询变体，提高召回率，避免因用户措辞差异遗漏文档。
- **工作流程**：接收 `originalQuery` → 调用 ChatClient 按提示词模板生成变体 → 返回 `List<Query>`。
- **关键参数**：
  - `numberOfQueries`：生成变体数量。
  - `includeOriginal`：是否包含原始查询（多路径场景常设 `false`，避免与路径 1 重复）。

**代码示例**：

```java
List<Query> expandedQueries = queryExpander.expand(originalQuery);
```

**扩展示例**（用户问「怎么学 Spring AI」）：

- "Spring AI 的学习步骤是什么？"
- "Spring AI 入门教程有哪些？"
- "如何上手 Spring AI 框架？"

分类标签：RAG检索增强 | 更新日期：2026-05-28

---

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

分类标签：RAG检索增强 | 更新日期：2026-05-28

---

## HyDE 是什么

**问**：什么是 HyDE（Hypothetical Document Embeddings）？核心思想是什么？

**答**：

- **定义**：HyDE 是一种 RAG 检索增强技术——先让 LLM 根据用户问题「想象」一份理想答案（假想文档），再基于**假想文档的向量**检索真实文档。
- **一句话**：不要直接搜文档，先让 AI 构思最佳答案的样子，再用这个想法去搜。

**工作流程**：

1. **用户提问**（如「LangSmith 是什么？为什么需要它？」）
2. **生成假想文档**：LLM 生成「看起来像答案」的文本（可不真实，但语义/结构有参考价值）
3. **转换为嵌入向量**：用嵌入模型将假想文档转为稠密向量
4. **基于假想文档检索**：用该向量在向量库做相似性搜索
5. **生成最终答案**：将召回的真实文档作为上下文，交给 LLM 回答

分类标签：RAG检索增强 | 更新日期：2026-05-28

---

## HyDE 为什么有效与 Query2Vec 区别

**问**：HyDE 为什么能提升召回？与传统 Query2Vec 有何本质不同？

**答**：

**为什么有效**：

- **意图理解更准**：假想文档比短查询语义更丰富，弥补信息不足。
- **零样本可用**：无需标注数据，直接利用 LLM 通用知识。
- **效果显著**：实验中 Top-3 召回率从 78% 提升到 91%。

**与 Query2Vec 的本质区别**：

- **HyDE**：用 LLM 生成的**假设性答案向量**检索。
- **Query2Vec**：直接对用户短问句 embed，易因表述模糊导致向量偏离。

分类标签：RAG检索增强 | 更新日期：2026-05-28

---

## HyDE 优缺点与适用场景

**问**：HyDE 有哪些优缺点？什么场景不适合使用？

**答**：

| 优点 | 缺点 |
| :--- | :--- |
| 无需标注数据 | 每次检索需调用 LLM 生成假想文档，增加延迟和成本 |
| 理解深层意图 | 假想文档可能含「幻觉」，需对比编码器过滤 |
| 易于集成（LangChain 等） | 不适合对响应延迟极其敏感的场景 |

**不适用场景**：专有名词、SKU、错误码等已高度规范且简短的查询，或问题本身已足够精确时，直接 Query2Vec 更划算。

分类标签：RAG检索增强 | 更新日期：2026-05-28

---

## HyDE Spring AI 实现

**问**：在 Spring AI 中如何实现 HyDE？请写出核心代码。

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

## HyDE LangChain 实现

**问**：如何使用 LangChain 的 `HypotheticalDocumentEmbedder` 实现 HyDE？

**答**：

`HypotheticalDocumentEmbedder` 是 LangChain 内置类，自动完成「生成假想文档 → 嵌入 → 检索」流程；也可手动拆分各步骤做精细控制。

**代码示例**：

```python
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.retrievers import HypotheticalDocumentEmbedder

# 1. 初始化 LLM 和嵌入模型
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
base_embeddings = OpenAIEmbeddings()

# 2. 创建 HyDE 检索器（包装普通嵌入模型）
hyde_retriever = HypotheticalDocumentEmbedder(
    llm=llm,
    base_embeddings=base_embeddings,
    prompt_key="web_search"   # 使用内置提示模板或自定义
)

# 3. 准备向量数据库（示例使用 FAISS 内存存储）
#    假设已有文档片段列表 documents
# vectorstore = FAISS.from_documents(documents, base_embeddings)
# retriever = vectorstore.as_retriever()

# 4. 用 HyDE 检索器生成假想文档并搜索
# query = "LangSmith 是什么？为什么需要它？"
# relevant_docs = hyde_retriever.get_relevant_documents(query)
# print(relevant_docs)
```

分类标签：RAG检索增强 | 更新日期：2026-05-28

---

## HyDE 衍生方案

**问**：HyDE 有哪些衍生改进方案？

**答**：

- **HyPE**：将生成过程迁移到**索引阶段**，降低查询延迟。
- **HyQE**：生成假想**查询**（而非假想文档），从另一角度改进检索对齐。
- **SL-HyDE**：引入自学习机制，迭代优化假想文档质量。

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

## RRF 是什么

**问**：什么是 RRF（Reciprocal Rank Fusion）？主要用在什么场景？

**答**：

- **定义**：RRF（倒数排名融合）是一种**结果融合算法**，将多种检索方式各自得到的排序列表合并为统一、更优的最终排名。
- **典型场景**：**混合检索（Hybrid Search）**，例如 BM25 关键词检索 + 向量 ANN 检索并行召回后的结果融合。

分类标签：RAG检索增强 | 更新日期：2026-05-28

---

## 为什么混合检索需要 RRF

**问**：单一检索方式有什么缺陷？RRF 要解决什么问题？

**答**：

| 检索方式 | 优点 | 缺点 |
| :--- | :--- | :--- |
| **关键词（BM25/TF-IDF）** | 精确匹配术语、型号、专有名词 | 无语义理解，搜「智能手机」找不到「iPhone」 |
| **向量（ANN）** | 语义理解强，近义词召回好 | 可能漏掉精确关键词匹配 |

**RRF 目标**：结合两者优势，让结果既包含精确术语匹配，又包含语义相关内容。

分类标签：RAG检索增强 | 更新日期：2026-05-28

---

## RRF 公式与融合计算

**问**：RRF 的核心公式是什么？请结合示例说明如何计算最终排名。

**答**：

**核心公式**：

```
RRF(d) = Σ_{i=1}^{k} 1 / (r_i(d) + 60)
```

- `d`：某个文档；`k`：检索路数；`r_i(d)`：文档 d 在第 i 路结果中的排名（从 1 开始）；`60`：平滑常数，防止靠后排名得分过低。

**示例**（问题：「如何训练神经网络」）：

- BM25 第 1 名《神经网络训练指南》+ 向量第 2 名同一文档 → 两路得分累加 **0.0325** → 融合第 1 名。
- 仅在某一路排名第 1、另一路未出现的文档，融合后通常低于两路都靠前的文档。

**代码示例（应用层 RRF 合并）**：

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
        return sortByScore(rrfScores);
    }
}
```

分类标签：RAG检索增强 | 更新日期：2026-05-28

---

## RRF 核心特性

**问**：RRF 相比直接合并原始分数有哪些优势？

**答**：

1. **无需归一化**：BM25 分与向量相似度量纲不同，RRF 只依赖**排名位置**，避开归一化难题。
2. **位置权重递减**：排名越靠前贡献越大（第 1 名 ≈ 0.0164，第 10 名 ≈ 0.0143），差距不会过于悬殊。
3. **自动处理缺失**：某文档在某路未出现则该项贡献为 0，不因「缺席」被额外惩罚。

分类标签：RAG检索增强 | 更新日期：2026-05-28

---

## Spring AI 中配置 RRF 混合检索

**问**：在 Spring AI 中如何启用 RRF 混合检索？Elasticsearch 向量存储如何配置？

**答**：

Spring AI 对 **Elasticsearch、OpenSearch** 等支持混合检索的向量存储内置 RRF。启用后自动执行 BM25 → ANN → RRF 融合三步。

**代码示例（application.yml）**：

```yaml
spring:
  ai:
    vectorstore:
      elasticsearch:
        hybrid:
          enabled: true
          similarity: rrf          # 使用 RRF 作为融合策略
          rrf:
            rank-constant: 60      # RRF 公式中的平滑常数
            window-size: 100       # 参与融合的排名窗口大小
```

**代码示例（Java）**：

```java
@Autowired
private ElasticsearchVectorStore vectorStore;

public void hybridSearch(String query) {
    List<Document> results = vectorStore.similaritySearch(
        SearchRequest.builder()
            .query(query)
            .topK(5)
            .withHybridSearch(true)  // 启用混合检索
            .build()
    );
    // results 已是 RRF 融合后的最终结果
    results.forEach(doc -> System.out.println(doc.getContent()));
}
```

分类标签：RAG检索增强 | 更新日期：2026-05-28

---

## 其他向量存储中的 RRF 实现

**问**：PgVector、Milvus 等存储如何实现 RRF？

**答**：

- **PgVector**：扩展本身不直接提供 RRF，可在应用层分别计算 `vector_score` 与 `ts_rank`，再用 RRF 融合。
- **Milvus 2.4+**：原生支持混合检索与 RRF，通过 `RRFRanker` 指定 `rank_constant`。

**代码示例（PgVector 思路）**：

```sql
-- pgvector 本身不直接支持 RRF，但可在应用层实现
-- 通过 vector_score 和 ts_rank 分别计算分数，再用 RRF 融合
```

**代码示例（Milvus）**：

```python
# Milvus 2.4+ 支持混合检索和 RRF
from pymilvus import AnnSearchRequest, RRFRanker

hybrid_req = AnnSearchRequest(...)
res = collection.hybrid_search(
    reqs=[hybrid_req, ...],
    ranker=RRFRanker(rank_constant=60),
    limit=10
)
```

分类标签：RAG检索增强 | 更新日期：2026-05-28

---

## RRF 与其他融合方法对比

**问**：RRF 与加权求和、Combinational Sum 等融合方式有何区别？

**答**：

| 方法 | 原理 | 优点 | 缺点 |
| :--- | :--- | :--- | :--- |
| **RRF** | 基于排名倒数求和 | 无需归一化，对异常值鲁棒 | 丢失原始分数信息 |
| **加权求和** | α × 向量分 + (1-α) × BM25 分 | 可调节权重 | 需要归一化，调参复杂 |
| **Combinational Sum** | 简单相加排名 | 实现简单 | 未考虑排名位置权重 |

分类标签：RAG检索增强 | 更新日期：2026-05-28

---

## 向量数据库实现跨会话长期记忆

**问**：大规模、需语义检索的跨会话记忆如何用向量库 + RAG 实现？核心接口与读写流程是什么？

**答**：

- **定位**：外部存储型长期记忆，适合大量用户事实、需按语义召回的场景；与工具型 `AutoMemoryTools`（文件 Markdown）互补。
- **核心接口**：`MemoryStore` / `VectorStore`；可用 `MemoryAdvisor` 在对话链中自动注入检索到的记忆片段。
- **写入流程**：将用户相关事实切片为 `Document`，向量化后写入向量库（可带 `userId` 等元数据过滤）。
- **读取流程**：对话前按用户问题做 `similaritySearch`（TopK + 过滤表达式），将命中片段拼入 System/User Prompt。
- **典型存储**：Redis Vector、Chroma、Pinecone、PGVector 等。
- **与短期记忆**：短期 `ChatMemory` 保当轮连贯；长期向量记忆提供跨会话个性化上下文。

**代码示例**：

```java
@Configuration
public class LongTermMemoryConfig {

    @Bean
    public VectorStore vectorStore(EmbeddingModel embeddingModel, RedisVectorStoreProperties properties) {
        return new RedisVectorStore(embeddingModel, properties);
    }

    @Bean
    public MemoryAdvisor memoryAdvisor(VectorStore vectorStore) {
        return new MemoryAdvisor(vectorStore);
    }
}

@Service
public class MemoryService {

    private final VectorStore vectorStore;

    public MemoryService(VectorStore vectorStore) {
        this.vectorStore = vectorStore;
    }

    public void remember(String userId, String fact) {
        Document doc = new Document(fact, Map.of("userId", userId));
        vectorStore.add(List.of(doc));
    }

    public String chatWithMemory(String userId, String query, ChatClient chatClient) {
        List<Document> memories = vectorStore.similaritySearch(
            SearchRequest.query(query)
                .withTopK(5)
                .withFilterExpression("userId == '" + userId + "'"));
        String memoryContext = memories.stream()
            .map(Document::getText)
            .collect(Collectors.joining("\n"));
        String prompt = String.format("已知用户信息：\n%s\n\n用户新问题：%s", memoryContext, query);
        return chatClient.call(prompt);
    }
}
```

分类标签：RAG检索增强 | 更新日期：2026-05-28

---

## Agent 流水线中的并行知识库检索

**问**：Spring AI 智能体操作数据库时，RAG 知识库如何在 Skills/Tools 执行的同时并行参与？子流程与典型存储内容是什么？

**答**：

- **触发时机**：意图识别与路由阶段即可启动，与 Skill 匹配、MCP 工具调用**并行**，不阻塞 `execute_sql` 等 Tool 执行。
- **子流程三步**：
  1. **查询重写**：将用户自然语言转为更适合检索的查询（消歧、补全表名/字段等实体）。
  2. **向量数据库检索**：Embedding 相似度召回相关文档片段。
  3. **上下文增强**：将检索结果整理为可注入 Prompt 的上下文块。
- **典型库内容**（数据库场景）：业务知识说明、**Schema 元数据**、历史查询模板、数据字典条目。
- **结果汇入**：增强后的上下文与 Tool 执行结果（如 `execute_sql` 查询数据集）在**结果整合**阶段一并进入模型上下文。
- **价值**：Tool 提供动态/实时查询结果，RAG 提供静态参考（表结构、字段含义、业务规则），二者互补后生成更准确的 SQL 与解释性回答。

分类标签：RAG检索增强 | 更新日期：2026-05-28


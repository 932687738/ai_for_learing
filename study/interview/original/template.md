Spring AI RAG 多路径检索与监控最佳实践
本文档总结了 Spring AI 框架中构建 RAG（检索增强生成）系统的核心技术点，包括多路径检索策略、查询扩展、向量存储设计及监控埋点。

1. 检索查询对象：为什么使用 Query 而不是直接传字符串？
   java
   Query originalQuery = Query.builder().text(question.trim()).build();
   List<Document> originalDocs = searchKnowledgeDocuments(originalQuery.text(), perPathK);
   作用
   构建一个标准的查询对象，封装用户问题。

为后续检索提供扩展性（如携带元数据、过滤条件、TopK等）。

为什么不直接使用 question.trim()？
直接传字符串	使用 Query 对象
无法携带额外参数	可携带相似度阈值、过滤表达式、用户标识等
接口变更成本高	Query 作为参数，扩展时无需修改方法签名
语义不明确	明确表达这是检索查询
不利于统一日志/监控	可在 Query 中嵌入元数据（如检索类型、时间戳）
最佳实践：

java
// 可扩展的 Query 构建
Query query = Query.builder()
.text(question.trim())
.withTopK(5)
.withSimilarityThreshold(0.7)
.withFilterExpression("tenant_id == '123'")
.build();
2. 多路径检索：三种召回策略的区别
   java
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
核心区别
维度	路径1（原始）	路径2（语义扩展）	路径3（关键词扩展）
输入形式	用户原问题	多个自然语言变体	关键词组合/布尔查询
转换方式	无	LLM 生成	规则/词典/模型扩展
检索原理	语义相似度	多角度语义覆盖	关键词匹配 + 语义
LLM 依赖	无	需要 LLM	可能不需要
计算成本	低（1次检索）	高（K次检索）	中（1次检索）
召回类型	直接相关	表述不同的间接相关文档	含关键词但语义可能偏离
示例
用户问："怎么用 Spring AI 做 RAG？"

路径1 召回："Spring AI RAG 实现步骤"

路径2 召回：通过 LLM 生成 "Spring AI中如何使用检索增强生成"、"基于Spring AI的RAG开发教程" 等，召回不同侧面的文档。

路径3 召回：转换为 "Spring AI RAG 检索 增强 生成 集成"，召回包含这些关键词的文档。

为什么要三路合并？
路径1：保证精准度（Precision）

路径2：提升召回率（Recall），覆盖不同表达

路径3：弥补语义检索可能遗漏的关键词匹配

合并时通常使用 RRF（倒数排名融合）或加权平均。

3. MultiQueryExpander.expand() 的作用
   java
   List<Query> expandedQueries = queryExpander.expand(originalQuery);
   核心功能
   利用大语言模型（LLM）将一个用户查询扩展成多个语义不同但相关的查询变体。

工作流程
接收 originalQuery。

调用配置的 ChatClient，按照提示词模板生成若干个变体。

返回 List<Query>。

配置参数（通过 Builder）
参数	作用
numberOfQueries	生成的变体数量
includeOriginal	是否包含原始查询（用于避免与路径1重复）
示例
用户查询："怎么学 Spring AI"
扩展后可能得到：

"Spring AI 的学习步骤是什么？"

"Spring AI 入门教程有哪些？"

"如何上手 Spring AI 框架？"

价值：显著提高召回率，避免因用户措辞问题而遗漏相关信息。

4. 监控埋点：Micrometer 指标记录
   java
   private static final String RECALL_PATH_HITS = "springai.rag.pgvector.recall.path.hits";

// joined 阶段（合并去重后）
Counter.builder(RECALL_PATH_HITS)
.tag("operation", operation)
.tag("stage", "joined")
.register(meterRegistry)
.increment(joinedCount);

// reranked 阶段（LLM Rerank 后）
Counter.builder(RECALL_PATH_HITS)
.tag("operation", operation)
.tag("stage", "reranked")
.register(meterRegistry)
.increment(rerankedCount);
指标含义
指标名称：springai.rag.pgvector.recall.path.hits

类型：Counter（只增计数器）

标签：

operation：操作类型（如 "user_query_123"）

stage：处理阶段（joined / reranked）

监控价值
问题	通过该指标回答
检索效率	joined 阶段有多少文档进入候选池？
Rerank 效果	reranked 阶段过滤掉了多少文档？
异常检测	若 rerankedCount 经常为 0，说明检索质量差
性能趋势	统计平均 joinedCount 和 rerankedCount 变化
Prometheus 查询示例
promql
# 平均 joined 阶段文档数
avg(springai_rag_pgvector_recall_path_hits_total{stage="joined"})

# Rerank 保留率
sum(springai_rag_pgvector_recall_path_hits_total{stage="reranked"}) /
sum(springai_rag_pgvector_recall_path_hits_total{stage="joined"})
告警规则示例
yaml
- alert: RAGRetrievalEmpty
  expr: |
  increase(springai_rag_pgvector_recall_path_hits_total{stage="reranked"}[5m]) == 0
  annotations:
  summary: "RAG 检索连续5分钟返回空结果"
5. content 与 metadata 的区别及向量搜索中的应用
   java
   Map<String, Object> metadata = new HashMap<>(extraMetadata);
   metadata.put("tenant_id", tenantId);
   metadata.put("user_id", userId);
   metadata.put("created_at", LocalDateTime.now().toString());

Document doc = new Document(content, metadata);
角色对比
特性	content	metadata
数据类型	String	Map<String, Object>
存储内容	文档的主要文本	键值对描述信息
是否参与向量计算	是（被 Embedding 模型转换为向量）	否（不参与相似度计算）
检索时作用	与查询向量计算相似度，找到语义相近的文档	作为过滤器，在相似度计算前后筛选文档
索引方式	向量索引	通常建立标量索引以加速过滤
向量搜索时的协同流程
生成查询向量。

应用元数据过滤（通过 SearchRequest.withFilterExpression(...)）：

预过滤：在向量搜索前先缩小候选集。

后过滤：在向量搜索后再筛选。

在过滤后的文档集中执行向量相似度计算。

返回 TopK 个最相似的文档。

java
// 带 metadata 过滤的检索请求
SearchRequest request = SearchRequest
.query("用户查询的问题")
.withTopK(5)
.withSimilarityThreshold(0.7)
.withFilterExpression("tenant_id == 'tenant123' && user_id == 'user456'");

List<Document> results = vectorStore.similaritySearch(request);
设计优势
安全隔离：通过 tenant_id 等 metadata 强制多租户数据隔离。

精确控制：可限定检索范围（部门、时间、类型等）。

性能提升：先用 metadata 缩小范围，再计算相似度，显著减少计算量并提高结果相关性。

总结
技术点	核心要点
Query 对象	封装检索参数，支持过滤、阈值、元数据，扩展性强
多路径检索	原始语义 + LLM 多查询扩展 + 关键词扩展，提升召回率和鲁棒性
MultiQueryExpander	利用 LLM 生成查询变体，弥补用户措辞差异
Micrometer 监控	记录 joined / reranked 阶段的文档命中数，便于性能分析和告警
content vs metadata	content 用于向量相似度计算，metadata 用于过滤，二者协同实现精准检索与隔离
以上模式已在生产级 RAG 系统中验证，可显著提升检索质量和系统可观测性。
<!-- 最后更新于 2026-05-28 -->

## QuestionAnswerAdvisor 检索结果缓存

**问**：在 Spring AI 生产级 RAG 应用中，QuestionAnswerAdvisor 默认每次请求同步调用向量存储。如何为检索结果引入缓存层，既能缓存相同或相似问题的检索结果，又能避免缓存污染？

**答**：

- **缓存 Key**：归一化查询文本的 MD5，或查询向量的哈希。
- **避免污染**：设置合理 TTL（如 5–30 分钟）；对含「今天」「昨天」等时效性查询动态禁用缓存；使用 `@Cacheable` 的 `condition` 属性。

**代码示例**：

```java
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
```

分类标签：RAG Advisor | 更新日期：2026-05-28

---

## QuestionAnswerAdvisor 工作流程

**问**：QuestionAnswerAdvisor 接收到用户问题后，会执行哪两个主要步骤？将什么内容传递给大模型？

**答**：

1. **Before 阶段**：调用 `VectorStore.similaritySearch` 检索相关文档。
2. **调用大模型前**：将检索到的 `Document.content`（文本片段）拼入 Prompt 作为上下文——传递的是**文本**，不是向量。

分类标签：RAG Advisor | 更新日期：2026-05-28

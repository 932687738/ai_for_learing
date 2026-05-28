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

## ResponseValidationAdvisor 回答质量检测

**问**：如何在 Spring AI Advisor 链中集成回答质量检测？检测维度与实现方式有哪些？

**答**：

**检测维度**：事实准确性、安全性、格式合规、相关性、逻辑一致性、来源可溯。

**实现方式**：

1. **规则校验**：JSON 解析、正则、关键词黑名单等确定性检查。
2. **LLM-as-Judge**：二次调用模型审查首答，错误则纠正或拒绝。
3. **Advisor 集成**：实现 `CallAdvisor`，在 `chain.nextCall()` 之后校验响应，不通过则抛异常或触发重试。

**代码示例（规则校验）**：

```java
public boolean isValidJson(String response) {
    try { new ObjectMapper().readTree(response); return true; }
    catch (Exception e) { return false; }
}
```

**代码示例（LLM-as-Judge 自校正）**：

```java
public String selfCorrect(String originalQuestion, String firstAnswer) {
    return chatClient.prompt()
        .user("Check the following answer for accuracy. If wrong, correct it.\n"
            + "Question: " + originalQuestion + "\nAnswer: " + firstAnswer)
        .call().content();
}
```

**代码示例（CallAdvisor 集成）**：

```java
public class ResponseValidationAdvisor implements CallAdvisor {
    @Override
    public AdvisedResponse adviseCall(AdvisedRequest request, CallAdvisorChain chain) {
        AdvisedResponse response = chain.nextCall(request);
        String content = response.response().getResult().getOutput().getText();
        if (!isValid(content)) {
            throw new RuntimeException("Invalid response");
        }
        return response;
    }

    @Override
    public int getOrder() { return 0; }
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

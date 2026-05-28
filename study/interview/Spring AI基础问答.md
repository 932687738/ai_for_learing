<!-- 最后更新于 2026-05-28 -->

## 检索 Query 对象 vs 直接传字符串

**问**：Spring AI RAG 检索中为什么使用 `Query` 对象而不是直接传 `question.trim()` 字符串？

**答**：

- **Query 作用**：封装用户问题为标准检索对象，为后续扩展 TopK、相似度阈值、过滤表达式、元数据等参数预留空间。
- **对比直接传字符串**：

| 直接传字符串 | 使用 Query 对象 |
| :--- | :--- |
| 无法携带额外参数 | 可携带阈值、过滤、用户标识等 |
| 接口变更成本高 | 扩展时无需修改方法签名 |
| 语义不明确 | 明确表达这是检索查询 |
| 不利于统一日志/监控 | 可嵌入检索类型、时间戳等元数据 |

**代码示例**：

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

分类标签：Spring AI基础 | 更新日期：2026-05-28

---

## ChatClient 与 ChatModel 的区别

**问**：ChatClient 和 ChatModel 有什么区别？

**答**：

- **ChatModel**：底层接口，直接与具体大模型 API 通信，返回 `ChatResponse`。
- **ChatClient**：高层门面，在 ChatModel 之上封装流式输出、Advisor 链、Tool 调用、Prompt 模板等，是业务侧更常用的入口。

**代码示例**：

```java
// 底层 ChatModel
ChatResponse response = chatModel.call(new Prompt("你好"));

// 高层 ChatClient
String answer = chatClient.prompt()
    .user("你好")
    .advisors(new QuestionAnswerAdvisor(vectorStore))
    .call()
    .content();
```

分类标签：Spring AI基础 | 更新日期：2026-05-28

---

## Prompt 与 UserMessage 的关系

**问**：Prompt 和 UserMessage 分别代表什么？关系是什么？

**答**：

- **Prompt**：一次完整调用的提示词容器，可包含 `SystemMessage`、`UserMessage`、`AssistantMessage` 等多种消息。
- **UserMessage**：表示用户输入的单条消息组件。
- **关系**：UserMessage 是 Prompt 的组成部分，Prompt 由多条 Message 组合而成。

**代码示例**：

```java
Prompt prompt = new Prompt(
    List.of(
        new SystemMessage("你是一个Spring技术专家"),
        new UserMessage("RAG中的Advisor是什么？")
    )
);
```

分类标签：Spring AI基础 | 更新日期：2026-05-28

---

## Advisor 的作用与执行位置

**问**：Advisor 接口的作用是什么？它的 around 方法在执行链路中处于什么位置？

**答**：

- **作用**：类似 AOP 切面，在 ChatClient 调用链中包裹模型请求，可在调用前（检索、日志）、调用后（格式化、审计）或异常时介入。
- **位置**：`around` 位于用户请求与最终 ChatModel 调用之间，通过 `AdvisorChain.next()` 将控制传递给下一环。

**代码示例**：

```java
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
```

分类标签：Spring AI基础 | 更新日期：2026-05-28

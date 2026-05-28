<!-- 最后更新于 2026-05-28 -->

## Spring AI Transform 结构化输出

**问**：Spring AI 中 Transform 如何将模型非结构化输出转为 Java 对象？

**答**：

- **作用**：将 LLM 生成的自由文本转换为结构化 Java 对象，充当输出「翻译官」。
- **实现**：ChatClient 结合 `BeanOutputConverter`，通过 `.entity(Class)` 直接映射为 Record 或 POJO。

**代码示例**：

```java
// 定义期望的 Java Record
record ActorsFilms(String actor, List<String> movies) {}

// 使用 ChatClient 发起请求，直接映射为对象
ActorsFilms films = ChatClient.create(chatModel)
    .prompt()
    .user(u -> u.text("为{actor}生成5部电影的作品年表。").param("actor", "汤姆·汉克斯"))
    .call()
    .entity(ActorsFilms.class);

System.out.println(films.actor());  // 输出：汤姆·汉克斯
films.movies().forEach(System.out::println);
```

分类标签：Spring AI基础 | 更新日期：2026-05-28

---

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

## Spring AI Advisor 机制

**问**：Spring AI 中 Advisor 是什么？有哪些内置 Advisor？如何自定义？

**答**：

- **定义**：Advisor 实现 AOP 风格，在 AI 模型调用前后动态插入横切逻辑（日志、重试、缓存等），无需修改业务代码。
- **位置**：`around` 位于用户请求与 ChatModel 调用之间，通过 `AdvisorChain.next()` 传递控制。

**常见内置 Advisor**：

| Advisor | 作用 |
| :--- | :--- |
| LoggerAdvisor | 记录请求/响应日志及耗时 |
| RetryAdvisor | 调用失败时自动重试 |
| CacheAdvisor | 缓存相同请求的响应 |
| RateLimiterAdvisor | 限制调用频率 |
| MessageHistoryAdvisor | 管理多轮对话历史 |
| CircuitBreakerAdvisor | 熔断保护 |

**代码示例（组合使用）**：

```java
ChatClient chatClient = ChatClient.create(chatModel)
    .advisors(
        new LoggerAdvisor(),
        new RetryAdvisor(3),
        new CacheAdvisor(cacheManager)
    )
    .build();

String response = chatClient.prompt("Hello AI")
    .advisors(anotherAdvisor)  // 单次调用可临时增加 Advisor
    .call()
    .content();
```

**代码示例（自定义 Advisor）**：

```java
public class SafeWordAdvisor implements Advisor {
    @Override
    public ChatResponse aroundCall(AdvisorChain chain, ChatRequest request) {
        if (containsSensitiveWords(request.getUserText())) {
            return new ChatResponse("请求包含敏感内容，已拒绝");
        }
        ChatResponse response = chain.next(request);
        return desensitize(response);
    }
}
```

分类标签：Spring AI基础 | 更新日期：2026-05-28

---

## Transformer 与 Advisor 的区别

**问**：Spring AI 中 Transformer 和 Advisor 有何区别？

**答**：

| 维度 | Transformer | Advisor |
| :--- | :--- | :--- |
| 作用阶段 | ETL 管道（调用前数据准备） | 模型调用时的请求/响应拦截 |
| 主要对象 | Document 文档块 | Prompt / ChatResponse |
| 典型场景 | 文本切分、格式统一、元数据丰富 | 日志、重试、缓存、限流、对话历史 |
| 是否直接调用模型 | 否 | 是（包裹模型调用过程） |

**小结**：Transformer 是数据「精炼厂」，Advisor 是 AI 调用的横切拦截器。

分类标签：Spring AI基础 | 更新日期：2026-05-28

---

## Spring AI 记忆类型对比与选型

**问**：Spring AI 中短期记忆、工具型长期记忆、向量库型长期记忆有何区别？如何选型？

**答**：

| 类型 | 生命周期 | 核心技术 | 典型存储 | 代码接口 |
| :--- | :--- | :--- | :--- | :--- |
| **短期记忆** | 单次会话 | `ChatMemory` + 滑动窗口 | Redis / 关系库 | `ChatMemoryRepository` |
| **长期记忆（工具型）** | 永久 / 跨会话 | `AutoMemoryTools` | 本地 Markdown 文件 | `MemoryStore` |
| **长期记忆（外部库型）** | 永久 / 跨会话 | 向量数据库 + RAG | Redis、Chroma、PGVector | `VectorStore` / `MemoryAdvisor` |

**选型建议**：

- 仅需会话内上下文 → 短期记忆（滑动窗口 + 可选 JDBC/Redis 持久化）
- 需记住用户偏好、少量事实、零代码文件存储 → `AutoMemoryTools`
- 大规模、语义检索型记忆 → 向量库 + RAG 检索注入
- **混合方案**：短期 `ChatMemory` 保持对话流畅，长期记忆通过检索或 Tool 注入个性化信息

分类标签：Spring AI基础 | 更新日期：2026-05-28

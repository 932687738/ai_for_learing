<!-- 模块：Spring AI 核心组件 | 最后更新于 2026-05-28 -->

# Spring AI 核心组件

> ChatClient、Prompt、Advisor、Transform 等框架基础抽象。

## 目录

- [Spring AI Transform 结构化输出](#spring-ai-transform-结构化输出)
- [ChatClient 与 ChatModel 的区别](#chatclient-与-chatmodel-的区别)
- [Prompt 与 UserMessage 的关系](#prompt-与-usermessage-的关系)
- [Spring AI Advisor 机制](#spring-ai-advisor-机制)
- [Transformer 与 Advisor 的区别](#transformer-与-advisor-的区别)
- [PromptTemplate 与提示词设计原则](#prompttemplate-与提示词设计原则)
- [ChatClient 文本补全模式](#chatclient-文本补全模式)

---
## Spring AI Transform 结构化输出

> **模块**：Spring AI 核心组件 | **标签**：Spring AI基础 | **更新**：2026-05-28

### 核心概念

作用：将 LLM 生成的自由文本转换为结构化 Java 对象，充当输出「翻译官」。

### 要点

- **作用**：将 LLM 生成的自由文本转换为结构化 Java 对象，充当输出「翻译官」。
- **实现**：ChatClient 结合 `BeanOutputConverter`，通过 `.entity(Class)` 直接映射为 Record 或 POJO。

### 代码示例

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

### 面试常问

**问**：Spring AI 中 Transform 如何将模型非结构化输出转为 Java 对象？

**答**：作用**：将 LLM 生成的自由文本转换为结构化 Java 对象，充当输出「翻译官」。；实现**：ChatClient 结合 `BeanOutputConverter`，通过 `.entity(Class)` 直接映射为 Record 或 POJO。。

### 关联知识点

- [RAG Advisor](RAG Advisor.md)
- [文档 ETL 与分块](文档ETL与分块.md)

---
## ChatClient 与 ChatModel 的区别

> **模块**：Spring AI 核心组件 | **标签**：Spring AI基础 | **更新**：2026-05-28

### 核心概念

ChatModel：底层接口，直接与具体大模型 API 通信，返回 `ChatResponse`。

### 要点

- **ChatModel**：底层接口，直接与具体大模型 API 通信，返回 `ChatResponse`。
- **ChatClient**：高层门面，在 ChatModel 之上封装流式输出、Advisor 链、Tool 调用、Prompt 模板等，是业务侧更常用的入口。

### 代码示例

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

### 面试常问

**问**：ChatClient 和 ChatModel 有什么区别？

**答**：ChatModel**：底层接口，直接与具体大模型 API 通信，返回 `ChatResponse`。；ChatClient**：高层门面，在 ChatModel 之上封装流式输出、Advisor 链、Tool 调用、Prompt 模板等，是业务侧更常用的入口。。

### 关联知识点

- [RAG Advisor](RAG Advisor.md)
- [文档 ETL 与分块](文档ETL与分块.md)

---
## Prompt 与 UserMessage 的关系

> **模块**：Spring AI 核心组件 | **标签**：Spring AI基础 | **更新**：2026-05-28

### 核心概念

Prompt：一次完整调用的提示词容器，可包含 `SystemMessage`、`UserMessage`、`AssistantMessage` 等多种消息。

### 要点

- **Prompt**：一次完整调用的提示词容器，可包含 `SystemMessage`、`UserMessage`、`AssistantMessage` 等多种消息。
- **UserMessage**：表示用户输入的单条消息组件。
- **关系**：UserMessage 是 Prompt 的组成部分，Prompt 由多条 Message 组合而成。

### 代码示例

```java
Prompt prompt = new Prompt(
    List.of(
        new SystemMessage("你是一个Spring技术专家"),
        new UserMessage("RAG中的Advisor是什么？")
    )
);
```

### 面试常问

**问**：Prompt 和 UserMessage 分别代表什么？关系是什么？

**答**：Prompt**：一次完整调用的提示词容器，可包含 `SystemMessage`、`UserMessage`、`AssistantMessage` 等多种消息。；UserMessage**：表示用户输入的单条消息组件。；关系**：UserMessage 是 Prompt 的组成部分，Prompt 由多条 Message 组合而成。。

### 关联知识点

- [RAG Advisor](RAG Advisor.md)
- [文档 ETL 与分块](文档ETL与分块.md)

---
## Spring AI Advisor 机制

> **模块**：Spring AI 核心组件 | **标签**：Spring AI基础 | **更新**：2026-05-28

### 核心概念

定义：Advisor 实现 AOP 风格，在 AI 模型调用前后动态插入横切逻辑（日志、重试、缓存等），无需修改业务代码。

### 要点

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

### 代码示例

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

// 组合使用 Advisor
ChatClient client = ChatClient.builder(chatModel)
    .addAdvisors(new MessageChatMemoryAdvisor(), new QuestionAnswerAdvisor())
    .build();
```

### 面试常问

**问**：Spring AI 中 Advisor 是什么？有哪些内置 Advisor？如何自定义？

**答**：定义**：Advisor 实现 AOP 风格，在 AI 模型调用前后动态插入横切逻辑（日志、重试、缓存等），无需修改业务代码。；位置**：`around` 位于用户请求与 ChatModel 调用之间，通过 `AdvisorChain.next()` 传递控制。。

### 关联知识点

- [RAG Advisor](RAG Advisor.md)
- [文档 ETL 与分块](文档ETL与分块.md)

---
## Transformer 与 Advisor 的区别

> **模块**：Spring AI 核心组件 | **标签**：Spring AI基础 | **更新**：2026-05-28

### 核心概念

Spring AI 中 Transformer 和 Advisor 有何区别？

### 要点

| 维度 | Transformer | Advisor |
| :--- | :--- | :--- |
| 作用阶段 | ETL 管道（调用前数据准备） | 模型调用时的请求/响应拦截 |
| 主要对象 | Document 文档块 | Prompt / ChatResponse |
| 典型场景 | 文本切分、格式统一、元数据丰富 | 日志、重试、缓存、限流、对话历史 |
| 是否直接调用模型 | 否 | 是（包裹模型调用过程） |

**小结**：Transformer 是数据「精炼厂」，Advisor 是 AI 调用的横切拦截器。

### 面试常问

**问**：Spring AI 中 Transformer 和 Advisor 有何区别？

**答**：Transformer :--- ETL 管道（调用前数据准备） Document 文档块 文本切分、格式统一、元数据丰富 否 **小结**：Transformer 是数据「精炼厂」，Advisor 是 AI 调用的横切拦截器。

### 关联知识点

- [RAG Advisor](RAG Advisor.md)
- [文档 ETL 与分块](文档ETL与分块.md)

---
## PromptTemplate 与提示词设计原则

> **模块**：Spring AI 核心组件 | **标签**：Spring AI基础 | **更新**：2026-05-28

### 核心概念

清晰明确：任务目标与约束无歧义。

### 要点

**设计原则**：

- **清晰明确**：任务目标与约束无歧义。
- **角色与背景**：声明模型身份与领域上下文。
- **分隔符**：用 `# Role`、`# Task` 等区块划分结构，降低指令混淆。
- **输出格式**：显式指定 JSON、列表等结构化输出要求。

**PromptTemplate 用法**：占位符 `{lang}`、`{text}` 等由 Map 注入，生成 `Prompt` 后交给 ChatClient。

### 代码示例

```text
# Role
你是一位资深Python面试官

# Task
提出3个关于装饰器的问题

# Constraints
由浅入深，每个问题附带预期答案

# Output Format
JSON: [{"question": "", "expected_answer": ""}]
```

```java
PromptTemplate template = new PromptTemplate("Translate to {lang}: {text}");
Prompt prompt = template.create(Map.of("lang", "French", "text", "Hello"));
String response = chatClient.prompt(prompt).call().content();
```

### 面试常问

**问**：Spring AI 中如何设计高质量提示词？PromptTemplate 如何使用？

**答**：清晰明确**：任务目标与约束无歧义。；角色与背景**：声明模型身份与领域上下文。；分隔符**：用 `# Role`、`# Task` 等区块划分结构，降低指令混淆。；输出格式**：显式指定 JSON、列表等结构化输出要求。。

### 关联知识点

- [RAG Advisor](RAG Advisor.md)
- [文档 ETL 与分块](文档ETL与分块.md)

---
## ChatClient 文本补全模式

> **模块**：Spring AI 核心组件 | **标签**：Spring AI基础 | **更新**：2026-05-28

### 核心概念

Spring AI ChatClient 支持哪些文本补全调用方式？如何配置流式输出与生成参数？

### 要点

| 模式 | 说明 | 典型 API |
| :--- | :--- | :--- |
| **极简同步** | 单轮 prompt → 字符串 | `.prompt().user(prompt).call().content()` |
| **结构化输出** | 直接映射 Java Record/POJO | `.call().entity(Champion.class)` |
| **流式输出** | SSE 逐 token 推送 | `.stream().content()` 返回 `Flux<String>` |
| **参数调优** | 控制 temperature、maxTokens 等 | `.options(ChatOptions.builder()...)` |

### 代码示例

```java
@Service
public class CompletionService {
    private final ChatClient chatClient;

    public CompletionService(ChatClient.Builder builder) {
        this.chatClient = builder.build();
    }

    public String complete(String prompt) {
        return chatClient.prompt().user(prompt).call().content();
    }
}

record Champion(String first, String last, List<Integer> years) {}

Champion champion = chatClient.prompt()
    .user("Current chess world champion and years")
    .call()
    .entity(Champion.class);

@GetMapping(value = "/stream", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
public Flux<String> stream(@RequestParam String prompt) {
    return chatClient.prompt().user(prompt).stream().content();
}

ChatResponse response = chatClient.prompt()
    .user(prompt)
    .options(ChatOptions.builder()
        .temperature(0.7)
        .maxTokens(500)
        .build())
    .call();
```

### 面试常问

**问**：Spring AI ChatClient 支持哪些文本补全调用方式？如何配置流式输出与生成参数？

**答**：说明 :--- 单轮 prompt → 字符串 直接映射 Java Record/POJO SSE 逐 token 推送 控制 temperature、maxTokens 等

### 关联知识点

- [RAG Advisor](RAG Advisor.md)
- [文档 ETL 与分块](文档ETL与分块.md)

---
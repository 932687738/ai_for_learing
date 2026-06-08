<!-- 模块：Spring AI 核心组件 | 最后更新于 2026-06-06（Few-shot 与重试）） -->

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
- [Spring AI 多模态输入与动态模型切换](#spring-ai-多模态输入与动态模型切换)
- [多语言 Prompt 与 Tool 回调](#多语言-prompt-与-tool-回调)

- [Few-shot 少样本学习与 Prompt 关系](#few-shot-少样本学习与-prompt-关系)
- [Few-shot 示例质量评估与代码生成设计](#few-shot-示例质量评估与代码生成设计)
- [Spring AI 重试与智能化自修正](#spring-ai-重试与智能化自修正)
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

> **模块**：Spring AI 核心组件 | **标签**：Spring AI基础 | **更新**：2026-05-29

### 核心概念

Advisor 实现 AOP 风格，在 AI 模型调用前后动态插入横切逻辑（日志、重试、缓存等），无需修改业务代码；多个 Advisor 按 `Ordered` 组成责任链——**前置升序、后置逆序**执行。

### 要点

- **定义**：Advisor 实现 AOP 风格，在 AI 模型调用前后动态插入横切逻辑（日志、重试、缓存等），无需修改业务代码。
- **位置**：`around` 位于用户请求与 ChatModel 调用之间，通过 `AdvisorChain.next()` 传递控制。
- **与 Hook / ToolCallback 层级**：Advisor 处于 ChatClient 与 ChatModel 间的**通信拦截层**；Agent 场景下外层还有 Hook（生命周期），内层 ToolCallback 由 ToolCallAdvisor 调度——详见 [ToolCallback、Advisor 与 Hook 区别及执行顺序](Agent架构与协同.md)。

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

**答**：Advisor 是包裹 ChatModel 调用的 AOP 拦截器，多个实例按 Order 组成链（前置升序、后置逆序），可自定义 `CallAdvisor`/`RequestResponseAdvisor` 实现日志、校验等横切逻辑；与 Hook（Agent 生命周期）、ToolCallback（工具执行）分属不同嵌套层。

### 关联知识点

- [ToolCallback、Advisor 与 Hook 区别及执行顺序](Agent架构与协同.md)
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
## Spring AI 多模态输入与动态模型切换

> **模块**：Spring AI 核心组件 | **标签**：多模态, ChatClient, 模型路由 | **更新**：2026-05-28

### 核心概念

Spring AI 通过 `UserMessage.media` 与 `ChatClient` 的 `.media()` 支持图像等多模态输入；运行时可通过多 Bean 配置、参数化选项或路由策略在多个 LLM 客户端间动态切换。

### 要点

- **多模态载体**：`UserMessage` 接受 `Media` 列表（MIME + Resource）；`ChatClient` 推荐用 `.user(u -> u.text(...).media(...))` 链式构建。
- **模型支持差异**：Gemini 支持文本/PDF/图像/音视频；OpenAI/Claude/Ollama 以文本+图像为主，具体以 Provider 文档为准。
- **动态切换思路**：注册多个 `ChatClient` Bean（如 primary / cheap），运行时按请求参数、任务复杂度或接口职责选择实例。
- **四种常见模式**：参数化临时改模型选项；Map 缓存已配置客户端；基于 prompt 长度/复杂度的自动路由；接口级硬编码绑定专用模型。

### 代码示例

```java
var imageResource = new ClassPathResource("/multimodal.test.png");
var userMessage = new UserMessage(
    "Explain what do you see in this picture?",
    new Media(MimeTypeUtils.IMAGE_PNG, imageResource)
);
ChatResponse response = chatModel.call(new Prompt(userMessage));

String reply = ChatClient.create(chatModel).prompt()
    .user(u -> u.text("Explain what do you see on this picture?")
        .media(MimeTypeUtils.IMAGE_PNG, new ClassPathResource("/multimodal.test.png")))
    .call()
    .content();
```

```java
@Configuration
public class ChatClientConfig {
    @Bean
    @Primary
    public ChatClient primaryChatClient(OpenAiChatModel chatModel) {
        return ChatClient.create(chatModel);
    }

    @Bean
    public ChatClient cheapChatClient(OpenAiChatModel chatModel) {
        return ChatClient.builder(chatModel)
            .defaultOptions(OpenAiChatOptions.builder()
                .withModel("gpt-3.5-turbo")
                .withTemperature(0.3).build())
            .build();
    }
}

@RestController
public class ChatController {
    private final Map<String, ChatClient> clientMap;

    public ChatController(@Qualifier("primaryChatClient") ChatClient primary,
                          @Qualifier("cheapChatClient") ChatClient cheap) {
        this.clientMap = Map.of("primary", primary, "cheap", cheap);
    }

    @GetMapping("/chat")
    public String chat(@RequestParam(defaultValue = "primary") String model,
                       @RequestParam String prompt) {
        ChatClient selected = clientMap.getOrDefault(model, clientMap.get("primary"));
        return selected.prompt().user(prompt).call().content();
    }

    @GetMapping("/smart-chat")
    public String smartChat(@RequestParam String prompt) {
        ChatClient client = prompt.length() > 50
            ? clientMap.get("primary") : clientMap.get("cheap");
        return client.prompt().user(prompt).call().content();
    }
}
```

### 面试常问

**问**：Spring AI 如何实现多模态输入？如何在运行时动态切换不同 LLM？

**答**：多模态通过 `UserMessage`/`ChatClient` 的 `media` 传入图像等资源；动态切换可配置多个 `ChatClient` Bean，按请求参数、任务复杂度或接口职责从 Map 选取，或在单次调用中通过 `options()` 覆盖模型名与温度。

### 关联知识点

- [上传文件 PDF/Excel/图片 处理原理](文档ETL与分块.md)
- [Agent 架构与协同](Agent架构与协同.md)

---
## 多语言 Prompt 与 Tool 回调

> **模块**：Spring AI 核心组件 | **标签**：i18n, PromptTemplate, Tool | **更新**：2026-05-28

### 核心概念

多语言场景可结合 Spring `MessageSource` 管理提示词模板，并依赖模型自身多语言能力；Tool 的 `description` 可写双语说明，便于 LLM 跨语言触发回调。

### 要点

- **Prompt 国际化**：`messages_zh_CN.properties` 等存放 system/user 模板，`MessageSource.getMessage(key, args, default, locale)` 按 Locale 取词。
- **热更新**：`ReloadableResourceBundleMessageSource` 设置 `cacheSeconds` 可在不重启时刷新提示词。
- **语言检测路由**：可选 Apache OpenNLP 等检测入参语言后分发不同模型或模板。
- **Tool 多语言**：`@Tool(description = "...")` 内写中英文描述，模型理解后即可用任意语言提问并触发同一工具。

### 代码示例

```properties
# messages_zh_CN.properties
system.prompt=你是一位乐于助人的中文助手。
user.greeting=你好！有什么可以帮助你的？
```

```java
@Autowired
private MessageSource messageSource;

String greeting = messageSource.getMessage("user.greeting", null, "Hello!", locale);

@Bean
public MessageSource messageSource() {
    ReloadableResourceBundleMessageSource source = new ReloadableResourceBundleMessageSource();
    source.setBasename("classpath:i18n/messages");
    source.setCacheSeconds(10);
    return source;
}
```

```java
@Component
public class WeatherService {
    @Tool(description = """
        Get the current weather in a given city.
        获取指定城市当前的天气情况。
        """)
    public String getWeather(String city) {
        return "晴朗，25°C";
    }
}

public String chatWithTool(String prompt) {
    return ChatClient.create(chatModel)
        .prompt(prompt)
        .tools(weatherService)
        .call()
        .content();
}
```

### 面试常问

**问**：Spring AI 如何支持多语言入参与 Tool 回调？

**答**：提示词用 Spring MessageSource + i18n 资源文件按 Locale 加载，可配合 Reloadable 实现热更新；Tool 描述写双语，ChatClient 注册 tools 后模型可用任意语言提问并触发回调；也可先做语言检测再路由模板或模型。

### 关联知识点

- [PromptTemplate 与提示词设计原则](#prompttemplate-与提示词设计原则)
- [Agent 架构与协同](Agent架构与协同.md)

---

## Few-shot 少样本学习与 Prompt 关系

> **模块**：Spring AI 核心组件 | **标签**：Few-shot, Prompt, In-Context Learning | **更新**：2026-06-06

### 核心概念

Few-shot 是 Prompt Engineering 中在提示内放 2–10 个输入-输出示例、让模型模仿任务模式的技术；Prompt 是包含指令、角色、上下文与示例的完整输入。

### 要点

| 类型 | 示例数 | 是否更新参数 |
| :--- | :--- | :--- |
| Zero-shot | 0 | 否 |
| One-shot | 1 | 否 |
| Few-shot | 2–10 | 否 |
| Fine-tuning | 数百+ | 是 |

- **有效原因**：格式对齐、任务模式暗示、减少歧义。
- **与 RAG**：RAG 供事实，Few-shot 定格式与推理模式，常组合使用。
- **Agent 技巧**：动态检索相似示例、CoT 示例、自我校正示例（含修正过程）。
- **正例 vs 负例**：以正确示例为主（80%+）；高风险场景可附「错误+纠正」对比，勿只用负例。

### 面试常问

**问**：Few-shot 和 Prompt 有什么区别？

**答**：Prompt 是发给模型的全部文本；Few-shot 是 Prompt 中嵌入多个示例的那部分，属于上下文学习，不更新模型权重。

### 关联知识点

- [PromptTemplate 与提示词设计原则](#prompttemplate-与提示词设计原则)
- [Fine-tuning 微调模型选型](其他.md)

---
## Few-shot 示例质量评估与代码生成设计

> **模块**：Spring AI 核心组件 | **标签**：Few-shot, 代码生成, 评估 | **更新**：2026-06-06

### 核心概念

高质量 Few-shot 需相关性、正确性、多样性、清晰度与顺序稳定性；代码生成场景还需完整签名、边缘案例与复杂度递增。

### 要点

**评估维度**：相关性、正确性、清晰度、代表性、简洁性、顺序鲁棒性。

**量化方法**：留一法测示例重要性、打乱顺序测一致性、交叉验证准确率。

**代码 Few-shot 设计**：
- 展示完整函数签名与类型
- 含空输入、异常、边界条件
- 命名与风格一致
- 复杂度从简单到递归/嵌套递增
- 单元测试驱动评估生成代码通过率

### 代码示例

```python
def sum_of_even_squares(numbers: List[int]) -> int:
    return sum(x * x for x in numbers if x % 2 == 0)
```

### 面试常问

**问**：如何评估 Few-shot 质量？代码生成如何设计示例？

**答**：从相关性、正确性、多样性等维度评估，并用留一法/顺序打乱实验；代码场景展示完整签名、边界处理、风格一致与递增复杂度，用单元测试验证生成结果。

### 关联知识点

- [Few-shot 少样本学习与 Prompt 关系](#few-shot-少样本学习与-prompt-关系)
- [Text2SQL 核心流程与高级技术](Agent架构与协同.md)

---
## Spring AI 重试与智能化自修正

> **模块**：Spring AI 核心组件 | **标签**：Retry, StructuredOutputValidationAdvisor, @Retryable | **更新**：2026-06-06

### 核心概念

Spring AI 提供三层容错：配置式 API 重试、StructuredOutputValidationAdvisor 内容自修正、Spring Retry 对任意 Bean 方法精细化重试。

### 要点

| 方案 | 机制 | 场景 |
| :--- | :--- | :--- |
| 声明式重试 | `spring.ai.retry.*` | 网络抖动、429 限流 |
| 递归顾问 | `StructuredOutputValidationAdvisor` | 输出格式/逻辑错误，错误喂回 LLM 自修正 |
| Spring Retry | `@Retryable` + `@Recover` | 外部 API（如 Dify）精细控制 |

### 代码示例

```properties
spring.ai.retry.max-attempts=3
spring.ai.retry.backoff.initial-interval=2s
spring.ai.retry.backoff.multiplier=2
spring.ai.retry.on-client-errors=false
```

```java
var validationAdvisor = StructuredOutputValidationAdvisor.builder()
    .outputType(MyResponseType.class)
    .maxRepeatAttempts(3)
    .build();
```

### 面试常问

**问**：Spring AI 如何实现错误重试与自修正？

**答**：application.properties 配声明式重试处理瞬时故障；StructuredOutputValidationAdvisor 校验结构化输出并将错误反馈给模型循环修正；@Retryable 对 Service 层外部调用做指数退避与 @Recover 兜底。

### 关联知识点

- [Spring AI Advisor 机制](#spring-ai-advisor-机制)
- [Agent 分级错误处理矩阵](Agent架构与协同.md)

---


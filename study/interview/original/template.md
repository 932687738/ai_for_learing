# Spring AI 多模态、工作流、记忆与向量数据库分片问答总结

## 目录
1. [Spring AI 多模态实现与动态模型切换](#1-spring-ai-多模态实现与动态模型切换)
2. [AI 处理上传文件（PDF/Excel/图片）的原理](#2-ai-处理上传文件pdfexcel图片的原理)
3. [Spring AI 根据提示词调用多个接口并分析组装](#3-spring-ai-根据提示词调用多个接口并分析组装)
4. [Spring AI 工作流实现](#4-spring-ai-工作流实现)
5. [Spring AI 多语言入参和回调](#5-spring-ai-多语言入参和回调)
6. [Spring AI 自动解析入参 vs 自定义分词的区别](#6-spring-ai-自动解析入参-vs-自定义分词的区别)
7. [Spring AI 中实现 Re-Ranker](#7-spring-ai-中实现-re-ranker)
8. [Spring AI 中长期记忆、短期记忆和历史记忆的载体](#8-spring-ai-中长期记忆短期记忆和历史记忆的载体)
9. [向量数据库中推荐的分片大小](#9-向量数据库中推荐的分片大小)

---

## 1. Spring AI 多模态实现与动态模型切换

### 多模态实现
Spring AI 通过 `Message API` 和 `ChatClient` 支持多模态。核心在于 `UserMessage` 的 `media` 字段，接受 `Media` 对象列表。

#### 使用 `ChatModel`
```java
var imageResource = new ClassPathResource("/multimodal.test.png");
var userMessage = new UserMessage(
    "Explain what do you see in this picture?",
    new Media(MimeTypeUtils.IMAGE_PNG, imageResource)
);
ChatResponse response = chatModel.call(new Prompt(userMessage));
String reply = response.getResult().getOutput().getContent();
使用 ChatClient（推荐）
java
String response = ChatClient.create(chatModel).prompt()
    .user(u -> u.text("Explain what do you see on this picture?")
        .media(MimeTypeUtils.IMAGE_PNG, new ClassPathResource("/multimodal.test.png")))
    .call()
    .content();
多模态支持模型
模型提供商	支持的多模态输入
Google Vertex AI Gemini	文本, PDF, 图像, 音频, 视频
OpenAI	输入: 文本, 图像, 音频；输出: 文本, 音频
Anthropic Claude	文本, PDF, 图像
Ollama	文本, 图像
动态切换模型
核心思想：配置多个 LLM 客户端 Bean，运行时根据条件动态选择。

配置多 Bean
java
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
四种切换模式
java
@RestController
public class ChatController {
    private final Map<String, ChatClient> clientMap;
    private final ChatClient primaryChatClient;

    public ChatController(@Qualifier("primaryChatClient") ChatClient primary,
                          @Qualifier("cheapChatClient") ChatClient cheap) {
        this.primaryChatClient = primary;
        this.clientMap = Map.of("primary", primary, "cheap", cheap);
    }

    @GetMapping("/chat")
    public String chat(@RequestParam(defaultValue = "primary") String model, 
                       @RequestParam String prompt) {
        // 模式一：参数化动态决策（临时创建）
        if ("cheap".equalsIgnoreCase(model)) {
            return primaryChatClient.prompt().user(prompt)
                    .options(OpenAiChatOptions.builder().withModel("gpt-3.5-turbo").build())
                    .call().content();
        }
        // 模式二：从 Map 获取已配置的实例
        ChatClient selectedClient = clientMap.getOrDefault(model, primaryChatClient);
        return selectedClient.prompt().user(prompt).call().content();
    }
    
    // 模式三：基于任务复杂度自动路由
    @GetMapping("/smart-chat")
    public String smartChat(@RequestParam String prompt) {
        ChatClient client = prompt.length() > 50 ? clientMap.get("primary") : clientMap.get("cheap");
        return client.prompt().user(prompt).call().content();
    }
    
    // 模式四：接口级硬编码绑定
    @GetMapping("/translate")
    public String translate(@RequestParam String text) {
        return clientMap.get("cheap").prompt().user("Translate to English: " + text).call().content();
    }
}
2. AI 处理上传文件（PDF/Excel/图片）的原理
文档类文件：通过 ETL 流水线（提取→转换→加载），利用 DocumentReader、DocumentTransformer、DocumentWriter 处理。

图像类文件：多模态模型使用“视觉编码器+LLM”直接理解。

混合处理包含图片的 PDF
混合解析：提取文本 + 单独提取图片。

并行处理：文本向量化，图片用多模态模型分析。

内容融合：在语义层面整合结果。

3. Spring AI 根据提示词调用多个接口并分析组装
核心是 Tool Calling (Function Calling)。

定义工具
java
@Service
public class BusinessTools {
    @Tool(description = "根据用户ID查询用户订单列表")
    public List<Order> queryOrders(String userId) {
        return orderRepository.findByUserId(userId);
    }

    @Tool(description = "查询指定城市的天气信息")
    public String getWeather(String city) {
        return weatherService.getWeatherByCity(city);
    }
}
调用工具
java
@Autowired private ChatClient chatClient;
@Autowired private BusinessTools businessTools;

public String processUserRequest(String userPrompt) {
    return chatClient.prompt()
            .user(userPrompt)
            .tools(businessTools)
            .call()
            .content();
}
工作流模式选择指南
场景	推荐模式
简单信息查询	工具调用
明确步骤的数据处理	链式工作流
不确定意图的请求分发	路由工作流
耗时并行分析与聚合	并行化工作流
复杂多级任务分解	编排器-工作者
大型系统多领域协作	多智能体路由
4. Spring AI 工作流实现
轻量级工作流代码示例
链式工作流
java
public class ChainWorkflow {
    private final ChatClient chatClient;
    private final String[] systemPrompts;

    public String chain(String userInput) {
        String response = userInput;
        for (String prompt : systemPrompts) {
            String input = String.format("{%s}\n {%s}", prompt, response);
            response = chatClient.prompt(input).call().content();
        }
        return response;
    }
}
并行化工作流
java
List<String> parallelResponse = new ParallelizationWorkflow(chatClient)
    .parallel(
        "Analyze how market changes will impact this stakeholder group.",
        List.of("Customers: ...", "Employees: ...", "Investors: ...", "Suppliers: ..."),
        4
    );
路由工作流
java
RoutingWorkflow workflow = new RoutingWorkflow(chatClient);
Map<String, String> routes = Map.of(
    "billing", "You are a billing specialist...",
    "technical", "You are a technical support engineer...",
    "general", "You are a customer service representative..."
);
String response = workflow.route(input, routes);
编排器-工作者
java
public class TravelOrchestratorWorkflow {
    private final ChatClient chatClient;

    public TravelPlan createPlan(TravelRequest request) {
        // 1. 编排器动态分解任务
        String taskList = chatClient.prompt()
            .user("Analyze this travel request and break it down into a list of independent subtasks: " + request.toString())
            .call().content();
        List<String> tasks = parseTasks(taskList);

        // 2. 并行执行
        List<String> results = tasks.parallelStream()
            .map(task -> chatClient.prompt().user(task).call().content())
            .toList();

        // 3. 合成
        String finalPlan = chatClient.prompt()
            .user("Synthesize these travel insights into a comprehensive plan: " + String.join("\n", results))
            .call().content();
        return parsePlan(finalPlan);
    }
}
多智能体协同
Spring AI Alibaba 提供开箱即用的多智能体模式，基于 Graph Core 管理状态。

顺序执行示例
java
ReactAgent writerAgent = ReactAgent.builder()
    .name("writer_agent").model(chatModel)
    .instruction("You are a writer. Write about: {input}.")
    .outputKey("article")
    .build();

ReactAgent reviewerAgent = ReactAgent.builder()
    .name("reviewer_agent").model(chatModel)
    .instruction("Review this article: {article}")
    .outputKey("reviewed_article")
    .build();

SequentialAgent blogAgent = SequentialAgent.builder()
    .name("blog_agent")
    .subAgents(List.of(writerAgent, reviewerAgent))
    .build();

Optional<OverAllState> result = blogAgent.invoke("Write about Spring AI");
5. Spring AI 多语言入参和回调
多语言输入处理
语言自动识别与路由：可使用 Apache OpenNLP 检测语言后分发给不同模型。

依赖 AI 模型自身多语言能力。

国际化 i18n 管理提示词
properties
# messages_zh_CN.properties
system.prompt=你是一位乐于助人的中文助手。
user.greeting=你好！有什么可以帮助你的？
yaml
spring:
  messages:
    basename: i18n/messages
    encoding: UTF-8
java
@Autowired
private MessageSource messageSource;
String greeting = messageSource.getMessage("user.greeting", null, "Hello!", locale);
热更新提示词
java
@Bean
public MessageSource messageSource() {
    ReloadableResourceBundleMessageSource source = new ReloadableResourceBundleMessageSource();
    source.setBasename("classpath:i18n/messages");
    source.setCacheSeconds(10); // 10秒刷新
    return source;
}
多语言回调（Tool Calling）
java
@Component
public class WeatherService {
    @Tool(description = """
        Get the current weather in a given city. 
        获取指定城市当前的天气情况。
        """)
    public String getWeather(String city) {
        return "晴朗， 25°C";
    }
}
java
@Autowired private WeatherService weatherService;
public String chatWithTool(String prompt) {
    return ChatClient.create(chatModel)
        .prompt(prompt)
        .tools(weatherService)
        .call()
        .content();
}
6. Spring AI 自动解析入参 vs 自定义分词的区别
维度	自动解析（结构化输出）	自定义分词（文本切分）
目的	将非结构化文本转为程序对象	将长文本切分成语义块
作用对象	AI 生成的响应（Output）	原始文档（Input）
时机	生成响应之后	发送请求之前
解决的问题	响应格式不统一	文本超出模型上下文窗口限制
自动解析示例
java
Student student = ChatClient.create(chatModel).prompt()
    .user("Generate a student record")
    .call()
    .entity(Student.class);
文本切分器选择
TokenTextSplitter：按 Token 硬性切分

SentenceSplitter：按句子语义边界

RecursiveCharacterTextSplitter：用分隔符递归切分

7. Spring AI 中实现 Re-Ranker
开箱即用方案（RetrievalRerankAdvisor）
java
public RerankController(ChatClient.Builder builder, VectorStore vectorStore, RerankModel rerankModel) {
    this.chatClient = builder
        .defaultAdvisors(new RetrievalRerankAdvisor(vectorStore, rerankModel))
        .build();
}
手动集成（DocumentPostProcessor）
java
@Component
public class MyRerankProcessor implements DocumentPostProcessor {
    @Override
    public List<Document> process(List<Document> documents) {
        // 调用重排序 API 对文档评分并排序
        return documents;
    }
}
8. Spring AI 中长期记忆、短期记忆和历史记忆的载体
记忆类型	核心载体	存储	生命周期	特性
短期记忆	ChatMemory / MessageWindowChatMemory	内存（可持久化）	单次会话	滑动窗口策略
长期记忆	VectorStore / AutoMemoryTools	向量数据库/文件系统	跨会话	用户画像、偏好，常结合 RAG
历史记录	ChatMemoryRepository	数据库（JDBC/Redis）	永久	完整审计日志
9. 向量数据库中推荐的分片大小
数据库	推荐单分片大小	建议
Milvus	512MB / 1GB / 2GB	使用官方 Sizing Tool 根据内存计算
Qdrant	< 1000万条向量	单分片模式上限约 1000 万条
腾讯云	< 200-300万条向量	通用场景 100-200 万，DISK_FLAT 可放宽至 300 万
Pinecone	约 100万-500万条向量	p1 Pod 约 100 万条，s1 Pod 约 500 万条
黄金法则：确保索引完全加载进内存，分片尽量大一些。

Milvus Sizing Tool 使用方法
访问 milvus.io/tools/sizing

输入向量总数、维度、索引类型、分段大小等参数

观察不同分段大小对内存的影响，选择最佳配置
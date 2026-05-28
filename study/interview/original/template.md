# Spring AI 知识库记忆存储：短期、长期与永久记忆

在 Spring AI 应用中，记忆管理可按照生命周期划分为**短期记忆**（单次会话上下文）和**长期/永久记忆**（跨会话保留用户偏好、事实等）。本文介绍各自的核心技术、存储方式及代码示例。

## 1. 短期记忆

短期记忆用于维护当前对话的上下文连贯性，会话结束后通常不再保留。

### 核心技术：`ChatMemory` 与 `ChatMemoryRepository`

Spring AI 通过 `ChatMemory` 接口管理对话历史，应用需将历史消息作为提示词的一部分发送给模型。

- **常用策略**：滑动窗口（保留最近 N 条消息）
- **默认实现**：`MessageWindowChatMemory`
- **存储实现**：
    - `InMemoryChatMemoryRepository`（开发/测试，重启丢失）
    - `JdbcChatMemoryRepository`（关系数据库，持久化）
    - `RedisSaver` / 自定义实现（Redis 等键值存储）

### 代码示例：配置基于数据库的短期记忆

```java
@Configuration
public class ChatMemoryConfig {

    @Bean
    public ChatMemoryRepository chatMemoryRepository(JdbcTemplate jdbcTemplate) {
        return new JdbcChatMemoryRepository(jdbcTemplate);
    }

    @Bean
    public ChatMemory chatMemory(ChatMemoryRepository repository) {
        // 滑动窗口，最多保留 20 条消息
        return MessageWindowChatMemory.builder()
                .chatMemoryRepository(repository)
                .maxMessages(20)
                .build();
    }
}
使用短期记忆
java
@Service
public class ConversationService {

    private final ChatMemory chatMemory;
    private final ChatClient chatClient;

    public ConversationService(ChatMemory chatMemory, ChatClient chatClient) {
        this.chatMemory = chatMemory;
        this.chatClient = chatClient;
    }

    public String talk(String conversationId, String userMessage) {
        // 获取历史消息
        List<Message> history = chatMemory.get(conversationId, 20);

        // 添加用户新消息
        history.add(new UserMessage(userMessage));

        // 调用模型
        ChatResponse response = chatClient.call(new ChatRequest(history));
        String assistantMessage = response.getResult().getOutput();

        // 保存助手回复到短期记忆
        history.add(new AssistantMessage(assistantMessage));
        chatMemory.add(conversationId, history);

        return assistantMessage;
    }
}
2. 长期/永久记忆
长期记忆用于跨会话保留信息，例如用户偏好、事实陈述、项目决策等。

2.1 工具驱动型：AutoMemoryTools
Spring AI 提供的 AutoMemoryTools 允许 AI 自主读写 Markdown 文件来记录持久化信息。

代码示例
java
@Configuration
public class MemoryToolsConfig {

    @Bean
    public MemoryStore memoryStore() {
        // 使用文件系统存储，路径可配置
        return new FileSystemMemoryStore(Path.of("./memories"));
    }

    @Bean
    public AutoMemoryTools autoMemoryTools(MemoryStore memoryStore) {
        return AutoMemoryTools.builder()
                .memoryStore(memoryStore)
                .build();
    }
}
然后在创建 ChatClient 时注册该工具：

java
@Bean
public ChatClient chatClient(ChatModel model, AutoMemoryTools memoryTools) {
    return ChatClient.builder(model)
            .tools(memoryTools)
            .build();
}
用户无需显式操作，AI 会根据对话内容自动调用 save_to_memory 或 recall_from_memory 工具来管理长期记忆。

2.2 外部存储型：向量数据库 + RAG
对于大量记忆或需要语义检索的场景，通常使用向量数据库（如 Redis、Chroma、Pinecone）与 RAG（检索增强生成） 结合。

核心接口：MemoryStore / VectorStore

工作流程：应用程序将用户相关事实切片、向量化后存入向量库；对话时检索最相似的“记忆片段”注入提示词。

代码示例（以 Redis Vector Store 为例）
java
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
写入长期记忆：

java
@Service
public class MemoryService {

    private final VectorStore vectorStore;
    private final EmbeddingModel embeddingModel;

    public void remember(String userId, String fact) {
        Document doc = new Document(fact, Map.of("userId", userId));
        vectorStore.add(List.of(doc));
    }
}
读取长期记忆（在对话前注入）：

java
public String chatWithMemory(String userId, String query) {
    // 检索与该用户相关的 topK 条记忆
    List<Document> memories = vectorStore.similaritySearch(SearchRequest.query(query)
            .withTopK(5)
            .withFilterExpression("userId == '" + userId + "'"));

    // 构建提示词，加入记忆内容
    String memoryContext = memories.stream()
            .map(Document::getText)
            .collect(Collectors.joining("\n"));

    String prompt = String.format("已知用户信息：\n%s\n\n用户新问题：%s", memoryContext, query);
    return chatClient.call(prompt);
}
3. 三种记忆对比总结
类型	生命周期	核心技术	典型存储	代码接口
短期记忆	单次会话	ChatMemory + 滑动窗口	Redis / 关系库	ChatMemoryRepository
长期记忆（工具型）	永久 / 跨会话	AutoMemoryTools	本地文件	MemoryStore
长期记忆（外部库型）	永久 / 跨会话	向量数据库 + RAG	Redis, Chroma, PGVector	VectorStore / MemoryStore
4. 选择建议
仅需要会话内上下文 → 短期记忆（滑动窗口 + 数据库）

需要记住用户偏好、少量事实 → AutoMemoryTools（零代码存储）

大规模、语义检索型记忆 → 向量数据库 + RAG

混合使用：短期记忆保持对话流畅，长期记忆通过检索注入个性化信息。
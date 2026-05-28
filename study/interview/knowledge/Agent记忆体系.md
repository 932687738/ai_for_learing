<!-- 模块：Agent 记忆体系 | 最后更新于 2026-05-28（记忆载体表增强） -->

# Agent 记忆体系

> ChatMemory 短期记忆与 AutoMemoryTools 长期记忆。

## 目录

- [多轮对话记忆管理（短期记忆）](#多轮对话记忆管理短期记忆)
- [AutoMemoryTools 工具驱动型长期记忆](#automemorytools-工具驱动型长期记忆)
- [Spring AI 记忆类型对比与选型](#spring-ai-记忆类型对比与选型)

---
## 多轮对话记忆管理（短期记忆）

> **模块**：Agent 记忆体系 | **标签**：Agent与对话 | **更新**：2026-05-28

### 核心概念

定位：短期记忆维护**单次会话**上下文连贯性；默认会话结束后不保留，若使用 JDBC/Redis 等 Repository 则可持久化会话历史。

### 要点

- **定位**：短期记忆维护**单次会话**上下文连贯性；默认会话结束后不保留，若使用 JDBC/Redis 等 Repository 则可持久化会话历史。
- **核心组件**：`ChatMemory` 管理对话历史；`ChatMemoryRepository` 负责存储；应用将历史消息作为 Prompt 一部分发送给模型。
- **常用策略**：滑动窗口，`MessageWindowChatMemory` 保留最近 N 条消息。
- **存储实现**：
  - `InMemoryChatMemoryRepository`：开发/测试，重启丢失
  - `JdbcChatMemoryRepository`：关系数据库持久化
  - Redis 或自定义实现：键值存储
- **Advisor 集成**：`MessageChatMemoryAdvisor` 自动注入/保存历史，业务侧无需手写 get/add 循环。
- **ToolContext**：在 Tool 调用间传递会话态，避免全量历史塞入 Prompt；超窗时可压缩历史提取要点。
- **与长期记忆分工**：短期保对话流畅；跨会话用户偏好/事实见 AutoMemoryTools 或向量库 + RAG 专题。

### 代码示例

```java
@Configuration
public class ChatMemoryConfig {

    @Bean
    public ChatMemoryRepository chatMemoryRepository(JdbcTemplate jdbcTemplate) {
        return new JdbcChatMemoryRepository(jdbcTemplate);
    }

    @Bean
    public ChatMemory chatMemory(ChatMemoryRepository repository) {
        return MessageWindowChatMemory.builder()
                .chatMemoryRepository(repository)
                .maxMessages(20)
                .build();
    }
}

@Service
public class ConversationService {

    private final ChatMemory chatMemory;
    private final ChatClient chatClient;

    public ConversationService(ChatMemory chatMemory, ChatClient chatClient) {
        this.chatMemory = chatMemory;
        this.chatClient = chatClient;
    }

    public String talk(String conversationId, String userMessage) {
        List<Message> history = chatMemory.get(conversationId, 20);
        history.add(new UserMessage(userMessage));
        ChatResponse response = chatClient.call(new ChatRequest(history));
        String assistantMessage = response.getResult().getOutput();
        history.add(new AssistantMessage(assistantMessage));
        chatMemory.add(conversationId, history);
        return assistantMessage;
    }
}

@Bean
public ChatClient chatClient(ChatClient.Builder builder, ChatMemory chatMemory) {
    return builder
        .defaultAdvisors(new MessageChatMemoryAdvisor(chatMemory))
        .build();
}
```

### 面试常问

**问**：Spring AI 短期记忆如何实现？如何在多轮对话中保持上下文并避免记忆膨胀？

**答**：定位：短期记忆维护单次会话**上下文连贯性；默认会话结束后不保留，若使用 JDBC/Redis 等 Repository 则可持久化会话历史。；核心组件**：`ChatMemory` 管理对话历史；`ChatMemoryRepository` 负责存储；应用将历史消息作为 Prompt 一部分发送给模型。；常用策略**：滑动窗口，`MessageWindowChatMemory` 保留最近 N 条消息。；存储实现**：。

### 关联知识点

- [RAG 长期记忆](RAG长期记忆.md)
- [Agent 架构与协同](Agent架构与协同.md)

---
## AutoMemoryTools 工具驱动型长期记忆

> **模块**：Agent 记忆体系 | **标签**：Agent与对话 | **更新**：2026-05-28

### 核心概念

定位：长期/永久记忆用于跨会话保留用户偏好、事实陈述、项目决策等；生命周期超出单次会话。

### 要点

- **定位**：长期/永久记忆用于跨会话保留用户偏好、事实陈述、项目决策等；生命周期超出单次会话。
- **机制**：`AutoMemoryTools` 允许模型自主读写 Markdown 文件（`save_to_memory` / `recall_from_memory`），底层由 `MemoryStore`（如 `FileSystemMemoryStore`）持久化。
- **使用方式**：将 `AutoMemoryTools` 注册为 ChatClient 的 Tool，用户无需显式调用，模型根据对话内容自动存取。
- **适用场景**：需要记住少量偏好/事实、希望零代码文件存储的场景；大规模语义检索见向量库 + RAG。

### 代码示例

```java
@Configuration
public class MemoryToolsConfig {

    @Bean
    public MemoryStore memoryStore() {
        return new FileSystemMemoryStore(Path.of("./memories"));
    }

    @Bean
    public AutoMemoryTools autoMemoryTools(MemoryStore memoryStore) {
        return AutoMemoryTools.builder()
                .memoryStore(memoryStore)
                .build();
    }
}

@Bean
public ChatClient chatClient(ChatModel model, AutoMemoryTools memoryTools) {
    return ChatClient.builder(model)
            .tools(memoryTools)
            .build();
}
```

### 面试常问

**问**：Spring AI 中如何用 AutoMemoryTools 实现跨会话长期记忆？与短期 ChatMemory 有何不同？

**答**：定位**：长期/永久记忆用于跨会话保留用户偏好、事实陈述、项目决策等；生命周期超出单次会话。；机制**：`AutoMemoryTools` 允许模型自主读写 Markdown 文件（`save_to_memory` / `recall_from_memory`），底层由 `MemoryStore`（如 `FileSystemMemoryStore`）持久化。；使用方式**：将 `AutoMemoryTools` 注册为 ChatClient 的 Tool，用户无需显式调用，模型根据对话内容自动存取。；适用场景**：需要记住少量偏好/事实、希望零代码文件存储的场景；大规模语义检索见向量库 + RAG。。

### 关联知识点

- [RAG 长期记忆](RAG长期记忆.md)
- [Agent 架构与协同](Agent架构与协同.md)

---
## Spring AI 记忆类型对比与选型

> **模块**：Agent 记忆体系 | **标签**：Spring AI基础 | **更新**：2026-05-28

### 核心概念

Spring AI 记忆按生命周期分为短期（会话内）、长期（跨会话）与历史记录（永久审计）；载体分别为 `ChatMemory`、`VectorStore`/`AutoMemoryTools` 与 `ChatMemoryRepository`。

### 要点

| 记忆类型 | 核心载体 | 存储 | 生命周期 | 特性 |
| :--- | :--- | :--- | :--- | :--- |
| **短期记忆** | `ChatMemory` / `MessageWindowChatMemory` | 内存（可 JDBC/Redis 持久化） | 单次会话 | 滑动窗口，保对话连贯 |
| **长期记忆** | `VectorStore` / `AutoMemoryTools` | 向量库 / 文件系统 | 跨会话 | 用户画像、偏好，常结合 RAG |
| **历史记录** | `ChatMemoryRepository` | 数据库（JDBC/Redis） | 永久 | 完整对话审计日志 |

**选型建议**

- 仅需会话内上下文 → 短期记忆（滑动窗口 + 可选 JDBC/Redis 持久化）
- 需记住用户偏好、少量事实、零代码文件存储 → `AutoMemoryTools`
- 大规模、语义检索型记忆 → 向量库 + RAG 检索注入
- 需合规审计、全量历史回溯 → `ChatMemoryRepository` 永久存储
- **混合方案**：短期 `ChatMemory` 保持对话流畅，长期记忆通过检索或 Tool 注入个性化信息

### 面试常问

**问**：Spring AI 短期、长期与历史记忆分别用什么载体存储？

**答**：短期用 ChatMemory/MessageWindowChatMemory 维护会话窗口；长期用 VectorStore 或 AutoMemoryTools 跨会话保留偏好与事实；历史记录用 ChatMemoryRepository 写入 JDBC/Redis 做永久审计，三者可组合使用。

### 关联知识点

- [RAG 长期记忆](RAG长期记忆.md)
- [多轮对话记忆管理（短期记忆）](#多轮对话记忆管理短期记忆)

---
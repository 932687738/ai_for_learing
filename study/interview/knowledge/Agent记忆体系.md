<!-- 模块：Agent 记忆体系 | 最后更新于 2026-05-28（MemorySaver HITL 续聊） -->

# Agent 记忆体系

> ChatMemory 短期记忆与 AutoMemoryTools 长期记忆。

## 目录

- [多轮对话记忆管理（短期记忆）](#多轮对话记忆管理短期记忆)
- [AutoMemoryTools 工具驱动型长期记忆](#automemorytools-工具驱动型长期记忆)
- [Spring AI 记忆类型对比与选型](#spring-ai-记忆类型对比与选型)
- [MemorySaver 检查点与 HITL resume 续聊](#memorysaver-检查点与-hitl-resume-续聊)

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
## MemorySaver 检查点与 HITL resume 续聊

> **模块**：Agent 记忆体系 | **标签**：MemorySaver, checkpoint, threadId | **更新**：2026-05-28

### 核心概念

`ReactAgent` 的 **MemorySaver** 负责按 `threadId` 持久化图状态（含 `messages` checkpoint），保证 HITL 中断后 resume 能加载同一对话上下文。Demo 层 `interruptionByThread` 仅暂存 HTTP 层的 `InterruptionMetadata`，与框架 checkpoint 职责分离。

### 要点

**同一 Agent 如何续聊**

- 每次调用都是**同一个** Spring Bean `ReactAgent`（应用启动时 `@Bean` 创建，非请求时）。
- resume 必须使用**相同** `threadId`。
- resume 输入为 **`""` 空串**，不追加新 `UserMessage`；上下文从 `MemorySaver` 检查点加载。

**AppendStrategy 与空串 resume**

- `messages` 键使用 **AppendStrategy**（合并，非 Replace）。
- 空串 `""` → `convertToMessages` 不生成 UserMessage → Append 时 **messages 不变**。
- 非空字符串 → **追加**到 checkpoint 尾部，**不覆盖**。
- Resume 语义是「从中断点续跑 ReAct」，非空 UserMessage 会让 LLM 看到额外用户指令，与 HITL feedback 语义冲突。

**两种存储对比**

| 存储 | 位置 | 作用 |
| :--- | :--- | :--- |
| `MemorySaver` | 框架 | **对话连续性**：同 `threadId` 恢复 messages |
| `interruptionByThread` | Demo `ConcurrentHashMap` | **HTTP 层**暂存 `InterruptionMetadata`，供 resume 构造 feedback |

生产环境应将 `interruptionByThread` 外置（Redis/DB），否则多实例或重启后无法 resume。

**Bean 注入要点**

| 参数 | 来源 |
| :--- | :--- |
| `ChatModel chatModel` | `spring-ai-starter-model-openai` 自动配置 |
| `List<ToolCallback> humanFeedbackToolCallbacks` | 同配置类 `@Bean` |
| `MemorySaver alibabaGraphHumanFeedbackMemorySaver` | 同配置类具名 `@Bean`（项目内多个 MemorySaver，靠**参数名**消歧） |

`AlibabaGraphHumanFeedbackToolDemo` 通过 `@Qualifier(HUMAN_FEEDBACK_AGENT_BEAN_NAME)` 注入 `ReactAgent`（项目内多个 ReactAgent，必须 Qualifier）。

### 代码示例

```java
// resume：空串 + threadId + HUMAN_FEEDBACK_METADATA_KEY
humanFeedbackAgent.invokeAndGetOutput("", resumeConfig);
```

### 面试常问

**问**：HITL resume 时为什么传空串而不是追加 UserMessage？

**答**：messages 使用 AppendStrategy，空串不生成 UserMessage，checkpoint 保持中断点状态；审批结果走 `HUMAN_FEEDBACK_METADATA_KEY` 由 Hook afterModel 消费，追加 UserMessage 会干扰 ReAct 续跑语义。

**问**：MemorySaver 与 Demo 的 interruptionByThread 分别存什么？

**答**：MemorySaver 存框架级对话 checkpoint（messages 等），保证同 threadId 上下文连续；interruptionByThread 仅存 HTTP 层 InterruptionMetadata 供构造人工 feedback，生产需外置避免多实例丢失。

### 关联知识点

- [Human-in-the-Loop 工具审批（ReactAgent + HumanInTheLoopHook）](Agent工作流模式.md)
- [多轮对话记忆管理（短期记忆）](#多轮对话记忆管理短期记忆)

---
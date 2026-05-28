<!-- 模块：RAG 长期记忆 | 最后更新于 2026-05-28 -->

# RAG 长期记忆

> 向量库跨会话记忆与 MemoryAdvisor 注入。

## 目录

- [向量数据库实现跨会话长期记忆](#向量数据库实现跨会话长期记忆)

---
## 向量数据库实现跨会话长期记忆

> **模块**：RAG 长期记忆 | **标签**：RAG检索增强 | **更新**：2026-05-28

### 核心概念

定位：外部存储型长期记忆，适合大量用户事实、需按语义召回的场景；与工具型 `AutoMemoryTools`（文件 Markdown）互补。

### 要点

- **定位**：外部存储型长期记忆，适合大量用户事实、需按语义召回的场景；与工具型 `AutoMemoryTools`（文件 Markdown）互补。
- **核心接口**：`MemoryStore` / `VectorStore`；可用 `MemoryAdvisor` 在对话链中自动注入检索到的记忆片段。
- **写入流程**：将用户相关事实切片为 `Document`，向量化后写入向量库（可带 `userId` 等元数据过滤）。
- **读取流程**：对话前按用户问题做 `similaritySearch`（TopK + 过滤表达式），将命中片段拼入 System/User Prompt。
- **典型存储**：Redis Vector、Chroma、Pinecone、PGVector 等。
- **与短期记忆**：短期 `ChatMemory` 保当轮连贯；长期向量记忆提供跨会话个性化上下文。

### 代码示例

```java
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

@Service
public class MemoryService {

    private final VectorStore vectorStore;

    public MemoryService(VectorStore vectorStore) {
        this.vectorStore = vectorStore;
    }

    public void remember(String userId, String fact) {
        Document doc = new Document(fact, Map.of("userId", userId));
        vectorStore.add(List.of(doc));
    }

    public String chatWithMemory(String userId, String query, ChatClient chatClient) {
        List<Document> memories = vectorStore.similaritySearch(
            SearchRequest.query(query)
                .withTopK(5)
                .withFilterExpression("userId == '" + userId + "'"));
        String memoryContext = memories.stream()
            .map(Document::getText)
            .collect(Collectors.joining("\n"));
        String prompt = String.format("已知用户信息：\n%s\n\n用户新问题：%s", memoryContext, query);
        return chatClient.call(prompt);
    }
}
```

### 面试常问

**问**：大规模、需语义检索的跨会话记忆如何用向量库 + RAG 实现？核心接口与读写流程是什么？

**答**：定位**：外部存储型长期记忆，适合大量用户事实、需按语义召回的场景；与工具型 `AutoMemoryTools`（文件 Markdown）互补。；核心接口**：`MemoryStore` / `VectorStore`；可用 `MemoryAdvisor` 在对话链中自动注入检索到的记忆片段。；写入流程**：将用户相关事实切片为 `Document`，向量化后写入向量库（可带 `userId` 等元数据过滤）。；读取流程**：对话前按用户问题做 `similaritySearch`（TopK + 过滤表达式），将命中片段拼入 System/User Prompt。。

### 关联知识点

- [Agent 记忆体系](Agent记忆体系.md)
- [Spring AI 核心组件](Spring AI核心组件.md)

---
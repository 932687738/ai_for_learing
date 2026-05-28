<!-- 最后更新于 2026-05-28 -->

## Agent 与 RAG 协同 @Tool 动态加载

**问**：如何让 Agent 动态决定是否调用 RAG 检索？请给出使用 @Tool 注解并动态加载工具的设计。

**答**：

- 将 RAG 检索封装为 `@Tool` 方法（含 name、description），返回拼接后的 Document 文本。
- 通过 `KnowledgeToolRegistry` 收集 Spring 容器中所有 `@Tool` Bean。
- `ChatClient.defaultTools()` 注入后，由 LLM 根据工具描述自主决定是否调用知识库。

**代码示例**：

```java
@Component
public class ProductDocumentTool {
    @Tool(name = "query_product_docs", 
         description = "查询产品功能、配置、API使用方法的官方文档知识库。")
    public String queryProductDocs(@ToolParam(description = "用户关于产品的具体问题") String query) {
        List<Document> docs = vectorStore.similaritySearch(SearchRequest.query(query).withTopK(3));
        return docs.stream().map(Document::getContent).collect(Collectors.joining("\n---\n"));
    }
}

@Service
public class KnowledgeToolRegistry {
    @Autowired
    private List<Object> allTools;
    private Map<String, Object> toolMap = new ConcurrentHashMap<>();
    
    @PostConstruct
    public void init() {
        for (Object tool : allTools) {
            // 通过反射获取 @Tool 注解的方法名注册
            toolMap.put(tool.getClass().getSimpleName(), tool);
        }
    }
    
    public Object[] getAllToolInstances() {
        return toolMap.values().toArray();
    }
}

// 配置 ChatClient
@Bean
public ChatClient agentChatClient(ChatClient.Builder builder) {
    return builder
        .defaultSystem("你是一个智能助手，优先使用知识库工具回答问题。")
        .defaultTools(toolRegistry.getAllToolInstances())
        .build();
}
```

分类标签：Agent与对话 | 更新日期：2026-05-28

---

## 多轮对话记忆管理

**问**：如何在多轮对话中让 Agent 记住上下文，并避免记忆膨胀？请说明 ChatMemory 与 ToolContext 的配合。

**答**：

- **短期记忆**：`MessageWindowChatMemory` 保留最近 N 条，配合 `MessageChatMemoryAdvisor`；超窗时压缩历史提取要点。
- **长期记忆**：将会话摘要或关键事实写入 ES/PgVector。
- **ToolContext**：在 Tool 调用间传递会话态，避免全量历史塞入 Prompt。

**代码示例**：

```java
@Bean
public ChatMemory chatMemory() {
    return new MessageWindowChatMemory(10); // 保留最近10条消息
}

@Bean
public ChatClient chatClient(ChatClient.Builder builder, ChatMemory chatMemory) {
    return builder
        .defaultAdvisors(new MessageChatMemoryAdvisor(chatMemory))
        .build();
}
```

分类标签：Agent与对话 | 更新日期：2026-05-28

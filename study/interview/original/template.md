# Spring Boot + Spring AI 构建智能体完全指南

本文档整合了从零开始搭建一个生产级智能体（Agent）所需的核心知识，包括：基础环境与必备条件、如何集成 Skills/MCP/Plugins 扩展能力，以及 Multi-Agent 多智能体协作的详细设计与实现。

## 一、搭建智能体的五个必备条件

### 1. 基础环境

- **JDK 17+**（Spring AI 3.x 要求）
- **Spring Boot 3.2.x+**
- **Maven / Gradle**

### 2. AI 服务商 API Key

| 提供商       | 推荐理由                         | 接入方式                   |
| ------------ | -------------------------------- | -------------------------- |
| 阿里云百炼   | 国内合规，深度集成               | spring-ai-alibaba-starter  |
| OpenAI       | 模型强，生态最完善               | spring-ai-starter-model-openai |
| DeepSeek     | 兼容 OpenAI，性价比高，国内可用  | 同上（修改 base-url）      |
| 本地 Ollama  | 私有化部署，零延迟               | spring-ai-starter-model-ollama |

配置示例（`application.yml`）：
```yaml
spring:
  ai:
    openai:
      api-key: ${OPENAI_API_KEY}
      base-url: ${OPENAI_BASE_URL:https://api.openai.com}
      chat:
        options:
          model: gpt-4o
3. 核心 Maven 依赖
xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>3.2.5</version>
</parent>

<properties>
    <spring-ai.version>1.0.0-M3</spring-ai.version>
</properties>

<dependencies>
    <!-- Spring AI 核心 BOM -->
    <dependency>
        <groupId>org.springframework.ai</groupId>
        <artifactId>spring-ai-bom</artifactId>
        <version>${spring-ai.version}</version>
        <type>pom</type>
        <scope>import</scope>
    </dependency>
    <!-- OpenAI 接入 -->
    <dependency>
        <groupId>org.springframework.ai</groupId>
        <artifactId>spring-ai-openai-spring-boot-starter</artifactId>
    </dependency>
    <!-- MCP 客户端（可选） -->
    <dependency>
        <groupId>org.springframework.ai</groupId>
        <artifactId>spring-ai-mcp-client-spring-boot-starter</artifactId>
    </dependency>
</dependencies>
4. 智能体核心能力组件
4.1 工具（Tools）—— @Tool 注解
java
@Component
public class WeatherService {

    @Tool(description = "根据城市名称查询当前天气")
    public String getWeather(String city) {
        // 调用真实 API
        return city + " 当前晴，25°C";
    }
}
4.2 记忆（Memory）
java
@Configuration
public class MemoryConfig {
    @Bean
    public ChatMemory chatMemory() {
        return new InMemoryChatMemory();  // 或 RedisChatMemory, JdbcChatMemory
    }
}
4.3 声明智能体 Bean
java
@Configuration
public class AgentConfig {

    @Bean
    public ChatClient chatClient(ChatModel chatModel,
                                 List<ToolCallback> toolCallbacks) {
        return ChatClient.builder(chatModel)
                .defaultTools(toolCallbacks.toArray(new ToolCallback[0]))
                .build();
    }
}
5. 运行时接口与监控
java
@RestController
public class AgentController {

    private final ChatClient chatClient;

    public AgentController(ChatClient chatClient) {
        this.chatClient = chatClient;
    }

    @PostMapping("/chat")
    public String chat(@RequestBody String userMessage) {
        return chatClient.prompt()
                .user(userMessage)
                .call()
                .content();
    }
}
二、集成 Skills / MCP / Plugins 能力
核心概念对比
概念	作用	类比
MCP	统一协议，连接外部工具（文件系统、数据库、第三方 API）	AI 世界的 USB-C 口
Skill	封装多步骤工作流，按需加载，避免上下文臃肿	工作流说明书
Plugin	具体的功能单元（通常用 @Tool 实现）	可插拔的功能模块
1. 集成 MCP 客户端（接入外部 MCP Server）
步骤一：添加依赖（见前文）

步骤二：配置 MCP Server 描述文件 src/main/resources/mcp-server.json5

json5
{
  mcpServers: {
    "baidu-map": {
      command: "npx",
      args: ["-y", "@baidumap/mcp-server-baidu-map"],
      env: { BAIDU_MAP_API_KEY: "your-api-key" }
    },
    "filesystem": {
      command: "npx",
      args: ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"]
    }
  }
}
步骤三：启用 MCP 客户端配置 application.yml

yaml
spring:
  ai:
    mcp:
      client:
        enabled: true
        stdio:
          servers-configuration: classpath:/mcp-server.json5
步骤四：注入 MCP 提供的工具

java
@Configuration
public class McpConfig {
    @Bean
    public ChatClient chatClient(ChatModel chatModel,
                                 ToolCallbackProvider mcpToolProvider) {
        return ChatClient.builder(chatModel)
                .defaultTools(mcpToolProvider)
                .build();
    }
}
2. 实现 Skills（技能工作流）
Skill 目录结构示例

text
src/main/resources/skills/
└── generate-report/
    ├── SKILL.md
    ├── references/
    │   └── template.md
    └── scripts/
        └── fetch_data.py
SKILL.md 内容

markdown
---
name: generate-report
description: 根据 Jira 任务记录自动生成周报
---

# 执行步骤
1. 调用工具 `get_jira_tasks` 获取本周任务。
2. 按“已完成/进行中/计划中”分类。
3. 参考 `references/template.md` 格式生成周报。
加载 Skills 并注册到 Agent

java
SkillRegistry skillRegistry = ClasspathSkillRegistry.builder()
        .skillPath("classpath:/skills")
        .build();

SkillsAgentHook skillsHook = SkillsAgentHook.builder()
        .skillRegistry(skillRegistry)
        .build();

ReactAgent agent = ReactAgent.builder()
        .name("assistant")
        .model(chatModel)
        .toolCallbacks(mcpToolProvider)   // MCP 工具
        .hooks(List.of(skillsHook))       // Skill 钩子
        .build();
工作流：用户请求“生成周报” → Agent 发现 generate-report Skill → 加载 SKILL.md 指令 → 调用 get_jira_tasks（MCP 工具）→ 生成最终内容。

三、Multi-Agent 多智能体协作详解
核心价值
能力解耦：不同 Agent 各司其职（代码专家、文案专家、质检员）。

认知减负：每个 Agent 只关注自己的上下文，决策更精准。

质量保证：引入评审 Agent 对执行结果进行校验。

Spring AI Alibaba 原生支持的协作模式
3.1 工具调用模式（集中式指挥）
java
// 定义专业 Agent 作为工具
@Component
public class CodeAgent {
    @Tool(description = "编写 Java 代码")
    public String writeCode(String requirement) {
        return "public class Hello { public static void main(String[] args) { System.out.println(\"Hello\"); } }";
    }
}

@Component
public class DocAgent {
    @Tool(description = "编写技术文档")
    public String writeDoc(String code) {
        return "## 使用说明\n该代码用于...";
    }
}

// 主管 Agent 自动注册上述工具
@Configuration
public class MultiAgentConfig {
    @Bean
    public ChatClient supervisor(ChatModel model,
                                 CodeAgent codeAgent,
                                 DocAgent docAgent) {
        return ChatClient.builder(model)
                .defaultTools(
                    ToolCallbacks.from(codeAgent),
                    ToolCallbacks.from(docAgent)
                )
                .build();
    }
}
用户请求：“帮我写一个打印 Hello 的 Java 程序，并生成说明文档”
→ 主管 Agent 依次调用 CodeAgent → DocAgent。

3.2 交接模式（Handoffs，去中心化）
java
// 订单 Agent
@Agent(name = "orderAgent", description = "处理订单相关问题")
public class OrderAgent {
    @Handoff(target = PaymentAgent.class, description = "转交支付问题")
    public String handleOrder(String question) {
        return "您的订单 #12345 正在配送中。";
    }
}

// 支付 Agent
@Agent(name = "paymentAgent", description = "处理支付相关问题")
public class PaymentAgent {
    public String handlePayment(String question) {
        return "您的支付已完成，交易号：ABC123。";
    }
}
用户问：“我的订单什么时候到？” → orderAgent 回答。
用户接着问：“那这笔交易的支付记录呢？” → orderAgent 主动交接给 paymentAgent，用户无感知切换。

更高级的编排：Graph 工作流
java
GraphAgent graph = GraphAgent.builder()
        .name("risk-control")
        .nodes(
            Node.of("data_collect", collectorAgent),
            Node.of("rule_engine", ruleEngineAgent),
            Node.of("human_review", humanReviewAgent)
        )
        .edges(
            Edge.from("data_collect").to("rule_engine"),
            Edge.from("rule_engine").conditional(
                result -> result.isPass() ? "end" : "human_review"
            )
        )
        .build();
上下文工程：占位符实现信息传递
java
@Agent(instruction = """
        请根据用户需求选择合适的专家。
        当前已收集的信息：{collected_info}
        最后决策结果：{last_decision}
        """)
public class SupervisorAgent {
    // 占位符会在运行时被自动填充
}
Multi-Agent 适用场景选择
场景	推荐模式	说明
自动周报生成	工具调用（顺序）	数据采集 → 分析 → 撰写
智能客服（跨领域）	交接模式	订单 → 支付 → 售后 无缝切换
视频生成流程	Graph 顺序编排	脚本 → 生成 → 字幕 → 发布
风控审核	Graph 条件分支	自动规则通过→放行；否则人工
并行信息聚合	并行节点	同时查询多个新闻源
四、完整可运行示例代码
以下是一个集成了 OpenAI + MCP 文件系统 + Skill 周报生成 的 Spring Boot 主类。

java
@SpringBootApplication
public class AgentApplication {

    public static void main(String[] args) {
        SpringApplication.run(AgentApplication.class, args);
    }

    @Bean
    public CommandLineRunner demo(ChatClient chatClient) {
        return args -> {
            String response = chatClient.prompt()
                    .user("帮我生成这周的周报")
                    .call()
                    .content();
            System.out.println(response);
        };
    }
}
配套 application.yml：

yaml
spring:
  ai:
    openai:
      api-key: ${OPENAI_API_KEY}
    mcp:
      client:
        enabled: true
        stdio:
          servers-configuration: classpath:/mcp-server.json5
至此，你已经拥有从基础环境、工具集成、MCP/Skills 到 Multi-Agent 协作的完整知识体系。根据实际业务场景，自由组合上述能力即可构建生产级智能体应用。
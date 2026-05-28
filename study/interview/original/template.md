# MCP 全面解析：原理、区别与 Spring AI 实战
## 一、MCP原理
...
## 二、MCP与Skill、Agent、Rule的区别
...
## 三、使用 Spring AI 实现 MCP
### 3.1 整体架构与依赖
### 3.2 MCP Server端
### 3.3 MCP Client端
...
## 四、一个服务既是Client又是Server
...
注意保留所有代码块（xml, yaml, java）。最后可能加上一个结语。

需要注意：之前回答中的代码示例使用了Spring AI MCP Starter，但版本未明确指定。可保留原样。我也可以稍微调整一下格式，确保正确。

现在，我将生成最终的Markdown内容。

markdown
# MCP 全面解析：原理、区别与 Spring AI 实战

## 一、MCP（Model Context Protocol）原理

### 1. 定位与设计哲学
MCP 是由 Anthropic 提出的开放标准协议，为大型语言模型（LLM）与外部工具、数据源之间建立统一的通信中间层。  
它常被类比为 **AI 领域的“USB‑C 接口”**，通过标准化的协议与数据格式，实现模型与外部系统安全、高效的双向连接。

三大核心设计：
- **能力解耦**：工具调用从提示词中剥离，避免硬编码导致的上下文膨胀。
- **动态发现**：运行时按需加载外部能力，无需预先定义所有工具指令。
- **安全隔离**：通过进程级隔离与权限控制，保证敏感数据仅本地处理。

### 2. 架构：三层 Client‑Server 模型
| 角色 | 职责 |
|------|------|
| **Host（宿主应用）** | 集成 MCP Client 的 AI 应用，如 Claude 桌面版、Cursor 等 |
| **MCP Client** | 协议解析、服务发现、会话管理，与 Server 一对一连接 |
| **MCP Server** | 暴露具体工具/资源的独立进程，隔离运行 |

### 3. 通信协议：基于 JSON‑RPC 2.0
所有请求与响应均采用结构化 JSON 格式，例如：

```json
// 请求
{
  "jsonrpc": "2.0",
  "id": "1",
  "method": "calendar.query",
  "params": {
    "start_time": "2024-11-01T00:00:00Z",
    "end_time": "2024-11-30T23:59:59Z"
  }
}

// 响应
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": [
    {"title": "团队会议", "time": "2024-11-15T10:00:00Z"},
    {"title": "客户访谈", "time": "2024-11-20T14:30:00Z"}
  ]
}
传输层支持 stdio、HTTP、SSE/WebFlux 等多种实现。

4. 三大核心能力
能力	描述	典型场景
Tools	执行具体操作	发邮件、查数据库、调 API
Resources	提供实时数据流	股票行情、天气、文件读取
Prompts	封装复杂任务模板	报告生成、数据分析
5. 完整工作流程
能力发现：Client 与 Server 握手，获取可用工具列表及其 JSON Schema。

任务分发：LLM 根据上下文决定调用哪个工具。

协议转换：Host 通过 Client 发送标准 JSON‑RPC 请求。

执行返回：Server 执行逻辑，返回结构化结果。

结果整合：Host 将数据融入模型上下文，生成最终回复。

6. 与传统 Function Calling 的对比
维度	传统 Function Calling	MCP
工具定义位置	硬编码在 Prompt 或代码中	独立存储于 Server 端，动态发现
厂商绑定	与 LLM 提供商强绑定	跨厂商标准化协议
执行管理	开发者手动解析、调度	Host/Client 统一完成转换与调度
生命周期	无标准化权限/连接管理	内置会话管理、权限、沙箱
二、MCP 与 Skill、Agent、Rule 的核心区别
这四个概念分别位于 AI 智能体生态的不同层次：

概念	定位	核心关注点	类比
MCP	标准化通信协议	能做什么 — 让 AI 触达外部工具和数据	USB‑C 接口
Skill	声明式流程规范	怎么做 — 将业务规则、工作流编码为可复用模块	操作手册 / 工作法
Agent	智能体运行框架	谁来调度 — 具备感知、规划、执行能力的自主实体	项目经理
Rule	约束与合规规则	什么能做/不能做 — 行为边界和合规约束	公司规章制度
协作关系：
一个完整的 Agent 通常 = 通用 LLM + MCP（连接外部工具）+ Skills（提供操作流程）+ Rules（行为约束）。

特别说明：MCP 与 Skill 并非替代关系，而是互补搭档。MCP 提供原子能力（如查天气），Skill 定义如何组合这些能力完成业务目标（如制定出行计划）。

三、使用 Spring AI 实现 MCP
Spring AI 为 MCP 提供了开箱即用的 Server 与 Client 自动配置。

1. 核心 Starter 与传输支持
Starter	用途	传输方式
spring-ai-starter-mcp-server	核心 Server	STDIO
spring-ai-starter-mcp-server-webmvc	Server (WebMVC)	SSE 流式
spring-ai-starter-mcp-server-webflux	Server (WebFlux)	SSE 流式
spring-ai-starter-mcp-client	核心 Client	STDIO + HTTP SSE
spring-ai-starter-mcp-client-webflux	Client (WebFlux)	SSE 流式
2. MCP Server 端：暴露工具能力
添加依赖 (pom.xml)：

xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webmvc</artifactId>
</dependency>
配置 (application.yml)：

yaml
server:
  port: 8014
spring:
  application:
    name: mcp-server-demo
  ai:
    mcp:
      server:
        type: async
        protocol: STREAMABLE      # Streamable-HTTP 协议
        name: custom-mcp-server
        version: 1.0.0
定义工具 （使用 @Tool 注解自动注册）：

java
@Service
public class WeatherService {
    @Tool(description = "根据城市名称获取天气预报")
    public String getWeatherByCity(
        @ToolParam(description = "城市名称，如北京、上海、深圳") String city) {
        return switch (city) {
            case "北京" -> "北京：多云，15℃~27℃，南风3级";
            case "上海" -> "上海：小雨，18℃~25℃，东风2级";
            default -> "暂无该城市天气信息";
        };
    }
}
3. MCP Client 端：连接服务并注入 AI 调用链
添加依赖 (pom.xml)：

xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-client</artifactId>
</dependency>
<!-- 示例使用通义千问模型 -->
<dependency>
    <groupId>com.alibaba.cloud.ai</groupId>
    <artifactId>spring-ai-alibaba-starter-dashscope</artifactId>
</dependency>
配置连接到 Streamable‑HTTP Server (application.yml)：

yaml
server:
  port: 8015
spring:
  ai:
    mcp:
      client:
        type: async
        request-timeout: 60s
        toolcallback:
          enabled: true
        streamable-http:
          connections:
            weather-server:
              url: http://localhost:8014
              endpoint: /mcp
连接第三方 STDIO 服务（如百度地图，通过 mcp-server.json5 描述启动命令）：

yaml
spring:
  ai:
    mcp:
      client:
        request-timeout: 20s
        toolcallback:
          enabled: true
        stdio:
          servers-configuration: classpath:/mcp-server.json5
mcp-server.json5 示例：

json5
{
  "mcpServers": {
    "baidu-map": {
      "command": "npx",
      "args": ["-y", "@baidumap/mcp-server-baidu-map"],
      "env": {
        "BAIDU_MAP_API_KEY": "${BAIDU_MAP_API_KEY}"
      }
    }
  }
}
将远程工具注册到 ChatClient：

java
@Configuration
public class AiConfig {
    @Bean
    public ChatClient chatClient(
            ChatModel chatModel,
            ToolCallbackProvider tools) {
        return ChatClient.builder(chatModel)
                .defaultToolCallbacks(tools.getToolCallbacks())
                .build();
    }
}
对话接口示例：

java
@RestController
public class ChatController {
    @Resource
    private ChatClient chatClient;

    @GetMapping("/chat")
    public Flux<String> chat(@RequestParam(defaultValue = "北京") String msg) {
        return chatClient.prompt(msg).stream().content();
    }
}
完整调用流程：

text
用户提问："北京今天天气怎么样？"
  → ChatClient 判断需要调用工具
  → MCP Client 发送 JSON‑RPC 请求到 MCP Server (:8014)
  → Server 执行 WeatherService.getWeatherByCity("北京")
  → 返回结果 {"result":{"content":[{"text":"北京：多云…"}]}}
  → ChatClient 整合结果生成自然语言回复
四、一个服务既是 Client 又是 Server（自调用）
结论：完全可行。 同一个 Spring 应用可以同时启动 MCP Server 和 MCP Client，并让 Client 连接自己的 Server 端点。

实现方式
同时引入 Server 与 Client 的 Starter，并配置 Client 指向本地服务地址：

依赖（两个 Starter 共存）：

xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webmvc</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-client</artifactId>
</dependency>
配置 (application.yml)：

yaml
server:
  port: 8080

spring:
  ai:
    mcp:
      server:
        type: ASYNC
        protocol: STREAMABLE
        name: self-serving-server
      client:
        type: ASYNC
        toolcallback:
          enabled: true
        streamable-http:
          connections:
            self:
              url: http://localhost:8080
              endpoint: /mcp
此时应用将自己暴露的工具通过本地网络回路供自己调用，模型可完全通过 MCP 协议使用这些工具。

典型应用场景
统一工具管理平面：本地与远程工具均使用同一套 MCP 协议接入。

强制解耦：为未来拆分模块做准备，代码无需改动。

开发调试：验证 MCP 协议实现的正确性。

安全沙箱：主动通过 MCP 权限限制 LLM 对本服务内部工具的访问范围。

注意事项与推荐实践
性能开销：自我调用会走完整的网络栈（序列化/反序列化、TCP 握手），高频轻量工具不建议如此。

循环调用风险：若工具内部又触发 ChatClient 推理，容易形成无限递归，需在业务层设计终止条件。

最佳实践：如果仅仅为了让 LLM 调用本服务的某个方法，直接使用 @Tool 注解 + 本地 ToolCallback 注入 ChatClient 是更简单、更高效的选择。
只有在需要将本地能力暴露为标准的、可供外部 Agent 发现的 MCP 服务，且自身也想复用同一套工具描述时，才值得采用“既是 Client 又是 Server”的模式。
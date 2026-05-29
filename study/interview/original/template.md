# Spring AI 智能体技术面试记录

## 问题 1：工具定义与注册
**问题**：在 Spring AI 中，如何定义一个可供智能体调用的工具（Tool）？请说明 `@Tool` 注解的作用，并给出一个简单的代码示例，展示如何将该工具注册到 `ChatClient` 中。

**候选人回答**：在方法上加上@tool注解，并定义其名称和方法，使用chantclient.tools方法

**面试官评价与补充**：基本正确，但漏掉了关键细节。`@Tool` 注解不仅标记方法，还需要通过 `ChatClient.Builder.tools()` 将工具对象注册进去，并且要提供方法的实例（通常是 Spring Bean）。`@Tool` 的作用是声明方法的元数据（名称、描述、参数信息），让框架能自动生成工具调用所需的 schema。

**参考答案**：
```java
@Component
public class WeatherService {
    @Tool(description = "获取指定城市的天气")
    public String getWeather(@ToolParam(description = "城市名称") String city) {
        // 实际调用天气 API
        return city + " 当前晴朗，25°C";
    }
}

// 注册到 ChatClient
@Autowired
private WeatherService weatherService;

ChatClient client = ChatClient.builder(chatModel)
    .defaultTools(weatherService)  // 这里传入 Bean 实例
    .build();
注意：defaultTools() 接收的是对象实例，框架会扫描其所有带 @Tool 的方法并转换为 MethodToolCallback。@ToolParam 用于描述参数，帮助大模型理解。

问题 2：工具调用内部流程
问题：工具注册后，当用户消息触发工具调用时，Spring AI 内部是如何处理这个过程的？请描述从大模型决策调用工具，到工具执行完毕并将结果返回给大模型的完整流程。

候选人回答：根据提示词与tools的名称描述进行匹配，匹配度最高的那个返回调用

面试官评价与补充：你的理解过于简化了。实际上，Spring AI 内部处理工具调用的流程要复杂得多，涉及多轮交互。

参考答案：
完整流程如下：

请求构建：ChatClient 调用时，会将已注册的工具（ToolCallback 列表）转换成 OpenAI 兼容的 functions 参数（包含函数名称、描述、参数 JSON Schema）随请求发送给大模型。

大模型决策：大模型根据用户消息和函数描述，决定是否调用某个工具。若需调用，返回的不是文本，而是一个 tool_calls 响应，指定调用的函数名和 JSON 参数。

框架拦截：ChatClient 内置的 ToolCallingChatModel 或相关拦截器检测到 tool_calls，不再直接返回给用户，而是根据函数名在注册的工具列表中查找匹配的 ToolCallback（默认按名称精确匹配）。

参数绑定与执行：将 JSON 参数反序列化为 ToolCallback 的输入参数，调用其 call(String toolInput) 方法（MethodToolCallback 会自动将 JSON 绑定到 @ToolParam 标注的方法参数并执行实际方法）。

结果回传：工具执行结果以 ToolResponseMessage 的形式追加到对话历史中，并立即发起一次新的模型调用（ReAct 循环），让模型基于工具返回结果生成最终回复。

终止条件：如果模型再次请求工具，则重复上述过程；如果返回普通文本，则将最终响应返回给调用方。
关键类是 DefaultToolCallingChatModel、ToolCallingManager，以及 ToolCallback 接口。

问题 3：FlowAgent 多智能体顺序执行
问题：在多智能体场景下，Spring AI 的 FlowAgent 是如何实现多个智能体按顺序执行并传递结果的？请说明其核心工作方式。

候选人回答：不知道

面试官评价与补充：无

参考答案：
FlowAgent 是 Spring AI 中用于实现多智能体顺序编排的核心类，它的工作方式类似于工作流引擎：

定义步骤：FlowAgent 内部维护一个有序的智能体列表（List<Agent>），每个智能体可以视为流程中的一个处理节点。

顺序执行：当用户输入进入 FlowAgent 后，它会按顺序依次调用每个智能体的 call(String input) 方法。

结果传递：第一个智能体接收原始用户输入，执行后的输出会作为下一个智能体的输入。默认情况下，是直接将上一个智能体的完整输出文本作为下一个智能体的输入，形成一个线性的数据流。

构建方式：通过 FlowAgent.builder() 创建，使用 .agents(agent1, agent2, ...) 注册智能体序列，也可通过 .name() 和 .description() 描述自身作为智能体的元数据（因为 FlowAgent 本身也实现了 Agent 接口，可以嵌套组合）。

终止条件：当所有智能体依次执行完毕后，最后一个智能体的输出就是整个 FlowAgent 的最终输出。

代码示例：

java
Agent analyzer = Agent.builder()
    .model(chatModel)
    .tool(new TextAnalysisTool())
    .build();

Agent reporter = Agent.builder()
    .model(chatModel)
    .tool(new ReportGenerateTool())
    .build();

FlowAgent flow = FlowAgent.builder()
    .name("analysis-flow")
    .agents(analyzer, reporter)
    .build();

String result = flow.call("请分析这份销售数据并生成报告");
这里 analyzer 先分析数据，输出分析结论；reporter 接收分析结论并生成格式化报告。两者之间就是通过输入输出文本进行通信的。

问题 4：MessageChatMemoryAdvisor 记忆机制
问题：Spring AI 中的 MessageChatMemoryAdvisor 是如何为智能体提供记忆能力的？它内部使用了什么数据结构，以及在对话流程中是如何与 ChatClient 交互的？

候选人回答：通过对chatmodel方法拦截，提供around方法，将结果追加到chatmemory中使用map进行本地临时缓存；发起时，将记忆中的内容填充进请求体中，作为输入参数

面试官评价与补充：基本正确，但描述不够精准。你提到的“拦截 chatmodel 方法”和“around 方法”思路对，但具体实现是基于 Spring AI 的 Advisor 机制。

参考答案：

MessageChatMemoryAdvisor 是一个 RequestResponseAdvisor，它围绕着 ChatClient 的请求-响应生命周期工作，而非直接拦截 ChatModel。

数据结构：它并不直接使用 Map，而是依赖 ChatMemory 接口，默认实现 InMemoryChatMemory 内部才使用 ConcurrentHashMap<String, List<Message>>（key 为 conversationId）。你也可以通过 ChatMemory 接口切换到持久化存储（如 Redis、数据库）。

交互流程：

请求前（before）：根据 conversationId 从 ChatMemory 取出历史消息，将其添加到当前 Prompt 的消息列表头部，这样大模型就能获取历史上下文。
响应后（after）：将本次请求的用户消息和模型响应消息追加回 ChatMemory，完成记忆更新。
使用方式：

java
ChatMemory memory = new InMemoryChatMemory();
ChatClient client = ChatClient.builder(chatModel)
    .defaultAdvisors(new MessageChatMemoryAdvisor(memory))
    .build();
// 每次调用需指定会话 ID
client.prompt().user("...").advisors(a -> a.param("conversationId", "user-123")).call();
注意：MessageChatMemoryAdvisor 本身不生成记忆键，必须通过 advisors 参数动态传入 conversationId，否则不同用户的对话会混在一起。

问题 5：MCP 动态工具发现
问题：在 Spring AI 与 MCP（Model Context Protocol）集成时，McpClient 如何实现工具的动态发现，并且这个流程与传统的通过 @Tool 静态注册工具有什么本质区别？

候选人回答：不知道

面试官评价与补充：无

参考答案：
传统的 @Tool 注册是在应用启动时就确定好的，工具列表编码在项目中。而 MCP 引入 McpClient，实现了运行时动态获取工具：

连接 MCP Server：McpClient 通过标准传输层（如 HTTP SSE、WebSocket）连接到一个或多个远程 MCP 服务器。

工具发现：连接建立后，McpClient 调用 MCP 协议的 tools/list 方法，从服务器获取所有可用工具的元数据列表（包含名称、描述、JSON Schema 参数定义）。

动态转换为 ToolCallback：Spring AI 将每个远程工具元数据动态包装成 McpToolCallback（实现了 ToolCallback 接口），并自动注册到 ToolRegistry 或直接提供给 ChatClient。

调用过程透明：当大模型决定调用某个 MCP 工具时，McpToolCallback 会通过 McpClient 向 MCP 服务器发送 tools/call 请求，获取执行结果后返回给模型。

本质区别：

@Tool 是静态绑定：代码内实现，工具能力和位置在编译/启动时固定。

MCP 是动态发现：工具可以在运行时添加/删除，由远程服务动态提供，无需重启应用。这实现了真正的工具即服务（Tool-as-a-Service），让智能体可以随时利用外部生态的工具能力，极大提升了灵活性。

java
// MCP 客户端连接到远程天气工具服务器
McpClient client = McpClient.using(transport).sync();
List<ToolCallback> tools = client.listTools()
    .stream()
    .map(McpToolCallback::new)
    .collect(Collectors.toList());

ChatClient chatClient = ChatClient.builder(chatModel)
    .tools(tools)  // 动态工具
    .build();
问题 6：SimpleAgent 与 ReAct 规划
问题：Spring AI 的 SimpleAgent 内部使用的 ReAct（Reasoning and Acting）规划模式具体是如何工作的？请描述其核心的“思考-行动-观察”循环的实现机制。

候选人回答：不知道

面试官评价与补充：SimpleAgent 实际上不涉及 ReAct 规划，它是单轮对话封装。真正实现 ReAct 的是 ReactAgent 或 ReActAgent。

参考答案：
SimpleAgent 是轻量级智能体，其核心价值是不涉及复杂的 ReAct 规划模式。它为简单问答场景提供单轮对话的封装：

java
SimpleAgent agent = SimpleAgent.builder()
    .chatModel(chatModel)
    .systemPrompt("你是一个客服助手")
    .build();
String result = agent.call("退货流程是什么？");
真正实现“思考-行动-观察”循环的是 ReactAgent 或 ReActAgent，核心机制如下：

推理与决策：向大模型发送包含历史、提示词和可用工具的请求，让其自主决策：是调用工具（给出函数名+参数JSON），还是调用“终结动作”（如 finish()）结束循环并生成最终答案。

行动与执行：框架解析大模型的响应，生成 ToolCallingChatModel 或 ToolCallback 调用。内部的 AgentToolNode 节点负责执行这些工具，支持顺序、并行调用及超时处理。

观察与反馈：将工具返回的结果（观察）作为新消息加入对话历史，开启新一轮思考，直至任务完成或触发停止条件。
为防止死循环，框架通常会设置硬性终止条件，如最大循环轮次（如5轮）或超时（如5分钟）。

问题 7：FlowAgent 多智能体协作细节
问题：Spring AI 是如何实现多智能体协作的？FlowAgent 在执行其智能体序列时，它们之间的输入和输出是如何传递的？

候选人回答：不知道

面试官评价与补充：无

参考答案：
FlowAgent 实现多智能体协作时，默认采用线性、字符串传递的方式，机制非常直接：

输入输出传递：FlowAgent 维护一个智能体列表，按顺序执行。上一个智能体 (Agent) 的 call() 方法返回的完整文本输出，直接作为下一个智能体 call() 方法的文本输入。

无中间转换：默认没有对输出进行结构化解析或转换，完全是原始字符串的透传。这就要求智能体之间的“约定”非常清晰，前一个的输出必须包含后一个能理解的上下文。

可组合性：FlowAgent 本身也是一个 Agent，因此可以被另一个 FlowAgent 嵌套，形成更复杂的流程，输入输出规则同上。

代码示例：

java
// 智能体1：提取关键词
Agent extractor = Agent.builder()
    .chatModel(chatModel)
    .systemPrompt("从文本中提取3个核心关键词，用逗号分隔。")
    .build();

// 智能体2：根据关键词写摘要
Agent summarizer = Agent.builder()
    .chatModel(chatModel)
    .systemPrompt("根据提供的关键词，写一段100字的摘要。")
    .build();

// 编排
FlowAgent pipeline = FlowAgent.builder()
    .agents(extractor, summarizer) // 输出 -> 输入 自动流转
    .build();

String article = "（一篇长文章）";
String summary = pipeline.call(article);
// extractor 输出: "AI, 智能体, 协作"
// summarizer 输入: "AI, 智能体, 协作"，并据此生成摘要
问题 8：人工审批工具调用（HumanFeedbackToolCallback）
问题：当一个关键的工具调用（如转账、删除数据）需要人工审批时，Spring AI 提供了什么机制来实现？HumanFeedbackToolCallback 是如何介入工具执行流程的？

候选人回答：不知道

面试官评价与补充：无

参考答案：
HumanFeedbackToolCallback 是 Spring AI 提供的工具调用审批机制，它通过装饰器模式包裹一个真实的 ToolCallback，在工具执行前插入人工审批环节。
工作流程：

拦截调用：当大模型决定调用某个关键工具时，HumanFeedbackToolCallback 不会立即执行，而是挂起当前对话。

发送审批请求：它通过 HumanFeedbackService 接口，向外部系统（如审批后台、即时通讯工具）发送审批请求，并携带工具名称和参数。

等待审批结果：对话会阻塞等待，直到审批完成。审批服务通过唯一的 feedbackId 返回结果（批准或拒绝，可附带修改意见）。

执行或拒绝：

批准：调用被包装的真实 ToolCallback 执行原始操作，并将结果返回给大模型。

拒绝：返回一个预设的错误或拒绝消息（如“操作已被管理员拒绝”），模型会据此生成相应的回复。

代码示例：

java
// 1. 定义真实工具
@Component
class PaymentTool {
    @Tool(description = "执行转账操作")
    public String transfer(String fromAccount, String toAccount, double amount) {
        return "转账成功";
    }
}

// 2. 包装为人工审批工具
ToolCallback rawCallback = MethodToolCallback.builder()
    .toolObject(new PaymentTool())
    .methodName("transfer")
    .build();

ToolCallback approvedCallback = HumanFeedbackToolCallback.builder()
    .toolCallback(rawCallback) // 被装饰的真实工具
    .humanFeedbackService(feedbackService) // 注入审批服务
    .build();

// 3. 注册到智能体
Agent agent = Agent.builder()
    .chatModel(chatModel)
    .tools(List.of(approvedCallback))
    .build();
适用场景： 转账、删除数据、发送重要通知等高风险操作，确保 AI 的决策在人类监督下执行。

问题 9：可观测性监控
问题：在构建生产级智能体应用时，如何对智能体的工具调用链路进行可观测性监控？Spring AI 提供了哪些关键指标或日志点来追踪一次完整的“思考-调用-返回”循环？

候选人回答：不会

面试官评价与补充：无

参考答案：
Spring AI 通过集成 Micrometer 和内置日志机制提供可观测性支持，主要包含以下几个方面：
1. 自动指标（Micrometer Metrics）
Spring AI 会自动注册以下核心指标，可在 /actuator/metrics 中查看：

spring.ai.chat.client.requests：记录 ChatClient 的调用次数、持续时间和状态。

spring.ai.tool.calls：记录工具调用的次数、耗时及成功/失败状态。

spring.ai.vector.store.requests：向量存储操作的延迟和计数（当与 RAG 协同使用时）。
2. 关键日志点
在 application.properties 中开启详细日志：

properties
logging.level.org.springframework.ai=DEBUG
logging.level.org.springframework.ai.chat.client=TRACE
可观察到的关键阶段包括：

请求构建：发送给大模型的完整消息体（含工具描述）。

大模型响应：返回的文本或 tool_calls JSON。

工具执行：MethodToolCallback 的实际调用输入与输出。

结果回传：工具结果追加到对话历史的完整报文。
3. 自定义观测（Span/Event）
利用 Micrometer Tracing 可创建自定义 Span，追踪一个完整的 ReAct 循环：

java
Observation observation = Observation.createNotStarted("agent.react.cycle", registry)
    .lowCardinalityKeyValue("agent.name", "myAgent")
    .start();
try {
    // 执行智能体调用
    String result = agent.call(input);
    return result;
} catch (Exception e) {
    observation.error(e);
    throw e;
} finally {
    observation.stop();
}
这能将工具调用、模型请求等子操作关联到同一 Trace，便于在 Jaeger/Zipkin 中分析完整链路。
4. Advisor 拦截点
通过自定义 CallAroundAdvisor 可在 ChatClient 调用前后记录详细的上下文快照，包括工具列表、消息历史和响应时间，实现精细化审计。

问题 10：工具调用错误恢复策略
问题：在 Spring AI 智能体中，如何处理工具调用时可能出现的错误（如参数无效、外部服务超时）？框架提供了怎样的错误恢复策略或重试机制来保证流程的鲁棒性？

候选人回答：不知道

面试官评价与补充：无

参考答案：
Spring AI 对工具调用错误提供了多层次的容错与恢复策略：
1. 工具层面的异常处理
ToolCallback 执行时若抛出异常，框架会捕获并将异常信息封装为 ToolResponseMessage 返回给大模型。大模型可据此判断错误原因，尝试重新生成参数或采取其他行动。
2. 重试机制

大模型层面的重试：框架默认在遇到工具调用异常时，会将错误消息追加到对话历史，立即发起一次新的大模型调用，让模型自行修正并重试调用。该过程受 MaxToolCallIterations 限制（ReAct 循环上限，默认 5 次）。

底层重试：可结合 Spring Retry 或 Resilience4j 为远程工具调用添加重试策略，例如在 McpClient 或 HTTP 客户端层面设置超时与重试次数。
3. 兜底与恢复策略

工具调用超时处理：通过 ToolCallingManager 可配置单个工具调用的超时时间。若超时，框架返回超时错误给大模型，由大模型决定后续步骤。

错误回调：可自定义 ToolCallback 包装器，在 call() 方法内实现 try-catch 逻辑，返回特定的错误提示（如“服务暂时不可用，请稍后重试”），避免暴露原始异常堆栈。

退避策略：结合 MessageChatMemoryAdvisor 保存完整的失败上下文，允许模型在获得新信息后重新尝试。
配置示例：

java
Agent agent = Agent.builder()
    .chatModel(chatModel)
    .tools(List.of(robustToolCallback))
    .maxToolCallIterations(3) // 限制重试次数，防止死循环
    .build();
问题 11：智能体与 RAG 协同边界
问题：在 Spring AI 中，智能体与 RAG（检索增强生成）的协同边界是什么？即什么时候应该由智能体自主调用工具检索，什么时候应该使用 RAG 进行知识注入，两者如何配合？

候选人回答：问题是一个相对准确的问题时使用rag检索，rag检索不到回退到工具检索，如果能直接匹配对应的工具则是直接使用工具进行检索

面试官评价与补充：思路基本正确，但核心区分点在于：RAG 是被动上下文注入，而工具调用是主动决策执行。

参考答案：

RAG 适用场景：对相对确定的事实性知识查询，如“公司报销政策是什么”，通过 QuestionAnswerAdvisor 在请求前自动从知识库检索文档并注入 prompt，模型无需决定调用哪个工具。

工具检索适用场景：需要实时数据、执行动作或多步推理时，如“查询今日汇率并换算”，模型动态判断调用汇率工具，而非依赖静态检索。

协同模式：两者可以融合——将 RAG 检索器封装成一个 Tool（如 RetrievalTool），让智能体自主决定何时检索。这样既保留了 RAG 的知识注入能力，又赋予智能体调用时机的自主权，形成“工具化 RAG”。

回退策略：你提到的“RAG 检索不到回退到工具检索”是一种实用的混合策略，实现上可借助 ToolCallingAdvisor 的组合，或自定义路由逻辑。

问题 12：工具结果校验
问题：在工具调用过程中，如何对工具返回的结果进行校验，确保格式符合预期？Spring AI 是否提供了类似 ToolResultValidator 的机制，还是需要自定义实现？

候选人回答：通过hooks机制拦截返回结果，使用对应的结果审核tools进行检查

面试官评价与补充：思路正确，但 Spring AI 并没有现成的 ToolResultValidator 接口。校验是通过装饰器模式包装 ToolCallback 或使用 Advisor 拦截来实现的。

参考答案：
1. 装饰器模式（最常用）
自定义 ToolCallback 包装类，在调用真实工具后对返回值进行校验：

java
public class ValidatingToolCallback implements ToolCallback {
    private final ToolCallback delegate;
    
    @Override
    public String call(String toolInput) {
        String result = delegate.call(toolInput);
        // 校验：检查是否包含 "error" 或格式不符合JSON
        if (result.contains("error") || !isValidJson(result)) {
            return "工具返回异常，请提示用户稍后重试";
        }
        return result;
    }
}
2. Advisor 机制（类似“hooks”）
利用 CallAroundAdvisor，在工具调用链中全局拦截 ToolResponseMessage，统一校验所有工具返回值：

java
public class ToolResultValidationAdvisor implements CallAroundAdvisor {
    @Override
    public ChatResponse around(ChatClientRequest request, CallAroundAdvisorChain chain) {
        ChatResponse response = chain.next(request);
        // 遍历响应中的 ToolResponseMessage 进行校验
        response.getResults().forEach(result -> {
            if (result instanceof ToolResponseMessage toolMsg) {
                // 校验逻辑，不符则替换为错误提示
            }
        });
        return response;
    }
}
问题 13：流式响应中的工具调用
问题：当智能体使用流式响应（Streaming）时，工具调用的处理与非流式有什么区别？大模型如何输出 tool_calls，框架又是如何中断流式输出转而执行工具的？

候选人回答：流式响应会将每次的结果返回，非流式的会等待工具调用完成后返回，通过@tools注解绑定工具，通过.tools

面试官评价与补充：回答只涉及表象。流式响应的核心挑战在于大模型的 tool_calls 决策是逐步输出的，框架必须在流式过程中实时检测并中断。

参考答案：

流式输出检测：大模型在流式响应的 delta 中，可能先输出部分文本，若决定调用工具，则会开始输出 tool_calls 的分块（delta.tool_calls）。框架（如 ToolCallingStreamingChatModel）会累积这些分块，直到形成一个完整的 tool_calls 指令。

中断与执行：一旦检测到完整的工具调用指令，流式输出立即终止（丢弃已输出的不完整文本），不再向客户端推送任何文本。框架同步或异步执行对应的 ToolCallback。

结果回传与二次流式：工具结果以 ToolResponseMessage 形式追加到对话历史，然后框架发起一次新的流式请求，将工具结果连同之前的历史再次发送给大模型，让其基于结果生成最终答案。这次生成以流式方式推送至客户端。

关键区别：非流式模式下，整个过程对客户端透明，最终一次性返回；流式模式下，客户端必须能处理“先无输出，后突然开始流式输出”的体验，且工具调用本身可能产生用户无感知的暂停。

java
// 流式调用工具
chatClient.prompt()
    .user("查天气并穿衣建议")
    .tools(weatherTool)
    .stream()
    .content(); // 收到的是最终流式文本，工具调用过程被框架隐式处理
问题 14：基于用户角色的工具权限过滤
问题：在生产环境中，如何确保不同用户只能调用其权限范围内的工具？Spring AI 如何实现基于用户角色的工具过滤？

候选人回答：通过advisor对提示词进行增强，只筛选权限范围内的工具，将角色与工具关系进行绑定，通过advisor增加提示词，限制tools的取值范围

面试官评价与补充：基本正确，通过 Advisor 动态控制工具范围是一个可行思路。但更直接的做法是在构建 ChatClient 请求时，根据用户权限动态传入不同的工具列表，而不是仅依赖提示词约束。

参考答案：

java
// 1. 定义所有可用工具
Map<String, ToolCallback> allTools = Map.of(
    "orderQuery", orderTool,
    "userDelete", deleteTool
);

// 2. 根据用户角色过滤工具
public List<ToolCallback> getToolsForUser(String userId) {
    User user = userService.getById(userId);
    if (user.hasRole("ADMIN")) {
        return new ArrayList<>(allTools.values());
    } else {
        return List.of(allTools.get("orderQuery")); // 普通用户只能查订单
    }
}

// 3. 每次调用动态注册
String userId = SecurityContextHolder.getContext().getAuthentication().getName();
ChatClient client = ChatClient.builder(chatModel).build();
client.prompt()
    .user("删除用户123")
    .tools(getToolsForUser(userId)) // 动态工具列表
    .call();
额外安全加固：ToolCallback 内部也应做权限校验，从 SecurityContext 获取当前用户身份并判断是否允许执行，防止绕过过滤。

问题 15：错误恢复（备选工具/降级）
问题：在 Spring AI 中，如何实现一个智能体在执行任务失败时，自动进行错误恢复，例如切换备选工具或降级为人工处理？框架是否提供了内置的恢复策略接口？

候选人回答：通过toolback进行补偿重试

面试官评价与补充：回答可能指 ToolCallback 的某种回退机制，但 Spring AI 没有内置名为 ToolBack 的接口。实际实现错误恢复需要综合运用以下策略。

参考答案：
1. ReAct 循环天然支持重试
当工具调用返回错误信息时，大模型会在同一 ReAct 循环中重新决策，例如尝试修正参数或选择另一个工具。框架通过 maxToolCallIterations 限制重试上限。
2. 装饰器模式实现 Fallback
自定义 ToolCallback 包装器，内部捕获异常并执行备用逻辑：

java
public class FallbackToolCallback implements ToolCallback {
    private final ToolCallback primary;
    private final ToolCallback fallback;
    
    @Override
    public String call(String toolInput) {
        try {
            return primary.call(toolInput);
        } catch (Exception e) {
            return fallback.call(toolInput); // 切换到备用工具
        }
    }
}
3. 全局异常处理的 Advisor
通过 CallAroundAdvisor 捕获 ToolResponseMessage 中的错误，统一注入降级提示给大模型，引导模型走人工处理流程。
4. 人工降级
结合 HumanFeedbackToolCallback，当所有自动恢复失败时，自动提交审批任务，由人工接管。

示例：智能体配置错误恢复边界

java
Agent agent = Agent.builder()
    .chatModel(chatModel)
    .tools(List.of(primaryWithFallback))
    .maxToolCallIterations(3) // 最多重试3次
    .build();
问题 16：并行工具调用
问题：当智能体需要同时调用多个工具，且工具之间没有依赖关系时，Spring AI 是否支持并行工具调用？如果支持，框架是如何实现并行执行并合并结果的？

候选人回答：parallel模式可以支持并行调用，每个调用返回自己的结果，然后等批处理结束后汇总所有的结果信息

面试官评价与补充：基本正确，但需明确实现细节。Spring AI 通过 ToolCallingManager 支持并行工具调用。

参考答案：

触发条件：大模型在一次响应中返回多个 tool_calls，且这些调用之间无依赖。

并行执行：ToolCallingManager 检测到多个调用后，使用线程池同时执行每个 ToolCallback，大幅降低总耗时。

结果汇总：框架等待所有工具执行完毕（或超时），将每个结果分别封装为独立的 ToolResponseMessage，追加到对话历史中，然后发起下一次模型请求。

配置方式：可通过 ChatClient 或 Agent 的构建器设置 toolCallingMode 为 PARALLEL 来显式启用。

java
Agent agent = Agent.builder()
    .chatModel(chatModel)
    .tools(tools)
    .toolCallingMode(ToolCallingMode.PARALLEL)
    .build();
问题 17：参数约束与防止幻觉
问题：在工具定义时，如何避免大模型因“幻觉”传递错误参数？Spring AI 中如何利用 @ToolParam 的 JSON Schema 生成来约束参数类型与取值范围？

候选人回答：使用advisor进行提示词增加，加以transform进行关键词切割，提示词

面试官评价与补充：回答没有抓住问题核心。避免大模型传递错误参数，主要不是靠 Advisor 增强提示词，而是依赖 @ToolParam 生成的 JSON Schema 强约束 + 后端参数校验兜底。

参考答案：

@ToolParam 自动生成 JSON Schema：框架会根据参数类型和注解属性生成 JSON Schema，作为工具定义的一部分发给大模型。大模型据此理解参数格式、是否必填、默认值等，从而降低幻觉。

java
@Tool(description = "查询订单")
public Order queryOrder(
    @ToolParam(description = "订单ID，纯数字", required = true) String orderId,
    @ToolParam(description = "查询日期，格式yyyy-MM-dd") String date) { ... }
硬约束仍需后端校验：JSON Schema 对模型只是“强烈建议”，无法完全阻止非法值。最佳实践是在 ToolCallback 内部或 call 方法中做参数验证，若非法则返回结构化的错误消息（如“orderId必须为数字”），模型看到后会在下一轮思考中修正参数。

利用 Schema 自定义注解（如 @JsonProperty）：结合 Jackson 注解可进一步约束枚举、格式等，生成的 Schema 会更精确。

问题 18：分布式共享对话记忆
问题：在分布式部署中，多个服务实例如何共享智能体的对话记忆？Spring AI 如何将 InMemoryChatMemory 替换为基于 Redis 或数据库的持久化实现？

候选人回答：共享一个threadId，通过id获取对应的chatmemory，替换对应的RedsiChatMemory

面试官评价与补充：基本正确。Spring AI 的 ChatMemory 接口设计支持扩展，只需注入自定义实现即可实现分布式共享。

参考答案：

java
// 1. 自定义 RedisChatMemory 实现 ChatMemory 接口
@Component
public class RedisChatMemory implements ChatMemory {
    @Autowired
    private RedisTemplate<String, List<Message>> redisTemplate;
    
    @Override
    public void add(String conversationId, List<Message> messages) {
        redisTemplate.opsForList().rightPushAll(conversationId, messages);
    }
    @Override
    public List<Message> get(String conversationId, int lastN) {
        // 从 Redis 获取并截取最近 N 条
    }
    @Override
    public void clear(String conversationId) {
        redisTemplate.delete(conversationId);
    }
}

// 2. 注入到 Advisor，所有服务实例共享同一 conversationId 的记忆
ChatClient client = ChatClient.builder(chatModel)
    .defaultAdvisors(new MessageChatMemoryAdvisor(redisChatMemory))
    .build();
核心要点：conversationId 是记忆的隔离键，不同实例间通过同一个 ID 就能从 Redis 读取相同的对话历史，实现无状态服务的水平扩展。
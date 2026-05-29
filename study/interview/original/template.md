# Spring AI 中 ToolCallback、Advisor 与 Hook 的区别及执行顺序

在 Spring AI 应用中，`ToolCallback`、`Advisor` 和 `Hook` 三个概念分别负责不同层级的功能增强与流程控制。理解它们的职责与协作顺序，是构建健壮、可控 AI 应用的关键。

---

## 1. 概念对比

| 特性 | 🔧 工具回调 (ToolCallback) | 📝 顾问/增强器 (Advisor) | ⚙️ 钩子 (Hook) |
| :--- | :--- | :--- | :--- |
| **核心职责** | 定义 AI 可以直接执行的**具体能力**（如调用 API、查数据库）。 | 在模型调用**前后**进行拦截与增强（如日志、RAG、记忆）。 | 在 Agent 执行的**关键生命周期节点**进行流程控制与监控（如人工介入、限制迭代次数）。 |
| **操作对象** | 模型请求调用的具体函数/工具。 | 用户提问 (`Prompt`) 和模型回复 (`Response`)。 | Agent 的完整状态（对话历史、规划步骤、执行上下文）。 |
| **工作层级** | 模型与外部世界交互的**具体执行层**。 | `ChatClient` 与 `ChatModel` 之间的**通信拦截层**。 | Agent 核心执行引擎内部的**状态与生命周期层**。 |
| **典型场景** | 查询天气、发送邮件、执行业务逻辑。 | 对话记忆、RAG 检索、日志记录、内容校验、护栏。 | 人工审批 (HITL)、消息压缩、规划步骤、工具重试、无限循环中断。 |

---

## 2. 详细说明与代码示例

### 2.1 ToolCallback：AI 的“工具箱”

`ToolCallback` 接口将具体函数包装成 AI 模型可调用的工具。你可以通过 `@Tool` 注解或手动构建 `MethodToolCallback` / `FunctionToolCallback` 来定义。

#### 自定义装饰器示例：`ValidatingToolCallback`

```java
import org.springframework.ai.tool.ToolCallback;
import org.springframework.ai.tool.definition.ToolDefinition;

public class ValidatingToolCallback implements ToolCallback {

    private final ToolCallback delegate;

    public ValidatingToolCallback(ToolCallback delegate) {
        this.delegate = delegate;
    }

    @Override
    public String call(String toolInput) {
        // 前置处理可在此处添加
        String result = delegate.call(toolInput);
        
        // 后置校验：检查结果是否包含 "error" 或是否为非法 JSON
        if (result != null && (result.contains("error") || !isValidJson(result))) {
            return "工具返回异常，请提示用户稍后重试";
        }
        return result;
    }

    @Override
    public ToolDefinition getToolDefinition() {
        return this.delegate.getToolDefinition();
    }

    private boolean isValidJson(String json) {
        // 简单校验（实际可使用 Jackson 等库）
        return json != null && (json.startsWith("{") || json.startsWith("["));
    }
}
注册被装饰的 ToolCallback
java
@Configuration
public class ToolConfig {

    @Bean
    public List<ToolCallback> myTools(MyWeatherService weatherService) {
        // 1. 从 @Tool 注解的方法生成原始 ToolCallback
        List<ToolCallback> original = ToolCallbacks.from(weatherService);
        
        // 2. 用 ValidatingToolCallback 装饰每一个原始实例
        return original.stream()
                .map(ValidatingToolCallback::new)
                .collect(Collectors.toList());
    }
}
💡 说明：ValidatingToolCallback::new 是构造函数引用，等价于 delegate -> new ValidatingToolCallback(delegate)，会在流迭代时为每个原始 ToolCallback 创建一个包装实例。

2.2 Advisor：对话的“高级秘书”
Advisor 在请求发送给模型之前和响应返回给用户之前执行通用增强逻辑。多个 Advisor 按 Ordered 顺序组成责任链。

java
import org.springframework.ai.chat.client.advisor.api.Advisor;
import org.springframework.ai.chat.client.advisor.api.RequestResponseAdvisor;
import org.springframework.core.Ordered;

public class LoggingAdvisor implements RequestResponseAdvisor, Ordered {

    @Override
    public int getOrder() {
        return 0; // 值越小优先级越高
    }

    @Override
    public AdviceResponse aroundCall(AdviceRequest request, AdvisorChain chain) {
        System.out.println(">>> 前置：请求内容为 " + request.userText());
        AdviceResponse response = chain.next(request);
        System.out.println("<<< 后置：模型响应为 " + response.response());
        return response;
    }
}
2.3 Hook：Agent 的“流程监理”
Hook 在 Agent 执行的关键节点（如 BEFORE_AGENT、AFTER_MODEL、TOOL_CALL）插入自定义逻辑，甚至可以中断流程等待外部输入。

java
import org.springframework.ai.agent.AgentHook;
import org.springframework.ai.agent.AgentState;

public class HumanInTheLoopHook implements AgentHook {

    @Override
    public AgentState beforeModel(AgentState state, AgentContext ctx) {
        // 检查是否需要人工审批
        if (state.getLastToolRequest() != null && state.getLastToolRequest().name().equals("deleteData")) {
            System.out.println("⚠️ 高风险操作，请人工确认 (y/n)：");
            // 等待用户输入（实际应用中可阻塞或异步回调）
            // 若拒绝，可修改 state 或抛出异常中断流程
        }
        return state;
    }
}
3. 执行顺序（三者共存时）
三者形成 分层嵌套 结构：最外层 Hook → 中层 Advisor → 内层 ToolCallback。

3.1 顺序流程图（Mermaid）
sequenceDiagram
    participant Client
    participant AdvisorChain
    participant HookSystem
    participant LLM
    participant ToolCallback

    Client->>AdvisorChain: 发起请求
    Note over AdvisorChain: 按 Order 排序执行
    AdvisorChain->>HookSystem: 调用前
    Note over HookSystem: 执行 BEFORE_AGENT 钩子
    loop 每次推理迭代
        Note over HookSystem: 执行 BEFORE_MODEL 钩子
        HookSystem->>LLM: 发送请求
        LLM-->>HookSystem: 返回响应
        Note over HookSystem: 执行 AFTER_MODEL 钩子
        alt 模型请求调用工具
            HookSystem->>ToolCallback: 执行工具调用
            ToolCallback-->>HookSystem: 返回结果
            Note over HookSystem: 将工具结果加入对话历史
        end
    end
    Note over HookSystem: 执行 AFTER_AGENT 钩子
    HookSystem-->>AdvisorChain: 返回最终响应
    AdvisorChain-->>Client: 最终响应
3.2 各阶段详细说明
阶段	执行组件	说明
1. 请求进入	BEFORE_AGENT Hook	在一切开始前执行（如初始化上下文、锁资源）。
2. Advisor 前置链	Advisor.before()	按 Ordered 升序执行（日志 → 记忆 → RAG 等）。
3. 迭代前	BEFORE_MODEL Hook	每次调用 LLM 前执行（如修改提示词、注入系统消息）。
4. LLM 调用	ChatModel	发送请求并接收响应。
5. 迭代后	AFTER_MODEL Hook	检查模型输出，决定是否继续迭代或中断。
6. 工具执行	ToolCallback	若模型请求调用工具，则执行对应的 ToolCallback（可能多次）。
7. Advisor 后置链	Advisor.after()	按 Ordered 逆序执行。
8. 请求结束	AFTER_AGENT Hook	执行清理、统计、持久化等收尾工作。
注意：步骤 3~6 可能循环多次（ReAct 模式），直到模型不再请求新工具或达到最大迭代次数。

4. 何时使用哪种扩展点？
需求场景	推荐组件	理由
让 AI 查询天气、发邮件、调用内部 API	ToolCallback	定义具体能力。
自动添加对话历史到每次请求	Advisor	横切关注点，与具体业务无关。
记录每次请求/响应的日志	Advisor	标准拦截器模式。
在 AI 执行前检索相关文档（RAG）	Advisor	修改请求上下文。
高风险操作需要人工审批	Hook (如 BEFORE_MODEL / TOOL_CALL)	流程控制、可中断。
限制 Agent 的推理迭代次数（防无限循环）	Hook (如 AFTER_MODEL)	检查状态并强制终止。
对工具调用的结果进行统一校验或重试	ToolCallback 装饰器 + ToolRetryInterceptor	属于工具执行层的增强。
5. 总结
ToolCallback 是 AI 的“手脚”，负责具体动作执行。

Advisor 是“高级秘书”，处理每次请求/响应的通用横切逻辑。

Hook 是“监理”，把控 Agent 整个生命周期的关键节点。

三者可以无缝组合使用：Advisor 装饰 ChatClient 调用链，Hook 嵌入 Agent 执行引擎，而 ToolCallback 则被 ToolCallAdvisor 调度执行。理解它们的协作顺序，能够帮助你设计出更加健壮、可控的 AI 应用。
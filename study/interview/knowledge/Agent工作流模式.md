<!-- 模块：Agent 工作流模式 | 最后更新于 2026-05-29（FlowAgent / HumanFeedbackToolCallback） -->

# Agent 工作流模式

> 串行/循环/路由/并行 Agent 与 CoT/ToT 推理。

## 目录

- [SequentialAgent 与 LoopAgent 工作流](#sequentialagent-与-loopagent-工作流)
- [共享 ChatMemory 的多 Agent 协作](#共享-chatmemory-的多-agent-协作)
- [Orchestrator 子任务拆解与 CoT/ToT 推理](#orchestrator-子任务拆解与-cottot-推理)
- [Spring AI 常见工作流模式](#spring-ai-常见工作流模式)
- [多智能体监督与交接模式](#多智能体监督与交接模式)
- [IDE 分阶段顺序多智能体协同](#ide-分阶段顺序多智能体协同)
- [Human-in-the-Loop 工具审批（ReactAgent + HumanInTheLoopHook）](#human-in-the-loop-工具审批reactagent--humanintheloophook)
- [FlowAgent 顺序多智能体编排](#flowagent-顺序多智能体编排)
- [HumanFeedbackToolCallback 装饰器式人工审批](#humanfeedbacktoolcallback-装饰器式人工审批)

---
## SequentialAgent 与 LoopAgent 工作流

> **模块**：Agent 工作流模式 | **标签**：Agent与对话 | **更新**：2026-05-28

### 核心概念

SequentialAgent：按 A → B → C 顺序执行，前一 Agent 的 `outputKey` 作为下一 Agent 输入，适合写作→审阅→润色等固定流水线。

### 要点

- **SequentialAgent**：按 A → B → C 顺序执行，前一 Agent 的 `outputKey` 作为下一 Agent 输入，适合写作→审阅→润色等固定流水线。
- **LoopAgent**：子 Agent 循环执行直到 `condition` 返回 false 或达到 `maxIterations`，适合规划→评审→再规划直到评分达标。

### 代码示例

```java
ReactAgent agentA = ReactAgent.builder()
    .name("writer")
    .model(chatModel)
    .instruction("Write content based on: {input}")
    .outputKey("article")
    .build();

ReactAgent agentB = ReactAgent.builder()
    .name("reviewer")
    .model(chatModel)
    .instruction("Review and improve: {article}")
    .outputKey("reviewed")
    .build();

ReactAgent agentC = ReactAgent.builder()
    .name("polisher")
    .model(chatModel)
    .instruction("Polish: {reviewed}")
    .outputKey("final")
    .build();

SequentialAgent workflow = SequentialAgent.builder()
    .name("blogPipeline")
    .subAgents(List.of(agentA, agentB, agentC))
    .build();

workflow.invoke("Spring AI basics");

LoopAgent loopAgent = LoopAgent.builder()
    .name("planningLoop")
    .subAgents(List.of(plannerAgent, reviewerAgent))
    .condition(state -> {
        int score = extractScore(state.get("review_result"));
        return score < 80;
    })
    .maxIterations(5)
    .build();
```

### 面试常问

**问**：Spring AI Alibaba 中如何实现多 Agent 串行流水线与条件循环？

**答**：SequentialAgent**：按 A → B → C 顺序执行，前一 Agent 的 `outputKey` 作为下一 Agent 输入，适合写作→审阅→润色等固定流水线。；LoopAgent**：子 Agent 循环执行直到 `condition` 返回 false 或达到 `maxIterations`，适合规划→评审→再规划直到评分达标。。

### 关联知识点

- [Agent 架构与协同](Agent架构与协同.md)
- [Agent 记忆体系](Agent记忆体系.md)

---
## 共享 ChatMemory 的多 Agent 协作

> **模块**：Agent 工作流模式 | **标签**：Agent与对话 | **更新**：2026-05-28

### 核心概念

多个 `ReactAgent` 共享同一 `ChatMemory` 实例（如 `InMemoryChatMemory`）。

### 要点

- 多个 `ReactAgent` 共享同一 `ChatMemory` 实例（如 `InMemoryChatMemory`）。
- 交替调用各 Agent，历史消息自动写入共享 memory，后续 Agent 可读取完整对话上下文。
- 适合辩论、协作写作、角色扮演等需要「共同记忆」的场景。

### 代码示例

```java
ChatMemory memory = new InMemoryChatMemory();
Agent a = new ReactAgent(..., memory);
Agent b = new ReactAgent(..., memory);
// 多轮交替调用，共享对话历史
```

### 面试常问

**问**：多个 Agent 如何基于外部记忆实现多轮双向交互？

**答**：多个 `ReactAgent` 共享同一 `ChatMemory` 实例（如 `InMemoryChatMemory`）。；交替调用各 Agent，历史消息自动写入共享 memory，后续 Agent 可读取完整对话上下文。；适合辩论、协作写作、角色扮演等需要「共同记忆」的场景。。

### 关联知识点

- [Agent 架构与协同](Agent架构与协同.md)
- [Agent 记忆体系](Agent记忆体系.md)

---
## Orchestrator 子任务拆解与 CoT/ToT 推理

> **模块**：Agent 工作流模式 | **标签**：Agent与对话 | **更新**：2026-05-28

### 核心概念

**Orchestrator 模式（规划→执行→聚合）**：

### 要点

**Orchestrator 模式（规划→执行→聚合）**：

1. LLM 将目标分解为 3–5 个子任务。
2. Worker Agent 逐个执行子任务。
3. Aggregator 合并子结果输出最终答案。

**Chain-of-Thought (CoT)**：在 Prompt 中引导模型「逐步思考」，显式列出推理步骤后再给出答案，适合算术、逻辑推理。

**Tree-of-Thoughts (ToT)**：在 CoT 基础上扩展为树搜索——每层生成多个 thought 分支，评估后剪枝（beam search），适合需要探索多条推理路径的复杂问题。

### 代码示例

```java
public class Orchestrator {
    public String execute(String goal) {
        List<String> subTasks = decompose(goal);
        List<String> results = new ArrayList<>();
        for (String task : subTasks) {
            results.add(workerAgent.act(task));
        }
        return aggregator.merge(results);
    }

    private List<String> decompose(String goal) {
        String response = chatClient.prompt()
            .user("Break this goal into 3-5 subtasks: " + goal)
            .call().content();
        return parseSubtasks(response);
    }
}
```

```java
String prompt = """
Question: Roger has 5 tennis balls. He buys 2 more cans of 3 balls each. How many does he have?
Let's think step by step:
 1. Roger starts with 5 balls.
 2. Each can has 3 balls, and he buys 2 cans → 2 * 3 = 6 balls.
 3. Total = 5 + 6 = 11.
    Answer: 11
    Now answer: {question}
    """;
```

```java
public class TreeOfThoughts {
    public String solve(String problem) {
        List<Node> currentLevel = List.of(new Node(problem, null));
        for (int depth = 0; depth < maxDepth; depth++) {
            List<Node> nextLevel = new ArrayList<>();
            for (Node node : currentLevel) {
                List<String> thoughts = generateThoughts(node.state);
                for (String thought : thoughts) {
                    String newState = evaluate(thought);
                    nextLevel.add(new Node(newState, node));
                }
            }
            currentLevel = prune(nextLevel, beamWidth);
        }
        return bestLeaf(currentLevel).getSolution();
    }
}
```

### 面试常问

**问**：复杂任务如何拆解为子任务？Chain-of-Thought 与 Tree-of-Thoughts 有何区别？

**答**：**Orchestrator 模式（规划→执行→聚合）**： 1. LLM 将目标分解为 3–5 个子任务。 2. Worker Agent 逐个执行子任务。 3. Aggregator 合并子结果输出最终答案。 **Chain-of-Thought (CoT)**：在 Prompt 中引导模型「逐步思考」，显式列出推理步骤后再给出答案，适合算术、逻辑推理。 **Tree-of-Thoughts (ToT)**：在 CoT 基础上扩展为…

### 关联知识点

- [Agent 架构与协同](Agent架构与协同.md)
- [Agent 记忆体系](Agent记忆体系.md)

---
## Spring AI 常见工作流模式

> **模块**：Agent 工作流模式 | **标签**：Agent与对话 | **更新**：2026-05-28

### 核心概念

Spring AI / Alibaba 生态提供链式、路由、并行、编排器-工作者、评估器-优化器等典型模式；轻量场景可用 `ChatClient` 手写循环，复杂多 Agent 可用 Spring AI Alibaba 的 `SequentialAgent` 等组件。

### 要点

| 模式 | 核心用途 | 典型组件 |
| :--- | :--- | :--- |
| **链式 (Chain)** | 固定顺序流水线 | `ChainWorkflow`、顺序 Prompt 列表 |
| **路由 (Routing)** | 按意图分发到专业 Agent | `RoutingWorkflow`、`LlmRoutingAgent` |
| **并行 (Parallelization)** | 并发独立子任务 | `ParallelizationWorkflow` |
| **编排器-工作者** | 动态拆解 + 并行执行 | `TravelOrchestratorWorkflow`、`@ParallelAgent` |
| **评估器-优化器** | 迭代改进直到达标 | Evaluator + Optimizer 循环 |
| **多智能体顺序** | 写作→审阅等固定协作 | Alibaba `SequentialAgent` + `ReactAgent` |

### 代码示例

```java
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
```

```java
List<String> parallelResponse = new ParallelizationWorkflow(chatClient)
    .parallel(
        "Analyze how market changes will impact this stakeholder group.",
        List.of("Customers: ...", "Employees: ...", "Investors: ...", "Suppliers: ..."),
        4
    );
```

```java
RoutingWorkflow workflow = new RoutingWorkflow(chatClient);
Map<String, String> routes = Map.of(
    "billing", "You are a billing specialist...",
    "technical", "You are a technical support engineer...",
    "general", "You are a customer service representative..."
);
String response = workflow.route(input, routes);
```

```java
public class TravelOrchestratorWorkflow {
    private final ChatClient chatClient;

    public TravelPlan createPlan(TravelRequest request) {
        String taskList = chatClient.prompt()
            .user("Analyze this travel request and break it down into subtasks: " + request)
            .call().content();
        List<String> tasks = parseTasks(taskList);
        List<String> results = tasks.parallelStream()
            .map(task -> chatClient.prompt().user(task).call().content())
            .toList();
        String finalPlan = chatClient.prompt()
            .user("Synthesize into a comprehensive plan: " + String.join("\n", results))
            .call().content();
        return parsePlan(finalPlan);
    }
}
```

```java
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

blogAgent.invoke("Write about Spring AI");
```

### 面试常问

**问**：Spring AI 中链式、路由、并行与编排器工作流分别如何实现？

**答**：链式用 ChatClient 循环串联 Prompt；路由用 RoutingWorkflow 或 LlmRoutingAgent 按意图选专家；并行用 ParallelizationWorkflow 并发子任务；编排器先 LLM 分解任务再 parallelStream 执行后合成；Alibaba SequentialAgent 适合固定多 Agent 流水线。

### 关联知识点

- [Agent 架构与协同](Agent架构与协同.md)
- [Tool Calling 聚合多接口业务数据](Agent架构与协同.md)

---
## 多智能体监督与交接模式

> **模块**：Agent 工作流模式 | **标签**：Agent与对话 | **更新**：2026-05-28

### 核心概念

工具调用模式（Supervisor）：监督 Agent 将其他 Agent 封装为 Tool 调用，由监督者统一调度。

### 要点

- **工具调用模式（Supervisor）**：监督 Agent 将其他 Agent 封装为 Tool 调用，由监督者统一调度。
- **交接模式（Handoff）**：当前 Agent 通过 `transfer_to` 将控制权移交给更专业的 Agent，类似客服转技术岗。
- **适用**：复杂客服、多领域问答——前台 Agent 识别意图后 handoff 到领域专家。

### 代码示例

```java
Agent supportAgent = new HandoffAgent("support", chatModel);
Agent technicalAgent = new HandoffAgent("technical", chatModel);
supportAgent.registerHandoff("technical_issue", technicalAgent);
```

### 面试常问

**问**：多 Agent 系统中「工具调用模式」与「交接模式」有何区别？Handoff 如何实现？

**答**：工具调用模式（Supervisor）**：监督 Agent 将其他 Agent 封装为 Tool 调用，由监督者统一调度。；交接模式（Handoff）**：当前 Agent 通过 `transfer_to` 将控制权移交给更专业的 Agent，类似客服转技术岗。；适用**：复杂客服、多领域问答——前台 Agent 识别意图后 handoff 到领域专家。。

### 关联知识点

- [Agent 架构与协同](Agent架构与协同.md)
- [Agent 记忆体系](Agent记忆体系.md)

---
## IDE 分阶段顺序多智能体协同

> **模块**：Agent 工作流模式 | **标签**：Cursor, 顺序协同 | **更新**：2026-05-28

### 核心概念

Cursor 不支持多 Agent 真并行对话，采用**顺序协同流水线**：产品经理 → 架构师 → 后端 → 前端 → 测试，各阶段产出通过 `@文件名` 注入下一阶段上下文，人类充当总工（触发、审核、合并）。

### 要点

| 阶段 | 触发示例 | 上游引用 | 产出 |
| :--- | :--- | :--- | :--- |
| 需求 | `@product-manager 设计任务协作平台 PRD` | — | `requirements.md` |
| 方案 | `@architect 基于需求设计技术方案` | `@requirements.md` | `design.md`（Mermaid、DDL、API 表） |
| 后端 | `@backend-dev 实现创建项目接口` | `@design.md` | 路由、模型、单测 |
| 前端 | `@frontend-dev 实现项目列表页` | `@design.md` + 后端接口 | 页面组件 |
| 测试 | `@tester 生成 Playwright E2E` | 前后端代码 | `tests/e2e/` |

- **上下文传递**：架构师引用 `requirements.md`；工程师引用 `design.md`；前端可同时 `@backend/models` 保持接口一致。
- **Git 分支协同**：各角色产出可提交 `feature/backend`、`feature/frontend` 等分支，由人工 merge 解决冲突。
- **Composer 跨栈**：单条指令可同时改 `projects.py` 与 `Projects.tsx`，保证字段一致（类 Spring AI 并行工作流的一次性编排）。
- **对照 SequentialAgent**：IDE 流水线由人切换 `@角色`；运行时由 `outputKey` 链式传参（写作→审阅→润色）。

### 代码示例

```python
# 后端：FastAPI 创建项目（节选）
@router.post("/", response_model=schemas.ProjectOut)
def create_project(
    project_in: schemas.ProjectCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    db_project = models.Project(name=project_in.name, owner_id=current_user.id)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project
```

```tsx
// 前端：调用 /api/projects（节选）
const handleCreate = async (name: string) => {
  const res = await api.post('/projects', { name });
  setProjects([...projects, res.data]);
  setShowModal(false);
};
```

```typescript
// Playwright E2E（节选）
test('用户能够创建新项目', async ({ page }) => {
  await page.goto('/login');
  await page.fill('#email', 'test@example.com');
  await page.click('button[type="submit"]');
  await page.click('text=新建项目');
  await page.fill('input[name="name"]', '我的项目');
  await expect(page.locator('text=我的项目')).toBeVisible();
});
```

### 面试常问

**问**：IDE 里多智能体协同与 Spring AI SequentialAgent 有何异同？

**答**：相同点都是固定顺序、上游产出作下游输入。不同点：IDE 靠 `@文件` 与人工切换角色，无框架级 `outputKey`；SequentialAgent 由代码编排子 Agent 与终止条件，适合可重复自动化流水线。

### 关联知识点

- [基于 Cursor Rules 的领域角色智能体](Agent架构与协同.md)
- [SequentialAgent 与 LoopAgent 工作流](#sequentialagent-与-loopagent-工作流)
- [Cursor 多智能体开发最佳实践](其他.md)

---
## Human-in-the-Loop 工具审批（ReactAgent + HumanInTheLoopHook）

> **模块**：Agent 工作流模式 | **标签**：HITL, ReactAgent, 工具审批 | **更新**：2026-05-28

### 核心概念

Spring AI Alibaba 的 **Human-in-the-Loop（HITL）工具审批**采用两段式 HTTP：`invoke` 驱动 `ReactAgent` 直至 `HumanInTheLoopHook` 挂起或正常结束，`resume` 携带人工决策（APPROVED/EDITED/REJECTED）恢复图执行。审批结果通过 `RunnableConfig.HUMAN_FEEDBACK_METADATA_KEY` 传递，而非追加 `UserMessage`。

### 要点

**两段式 API（`/tool-feedback/*`）**

| 阶段 | HTTP | 作用 |
| :--- | :--- | :--- |
| Step1 | `GET /tool-feedback/invoke?threadId=&question=` | 驱动 Agent 直至中断或完成 |
| Step2 | `POST /tool-feedback/resume` | 携带人工决策恢复 Agent |

**返回 status 含义**

| status | 含义 |
| :--- | :--- |
| `INTERRUPTED_AWAITING_TOOL_APPROVAL` | 命中工具审批，等待 resume |
| `COMPLETED_WITHOUT_TOOL_INTERRUPT` | invoke 结束但未触发审批 |
| `COMPLETED` | resume 后 ReAct 跑完 |

**中断机制**

- 非 Controller 阻塞，而是 `ReactAgent` 编译为 `StateGraph`，`HumanInTheLoopHook#interrupt` 在 LLM 输出含 `toolCalls` 且工具名在 `approvalOn` 白名单内时构造 `InterruptionMetadata`（`ToolFeedback.result = null`），工具尚未执行。
- `MemorySaver` + `threadId` 持久化 checkpoint；`releaseThread(true)` 释放 HTTP 线程，图挂起。
- 中断时 messages 形态：`[UserMessage, AssistantMessage(toolCalls pending)]`。
- Demo 层 `interruptionByThread`（`ConcurrentHashMap`）暂存 `InterruptionMetadata` 供 resume 构造 feedback；生产应外置 Redis/DB。

**invoke 与 resume 差异**

| 维度 | invoke | resume |
| :--- | :--- | :--- |
| 用户输入 | 完整 `question` | `""`，不新增 UserMessage |
| RunnableConfig | 仅 `threadId` | `threadId` + `HUMAN_FEEDBACK_METADATA_KEY` |
| Hook interrupt | 无 feedback → 可能中断 | 有有效 feedback → 不二次中断 |
| Hook afterModel | 无 feedback → 空操作 | 消费 feedback，改写 toolCalls 或注入拒绝 TR |

**approvalOn 与多工具**

- 多次 `approvalOn` 仅向 `Map<String, ToolConfig>` 注册，**无审批优先级**。
- 一次 LLM 返回多个需审批 tool → **一次 interrupt**，`InterruptionMetadata` 含多条 `ToolFeedback`；顺序按 LLM `toolCalls` 顺序。
- 未在 `approvalOn` 的工具自动放行。

**三种决策**

| 决策 | afterModel 行为 | 是否执行 FunctionToolCallback | LLM 后续 |
| :--- | :--- | :--- | :--- |
| APPROVED | 保留原 toolCall | 是，原 arguments | 读真实 ToolResponse |
| EDITED | 同 id/name，替换 arguments | 是，人工 JSON | 读按新参执行的结果 |
| REJECTED | 保留 toolCall + 注入拒绝 ToolResponse | 否 | 读拒绝说明，可能改策略或再调工具 |

- **EDITED 必须传 `decision=EDITED`**，传 APPROVED 即使用户改了 JSON 也会按原参执行。
- Demo `buildFeedbackMetadata` 一次 resume 只有一个 `decision`，对**所有** pending 应用同一决策；不支持「批一个、拒一个」，需按 `toolCallId` 扩展。
- 默认 ReAct：**拒绝 ≠ 流程结束**；拒绝后 LLM 仍可能再调工具。合规「拒即停」需显式改造。

**messages 状态变迁（APPROVED 主路径）**

```
[] → [U1] invoke
→ [U1, A1★] LLM + toolCall，interrupt
→ [U1, A1★] resume("")，messages 不变
→ [U1, A1'] afterModel APPROVED（RemoveByHash 删旧 Assistant + 加新）
→ [U1, A1', TR1] Tool 执行
→ [U1, A1', TR1, A2] LLM 最终回复
```

- REJECTED：`[U1, A1★] → [U1, A1', TR_reject]`，工具未真实执行。
- 第二轮审批：Hook `getLastAssistantMessage` 规则——若 `AssistantMessage` 后紧跟 `ToolResponseMessage` 视为已处理，不再 interrupt。

**与 Graph interruptBefore HIL 的区别**

| 路径 | 机制 | 入口 |
| :--- | :--- | :--- |
| `/step1`、`/step2` | `StateGraph` + `interruptBefore` | `AlibabaGraphHumanLoopDemo` |
| `/tool-feedback/*` | `ReactAgent` + `HumanInTheLoopHook` | `AlibabaGraphHumanFeedbackToolDemo` |

二者都是 Human-in-the-loop，但中断点与恢复 API 不同，检查点 Bean 也相互隔离。

**技术债务**

1. `interruptionByThread` 进程内内存：多实例/重启丢失 → 外置 Redis。
2. 整批单一 decision：多工具需按 `toolCallId` 拆分决策。
3. REJECTED 后 ReAct 仍继续：合规场景可加「拒即停」策略。
4. EDITED 多工具共用 `editedArguments`：应按 tool 分别传参。

### 代码示例

```java
// AlibabaGraphHumanFeedbackAgentConfiguration
HumanInTheLoopHook.builder()
    .approvalOn(TOOL_SEND_EMAIL, ...)
    .approvalOn(TOOL_WRITE_FILE, ...)
    .build();

ReactAgent.builder()
    .tools(humanFeedbackToolCallbacks...)
    .saver(alibabaGraphHumanFeedbackMemorySaver)
    .hooks(humanInTheLoopHook)
    .releaseThread(true)
    .build();
```

```java
// AlibabaGraphHumanFeedbackToolDemo#resumeWithHumanDecision
humanFeedbackAgent.invokeAndGetOutput("", resumeConfig);
// resumeConfig: threadId + RunnableConfig.HUMAN_FEEDBACK_METADATA_KEY
```

### 面试常问

**问**：Spring AI ReactAgent 的 Human-in-the-Loop 工具审批如何实现 invoke/resume 两段式流程？

**答**：invoke 用 question + threadId 驱动 ReAct，Hook 在 approvalOn 白名单工具 pending 时 interrupt 并返回 `INTERRUPTED_AWAITING_TOOL_APPROVAL`；resume 传空串 question、相同 threadId，并将 APPROVED/EDITED/REJECTED 写入 `HUMAN_FEEDBACK_METADATA_KEY`，Hook afterModel 处理后再执行或拒绝工具，checkpoint 由 MemorySaver 按 threadId 恢复。

**问**：同一次 interrupt 两个需审批工具，Demo 能否「批准一个、拒绝一个」？

**答**：当前 Demo 不支持。一次 resume 只有一个 decision，`buildFeedbackMetadata` 对所有 pending 应用同一决策；框架 Hook 支持逐条 `FeedbackResult`，需扩展请求体按 `toolCallId` 分别决策。

**问**：REJECTED 后第二个 tool 还会自动执行吗？

**答**：同批 REJECTED 时两个都不会执行（整批同 decision）。若模型在拒绝后改调新 tool，会触发新的 interrupt/resume，与第一批无关。

### 关联知识点

- [MemorySaver 检查点与 HITL resume 续聊](Agent记忆体系.md)
- [ReactAgent 中 Tool Callback 与 HumanInTheLoopHook 协作](Agent架构与协同.md)
- [ReAct 与 Transformer 架构的区别](Agent架构与协同.md)

---
## FlowAgent 顺序多智能体编排

> **模块**：Agent 工作流模式 | **标签**：FlowAgent, 顺序编排 | **更新**：2026-05-29

### 核心概念

`FlowAgent` 维护有序智能体列表，按序调用各 Agent 的 `call(String input)`；上一 Agent 的**完整文本输出**直接作为下一 Agent 的输入，形成线性数据流。FlowAgent 本身也实现 `Agent` 接口，可嵌套组合。

### 要点

1. **定义步骤**：`FlowAgent.builder().agents(agent1, agent2, ...).build()` 注册有序序列。
2. **顺序执行**：用户输入进入后依次调用每个 Agent。
3. **结果传递**：默认无结构化转换，纯字符串透传；前后 Agent 的 Prompt 约定须清晰。
4. **终止**：最后一个 Agent 的输出即为 FlowAgent 最终输出。
5. **可组合**：FlowAgent 可作为子 Agent 被更大 FlowAgent 嵌套。

### 代码示例

```java
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

Agent extractor = Agent.builder()
    .chatModel(chatModel)
    .systemPrompt("从文本中提取3个核心关键词，用逗号分隔。")
    .build();

Agent summarizer = Agent.builder()
    .chatModel(chatModel)
    .systemPrompt("根据提供的关键词，写一段100字的摘要。")
    .build();

FlowAgent pipeline = FlowAgent.builder()
    .agents(extractor, summarizer)
    .build();
```

### 面试常问

**问**：FlowAgent 如何实现多智能体顺序执行并传递结果？

**答**：维护有序 Agent 列表，依次 call；上一 Agent 返回的完整文本直接作为下一 Agent 输入，无中间转换；全部执行完毕后返回最后一个 Agent 的输出。

**问**：多智能体协作时输入输出如何传递？

**答**：默认线性字符串透传，要求前一 Agent 输出格式能被后一 Agent 的 systemPrompt 理解；FlowAgent 本身也是 Agent，可嵌套形成更复杂流程。

### 关联知识点

- [SequentialAgent 与 LoopAgent 工作流](#sequentialagent-与-loopagent-工作流)
- [SimpleAgent 与 ReactAgent ReAct 规划模式](Agent架构与协同.md)

---
## HumanFeedbackToolCallback 装饰器式人工审批

> **模块**：Agent 工作流模式 | **标签**：HITL, HumanFeedback, 装饰器 | **更新**：2026-05-29

### 核心概念

`HumanFeedbackToolCallback` 通过**装饰器模式**包裹真实 `ToolCallback`，在工具执行前挂起对话、经 `HumanFeedbackService` 发送审批请求，阻塞等待批准/拒绝后再执行或返回拒绝消息。适用于转账、删数据等高风险操作。

### 要点

**工作流程**

1. 模型决定调用关键工具 → 装饰器拦截，不立即执行。
2. 经 `HumanFeedbackService` 向审批系统发送工具名与参数，携带唯一 `feedbackId`。
3. 对话阻塞等待审批结果（批准 / 拒绝 / 可附带修改意见）。
4. **批准**：调用被包装的真实 ToolCallback，结果回注模型。
5. **拒绝**：返回预设拒绝消息，模型据此生成回复。

**与 HumanInTheLoopHook 的区别**：`HumanFeedbackToolCallback` 是 Tool 层装饰器；`HumanInTheLoopHook` 是 ReactAgent 图节点级 interrupt/resume，二者可组合使用。

### 代码示例

```java
@Component
class PaymentTool {
    @Tool(description = "执行转账操作")
    public String transfer(String fromAccount, String toAccount, double amount) {
        return "转账成功";
    }
}

ToolCallback rawCallback = MethodToolCallback.builder()
    .toolObject(new PaymentTool())
    .methodName("transfer")
    .build();

ToolCallback approvedCallback = HumanFeedbackToolCallback.builder()
    .toolCallback(rawCallback)
    .humanFeedbackService(feedbackService)
    .build();

Agent agent = Agent.builder()
    .chatModel(chatModel)
    .tools(List.of(approvedCallback))
    .build();
```

### 面试常问

**问**：关键工具调用如何加入人工审批？HumanFeedbackToolCallback 如何工作？

**答**：用 HumanFeedbackToolCallback 装饰真实 ToolCallback；模型触发调用时挂起并发送审批，批准则执行原工具，拒绝则返回拒绝消息给模型；适合转账、删数据等高风险场景。

### 关联知识点

- [Human-in-the-Loop 工具审批（ReactAgent + HumanInTheLoopHook）](#human-in-the-loop-工具审批reactagent--humanintheloophook)
- [工具调用错误恢复与 Fallback 策略](Agent架构与协同.md)

---
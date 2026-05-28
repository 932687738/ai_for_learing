<!-- 模块：Agent 工作流模式 | 最后更新于 2026-05-28 -->

# Agent 工作流模式

> 串行/循环/路由/并行 Agent 与 CoT/ToT 推理。

## 目录

- [SequentialAgent 与 LoopAgent 工作流](#sequentialagent-与-loopagent-工作流)
- [共享 ChatMemory 的多 Agent 协作](#共享-chatmemory-的多-agent-协作)
- [Orchestrator 子任务拆解与 CoT/ToT 推理](#orchestrator-子任务拆解与-cottot-推理)
- [Spring AI 常见工作流模式](#spring-ai-常见工作流模式)
- [多智能体监督与交接模式](#多智能体监督与交接模式)
- [IDE 分阶段顺序多智能体协同](#ide-分阶段顺序多智能体协同)

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

Spring AI / Alibaba 生态中有哪些典型 Agent 工作流模式？各自适用场景是什么？

### 要点

| 模式 | 核心用途 | 典型组件 |
| :--- | :--- | :--- |
| **链式 (Chain)** | 固定顺序流水线 | `ChainWorkflow`、顺序 Prompt 列表 |
| **路由 (Routing)** | 按意图分发到专业 Agent | `LlmRoutingAgent` |
| **并行 (Parallelization)** | 并发独立子任务 | `ParallelizationWorkflow` |
| **编排器-工作者** | 动态拆解 + 并行执行 | `@ParallelAgent`、`@SubAgent` |
| **评估器-优化器** | 迭代改进直到达标 | Evaluator + Optimizer 循环 |

### 代码示例

```java
public class ChainWorkflow {
    private final ChatClient client;
    private final List<String> prompts;

    public String execute(String input) {
        String result = input;
        for (String prompt : prompts) {
            result = client.prompt(prompt + "\n" + result).call().content();
        }
        return result;
    }
}
```

```java
LlmRoutingAgent router = LlmRoutingAgent.builder()
    .name("router")
    .model(chatModel)
    .subAgents(List.of(weatherAgent, newsAgent, financeAgent))
    .build();

router.invoke("What's the weather in London?");
```

```java
ParallelizationWorkflow workflow = new ParallelizationWorkflow(chatClient);
List<String> tasks = List.of("Impact on customers", "Impact on employees", "Impact on suppliers");
List<String> results = workflow.parallel(
    "Analyze how market change affects stakeholders",
    tasks,
    maxConcurrency = 4
);
```

```java
@ParallelAgent
public class Orchestrator {
    @SubAgent
    public String researchAgent(String topic) { ... }

    @SubAgent
    public String writerAgent(String outline) { ... }

    @ParallelTask
    public List<String> gatherData(String[] sources) { ... }
}
```

```java
public class IterativeRefinement {
    public String refine(String initialDraft) {
        String current = initialDraft;
        for (int i = 0; i < maxIterations; i++) {
            String feedback = evaluator.evaluate(current);
            if (isAcceptable(feedback)) break;
            current = optimizer.improve(current, feedback);
        }
        return current;
    }
}
```

### 面试常问

**问**：Spring AI / Alibaba 生态中有哪些典型 Agent 工作流模式？各自适用场景是什么？

**答**：核心用途 :--- 固定顺序流水线 按意图分发到专业 Agent 并发独立子任务 动态拆解 + 并行执行 迭代改进直到达标

### 关联知识点

- [Agent 架构与协同](Agent架构与协同.md)
- [Agent 记忆体系](Agent记忆体系.md)

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
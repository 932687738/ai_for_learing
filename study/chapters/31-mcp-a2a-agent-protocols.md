# 第 31 课：MCP 与 A2A：工具协议和 Agent 协作协议

## 0. 本课定位

本课补齐 MCP 和 A2A。第 11 课讲工具调用与 Agent，本课进一步讲协议层：MCP 解决模型 / Agent 如何连接工具、资源和提示模板；A2A 解决不同 Agent 如何发现、通信、委派和协作。

## 1. 学习目标

完成本课后，你应该能：

1. 解释 MCP 的 tools、resources、prompts。
2. 解释 A2A 的 Agent Card、Task、Message、Artifact。
3. 区分 MCP 与 A2A 的职责边界。
4. 设计一个 Java / Python MCP server 的工具清单。
5. 设计两个 Agent 之间通过 A2A 协作的任务协议。

## 2. MCP：模型连接工具和上下文

MCP 可以理解为 AI 应用的标准化外设接口。

```text
AI client / Agent
  -> MCP client
  -> MCP server
     -> tools
     -> resources
     -> prompts
```

例子：

- tools：查询订单、搜索文档、运行测试。
- resources：代码文件、设计文档、数据库 schema。
- prompts：团队固定的问题分析模板、代码评审模板。

## 3. A2A：Agent 连接 Agent

A2A 的核心不是“调用一个函数”，而是“把任务交给另一个独立 Agent 系统”。

```text
Client Agent
  -> discover Agent Card
  -> send Message
  -> create / continue Task
  -> receive Artifact / status updates
```

核心对象：

- Agent Card：描述 Agent 身份、能力、端点和安全方案。
- Task：一次可追踪的任务。
- Message：Agent 间交流内容。
- Artifact：任务产物，如文件、报告、结构化数据。

## 4. MCP 与 A2A 的边界

| 问题 | 适合 MCP | 适合 A2A |
| --- | --- | --- |
| 当前 Agent 需要查数据库 | 是 | 否 |
| 当前 Agent 需要调用内部 API | 是 | 否 |
| 当前 Agent 需要委派给另一个专门 Agent | 否 | 是 |
| 需要暴露文件、文档、prompt 模板 | 是 | 否 |
| 需要跨厂商 Agent 协作 | 否 | 是 |

工程上可以组合：一个 Agent 通过 A2A 接收任务，同时内部通过 MCP 调用工具。

## 5. 安全要求

- 不在 Agent Card 中写明文密钥。
- 工具执行必须做身份、权限、参数校验。
- 写操作必须有审批或补偿机制。
- MCP server 要最小权限暴露。
- A2A 任务要有审计日志、超时、取消和失败状态。

## 6. 实践任务

1. 为企业知识库设计一个 MCP server 工具清单。
2. 为“合同审查 Agent”和“法务问答 Agent”设计 A2A Agent Card 摘要。
3. 画出 MCP + A2A 组合架构。
4. 写出 5 条协议安全检查项。

## 7. 阶段验收标准

- 能解释 MCP 不是 Agent，A2A 也不是工具调用。
- 能设计 MCP 工具、资源和 prompts。
- 能设计 A2A Agent Card 和任务流。

## 8. 本课使用的信息源

- MCP 官方仓库：https://github.com/modelcontextprotocol/modelcontextprotocol
- MCP 官方文档：https://modelcontextprotocol.io/
- A2A Specification：https://google-a2a.github.io/A2A/specification/
- A2A GitHub：https://github.com/google/A2A

## 9. 问答记录

暂无。

## 10. 外部补充

暂无。

## 11. 结构化补充（整改）

### 核心讲解

- MCP 解决“Agent 如何安全使用工具和上下文”，A2A 解决“Agent 与 Agent 如何协作”。
- 两者是互补关系：A2A 负责任务协同，MCP 负责能力接入。
- 协议工程要先定义契约，再实现工具与流程。

### 拓展阅读

- MCP Docs: https://modelcontextprotocol.io/
- A2A Spec: https://google-a2a.github.io/A2A/specification/

### 问答记录

- 2026-05-12：完成模板统一，下一步补协议报文样例。

### 外部补充

- 暂无（可补充你们内部 Agent 协作场景）。

### 本课掌握检查

- 你能否区分“调用工具”和“委派 Agent”两类场景？
- 你能否写出一个最小 MCP tool schema 与 A2A task 流程？

### 下一课前置条件

- 输出一页协议设计稿：对象模型、鉴权、幂等、错误处理、审计字段。

## 12. 协议落地样例（整改新增）

### MCP Tool Schema（最小示例）

```json
{
  "name": "search_policy_docs",
  "description": "搜索制度文档并返回可引用片段",
  "inputSchema": {
    "type": "object",
    "properties": {
      "query": { "type": "string", "minLength": 2 },
      "tenantId": { "type": "string" },
      "topK": { "type": "integer", "minimum": 1, "maximum": 20 }
    },
    "required": ["query", "tenantId"]
  }
}
```

### A2A Task（最小示例）

```json
{
  "taskId": "task-20260512-001",
  "fromAgent": "contract-review-agent",
  "toAgent": "legal-qa-agent",
  "intent": "clause-risk-check",
  "payload": {
    "contractId": "C-1024",
    "tenantId": "tenant-a"
  },
  "traceId": "trace-abc-001"
}
```

### 错误码与幂等建议

| 错误码 | 含义 | 处理策略 |
| --- | --- | --- |
| `AUTH_401` | 鉴权失败 | 立即拒绝并审计 |
| `PERM_403` | 权限不足 | 不重试，返回最小错误信息 |
| `RATE_429` | 限流触发 | 指数退避重试，保留 `traceId` |
| `TIMEOUT_504` | 下游超时 | 可重试（幂等 key 必填） |
| `TOOL_422` | 参数校验失败 | 不重试，返回字段级错误 |

- 写操作请求必须包含 `idempotencyKey`，服务端持久化 `requestHash + result`，重复请求直接返回历史结果。

## 回归评测记录（2026-05-12）

- run_id: `baseline-2026-05-12`
- case: `E31-protocol-schema`
- result: `PASS`
- 记录：`study/projects/27-36-min-eval-regression-run-2026-05-12.md`

## 可运行示例（Java，整改新增）

```java
public class ProtocolValidationDemo {
    static class Task {
        String taskId, fromAgent, toAgent, traceId;
        Task(String taskId, String fromAgent, String toAgent, String traceId) {
            this.taskId = taskId; this.fromAgent = fromAgent; this.toAgent = toAgent; this.traceId = traceId;
        }
    }

    static boolean isValid(Task t) {
        return notBlank(t.taskId) && notBlank(t.fromAgent) && notBlank(t.toAgent) && notBlank(t.traceId);
    }

    static boolean notBlank(String s) {
        return s != null && s.trim().length() > 0;
    }

    public static void main(String[] args) {
        Task ok = new Task("task-1", "agent-a", "agent-b", "trace-1");
        Task bad = new Task("", "agent-a", "agent-b", null);
        System.out.println(isValid(ok));  // true
        System.out.println(isValid(bad)); // false
    }
}
```

## 学习状态

- 状态：未开始（内容已就绪）
- 最近更新：2026-05-12
- 进入下一课条件：学员明确回复“这节课已经学会”

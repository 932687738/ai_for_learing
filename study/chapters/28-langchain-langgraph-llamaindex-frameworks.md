# 第 28 课：LangChain、LangGraph 与 LlamaIndex 框架对比

## 0. 本课定位

本课补齐 LangChain、LangGraph、LlamaIndex 三类框架在现代 AI 应用中的分工。第 13 课已经讲 LangChain4j，本课重点从 Python / TypeScript 生态理解框架思想，并反推 Java 工程如何借鉴。

## 1. 学习目标

完成本课后，你应该能：

1. 区分 LangChain、LangGraph、LlamaIndex 的核心定位。
2. 判断 RAG、Agent、Workflow 场景该选哪类框架。
3. 理解 stateful agent、graph workflow、checkpoint、human-in-the-loop。
4. 解释 LlamaIndex 的 Document、Node、Index、Query Engine、Agent。
5. 将 Python 生态设计思想映射到 Java / Spring AI / LangChain4j。

## 2. 核心概念

| 框架 | 主要定位 | 适合场景 |
| --- | --- | --- |
| LangChain | LLM 应用组件和高层 agent 抽象 | 快速串接模型、提示词、工具、检索 |
| LangGraph | 有状态、可控、长运行 agent 编排 | 多步骤、多 Agent、人工审批、可恢复工作流 |
| LlamaIndex | 面向数据的 context augmentation 框架 | 文档摄取、索引、RAG、数据 Agent |
| LangChain4j | Java 侧 LLM 应用框架 | Spring Boot / 企业 Java 系统接入 AI |

## 3. LangGraph 为什么重要

传统 agent loop 常见问题是控制流隐式、状态不清楚、失败后难恢复。LangGraph 把 agent 工作流建模成图：

```text
START
  -> classify_intent
  -> retrieve_context
  -> decide_tool_or_answer
  -> human_approval?
  -> execute_tool
  -> final_answer
  -> END
```

这种图结构适合企业场景，因为它能显式表达：

- 哪些节点可以调用模型。
- 哪些节点只能执行确定性代码。
- 哪些分支需要人工确认。
- 哪些状态要持久化和恢复。
- 哪些步骤要记录审计日志。

## 4. LlamaIndex 为什么重要

LlamaIndex 的强项是把企业数据变成模型可用上下文。它关注：

- 文档加载与解析。
- chunk / node 的组织。
- index 构建。
- query engine 和 retriever。
- RAG pipeline 作为 Agent 的一个工具。

如果你的项目难点主要在“数据怎么进来、怎么切、怎么索引、怎么查”，优先研究 LlamaIndex 思路；如果难点主要在“多步骤任务怎么控制”，优先研究 LangGraph 思路。

## 5. Java 工程映射

Java 项目不一定直接使用 Python 框架，但可以吸收其架构：

- 用 Spring Batch / Spring Integration 承接文档摄取流水线。
- 用 Spring AI VectorStore 或 LangChain4j EmbeddingStore 承接检索。
- 用状态机、工作流引擎或显式 service 编排模拟 LangGraph 控制流。
- 用数据库记录 Agent run、node state、tool call、approval 和 eval 结果。

## 6. 实践任务

1. 画出一个 6 节点 LangGraph 风格客服 Agent。
2. 将同一流程改写成 Java service 编排图。
3. 列出哪些节点允许调用模型，哪些节点必须是确定性代码。
4. 为 RAG 摄取流程设计 LlamaIndex 风格的 Document / Node / Index 映射。

## 7. 阶段验收标准

- 能解释 LangChain、LangGraph、LlamaIndex 的区别。
- 能判断框架是否解决当前问题，而不是为框架而框架。
- 能把框架思想落到 Java / Python 项目结构中。

## 8. 本课使用的信息源

- LangGraph 官方文档：https://docs.langchain.com/langgraph
- LangChain LangGraph 产品页：https://www.langchain.com/langgraph
- LlamaIndex 官方文档：https://docs.llamaindex.ai/
- LlamaIndex RAG 入门：https://docs.llamaindex.ai/en/stable/understanding/rag/

## 9. 问答记录

暂无。

## 10. 外部补充

暂无。

## 11. 结构化补充（整改）

### 核心讲解

- LangChain 侧重组件复用，LangGraph 侧重状态化工作流，LlamaIndex 侧重数据索引与检索。
- 选型原则是“问题驱动”，不是“框架驱动”。
- Java 项目可借鉴其设计思想，在应用层编排、在基础设施层适配。

### 拓展阅读

- LangChain: https://python.langchain.com/
- LangGraph: https://docs.langchain.com/langgraph
- LlamaIndex: https://docs.llamaindex.ai/

### 问答记录

- 2026-05-12：补齐结构化小节与学习闭环检查项。

### 外部补充

- 暂无（可补充你的项目框架选型对比结论）。

### 本课掌握检查

- 你能否说明“什么时候该用 LangGraph，而不是普通链式调用”？
- 你能否把一个检索问答流程映射到 Java 分层架构？

### 下一课前置条件

- 输出一份框架选型结论：场景、约束、选型、风险、验证方式。

## 回归评测记录（2026-05-12）

- run_id: `baseline-2026-05-12`
- case: `E28-framework-select`
- result: `PASS`
- 记录：`study/projects/27-36-min-eval-regression-run-2026-05-12.md`

## 可运行示例（Java，整改新增）

```java
public class FrameworkSelectorDemo {
    public static String select(boolean needWorkflowState, boolean dataIndexHeavy, boolean simpleChain) {
        if (needWorkflowState) return "LangGraph-like";
        if (dataIndexHeavy) return "LlamaIndex-like";
        if (simpleChain) return "LangChain-like";
        return "Hybrid";
    }

    public static void main(String[] args) {
        System.out.println(select(true, false, false));   // LangGraph-like
        System.out.println(select(false, true, false));   // LlamaIndex-like
        System.out.println(select(false, false, true));   // LangChain-like
        System.out.println(select(false, false, false));  // Hybrid
    }
}
```

## 学习状态

- 状态：未开始（内容已就绪）
- 最近更新：2026-05-12
- 进入下一课条件：学员明确回复“这节课已经学会”

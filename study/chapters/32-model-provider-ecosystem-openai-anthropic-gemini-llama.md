# 第 32 课：OpenAI、Anthropic、Claude、Codex、Gemini 与 Llama 生态

## 0. 本课定位

本课补齐主流模型和工具生态：OpenAI、Anthropic、Claude、Claude Code、Codex、Google DeepMind、Gemini、Meta Llama。目标不是追逐型号，而是建立选型框架。

## 1. 学习目标

完成本课后，你应该能：

1. 从能力、成本、延迟、上下文、工具调用、多模态、安全和部署方式选模型。
2. 区分闭源 API 模型、开放权重模型、本地模型和 coding agent 产品。
3. 解释 Claude、Claude Code、Codex、Gemini、Llama 在工程中的常见角色。
4. 设计模型抽象层，避免业务代码绑定单一厂商。
5. 建立模型升级和回退机制。

## 2. 生态定位

| 生态 | 常见角色 | 关注点 |
| --- | --- | --- |
| OpenAI | 通用模型、Responses API、工具、Codex、Realtime、Evals | 工具链完整、API 生态、评测和 coding agent |
| Anthropic / Claude | 长上下文、代码、Claude Code、MCP 生态 | 安全边界、代码任务、Agent 工具链 |
| Google DeepMind / Gemini | 多模态、搜索 grounding、Google 生态 | 多模态、搜索、Workspace / Cloud 集成 |
| Meta Llama | 开放权重、本地部署、微调、安全模型 | 私有化、成本控制、可控部署 |
| Hermes | 开放模型系列和 agentic 能力实验 | 函数调用、长上下文、多轮对话 |

## 3. 选型维度

```text
任务类型
  -> 文本 / 代码 / 图像 / 音频 / 视频
数据敏感性
  -> API / 私有化 / 混合
延迟要求
  -> 批处理 / 在线 / 实时
成本约束
  -> 高质量 / 高吞吐 / 低成本
工程能力
  -> SDK / 工具调用 / RAG / eval / 监控
合规要求
  -> 数据驻留 / 审计 / 权限 / 日志
```

## 4. Java 项目中的模型抽象

建议业务代码只依赖内部接口：

```java
public interface AiChatClient {
    AiAnswer chat(AiRequest request);
    Stream<AiChunk> stream(AiRequest request);
}
```

实现层再适配 OpenAI、Anthropic、Gemini、Llama 本地服务或 Spring AI `ChatModel`。这样模型切换、A/B 测试、降级和多模型路由不会污染业务逻辑。

## 5. 常见误区

1. 只看榜单，不看业务 eval。
2. 把 ChatGPT / Claude 网页体验等同于 API 行为。
3. 忽略模型退役、版本变动和上下文窗口差异。
4. 没有 fallback，单一供应商失败导致业务不可用。
5. 开放权重模型私有化后忽略推理成本和运维难度。

## 6. 实践任务

1. 为客服系统设计主模型、备用模型和低成本模型路由。
2. 比较 API 模型和本地 Llama 部署在数据合规上的差异。
3. 设计模型升级流程：灰度、eval、回滚、日志。
4. 说明 coding agent 与普通 chat model API 的区别。

## 7. 阶段验收标准

- 能建立模型选型表，而不是只说“哪个模型最好”。
- 能设计多厂商适配层。
- 能把模型升级纳入 eval 和发布流程。

## 8. 本课使用的信息源

- OpenAI Models：https://platform.openai.com/docs/models
- Anthropic Models List：https://docs.claude.com/en/api/models-list
- Google Gemini Models：https://ai.google.dev/models/gemini
- Meta Llama Hugging Face：https://huggingface.co/meta-llama

## 9. 问答记录

暂无。

## 10. 外部补充

暂无。

## 11. 结构化补充（整改）

### 核心讲解

- 模型选型是系统工程，必须在能力、成本、延迟、合规之间平衡。
- 业务代码应依赖统一抽象接口，避免被单一厂商 API 绑死。
- 多模型路由与回退策略是生产可用性的基础能力。

### 拓展阅读

- OpenAI Models: https://platform.openai.com/docs/models
- Anthropic Models: https://docs.claude.com/en/api/models-list
- Gemini Models: https://ai.google.dev/models/gemini

### 问答记录

- 2026-05-12：补统一结构，后续补“模型选型评分卡”模板。

### 外部补充

- 暂无（可补充你当前生产模型与备选模型名单）。

### 本课掌握检查

- 你能否给出一个多模型路由策略（主模型/降级模型/备用模型）？
- 你能否说明一次模型升级如何灰度、评测和回滚？

### 下一课前置条件

- 完成一份模型选型表并给出权重和量化评分。

## 12. 模型选型评分卡（整改新增）

### 评分维度模板

| 维度 | 权重(0-1) | 评分(1-5) | 加权分 |
| --- | --- | --- | --- |
| 任务效果（正确率/遵循度） | 0.30 |  |  |
| 成本（输入/输出 token） | 0.20 |  |  |
| 延迟（P95） | 0.20 |  |  |
| 安全与合规能力 | 0.15 |  |  |
| 工程可集成性（SDK/Tool/监控） | 0.15 |  |  |

> 总分 = `sum(权重 * 评分)`，上线候选模型建议总分 >= 3.5。

### 路由策略模板（主模型 + 降级模型）

```text
if (task == "code_generation" && latency_budget_ms > 5000) {
  use primary_model;
} else if (latency_budget_ms <= 2000 || traffic_peak) {
  use fast_model;
} else if (primary_model_error_rate > threshold) {
  fallback to backup_model;
}
```

### 升级发布门禁（最小）

1. 新模型离线 Eval 总分 >= 基线模型。
2. 线上灰度 5%-10%，错误率和成本不劣化。
3. 任一关键指标劣化超过阈值时自动回滚。

## 回归评测记录（2026-05-12）

- run_id: `baseline-2026-05-12`
- case: `E32-model-routing`
- result: `PASS`
- 记录：`study/projects/27-36-min-eval-regression-run-2026-05-12.md`

## 可运行示例（Java，整改新增）

```java
public class ModelRouterDemo {
    static String route(boolean peak, boolean highQuality, boolean primaryDown) {
        if (primaryDown) return "backup-model";
        if (peak) return "fast-model";
        if (highQuality) return "primary-model";
        return "balanced-model";
    }

    public static void main(String[] args) {
        System.out.println(route(false, true, false)); // primary-model
        System.out.println(route(true, true, false));  // fast-model
        System.out.println(route(false, true, true));  // backup-model
    }
}
```

## 学习状态

- 状态：未开始（内容已就绪）
- 最近更新：2026-05-12
- 进入下一课条件：学员明确回复“这节课已经学会”

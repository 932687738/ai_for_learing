# 第 30 课：模型评测、Eval 与 Benchmark 工程

## 0. 本课定位

本课补齐模型评测、eval、benchmark。第 5 课讲传统机器学习评估，第 14 课讲 Java AI 工程化评估，本课专门讲 LLM / RAG / Agent / Tool / 多模态系统的评测工程。

## 1. 学习目标

完成本课后，你应该能：

1. 区分 benchmark、offline eval、online eval、human eval。
2. 为 Prompt、RAG、Tool Calling、Agent、多模态任务设计评测集。
3. 理解 grader、LLM-as-judge、reference answer、rubric 的边界。
4. 建立模型升级、提示词改动、知识库更新后的回归测试。
5. 在 Java / Python 项目中保存 eval case、run、score 和错误分析。

## 2. 核心概念

| 概念 | 含义 |
| --- | --- |
| Benchmark | 通用榜单或公开测试集，用于横向比较 |
| Eval | 面向自己业务目标的测试任务集合 |
| Grader | 自动评分器，可以是规则、相似度、代码执行或模型评分 |
| Golden Set | 人工确认过的高质量评测样本 |
| Regression Eval | 防止提示词、模型、RAG 数据改动导致质量倒退 |
| Human Eval | 人工专家评分，适合高风险和开放式任务 |

## 3. LLM 应用评测层次

```text
输入理解
检索召回
上下文组装
工具调用
答案正确性
答案安全性
引用可靠性
成本与延迟
用户满意度
```

不要只看最终答案。RAG 答错可能是检索没召回，也可能是召回正确但上下文太长，还可能是模型忽略证据。

## 4. Java / Python Eval 数据模型

```json
{
  "id": "rag-policy-001",
  "input": "员工年假最多可以累计几年？",
  "expected": "根据公司制度回答具体累计规则，并引用制度章节。",
  "tags": ["rag", "policy", "citation"],
  "rubric": {
    "grounded": 0.4,
    "correct": 0.4,
    "citation": 0.2
  }
}
```

工程表建议：

- `eval_case`
- `eval_run`
- `eval_sample_result`
- `eval_error_analysis`
- `prompt_version`
- `model_version`
- `knowledge_base_version`

## 5. 常见误区

1. 只看公开 benchmark，不做业务 eval。
2. 只评最终回答，不评检索和工具调用过程。
3. 过度相信 LLM-as-judge，没有抽样人工复核。
4. 模型升级不跑回归测试。
5. 只记录分数，不记录失败样例和原因。

## 6. 实践任务

1. 为第 10 课 RAG 系统设计 30 条 eval case。
2. 写出一个规则评分器：检查答案是否包含引用。
3. 设计一个 Tool Calling eval：判断模型是否调用了正确工具。
4. 设计一次模型升级 A/B 评测流程。

## 7. 阶段验收标准

- 能独立设计 LLM 应用 eval。
- 能解释 benchmark 分数不能直接代表业务可用性。
- 能把 eval 纳入 CI、发布和模型升级流程。

## 8. 本课使用的信息源

- OpenAI Evals API：https://platform.openai.com/docs/api-reference/evals
- OpenAI Evals 指南：https://platform.openai.com/docs/guides/evals
- OpenAI Graders：https://platform.openai.com/docs/guides/graders/
- OpenAI Cookbook Evals：https://cookbook.openai.com/topic/evals

## 9. 问答记录

暂无。

## 10. 外部补充

暂无。

## 11. 结构化补充（整改）

### 核心讲解

- Benchmark 用于横向比较，Eval 用于业务可用性验证，两者不能互相替代。
- Eval 必须覆盖输入、过程、输出和失败样例，不只看最终答案。
- 评测要进入 CI/CD，成为模型升级与发布门禁。

### 拓展阅读

- OpenAI Evals: https://platform.openai.com/docs/guides/evals
- OpenAI Graders: https://platform.openai.com/docs/guides/graders/

### 问答记录

- 2026-05-12：补齐学习闭环结构，后续补可运行评测脚本模板。

### 外部补充

- 回归执行说明：`study/projects/27-36-min-eval-regression.md`

### 本课掌握检查

- 你能否设计一个最小 eval 数据集并定义评分 rubric？
- 你能否说明模型升级前后的回归门禁条件？

### 下一课前置条件

- 至少落地 10 条业务 eval case，并完成一次基线评测。

## 12. 跨章节边界（去重指引）

- 本课主讲：Eval/Benchmark 方法论与工程门禁。
- 第 14 课主讲：Java 工程化落地，本课提供评测治理能力并由第 14 课承接上线流程。
- 第 29 课主讲：企业搜索场景评测，本课提供通用评测框架。
- 第 33 课主讲：安全测试，本课仅定义安全评测应纳入总回归。

## 回归评测记录（2026-05-12）

- run_id: `baseline-2026-05-12`
- case: `E30-eval-rubric`
- result: `PASS`
- 记录：`study/projects/27-36-min-eval-regression-run-2026-05-12.md`

## 可运行示例（Java，整改新增）

```java
public class EvalRubricDemo {
    public static double score(double grounded, double correct, double citation) {
        // rubric: grounded 0.4, correct 0.4, citation 0.2
        return grounded * 0.4 + correct * 0.4 + citation * 0.2;
    }

    public static void main(String[] args) {
        double total = score(0.9, 0.8, 1.0);
        System.out.println("Eval score = " + total); // 0.88
        System.out.println("Pass = " + (total >= 0.8));
    }
}
```

## 学习状态

- 状态：未开始（内容已就绪）
- 最近更新：2026-05-12
- 进入下一课条件：学员明确回复“这节课已经学会”

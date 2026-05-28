# Ragas 框架简介

Ragas 是一个开源的 Python 框架，专门用于**评估和优化检索增强生成（RAG）应用**。它将复杂 AI 系统的性能评估从主观判断转化为数据驱动的科学流程，支持无参考（reference‑free）评估，即无需人工标注标准答案。

## 🎯 核心价值

- **无参考评估**：直接使用 LLM 作为评审员，自动评估 RAG 系统的各个环节。
- **快速定位瓶颈**：区分是检索环节（Retrieval）还是生成环节（Generation）的问题。
- **合成测试集生成**：根据自有文档库自动生成问答对，减少人工标注成本。

## 📊 评估指标体系

| 环节 | 指标 | 说明 |
|------|------|------|
| 检索器 | 上下文精度 (Context Precision) | 检索回文档的信噪比，衡量结果是否精准。 |
| 检索器 | 上下文召回率 (Context Recall) | 关键信息覆盖率，判断是否遗漏重要内容。 |
| 生成器 | 忠实度 (Faithfulness) | 回答是否完全基于检索到的上下文，**减少幻觉**。 |
| 生成器 | 答案相关性 (Answer Relevancy) | 回答是否切题、简洁。 |
| 端到端 | 答案正确性 (Answer Correctness) | 与标准答案（若有）比对，评估最终效果。 |

## 🚀 快速上手（含代码示例）

### 1. 安装

```bash
pip install ragas
2. 准备测试数据
构造包含 question（问题）、answer（RAG 回答）、contexts（检索到的上下文列表）的数据。

python
from datasets import Dataset

data = {
    "question": ["什么是 RAG？", "Ragas 框架能做什么？"],
    "answer": [
        "RAG 是检索增强生成，结合检索和生成模型。",
        "Ragas 可以评估 RAG 系统的检索和生成质量。"
    ],
    "contexts": [
        ["RAG 结合了信息检索和文本生成技术。"],
        ["Ragas 提供忠实度、答案相关性等评估指标。"]
    ]
}

dataset = Dataset.from_dict(data)
3. 选择评估指标并运行评测
python
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision

result = evaluate(
    dataset,
    metrics=[faithfulness, answer_relevancy, context_precision]
)

print(result)
输出将显示每个指标的平均得分（0~1之间），分数越高表示性能越好。

4. 分析结果
根据指标得分定位问题：

如果 faithfulness 低 → 生成模型产生幻觉，需优化 prompt 或检索内容。

如果 context_precision 低 → 检索器带回过多噪音，需调整检索策略。

如果 answer_relevancy 低 → 回答偏离问题，可改进生成提示词。

🔧 进阶功能
合成测试集生成：使用 from ragas.testset import TestsetGenerator 根据您的文档自动生成问答对。

集成 LangChain / LlamaIndex：无缝嵌入现有 RAG 流水线。

生产环境监控：通过 Ragas Cloud 实现持续评估。
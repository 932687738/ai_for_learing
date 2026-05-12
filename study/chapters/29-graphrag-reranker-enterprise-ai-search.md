# 第 29 课：GraphRAG、Reranker 与企业 AI 搜索

## 0. 本课定位

本课在第 9 课向量数据库和第 10 课 RAG 基础上继续深入，补齐 GraphRAG、reranker、hybrid search、enterprise AI search 等企业级检索增强能力。

## 1. 学习目标

完成本课后，你应该能：

1. 解释普通 RAG、Hybrid Search、GraphRAG 的区别。
2. 说明 embedding、vector database、reranker 在检索链路中的位置。
3. 设计带权限过滤、引用、重排、缓存和评测的企业 AI 搜索系统。
4. 判断什么时候需要 GraphRAG，什么时候普通 RAG 足够。
5. 用 Java / Python 描述检索服务的模块划分。

## 2. 核心概念

| 概念 | 作用 | 典型风险 |
| --- | --- | --- |
| Embedding | 把文本转成向量 | 语义相近但事实不匹配 |
| Vector Database | 存储和近似检索向量 | 权限过滤、召回不足 |
| BM25 / Keyword Search | 精确词项匹配 | 同义表达召回差 |
| Hybrid Search | 融合向量和关键词 | 权重调参复杂 |
| Reranker | 对候选片段重新排序 | 成本和延迟增加 |
| GraphRAG | 利用实体、关系、社区摘要增强问答 | 构图成本、增量更新复杂 |

## 3. GraphRAG 的基本思路

普通 RAG 通常检索 chunk。GraphRAG 会额外抽取实体和关系，形成知识图谱或社区摘要。

```text
documents
  -> chunks
  -> entities / relations
  -> graph communities
  -> summaries
  -> local query / global query
  -> grounded answer
```

适用场景：

- 文档之间关系复杂。
- 用户问题是跨文档、跨实体、跨组织的综合问题。
- 需要全局摘要、主题发现、实体关系解释。

不适用场景：

- 数据量很小。
- 问题通常能由单个文档片段回答。
- 数据更新频繁但没有构图增量机制。

## 4. 企业 AI 搜索推荐架构

```text
用户问题
  -> 权限上下文
  -> 查询改写
  -> hybrid retrieval
  -> metadata filter
  -> rerank
  -> context packing
  -> LLM answer
  -> citation check
  -> eval logging
```

关键工程要求：

- 权限过滤必须发生在答案生成前。
- 引用必须指向可访问文档。
- 检索和回答要分别评测。
- 记录 query、召回片段、rerank 分数、模型回答、人工反馈。

## 5. 实践任务

1. 为企业制度库设计 hybrid search 查询流程。
2. 设计一个 reranker 接口，输入候选片段，输出重排结果。
3. 判断一个跨部门知识问答场景是否需要 GraphRAG。
4. 为 RAG 系统设计 20 条回归评测问题。

## 6. 阶段验收标准

- 能解释 GraphRAG 与普通 RAG 的核心差异。
- 能说明 reranker 在召回和生成之间的作用。
- 能设计企业 AI 搜索中的权限、引用、评测和日志。

## 7. 本课使用的信息源

- Microsoft GraphRAG：https://github.com/microsoft/graphrag
- LlamaIndex API Reference：https://docs.llamaindex.ai/en/stable/api_reference/
- OpenAI Retrieval 文档：https://platform.openai.com/docs/guides/retrieval

## 8. 问答记录

暂无。

## 9. 外部补充

暂无。

## 10. 结构化补充（整改）

### 核心讲解

- 企业 AI 搜索要分开评估“召回质量”和“生成质量”。
- GraphRAG 适合跨实体、跨文档关系强的问题，不是所有场景都要上图。
- Reranker 是“召回到生成”之间的关键质量闸门。

### 拓展阅读

- Microsoft GraphRAG: https://github.com/microsoft/graphrag
- OpenAI Retrieval Guide: https://platform.openai.com/docs/guides/retrieval

### 问答记录

- 2026-05-12：新增结构化模板，后续将补企业搜索评分样例。

### 外部补充

- 暂无（可补充企业知识库真实查询日志样本）。

### 本课掌握检查

- 你能否判断一个业务问题是否需要 GraphRAG？
- 你能否定义 reranker 的输入输出契约与评测指标？

### 下一课前置条件

- 完成一份企业搜索链路设计草案（权限、检索、重排、引用、评测）。

## 11. 企业搜索评测样例（整改新增）

### 评测拆分原则

- 检索评测：看“能否找对材料”
- 重排评测：看“候选顺序是否合理”
- 生成评测：看“回答是否正确且有引用”

### 最小评测样本（JSON）

```json
{
  "id": "ent-search-001",
  "query": "员工差旅报销上限是多少？",
  "expected_docs": ["policy-travel-v3#4.2"],
  "expected_answer_keywords": ["报销上限", "引用制度条款"],
  "ground_truth": "根据制度4.2条..."
}
```

### 指标建议

- Retrieval Recall@K
- Rerank NDCG@K
- Answer Groundedness
- Citation Accuracy

### 跨章节边界（去重指引）

- 第 09 课主讲 `embedding/向量库基础`，本课仅引用其底层概念。
- 第 10 课主讲 `RAG 基本链路`，本课主讲 `企业搜索与 GraphRAG 增强`。
- 第 33 课主讲 `安全治理`，本课只保留与检索链路直接相关的安全点。

## 回归评测记录（2026-05-12）

- run_id: `baseline-2026-05-12`
- case: `E29-search-eval`
- result: `PASS`
- 记录：`study/projects/27-36-min-eval-regression-run-2026-05-12.md`

## 可运行示例（Java，整改新增）

```java
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class RetrievalMetricDemo {
    public static double recallAtK(List<String> predictedTopK, Set<String> truth) {
        int hit = 0;
        for (String p : predictedTopK) if (truth.contains(p)) hit++;
        return truth.isEmpty() ? 0.0 : (double) hit / truth.size();
    }

    public static void main(String[] args) {
        List<String> topK = Arrays.asList("doc-A", "doc-X", "doc-B");
        Set<String> truth = new HashSet<String>(Arrays.asList("doc-A", "doc-B", "doc-C"));
        System.out.println("Recall@3 = " + recallAtK(topK, truth)); // 0.666...
    }
}
```

## 学习状态

- 状态：未开始（内容已就绪）
- 最近更新：2026-05-12
- 进入下一课条件：学员明确回复“这节课已经学会”

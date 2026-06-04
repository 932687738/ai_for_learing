<!-- 模块：RRF 混合检索融合 | 最后更新于 2026-05-28 -->

# RRF 混合检索融合

> Reciprocal Rank Fusion 公式、配置与对比。

## 目录

- [RRF 是什么](#rrf-是什么)
- [为什么混合检索需要 RRF](#为什么混合检索需要-rrf)
- [RRF 公式与融合计算](#rrf-公式与融合计算)
- [RRF 核心特性](#rrf-核心特性)
- [Spring AI 中配置 RRF 混合检索](#spring-ai-中配置-rrf-混合检索)
- [其他向量存储中的 RRF 实现](#其他向量存储中的-rrf-实现)
- [RRF 与其他融合方法对比](#rrf-与其他融合方法对比)

---
## RRF 是什么

> **模块**：RRF 混合检索融合 | **标签**：RAG检索增强 | **更新**：2026-05-28

### 核心概念

定义：RRF（倒数排名融合）是一种**结果融合算法**，将多种检索方式各自得到的排序列表合并为统一、更优的最终排名。

### 要点

- **定义**：RRF（倒数排名融合）是一种**结果融合算法**，将多种检索方式各自得到的排序列表合并为统一、更优的最终排名。
- **典型场景**：**混合检索（Hybrid Search）**，例如 BM25 关键词检索 + 向量 ANN 检索并行召回后的结果融合。

### 面试常问

**问**：什么是 RRF（Reciprocal Rank Fusion）？主要用在什么场景？

**答**：定义：RRF（倒数排名融合）是一种结果融合算法**，将多种检索方式各自得到的排序列表合并为统一、更优的最终排名。；典型场景：混合检索（Hybrid Search）**，例如 BM25 关键词检索 + 向量 ANN 检索并行召回后的结果融合。。

### 关联知识点

- [RAG 检索策略](RAG检索策略.md)
- [索引与存储](索引与存储.md)

---
## 为什么混合检索需要 RRF

> **模块**：RRF 混合检索融合 | **标签**：RAG检索增强 | **更新**：2026-05-28

### 核心概念

单一检索方式有什么缺陷？RRF 要解决什么问题？

### 要点

| 检索方式 | 优点 | 缺点 |
| :--- | :--- | :--- |
| **关键词（BM25/TF-IDF）** | 精确匹配术语、型号、专有名词 | 无语义理解，搜「智能手机」找不到「iPhone」 |
| **向量（ANN）** | 语义理解强，近义词召回好 | 可能漏掉精确关键词匹配 |

**RRF 目标**：结合两者优势，让结果既包含精确术语匹配，又包含语义相关内容。

### 面试常问

**问**：单一检索方式有什么缺陷？RRF 要解决什么问题？

**答**：优点 :--- 精确匹配术语、型号、专有名词 语义理解强，近义词召回好 **RRF 目标**：结合两者优势，让结果既包含精确术语匹配，又包含语义相关内容。

### 关联知识点

- [RAG 检索策略](RAG检索策略.md)
- [索引与存储](索引与存储.md)

---
## RRF 公式与融合计算

> **模块**：RRF 混合检索融合 | **标签**：RAG检索增强 | **更新**：2026-05-28

### 核心概念

`d`：某个文档；`k`：检索路数；`r_i(d)`：文档 d 在第 i 路结果中的排名（从 1 开始）；`60`：平滑常数，防止靠后排名得分过低。

### 要点

**核心公式**：

```
RRF(d) = Σ_{i=1}^{k} 1 / (r_i(d) + 60)
```

- `d`：某个文档；`k`：检索路数；`r_i(d)`：文档 d 在第 i 路结果中的排名（从 1 开始）；`60`：平滑常数，防止靠后排名得分过低。

**示例**（问题：「如何训练神经网络」）：

- BM25 第 1 名《神经网络训练指南》+ 向量第 2 名同一文档 → 两路得分累加 **0.0325** → 融合第 1 名。
- 仅在某一路排名第 1、另一路未出现的文档，融合后通常低于两路都靠前的文档。

### 代码示例

```java
public class RRFMerger {
    private static final int K = 60;

    public List<Document> merge(List<List<Document>> rankedLists) {
        Map<String, Double> rrfScores = new HashMap<>();
        for (List<Document> list : rankedLists) {
            for (int i = 0; i < list.size(); i++) {
                double contribution = 1.0 / (K + i + 1);
                rrfScores.merge(list.get(i).getId(), contribution, Double::sum);
            }
        }
        return sortByScore(rrfScores);
    }
}
```

### 面试常问

**问**：RRF 的核心公式是什么？请结合示例说明如何计算最终排名。

**答**：`d`：某个文档；`k`：检索路数；`r_i(d)`：文档 d 在第 i 路结果中的排名（从 1 开始）；`60`：平滑常数，防止靠后排名得分过低。；BM25 第 1 名《神经网络训练指南》+ 向量第 2 名同一文档 → 两路得分累加 0.0325 → 融合第 1 名。；仅在某一路排名第 1、另一路未出现的文档，融合后通常低于两路都靠前的文档。。

### 关联知识点

- [RAG 检索策略](RAG检索策略.md)
- [索引与存储](索引与存储.md)

---
## RRF 核心特性

> **模块**：RRF 混合检索融合 | **标签**：RAG检索增强 | **更新**：2026-05-28

### 核心概念

1. **无需归一化**：BM25 分与向量相似度量纲不同，RRF 只依赖**排名位置**，避开归一化难题。

### 要点

1. **无需归一化**：BM25 分与向量相似度量纲不同，RRF 只依赖**排名位置**，避开归一化难题。
2. **位置权重递减**：排名越靠前贡献越大（第 1 名 ≈ 0.0164，第 10 名 ≈ 0.0143），差距不会过于悬殊。
3. **自动处理缺失**：某文档在某路未出现则该项贡献为 0，不因「缺席」被额外惩罚。

### 面试常问

**问**：RRF 相比直接合并原始分数有哪些优势？

**答**：1. **无需归一化**：BM25 分与向量相似度量纲不同，RRF 只依赖**排名位置**，避开归一化难题。 2. **位置权重递减**：排名越靠前贡献越大（第 1 名 ≈ 0.0164，第 10 名 ≈ 0.0143），差距不会过于悬殊。 3. **自动处理缺失**：某文档在某路未出现则该项贡献为 0，不因「缺席」被额外惩罚。

### 关联知识点

- [RAG 检索策略](RAG检索策略.md)
- [索引与存储](索引与存储.md)

---
## Spring AI 中配置 RRF 混合检索

> **模块**：RRF 混合检索融合 | **标签**：RAG检索增强 | **更新**：2026-05-28

### 核心概念

Spring AI 对 **Elasticsearch、OpenSearch** 等支持混合检索的向量存储内置 RRF。启用后自动执行 BM25 → ANN → RRF 融合三步。

### 要点

Spring AI 对 **Elasticsearch、OpenSearch** 等支持混合检索的向量存储内置 RRF。启用后自动执行 BM25 → ANN → RRF 融合三步。

### 代码示例

```yaml
spring:
  ai:
    vectorstore:
      elasticsearch:
        hybrid:
          enabled: true
          similarity: rrf          # 使用 RRF 作为融合策略
          rrf:
            rank-constant: 60      # RRF 公式中的平滑常数
            window-size: 100       # 参与融合的排名窗口大小
```

```java
@Autowired
private ElasticsearchVectorStore vectorStore;

public void hybridSearch(String query) {
    List<Document> results = vectorStore.similaritySearch(
        SearchRequest.builder()
            .query(query)
            .topK(5)
            .withHybridSearch(true)  // 启用混合检索
            .build()
    );
    // results 已是 RRF 融合后的最终结果
    results.forEach(doc -> System.out.println(doc.getContent()));
}
```

### 面试常问

**问**：在 Spring AI 中如何启用 RRF 混合检索？Elasticsearch 向量存储如何配置？

**答**：Spring AI 对 **Elasticsearch、OpenSearch** 等支持混合检索的向量存储内置 RRF。启用后自动执行 BM25 → ANN → RRF 融合三步。

### 关联知识点

- [RAG 检索策略](RAG检索策略.md)
- [索引与存储](索引与存储.md)

---
## 其他向量存储中的 RRF 实现

> **模块**：RRF 混合检索融合 | **标签**：RAG检索增强 | **更新**：2026-05-28

### 核心概念

PgVector：扩展本身不直接提供 RRF，可在应用层分别计算 `vector_score` 与 `ts_rank`，再用 RRF 融合。

### 要点

- **PgVector**：扩展本身不直接提供 RRF，可在应用层分别计算 `vector_score` 与 `ts_rank`，再用 RRF 融合。
- **Milvus 2.4+**：原生支持混合检索与 RRF，通过 `RRFRanker` 指定 `rank_constant`。

### 代码示例

```sql
-- pgvector 本身不直接支持 RRF，但可在应用层实现
-- 通过 vector_score 和 ts_rank 分别计算分数，再用 RRF 融合
```

```python
# Milvus 2.4+ 支持混合检索和 RRF
from pymilvus import AnnSearchRequest, RRFRanker

hybrid_req = AnnSearchRequest(...)
res = collection.hybrid_search(
    reqs=[hybrid_req, ...],
    ranker=RRFRanker(rank_constant=60),
    limit=10
)
```

### 面试常问

**问**：PgVector、Milvus 等存储如何实现 RRF？

**答**：PgVector**：扩展本身不直接提供 RRF，可在应用层分别计算 `vector_score` 与 `ts_rank`，再用 RRF 融合。；Milvus 2.4+**：原生支持混合检索与 RRF，通过 `RRFRanker` 指定 `rank_constant`。。

### 关联知识点

- [RAG 检索策略](RAG检索策略.md)
- [索引与存储](索引与存储.md)

---
## RRF 与其他融合方法对比

> **模块**：RRF 混合检索融合 | **标签**：RAG检索增强 | **更新**：2026-05-28

### 核心概念

RRF 与加权求和、Combinational Sum 等融合方式有何区别？

### 要点

| 方法 | 原理 | 优点 | 缺点 |
| :--- | :--- | :--- | :--- |
| **RRF** | 基于排名倒数求和 | 无需归一化，对异常值鲁棒 | 丢失原始分数信息 |
| **加权求和** | α × 向量分 + (1-α) × BM25 分 | 可调节权重 | 需要归一化，调参复杂 |
| **Combinational Sum** | 简单相加排名 | 实现简单 | 未考虑排名位置权重 |

### 面试常问

**问**：RRF 与加权求和、Combinational Sum 等融合方式有何区别？

**答**：原理 缺点 :--- :--- 基于排名倒数求和 丢失原始分数信息 **加权求和** 可调节权重 简单相加排名 未考虑排名位置权重 |

### 关联知识点

- [RAG 检索策略](RAG检索策略.md)
- [索引与存储](索引与存储.md)

---
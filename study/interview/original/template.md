# RRF（Reciprocal Rank Fusion）详解

## 📌 什么是 RRF？

**RRF（Reciprocal Rank Fusion，倒数排名融合）** 是一种**结果融合算法**，主要用于**混合检索**（Hybrid Search）场景。当使用多种检索方式（如关键词检索 + 向量检索）分别得到结果后，RRF 能将它们合并成一个**统一的、更优的最终排名**。

## 🎯 为什么需要 RRF？

单一的检索方式都有缺陷：

| 检索方式 | 优点 | 缺点 |
| :--- | :--- | :--- |
| **关键词检索 (BM25/TF-IDF)** | 精确匹配术语、产品型号、专有名词效果好 | 无法理解语义，搜“智能手机”找不到“iPhone” |
| **向量检索 (ANN)** | 语义理解强，能找近义词相关内容 | 可能漏掉精确的关键词匹配 |

**RRF 的目标**：结合两者优势，让结果既包含精确匹配的术语，又包含语义相关的内容。

## ⚙️ RRF 工作原理

### 核心公式
RRF(d) = Σ_{i=1}^{k} 1 / (r_i(d) + 60)

text

其中：
- `d`：某个文档
- `k`：检索方式的数量（如 2 种）
- `r_i(d)`：文档 d 在第 i 种检索结果中的排名（从 1 开始）
- `60`：平滑常数，防止排名靠后的文档得分过低

### 📊 计算示例

假设问题：“如何训练神经网络”

**BM25（关键词检索）结果**：
1. 《神经网络训练指南》
2. 《PyTorch入门教程》
3. 《深度学习中的反向传播》

**向量检索（语义检索）结果**：
1. 《深度学习的梯度下降法》
2. 《神经网络训练指南》
3. 《反向传播算法详解》

**RRF 融合计算**：

| 文档 | BM25排名 | 向量排名 | BM25得分 | 向量得分 | **RRF总分** | **最终排名** |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| 《神经网络训练指南》 | 1 | 2 | 1/(1+60)=0.0164 | 1/(2+60)=0.0161 | **0.0325** | 🥇 第1名 |
| 《深度学习的梯度下降法》 | - | 1 | 0 | 1/(1+60)=0.0164 | **0.0164** | 🥈 第2名 |
| 《PyTorch入门教程》 | 2 | - | 1/(2+60)=0.0161 | 0 | 0.0161 | 第3名 |
| 《深度学习中的反向传播》 | 3 | - | 1/(3+60)=0.0159 | 0 | 0.0159 | 第4名 |
| 《反向传播算法详解》 | - | 3 | 0 | 1/(3+60)=0.0159 | 0.0159 | 第4名（并列） |

**结果分析**：
- 《神经网络训练指南》在两种检索中**排名都很靠前** → RRF 最高分 → 最终第1名
- 单一检索的第1名如果没有另一种检索的确认 → 排到融合结果的第2位

## 💡 RRF 核心特性

### 1. 不需要归一化
不同检索方式的分数（BM25 分数、向量相似度）量纲不同，无法直接比较。RRF 只依赖**排名位置**，避开归一化难题。

### 2. 位置权重递减
排名越靠前，得分贡献越大。第1名得分 ≈ 0.0164，第10名得分 ≈ 0.0143，差距不会过于悬殊。

### 3. 自动处理缺失结果
文档如果在某种检索中没出现，就不参与该项计分（贡献为0），不会因为缺失而受到惩罚。

## 🚀 在 Spring AI 中使用 RRF

Spring AI 已内置 RRF 支持，特别适用于 **Elasticsearch、OpenSearch** 等支持混合检索的向量存储。

### 配置示例（application.yml）

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
Java 代码示例
java
@Autowired
private ElasticsearchVectorStore vectorStore;

public void hybridSearch(String query) {
    // Spring AI 会自动执行：
    // 1. BM25 关键词检索
    // 2. ANN 向量检索
    // 3. RRF 融合两个结果集

    List<Document> results = vectorStore.similaritySearch(
        SearchRequest.builder()
            .query(query)
            .topK(5)
            .withHybridSearch(true)  // 启用混合检索
            .build()
    );

    // results 已经是经过 RRF 融合后的最终结果
    results.forEach(doc -> 
        System.out.println(doc.getContent())
    );
}
其他向量存储的配置（示意）
PGvector + pgvector 扩展（需自定义查询）：

sql
-- pgvector 本身不直接支持 RRF，但可在应用层实现
-- 通过 vector_score 和 ts_rank 分别计算分数，再用 RRF 融合
Milvus：

python
# Milvus 2.4+ 支持混合检索和 RRF
from pymilvus import AnnSearchRequest, RRFRanker

hybrid_req = AnnSearchRequest(...)
res = collection.hybrid_search(
    reqs=[hybrid_req, ...],
    ranker=RRFRanker(rank_constant=60),
    limit=10
)
🔄 RRF vs 其他融合方法
方法	原理	优点	缺点
RRF	基于排名倒数求和	无需归一化，对异常值鲁棒	丢失原始分数信息
加权求和 (Weighted Sum)	α * 向量分 + (1-α) * BM25分	可调节权重	需要归一化，调参复杂
Combinational Sum	简单相加排名	实现简单	未考虑排名位置权重
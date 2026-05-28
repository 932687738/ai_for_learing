# VectorStore 检索方法对比：similaritySearch vs similarityThreshold

在向量检索中，`similaritySearch` 和基于 `similarityThreshold` 的检索是两种不同的策略。  
`SIMILARITY_THRESHOLD_ACCEPT_ALL`（值为 `0.0`）是 Spring AI 中用于“接受所有结果”的特殊常量，可使阈值检索退化为普通的 `similaritySearch`。

## 核心区别一览

| 特性               | `similaritySearch` (无阈值)                 | `similarityThreshold` (带阈值)                |
| ------------------ | ------------------------------------------- | ---------------------------------------------- |
| **核心理念**       | 数量优先，保证返回 `topK` 条结果            | 质量优先，只返回相似度超过阈值的结果           |
| **返回数量**       | **固定为 K** （即使低分文档也会被强制返回） | **不固定**（可能少于 K，甚至为 0）             |
| **文档质量**       | 可能混入不相关内容                          | 通过阈值过滤，结果更精准、更相关               |
| **典型应用场景**   | 对结果数量有硬性要求，或需要二次排序/过滤   | 对检索准确性要求高，希望避免低质量噪声         |

## 举例说明

假设检索“猫咪吃什么比较好？”，向量库中有以下文档及相似度得分：

1.  “猫咪需要高蛋白食物”  → 得分 0.92
2.  “猫咪喜欢睡觉”      → 得分 0.35
3.  “狗狗需要运动”      → 得分 0.12

- **使用 `similaritySearch`（topK=2）**：返回文档 1 和文档 2。文档 2 得分很低，但为了凑够数量仍被返回。
- **使用 `similarityThreshold`（阈值=0.7）**：仅返回文档 1。文档 2 和 3 因得分低于 0.7 被过滤，即使请求 topK=10 也只会返回 1 条。

## 常量 `SIMILARITY_THRESHOLD_ACCEPT_ALL`

该常量定义为 `0.0`，表示**接受所有文档**。  
当阈值设为 `0.0` 时，所有文档（得分 ≥ 0）都被视为通过筛选，效果等同于普通的 `similaritySearch`。

## Spring AI 中的代码示例

使用 `SearchRequest` 构建请求，并调用 `VectorStore.similaritySearch(request)`。

### 方式一：关闭阈值（等效 similaritySearch）

```java
SearchRequest request = SearchRequest.query("用户问题")
        .withTopK(5)  // 固定返回 5 条文档
        .withSimilarityThreshold(SearchRequest.SIMILARITY_THRESHOLD_ACCEPT_ALL);

List<Document> results = vectorStore.similaritySearch(request);
方式二：开启阈值过滤
java
SearchRequest request = SearchRequest.query("用户问题")
        .withTopK(10)          // 候选池大小（最多返回 10 条）
        .withSimilarityThreshold(0.75);  // 只返回相似度 ≥ 0.75 的文档

List<Document> results = vectorStore.similaritySearch(request);
如何选择？实践建议
使用阶段	推荐方式
初期开发 / 快速验证	使用 SIMILARITY_THRESHOLD_ACCEPT_ALL（即普通 similaritySearch）
需要保证召回数量	使用 similaritySearch 并调高 topK，后续再对结果做业务过滤
追求检索精准度	设置合适的阈值（如 0.75 ~ 0.82），并配合稍大的 topK 作为候选池
混合策略（推荐）	先用 similaritySearch 拉取较多候选（如 topK=20），再在内存中二次阈值过滤
补充说明
阈值 0.0 的含义：通常相似度得分在 [0, 1] 区间，0.0 表示接受任何得分（含 0 分）的文档，因此相当于“不过滤”。

不同向量数据库（如 Chroma, PGVector, Pinecone）对相似度度量的实现可能略有差异，但 SearchRequest 的抽象保证了行为一致。

若阈值设置过高（如 0.95），可能返回空列表，建议结合业务数据分布进行调优。
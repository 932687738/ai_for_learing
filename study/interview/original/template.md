
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


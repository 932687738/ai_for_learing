# RAG检索增强 问答

<!-- 最后更新于 2026-05-28 -->

多路召回（向量 + BM25）
问：如何通过多路召回（例如结合关键词搜索 BM25 和向量搜索）来提升召回率？请简述在 Spring AI 中集成 ElasticsearchVectorStore 并实现混合检索的思路。
答：向量语义召回与 BM25 关键词召回并行；ElasticsearchVectorStore 可开 hybridSearch 调权重，否则双路检索后合并去重再 Rerank。
分类标签：RAG检索增强 | 更新日期：2026-05-28


---

重排序（Rerank）集成
问：多路召回后，如何集成重排序模型（如 CrossEncoder）？请简要说明在 RetrievalAugmentationAdvisor 中添加 reranker 的步骤。
答：多路召回后用 CrossEncoder 等重排；Spring AI Alibaba 可用 RetrievalRerankAdvisor，在 ChatClient 默认 Advisor 链中注入，流程为检索→重排→生成。
分类标签：RAG检索增强 | 更新日期：2026-05-28


---

查询改写（Query Rewriting）
问：如何通过查询改写缓解因用户表述不清而导致的检索失败？请给出 Spring AI 中的实现思路。
答：用 RewriteQueryTransformer、MultiQueryExpander、CompressionQueryTransformer 等改写或扩展 query，经 RetrievalAugmentationAdvisor 配置，缓解表述不清导致的漏召。
分类标签：RAG检索增强 | 更新日期：2026-05-28


---

HyDE 实现
问：在 Spring AI 中实现 HyDE 的具体步骤是什么？请写出核心代码。
答：先让 LLM 生成假设性答案文档，再对答案做向量检索；实现 QueryTransformer，在 transform 中生成假设文档作为检索 query。
分类标签：RAG检索增强 | 更新日期：2026-05-28


---

HyDE 核心思路
问：简述 HyDE 的核心思路，与传统 Query2Vec 有何本质不同？
答：用假设答案文档的向量检索，而非仅改写问题；与 Query2Vec 直接编码问题不同，适合模糊问法。
分类标签：RAG检索增强 | 更新日期：2026-05-28


---

HyDE 不适用场景
问：什么场景下 HyDE 的召回提升不值得额外代价？
答：专有名词、已很规范的问题不必 HyDE，额外 LLM 成本不值。
分类标签：RAG检索增强 | 更新日期：2026-05-28


---

智能路由（名词库）
问：如何自动判断问题是否需要 HyDE？
答：可用名词库/规则判断：命中走直通检索，未命中再走 HyDE，平衡成本与召回。
分类标签：RAG检索增强 | 更新日期：2026-05-28


---

RRF 多路召回融合
问：如何实现多路召回的结果融合？请给出 RRF 伪代码。
答：RRF 对各路的 rank 贡献 1/(K+rank) 求和（K 常取 60），按融合分排序选文档。
分类标签：RAG检索增强 | 更新日期：2026-05-28


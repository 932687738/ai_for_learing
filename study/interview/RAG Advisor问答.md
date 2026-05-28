# RAG Advisor 问答

<!-- 最后更新于 2026-05-28 -->

QuestionAnswerAdvisor 缓存
问：在 Spring AI 生产级 RAG 应用中，QuestionAnswerAdvisor 默认每次请求同步调用向量存储。如何为检索结果引入缓存层，既能缓存相同或相似问题的检索结果，又能避免缓存污染？请给出基于 Spring Cache 或自定义 CacheManager 的配置思路。
答：对归一化 query 或向量哈希做缓存 Key，设 TTL；含时间敏感词时禁用缓存；可用 @Cacheable 或自定义 CacheManager，避免脏读。
分类标签：RAG Advisor | 更新日期：2026-05-28


---

QuestionAnswerAdvisor 工作流程
问：QuestionAnswerAdvisor 接收到用户问题后，会执行哪两个主要步骤？将什么内容传递给大模型？
答：before 阶段 similaritySearch 取文档；生成前把 Document.content 文本拼进 Prompt，传的是文本不是向量。
分类标签：RAG Advisor | 更新日期：2026-05-28


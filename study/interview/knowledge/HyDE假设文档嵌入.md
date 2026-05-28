<!-- 模块：HyDE 假设文档嵌入 | 最后更新于 2026-05-28 -->

# HyDE 假设文档嵌入

> HyDE 原理、实现、衍生方案与智能路由。

## 目录

- [HyDE 是什么](#hyde-是什么)
- [HyDE 为什么有效与 Query2Vec 区别](#hyde-为什么有效与-query2vec-区别)
- [HyDE 优缺点与适用场景](#hyde-优缺点与适用场景)
- [HyDE Spring AI 实现](#hyde-spring-ai-实现)
- [HyDE LangChain 实现](#hyde-langchain-实现)
- [HyDE 衍生方案](#hyde-衍生方案)
- [智能路由判断是否使用 HyDE](#智能路由判断是否使用-hyde)

---
## HyDE 是什么

> **模块**：HyDE 假设文档嵌入 | **标签**：RAG检索增强 | **更新**：2026-05-28

### 核心概念

定义：HyDE 是一种 RAG 检索增强技术——先让 LLM 根据用户问题「想象」一份理想答案（假想文档），再基于**假想文档的向量**检索真实文档。

### 要点

- **定义**：HyDE 是一种 RAG 检索增强技术——先让 LLM 根据用户问题「想象」一份理想答案（假想文档），再基于**假想文档的向量**检索真实文档。
- **一句话**：不要直接搜文档，先让 AI 构思最佳答案的样子，再用这个想法去搜。

**工作流程**：

1. **用户提问**（如「LangSmith 是什么？为什么需要它？」）
2. **生成假想文档**：LLM 生成「看起来像答案」的文本（可不真实，但语义/结构有参考价值）
3. **转换为嵌入向量**：用嵌入模型将假想文档转为稠密向量
4. **基于假想文档检索**：用该向量在向量库做相似性搜索
5. **生成最终答案**：将召回的真实文档作为上下文，交给 LLM 回答

### 面试常问

**问**：什么是 HyDE（Hypothetical Document Embeddings）？核心思想是什么？

**答**：定义：HyDE 是一种 RAG 检索增强技术——先让 LLM 根据用户问题「想象」一份理想答案（假想文档），再基于假想文档的向量**检索真实文档。；一句话**：不要直接搜文档，先让 AI 构思最佳答案的样子，再用这个想法去搜。。

### 关联知识点

- [RAG 检索策略](RAG检索策略.md)
- [RRF 混合检索融合](RRF混合检索融合.md)

---
## HyDE 为什么有效与 Query2Vec 区别

> **模块**：HyDE 假设文档嵌入 | **标签**：RAG检索增强 | **更新**：2026-05-28

### 核心概念

意图理解更准：假想文档比短查询语义更丰富，弥补信息不足。

### 要点

**为什么有效**：

- **意图理解更准**：假想文档比短查询语义更丰富，弥补信息不足。
- **零样本可用**：无需标注数据，直接利用 LLM 通用知识。
- **效果显著**：实验中 Top-3 召回率从 78% 提升到 91%。

**与 Query2Vec 的本质区别**：

- **HyDE**：用 LLM 生成的**假设性答案向量**检索。
- **Query2Vec**：直接对用户短问句 embed，易因表述模糊导致向量偏离。

### 面试常问

**问**：HyDE 为什么能提升召回？与传统 Query2Vec 有何本质不同？

**答**：意图理解更准**：假想文档比短查询语义更丰富，弥补信息不足。；零样本可用**：无需标注数据，直接利用 LLM 通用知识。；效果显著**：实验中 Top-3 召回率从 78% 提升到 91%。；HyDE：用 LLM 生成的假设性答案向量**检索。。

### 关联知识点

- [RAG 检索策略](RAG检索策略.md)
- [RRF 混合检索融合](RRF混合检索融合.md)

---
## HyDE 优缺点与适用场景

> **模块**：HyDE 假设文档嵌入 | **标签**：RAG检索增强 | **更新**：2026-05-28

### 核心概念

HyDE 有哪些优缺点？什么场景不适合使用？

### 要点

| 优点 | 缺点 |
| :--- | :--- |
| 无需标注数据 | 每次检索需调用 LLM 生成假想文档，增加延迟和成本 |
| 理解深层意图 | 假想文档可能含「幻觉」，需对比编码器过滤 |
| 易于集成（LangChain 等） | 不适合对响应延迟极其敏感的场景 |

**不适用场景**：专有名词、SKU、错误码等已高度规范且简短的查询，或问题本身已足够精确时，直接 Query2Vec 更划算。

### 面试常问

**问**：HyDE 有哪些优缺点？什么场景不适合使用？

**答**：缺点 :--- 每次检索需调用 LLM 生成假想文档，增加延迟和成本 理解深层意图 不适合对响应延迟极其敏感的场景 | **不适用场景**：专有名词、SKU、错误码等已高度规范且简短的查询，或问题本身已足够精确时，直接 Query2Vec 更划算。

### 关联知识点

- [RAG 检索策略](RAG检索策略.md)
- [RRF 混合检索融合](RRF混合检索融合.md)

---
## HyDE Spring AI 实现

> **模块**：HyDE 假设文档嵌入 | **标签**：RAG检索增强 | **更新**：2026-05-28

### 核心概念

1. 用 ChatClient 根据用户问题生成「假设性理想答案」文档。

### 要点

1. 用 ChatClient 根据用户问题生成「假设性理想答案」文档。
2. 对该文本做 embed 并 similaritySearch，而非直接对原始短问句向量化。
3. 封装为 `QueryTransformer` 接入 `RetrievalAugmentationAdvisor`。

### 代码示例

```java
@Service
public class HyDEQueryGenerator {
    @Autowired
    private ChatClient chatClient;

    public String generateHypotheticalDocument(String userQuery) {
        String prompt = """
            你是一个信息检索助手。请根据以下用户问题，直接生成一篇内容详实、信息准确的理想答案。
            用户问题：%s
            """.formatted(userQuery);
        return chatClient.prompt().user(prompt).call().content();
    }
}

@Component
public class HyDEQueryTransformer implements QueryTransformer {
    @Autowired
    private HyDEQueryGenerator hydeGenerator;

    @Override
    public String transform(String query) {
        return hydeGenerator.generateHypotheticalDocument(query);
    }
}
```

### 面试常问

**问**：在 Spring AI 中如何实现 HyDE？请写出核心代码。

**答**：1. 用 ChatClient 根据用户问题生成「假设性理想答案」文档。 2. 对该文本做 embed 并 similaritySearch，而非直接对原始短问句向量化。 3. 封装为 `QueryTransformer` 接入 `RetrievalAugmentationAdvisor`。

### 关联知识点

- [RAG 检索策略](RAG检索策略.md)
- [RRF 混合检索融合](RRF混合检索融合.md)

---
## HyDE LangChain 实现

> **模块**：HyDE 假设文档嵌入 | **标签**：RAG检索增强 | **更新**：2026-05-28

### 核心概念

`HypotheticalDocumentEmbedder` 是 LangChain 内置类，自动完成「生成假想文档 → 嵌入 → 检索」流程；也可手动拆分各步骤做精细控制。

### 要点

`HypotheticalDocumentEmbedder` 是 LangChain 内置类，自动完成「生成假想文档 → 嵌入 → 检索」流程；也可手动拆分各步骤做精细控制。

### 代码示例

```python
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.retrievers import HypotheticalDocumentEmbedder

# 1. 初始化 LLM 和嵌入模型
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
base_embeddings = OpenAIEmbeddings()

# 2. 创建 HyDE 检索器（包装普通嵌入模型）
hyde_retriever = HypotheticalDocumentEmbedder(
    llm=llm,
    base_embeddings=base_embeddings,
    prompt_key="web_search"   # 使用内置提示模板或自定义
)

# 3. 准备向量数据库（示例使用 FAISS 内存存储）
#    假设已有文档片段列表 documents
# vectorstore = FAISS.from_documents(documents, base_embeddings)
# retriever = vectorstore.as_retriever()

# 4. 用 HyDE 检索器生成假想文档并搜索
# query = "LangSmith 是什么？为什么需要它？"
# relevant_docs = hyde_retriever.get_relevant_documents(query)
# print(relevant_docs)
```

### 面试常问

**问**：如何使用 LangChain 的 `HypotheticalDocumentEmbedder` 实现 HyDE？

**答**：`HypotheticalDocumentEmbedder` 是 LangChain 内置类，自动完成「生成假想文档 → 嵌入 → 检索」流程；也可手动拆分各步骤做精细控制。

### 关联知识点

- [RAG 检索策略](RAG检索策略.md)
- [RRF 混合检索融合](RRF混合检索融合.md)

---
## HyDE 衍生方案

> **模块**：HyDE 假设文档嵌入 | **标签**：RAG检索增强 | **更新**：2026-05-28

### 核心概念

HyPE：将生成过程迁移到**索引阶段**，降低查询延迟。

### 要点

- **HyPE**：将生成过程迁移到**索引阶段**，降低查询延迟。
- **HyQE**：生成假想**查询**（而非假想文档），从另一角度改进检索对齐。
- **SL-HyDE**：引入自学习机制，迭代优化假想文档质量。

### 面试常问

**问**：HyDE 有哪些衍生改进方案？

**答**：HyPE：将生成过程迁移到索引阶段**，降低查询延迟。；HyQE：生成假想查询**（而非假想文档），从另一角度改进检索对齐。；SL-HyDE**：引入自学习机制，迭代优化假想文档质量。。

### 关联知识点

- [RAG 检索策略](RAG检索策略.md)
- [RRF 混合检索融合](RRF混合检索融合.md)

---
## 智能路由判断是否使用 HyDE

> **模块**：HyDE 假设文档嵌入 | **标签**：RAG检索增强 | **更新**：2026-05-28

### 核心概念

维护术语/名词库（TerminologyRegistry），命中规范术语时走直通向量检索，否则走 HyDE。可在自定义 `CallAroundAdvisor` 中根据 `userText` 路由不同检索策略。

### 要点

维护术语/名词库（TerminologyRegistry），命中规范术语时走直通向量检索，否则走 HyDE。可在自定义 `CallAroundAdvisor` 中根据 `userText` 路由不同检索策略。

### 代码示例

```java
@Component
public class SmartRoutingAdvisor implements CallAroundAdvisor {
    @Autowired
    private TerminologyRegistry terminologyRegistry;
    
    @Override
    public AdvisedResponse around(AdvisedRequest request, AdvisorChain chain) {
        if (terminologyRegistry.containsTechnicalTerm(request.userText())) {
            // 直通车检索
        } else {
            // HyDE 检索
        }
    }
}
```

### 面试常问

**问**：如何自动判断问题是否需要 HyDE？

**答**：维护术语/名词库（TerminologyRegistry），命中规范术语时走直通向量检索，否则走 HyDE。可在自定义 `CallAroundAdvisor` 中根据 `userText` 路由不同检索策略。

### 关联知识点

- [RAG 检索策略](RAG检索策略.md)
- [RRF 混合检索融合](RRF混合检索融合.md)

---
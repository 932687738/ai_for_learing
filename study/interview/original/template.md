markdown
# Hypothetical Document Embeddings (HyDE) 总结

## 什么是 HyDE？

**HyDE** 是一种创新的检索增强生成（RAG）技术。核心思想：**先让大语言模型（LLM）根据用户问题“想象”一份理想答案（假想文档），再基于这份假想文档的向量去检索真实文档**。

> 一句话概括：不要直接搜文档，先让 AI 帮你构思最佳答案的样子，再用这个想法去搜。

## 工作流程

1. **用户提问**  
   例如：`LangSmith 是什么？为什么需要它？`

2. **生成假想文档**  
   LLM 根据问题生成一段“看起来像答案”的文本（内容可以不真实，但结构/语义要有参考价值）。

3. **转换为嵌入向量**  
   使用嵌入模型（如 `text-embedding-ada-002`）将假想文档转为稠密向量。

4. **基于假想文档检索**  
   用该向量在向量数据库中做相似性搜索，召回与“假想答案”最接近的真实文档片段。

5. **生成最终答案**  
   将检索到的真实文档作为上下文，交给 LLM 产生最终回答。

## 为什么有效？

- **意图理解更准**：假想文档包含比原始查询更丰富的语义信息，弥补了短查询的信息不足。
- **零样本可用**：无需标注数据，直接利用 LLM 的通用知识。
- **效果提升显著**：实验中，HyDE 将语义检索的 Top‑3 召回率从 78% 提升到 91%。

## 优缺点

| 优点 | 缺点 |
|------|------|
| 无需标注数据 | 每次检索都需要调用 LLM 生成假想文档，增加延迟和成本 |
| 理解深层意图 | 假想文档可能含有“幻觉”内容，需依赖对比编码器过滤 |
| 易于集成（LangChain 等） | 不适合对响应延迟极其敏感的场景 |

## 代码示例（LangChain 实现）

以下代码展示如何使用 LangChain 快速实现 HyDE：

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
注：HypotheticalDocumentEmbedder 是 LangChain 中的内置类，它会自动完成“生成假想文档 → 嵌入 → 检索”的流程。你也可以手动实现每个步骤以进行更精细的控制。

衍生方案
HyPE：将生成过程迁移到索引阶段，降低查询延迟。

HyQE：生成假想查询，从另一角度改进检索对齐。

SL‑HyDE：引入自学习机制，迭代优化假想文档质量。
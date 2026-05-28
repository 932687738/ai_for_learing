# ChromaDB 概述与使用指南

## 1. 什么是 ChromaDB？

ChromaDB 是一个**专为 AI 应用设计的开源向量数据库**。它以“轻量级”和“开发者友好”著称，主要用于存储、索引和检索由非结构化数据（文本、图片、音视频等）转换而来的高维向量（Embedding）。常被用作学习向量数据库和构建 RAG（检索增强生成）应用原型的首选工具。

## 2. 核心作用与主要职责

### 核心作用
高效处理海量数据的**语义相似性搜索**。传统数据库通过关键词匹配查找信息，而 ChromaDB 能够“理解”数据的语义，返回最接近的结果。

### 主要职责
- **向量存储与管理**：将非结构化数据转换为向量后持久化存储。
- **语义检索**：根据查询向量的语义返回最相似的向量列表（基于余弦相似度、欧氏距离等）。
- **支撑 RAG 应用**：作为 RAG 架构中的知识库，为大模型提供外部知识以生成更准确的回答。
- **元数据过滤**：在语义搜索基础上附加元数据条件（如类别、来源）进行结果过滤。

## 3. 数据结构

ChromaDB 的数据模型清晰且层次分明，类比关系型数据库如下：

| 概念              | 说明                                                                 | 类比         |
| :---------------- | :------------------------------------------------------------------- | :----------- |
| **租户 (Tenant)** | 顶级隔离单元，代表团队或组织。                                         | 实例/集群     |
| **数据库 (Database)** | 逻辑空间，归属于租户，用于区分不同项目或应用。                           | 数据库实例   |
| **集合 (Collection)** | **最核心的数据单元**，存储一组向量记录，是执行查询的最小单位。             | 数据表       |
| **文档 (Document)** | 存储的原始文本块，向量的生成通常基于文档内容。                           | 表行         |
| **嵌入向量 (Embedding)** | 由文档通过 AI 模型生成的数值数组，代表其语义。                         | 行中的字段   |
| **元数据 (Metadata)** | 附加的可过滤信息（键值对形式），用于在搜索前后进行过滤。                   | 其他字段     |

## 4. 快速上手代码示例（Python）

以下示例演示了 ChromaDB 的基本使用流程：安装、创建客户端、创建集合、添加文档、执行查询。

### 安装
```bash
pip install chromadb
基础用法
python
import chromadb
from chromadb.utils import embedding_functions

# 1. 创建客户端（使用本地持久化目录）
client = chromadb.PersistentClient(path="./chroma_data")

# 2. 创建集合（需指定 embedding 函数，此处使用默认的 all-MiniLM-L6-v2）
collection = client.create_collection(
    name="my_knowledge_base",
    embedding_function=embedding_functions.SentenceTransformerEmbeddingFunction()
)

# 3. 准备数据：文档、元数据、唯一 ID
documents = [
    "巴黎是法国的首都，以埃菲尔铁塔闻名。",
    "东京是日本的首都，以樱花和寿司闻名。",
    "北京是中国的首都，拥有故宫和长城。"
]
metadatas = [
    {"country": "法国", "feature": "铁塔"},
    {"country": "日本", "feature": "樱花"},
    {"country": "中国", "feature": "长城"}
]
ids = ["id1", "id2", "id3"]

# 4. 添加数据到集合
collection.add(
    documents=documents,
    metadatas=metadatas,
    ids=ids
)

# 5. 执行语义查询
query_text = "哪个国家的首都有著名的高塔？"
results = collection.query(
    query_texts=[query_text],
    n_results=2  # 返回最相似的 2 条结果
)

# 6. 查看结果
print("查询结果：")
for doc, meta, dist in zip(results['documents'][0], results['metadatas'][0], results['distances'][0]):
    print(f"文档: {doc}\n元数据: {meta}\n距离: {dist}\n")

# 7. 带元数据过滤的查询
filtered_results = collection.query(
    query_texts=["首都美食"],
    where={"country": "日本"},   # 仅查询 country 为日本的数据
    n_results=1
)
print("过滤后的查询结果：", filtered_results['documents'])
5. 类似项目对比
项目	特点	部署方式	擅长领域 / 适用场景	学习曲线
ChromaDB	简单、轻量、API友好。pip install chromadb 即可使用。	嵌入式、单机	原型开发、小规模项目、学习与实验	低
Weaviate	支持混合搜索（向量+关键词），提供 GraphQL 接口。	单机、集群	需要混合查询的生产环境（如电商搜索）	中
Milvus	功能强大，云原生架构，支持高并发和高可用，社区活跃。	分布式集群	大规模、高要求的向量检索生产应用	高
Qdrant	功能丰富，性能优秀，提供强大的过滤能力。	单机、集群	需要精细过滤和高性能向量检索的应用	中
FAISS	Meta 开源的算法库（非数据库），高效、轻量，支持向量聚类与相似搜索。	嵌入式库（内存）	高度定制化算法、学术研究、不关心持久化的实验场景	中
Pinecone	全托管云服务，免运维，开箱即用。	云服务	不想管理基础设施的生产级应用	低
6. 如何选择？
选 ChromaDB：个人开发者或小团队，快速尝试 RAG 或构建小型应用，追求简单高效。

选 Milvus / Weaviate：面对亿级以上向量数据、高并发、高可用的生产环境需求。

选 Pinecone / Qdrant：不想自己运维数据库（备份、扩展等），专注业务逻辑；或需要极强的过滤能力。

选 FAISS：仅需要向量相似度计算的算法，不需要数据持久化、分布式等数据库功能（如学术研究）。

以上代码示例可以在 Python 3.8+ 环境中直接运行，请确保已安装 chromadb 和 sentence-transformers（用于默认 embedding 函数）。
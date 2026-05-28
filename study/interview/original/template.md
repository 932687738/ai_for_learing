# RAG、知识图谱与向量图谱综合指南

## 1. 核心概念速览

| 概念 | 核心思想 | 典型用途 |
|------|---------|----------|
| **RAG**（检索增强生成） | 生成前先从外部知识库检索相关上下文 | 减少 LLM 幻觉，接入私有数据 |
| **知识图谱** | 实体（节点） + 关系（边）构成的图网络 | 多跳推理、可解释性、复杂关系问答 |
| **向量图谱（向量数据库）** | 文本 → 高维向量，通过 ANN 搜索语义相似项 | 模糊语义匹配、相似性检索 |
| **GraphRAG** | 知识图谱 + RAG，可融合向量检索 | 跨文档复杂推理、全局性问题 |

## 2. ANN 搜索（近似最近邻）

> 用精度换速度，在海量向量中快速找到“足够相似”的邻居。

### 常见算法
- HNSW（分层可导航小世界图）
- IVF（倒排文件索引）
- LSH（局部敏感哈希）

### 示例：使用 Faiss 进行 ANN 搜索（Python）

```python
import faiss
import numpy as np

# 生成 10000 个 128 维向量
dim = 128
data = np.random.random((10000, dim)).astype('float32')

# 构建 HNSW 索引
index = faiss.IndexHNSWFlat(dim, 32)
index.add(data)

# 查询
query = np.random.random((1, dim)).astype('float32')
distances, indices = index.search(query, k=5)  # 返回 top-5

print("最近邻索引:", indices)
print("相似度距离:", distances)
3. 召回率（Recall）
衡量系统“查全”能力：召回率 = 检索到的相关文档数 / 总相关文档数

提高召回率的方法
混合检索：向量 + 关键词（BM25）取并集

增大 Top-K：从 10 提升到 100，再用重排序（Reranker）

查询扩展：LLM 生成同义问句、HyDE（假设文档嵌入）

多路召回：不同 embedding 模型分别检索后合并

示例：使用 Elasticsearch 实现混合检索
json
{
  "query": {
    "bool": {
      "should": [
        { "match": { "content": "用户查询关键词" } },
        { "script_score": {
            "query": { "match_all": {} },
            "script": {
              "source": "cosineSimilarity(params.query_vector, 'vector_field') + 1.0",
              "params": { "query_vector": [0.1, 0.2, ...] }
            }
          }
        }
      ]
    }
  }
}
4. GraphRAG 原理与第二次搜索
默认行为：每次搜索独立执行（无状态），不自动复用前次结果。

加速方法：应用层加入查询缓存；图数据库自身的热点节点缓存。

会话式 GraphRAG：上层维护对话状态，将历史实体注入当前查询。

示例：使用 Neo4j 的 Cypher 查询（第一次 vs 第二次）
cypher
// 第一次：查找“山本屋”
MATCH (r:Restaurant {name: '山本屋'}) RETURN r

// 第二次：基于历史实体扩展（需应用层传入）
MATCH (r:Restaurant {name: '山本屋'})-[:LOCATED_IN]->(city:City)
MATCH (other:Restaurant)-[:LOCATED_IN]->(city)
WHERE other.vegan_friendly = true
RETURN other
5. 存储介质选型（个人电脑小型知识库）
针对纯 RAG（向量为主）
方案	介质	特点
轻量级	Chroma + 本地文件系统	零配置，内存索引
高召回	PostgreSQL + pgvector	支持混合查询（向量+全文）
开发者	SQLite + sqlite-vec	单文件，嵌入式
针对 GraphRAG（需图存储）
类型	代表	优点	资源消耗
嵌入式图数据库	KùzuDB	列式存储，无服务	低（<500MB）
全能融合	DuckDB + 图扩展	单文件，SQL 统一查询	低
封装易用	fathomdb（基于 SQLite）	图+向量+全文开箱即用	很低
传统重型	Neo4j（Docker）	功能最强	高（≥1GB 内存）
微软 GraphRAG 推荐配置：32GB 内存；知识库存储约为源文件的 10 倍。

6. 知识图谱举例：餐厅推荐
原始文档
text
山本屋：日料，朝阳区，有寿司拉面，安静，不适合儿童，提供素食。
樱花园：日料，朝阳区，榻榻米，欢迎儿童，素食需提前告知。
图谱结构（实体与关系）
cypher
// 创建节点
CREATE (:Restaurant {name:'山本屋', type:'日料', district:'朝阳区', kid_friendly:false, vegan_friendly:true})
CREATE (:Restaurant {name:'樱花园', type:'日料', district:'朝阳区', kid_friendly:true, vegan_friendly:'warning'})

// 创建关系
MATCH (a:Restaurant {name:'山本屋'}), (b:Restaurant {name:'樱花园'})
CREATE (a)-[:LOCATED_IN]->(:City {name:'朝阳区'})
CREATE (b)-[:LOCATED_IN]->(:City {name:'朝阳区'})
搜索“山本屋”的不同粒度
基础检索（直接属性）
cypher
MATCH (r:Restaurant {name:'山本屋'}) RETURN properties(r)
一跳检索（直接关系）
cypher
MATCH (r:Restaurant {name:'山本屋'})-[*1]-(neighbor)
RETURN r, neighbor
多跳推理（寻找同区域素食选择）
cypher
MATCH (r:Restaurant {name:'山本屋'})-[:LOCATED_IN]->(city:City)
MATCH (other:Restaurant)-[:LOCATED_IN]->(city)
WHERE other.vegan_friendly = true OR other.vegan_friendly = 'warning'
RETURN other.name
7. 总结：何时选用何种存储
任务类型	推荐介质	理由
简单 QA（单文档）	向量数据库（Chroma）	快速，语义匹配
精确关键词查询	SQLite FTS5	毫秒级，无依赖
多跳推理、关系问答	KùzuDB / Neo4j	图遍历效率高
个人笔记 + 图谱	fathomdb / Trilium Notes	零运维，便携
海量数据 + 复杂分析	DuckDB + 图扩展	分析型存储，SQL 统一
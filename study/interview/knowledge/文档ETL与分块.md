<!-- 模块：文档 ETL 与分块 | 最后更新于 2026-05-28（上传文件与切分边界） -->

# 文档 ETL 与分块

> Document 读取、切分、元数据增强与 ETL 流水线。

## 目录

- [Spring AI ETL Transform 数据转换](#spring-ai-etl-transform-数据转换)
- [DocumentReader 与 TikaDocumentReader](#documentreader-与-tikadocumentreader)
- [TokenTextSplitter 与普通 TextSplitter](#tokentextsplitter-与普通-textsplitter)
- [Document 的 content 与 metadata](#document-的-content-与-metadata)
- [TokenTextSplitter 参数 chunkSize 与 chunkOverlap](#tokentextsplitter-参数-chunksize-与-chunkoverlap)
- [其他分块工具](#其他分块工具)
- [KeywordMetadataEnricher 与 SummaryMetadataEnricher 存储位置](#keywordmetadataenricher-与-summarymetadataenricher-存储位置)
- [上传文件 PDF/Excel/图片 处理原理](#上传文件-pdfexcel图片-处理原理)
- [结构化输出与文本切分的职责边界](#结构化输出与文本切分的职责边界)

---
## Spring AI ETL Transform 数据转换

> **模块**：文档 ETL 与分块 | **标签**：文档与分块 | **更新**：2026-05-28

### 核心概念

文本分割：`TokenTextSplitter` 按 Token 大小切分长文本。

### 要点

在 RAG ETL 阶段，Transform 负责清洗、优化与扩充原始数据，为向量库准备高质量输入：

- **文本分割**：`TokenTextSplitter` 按 Token 大小切分长文本。
- **格式统一**：`ContentFormatTransformer` 将 PDF、HTML 等转为纯文本。
- **元数据丰富**：`KeywordMetadataEnricher` / `SummaryMetadataEnricher` 自动提取关键词和摘要。

可组合多个 Transformer 形成流水线。

### 代码示例

```java
// 文档处理流水线
List<Document> transformedDocs = keywordEnricher.apply(
    tokenTextSplitter.apply(rawDocs)
);
```

### 面试常问

**问**：Spring AI RAG 的 ETL 管道中 Transform 负责什么？有哪些常见实现？

**答**：文本分割**：`TokenTextSplitter` 按 Token 大小切分长文本。；格式统一**：`ContentFormatTransformer` 将 PDF、HTML 等转为纯文本。；元数据丰富**：`KeywordMetadataEnricher` / `SummaryMetadataEnricher` 自动提取关键词和摘要。。

### 关联知识点

- [向量与嵌入](向量与嵌入.md)
- [索引与存储](索引与存储.md)

---
## DocumentReader 与 TikaDocumentReader

> **模块**：文档 ETL 与分块 | **标签**：文档与分块 | **更新**：2026-05-28

### 核心概念

DocumentReader 职责：从不同数据源读取原始文档，生成 `Document` 对象（含 `content` 与 `metadata`），是 RAG ETL 管道的入口。

### 要点

- **DocumentReader 职责**：从不同数据源读取原始文档，生成 `Document` 对象（含 `content` 与 `metadata`），是 RAG ETL 管道的入口。
- **TikaDocumentReader 优势**：基于 Apache Tika，自动检测并解析 PDF、DOCX、XLSX、PPTX、HTML、XML、TXT 等格式，无需按 MIME 类型分别配置解析器。

### 代码示例

```java
Resource pdfResource = new FileSystemResource("doc.pdf");
TikaDocumentReader reader = new TikaDocumentReader(pdfResource);
List<Document> docs = reader.read();
```

### 面试常问

**问**：请解释 `DocumentReader` 在 Spring AI RAG 管道中的核心职责，并说明 `TikaDocumentReader` 相比其他 `DocumentReader` 实现的主要优势。

**答**：DocumentReader 职责**：从不同数据源读取原始文档，生成 `Document` 对象（含 `content` 与 `metadata`），是 RAG ETL 管道的入口。；TikaDocumentReader 优势**：基于 Apache Tika，自动检测并解析 PDF、DOCX、XLSX、PPTX、HTML、XML、TXT 等格式，无需按 MIME 类型分别配置解析器。。

### 关联知识点

- [向量与嵌入](向量与嵌入.md)
- [索引与存储](索引与存储.md)

---
## TokenTextSplitter 与普通 TextSplitter

> **模块**：文档 ETL 与分块 | **标签**：文档与分块 | **更新**：2026-05-28

### 核心概念

普通 TextSplitter：按字符数或段落等表面规则分块，不感知 LLM 的 token 限制。

### 要点

- **普通 TextSplitter**：按字符数或段落等表面规则分块，不感知 LLM 的 token 限制。
- **TokenTextSplitter**：按 token 数量分块，能精确保证每块在模型上下文窗口内。
- **推荐原因**：与 LLM 计费/限长对齐、减少截断浪费、跨语言更稳定。

### 代码示例

```java
TokenTextSplitter splitter = new TokenTextSplitter(
    500,   // chunkSize (tokens)
    50,    // chunkOverlap (tokens)
    "cl100k_base" // tokenizer name
);
List<Document> chunks = splitter.split(documents);
```

### 面试常问

**问**：在 RAG 的 ETL 流程中，TokenTextSplitter 与普通 TextSplitter 在分块依据上有什么本质区别？为什么推荐使用 TokenTextSplitter？

**答**：普通 TextSplitter**：按字符数或段落等表面规则分块，不感知 LLM 的 token 限制。；TokenTextSplitter**：按 token 数量分块，能精确保证每块在模型上下文窗口内。；推荐原因**：与 LLM 计费/限长对齐、减少截断浪费、跨语言更稳定。。

### 关联知识点

- [向量与嵌入](向量与嵌入.md)
- [索引与存储](索引与存储.md)

---
## Document 的 content 与 metadata

> **模块**：文档 ETL 与分块 | **标签**：文档与分块 | **更新**：2026-05-28

### 核心概念

Document 的 content 和 metadata 分别存储什么？在向量搜索中如何协同工作？

### 要点

| 特性 | content | metadata |
| :--- | :--- | :--- |
| 数据类型 | String | Map<String, Object> |
| 存储内容 | 文档主要文本 | 键值对描述信息 |
| 是否参与向量计算 | 是（被 Embedding 转为向量） | 否（不参与相似度计算） |
| 检索时作用 | 与查询向量算相似度 | 作为过滤器筛选文档 |
| 索引方式 | 向量索引 | 通常建标量索引加速过滤 |

**向量搜索协同流程**：

1. 生成查询向量。
2. 应用 metadata 过滤（`SearchRequest.withFilterExpression`）：预过滤缩小候选集，或后过滤再筛选。
3. 在过滤后的文档集中执行向量相似度计算。
4. 返回 TopK 最相似文档。

**设计优势**：通过 `tenant_id` 等实现多租户隔离；限定部门/时间/类型范围；先 metadata 缩小范围再算相似度，减少计算量。

### 代码示例

```java
Map<String, Object> metadata = new HashMap<>(extraMetadata);
metadata.put("tenant_id", tenantId);
metadata.put("user_id", userId);
metadata.put("created_at", LocalDateTime.now().toString());

Document doc = new Document(content, metadata);

// 带 metadata 过滤的检索请求
SearchRequest request = SearchRequest
    .query("用户查询的问题")
    .withTopK(5)
    .withSimilarityThreshold(0.7)
    .withFilterExpression("tenant_id == 'tenant123' && user_id == 'user456'");

List<Document> results = vectorStore.similaritySearch(request);
```

### 面试常问

**问**：Document 的 content 和 metadata 分别存储什么？在向量搜索中如何协同工作？

**答**：content :--- String 文档主要文本 是（被 Embedding 转为向量） 与查询向量算相似度 向量索引 **向量搜索协同流程**： 1. 生成查询向量。 2. 应用 metadata 过滤（`SearchRequest.withFilterExpression`）：预过滤缩小候选集，或后过滤再筛选。 3. 在过滤后的文档集中执行向量相似度计算。 4. 返回 TopK 最相似文档。 **设计优势**：通过 `tenan…

### 关联知识点

- [向量与嵌入](向量与嵌入.md)
- [索引与存储](索引与存储.md)

---
## TokenTextSplitter 参数 chunkSize 与 chunkOverlap

> **模块**：文档 ETL 与分块 | **标签**：文档与分块 | **更新**：2026-05-28

### 核心概念

chunkSize：每个块的最大 token 数。

### 要点

- **chunkSize**：每个块的最大 token 数。
- **chunkOverlap**：相邻块重叠的 token 数，避免语义在边界断裂。
- **示例**：块 1 为 token 1–500；块 2 从 451 起（重叠 50），即 451–950。

### 面试常问

**问**：chunkSize 和 chunkOverlap 分别控制什么？若 chunkSize=500, chunkOverlap=50，第二个块包含哪些 tokens？

**答**：chunkSize**：每个块的最大 token 数。；chunkOverlap**：相邻块重叠的 token 数，避免语义在边界断裂。；示例**：块 1 为 token 1–500；块 2 从 451 起（重叠 50），即 451–950。。

### 关联知识点

- [向量与嵌入](向量与嵌入.md)
- [索引与存储](索引与存储.md)

---
## 其他分块工具

> **模块**：文档 ETL 与分块 | **标签**：文档与分块 | **更新**：2026-05-28

### 核心概念

**SentenceSplitter**（Alibaba）：基于模型识别句子边界，中文友好。

### 要点

- **SentenceSplitter**（Alibaba）：基于模型识别句子边界，中文友好。
- **RecursiveCharacterTextSplitter**（Alibaba）：按分隔符优先级递归切割，适合长文本。

### 代码示例

```java
SentenceSplitter splitter = new SentenceSplitter(100);  // 最大100 token
List<Document> newDocuments = splitter.split(documents);

RecursiveCharacterTextSplitter splitter2 = new RecursiveCharacterTextSplitter();
List<Document> newDocs = splitter2.split(documents);
```

### 面试常问

**问**：除了 TokenTextSplitter，还有没有类似的分块工具？

**答**：SentenceSplitter**（Alibaba）：基于模型识别句子边界，中文友好。；RecursiveCharacterTextSplitter**（Alibaba）：按分隔符优先级递归切割，适合长文本。。

### 关联知识点

- [向量与嵌入](向量与嵌入.md)
- [索引与存储](索引与存储.md)

---
## KeywordMetadataEnricher 与 SummaryMetadataEnricher 存储位置

> **模块**：文档 ETL 与分块 | **标签**：文档与分块 | **更新**：2026-05-28

### 核心概念

Enricher 处理后将 `keywords`、`summary` 等字段写入 Document 的 **metadata**，随文档一并入库；后续可通过 metadata 过滤或混合检索利用这些字段提升召回。

### 要点

Enricher 处理后将 `keywords`、`summary` 等字段写入 Document 的 **metadata**，随文档一并入库；后续可通过 metadata 过滤或混合检索利用这些字段提升召回。

### 代码示例

```java
KeywordMetadataEnricher enricher = new KeywordMetadataEnricher(chatModel, 5);
List<Document> enriched = enricher.apply(List.of(doc));
// doc.getMetadata().get("keywords") -> ["Spring AI", "VectorStore"]
```

### 面试常问

**问**：KeywordMetadataEnricher 和 SummaryMetadataEnricher 生成的关键词和摘要最终存储在哪里？

**答**：Enricher 处理后将 `keywords`、`summary` 等字段写入 Document 的 **metadata**，随文档一并入库；后续可通过 metadata 过滤或混合检索利用这些字段提升召回。

### 关联知识点

- [向量与嵌入](向量与嵌入.md)
- [索引与存储](索引与存储.md)

---
## 上传文件 PDF/Excel/图片 处理原理

> **模块**：文档 ETL 与分块 | **标签**：DocumentReader, ETL, 多模态 | **更新**：2026-05-28

### 核心概念

文档类上传走 ETL 流水线（Extract → Transform → Load），由 `DocumentReader`、`DocumentTransformer`、`DocumentWriter` 解析并向量化；图像类可走多模态模型的视觉编码器直接理解；含图 PDF 需混合解析与并行融合。

### 要点

- **文档类（PDF/Excel/Word）**：`TikaDocumentReader` 等提取文本 → `TokenTextSplitter` 等切分 → 写入 `VectorStore`。
- **图像类**：不强制 ETL，可直接通过 `UserMessage.media` 交给多模态 LLM 做视觉理解。
- **含图 PDF 混合方案**：文本与图片分别提取；文本向量化入库，图片走多模态分析；最终在语义层合并检索或回答上下文。
- **流水线组件**：Reader 负责 Extract；Transformer 负责清洗/切分/元数据增强；Writer 负责 Load 至向量库。

### 代码示例

```java
Resource pdfResource = new FileSystemResource("upload/report.pdf");
TikaDocumentReader reader = new TikaDocumentReader(pdfResource);
List<Document> rawDocs = reader.read();

List<Document> chunks = tokenTextSplitter.apply(rawDocs);
vectorStore.add(chunks);
```

### 面试常问

**问**：用户上传 PDF、Excel 或图片时，Spring AI 分别如何处理？

**答**：PDF/Excel 走 DocumentReader ETL：提取文本、切分、嵌入入库；纯图片可用多模态模型的 media 输入直接理解；含图 PDF 需文本提取与图像分析并行，再在 RAG 或回答阶段融合两类结果。

### 关联知识点

- [DocumentReader 与 TikaDocumentReader](#documentreader-与-tikadocumentreader)
- [Spring AI 多模态输入与动态模型切换](Spring AI核心组件.md)

---
## 结构化输出与文本切分的职责边界

> **模块**：文档 ETL 与分块 | **标签**：Transform, TextSplitter | **更新**：2026-05-28

### 核心概念

「自动解析」（`.entity(Class)` 结构化输出）作用于 **模型响应**，解决格式不统一；「自定义分词/切分」作用于 **原始文档输入**，解决上下文窗口超限。二者阶段与对象完全不同，不可互换。

### 要点

| 维度 | 自动解析（结构化输出） | 自定义分词（文本切分） |
| :--- | :--- | :--- |
| 目的 | 非结构化文本 → Java 对象 | 长文本 → 语义块 |
| 作用对象 | AI **输出** | 原始文档 **输入** |
| 时机 | 生成响应之后 | 发送请求之前 |
| 解决问题 | 响应格式不统一 | 超出模型上下文窗口 |

**常用切分器**

- `TokenTextSplitter`：按 Token 硬性切分，可控 chunkSize/overlap
- `SentenceSplitter`：按句子语义边界
- `RecursiveCharacterTextSplitter`：分隔符递归切分

### 代码示例

```java
// 结构化输出：解析模型响应
Student student = ChatClient.create(chatModel).prompt()
    .user("Generate a student record")
    .call()
    .entity(Student.class);

// 文本切分：RAG 入库前
List<Document> chunks = new TokenTextSplitter(512, 50).apply(rawDocs);
```

### 面试常问

**问**：Spring AI 中「自动解析入参」与「自定义分词」有什么区别？

**答**：自动解析是 ChatClient `.entity()` 把模型输出映射为 POJO，发生在响应后；自定义分词是 TokenTextSplitter 等把长文档切成块，发生在请求前入库。前者管输出结构，后者管输入长度与检索粒度。

### 关联知识点

- [Spring AI Transform 结构化输出](Spring AI核心组件.md)
- [TokenTextSplitter 与普通 TextSplitter](#tokentextsplitter-与普通-textsplitter)

---
# -*- coding: utf-8 -*-
"""Parse interview Q&A, summarize answers, classify by topic, write to study/interview."""
import re
import os
from datetime import date
from collections import defaultdict

SOURCE = r"study/interview/original/template.md"
OUT_DIR = r"study/interview"
TODAY = date.today().strftime("%Y-%m-%d")

SECTION_START = re.compile(
    r"(?:^|\n)(?:##\s*(\d+)\.\s*(.+?)|(\d+)\.\s*(.+?))\s*(?:\n|$)",
    re.M,
)

# 按题目标题映射分类（根据语义，非单一文件）
CATEGORY_BY_TITLE = {
    "DocumentReader 与 TikaDocumentReader": "文档与分块",
    "TokenTextSplitter 与普通 TextSplitter": "文档与分块",
    "TokenTextSplitter 参数详解": "文档与分块",
    "其他分块工具": "文档与分块",
    "关键词/摘要存储位置": "文档与分块",
    "EmbeddingModel 与本地 ONNX 模型": "向量与嵌入",
    "VectorStore 相似度搜索与元数据过滤": "向量与嵌入",
    "VectorStore.add() 的两个职责": "向量与嵌入",
    "元数据过滤中的 eq vs in": "向量与嵌入",
    "VectorStore 内部调用链": "向量与嵌入",
    "QuestionAnswerAdvisor 缓存": "RAG Advisor",
    "QuestionAnswerAdvisor 工作流程": "RAG Advisor",
    "多路召回（向量 + BM25）": "RAG检索增强",
    "重排序（Rerank）集成": "RAG检索增强",
    "查询改写（Query Rewriting）": "RAG检索增强",
    "HyDE 实现": "RAG检索增强",
    "HyDE 核心思路": "RAG检索增强",
    "HyDE 不适用场景": "RAG检索增强",
    "智能路由（名词库）": "RAG检索增强",
    "RRF 多路召回融合": "RAG检索增强",
    "向量索引优化（HNSW vs IVFFlat）": "索引与存储",
    "SimpleVectorStore vs PgVector": "索引与存储",
    "可观测性（Metrics & Tracing）": "可观测与评估",
    "Ragas 评估集成": "可观测与评估",
    "可观测性大盘（Prometheus + Grafana）": "可观测与评估",
    "Agent 与 RAG 协同（@Tool 注册与动态加载）": "Agent与对话",
    "多轮对话记忆管理": "Agent与对话",
    "基础巩固：ChatClient vs ChatModel": "Spring AI基础",
    "Prompt 与 UserMessage 的关系": "Spring AI基础",
    "Advisor 的作用与位置": "Spring AI基础",
    "Document 的 content 与 metadata": "Spring AI基础",
    "异步并行检索与超时控制": "性能与高可用",
    "多租户数据隔离": "性能与高可用",
    "超时控制": "性能与高可用",
}

# 精炼答（非原文复制）
SUMMARY_BY_TITLE = {
    "DocumentReader 与 TikaDocumentReader": "DocumentReader 将原始数据读成带 content/metadata 的 Document；TikaDocumentReader 基于 Apache Tika 自动识别并解析 PDF、Office、HTML 等多格式，无需为每种格式单独配解析器。",
    "TokenTextSplitter 与普通 TextSplitter": "普通分块按字符或段落切分，不感知 token 上限；TokenTextSplitter 按 token 切分，与模型上下文和计费对齐，跨语言更稳，生产 RAG 更推荐后者。",
    "EmbeddingModel 与本地 ONNX 模型": "embed(Document) 返回 EmbeddingResponse（内含向量列表）；本地 ONNX 可用 OnnxEmbeddingModel（spring-ai-transformers），如 all-MiniLM-L6-v2。",
    "VectorStore 相似度搜索与元数据过滤": "用 SearchRequest 组合查询与 Filter.Expression（如 category=technology 且 score>0.7），similaritySearch 返回 Top-K 文档。",
    "QuestionAnswerAdvisor 缓存": "对归一化 query 或向量哈希做缓存 Key，设 TTL；含时间敏感词时禁用缓存；可用 @Cacheable 或自定义 CacheManager，避免脏读。",
    "多路召回（向量 + BM25）": "向量语义召回与 BM25 关键词召回并行；ElasticsearchVectorStore 可开 hybridSearch 调权重，否则双路检索后合并去重再 Rerank。",
    "重排序（Rerank）集成": "多路召回后用 CrossEncoder 等重排；Spring AI Alibaba 可用 RetrievalRerankAdvisor，在 ChatClient 默认 Advisor 链中注入，流程为检索→重排→生成。",
    "查询改写（Query Rewriting）": "用 RewriteQueryTransformer、MultiQueryExpander、CompressionQueryTransformer 等改写或扩展 query，经 RetrievalAugmentationAdvisor 配置，缓解表述不清导致的漏召。",
    "可观测性（Metrics & Tracing）": "Micrometer Tracing 打 Span；关注检索延迟、Top-K 命中、重排收益、缓存命中、Token 消耗等指标。",
    "Ragas 评估集成": "建议 Docker 化 Python Ragas 服务 HTTP 调用；CI 中跑数据集、算 context_recall 等指标并设质量门禁；Java 侧可用 Dokimos 等做轻量评估。",
    "向量索引优化（HNSW vs IVFFlat）": "HNSW 查询快、内存高、召回好；IVFFlat 构建快、省内存需训练。PgVector/Milvus/Redis 各有 HNSW 参数与分区策略，按数据量与延迟选型。",
    "可观测性大盘（Prometheus + Grafana）": "接入 micrometer-registry-prometheus，暴露 actuator 指标；Grafana 看 LLM/向量客户端耗时与 RAG 相关 score，并配置 p99、Token 突增等告警。",
    "异步并行检索与超时控制": "@Async + CompletableFuture 并行查多库/分区，orTimeout 与 exceptionally 兜底，合并去重后再重排或生成。",
    "HyDE 实现": "先让 LLM 生成假设性答案文档，再对答案做向量检索；实现 QueryTransformer，在 transform 中生成假设文档作为检索 query。",
    "多租户数据隔离": "写入时 metadata 强制 tenant_id；检索用 Filter.Expression.eq(\"tenant_id\", id)；可按单库+过滤、独立集合或库隔离。",
    "Agent 与 RAG 协同（@Tool 注册与动态加载）": "每知识库 @Tool 声明 name/description，Registry 扫描注册到 ChatClient；工具过多可做向量发现；本地无结果再降级 web_search 或 LLM。",
    "多轮对话记忆管理": "短期用 MessageWindowChatMemory + Advisor 控窗口；长期用 Jdbc 或向量库存摘要；超窗压缩历史，避免膨胀。",
    "基础巩固：ChatClient vs ChatModel": "ChatModel 直连模型 API；ChatClient 是门面，封装流式、Advisor、Tool、模板。日常用 Client，调试或极简调用才用 Model。",
    "Prompt 与 UserMessage 的关系": "Prompt 是消息列表容器；UserMessage 是其中表示用户输入的一条，还可含 SystemMessage、Tool 消息等。",
    "Advisor 的作用与位置": "Advisor 类似切面，around 包裹 ChatClient→ChatModel 全链路，可链式增强检索、记忆、日志等。",
    "Document 的 content 与 metadata": "content 存正文；metadata 存 tenant_id、source、page 等，用于过滤、隔离与溯源。",
    "TokenTextSplitter 参数详解": "chunkSize 为块最大 token 数，chunkOverlap 为相邻块重叠 token；如 500/50 时第二块约从第 451 个 token 起。",
    "其他分块工具": "还有 SentenceSplitter、RecursiveCharacterTextSplitter（Alibaba 等），中文场景可优先句子或递归字符切分。",
    "VectorStore.add() 的两个职责": "先 EmbeddingModel 把 content 转向量，再持久化 content+metadata+向量；去重策略因实现而异（内存按 id 覆盖，库常 upsert）。",
    "关键词/摘要存储位置": "KeywordMetadataEnricher、SummaryMetadataEnricher 的结果写入 Document.metadata 的 keywords、summary 字段。",
    "元数据过滤中的 eq vs in": "keywords 等多值字段应用 Filter.in 而非 eq；可结合向量检索与 metadata 过滤做混合召回。",
    "SimpleVectorStore vs PgVector": "SimpleVectorStore 内存易失，适合开发；PgVector 基于 PostgreSQL 持久化，适合生产。",
    "QuestionAnswerAdvisor 工作流程": "before 阶段 similaritySearch 取文档；生成前把 Document.content 文本拼进 Prompt，传的是文本不是向量。",
    "VectorStore 内部调用链": "embed(query) 得查询向量，再执行 ANN（如 pgvector <=>），封装为 Document 列表返回。",
    "HyDE 核心思路": "用假设答案文档的向量检索，而非仅改写问题；与 Query2Vec 直接编码问题不同，适合模糊问法。",
    "HyDE 不适用场景": "专有名词、已很规范的问题不必 HyDE，额外 LLM 成本不值。",
    "智能路由（名词库）": "可用名词库/规则判断：命中走直通检索，未命中再走 HyDE，平衡成本与召回。",
    "RRF 多路召回融合": "RRF 对各路的 rank 贡献 1/(K+rank) 求和（K 常取 60），按融合分排序选文档。",
    "超时控制": "CompletableFuture.supplyAsync 检索链路上加 orTimeout，超时 exceptionally 返回空列表，避免拖垮主请求。",
}


def infer_category(title):
    if title in CATEGORY_BY_TITLE:
        return CATEGORY_BY_TITLE[title]
    t = title.lower()
    if any(k in t for k in ("hyde", "召回", "rerank", "改写", "rrf", "bm25")):
        return "RAG检索增强"
    if any(k in t for k in ("vector", "embedding", "相似", "metadata", "filter")):
        return "向量与嵌入"
    if any(k in t for k in ("split", "document", "chunk", "tika", "分块", "enricher")):
        return "文档与分块"
    if any(k in t for k in ("advisor", "questionanswer")):
        return "RAG Advisor"
    if any(k in t for k in ("agent", "memory", "chatclient", "prompt", "tool")):
        return "Agent与对话" if "agent" in t or "memory" in t else "Spring AI基础"
    if any(k in t for k in ("prometheus", "ragas", "tracing", "可观测")):
        return "可观测与评估"
    if any(k in t for k in ("hnsw", "pgvector", "索引", "simplevector")):
        return "索引与存储"
    if any(k in t for k in ("async", "超时", "租户", "并行")):
        return "性能与高可用"
    return "其他"


def read_source():
    with open(SOURCE, "r", encoding="utf-8") as f:
        return f.read()


def split_by_sections(text):
    idx = text.find("\n---\n")
    body = text[idx:] if idx != -1 else text
    matches = list(SECTION_START.finditer(body))
    chunks = []
    for i, m in enumerate(matches):
        start = m.start() + (1 if body[m.start()] == "\n" else 0)
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        chunk = body[start:end].strip()
        chunk = re.sub(r"\n*---\s*$", "", chunk)
        title = (m.group(2) or m.group(4) or "").strip()
        chunks.append((title, chunk))
    return chunks


def parse_section(body, title):
    q = ""
    mq = re.search(r"\*\*问\*\*[：:]\s*(.+?)(?=\n\n\*\*答\*\*|\n\n\*\*参考|\n\n答[：:]|$)", body, re.S)
    if mq:
        q = mq.group(1).strip()
    else:
        mq = re.search(r"(?:^|\n)问[：:]\s*(.+?)(?=\n\n答[：:]|\n\n参考|$)", body, re.S)
        if mq:
            q = mq.group(1).strip()
    a = SUMMARY_BY_TITLE.get(title, "")
    if not a:
        mref = re.search(r"(?:\*\*参考答案\*\*|参考答案)[：:]\s*(.+?)(?=\n\n\*\*评价|\n\n评价|$)", body, re.S)
        if mref:
            raw = mref.group(1).strip()
            raw = re.sub(r"```[\s\S]*?```", "[代码略]", raw)
            lines = [ln.strip() for ln in raw.split("\n") if ln.strip() and not ln.strip().startswith("java")]
            a = "；".join(lines[:4])[:500]
    if not a:
        a = "（待补充）"
    return {"title": title, "q": q or title, "a": a, "category": infer_category(title)}


def format_entry(entry):
    return (
        f"{entry['title']}\n"
        f"问：{entry['q']}\n"
        f"答：{entry['a']}\n"
        f"分类标签：{entry['category']} | 更新日期：{TODAY}\n"
    )


def write_category_file(category, entries):
    path = os.path.join(OUT_DIR, category + "问答.md")
    lines = [
        f"# {category} 问答",
        "",
        f"<!-- 最后更新于 {TODAY} -->",
        "",
    ]
    for i, e in enumerate(entries):
        if i > 0:
            lines.append("\n---\n")
        lines.append(format_entry(e))
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return path, len(entries)


def remove_obsolete_outputs():
    obsolete = ["Spring AI RAG问答.md", "Spring AI RAG问答.bak.md"]
    for name in obsolete:
        p = os.path.join(OUT_DIR, name)
        if os.path.isfile(p):
            os.remove(p)


def append_log(created, updated, total):
    log_path = os.path.join(OUT_DIR, "_merge_log.md")
    block = (
        f"\n## {TODAY}\n\n"
        f"- 源文件：`{SOURCE}`\n"
        f"- 新建：{', '.join('`' + c + '`' for c in created) or '无'}\n"
        f"- 更新：{', '.join('`' + u + '`' for u in updated) or '无'}\n"
        f"- 处理条数：{total}\n"
        f"- 备份：无（按规则不生成 .bak）\n"
    )
    if os.path.isfile(log_path):
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(block)
    else:
        with open(log_path, "w", encoding="utf-8") as f:
            f.write("# 问答合并日志\n" + block)


def main():
    sections = split_by_sections(read_source())
    entries = []
    for title, chunk in sections:
        e = parse_section(chunk, title)
        if e["q"]:
            entries.append(e)

    by_cat = defaultdict(list)
    for e in entries:
        by_cat[e["category"]].append(e)

    os.makedirs(OUT_DIR, exist_ok=True)
    remove_obsolete_outputs()

    created = []
    for cat in sorted(by_cat.keys()):
        path, n = write_category_file(cat, by_cat[cat])
        created.append(f"{cat}问答.md（{n}条）")

    append_log(created, [], len(entries))
    print("OK total=%d files=%s" % (len(entries), ", ".join(created)))


if __name__ == "__main__":
    main()

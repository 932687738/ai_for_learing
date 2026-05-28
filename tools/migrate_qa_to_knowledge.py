#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Migrate study/interview/*问答.md to study/interview/knowledge/*.md standard format."""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INTERVIEW = ROOT / "study" / "interview"
KNOWLEDGE = INTERVIEW / "knowledge"
TODAY = date.today().isoformat()

SOURCE_TO_MODULE = {
    "Spring AI基础问答.md": "spring-ai-core",
    "文档与分块问答.md": "document-etl-chunking",
    "向量与嵌入问答.md": "embedding-vectorstore",
    "索引与存储问答.md": "index-storage",
    "RAG Advisor问答.md": "rag-advisor",
    "可观测与评估问答.md": "observability-evaluation",
    "性能与高可用问答.md": "performance-reliability",
}

MODULE_META = {
    "spring-ai-core": ("Spring AI 核心组件", "ChatClient、Prompt、Advisor、Transform 等框架基础抽象。"),
    "document-etl-chunking": ("文档 ETL 与分块", "Document 读取、切分、元数据增强与 ETL 流水线。"),
    "embedding-vectorstore": ("向量与嵌入", "EmbeddingModel 与 VectorStore 读写机制。"),
    "index-storage": ("索引与存储", "向量索引类型、相似度策略、多租户与 ES/PgVector 配置。"),
    "rag-advisor": ("RAG Advisor", "QuestionAnswerAdvisor 与回答质量检测等横切能力。"),
    "rag-retrieval-strategies": ("RAG 检索策略", "多路召回、查询扩展/改写、混合检索与 Rerank。"),
    "rag-retrieval-hyde": ("HyDE 假设文档嵌入", "HyDE 原理、实现、衍生方案与智能路由。"),
    "rag-retrieval-rrf": ("RRF 混合检索融合", "Reciprocal Rank Fusion 公式、配置与对比。"),
    "rag-memory": ("RAG 长期记忆", "向量库跨会话记忆与 MemoryAdvisor 注入。"),
    "agent-memory": ("Agent 记忆体系", "ChatMemory 短期记忆与 AutoMemoryTools 长期记忆。"),
    "agent-architecture": ("Agent 架构与协同", "ReAct、@Tool、Skills/Tools/MCP 与 RAG 协同。"),
    "agent-workflow": ("Agent 工作流模式", "串行/循环/路由/并行 Agent 与 CoT/ToT 推理。"),
    "observability-evaluation": ("可观测与评估", "Micrometer、Tracing、Ragas 与监控大盘。"),
    "performance-reliability": ("性能与高可用", "并行检索、超时控制与响应缓存。"),
    "other": ("其他", "暂未归类的知识点。"),
}

MODULE_FILENAME = {
    "spring-ai-core": "Spring AI核心组件.md",
    "document-etl-chunking": "文档ETL与分块.md",
    "embedding-vectorstore": "向量与嵌入.md",
    "index-storage": "索引与存储.md",
    "rag-advisor": "RAG Advisor.md",
    "rag-retrieval-strategies": "RAG检索策略.md",
    "rag-retrieval-hyde": "HyDE假设文档嵌入.md",
    "rag-retrieval-rrf": "RRF混合检索融合.md",
    "rag-memory": "RAG长期记忆.md",
    "agent-memory": "Agent记忆体系.md",
    "agent-architecture": "Agent架构与协同.md",
    "agent-workflow": "Agent工作流模式.md",
    "observability-evaluation": "可观测与评估.md",
    "performance-reliability": "性能与高可用.md",
    "other": "其他.md",
}


def module_cn(module_id: str) -> str:
    return MODULE_META.get(module_id, MODULE_META["other"])[0]

RAG_TITLE_ROUTES = [
    (r"HyDE|HyPE|HyQE|SL-HyDE|假设文档|智能路由判断是否", "rag-retrieval-hyde"),
    (r"RRF|倒数排名|Reciprocal Rank|混合检索需要 RRF|融合方法对比", "rag-retrieval-rrf"),
    (r"跨会话长期记忆|MemoryAdvisor|向量数据库实现跨会话", "rag-memory"),
    (r"Agent 流水线.*RAG|Agent 流水线中的并行", "agent-architecture"),
]

AGENT_TITLE_ROUTES = [
    (r"短期记忆|AutoMemoryTools|多轮对话记忆|记忆类型对比", "agent-memory"),
    (r"ReAct|@Tool|Skills[/、]|MCP", "agent-architecture"),
    (r"Sequential|LoopAgent|共享 ChatMemory|Orchestrator|CoT|ToT|工作流模式|Handoff|交接", "agent-workflow"),
]

# 同一文件内按标题精确路由（优先级高于 SOURCE_TO_MODULE）
TITLE_OVERRIDES = {
    "检索 Query 对象 vs 直接传字符串": "rag-retrieval-strategies",
    "Spring AI 记忆类型对比与选型": "agent-memory",
}


@dataclass
class Entry:
    title: str
    question: str
    answer: str
    code: str
    tags: str
    module: str
    source: str


def slug(text: str) -> str:
    s = text.lower().strip()
    s = re.sub(r"[^\w\u4e00-\u9fff\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    return s[:80] or "section"


def route_entry(source_file: str, title: str, question: str) -> str:
    if title in TITLE_OVERRIDES:
        return TITLE_OVERRIDES[title]
    text = f"{title} {question}"
    if source_file == "RAG检索增强问答.md":
        for pattern, module in RAG_TITLE_ROUTES:
            if re.search(pattern, text, re.I):
                return module
        return "rag-retrieval-strategies"
    if source_file == "Agent与对话问答.md":
        for pattern, module in AGENT_TITLE_ROUTES:
            if re.search(pattern, text, re.I):
                return module
        return "agent-workflow"
    return SOURCE_TO_MODULE.get(source_file, "other")


def parse_qa_file(path: Path) -> list[Entry]:
    content = path.read_text(encoding="utf-8")
    chunks = re.split(r"\n---\n", content)
    entries: list[Entry] = []
    for chunk in chunks:
        chunk = chunk.strip()
        chunk = re.sub(r"^<!--[\s\S]*?-->\s*", "", chunk).strip()
        if not chunk.startswith("## "):
            continue
        m_title = re.match(r"^## (.+)$", chunk, re.M)
        if not m_title:
            continue
        title = m_title.group(1).strip()
        q_idx = chunk.find("**问**")
        a_idx = chunk.find("**答**")
        if q_idx == -1 or a_idx == -1:
            continue
        question = chunk[q_idx:a_idx]
        question = re.sub(r"^\*\*问\*\*[：:]\s*", "", question, flags=re.M).strip()

        tag_m = re.search(r"^分类标签[：:].+$", chunk, re.M)
        tag_end = tag_m.start() if tag_m else len(chunk)
        body = chunk[a_idx:tag_end]

        code_marker = re.search(r"\*\*代码示例[^*]*\*\*", body)
        if code_marker:
            answer = body[: code_marker.start()]
            code_section = body[code_marker.start() :]
        else:
            answer = body
            code_section = ""

        answer = re.sub(r"^\*\*答\*\*[：:]\s*", "", answer, flags=re.M).strip()
        code_blocks = re.findall(r"```[\s\S]+?```", code_section)
        code = "\n\n".join(code_blocks)

        tm = re.search(r"分类标签[：:]\s*(.+?)\s*\|\s*更新日期", chunk)
        tags = tm.group(1).strip() if tm else ""
        module = route_entry(path.name, title, question)
        entries.append(Entry(title, question, answer, code, tags, module, path.name))
    return entries


def summarize_interview_answer(answer: str) -> str:
    lines = [ln.strip() for ln in answer.splitlines() if ln.strip()]
    bullets = [ln for ln in lines if ln.startswith("- ") or ln.startswith("* ")]
    if bullets:
        parts = []
        for b in bullets[:4]:
            text = b.lstrip("-* ").strip()
            text = re.sub(r"\*\*([^*]+)\*\*[：:]\s*", r"\1：", text)
            text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
            parts.append(text)
        return "；".join(parts) + ("。" if parts else "")
    plain = " ".join(lines)
    plain = re.sub(r"\|[^|]+\|", " ", plain)
    plain = re.sub(r"\s+", " ", plain).strip()
    if len(plain) > 220:
        plain = plain[:220].rstrip() + "…"
    return plain or answer[:200]


def format_entry(entry: Entry) -> str:
    interview_ans = summarize_interview_answer(entry.answer)
    related = suggest_related(entry.module)
    parts = [
        f"## {entry.title}",
        "",
        f"> **模块**：{module_cn(entry.module)} | **标签**：{entry.tags or entry.module} | **更新**：{TODAY}",
        "",
        "### 核心概念",
        "",
        core_concept(entry.answer, entry.question),
        "",
        "### 要点",
        "",
        entry.answer if entry.answer else interview_ans,
        "",
    ]
    if entry.code:
        parts.extend(["### 代码示例", "", entry.code, ""])
    parts.extend([
        "### 面试常问",
        "",
        f"**问**：{entry.question}",
        "",
        f"**答**：{interview_ans}",
        "",
        "### 关联知识点",
        "",
    ])
    for rel in related:
        parts.append(f"- [{rel[0]}]({rel[1]})")
    parts.append("")
    parts.append("---")
    return "\n".join(parts)


def core_concept(answer: str, question: str) -> str:
    lines = [ln.strip() for ln in answer.splitlines() if ln.strip()]
    for ln in lines:
        if ln.startswith("- ") and len(ln) > 10:
            text = re.sub(r"^\*\*([^*]+)\*\*[：:]\s*", r"\1：", ln.lstrip("- "))
            return text
    if lines:
        first = lines[0]
        if not first.startswith("|"):
            return first[:300]
    return question


def suggest_related(module: str) -> list[tuple[str, str]]:
    rel_map = {
        "spring-ai-core": [("RAG Advisor", MODULE_FILENAME["rag-advisor"]), ("文档 ETL 与分块", MODULE_FILENAME["document-etl-chunking"])],
        "document-etl-chunking": [("向量与嵌入", MODULE_FILENAME["embedding-vectorstore"]), ("索引与存储", MODULE_FILENAME["index-storage"])],
        "embedding-vectorstore": [("索引与存储", MODULE_FILENAME["index-storage"]), ("RAG 检索策略", MODULE_FILENAME["rag-retrieval-strategies"])],
        "index-storage": [("RAG 检索策略", MODULE_FILENAME["rag-retrieval-strategies"]), ("RRF 混合检索融合", MODULE_FILENAME["rag-retrieval-rrf"])],
        "rag-advisor": [("Spring AI 核心组件", MODULE_FILENAME["spring-ai-core"]), ("RAG 检索策略", MODULE_FILENAME["rag-retrieval-strategies"])],
        "rag-retrieval-strategies": [("HyDE 假设文档嵌入", MODULE_FILENAME["rag-retrieval-hyde"]), ("RRF 混合检索融合", MODULE_FILENAME["rag-retrieval-rrf"])],
        "rag-retrieval-hyde": [("RAG 检索策略", MODULE_FILENAME["rag-retrieval-strategies"]), ("RRF 混合检索融合", MODULE_FILENAME["rag-retrieval-rrf"])],
        "rag-retrieval-rrf": [("RAG 检索策略", MODULE_FILENAME["rag-retrieval-strategies"]), ("索引与存储", MODULE_FILENAME["index-storage"])],
        "rag-memory": [("Agent 记忆体系", MODULE_FILENAME["agent-memory"]), ("Spring AI 核心组件", MODULE_FILENAME["spring-ai-core"])],
        "agent-memory": [("RAG 长期记忆", MODULE_FILENAME["rag-memory"]), ("Agent 架构与协同", MODULE_FILENAME["agent-architecture"])],
        "agent-architecture": [("Agent 工作流模式", MODULE_FILENAME["agent-workflow"]), ("RAG 检索策略", MODULE_FILENAME["rag-retrieval-strategies"])],
        "agent-workflow": [("Agent 架构与协同", MODULE_FILENAME["agent-architecture"]), ("Agent 记忆体系", MODULE_FILENAME["agent-memory"])],
        "observability-evaluation": [("RAG 检索策略", MODULE_FILENAME["rag-retrieval-strategies"]), ("性能与高可用", MODULE_FILENAME["performance-reliability"])],
        "performance-reliability": [("RAG 检索策略", MODULE_FILENAME["rag-retrieval-strategies"]), ("索引与存储", MODULE_FILENAME["index-storage"])],
    }
    return rel_map.get(module, [])


def build_module_file(module_id: str, entries: list[Entry]) -> str:
    title, desc = MODULE_META[module_id]
    toc = []
    body_parts = []
    for e in entries:
        anchor = slug(e.title)
        toc.append(f"- [{e.title}](#{anchor})")
        body_parts.append(format_entry(e))
    header = [
        f"<!-- 模块：{module_cn(module_id)} | 最后更新于 {TODAY} -->",
        "",
        f"# {title}",
        "",
        f"> {desc}",
        "",
        "## 目录",
        "",
        *toc,
        "",
        "---",
        "",
    ]
    return "\n".join(header) + "\n".join(body_parts)


def build_readme(counts: dict[str, int]) -> str:
    lines = [
        "# Spring AI 面试知识点索引",
        "",
        f"> 最后更新于 {TODAY}。分类体系见 [`.cursor/knowledge-taxonomy.md`](../../../.cursor/knowledge-taxonomy.md)。",
        "",
        "## 模块列表",
        "",
        "| 模块 | 文件 | 知识点数 |",
        "| :--- | :--- | ---: |",
    ]
    order = list(MODULE_META.keys())
    total = 0
    for mid in order:
        if mid == "other" and counts.get(mid, 0) == 0:
            continue
        title, _ = MODULE_META[mid]
        fname = MODULE_FILENAME[mid]
        c = counts.get(mid, 0)
        if c == 0:
            continue
        total += c
        lines.append(f"| {title} | [{fname}]({fname}) | {c} |")
    lines.extend(["", f"**合计**：{total} 个知识点", ""])
    return "\n".join(lines)


def main() -> int:
    KNOWLEDGE.mkdir(parents=True, exist_ok=True)
    qa_files = sorted(INTERVIEW.glob("*问答.md"))
    if not qa_files:
        print("No *问答.md files found.", file=sys.stderr)
        return 1

    by_module: dict[str, list[Entry]] = defaultdict(list)
    for path in qa_files:
        for entry in parse_qa_file(path):
            by_module[entry.module].append(entry)

    counts: dict[str, int] = {}
    for module_id, entries in by_module.items():
        if module_id not in MODULE_META:
            module_id = "other"
        fname = KNOWLEDGE / MODULE_FILENAME[module_id]
        counts[module_id] = len(entries)
        fname.write_text(build_module_file(module_id, entries), encoding="utf-8")
        print(f"Wrote {fname.name}: {len(entries)} entries")

    (KNOWLEDGE / "索引.md").write_text(build_readme(counts), encoding="utf-8")
    print(f"Wrote 索引.md, total {sum(counts.values())} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

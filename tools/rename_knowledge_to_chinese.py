#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rename knowledge/*.md to Chinese filenames and fix internal links."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "study" / "interview" / "knowledge"

# module_id -> (中文模块名, 中文文件名)
MODULE_CN = {
    "spring-ai-core": ("Spring AI 核心组件", "Spring AI核心组件.md"),
    "document-etl-chunking": ("文档 ETL 与分块", "文档ETL与分块.md"),
    "embedding-vectorstore": ("向量与嵌入", "向量与嵌入.md"),
    "index-storage": ("索引与存储", "索引与存储.md"),
    "rag-advisor": ("RAG Advisor", "RAG Advisor.md"),
    "rag-retrieval-strategies": ("RAG 检索策略", "RAG检索策略.md"),
    "rag-retrieval-hyde": ("HyDE 假设文档嵌入", "HyDE假设文档嵌入.md"),
    "rag-retrieval-rrf": ("RRF 混合检索融合", "RRF混合检索融合.md"),
    "rag-memory": ("RAG 长期记忆", "RAG长期记忆.md"),
    "agent-memory": ("Agent 记忆体系", "Agent记忆体系.md"),
    "agent-architecture": ("Agent 架构与协同", "Agent架构与协同.md"),
    "agent-workflow": ("Agent 工作流模式", "Agent工作流模式.md"),
    "observability-evaluation": ("可观测与评估", "可观测与评估.md"),
    "performance-reliability": ("性能与高可用", "性能与高可用.md"),
    "other": ("其他", "其他.md"),
}

EN_TO_CN_FILE = {f"{mid}.md": meta[1] for mid, meta in MODULE_CN.items()}
EN_TO_CN_FILE["README.md"] = "索引.md"

ID_TO_CN_NAME = {mid: meta[0] for mid, meta in MODULE_CN.items()}


def fix_content(text: str) -> str:
    for old, new in sorted(EN_TO_CN_FILE.items(), key=lambda x: -len(x[0])):
        text = text.replace(old, new)
    for mid, cn in ID_TO_CN_NAME.items():
        text = text.replace(f"<!-- 模块：{mid} |", f"<!-- 模块：{cn} |")
        text = text.replace(f"> **模块**：{mid} |", f"> **模块**：{cn} |")
    text = text.replace(
        "](../../../.cursor/knowledge-taxonomy.md)",
        "](../../../.cursor/knowledge-taxonomy.md)",
    )
    text = text.replace(
        "](../../.cursor/knowledge-taxonomy.md)",
        "](../../../.cursor/knowledge-taxonomy.md)",
    )
    return text


def main() -> None:
    if not KNOWLEDGE.is_dir():
        raise SystemExit(f"Not found: {KNOWLEDGE}")

    md_files = list(KNOWLEDGE.glob("*.md"))
    updated: dict[Path, str] = {}
    for path in md_files:
        updated[path] = fix_content(path.read_text(encoding="utf-8"))

    for path, content in updated.items():
        new_name = EN_TO_CN_FILE.get(path.name, path.name)
        target = KNOWLEDGE / new_name
        target.write_text(content, encoding="utf-8")
        if target.resolve() != path.resolve():
            path.unlink()
            print(f"Renamed: {path.name} -> {new_name}")
        else:
            print(f"Updated: {path.name}")


if __name__ == "__main__":
    main()

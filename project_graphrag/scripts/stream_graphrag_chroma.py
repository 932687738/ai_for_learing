#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple


EXCLUDED_DIRS = {
    ".git",
    ".idea",
    ".cursor",
    ".vscode",
    "node_modules",
    "target",
    "build",
    "dist",
    "out",
    "__pycache__",
    ".mvn",
    ".gradle",
    ".lingma",
    "log",
    "本地仓库路程",
}

SOURCE_EXTENSIONS = {
    ".java": "java",
    ".kt": "kotlin",
    ".xml": "xml",
    ".sql": "sql",
    ".properties": "properties",
    ".yml": "yaml",
    ".yaml": "yaml",
    ".ts": "typescript",
    ".tsx": "typescript",
    ".js": "javascript",
    ".jsx": "javascript",
    ".py": "python",
    ".go": "go",
    ".cs": "csharp",
    ".pom": "xml",
}

CALL_KEYWORDS = {
    "if",
    "for",
    "while",
    "switch",
    "catch",
    "return",
    "new",
    "throw",
    "super",
    "this",
    "class",
    "interface",
    "enum",
    "try",
    "else",
    "do",
    "case",
    "default",
    "synchronized",
}

JAVA_MODIFIERS = (
    "public",
    "private",
    "protected",
    "static",
    "final",
    "abstract",
    "synchronized",
    "native",
    "strictfp",
    "default",
    "transient",
    "volatile",
)

EMBEDDING_DIM = 384


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def stable_id(prefix: str, *parts: object) -> str:
    raw = "|".join(str(p) for p in parts)
    return f"{prefix}_{hashlib.sha1(raw.encode('utf-8', errors='ignore')).hexdigest()[:32]}"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def text_embedding_deterministic(text: str, dim: int = EMBEDDING_DIM) -> List[float]:
    vec: List[float] = [0.0] * dim
    tokens = re.findall(r"[\w.\-/:\u4e00-\u9fff]+", text.lower())[:512]
    if not tokens:
        tokens = [hashlib.sha1(text.encode("utf-8", errors="ignore")).hexdigest()]
    for tok in tokens:
        h = hashlib.blake2b(tok.encode("utf-8", errors="ignore"), digest_size=8).digest()
        bucket = int.from_bytes(h[:4], "big") % dim
        sign = 1.0 if (h[4] & 1) else -1.0
        vec[bucket] += sign
    norm = math.sqrt(sum(x * x for x in vec)) or 1.0
    return [x / norm for x in vec]


def safe_read(path: Path, max_bytes: int) -> Optional[str]:
    try:
        if path.stat().st_size > max_bytes:
            return None
        data = path.read_bytes()
        if b"\x00" in data[:4096]:
            return None
        for enc in ("utf-8", "utf-8-sig", "gb18030", "latin-1"):
            try:
                return data.decode(enc)
            except UnicodeDecodeError:
                continue
        return data.decode("utf-8", errors="replace")
    except Exception:
        return None


def line_of(text: str, index: int) -> int:
    return text.count("\n", 0, max(0, index)) + 1


def compact(s: str, limit: int = 1800) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    return s[:limit]


def scalar_meta(meta: Dict[str, Any]) -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    for k, v in meta.items():
        if v is None:
            continue
        if isinstance(v, bool):
            out[k] = v
        elif isinstance(v, int):
            out[k] = v
        elif isinstance(v, float):
            out[k] = float(v)
        else:
            out[k] = str(v)[:2048]
    return out


class StatusWriter:
    def __init__(self, graph_root: Path):
        self.graph_root = graph_root
        self.path = graph_root / "task_status.json"
        self.stream_path = graph_root / "stream_progress.json"
        self.started_at = now_iso()

    def write(self, **kwargs: Any) -> None:
        data = {
            "tasks": {
                "STREAM_GRAPH_CHROMA": {
                    "task_id": "stream-from-scratch",
                    "task_type": "STREAM_GRAPH_CHROMA",
                    "status": kwargs.get("status", "running"),
                    "start_time": self.started_at,
                    "end_time": kwargs.get("end_time"),
                    "processed_targets": kwargs.get("processed_targets", [])[-50:],
                    "summary": kwargs.get("summary", ""),
                }
            },
            "history": [
                {
                    "task_id": "stream-from-scratch",
                    "task_type": "STREAM_GRAPH_CHROMA",
                    "status": kwargs.get("status", "running"),
                    "start_time": self.started_at,
                    "end_time": kwargs.get("end_time"),
                    "summary": kwargs.get("summary", ""),
                }
            ],
            "last_updated": now_iso(),
            "stream": kwargs,
        }
        tmp = self.path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        replace_with_retry(tmp, self.path)
        tmp2 = self.stream_path.with_suffix(".json.tmp")
        tmp2.write_text(json.dumps(kwargs, ensure_ascii=False, indent=2), encoding="utf-8")
        replace_with_retry(tmp2, self.stream_path)


def replace_with_retry(src: Path, dst: Path, attempts: int = 12, delay: float = 0.25) -> None:
    last: Optional[Exception] = None
    for _ in range(attempts):
        try:
            os.replace(src, dst)
            return
        except PermissionError as ex:
            last = ex
            time.sleep(delay)
    if last:
        raise last


class JsonlWriter:
    def __init__(self, path: Path):
        self.path = path
        self.f = path.open("w", encoding="utf-8", newline="\n")

    def write_many(self, rows: Iterable[dict]) -> None:
        for row in rows:
            self.f.write(json.dumps(row, ensure_ascii=False) + "\n")
        self.f.flush()
        os.fsync(self.f.fileno())

    def close(self) -> None:
        self.f.close()


class ChromaSink:
    def __init__(self, repo_root: Path, persist_dir: Path, nodes_collection: str, edges_collection: str):
        sys.path.insert(0, str(repo_root))
        from tools import chroma_crud  # type: ignore

        chromadb = chroma_crud._require_chroma()
        self.client = chromadb.PersistentClient(path=str(persist_dir.resolve()))
        self.nodes_collection_name = nodes_collection
        self.edges_collection_name = edges_collection
        self.nodes = None
        self.edges = None

    def reset(self) -> None:
        for name in (self.nodes_collection_name, self.edges_collection_name):
            try:
                self.client.delete_collection(name)
            except Exception:
                pass
        self.nodes = self.client.get_or_create_collection(
            name=self.nodes_collection_name,
            metadata={"hnsw:space": "cosine", "source": "stream_graphrag_chroma"},
        )
        self.edges = self.client.get_or_create_collection(
            name=self.edges_collection_name,
            metadata={"hnsw:space": "cosine", "source": "stream_graphrag_chroma"},
        )

    def upsert_nodes(self, nodes: List[dict]) -> None:
        if not nodes:
            return
        assert self.nodes is not None
        for chunk in chunks(nodes, 2000):
            docs = [node_doc(n) for n in chunk]
            self.nodes.upsert(
                ids=[n["id"] for n in chunk],
                documents=docs,
                embeddings=[text_embedding_deterministic(d) for d in docs],
                metadatas=[scalar_meta(node_meta(n)) for n in chunk],
            )

    def upsert_edges(self, edges: List[dict]) -> None:
        if not edges:
            return
        assert self.edges is not None
        for chunk in chunks(edges, 2000):
            docs = [edge_doc(e) for e in chunk]
            self.edges.upsert(
                ids=[edge_id(e) for e in chunk],
                documents=docs,
                embeddings=[text_embedding_deterministic(d) for d in docs],
                metadatas=[scalar_meta(edge_meta(e)) for e in chunk],
            )


def chunks(items: List[dict], size: int) -> Iterable[List[dict]]:
    for i in range(0, len(items), size):
        yield items[i : i + size]


def node_doc(n: dict) -> str:
    p = n.get("properties") or {}
    lines = [
        f"node_type: {n.get('type', '')}",
        f"name: {n.get('name', '')}",
    ]
    for key in (
        "qualified_name",
        "relative_path",
        "file_path",
        "language",
        "signature",
        "evidence",
        "description",
        "package",
        "annotations",
        "condition",
    ):
        value = p.get(key)
        if value:
            lines.append(f"{key}: {value}")
    if p.get("line") is not None:
        lines.append(f"line: {p.get('line')}")
    return "\n".join(lines)


def node_meta(n: dict) -> Dict[str, Any]:
    p = n.get("properties") or {}
    return {
        "graph_node_id": n.get("id"),
        "node_type": n.get("type"),
        "name": n.get("name"),
        "qualified_name": p.get("qualified_name"),
        "relative_path": p.get("relative_path"),
        "file_path": p.get("file_path"),
        "language": p.get("language"),
        "line": p.get("line"),
        "confidence": p.get("confidence"),
        "inferred": p.get("inferred", False),
    }


def edge_id(e: dict) -> str:
    p = e.get("properties") or {}
    return stable_id("e", e.get("source_id"), e.get("target_id"), e.get("type"), p.get("line"), p.get("evidence"))


def edge_doc(e: dict) -> str:
    p = e.get("properties") or {}
    return "\n".join(
        [
            f"edge_type: {e.get('type', '')}",
            f"source_id: {e.get('source_id', '')}",
            f"target_id: {e.get('target_id', '')}",
            f"file_path: {p.get('file_path', '')}",
            f"line: {p.get('line', '')}",
            f"evidence: {p.get('evidence', '')}",
            f"confidence: {p.get('confidence', '')}",
            f"inferred: {p.get('inferred', False)}",
        ]
    )


def edge_meta(e: dict) -> Dict[str, Any]:
    p = e.get("properties") or {}
    return {
        "edge_type": e.get("type"),
        "source_id": e.get("source_id"),
        "target_id": e.get("target_id"),
        "file_path": p.get("file_path"),
        "line": p.get("line"),
        "confidence": p.get("confidence"),
        "inferred": p.get("inferred", False),
    }


def mk_node(ntype: str, name: str, **props: Any) -> dict:
    qn = props.get("qualified_name") or props.get("relative_path") or name
    return {"id": stable_id("n", ntype, qn, props.get("line", "")), "type": ntype, "name": name, "properties": props}


def mk_edge(source_id: str, target_id: str, etype: str, **props: Any) -> dict:
    return {"source_id": source_id, "target_id": target_id, "type": etype, "properties": props}


def scan_files(project_root: Path, max_bytes: int) -> List[dict]:
    files: List[dict] = []
    for root, dirs, names in os.walk(project_root):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
        for name in names:
            path = Path(root) / name
            suffix = path.suffix.lower()
            lang = SOURCE_EXTENSIONS.get(suffix)
            if not lang and name == "pom.xml":
                lang = "xml"
            if not lang:
                continue
            try:
                st = path.stat()
            except OSError:
                continue
            if st.st_size > max_bytes:
                continue
            rel = path.relative_to(project_root).as_posix()
            files.append(
                {
                    "path": str(path),
                    "relative_path": rel,
                    "language": lang,
                    "size": st.st_size,
                    "mtime_ns": st.st_mtime_ns,
                }
            )
    return sorted(files, key=lambda x: x["relative_path"])


def package_name(text: str) -> str:
    m = re.search(r"^\s*package\s+([\w.]+)\s*;", text, re.M)
    return m.group(1) if m else ""


def annotation_block_before(text: str, start: int) -> str:
    prefix = text[:start].splitlines()[-8:]
    anns = []
    for line in reversed(prefix):
        s = line.strip()
        if s.startswith("@"):
            anns.append(s)
        elif s == "":
            continue
        else:
            break
    return " ".join(reversed(anns))


def extract_java_like(item: dict, text: str) -> Tuple[List[dict], List[dict], dict]:
    rel = item["relative_path"]
    path = item["path"]
    lang = item["language"]
    pkg = package_name(text)
    nodes: List[dict] = []
    edges: List[dict] = []
    file_node = mk_node("File", rel, qualified_name=rel, relative_path=rel, file_path=path, language=lang, line=1)
    nodes.append(file_node)
    file_index = {"classes": [], "methods": [], "fields": [], "tables": [], "apis": []}

    imports = [(m.group(1), line_of(text, m.start())) for m in re.finditer(r"^\s*import\s+(?:static\s+)?([\w.*]+)\s*;", text, re.M)]

    class_pat = re.compile(
        r"(?P<ann>(?:@\w+(?:\([^)]*\))?\s*)*)"
        r"(?P<mods>(?:(?:public|private|protected|abstract|final|static)\s+)*)"
        r"(?P<kind>class|interface|enum)\s+"
        r"(?P<name>[A-Za-z_]\w*)"
        r"(?:\s+extends\s+(?P<extends>[A-Za-z_][\w.<>]*))?"
        r"(?:\s+implements\s+(?P<implements>[A-Za-z0-9_.,\s<>]+))?",
        re.M,
    )
    classes = list(class_pat.finditer(text))
    class_nodes: List[Tuple[re.Match[str], dict, int, int]] = []
    for i, m in enumerate(classes):
        name = m.group("name")
        qn = f"{pkg}.{name}" if pkg else name
        line = line_of(text, m.start())
        start = m.start()
        end = classes[i + 1].start() if i + 1 < len(classes) else len(text)
        ann = compact((m.group("ann") or "") + " " + annotation_block_before(text, m.start()), 600)
        ntype = "JavaClass" if m.group("kind") == "class" else ("JavaEnum" if m.group("kind") == "enum" else "JavaInterface")
        class_node = mk_node(
            ntype,
            name,
            qualified_name=qn,
            relative_path=rel,
            file_path=path,
            language=lang,
            package=pkg,
            line=line,
            annotations=ann,
            confidence="high",
            inferred=False,
            evidence=compact(text[m.start() : text.find("{", m.start()) if "{" in text[m.start():end] else m.end()], 1000),
        )
        nodes.append(class_node)
        class_nodes.append((m, class_node, start, end))
        file_index["classes"].append(qn)
        edges.append(mk_edge(file_node["id"], class_node["id"], "DECLARES_CLASS", file_path=path, line=line, confidence="high", inferred=False))
        ext = m.group("extends")
        if ext:
            ext_node = mk_node("JavaTypeRef", ext, qualified_name=ext, relative_path=rel, file_path=path, language=lang, line=line, confidence="medium", inferred=True)
            nodes.append(ext_node)
            edges.append(mk_edge(class_node["id"], ext_node["id"], "EXTENDS", file_path=path, line=line, evidence=ext, confidence="medium", inferred=True))
        impls = m.group("implements") or ""
        for impl in re.findall(r"[A-Za-z_][\w.]*", impls):
            impl_node = mk_node("JavaTypeRef", impl, qualified_name=impl, relative_path=rel, file_path=path, language=lang, line=line, confidence="medium", inferred=True)
            nodes.append(impl_node)
            edges.append(mk_edge(class_node["id"], impl_node["id"], "IMPLEMENTS", file_path=path, line=line, evidence=impl, confidence="medium", inferred=True))

    if not class_nodes:
        class_nodes = [(None, file_node, 0, len(text))]  # type: ignore[list-item]

    for imp, ln in imports:
        imp_node = mk_node("JavaImport", imp, qualified_name=imp, relative_path=rel, file_path=path, language=lang, line=ln, confidence="high", inferred=False)
        nodes.append(imp_node)
        edges.append(mk_edge(file_node["id"], imp_node["id"], "IMPORTS", file_path=path, line=ln, evidence=imp, confidence="high", inferred=False))

    field_pat = re.compile(
        r"(?P<ann>(?:^\s*@[\w.]+(?:\([^;\n]*\))?\s*\n)*)"
        r"^\s*(?P<mods>(?:(?:public|private|protected|static|final|transient|volatile)\s+)*)"
        r"(?P<type>[A-Za-z_][\w.<>, ?\[\]]+)\s+"
        r"(?P<name>[A-Za-z_]\w*)\s*(?:=[^;]*)?;",
        re.M,
    )
    method_pat = re.compile(
        r"(?P<ann>(?:^\s*@[\w.]+(?:\([^;\n]*\))?\s*\n)*)"
        r"^\s*(?P<mods>(?:(?:" + "|".join(JAVA_MODIFIERS) + r")\s+)*)"
        r"(?P<ret>[A-Za-z_][\w.<>, ?\[\]]+)\s+"
        r"(?P<name>[A-Za-z_]\w*)\s*\((?P<params>[^)]*)\)\s*(?:throws\s+[^{]+)?\{",
        re.M,
    )

    for _, class_node, cstart, cend in class_nodes:
        body = text[cstart:cend]
        class_qn = class_node["properties"].get("qualified_name", rel)
        for fm in field_pat.finditer(body):
            line = line_of(text, cstart + fm.start())
            ann = compact(fm.group("ann") or "", 600)
            fname = fm.group("name")
            ftype = compact(fm.group("type"), 300)
            qn = f"{class_qn}.{fname}"
            field_node = mk_node(
                "Field",
                fname,
                qualified_name=qn,
                relative_path=rel,
                file_path=path,
                language=lang,
                line=line,
                type=ftype,
                annotations=ann,
                evidence=compact(fm.group(0), 600),
                confidence="high",
                inferred=False,
            )
            nodes.append(field_node)
            file_index["fields"].append(qn)
            edges.append(mk_edge(class_node["id"], field_node["id"], "DECLARES_FIELD", file_path=path, line=line, evidence=fm.group(0), confidence="high", inferred=False))
            if "@Autowired" in ann or "@Resource" in ann or "@Inject" in ann:
                edges.append(mk_edge(class_node["id"], field_node["id"], "BEAN_INJECTED", file_path=path, line=line, evidence=fm.group(0), confidence="high", inferred=False))

        for mm in method_pat.finditer(body):
            abs_start = cstart + mm.start()
            line = line_of(text, abs_start)
            mname = mm.group("name")
            params = compact(mm.group("params"), 1000)
            ret = compact(mm.group("ret"), 300)
            ann = compact(mm.group("ann") or "", 800)
            qn = f"{class_qn}.{mname}({params})"
            method_node = mk_node(
                "Method",
                mname,
                qualified_name=qn,
                relative_path=rel,
                file_path=path,
                language=lang,
                line=line,
                return_type=ret,
                parameters_raw=params,
                annotations=ann,
                signature=compact(mm.group(0), 1000),
                evidence=compact(mm.group(0), 1000),
                confidence="high",
                inferred=False,
            )
            nodes.append(method_node)
            file_index["methods"].append(qn)
            edges.append(mk_edge(class_node["id"], method_node["id"], "DECLARES_METHOD", file_path=path, line=line, evidence=mm.group(0), confidence="high", inferred=False))

            api_paths = re.findall(r"@(GetMapping|PostMapping|PutMapping|DeleteMapping|PatchMapping|RequestMapping)\s*(?:\(([^)]*)\))?", ann + " " + mm.group(0), re.S)
            for http_anno, args in api_paths:
                path_match = re.search(r'"([^"]+)"', args or "")
                api_name = f"{http_anno}:{path_match.group(1) if path_match else qn}"
                api_node = mk_node("RestApi", api_name, qualified_name=f"{rel}:{api_name}", relative_path=rel, file_path=path, language=lang, line=line, evidence=compact(args or http_anno, 600), confidence="medium", inferred=False)
                nodes.append(api_node)
                file_index["apis"].append(api_name)
                edges.append(mk_edge(method_node["id"], api_node["id"], "HANDLES_API", file_path=path, line=line, evidence=api_name, confidence="medium", inferred=False))

            next_method = method_pat.search(body, mm.end())
            method_body = body[mm.end() : next_method.start() if next_method else min(len(body), mm.end() + 12000)]
            calls_seen: Set[str] = set()
            for cm in re.finditer(r"\b([A-Za-z_]\w*)\s*\(", method_body):
                call = cm.group(1)
                if call in CALL_KEYWORDS or call == mname:
                    continue
                calls_seen.add(call)
                if len(calls_seen) >= 80:
                    break
            for call in sorted(calls_seen):
                call_node = mk_node("MethodCall", call, qualified_name=call, relative_path=rel, file_path=path, language=lang, line=line, confidence="low", inferred=True)
                nodes.append(call_node)
                edges.append(mk_edge(method_node["id"], call_node["id"], "INVOKES", file_path=path, line=line, evidence=call, confidence="low", inferred=True))

            for im in re.finditer(r"\bif\s*\(([^)]{3,500})\)", method_body):
                cond = compact(im.group(1), 600)
                rule_line = line_of(text, cstart + mm.end() + im.start())
                rule_node = mk_node("BusinessRule", f"{mname}: if {cond[:80]}", qualified_name=f"{qn}:if:{rule_line}", relative_path=rel, file_path=path, language=lang, line=rule_line, condition=cond, evidence=compact(im.group(0), 800), confidence="medium", inferred=False)
                nodes.append(rule_node)
                edges.append(mk_edge(method_node["id"], rule_node["id"], "CONDITIONAL_BRANCH", file_path=path, line=rule_line, evidence=cond, confidence="medium", inferred=False))
                if len([n for n in nodes if n.get("type") == "BusinessRule"]) > 200:
                    break

            for tm in re.finditer(r"\b(from|join|update|into)\s+[`\"\[]?([A-Za-z0-9_.]+)", method_body, re.I):
                table = tm.group(2).strip("`[]\"")
                table_line = line_of(text, cstart + mm.end() + tm.start())
                table_node = mk_node("DatabaseTable", table, qualified_name=table, relative_path=rel, file_path=path, language=lang, line=table_line, evidence=compact(tm.group(0), 300), confidence="medium", inferred=True)
                nodes.append(table_node)
                file_index["tables"].append(table)
                edges.append(mk_edge(method_node["id"], table_node["id"], "MAPS_TO", file_path=path, line=table_line, evidence=tm.group(0), confidence="medium", inferred=True))

    return nodes, edges, file_index


def extract_xml_sql_props(item: dict, text: str) -> Tuple[List[dict], List[dict], dict]:
    rel = item["relative_path"]
    path = item["path"]
    lang = item["language"]
    nodes: List[dict] = []
    edges: List[dict] = []
    file_node = mk_node("File", rel, qualified_name=rel, relative_path=rel, file_path=path, language=lang, line=1)
    nodes.append(file_node)
    file_index = {"classes": [], "methods": [], "fields": [], "tables": [], "apis": []}

    for m in re.finditer(r"\b(create\s+table|from|join|update|into)\s+[`\"\[]?([A-Za-z0-9_.]+)", text, re.I):
        table = m.group(2).strip("`[]\"")
        ln = line_of(text, m.start())
        table_node = mk_node("DatabaseTable", table, qualified_name=table, relative_path=rel, file_path=path, language=lang, line=ln, evidence=compact(m.group(0), 300), confidence="medium", inferred=not m.group(1).lower().startswith("create"))
        nodes.append(table_node)
        edges.append(mk_edge(file_node["id"], table_node["id"], "MAPS_TO", file_path=path, line=ln, evidence=m.group(0), confidence="medium", inferred=not m.group(1).lower().startswith("create")))
        file_index["tables"].append(table)

    if lang in {"properties", "yaml"}:
        for idx, line in enumerate(text.splitlines(), start=1):
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            if "=" in s:
                key, value = s.split("=", 1)
            elif ":" in s and not s.startswith("-"):
                key, value = s.split(":", 1)
            else:
                continue
            key = key.strip()
            if not key:
                continue
            cfg = mk_node("ConfigurationProperty", key, qualified_name=f"{rel}:{key}", relative_path=rel, file_path=path, language=lang, line=idx, evidence=compact(line, 600), description=compact(value, 600), confidence="high", inferred=False)
            nodes.append(cfg)
            edges.append(mk_edge(file_node["id"], cfg["id"], "DECLARES_PROPERTY", file_path=path, line=idx, evidence=line, confidence="high", inferred=False))

    return nodes, edges, file_index


def extract_generic(item: dict, text: str) -> Tuple[List[dict], List[dict], dict]:
    rel = item["relative_path"]
    path = item["path"]
    lang = item["language"]
    node = mk_node("File", rel, qualified_name=rel, relative_path=rel, file_path=path, language=lang, line=1, description=compact(text[:1200]), confidence="high", inferred=False)
    return [node], [], {"classes": [], "methods": [], "fields": [], "tables": [], "apis": []}


def extract(item: dict, text: str) -> Tuple[List[dict], List[dict], dict]:
    if item["language"] in {"java", "kotlin", "csharp"}:
        return extract_java_like(item, text)
    if item["language"] in {"xml", "sql", "properties", "yaml"}:
        return extract_xml_sql_props(item, text)
    return extract_generic(item, text)


def merge_index(dst: Dict[str, Any], rel: str, item_index: dict) -> None:
    dst[rel] = item_index


def load_config(graph_root: Path) -> dict:
    p = graph_root / "graphrag_config.json"
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}


def update_config_snapshot(graph_root: Path, generated_at: str, project_root: Path) -> None:
    p = graph_root / "graphrag_config.json"
    cfg = load_config(graph_root)
    cfg["storage_root"] = str(graph_root)
    cfg["target_project_path"] = str(project_root)
    cfg.setdefault("graph_snapshot", {})["baseline_generated_at_utc"] = generated_at
    cfg["graph_snapshot"]["baseline_local_calendar_date_hint"] = datetime.now().strftime("%Y-%m-%d")
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(cfg, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(tmp, p)


def write_summary(graph_root: Path, project_root: Path, generated_at: str, total_files: int, indexed_files: int, nodes: int, edges: int, elapsed: float, gaps: List[dict]) -> None:
    lines = [
        "# GraphRAG Summary",
        "",
        f"- Generated At (UTC): {generated_at}",
        f"- Project Root: {project_root}",
        f"- Graph Storage: {graph_root}",
        "- Build Mode: full streaming to Chroma (fresh run)",
        f"- Total Scanned Files: {total_files}",
        f"- Indexed Files: {indexed_files}",
        f"- Total Nodes (entities): {nodes}",
        f"- Total Edges (relations): {edges}",
        f"- Elapsed Seconds: {elapsed:.1f}",
        "- Chroma Mode: local PersistentClient, deterministic 384-d embeddings",
        "",
        "## Coverage",
        "",
        "- Java/Kotlin/C# classes, methods, fields, imports, REST annotations, coarse calls, conditions, SQL table references.",
        "- XML/SQL table references and properties/YAML configuration keys.",
        "",
        "## Known Gaps",
        "",
    ]
    if gaps:
        for g in gaps[:20]:
            lines.append(f"- {g.get('relative_path')}: {g.get('reason')}")
    else:
        lines.append("- No fatal parse gaps recorded. Dynamic dispatch/reflection remains inferred where not statically resolvable.")
    (graph_root / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Stream project GraphRAG into JSONL and local ChromaDB.")
    parser.add_argument("--project-root", required=True, type=Path)
    parser.add_argument("--graph-root", required=True, type=Path)
    parser.add_argument("--repo-root", default=None, type=Path)
    parser.add_argument("--batch-size", type=int, default=256)
    parser.add_argument("--max-file-bytes", type=int, default=2_000_000)
    parser.add_argument("--status-interval", type=int, default=25)
    parser.add_argument("--reset-chroma", action="store_true")
    args = parser.parse_args()

    project_root = args.project_root.resolve()
    graph_root = args.graph_root.resolve()
    repo_root = (args.repo_root or graph_root.parent).resolve()
    graph_root.mkdir(parents=True, exist_ok=True)
    (graph_root / "logs").mkdir(parents=True, exist_ok=True)
    status = StatusWriter(graph_root)
    generated_at = now_iso()
    started = time.time()
    cfg = load_config(graph_root)
    chroma_cfg = cfg.get("chroma") or {}
    persist_dir = graph_root / chroma_cfg.get("persist_directory_relative", "chroma_data")
    nodes_collection = chroma_cfg.get("nodes_collection", "graphrag_nodes")
    edges_collection = chroma_cfg.get("edges_collection", "graphrag_edges")

    node_writer = JsonlWriter(graph_root / "graph_nodes.jsonl")
    edge_writer = JsonlWriter(graph_root / "graph_edges.jsonl")
    all_node_ids: Set[str] = set()
    all_edge_ids: Set[str] = set()
    file_index: Dict[str, Any] = {}
    manifest_files: Dict[str, Any] = {}
    lookup: Dict[str, List[str]] = {}
    gaps: List[dict] = []
    node_batch: List[dict] = []
    edge_batch: List[dict] = []
    total_nodes = 0
    total_edges = 0
    indexed_files = 0
    processed_targets: List[str] = []

    try:
        files = scan_files(project_root, args.max_file_bytes)
        status.write(
            status="running",
            phase="initializing_chroma",
            total_files=len(files),
            processed_files=0,
            indexed_files=0,
            nodes=0,
            edges=0,
            summary="Fresh streaming run initializing Chroma.",
        )
        sink = ChromaSink(repo_root, persist_dir, nodes_collection, edges_collection)
        if args.reset_chroma:
            sink.reset()
        else:
            sink.nodes = sink.client.get_or_create_collection(name=nodes_collection, metadata={"hnsw:space": "cosine", "source": "stream_graphrag_chroma"})
            sink.edges = sink.client.get_or_create_collection(name=edges_collection, metadata={"hnsw:space": "cosine", "source": "stream_graphrag_chroma"})

        status.write(status="running", phase="scan_complete", total_files=len(files), processed_files=0, indexed_files=0, nodes=0, edges=0, summary="Fresh streaming run started.")
        print(f"Streaming GraphRAG: files={len(files)} graph_root={graph_root} chroma={persist_dir}", flush=True)

        for idx, item in enumerate(files, start=1):
            rel = item["relative_path"]
            processed_targets.append(rel)
            text = safe_read(Path(item["path"]), args.max_file_bytes)
            if text is None:
                gaps.append({"relative_path": rel, "reason": "read_skip_or_too_large"})
                continue
            try:
                nodes, edges, item_index = extract(item, text)
                indexed_files += 1
            except Exception as ex:
                gaps.append({"relative_path": rel, "reason": f"parse_exception: {ex}"})
                continue

            unique_nodes: List[dict] = []
            for n in nodes:
                if n["id"] in all_node_ids:
                    continue
                all_node_ids.add(n["id"])
                unique_nodes.append(n)
                name = n.get("name")
                if name:
                    lookup.setdefault(str(name), []).append(n["id"])
            unique_edges: List[dict] = []
            for e in edges:
                eid = edge_id(e)
                if eid in all_edge_ids:
                    continue
                all_edge_ids.add(eid)
                unique_edges.append(e)

            if unique_nodes:
                node_writer.write_many(unique_nodes)
                node_batch.extend(unique_nodes)
                total_nodes += len(unique_nodes)
            if unique_edges:
                edge_writer.write_many(unique_edges)
                edge_batch.extend(unique_edges)
                total_edges += len(unique_edges)

            merge_index(file_index, rel, item_index)
            manifest_files[rel] = {
                "relative_path": rel,
                "path": item["path"],
                "language": item["language"],
                "size": item["size"],
                "mtime_ns": item["mtime_ns"],
                "sha256": sha256_file(Path(item["path"])),
            }

            if len(node_batch) >= args.batch_size:
                sink.upsert_nodes(node_batch)
                node_batch.clear()
            if len(edge_batch) >= args.batch_size:
                sink.upsert_edges(edge_batch)
                edge_batch.clear()

            if idx % args.status_interval == 0:
                summary = f"processed={idx}/{len(files)}, indexed={indexed_files}, nodes={total_nodes}, edges={total_edges}"
                status.write(
                    status="running",
                    phase="streaming",
                    total_files=len(files),
                    processed_files=idx,
                    indexed_files=indexed_files,
                    nodes=total_nodes,
                    edges=total_edges,
                    gaps=len(gaps),
                    processed_targets=processed_targets,
                    summary=summary,
                )
                print(summary, flush=True)

        if node_batch:
            sink.upsert_nodes(node_batch)
            node_batch.clear()
        if edge_batch:
            sink.upsert_edges(edge_batch)
            edge_batch.clear()

        node_writer.close()
        edge_writer.close()
        manifest = {"project_root": str(project_root), "generated_at": generated_at, "files": manifest_files}
        (graph_root / "source_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        (graph_root / "file_index.json").write_text(json.dumps(file_index, ensure_ascii=False, indent=2), encoding="utf-8")
        (graph_root / "entity_lookup.json").write_text(json.dumps(lookup, ensure_ascii=False, indent=2), encoding="utf-8")
        write_summary(graph_root, project_root, generated_at, len(files), indexed_files, total_nodes, total_edges, time.time() - started, gaps)
        update_config_snapshot(graph_root, generated_at, project_root)
        status.write(
            status="completed",
            phase="completed",
            end_time=now_iso(),
            total_files=len(files),
            processed_files=len(files),
            indexed_files=indexed_files,
            nodes=total_nodes,
            edges=total_edges,
            gaps=len(gaps),
            processed_targets=processed_targets,
            summary=f"Completed fresh streaming build. indexed={indexed_files}, nodes={total_nodes}, edges={total_edges}",
        )
        print(f"completed indexed={indexed_files} nodes={total_nodes} edges={total_edges}", flush=True)
        return 0
    except Exception as ex:
        try:
            node_writer.close()
            edge_writer.close()
        except Exception:
            pass
        err_path = graph_root / "logs" / f"stream_error_{datetime.now().strftime('%Y%m%d-%H%M%S')}.log"
        err_path.write_text(traceback.format_exc(), encoding="utf-8")
        status.write(status="failed", phase="failed", end_time=now_iso(), nodes=total_nodes, edges=total_edges, gaps=len(gaps), summary=f"Failed: {ex}")
        print(f"failed: {ex}", file=sys.stderr, flush=True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

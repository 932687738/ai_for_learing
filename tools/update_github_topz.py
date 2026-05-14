#!/usr/bin/env python3
"""更新 dailyReport/github-topz.md：拉取 GitHub 按 Star 全局排序前十名，与文件中已有条目合并。"""
from __future__ import annotations

import argparse
import json
import os
import re
import ssl
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from typing import Dict, List, Tuple

# 第四列为裸 URL，便于再次解析回写
TABLE_ROW_RE = re.compile(
    r"^\|\s*\d+\s*\|\s*`([^`]+)`\s*\|\s*(\d+)\s*\|\s*(https?://\S+)\s*\|\s*$"
)

Entry = Tuple[int, str, str]


def repo_key(full_name: str) -> str:
    parts = [p for p in full_name.strip().strip("`").split("/") if p.strip()]
    if len(parts) != 2:
        return ""
    return "{}/{}".format(parts[0], parts[1]).lower()


def parse_existing_table(md_text: str) -> Dict[str, Entry]:
    """owner/repo 小写键 -> (stars, url, display_label)。"""
    out: Dict[str, Entry] = {}
    for line in md_text.splitlines():
        m = TABLE_ROW_RE.match(line.strip())
        if not m:
            continue
        full_raw, stars_str, url = m.group(1), m.group(2), m.group(3)
        key = repo_key(full_raw)
        if not key:
            continue
        stars = int(stars_str)
        label = full_raw.strip()
        out[key] = (stars, url.strip(), label)
    return out


def github_search_top10(ssl_ctx: ssl.SSLContext | None, token: str | None) -> List[dict]:
    url = "https://api.github.com/search/repositories?q=stars:%3E0&sort=stars&order=desc&per_page=10"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "ai_for_learing-tools-update-github-topz",
    }
    if token:
        headers["Authorization"] = "Bearer {}".format(token)
    req = Request(url, headers=headers, method="GET")
    with urlopen(req, timeout=90, context=ssl_ctx) as resp:
        data = resp.read().decode("utf-8")
    payload = json.loads(data)
    items = payload.get("items") or []
    return items


def build_merged(existing: Dict[str, Entry], fetch_items: List[dict]) -> Dict[str, Entry]:
    merged: Dict[str, Entry] = dict(existing)
    for item in fetch_items:
        full = item.get("full_name") or ""
        stars = item.get("stargazers_count")
        html_url = item.get("html_url") or ""
        key = repo_key(full)
        if not key or stars is None:
            continue
        prior = merged.get(key)
        url = html_url.strip() if html_url else (prior[1] if prior else "")
        label = full.strip() if full.strip() else (prior[2] if prior else key)
        merged[key] = (int(stars), url, label)
    return merged


def render_md(merged: Dict[str, Entry]) -> str:
    zone = datetime.now(tz=_shanghai_tz()).strftime("%Y-%m-%d %H:%M:%S")
    rows = sorted(
        merged.items(),
        key=lambda kv: (-kv[1][0], kv[0]),
    )
    lines = [
        "# GitHub star 前十名（快照合并）",
        "",
        "- 数据源：[`dual-digest-on-pull`](../.cursor/rules/dual-digest-on-pull.mdc) 工作流程下，Knowledge Base Digest 配套的 GitHub Search API：`sort=stars` 前十名。",
        "- 与本文件已有仓库合并：**已出现的仓库更新 Stars**，新增的按 Star **降序** 插入整表排序。",
        "",
        "**最近一次更新时间**（Asia/Shanghai）： {}".format(zone),
        "",
        "| 序号 | 仓库 | Stars | 链接 |",
        "| --- | --- | ---:| --- |",
    ]
    for i, (_key, (stars, html_url, label)) in enumerate(rows, start=1):
        safe_url = html_url if html_url else "https://github.com/{}/{}".format(_key.split("/")[0], _key.split("/")[1])
        lines.append("| {} | `{}` | {} | {} |".format(i, label, stars, safe_url))
    lines.append("")
    return "\n".join(lines)


def _shanghai_tz():
    try:
        from zoneinfo import ZoneInfo
        return ZoneInfo("Asia/Shanghai")
    except Exception:
        return timezone(timedelta(hours=8))


def main() -> None:
    parser = argparse.ArgumentParser(description="Merge GitHub top-10-by-stars snapshot into github-topz.md")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("dailyReport/github-topz.md"),
        help="Path to markdown file (default: dailyReport/github-topz.md)",
    )
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    out_path = args.output
    if not out_path.is_absolute():
        out_path = (root / out_path).resolve()
    else:
        out_path = out_path.resolve()

    ssl_ctx = ssl.create_default_context()
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")

    existing: Dict[str, Entry] = {}
    if out_path.is_file():
        existing = parse_existing_table(out_path.read_text(encoding="utf-8"))

    try:
        items = github_search_top10(ssl_ctx, token)
    except HTTPError as e:
        print("GitHub API 错误 HTTP {}： {}".format(e.code, e.reason))
        raise SystemExit(1) from e
    except URLError as e:
        print("请求失败： {}".format(e.reason))
        raise SystemExit(1) from e

    if len(items) < 1:
        print("GitHub API 返回空结果，跳过写入")
        raise SystemExit(2)

    merged = build_merged(existing, items)
    text = render_md(merged)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    tmp = out_path.with_suffix(out_path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    tmp.replace(out_path)
    print("已写入 {}".format(out_path))


if __name__ == "__main__":
    main()

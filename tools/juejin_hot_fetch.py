#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fetch Juejin hot / collected-article ranks for fixed categories.

Outputs a staging JSON for the juejin-hot-digest skill. Deduplicates by
canonical article URL against the persistent state file's seen_urls.
"""

from __future__ import print_function

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime

try:
    from zoneinfo import ZoneInfo
except ImportError:
    ZoneInfo = None

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_STATE = os.path.join(
    ROOT, "dailyReport", "juejin-hot-news", "juejin-hot-state.json"
)
DEFAULT_OUT = os.path.join(
    ROOT, "dailyReport", "juejin-hot-news", "_staging_latest.json"
)

RANK_API = (
    "https://api.juejin.cn/content_api/v1/content/article_rank"
    "?category_id={cate_id}&type={rank_type}"
)
DETAIL_API = "https://api.juejin.cn/content_api/v1/article/detail"

# Official category_id from tag_api/v1/query_category_briefs
CATEGORIES = [
    {"name": "后端", "slug": "backend", "cate_id": "6809637769959178254"},
    {"name": "前端", "slug": "frontend", "cate_id": "6809637767543259144"},
    {"name": "人工智能", "slug": "ai", "cate_id": "6809637773935378440"},
    {"name": "开发工具", "slug": "freebie", "cate_id": "6809637771511070734"},
]

BOARDS = [
    {
        "name": "文章热榜",
        "slug": "hot",
        "rank_type": "hot",
        "page_url": "https://juejin.cn/hot/articles",
    },
    {
        "name": "收藏热榜",
        "slug": "collect",
        "rank_type": "collect",
        "page_url": "https://juejin.cn/hot/collected-articles",
    },
]

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)


def today_shanghai():
    if ZoneInfo is not None:
        return datetime.now(ZoneInfo("Asia/Shanghai")).strftime("%Y-%m-%d")
    return datetime.now().strftime("%Y-%m-%d")


def canonical_url(article_id):
    return "https://juejin.cn/post/%s" % article_id


def http_get_json(url):
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": UA,
            "Referer": "https://juejin.cn/",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=45) as resp:
        return json.loads(resp.read().decode("utf-8"))


def http_post_json(url, payload):
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "User-Agent": UA,
            "Content-Type": "application/json",
            "Origin": "https://juejin.cn",
            "Referer": "https://juejin.cn/",
            "Accept": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=45) as resp:
        return json.loads(resp.read().decode("utf-8"))


def load_state(path):
    if not os.path.isfile(path):
        return {
            "last_end_date": None,
            "last_sync_ymd": None,
            "processed_dates": [],
            "seen_urls": [],
        }
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if "seen_urls" not in data or data["seen_urls"] is None:
        data["seen_urls"] = []
    if "processed_dates" not in data or data["processed_dates"] is None:
        data["processed_dates"] = []
    return data


def fetch_rank(cate_id, rank_type, limit):
    url = RANK_API.format(cate_id=cate_id, rank_type=rank_type)
    payload = http_get_json(url)
    if payload.get("err_msg") not in (None, "success") and payload.get("err_no") not in (
        0,
        None,
    ):
        raise RuntimeError(
            "rank API failed cate=%s type=%s: %s"
            % (cate_id, rank_type, payload.get("err_msg"))
        )
    items = payload.get("data") or []
    return items[:limit]


def fetch_detail(article_id):
    payload = http_post_json(
        DETAIL_API,
        {"article_id": str(article_id), "client_type": 2608},
    )
    if payload.get("err_no") not in (0, None) and payload.get("err_msg") != "success":
        return None
    data = payload.get("data") or {}
    article_info = data.get("article_info") or {}
    author_user = (data.get("author_user_info") or {})
    tags = []
    for t in data.get("tags") or []:
        tag = t.get("tag_name") or t.get("name")
        if tag:
            tags.append(tag)
    mark = article_info.get("mark_content") or ""
    # Cap body for staging size; skill summarizes from this text
    if len(mark) > 12000:
        mark = mark[:12000] + "\n\n…(正文截断，请以原文链接为准)"
    return {
        "title": article_info.get("title") or "",
        "brief": article_info.get("brief_content") or "",
        "mark_content": mark,
        "author": author_user.get("user_name")
        or author_user.get("user_id")
        or "",
        "ctime": article_info.get("ctime"),
        "mtime": article_info.get("mtime"),
        "view_count": article_info.get("view_count"),
        "digg_count": article_info.get("digg_count"),
        "collect_count": article_info.get("collect_count"),
        "comment_count": article_info.get("comment_count"),
        "tags": tags,
    }


def main():
    parser = argparse.ArgumentParser(description="Fetch Juejin hot digests staging data")
    parser.add_argument(
        "--state",
        default=DEFAULT_STATE,
        help="Path to juejin-hot-state.json",
    )
    parser.add_argument(
        "--out",
        default=DEFAULT_OUT,
        help="Staging JSON output path",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=15,
        help="Max items per category per board (default 15)",
    )
    parser.add_argument(
        "--date",
        default=None,
        help="Snapshot date YYYY-MM-DD (Asia/Shanghai). Default: today.",
    )
    parser.add_argument(
        "--include-seen",
        action="store_true",
        help="Ignore seen_urls filter (for debugging only)",
    )
    args = parser.parse_args()

    snap_date = args.date or today_shanghai()
    state = load_state(args.state)
    seen = set(state.get("seen_urls") or [])

    listings = []
    new_articles = {}
    skipped_seen = []

    for board in BOARDS:
        for cat in CATEGORIES:
            try:
                raw_items = fetch_rank(cat["cate_id"], board["rank_type"], args.limit)
            except (urllib.error.URLError, urllib.error.HTTPError, RuntimeError) as exc:
                listings.append(
                    {
                        "board": board["name"],
                        "board_slug": board["slug"],
                        "board_page": board["page_url"],
                        "category": cat["name"],
                        "category_slug": cat["slug"],
                        "error": str(exc),
                        "items": [],
                    }
                )
                continue

            board_items = []
            for idx, row in enumerate(raw_items, start=1):
                content = row.get("content") or {}
                counter = row.get("content_counter") or {}
                author = row.get("author") or {}
                article_id = str(content.get("content_id") or "")
                if not article_id:
                    continue
                url = canonical_url(article_id)
                entry = {
                    "rank": idx,
                    "article_id": article_id,
                    "url": url,
                    "title": content.get("title") or "",
                    "author": author.get("name") or "",
                    "view": counter.get("view"),
                    "like": counter.get("like"),
                    "collect": counter.get("collect"),
                    "comment_count": counter.get("comment_count"),
                    "hot_rank": counter.get("hot_rank"),
                    "is_new": url not in seen,
                }
                board_items.append(entry)

                if url in seen and not args.include_seen:
                    skipped_seen.append(
                        {
                            "url": url,
                            "title": entry["title"],
                            "board": board["name"],
                            "category": cat["name"],
                        }
                    )
                    continue

                if url not in new_articles:
                    new_articles[url] = {
                        "article_id": article_id,
                        "url": url,
                        "list_title": entry["title"],
                        "list_author": entry["author"],
                        "appearances": [],
                        "metrics": {
                            "view": entry["view"],
                            "like": entry["like"],
                            "collect": entry["collect"],
                            "comment_count": entry["comment_count"],
                            "hot_rank": entry["hot_rank"],
                        },
                        "detail": None,
                    }
                new_articles[url]["appearances"].append(
                    {
                        "board": board["name"],
                        "board_slug": board["slug"],
                        "category": cat["name"],
                        "category_slug": cat["slug"],
                        "rank": idx,
                    }
                )

            listings.append(
                {
                    "board": board["name"],
                    "board_slug": board["slug"],
                    "board_page": board["page_url"],
                    "category": cat["name"],
                    "category_slug": cat["slug"],
                    "items": board_items,
                }
            )

    # Fetch details only for new URLs
    detail_ok = 0
    detail_fail = 0
    for url, art in new_articles.items():
        try:
            detail = fetch_detail(art["article_id"])
        except (urllib.error.URLError, urllib.error.HTTPError, ValueError) as exc:
            art["detail_error"] = str(exc)
            detail_fail += 1
            continue
        if detail is None:
            art["detail_error"] = "empty detail"
            detail_fail += 1
            continue
        art["detail"] = detail
        detail_ok += 1

    staging = {
        "snapshot_date": snap_date,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "source_pages": [b["page_url"] for b in BOARDS],
        "categories": [c["name"] for c in CATEGORIES],
        "limit_per_board_category": args.limit,
        "stats": {
            "listing_slots": sum(len(x.get("items") or []) for x in listings),
            "unique_new_urls": len(new_articles),
            "skipped_seen_urls": len(skipped_seen),
            "detail_ok": detail_ok,
            "detail_fail": detail_fail,
            "seen_urls_in_state": len(seen),
        },
        "listings": listings,
        "new_articles": list(new_articles.values()),
        "skipped_seen": skipped_seen,
        "state_path": os.path.relpath(args.state, ROOT).replace("\\", "/"),
        "note": (
            "Agent must summarize from new_articles[].detail.mark_content / brief; "
            "write digest; then merge new urls into state seen_urls."
        ),
    }

    out_dir = os.path.dirname(args.out)
    if out_dir and not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    with open(args.out, "w", encoding="utf-8", newline="\n") as f:
        json.dump(staging, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(
        "wrote %s | new=%s skipped_seen=%s detail_ok=%s detail_fail=%s"
        % (
            args.out,
            len(new_articles),
            len(skipped_seen),
            detail_ok,
            detail_fail,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

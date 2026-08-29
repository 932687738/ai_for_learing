# -*- coding: utf-8 -*-
import json
import re

path = r"dailyReport/juejin-hot-news/_staging_latest.json"
d = json.load(open(path, encoding="utf-8"))
arts = d["new_articles"]
print("STATS", json.dumps(d["stats"], ensure_ascii=False))
print()
for a in arts:
    det = a.get("detail") or {}
    title = a.get("list_title") or det.get("title") or ""
    author = a.get("list_author") or det.get("author") or ""
    brief = (det.get("brief") or "")[:240]
    mc = det.get("mark_content") or ""
    text = re.sub(r"[#>*`\[\]]", " ", mc)
    text = re.sub(r"\s+", " ", text).strip()[:320]
    m = a.get("metrics") or {}
    apps = ",".join(
        "%s/%s#%s" % (x["category"], x["board"], x["rank"])
        for x in (a.get("appearances") or [])
    )
    print("URL", a["url"])
    print("TITLE", title)
    print(
        "AUTHOR",
        author,
        "|",
        apps,
        "| like=%s collect=%s view=%s" % (m.get("like"), m.get("collect"), m.get("view")),
    )
    print("BRIEF", brief)
    print("BODY", text)
    print("====")

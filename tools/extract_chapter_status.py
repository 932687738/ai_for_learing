# -*- coding: utf-8 -*-
import os
import re

BASE = os.path.join(os.path.dirname(__file__), '..', 'story', '人皮契约', '正文')

def find_chapter_file(num):
    for f in os.listdir(BASE):
        if f.startswith(f'第{num.zfill(3)}章') or f.startswith(f'第{int(num)}章'):
            if re.match(rf'第{int(num):03d}章', f) or re.match(rf'第{int(num)}章', f):
                return os.path.join(BASE, f)
    for f in os.listdir(BASE):
        m = re.match(r'第(\d+)章', f)
        if m and int(m.group(1)) == int(num):
            return os.path.join(BASE, f)
    return None

def parse_chapter(num):
    path = find_chapter_file(num)
    if not path:
        return None
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    title_m = re.search(r'^#\s*第\d+章\s*(.+)$', content, re.M)
    title = title_m.group(1).strip() if title_m else ''
    status = content.split('## 本章状态更新')
    if len(status) < 2:
        return {'num': num, 'title': title, 'path': path}
    s = status[1]
    def get_val(label):
        m = re.search(rf'\|\s*{re.escape(label)}\s*\|\s*([^|]+?)\s*\|', s)
        return m.group(1).strip() if m else ''
    start = get_val('章初')
    end = get_val('章末')
    change = get_val('变化')
    memory_block = ''
    mem_m = re.search(r'### 记忆碎片记录\n(.*?)(?=\n### |\Z)', s, re.S)
    if mem_m:
        memory_block = mem_m.group(1).strip()
    return {
        'num': int(num), 'title': title, 'path': path,
        'start': start, 'end': end, 'change': change,
        'memory': memory_block
    }

results = []
for i in range(1, 49):
    r = parse_chapter(i)
    if r:
        results.append(r)

# Print ghost progress table
print('=== GHOST PROGRESS ===')
for r in results:
    note = r['change'] if r['change'] else '—'
    print(f"| 第{r['num']:03d}章 | {r['end']} | {note} | {r['title']} |")

# Print memory entries
print('\n=== MEMORY ===')
for r in results:
    mem = r['memory']
    if not mem or '无新增' in mem and '失去' not in mem:
        if r['num'] <= 12:
            continue
        if '无新增' in mem:
            continue
    if '无新增' in mem and '失去' not in mem:
        continue
    print(f"\n--- CH{r['num']:03d} ---")
    print(mem)

---
name: markdown-qa-classify-merge
description: Classifies Markdown Q&A by topic into study/interview with summarized answers (not copy-paste), no bak files. Use when user @-mentions markdown-qa-classify-merge with uploaded .md files.
---

# Markdown 问答分类与合并

## 触发

`@markdown-qa-classify-merge` + 上传/路径 → 立即直写，不预览。**不生成 .bak` 文件。**

## 内容原则

- **只保留问 + 答**；答须**总结**，禁止复制参考答案/评价/无效「不知道」。
- **分类**：按每条**实际主题**拆分多个 `{分类名}问答.md`，禁止整份塞进单一笼统分类。

## 路径

- 目录：`study/interview`
- 文件：`{分类名}问答.md`
- 日志：`study/interview/_merge_log.md`（不写 bak 路径）

## 格式

```markdown
问题标题
问：…
答：总结后的回答
分类标签：{分类名} | 更新日期：YYYY-MM-DD
```

完整流程与边界见 `.cursor/agents/markdown-qa-classify-merge.md`。

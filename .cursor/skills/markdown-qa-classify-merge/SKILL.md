---
name: markdown-qa-classify-merge
description: Classifies Markdown Q&A into study/interview/knowledge (Chinese filenames) by topic relevance with summarized knowledge-point format (not copy-paste), no bak files. Use when user @-mentions markdown-qa-classify-merge with uploaded .md files.
---

# Markdown 问答 → 标准知识点

## 触发

`@markdown-qa-classify-merge` + 上传/路径 → 立即直写 `study/interview/knowledge/`，不预览。**不生成 .bak`；不写 `*问答.md`；文件名用中文。**

## 分类体系

**必读** [`.cursor/knowledge-taxonomy.md`](../../knowledge-taxonomy.md)：

- 产出目录：`study/interview/knowledge/{中文文件名}.md`
- 14 个模块（如 `Spring AI核心组件.md`、`RAG检索策略.md`、`Agent工作流模式.md`）
- 按**知识点相关性**路由；`module_id` 仅内部路由，落盘必须中文文件名

## 内容原则

- 条目结构：**核心概念 → 要点 → 代码示例 → 面试常问 → 关联知识点**
- 答须**总结且可读**；源代码**须保留**为 fenced block
- 关联链接指向**中文文件名**

## 路径

| 用途 | 路径 |
|------|------|
| 知识点模块 | `study/interview/knowledge/{中文文件名}.md` |
| 模块索引 | `study/interview/knowledge/索引.md` |
| 分类规范 | `.cursor/knowledge-taxonomy.md` |
| 日志 | `study/interview/_merge_log.md` |
| 原始输入 | `study/interview/original/` |

## 合并后收尾

1. 更新模块文件头日期与目录
2. 刷新 `knowledge/索引.md`
3. 追加 `_merge_log.md`

完整流程见 `.cursor/agents/markdown-qa-classify-merge.md`。

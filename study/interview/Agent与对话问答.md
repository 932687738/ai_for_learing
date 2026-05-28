# Agent与对话 问答

<!-- 最后更新于 2026-05-28 -->

Agent 与 RAG 协同（@Tool 注册与动态加载）
问：如何让 Agent 动态决定是否调用 RAG 检索？请给出使用 @Tool 注解并动态加载工具的设计。
答：每知识库 @Tool 声明 name/description，Registry 扫描注册到 ChatClient；工具过多可做向量发现；本地无结果再降级 web_search 或 LLM。
分类标签：Agent与对话 | 更新日期：2026-05-28


---

多轮对话记忆管理
问：如何在多轮对话中让 Agent 记住上下文，并避免记忆膨胀？请说明 ChatMemory 与 ToolContext 的配合。
答：短期用 MessageWindowChatMemory + Advisor 控窗口；长期用 Jdbc 或向量库存摘要；超窗压缩历史，避免膨胀。
分类标签：Agent与对话 | 更新日期：2026-05-28


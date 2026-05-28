# Spring AI基础 问答

<!-- 最后更新于 2026-05-28 -->

基础巩固：ChatClient vs ChatModel
问：ChatClient 和 ChatModel 有什么区别？
答：ChatModel 直连模型 API；ChatClient 是门面，封装流式、Advisor、Tool、模板。日常用 Client，调试或极简调用才用 Model。
分类标签：Spring AI基础 | 更新日期：2026-05-28


---

Prompt 与 UserMessage 的关系
问：Prompt 和 UserMessage 分别代表什么？关系是什么？
答：Prompt 是消息列表容器；UserMessage 是其中表示用户输入的一条，还可含 SystemMessage、Tool 消息等。
分类标签：Spring AI基础 | 更新日期：2026-05-28


---

Advisor 的作用与位置
问：Advisor 接口的作用是什么？它的 around 方法在执行链路中处于什么位置？
答：Advisor 类似切面，around 包裹 ChatClient→ChatModel 全链路，可链式增强检索、记忆、日志等。
分类标签：Spring AI基础 | 更新日期：2026-05-28


---

Document 的 content 与 metadata
问：Document 对象的 content 和 metadata 分别存储什么？请各举两个例子。
答：content 存正文；metadata 存 tenant_id、source、page 等，用于过滤、隔离与溯源。
分类标签：Spring AI基础 | 更新日期：2026-05-28


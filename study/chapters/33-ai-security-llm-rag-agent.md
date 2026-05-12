# 第 33 课：AI 安全：LLM / RAG / Agent 风险治理

## 0. 本课定位

本课系统补齐 AI 安全。第 14 课已有工程安全内容，第 26 课讲模型行为分析，本课聚焦企业 AI 应用的实际威胁：LLM、RAG、Agent、MCP、Skills、供应链和数据治理。

## 1. 学习目标

完成本课后，你应该能：

1. 解释 Prompt Injection、Indirect Prompt Injection、Data Leakage、Excessive Agency。
2. 为 RAG、Tool Calling、MCP、Agent Skills 设计安全边界。
3. 将 OWASP Top 10 for LLM Applications 映射到 Java / Python 项目。
4. 设计权限、审计、隔离、人工确认和回滚机制。
5. 建立安全 eval 和红队测试清单。

## 2. 主要风险

| 风险 | 场景 | 防护 |
| --- | --- | --- |
| Prompt Injection | 用户输入指示模型忽略规则 | 指令分层、输入标记、拒绝策略、eval |
| Indirect Prompt Injection | 文档、网页、邮件中藏恶意指令 | 检索内容隔离、引用约束、工具权限 |
| Sensitive Information Disclosure | 泄露密钥、个人信息、内部文档 | DLP、脱敏、权限过滤、日志控制 |
| Excessive Agency | Agent 权限过大 | 最小权限、审批、最大步数、沙箱 |
| Supply Chain | 恶意 skill、MCP server、依赖包 | 签名、白名单、代码审查、隔离运行 |
| Overreliance | 人类过度相信输出 | 置信度、引用、人工复核、高风险阻断 |

## 3. RAG 安全

RAG 的安全重点不只是“答案是否正确”，还包括：

- 用户是否有权限访问召回文档。
- 召回文档是否含恶意提示。
- 答案引用是否真实且可访问。
- 模型是否把上下文中的指令当成系统指令。
- 是否记录了检索证据和回答链路。

## 4. Agent 安全

Agent 风险来自“模型输出会触发动作”。

关键控制：

- 工具白名单。
- 参数 schema 校验。
- 用户身份传递。
- 写操作人工确认。
- 最大工具调用次数。
- 沙箱和网络隔离。
- 审计日志和回滚。

## 5. Skill / MCP 安全

Skill 和 MCP 都会扩展 Agent 能力，因此需要供应链治理：

- 只安装可信来源。
- 检查脚本和依赖。
- 区分只读工具和写操作工具。
- 给 MCP server 单独账号和最小权限。
- 避免把密钥写入文档、skill 或 Agent Card。

## 6. 实践任务

1. 为第 10 课 RAG 系统设计 prompt injection 测试集。
2. 为第 11 课 Tool Calling 系统设计写操作审批流程。
3. 为第 27 课 Skill 设计供应链安全检查表。
4. 为 MCP server 设计最小权限账号方案。

## 7. 阶段验收标准

- 能把 OWASP LLM 风险映射到实际代码和架构。
- 能设计 RAG / Agent / MCP / Skill 的安全边界。
- 能把安全测试纳入 eval 和发布流程。

## 8. 本课使用的信息源

- OWASP Top 10 for LLM Applications：https://owasp.org/www-project-top-10-for-large-language-model-applications
- OWASP Top 10 for LLM Applications 2025：https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025
- OpenAI Production Best Practices：https://platform.openai.com/docs/guides/production-best-practices

## 9. 问答记录

暂无。

## 10. 外部补充

暂无。

## 11. 结构化补充（整改）

### 核心讲解

- AI 安全不是单点防护，而是输入、检索、工具、输出和审计的全链路治理。
- RAG/Agent 场景要同时关注权限边界与提示注入风险。
- 安全策略必须可验证：可测试、可审计、可回滚。

### 拓展阅读

- OWASP LLM Top 10: https://owasp.org/www-project-top-10-for-large-language-model-applications
- OWASP GenAI 2025: https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025

### 问答记录

- 2026-05-12：完成结构化整改，后续补攻击样例与防护基线清单。

### 外部补充

- 暂无（可补充你们安全红队或审计规则）。

### 本课掌握检查

- 你能否列出本项目最主要的 3 个 AI 安全风险和对应控制措施？
- 你能否设计一套最小安全回归测试（含越权与注入场景）？

### 下一课前置条件

- 完成一页安全基线：输入校验、权限控制、工具隔离、日志审计、应急回滚。

## 12. 跨章节边界（去重指引）

- 本课主讲：LLM/RAG/Agent 全链路安全治理。
- 第 14 课主讲：Java AI 工程化，本课为其提供安全基线与测试要求。
- 第 29 课主讲：企业搜索能力，本课只对其补充安全控制约束。
- 第 36 课主讲：新兴生态评估，本课提供统一安全审查框架。

## 回归评测记录（2026-05-12）

- run_id: `baseline-2026-05-12`
- case: `E33-security-baseline`
- result: `PASS`
- 记录：`study/projects/27-36-min-eval-regression-run-2026-05-12.md`

## 可运行示例（Java，整改新增）

```java
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class SecurityGuardDemo {
    private static final Set<String> TOOL_ALLOWLIST =
            new HashSet<String>(Arrays.asList("read_docs", "search_kb", "summarize"));

    static boolean canExecute(String tool, boolean hasPermission) {
        return hasPermission && TOOL_ALLOWLIST.contains(tool);
    }

    public static void main(String[] args) {
        System.out.println(canExecute("search_kb", true));   // true
        System.out.println(canExecute("write_db", true));    // false
        System.out.println(canExecute("read_docs", false));  // false
    }
}
```

## 学习状态

- 状态：未开始（内容已就绪）
- 最近更新：2026-05-12
- 进入下一课条件：学员明确回复“这节课已经学会”

# 第 36 课：OpenClaw、Hermes 与新兴 Agent 生态观察

## 0. 本课定位

本课补齐 OpenClaw、Hermes 与新兴 Agent 生态。由于这类项目变化很快，本课采用“工程观察 + 风险评估”方式，不把任何新工具默认视为生产级标准。

## 1. 学习目标

完成本课后，你应该能：

1. 解释 OpenClaw 这类本地 / 个人 Agent 平台的产品形态和潜在风险。
2. 解释 Hermes 这类开放模型系列在 agentic、函数调用、长上下文场景中的意义。
3. 用安全、可维护性、生态成熟度、可审计性评估新兴 AI 工具。
4. 判断一个 Agent 工具是否适合进入企业环境。
5. 将新兴生态内容归档到课程相关章节，而不是盲目追热点。

## 2. OpenClaw 观察维度

OpenClaw 类工具通常强调：

- 本地运行或自托管。
- 连接邮件、浏览器、文件、日历、消息等个人工具。
- 通过自然语言执行多步骤自动化。
- 与 coding agent、skills、MCP、A2A 等生态组合。

企业评估时必须关注：

- 默认权限是否过大。
- 是否能细粒度控制工具。
- skill / plugin 是否有供应链审计。
- 日志和数据是否可追踪。
- 是否支持企业身份、权限和密钥管理。

## 3. Hermes 观察维度

Hermes 通常指 Nous Research 的 Hermes 开放模型系列。课程中关注它的原因不是“必须使用”，而是通过它理解开放模型生态：

- 开放权重模型如何支持私有化部署。
- 函数调用和 agentic 数据训练如何影响工具使用能力。
- 长上下文和多轮对话如何影响 Agent 任务。
- 开放模型如何与 vLLM、量化、RAG、MCP 结合。

## 4. 新兴工具进入企业的检查表

| 检查项 | 问题 |
| --- | --- |
| 来源可信 | 是否有官方仓库、许可证、维护者和 release 记录 |
| 权限模型 | 是否能最小权限运行 |
| 供应链 | plugin / skill / 依赖是否可审查 |
| 数据边界 | 数据是否出域，是否可配置 |
| 审计 | 工具调用、文件改动、外部请求是否记录 |
| 回滚 | 自动化动作失败后是否可撤销 |
| Eval | 是否能对任务成功率和安全性做回归测试 |

## 5. 与前序课程的关系

- 第 27 课提供 Skill 设计方法。
- 第 31 课提供 MCP / A2A 协议边界。
- 第 33 课提供安全评估框架。
- 第 34 课提供本地模型部署和推理成本判断。

本课不是鼓励安装所有工具，而是训练工程判断：任何能访问文件、浏览器、邮件、密钥、支付、代码仓库的 Agent，都必须先经过权限和安全评估。

## 6. 实践任务

1. 为一个新兴 Agent 工具写 20 项企业准入检查表。
2. 为 Hermes 本地部署设计一个最小 RAG demo 架构。
3. 比较 OpenClaw 类个人 Agent 与 Codex / Claude Code 类 coding agent 的边界。
4. 设计一个 skill marketplace 的安全扫描流程。

## 7. 阶段验收标准

- 能冷静评估新兴 Agent 工具，而不是只看热度。
- 能解释 OpenClaw / Hermes 与 Agent、Skills、MCP、RAG、推理基础设施的关系。
- 能把新技术纳入安全、eval、权限和工程治理体系。

## 8. 本课使用的信息源

- OpenClaw 官网：https://openclaw.ai/
- Nous Research Hermes 3：https://nousresearch.com/hermes3/
- Hermes 3 Hugging Face：https://huggingface.co/collections/NousResearch/hermes-3

## 9. 问答记录

暂无。

## 10. 外部补充

暂无。

## 11. 结构化补充（整改）

### 核心讲解

- 新兴 Agent 生态要先做工程可控性评估，再谈功能新颖性。
- OpenClaw/Hermes 的价值在于理解开放生态能力边界，而不是盲目替换现有栈。
- 企业落地优先级应是安全、权限、审计、回滚和评测闭环。

### 拓展阅读

- OpenClaw: https://openclaw.ai/
- Hermes 3: https://nousresearch.com/hermes3/

### 问答记录

- 2026-05-12：完成结构化整改，后续补“新工具准入评分卡”模板。

### 外部补充

- 暂无（可补充待评估的新工具列表）。

### 本课掌握检查

- 你能否用检查表评估一个新 Agent 工具是否可进入生产？
- 你能否识别“演示可用”与“生产可用”的关键差异？

### 下一课前置条件

- 完成一份新兴工具企业准入评审单（含风险与回滚方案）。

## 12. 跨章节边界（去重指引）

- 本课主讲：新兴 Agent 生态与企业准入评估方法。
- 第 27 课主讲：Skill 设计与工作流，本课只引用其设计规范。
- 第 31 课主讲：MCP/A2A 协议，本课只讨论生态接入可行性。
- 第 33 课主讲：安全治理，本课沿用其安全检查基线。
- 第 34 课主讲：基础设施能力，本课只补充开放模型生态视角。

## 回归评测记录（2026-05-12）

- run_id: `baseline-2026-05-12`
- case: `E36-ecosystem-gate`
- result: `PASS`
- 记录：`study/projects/27-36-min-eval-regression-run-2026-05-12.md`

## 可运行示例（Java，整改新增）

```java
public class ToolAdmissionDemo {
    static int score(boolean trustedSource, boolean leastPrivilege, boolean auditable, boolean rollbackReady) {
        int s = 0;
        if (trustedSource) s += 25;
        if (leastPrivilege) s += 25;
        if (auditable) s += 25;
        if (rollbackReady) s += 25;
        return s;
    }

    public static void main(String[] args) {
        int s = score(true, true, false, true);
        System.out.println("admission_score=" + s); // 75
        System.out.println("allow_production=" + (s >= 80)); // false
    }
}
```

## 学习状态

- 状态：未开始（内容已就绪）
- 最近更新：2026-05-12
- 进入下一课条件：学员明确回复“这节课已经学会”

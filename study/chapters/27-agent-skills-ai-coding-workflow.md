# 第 27 课：Agent Skills 与 AI 编程工作流

## 0. 本课定位

本课补齐 Agent Skills、AI skills、Codex Skills、Claude Skills、Cursor Skills、Claude Code skills 等概念。它不是单纯讲“写提示词”，而是讲如何把可复用工作流程、项目规范、参考资料、脚本和评测方法组织成 AI agent 可以按需调用的能力包。

关联旧课：

- 第 8 课：Prompt Engineering
- 第 11 课：Function Calling、Tool Calling 与 Agent
- 第 14 课：Java AI 工程化

## 1. 学习目标

完成本课后，你应该能：

1. 解释 skill 与 prompt、tool、MCP server、agent 的区别。
2. 设计一个 Java / Python 项目的 `SKILL.md` 能力包。
3. 说明 Codex、Claude Code、Cursor 这类 coding agent 的共同工作流。
4. 为团队沉淀 AI 编程规范：读代码、改代码、跑测试、写文档、做评审。
5. 判断什么时候应该用 Skill，什么时候应该直接写提示词或工具。

## 2. 核心概念

### 2.1 Agent Skill

Agent Skill 是给 AI agent 使用的“可复用任务说明 + 参考资料 + 可选脚本”。它的重点是降低上下文噪声：平时不把所有资料塞进模型，只有当任务匹配 skill 描述时再加载。

典型结构：

```text
skill-name/
  SKILL.md
  references/
  scripts/
  assets/
```

### 2.2 Skill、Prompt、Tool、MCP 的区别

| 概念 | 解决什么问题 | 典型内容 |
| --- | --- | --- |
| Prompt | 单次任务怎么问 | 指令、上下文、输出格式 |
| Skill | 一类任务怎么稳定执行 | `SKILL.md`、参考资料、脚本、模板 |
| Tool | 让模型请求外部动作 | 查询订单、执行检索、调用接口 |
| MCP | 标准化暴露工具和上下文 | tools、resources、prompts |
| Agent | 多步规划、工具使用和反馈循环 | plan、act、observe、reflect |

### 2.3 Coding Agent

Coding agent 是面向软件工程任务的 AI agent，通常能读取代码库、编辑文件、运行命令、执行测试、解释失败、生成补丁和参与代码评审。

工程边界：

- 它不是 IDE 自动补全，而是能处理多文件任务。
- 它不是完全自治员工，仍需要权限、测试、代码评审和回滚策略。
- 它的质量很大程度取决于项目说明、测试覆盖、任务拆分和评测标准。

## 3. Java / Python 项目中的 Skill 示例

```markdown
# spring-ai-controller-review

## When to use
Use this skill when reviewing Spring Boot controllers that call LLM, RAG, tool calling, or streaming AI APIs.

## Checklist
- Check request validation.
- Check authentication and authorization.
- Check tenant or user-level data filtering before retrieval.
- Check timeout, retry, rate limit, and fallback behavior.
- Check prompt injection exposure.
- Check logging does not include secrets or full private prompts.
- Check tests cover success, provider failure, and unsafe input.

## Output
Return findings ordered by severity, with file and line references.
```

这个 skill 不替代代码评审能力，它把团队的评审标准显式化，减少每次重新解释规则的成本。

## 4. 常见误区

1. 把 skill 写成一大段泛泛而谈的提示词。
2. 在 skill 中放入过多无关资料，导致上下文污染。
3. 不写触发条件，agent 不知道什么时候该加载。
4. skill 只讲理念，没有 checklist、脚本或输出标准。
5. 把危险操作交给 skill 自动执行，却没有审批、测试和回滚。

## 5. 实践任务

1. 为一个 Spring Boot 项目写一个“AI 接口安全评审”skill。
2. 为一个 Python RAG 项目写一个“数据摄取管道检查”skill。
3. 设计一个 coding agent 工作流：读需求、定位代码、改动、运行测试、总结风险。
4. 比较 `AGENTS.md`、`.cursorrules`、`SKILL.md`、MCP tool 描述之间的职责边界。

## 6. 阶段验收标准

你应该能做到：

- 能解释 Agent Skills、Codex Skills、Claude Code Skills、Cursor Skills 的共同抽象。
- 能写出一个可执行、可复用、低噪声的 skill。
- 能说明 skill 与工具调用、MCP、Agent 之间的边界。

## 7. 本课使用的信息源

- OpenAI Codex 文档：https://platform.openai.com/docs/codex/overview
- OpenAI Codex 产品页：https://openai.com/codex
- Claude Code Skills 文档：https://code.claude.com/docs/en/skills
- Claude Code 概览：https://docs.claude.com/en/docs/claude-code/overview

## 8. 问答记录

暂无。

## 9. 外部补充

暂无。

## 10. 结构化补充（整改）

### 核心讲解

- 本课核心是明确 `skills`、`agent`、`tool/MCP` 的职责边界，避免把系统能力都堆进提示词。
- 任何可执行 skill 都应具备触发条件、执行步骤、输出规范和安全约束。
- 在 Java/Python 工程中，skill 需要和测试、发布、回滚流程一起设计。

### 拓展阅读

- Cursor Skills: https://cursor.com/docs/context/skills
- Model Context Protocol: https://modelcontextprotocol.io/

### 问答记录

- 2026-05-12：启动结构化整改，统一课程模板并补学习闭环。

### 外部补充

- 暂无（等待学员补充项目链接或案例）。

### 本课掌握检查

- 你能否用一句话区分 `rule`、`skill`、`agent`、`MCP tool`？
- 你能否写出一个“可执行且可审计”的 skill 最小模板？

### 下一课前置条件

- 完成一个 skill 设计小练习并通过自检（触发条件、步骤、输出、安全）。

## 回归评测记录（2026-05-12）

- run_id: `baseline-2026-05-12`
- case: `E27-skill-boundary`
- result: `PASS`
- 记录：`study/projects/27-36-min-eval-regression-run-2026-05-12.md`

## 可运行示例（Java，整改新增）

```java
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class SkillBoundaryDemo {
    static class SkillSpec {
        String name;
        Set<String> capabilities = new HashSet<String>();
        SkillSpec(String name, String... caps) {
            this.name = name;
            this.capabilities.addAll(Arrays.asList(caps));
        }
    }

    static boolean isValidSkill(SkillSpec s) {
        // skill 只应描述流程与检查项，不直接拥有系统级权限
        return !s.capabilities.contains("direct_db_write")
                && !s.capabilities.contains("raw_shell_delete");
    }

    public static void main(String[] args) {
        SkillSpec safe = new SkillSpec("code-review", "read_repo", "lint", "report");
        SkillSpec risk = new SkillSpec("danger-op", "read_repo", "direct_db_write");
        System.out.println("safe valid = " + isValidSkill(safe)); // true
        System.out.println("risk valid = " + isValidSkill(risk)); // false
    }
}
```

## 学习状态

- 状态：未开始（内容已就绪）
- 最近更新：2026-05-12
- 进入下一课条件：学员明确回复“这节课已经学会”

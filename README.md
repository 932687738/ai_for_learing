# ai_for_learning

本项目已新增一组“AI 课程导师”自定义 Agent（基于 Cursor Subagents），用于围绕单一课程大纲文件进行持续教学与项目实战辅导。**本机仓库目录名**可能为 `ai_for_learing` 等，以你克隆/打开的实际路径为准。

## 仓库地图：主要目录

| 路径 | 用途 |
| --- | --- |
| [`study/`](study/) | **课程主资产**：章节 [`study/chapters/`](study/chapters/)、项目实战小节 [`study/projects/`](study/projects/)、大纲 [`study/COURSE_OUTLINE.md`](study/COURSE_OUTLINE.md)、进度 [`study/COURSE_PROGRESS.md`](study/COURSE_PROGRESS.md)、任务 [`study/COURSE_TASKS.md`](study/COURSE_TASKS.md)、写作规范 [`study/COURSE_WRITING_STANDARD.md`](study/COURSE_WRITING_STANDARD.md)、高阶路线 [`study/high/`](study/high/) 等；总览可选读 [`study/README.md`](study/README.md) |
| [`ai-learning/`](ai-learning/) | **可运行练习代码与数据**：与各课章对应的 `scripts/`、`src/`、`data/` |
| [`dailyReport/`](dailyReport/) | **日报与状态**：AI 日报 [`dailyReport/ai-daily-news/`](dailyReport/ai-daily-news/)、知识库摘要 [`dailyReport/knowledge-base-news/`](dailyReport/knowledge-base-news/)、GitHub 快照 [`dailyReport/github-topz.md`](dailyReport/github-topz.md) |
| [`project_graphrag/`](project_graphrag/) | **本地知识图谱与 GraphRAG**：配置、节点/边导出、构建与同步脚本、`summary.md`、可选 Chroma 向量数据等（只写本目录，不改动被分析的目标业务项目源码） |
| [`tools/`](tools/) | **仓库级命令行工具**（见下文「脚本与工具」） |
| [`.cursor/`](.cursor/) | **Cursor Agents、Rules、Skills、Settings**（见下文） |
| 仓库根其它 | 如 [`LOCAL_PATH.md`](LOCAL_PATH.md)（本地路径备忘）、[`RAG_LangChain_Java_Beginner_Guide.md`](RAG_LangChain_Java_Beginner_Guide.md)、根级 `ai-daily-digest.md`（若仍存在则多为历史/副本，**以 `dailyReport/` 下为准**） |

## Agents（`.cursor/agents/`）

在 Cursor 中以 **Subagents / 自定义 Agent** 使用的说明文件（YAML front matter + 角色与回写规则）。

| 文件 | 作用 |
| --- | --- |
| [`.cursor/agents/ai-course-mentor-course-mode.md`](.cursor/agents/ai-course-mentor-course-mode.md) | **课程模式**：围绕 `{COURSE_PATH}` 逐课教学、问答回写、进度维护 |
| [`.cursor/agents/ai-course-mentor-project-mode.md`](.cursor/agents/ai-course-mentor-project-mode.md) | **项目模式**：结合 `{JAVA_PROJECT_PATH}` / `{PYTHON_PROJECT_PATH}` 做项目分析与改造，结论回写课程实战小节 |

触发方式仍可用对话中的短指令（例如「调用 /ai-course-mentor-course-mode」），详见下文「触发示例」。

## Rules（`.cursor/rules/`）

给 **主对话或匹配文件** 的长期规则（`.mdc`，可含 `alwaysApply`、`globs` 等）。

| 文件 | 说明 |
| --- | --- |
| [`.cursor/rules/dual-digest-on-pull.mdc`](.cursor/rules/dual-digest-on-pull.mdc) | **双 Digest**：当用户语义为「拉取日报」（非 Git `pull`）时，必须先读并按顺序执行两条 Skill（AI 日报 + 知识库），并约定与 `dailyReport/`、`github-topz` 的配合方式 |
| [`.cursor/rules/front-end-cursor-rules.mdc`](.cursor/rules/front-end-cursor-rules.mdc) | **前端主线栈**（React 16、react-router-dom 4、Redux/Zustand、Ant Design 5、Less 等）的编码约束与偏好 |
| [`.cursor/rules/graphrag.mdc`](.cursor/rules/graphrag.mdc) | **GraphRAG 智能体**：在 `project_graphrag/**`、`tools/chroma_crud.py` 等上下文下，规定目标项目只读、构建/增量/语义增强/写回与安全边界 |

## Skills（`.cursor/skills/`）

供 Agent **按文件名显式读取** 的流程说明书（通常为 `SKILL.md`）。

| Skill | 路径 | 用途 |
| --- | --- | --- |
| `ai-daily-digest` | [`.cursor/skills/ai-daily-digest/SKILL.md`](.cursor/skills/ai-daily-digest/SKILL.md) | 中文 **AI 资讯日报**：增量/指定日、去重、写入 `dailyReport/ai-daily-news/` 与状态 JSON |
| `knowledge-base-digest` | [`.cursor/skills/knowledge-base-digest/SKILL.md`](.cursor/skills/knowledge-base-digest/SKILL.md) | 中文 **知识库日报**：固定中文技术源、写入 `dailyReport/knowledge-base-news/`；流程中要求同批执行 `python tools/update_github_topz.py` 刷新 `dailyReport/github-topz.md` |

与「拉取」相关的总入口逻辑见 **Rule** `dual-digest-on-pull.mdc`。

## 脚本与工具（`tools/`）

| 路径 | 说明 |
| --- | --- |
| [`tools/update_github_topz.py`](tools/update_github_topz.py) | 生成/更新 [`dailyReport/github-topz.md`](dailyReport/github-topz.md)：**模块一** 全局 Star Search API 与历史表合并；**模块二** 抓取 GitHub Trending（日/周/月）HTML 解析 |
| [`tools/github_topz/`](tools/github_topz/) | 上述脚本的子包：`stars_merge.py`（Search + 合并）、`trending_fetch.py`（Trending）、`display_zh.py`（简介中文化与翻译辅助） |
| [`tools/chroma_crud.py`](tools/chroma_crud.py) | **ChromaDB** 统一 CRUD/查询 CLI；依赖见 [`project_graphrag/requirements-chroma.txt`](project_graphrag/requirements-chroma.txt)；大规模整库同步仍用 `project_graphrag/scripts/sync_graphrag_chroma.py`（与 GraphRAG Rule 一致） |

## 其它 Cursor 文件

- [`.cursor/settings.json`](.cursor/settings.json)：本仓库在 Cursor 侧的工作区相关设置（若存在）。

## 使用说明

建议在对话开始时提供以下参数：

- `{COURSE_PATH}`（必填）：课程大纲文件路径，例如 `study/COURSE_OUTLINE.md`
- `{JAVA_PROJECT_PATH}`（选填）：Java 项目根目录
- `{PYTHON_PROJECT_PATH}`（选填）：Python 项目根目录

若未提供 `{COURSE_PATH}`，Agent 会先询问后再开始教学。

## 使用 Python（PyCharm 解释器）

在本仓库中若要运行或编辑 Python 相关代码，请在 **PyCharm** 中为当前工程配置解释器：

1. 打开 **Settings / Preferences**（Windows/Linux：`File` → `Settings`；macOS：`PyCharm` → `Preferences`）。
2. 进入 **Project → Python Interpreter**（左侧项目区域下）。
3. 在 **Python Interpreter** 下拉框中选择本机已有的解释器；若尚无合适环境，可通过 **Add Interpreter** 新建虚拟环境（venv）或指定 Conda/Python 路径。

配置完成后，PyCharm 的代码补全、运行/调试与会话所使用的 Python 才与项目目录一致。

### `ai-learning` 示例代码依赖安装

`ai-learning` 目录下练习与脚本包括：

- `**/scripts/**/*.py`（如第 1～2 课）
- **`03-machine-learning-workflow/src/**/*.py`**（第 3 课教材第九节起的配套脚本，见 `study/chapters/03-machine-learning-workflow.md`）
- **`07-cnn-rnn-transformer-intro/scripts/**/*.py`**（第 7 课小节 0.1.2 起：`cnn_valid_conv_numpy_demo.py`、`cnn_output_spatial_formula_demo.py`、`pooling_2x2_stride2_numpy_demo.py` 等）

用到的第三方包汇总如下（按需安装）：

| 包名 | 说明 |
| --- | --- |
| `numpy` | 数值与张量练习（第 2 课 `**/scripts/`） |
| `pandas` | CSV 与表格（各课；含 `house_price_*.py` 系列脚本） |
| `matplotlib` | 图表；未安装时部分脚本跳过绘图 |
| `scikit-learn` | `LinearRegression`、`train_test_split`、metrics、Pipeline、`cross_val_score` 等（第 3 课 **`src`** 与教材共用） |
| `joblib` | 教材保存模型小节（第十八节示例）用到的 `.joblib` 序列化 |

在已激活的虚拟环境中，**推荐一条命令覆盖当前仓库上述全部示例**（含 `03-machine-learning-workflow/src`）：

```bash
python -m pip install numpy pandas matplotlib scikit-learn joblib
```

若只跑 **第 3 课** `ai-learning/03-machine-learning-workflow/src/house_price_linear_regression.py`，最少需要 **`pandas`** 与 **`scikit-learn`**（`numpy` 常随依赖装好；为保证环境一致仍建议用上条完整命令）。

```bash
python -m pip install pandas scikit-learn
```

**说明**：新增示例若仍在使用表中已有包（未出现新的 PyPI 名），**不会产生新的包名**，但应在 **本节覆盖路径**——此前 README 仅写 **`**/scripts/`**，遗漏了 **`**/src/`**，易造成「没有对应安装命令」的观感。

**续课（控制上下文长度）**：进度已落在 `study/COURSE_PROGRESS.md`，新开对话时让助手**先读该文件**再讲，无需复述整段聊天历史。

## 触发示例

> 已精简为“短指令 + 参数”，更容易触发。

### 课程模式（最短）

```text
调用 /ai-course-mentor-course-mode
COURSE_PATH=study/COURSE_OUTLINE.md
从第1课开始讲。
```

### 项目模式（最短）

```text
调用 /ai-course-mentor-project-mode
COURSE_PATH=study/COURSE_OUTLINE.md
JAVA_PROJECT_PATH=D:/workspace/order-ai-demo
先识别技术栈并回写项目实战。
```

## 约束与回写规则（简要）

- 所有讲解、问答、外部补充都写回 `{COURSE_PATH}`，不额外创建独立笔记。
- 不删除已有内容，只做追加或精确插入。
- 严格逐课推进，需学生明确确认“这节课已经学会”后再进入下一课。

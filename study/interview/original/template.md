# 使用 Cursor 搭建多智能体协同编码完整指南

本指南展示如何利用 Cursor 内置的 AI 能力（Composer、Chat、Agent 模式）以及自定义角色指令，模拟“产品经理、架构师、前端工程师、后端工程师、测试工程师”等多个智能体，协作完成一个完整项目的开发。

## 目录
1. [总体架构与角色定义](#总体架构与角色定义)
2. [阶段一：需求设计 —— 产品经理智能体](#阶段一需求设计--产品经理智能体)
3. [阶段二：方案设计 —— 架构师智能体](#阶段二方案设计--架构师智能体)
4. [阶段三：后端编码 —— 后端工程师智能体](#阶段三后端编码--后端工程师智能体)
5. [阶段四：前端编码 —— 前端工程师智能体](#阶段四前端编码--前端工程师智能体)
6. [阶段五：测试 —— 测试工程师智能体](#阶段五测试--测试工程师智能体)
7. [多智能体协同工作流](#多智能体协同工作流)
8. [最佳实践与技巧](#最佳实践与技巧)

---

## 总体架构与角色定义

在 Cursor 中，我们通过 **`.cursorrules`** 文件为每个“智能体”定义角色、职责和输出规范。实际使用时，可以在不同对话中切换角色，或通过 `@` 引用不同的规则文件。

### 示例：项目根目录结构
my-project/
├── .cursor/
│ ├── rules/
│ │ ├── product-manager.mdc
│ │ ├── architect.mdc
│ │ ├── frontend-dev.mdc
│ │ ├── backend-dev.mdc
│ │ └── tester.mdc
│ └── prompts/
│ └── common.md
├── docs/
│ ├── requirements.md
│ ├── design.md
│ └── test-plan.md
├── frontend/
├── backend/
└── tests/

text

### 角色定义示例（`.cursor/rules/product-manager.mdc`）

```markdown
---
description: 产品经理智能体 - 负责需求分析与PRD撰写
globs: docs/requirements.md
alwaysApply: false
---

# 角色：产品经理

## 职责
- 与用户沟通，挖掘真实需求
- 编写清晰、可量化的产品需求文档（PRD）
- 拆解用户故事（User Story）
- 输出 Markdown 格式，包含以下章节：
  1. 背景与目标
  2. 功能列表（优先级 P0/P1/P2）
  3. 用户故事（格式：作为…，我希望…，以便…）
  4. 非功能性需求（性能、安全等）
  5. 验收标准

## 输出要求
- 使用中文
- 每项功能必须附带验收标准
- 禁止直接输出代码
其他角色定义类似，可根据需要调整 globs 和作用文件。

阶段一：需求设计 —— 产品经理智能体
触发方式
在 Cursor 中按 Cmd+K (Mac) 或 Ctrl+K (Win)，切换到 Agent 模式，输入：

text
@product-manager 请帮我们设计一个“任务协作平台”的需求文档，用户可以在平台上创建项目、分配任务、评论和上传附件。
输出示例（docs/requirements.md）
markdown
# 任务协作平台 - 产品需求文档

## 背景与目标
为了提升团队协作效率，需要一个轻量级的任务管理工具…

## 功能列表
| 模块 | 优先级 | 功能点 | 验收标准 |
|------|--------|--------|----------|
| 项目管理 | P0 | 创建/编辑/删除项目 | 只有项目拥有者可删除 |
| 任务管理 | P0 | 分配任务、设置截止日期 | 任务状态支持待办/进行中/已完成 |
| 评论 | P1 | 在任务下添加评论 | 支持@提及成员 |
| 附件 | P2 | 上传图片或文件 | 单个文件≤10MB |

## 用户故事
- 作为项目管理员，我希望邀请成员加入项目，以便协作…
…
💡 可以继续追问：@product-manager 请补充用户权限表，生成更详细的权限矩阵。

阶段二：方案设计 —— 架构师智能体
触发示例
text
@architect 基于上面的需求文档，设计技术方案。要求：前端使用 React + TypeScript，后端使用 FastAPI + PostgreSQL，提供 RESTful API。
输出（docs/design.md 节选）
markdown
# 技术方案设计

## 架构图（Mermaid）

```mermaid
graph LR
    A[React SPA] --> B[FastAPI + Nginx]
    B --> C[(PostgreSQL)]
    B --> D[MinIO (附件)]
    A --> E[WebSocket (实时通知)]
数据库设计（核心表）
sql
-- 项目表
CREATE TABLE projects (
    id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    owner_id UUID REFERENCES users(id),
    created_at TIMESTAMP DEFAULT NOW()
);

-- 任务表
CREATE TABLE tasks (
    id UUID PRIMARY KEY,
    project_id UUID REFERENCES projects(id) ON DELETE CASCADE,
    title VARCHAR(200),
    assignee_id UUID REFERENCES users(id),
    status VARCHAR(20) DEFAULT 'todo',
    due_date DATE
);
API 设计（节选）
方法	路径	描述
GET	/api/projects	获取用户的项目列表
POST	/api/projects	创建项目
GET	/api/tasks/{id}	获取任务详情
安全设计
JWT 身份认证

项目成员权限中间件

text

---

## 阶段三：后端编码 —— 后端工程师智能体

### 在 Cursor 中创建后端代码
打开 `/backend` 文件夹，使用 `Cmd+L` 打开 Composer，输入：
@backend-dev 根据 design.md 中的数据库模型和 API 设计，使用 FastAPI 实现项目创建的接口，包括：

模型定义（SQLAlchemy）

请求/响应 Schema (Pydantic)

路由和依赖注入（当前用户）

单元测试

text

### 生成的代码示例（`backend/app/routers/projects.py`）

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from app.auth import get_current_user

router = APIRouter(prefix="/api/projects", tags=["projects"])

@router.post("/", response_model=schemas.ProjectOut)
def create_project(
    project_in: schemas.ProjectCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """创建项目"""
    db_project = models.Project(
        name=project_in.name,
        owner_id=current_user.id
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project
自动生成测试代码（backend/tests/test_projects.py）
python
def test_create_project(client, test_user):
    response = client.post(
        "/api/projects",
        json={"name": "新项目"},
        headers={"Authorization": f"Bearer {test_user.token}"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "新项目"
阶段四：前端编码 —— 前端工程师智能体
触发示例
text
@frontend-dev 根据 requirements.md 和 design.md，使用 React + TypeScript + TailwindCSS 实现“项目列表页”和“创建项目”弹窗。调用后端 /api/projects 接口。
生成的代码（frontend/src/pages/Projects.tsx）
tsx
import React, { useEffect, useState } from 'react';
import { api } from '../lib/api';
import { Project } from '../types';

export const ProjectsPage: React.FC = () => {
  const [projects, setProjects] = useState<Project[]>([]);
  const [showModal, setShowModal] = useState(false);

  useEffect(() => {
    api.get('/projects').then(res => setProjects(res.data));
  }, []);

  const handleCreate = async (name: string) => {
    const res = await api.post('/projects', { name });
    setProjects([...projects, res.data]);
    setShowModal(false);
  };

  return (
    <div className="p-6">
      <button onClick={() => setShowModal(true)} className="bg-blue-500 text-white px-4 py-2 rounded">
        新建项目
      </button>
      {/* 项目列表渲染... */}
    </div>
  );
};
阶段五：测试 —— 测试工程师智能体
自动生成端到端测试
text
@tester 为上面的“创建项目”功能生成 Playwright 端到端测试脚本，包含登录、创建项目、验证列表更新。
输出（tests/e2e/create-project.spec.ts）
typescript
import { test, expect } from '@playwright/test';

test('用户能够创建新项目', async ({ page }) => {
  await page.goto('/login');
  await page.fill('#email', 'test@example.com');
  await page.fill('#password', 'password');
  await page.click('button[type="submit"]');

  await page.click('text=新建项目');
  await page.fill('input[name="name"]', '我的项目');
  await page.click('button:has-text("确认")');

  await expect(page.locator('text=我的项目')).toBeVisible();
});
多智能体协同工作流
Cursor 本身并不直接支持多个智能体同时对话，但可以通过以下方式实现 顺序协同：

上下文传递：使用 @文件名 引用上一个阶段产出的文档。例如：

架构师引用 requirements.md → 生成 design.md

后端工程师引用 design.md → 生成代码

前端工程师引用 design.md 和 backend/models.py（保持接口一致）

指令模板：创建 .cursor/prompts/common.md 存储公共约束，每次对话时粘贴或使用 @common。

Git 分支协同：

每个智能体生成的内容提交到不同分支（feature/backend, feature/frontend）

人类作为总工程师合并代码并解决冲突

Cursor 的 Composer 多文件编辑：在 Composer 中，可以要求 AI 同时修改前后端多个文件，实现一个指令完成跨智能体任务，例如：

text
请同时完成后端创建项目接口（projects.py）和前端调用该接口的代码（Projects.tsx），保持字段一致。
最佳实践与技巧
实践	说明
使用 .cursorrules 分角色	为每个智能体独立规则文件，通过 @规则名 切换
明确输出格式	在角色定义中强制要求输出 Markdown、JSON 或代码块
增量迭代	不要一次要求全部功能，分模块逐步生成
保留人类审核权	所有生成的代码必须经过人工 review 再合并
结合 Cursor 的 “Apply” 功能	AI 生成的 diff 可以直接应用到文件，提高效率
使用 // @ai 注释	在代码中写注释引导 AI 生成具体实现，例如 // @ai 实现附件上传逻辑
总结
通过上述方法，你可以利用 Cursor 模拟多个智能体角色，从需求到测试全流程自动化辅助开发。关键在于：

角色定义清晰（.cursorrules）

上下文严格传递（@引用文件）

人类作为流程管理者（触发、审核、合并）

此流程不仅适用于新项目，也可以用于遗留系统的维护和迭代。将重复性工作交给 AI 智能体，让人类专注于架构决策和关键业务逻辑。
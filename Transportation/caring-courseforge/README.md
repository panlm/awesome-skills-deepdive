# Caring CourseForge

> Create and manage online courses via the CourseForge API (caringcourseforge.com). Use when the user wants to create courses, modules, lessons, generate AI content, export to SCORM/xAPI, manage knowledge libraries, or interact with the CourseForge platform. Handles course building, content generation, quizzes, accessibility validation, and course export.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Caring CourseForge |
| **作者** | michaeljmoody |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/michaeljmoody-caring-courseforge |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/michaeljmoody/caring-courseforge |
| **安全评级** | 🟡 Medium |

## 功能概述
- Get your key: caringcourseforge.com → Settings → API Keys
- Store securely via your gateway environment config or shell profile (`export COURSEFORGE_API_KEY=cf_prod_...`). Do not s
- Courses (7): `list_courses`, `create_course`, `get_course`, `update_course`, `delete_course`, `get_course_settings`, `up
- Modules (5): `create_module`, `update_module`, `delete_module`, `reorder_modules`, `get_module`
- Lessons (7): `create_lesson`, `get_lesson`, `update_lesson`, `delete_lesson`, `reorder_lessons`, `move_lesson`, `duplica
- Content Blocks (6): `add_content_block`, `get_content_block`, `update_content_block`, `delete_content_block`, `reorder_c

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
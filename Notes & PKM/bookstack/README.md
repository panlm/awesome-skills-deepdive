# BookStack

> "BookStack Wiki & Documentation API integration. Manage your knowledge base programmatically: create, read, update, and delete books, chapters, pages, and shelves. Full-text search across all content. Use when you need to: (1) Create or edit wiki pages and documentation, (2) Organize content in books and chapters, (3) Search your knowledge base, (4) Automate documentation workflows, (5) Sync content between systems. Supports both HTML and Markdown content."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | BookStack |
| **作者** | xenofex7 |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawskills.sh/skills/xenofex7-bookstack |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/xenofex7/bookstack |
| **安全评级** | 🟡 Medium |

## 功能概述
- 📚 Books – create, edit, delete
- 📑 Chapters – organize content within books
- 📄 Pages – create/edit with HTML or Markdown
- 🔍 Full-text search – search across all content
- 📁 Shelves – organize books into collections

## 使用场景
- 管理个人笔记和知识
- 自动化信息整理
- 构建个人知识管理系统

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
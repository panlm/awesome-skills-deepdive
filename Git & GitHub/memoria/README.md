# Memoria

> Structured memory system for AI agents. Use when the user wants to store, recall, or search memories, manage session lifecycle (wake/sleep/checkpoint), sync to Notion, or when the user shares important information that should be remembered (facts, decisions, preferences, lessons, commitments, relationships, projects).

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Memoria |
| **作者** | kitakitsune0x |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/kitakitsune0x-memoria |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kitakitsune0x/memoria |
| **安全评级** | 🟡 Medium |

## 功能概述
- Push: Local documents are compared against the last sync state. New or updated files are created/updated in Notion.
- Pull: Notion databases are queried for pages modified since the last sync. Changes are written back to local markdown.
- Conflicts: When both sides have changed, local is preferred by default. Use `--prefer-notion` to override.
- Databases: One Notion database is created per category (decisions, lessons, facts, etc.) under the root page.
- `fact` -- raw information, data points
- `decision` -- choices made with reasoning

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- 数据库

## 包含文件
- `INSTRUCTIONS.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `bin`
- `package-lock.json`
- `package.json`
- `src`
- `tsconfig.json`
- `vitest.config.ts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，4 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
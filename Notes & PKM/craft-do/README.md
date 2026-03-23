# Craft API Skill and Obsidian Migration Tool

> Complete REST API integration for Craft.do - the beautiful note-taking and document app.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Craft API Skill and Obsidian Migration Tool |
| **作者** | atomtanstudio |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawskills.sh/skills/atomtanstudio-craft-do |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/atomtanstudio/craft-do |
| **安全评级** | 🟡 Medium |

## 功能概述
- 🔄 Obsidian Migration - Full vault migration with nested folders & content
- 📝 Document Management - Create, read, organize documents programmatically
- ✅ Task Automation - Create, update, list tasks across inbox/daily notes/logbook
- 📁 Folder Organization - Build nested folder hierarchies via API
- 🔧 Helper Scripts - Ready-to-use bash scripts for common operations
- 🧹 Cleanup Tools - Safe deletion and recovery utilities

## 使用场景
- 管理个人笔记和知识
- 自动化信息整理
- 构建个人知识管理系统

## 依赖和前提条件
- API Key

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `cleanup-craft.sh`
- `craft-api.sh`
- `migrate-obsidian-nested.sh`
- `migrate-obsidian.sh`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
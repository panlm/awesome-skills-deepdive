# Sovereign Commit Craft

> Git commit message expert. Analyzes diffs to generate perfect conventional commits, changelogs, release notes, and PR descriptions. Enforces commit message best practices and conventional commits spec.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Sovereign Commit Craft |
| **作者** | ryudi84 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/ryudi84-sovereign-commit-craft |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ryudi84/sovereign-commit-craft |
| **安全评级** | 🟡 Medium |

## 功能概述
- Conventional commit messages — properly typed, scoped, and formatted with subject, body, and footers
- Changelogs — Keep a Changelog format, written for users not developers
- Release notes — marketing-friendly summaries with highlights, upgrade instructions, and breaking change migration guides
- PR descriptions — structured templates with summary, change list, test plan, and checklists
- Commit splitting advice — when one commit should be three
- Version bump recommendations — semantic versioning derived from commit types
- Commit message reviews — analyze existing messages and suggest improvements

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- Docker
- OAuth
- 数据库

## 包含文件
- `EXAMPLES.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
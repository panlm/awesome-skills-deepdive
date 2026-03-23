# Doro Git Essentials

> Essential Git commands and workflows for version control, branching, and collaboration.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Doro Git Essentials |
| **作者** | a2mus |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/a2mus-doro-git-essentials |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/a2mus/doro-git-essentials |
| **安全评级** | 🟡 Medium |

## 功能概述
- Commit often, perfect later (interactive rebase)
- Write meaningful commit messages
- Use `.gitignore` for files to exclude
- Never force push to shared branches
- Pull before starting work
- Use feature branches, not main

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
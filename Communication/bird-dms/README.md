# Bird DMs

> An add-on to the Bird skill that lets your agent check its X/Twitter DM inbox. Use when the user asks to check DMs, read Twitter direct messages, list DM conversations, or monitor their X inbox.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Bird DMs |
| **作者** | tolibear |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/tolibear-bird-dms |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tolibear/bird-dms |
| **安全评级** | 🟡 Medium |

## 功能概述
- [bird](https://github.com/steipete/bird) for auth verification

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `dist`
- `package-lock.json`
- `package.json`
- `src`
- `tsconfig.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
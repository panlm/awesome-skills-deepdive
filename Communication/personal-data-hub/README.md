# Personal Data Hub

> 拉取个人数据（邮件、GitHub Issue 等），提议外发操作如草稿和回复

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Personal Data Hub |
| **作者** | haojian |
| **版本** | 0.1.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/haojian-personal-data-hub |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/haojian/personal-data-hub |
| **安全评级** | 🔴 High |

## 功能概述
- 聚合多来源个人数据（邮件、Issue 等）
- 智能分析和摘要收到的信息
- 提议回复草稿和外发操作
- 统一管理个人通信数据
- 支持邮件和 GitHub Issue 集成

## 使用场景
- 每日个人信息汇总与待办提醒
- 快速起草邮件回复和 Issue 评论
- 跨平台个人数据统一查看

## 依赖和前提条件
- 配置邮件账号访问权限
- GitHub 个人访问令牌
- 相关 API 凭证配置

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `openclaw.plugin.json`
- `package.json`
- `src`
- `tsconfig.json`
- `vitest.config.ts`

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
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

# Personaldatahub

> 拉取个人数据（邮件、Issue 等），提议外发操作（personal-data-hub 的替代版本）

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Personaldatahub |
| **作者** | haojian |
| **版本** | 0.1.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/haojian-personaldatahub |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/haojian/personaldatahub |
| **安全评级** | 🔴 High |

## 功能概述
- 聚合邮件和 Issue 等个人数据
- 智能分析收件箱信息
- 生成回复建议和操作草稿
- 跨平台个人信息整合
- 支持多种数据源接入

## 使用场景
- 统一查看和管理个人通信数据
- AI 辅助起草邮件和回复
- 个人信息流自动化处理

## 依赖和前提条件
- 配置邮件和数据源访问凭证
- 设置数据拉取频率和范围

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `dist`
- `openclaw.plugin.json`
- `package-lock.json`
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

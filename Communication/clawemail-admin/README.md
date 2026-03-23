# ClawEmail Admin

> 管理和配置 @clawemail.com Google Workspace 邮箱账户的管理工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | ClawEmail Admin |
| **作者** | cto1 |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/cto1-clawemail-admin |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/cto1/clawemail-admin |
| **安全评级** | 🔴 High |

## 功能概述
- 创建和管理 @clawemail.com 邮箱账户
- 用户权限和角色配置
- 邮箱配额和存储管理
- 安全策略和访问控制设置
- 批量账户管理操作

## 使用场景
- 管理员为团队智能体批量配置 Google Workspace 邮箱
- IT 运维管理 ClawEmail 域名下的账户权限和安全策略
- 初始部署时快速搭建团队邮箱系统

## 依赖和前提条件
- 拥有 ClawEmail.com 管理员权限
- 配置 Google Workspace 管理 API
- 已有 ClawEmail 域名和组织账户

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

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
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

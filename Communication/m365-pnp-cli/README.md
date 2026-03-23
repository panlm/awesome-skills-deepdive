# Skill

> 通过 Microsoft 365 CLI (PnP) 管理 M365 租户，涵盖 SharePoint、Teams、OneDrive 等服务

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Skill |
| **作者** | thomyg |
| **版本** | 1.0.1 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/thomyg-m365-pnp-cli |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/thomyg/m365-pnp-cli |
| **安全评级** | 🔴 High |

## 功能概述
- SharePoint Online 站点和列表管理
- Microsoft Teams 团队和频道操作
- OneDrive 文件管理和共享
- Azure AD 用户和组管理
- Power Platform 资源管理
- M365 租户配置和设置
- 批量操作和自动化脚本执行

## 使用场景
- 批量管理 SharePoint 站点权限和内容
- 自动化 Teams 频道创建和成员管理
- 通过 CLI 批量处理 M365 租户管理任务

## 依赖和前提条件
- 安装 Microsoft 365 CLI (m365)
- M365 租户管理员账户或相应权限
- Node.js 运行环境
- 完成 m365 login 认证

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

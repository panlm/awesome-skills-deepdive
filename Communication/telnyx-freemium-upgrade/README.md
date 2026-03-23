# Telnyx Freemium Upgrade

> 自动化完成 Telnyx 电信账户从免费版到专业版的升级流程

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Telnyx Freemium Upgrade |
| **作者** | teamtelnyx |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/teamtelnyx-telnyx-freemium-upgrade |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/teamtelnyx/telnyx-freemium-upgrade |
| **安全评级** | 🔴 High |

## 功能概述
- 自动检测当前 Telnyx 账户等级
- 引导并执行从免费版到专业版的升级操作
- 处理升级过程中的验证和确认步骤
- 升级完成后验证新功能可用性

## 使用场景
- 需要使用 Telnyx 高级功能时快速完成账户升级
- 批量管理多个 Telnyx 账户的版本升级

## 依赖和前提条件
- Telnyx 账户凭据
- Telnyx API 密钥
- 有效的支付方式（专业版需付费）

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

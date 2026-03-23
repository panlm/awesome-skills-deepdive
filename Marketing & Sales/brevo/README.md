# Brevo

> Brevo (SendinBlue) 营销自动化工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Brevo |
| **作者** | yujesyoga |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/yujesyoga-brevo |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/yujesyoga/brevo |
| **安全评级** | 🟡 Medium |

## 功能概述
- Brevo 邮件营销管理
- 联系人列表操作
- 邮件模板和活动管理
- 营销自动化工作流

## 使用场景
- 通过 Brevo 平台管理邮件营销活动
- 自动化 Brevo 中的客户触达流程

## 依赖和前提条件
- API 密钥
- Python 运行环境
- Brevo (SendinBlue)

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
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
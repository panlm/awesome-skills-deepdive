# Kit Email Marketing Operator

> **AI-powered email marketing for Kit (ConvertKit)**

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Kit Email Marketing Operator |
| **作者** | kevjade |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/kevjade-kit-email-operator |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kevjade/kit-email-operator |
| **安全评级** | 🟡 Medium |

## 功能概述
- Writes complete emails matching your brand voice
- Creates 3 subject line options for every email
- Follows proven email marketing best practices
- Uses Kit personalization tags (first name, custom fields)
- Creates and schedules broadcasts via API
- Targets specific tags and segments
- Tracks campaign performance
- Manages drafts and scheduled sends

## 使用场景
- 自动化邮件营销
- 管理外联和跟进
- 个性化营销邮件生成

## 依赖和前提条件
- Node.js / npm
- 数据库

## 包含文件
- `BUILD-COMPLETE.md`
- `INSTALLATION.md`
- `ORIGINAL_README.md`
- `SETUP.md`
- `SKILL.md`
- `_meta.json`
- `examples`
- `references`
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
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
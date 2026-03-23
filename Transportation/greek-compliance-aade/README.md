# Greek Compliance Aade

> Greek tax compliance with AADE/TAXIS integration — VAT, payroll, EFKA, municipal taxes, stamp duty. Human confirmation for all submissions.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Greek Compliance Aade |
| **作者** | satoshistackalotto |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/satoshistackalotto-greek-compliance-aade |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/satoshistackalotto/greek-compliance-aade |
| **安全评级** | 🔴 High |

## 功能概述
- AADE credentials are only used when submitting filings to the government portal
- All submissions require human approval (four-eyes workflow: preparer ≠ approver)
- Filing preparation, VAT calculation, and report generation work fully offline
- Credentials are never stored on disk — always use environment variables
- Greek Law First: All calculations and processes comply with current Greek tax and labor law
- AADE Ready: All data formatted for direct TAXIS platform submission

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `EVALS.json`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，5 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
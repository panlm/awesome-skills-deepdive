# Efka Api Integration

> Greek social security (EFKA) integration — employee records, contribution calculations, APD declarations. Human approval for submissions.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Efka Api Integration |
| **作者** | satoshistackalotto |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/satoshistackalotto-efka-api-integration |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/satoshistackalotto/efka-api-integration |
| **安全评级** | 🟡 Medium |

## 功能概述
- OpenClaw Artifact Ready: Designed specifically for upload and deployment to OpenClaw instances
- File-Based Processing: Robust file system approach suitable for production deployment
- Greek Employment Law Compliance: Complete adherence to Greek social security regulations
- Payroll Integration: Seamless connection with existing Greek payroll systems
- Production Scalability: Built to handle multiple clients and high transaction volumes
- /data/efka/employees/active/           # Current employee records

## 使用场景
- 健康数据管理与分析
- 健身目标跟踪
- 个人健康报告生成

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
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
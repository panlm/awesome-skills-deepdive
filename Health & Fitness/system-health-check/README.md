# System Health Check

> 系统健康检查和监控工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | System Health Check |
| **作者** | satoshistackalotto |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/satoshistackalotto-system-health-check |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/satoshistackalotto/system-health-check |
| **安全评级** | 🔴 High |

## 功能概述
- Fast & Non-Destructive: Read-only checks — never modifies any data
- Comprehensive: Covers every layer from skill files to encryption status
- Actionable Output: Every failure includes a specific remediation command
- Cron-Friendly: Exit code 0 for all-pass, exit code 1 for any failure
- English Output: Plain English report suitable for accounting assistants and system admins
- "canonical-data-map"
- "accounting-workflows"
- "greek-compliance-aade"

## 使用场景
- 执行服务器和服务的健康检查
- 监控系统资源使用和性能
- 生成系统健康状态报告

## 依赖和前提条件
- API 密钥或访问令牌
- 数据库
- 网络连接

## 包含文件
- `EVALS.json`
- `SKILL.md`
- `_meta.json`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，5 项中风险。凭证获取：需要多种敏感凭证；持久化机制：设置系统级持久化

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

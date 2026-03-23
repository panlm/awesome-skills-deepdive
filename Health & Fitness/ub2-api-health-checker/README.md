# API Health Checker

> A skill that enables Claw to test API endpoints, verify their responses, measure performance, and generate a health report.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | API Health Checker |
| **作者** | underbench2-gif |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/underbench2-gif-ub2-api-health-checker |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/underbench2-gif/ub2-api-health-checker |
| **安全评级** | 🟡 Medium |

## 功能概述
- "Check if https://api.example.com/v1/status is responding correctly"
- "Test all endpoints in this API and report which ones are failing"
- "Monitor these 5 endpoints and tell me their average response times"
- "Verify that the /users endpoint returns a JSON array with the expected fields"
- Endpoints — A list of URLs to test
- Expected status codes — What HTTP status each endpoint should return (default: 200)

## 使用场景
- 健康数据管理与分析
- 健身目标跟踪
- 个人健康报告生成

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
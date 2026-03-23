# Jenkins

> Interact with Jenkins CI/CD server via REST API. Use when you need to trigger builds, check build status, view console output, manage jobs, or monitor Jenkins nodes and queue. Supports deployment to different Jenkins instances via environment variables.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Jenkins |
| **作者** | guoway |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/guoway-jenkins |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/guoway/jenkins |
| **安全评级** | 🟢 Low |

## 功能概述
- `JENKINS_URL` (example: `https://jenkins.example.com`)
- `JENKINS_USER` (your Jenkins username)
- `JENKINS_API_TOKEN` (API token from Jenkins user settings)
- URL and credentials are variables by design for cross-environment deployment.
- API responses are output as JSON.
- For parameterized builds, use `--params` with JSON string.

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；信息采集：读取环境变量或系统信息

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
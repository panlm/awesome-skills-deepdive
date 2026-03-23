# Key Expiry Tracker

> Track **only expiry dates** (metadata) for API keys/client secrets/certificates and alert before they expire.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Key Expiry Tracker |
| **作者** | tradmangh |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/tradmangh-key-expiry-tracker |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tradmangh/key-expiry-tracker |
| **安全评级** | 🟡 Medium |

## 功能概述
- `client-secret`: Azure AD, API keys
- `api-key`: Third-party APIs (OpenAI, etc.)
- `certificate`: SSL/TLS certs
- `token`: OAuth tokens, refresh tokens
- `password`: Passwords with expiry
- 14 days: Warning (yellow)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- API Key
- OAuth

## 包含文件
- `METADATA.json`
- `SKILL.md`
- `_meta.json`
- `scripts`

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
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
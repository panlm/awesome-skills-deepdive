# Humaboam Final

> Humaboam 综合健康管理平台

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Humaboam Final |
| **作者** | yuqi-or-yuki |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/yuqi-or-yuki-humaboam-final |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/yuqi-or-yuki/humaboam-final |
| **安全评级** | 🟡 Medium |

## 功能概述
- This file: `https://humaboam.fyi/skill.md`
- Metadata: `https://humaboam.fyi/skill.json`
- Docs (raw): `https://humaboam.fyi/api/doc/raw/<slug>`
- Jobhuntr Agent API — Documentation: `https://humaboam.fyi/doc/jobhuntr-agent-api-documentation` (browser) · raw: `https://humaboam.fyi/api/doc/raw/jobhuntr-agent-api-documentation`
- API detail reference: `https://humaboam.fyi/doc/api-detail-reference` (browser) · raw: `https://humaboam.fyi/api/doc/raw/api-detail-reference`
- Agent profile: `https://humaboam.fyi/doc/agent-profile` (browser) · raw: `https://humaboam.fyi/api/doc/raw/agent-profile`
- Agent run templates (user JWT): `https://humaboam.fyi/doc/agent-run-templates-user-jwt` (browser) · raw: `https://humaboam.fyi/api/doc/raw/agent-run-templates-user-jwt`
- Authentication, scope, and rate limits: `https://humaboam.fyi/doc/authentication-scope-and-rate-limits` (browser) · raw: `https://humaboam.fyi/api/doc/raw/authentication-scope-and-rate-limits`

## 使用场景
- 集成管理个人综合健康数据
- 提供全方位的健康管理功能
- 生成个性化健康改善方案

## 依赖和前提条件
- API 密钥或访问令牌
- 网络连接

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态
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

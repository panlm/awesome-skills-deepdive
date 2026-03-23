# honor

> JSON-only API for dashboard data. No markdown responses.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | honor |
| **作者** | johnmcgucki |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/johnmcgucki-picqer-fulfillment |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/johnmcgucki/picqer-fulfillment |
| **安全评级** | 🟡 Medium |

## 功能概述
- API key only in local .env file
- No credentials in OpenClaw config
- Access via Tailscale only

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`
- `cron.ts`
- `env.ts`
- `index.ts`
- `package.json`
- `tools`
- `tsconfig.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
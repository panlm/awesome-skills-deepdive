# Air France - KLM

> Track Air France flights using the Air France–KLM Open Data APIs (Flight Status). Use when the user gives a flight number/date (e.g., AF007 on 2026-01-29) and wants monitoring, alerts (delay/gate/aircraft changes), or analysis (previous-flight chain, aircraft tail number → cabin recency / Wi‑Fi). Also use when setting up or tuning polling schedules within API rate limits.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Air France - KLM |
| **作者** | iclems |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/iclems-airfrance-afkl |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/iclems/airfrance-afkl |
| **安全评级** | 🟡 Medium |

## 功能概述
- Flight status + schedule vs latest published times
- Terminal / gate (when published)
- Boarding close time (when available)
- Aircraft tail number + cabin configuration summary (best-effort)
- Previous-flight chain (useful to estimate delay risk)
- Compact alerts: you only get pinged when displayed fields change

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- API Key

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
# Nori Health

> Query your personal health data and get coaching from Nori, your AI health coach. Use when the user asks about sleep, workouts, nutrition, weight, heart rate, HRV, or wants health insights. NOT for: medical diagnosis, prescriptions, or emergency health situations.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Nori Health |
| **作者** | danmurphy1217 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/danmurphy1217-nori-health |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/danmurphy1217/nori-health |
| **安全评级** | 🟡 Medium |

## 功能概述
- "Compare my sleep on days I work out vs rest days"
- "What should I eat to hit my protein goal today?"
- "Show me my resting heart rate trend this month"
- "How's my recovery looking after yesterday's run?"
- "I had two eggs and toast with avocado for breakfast"
- "I did 30 minutes of strength training"

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`

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
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
# Intervals Icu Api

> Intervals.icu 运动训练分析 API

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Intervals Icu Api |
| **作者** | pseuss |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/pseuss-intervals-icu-api |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/pseuss/intervals-icu-api |
| **安全评级** | 🟡 Medium |

## 功能概述
- Activities: Completed workouts with actual data (GPS, power, HR). Retrieved from `/athlete/{id}/activities`
- Events: Planned workouts on your calendar. Retrieved from `/athlete/{id}/events`
- 200: Success
- 201: Created successfully (activities, events)
- 400: Bad request (invalid parameters)
- 401: Unauthorized (invalid API key or token)
- 404: Not found (invalid IDs)
- 429: Rate limited (too many requests)

## 使用场景
- 获取 Intervals.icu 的训练数据
- 分析运动表现和训练负荷
- 同步训练计划和实际执行情况

## 依赖和前提条件
- API Key
- OAuth

## 包含文件
- `ORIGINAL_README.md`
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

# MH weather

> 通过 wttr.in 或 Open-Meteo API 获取全球任意地点的实时天气和天气预报

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | MH weather |
| **作者** | mohdalhashemi98-hue |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/mohdalhashemi98-hue-mh-weather |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mohdalhashemi98-hue/mh-weather |
| **安全评级** | 🟢 Low |

## 功能概述
- 实时天气状况查询
- 多日天气预报获取
- 支持全球任意城市和地点
- 温度、湿度、风速等详细气象数据
- 双数据源（wttr.in 和 Open-Meteo）
- 无需 API 密钥即可使用

## 使用场景
- 出行前查询目的地天气情况
- 每日早间天气播报提醒
- 根据天气预报智能推荐穿衣和出行建议

## 依赖和前提条件
- 网络访问权限（访问 wttr.in 或 Open-Meteo）
- 无需额外 API 密钥

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 存在 1 项高风险，0 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

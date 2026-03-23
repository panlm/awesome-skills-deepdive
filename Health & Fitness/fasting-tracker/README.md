# Fasting Tracker

> 间歇性禁食计时和跟踪工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Fasting Tracker |
| **作者** | jhillin8 |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/jhillin8-fasting-tracker |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jhillin8/fasting-tracker |
| **安全评级** | 🟢 Low |

## 功能概述
- Fast Timer: Start a fast and get real-time elapsed tracking with countdown to key metabolic milestones
- Eating Window Tracking: Log when you break your fast and automatically calculate your eating window duration
- Metabolic Milestones: Receive alerts at ketosis (12h), fat adaptation (16h), autophagy (24h), and deeper cellular renewal thresholds
- Smart History: Review past fasts with duration, eating windows, and consistency metrics
- Logs the fast start time
- Displays current time and target milestones
- Sets background tracking (runs even when you close the app)
- Records the end time

## 使用场景
- 记录禁食开始和结束时间
- 跟踪禁食窗口和进食窗口
- 分析禁食历史和达标率

## 依赖和前提条件
- 参见 SKILL.md 获取详细依赖信息

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

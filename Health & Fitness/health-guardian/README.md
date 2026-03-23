# Health Guardian

> Proactive health monitoring for AI agents. Apple Health integration, pattern detection, anomaly alerts. Built for agents caring for humans with chronic conditions.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Health Guardian |
| **作者** | cgtreadw |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/cgtreadw-health-guardian |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/cgtreadw/health-guardian |
| **安全评级** | 🟢 Low |

## 功能概述
- Detects concerning patterns before they become emergencies
- Alerts your human (or you) when something needs attention
- Learns what's normal for YOUR human, not population averages
- Apple Health via Health Auto Export (iCloud sync)
- 39 metrics supported: HR, HRV, sleep, steps, temperature, BP, SpO2, and more
- Hourly import option for real-time monitoring

## 使用场景
- 健康数据管理与分析
- 健身目标跟踪
- 个人健康报告生成

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `config.example.json`
- `package.json`
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
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；持久化机制：涉及定时或后台任务

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
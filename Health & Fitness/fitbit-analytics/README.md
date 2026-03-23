# Fitbit Analytics

> Fitbit 数据深度分析和可视化工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Fitbit Analytics |
| **作者** | kesslerio |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/kesslerio-fitbit-analytics |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kesslerio/fitbit-analytics |
| **安全评级** | 🔴 High |

## 功能概述
- Activity Tracking: Fetch daily steps, distance, calories, and active minutes
- Heart Rate: Access continuous heart rate data and resting heart rate trends
- Sleep Analytics: Analyze sleep stages (Deep, Light, REM, Wake) and efficiency
- Reports: Generate daily/weekly health reports with trend analysis
- Automation: Scripts ready for cron jobs (e.g., daily summaries)

## 使用场景
- 对 Fitbit 数据进行深度统计分析
- 生成健康数据的可视化报告
- 识别健康指标的异常模式

## 依赖和前提条件
- Python / pip
- OAuth

## 包含文件
- `ORIGINAL_README.md`
- `SETUP.md`
- `SKILL.md`
- `_meta.json`
- `docs`
- `references`
- `scripts`

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
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

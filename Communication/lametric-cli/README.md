# Lametric Cli

> LaMetric TIME/SKY 智能显示器的命令行控制工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Lametric Cli |
| **作者** | dedene |
| **版本** | 1.0.2 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/dedene-lametric-cli |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/dedene/lametric-cli |
| **安全评级** | 🔴 High |

## 功能概述
- 通过命令行控制 LaMetric 智能显示器
- 推送自定义文字和图标到显示屏
- 管理设备上的应用和小工具
- 设置通知、闹钟和计时器
- 调节显示亮度和音量
- 支持 LaMetric TIME 和 SKY 两款设备

## 使用场景
- 在桌面智能显示器上展示实时数据和通知
- 将 AI 助手的消息和提醒推送到 LaMetric 设备
- 作为智能家居仪表盘显示关键指标

## 依赖和前提条件
- LaMetric TIME 或 SKY 智能显示器
- LaMetric 开发者账户和 API 密钥
- 设备与控制端在同一网络
- OpenClaw 运行环境

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

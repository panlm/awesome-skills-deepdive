# Lametric Cli

> Control LaMetric TIME/SKY smart displays from the command line. Use when sending notifications, controlling device brightness/volume, managing timers, or displaying data on LaMetric devices. Triggers on "LaMetric", "smart display", "notification to device", "set timer", "send alert to clock".

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Lametric Cli |
| **作者** | dedene |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/dedene-lametric-cli |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/dedene/lametric-cli |
| **安全评级** | 🟡 Medium |

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- macOS
- Homebrew
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
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
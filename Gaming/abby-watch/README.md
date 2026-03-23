# abby-watch

> 简单的时间显示工具，为 Abby 提供当前时间查询和倒计时功能

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | abby-watch |
| **作者** | earnabitmore365 |
| **ClawHub** | https://clawskills.sh/skills/earnabitmore365-abby-watch |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/earnabitmore365/abby-watch |
| **安全评级** | 🟢 Low |

## 功能概述
- 显示当前时间（简洁格式 HH:MM）
- 详细模式输出完整日期、时间和时区
- 倒计时功能，计算到指定时间的剩余时长
- 基于 Python 的 CLI 工具，无外部依赖
- 支持命令行参数 `--verbose` 和 `--countdown`

## 使用场景
- 快速查询当前时间
- 设置特定时间的倒计时提醒
- 在 agent 对话中提供时间信息

## 依赖和前提条件
- Python 3
- 无外部 Python 包依赖

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 技能描述和使用说明 |
| scripts/time_cli.py | Python 时间 CLI 脚本 |
| references/time-formats.md | 时间格式参考文档 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 仅使用 Python 标准库 datetime 和 argparse，无 shell 调用 |
| SEC-02 数据外泄 | 🟢 Safe | 无网络请求，不发送任何数据到外部 |
| SEC-03 凭证获取 | 🟢 Safe | 不读取任何凭证或环境变量 |
| SEC-04 供应链风险 | 🟢 Safe | 无第三方依赖，仅使用 Python 标准库 |
| SEC-05 文件系统篡改 | 🟢 Safe | 不读写任何文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 纯 CLI 工具，无 prompt 操作 |
| SEC-07 越权操作 | 🟢 Safe | 无权限提升或系统操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无 cron、服务注册或持久化行为 |
| SEC-09 信息采集 | 🟢 Safe | 仅获取本地系统时间 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读，无混淆 |

**综合评级: 🟢 Low**
**风险摘要:** 极简的纯本地时间工具，无网络、无文件读写、无外部依赖，安全风险极低。

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

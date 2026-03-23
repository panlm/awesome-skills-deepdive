# casual-cron

> 通过自然语言创建 OpenClaw 定时任务

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | casual-cron |
| **作者** | gostlightai |
| **ClawHub** | https://clawskills.sh/skills/gostlightai-casual-cron |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/gostlightai/casual-cron |
| **安全评级** | 🟡 Medium |

## 功能概述
- 自然语言解析为 cron 表达式（如"每天早上8点"→ `0 8 * * *`）
- 支持一次性和重复定时任务
- DST 时区感知（默认 America/New_York）
- 支持 Telegram、WhatsApp、Slack、Discord、Signal 多渠道投递
- 严格的 cron 运行守卫规则
- 执行前需用户确认

## 使用场景
- 通过聊天自然语言设置提醒："20分钟后提醒我"
- 创建每日/每周定时任务并投递到 Telegram

## 依赖和前提条件
- Python 3、openclaw CLI
- `CRON_DEFAULT_CHANNEL` 环境变量

## 包含文件
- `SKILL.md` — 技能定义和调度规则
- `scripts/cron_builder.py` — 自然语言解析为 cron 命令
- `test/test_cron_builder.py` — 测试文件

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 生成并可执行 `openclaw cron add` 命令 |
| SEC-02 数据外泄 | 🟡 Medium | 通过 --deliver 将消息发送到外部渠道（Telegram 等） |
| SEC-03 凭证获取 | 🟢 Safe | 不直接处理凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 纯 Python 标准库，无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 不修改文件系统 |
| SEC-06 Prompt 注入 | 🟡 Medium | 用户输入直接进入 --message 参数，可能被注入 |
| SEC-07 越权操作 | 🟢 Safe | 通过 openclaw CLI 正常操作 |
| SEC-08 持久化机制 | 🟡 Medium | 创建 cron 定时任务，持久运行 |
| SEC-09 信息采集 | 🟢 Safe | 不采集信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 可创建持久化定时任务并向外部渠道发送消息，用户输入需注意注入风险

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

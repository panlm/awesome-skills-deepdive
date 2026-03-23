# birthday-reminder

> 自然语言生日管理工具，支持添加/查询/提醒生日和计算年龄

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | birthday-reminder |
| **作者** | manantra |
| **ClawHub** | https://clawskills.sh/skills/manantra-birthday-reminder |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/manantra/birthday-reminder |
| **安全评级** | 🟢 Low |

## 功能概述
- 自然语言解析生日信息
- 支持多种日期格式
- 自动计算年龄和倒计时
- 生日提醒（7天/1天/当天）
- JSON 文件存储
- 支持 Cron 自动检查

## 使用场景
- 用自然语言管理亲友生日
- 设置自动生日提醒通知
- 查询即将到来的生日

## 依赖和前提条件
Python 3

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts/birthday.py`
- `scripts/reminder.py`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | Python 脚本执行，涉及文件读写 |
| SEC-02 数据外泄 | 🟢 Safe | 无网络通信 |
| SEC-03 凭证获取 | 🟢 Safe | 不涉及凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 仅使用 Python 标准库 |
| SEC-05 文件系统篡改 | 🟡 Medium | 写入固定路径 /home/clawd/clawd/data/birthdays.json |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权操作 |
| SEC-08 持久化机制 | 🟡 Medium | 支持 cron 定时任务 |
| SEC-09 信息采集 | 🟢 Safe | 仅管理用户提供的生日数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰简洁 |

**综合评级: 🟢 Low**
**风险摘要:** 简单的本地文件操作工具，路径硬编码但安全性可控

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

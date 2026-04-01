# apple-remind-me

> 自然语言创建 Apple 提醒事项

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | apple-remind-me |
| **作者** | plgonzalezrx8 |
| **ClawHub** | https://clawskills.sh/skills/plgonzalezrx8-apple-remind-me |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/plgonzalezrx8/apple-remind-me |
| **许可证** | 未指定 |
| **安全评级** | 🟢 Low |

## 功能概述
- Output Format:
- Note: Day names must be lowercase (monday, tuesday, etc.)
- Backend: Uses `remindctl` command-line tool (macOS native)
- Date Parsing: BSD date utility (macOS compatible)
- Time Format: ISO 8601 timestamps for remindctl
- List Filtering: Shows only incomplete reminders by default

## 依赖和前提条件
- macOS (darwin)
- `date` (BSD version, macOS default)
- `python3` (for JSON parsing in list-reminders.sh)
- Apple Reminders.app

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `complete-reminder.sh` — 脚本文件
- `create-reminder.sh` — 脚本文件
- `delete-reminder.sh` — 脚本文件
- `edit-reminder-message.sh` — 脚本文件
- `edit-reminder-time.sh` — 脚本文件
- `list-reminders.sh` — 脚本文件

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟢 Low**
**风险摘要:** 低风险技能，可安全使用

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
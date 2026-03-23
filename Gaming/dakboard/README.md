# dakboard

> 管理 DAKboard 屏幕显示设备，推送自定义数据到智能展示面板

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | dakboard |
| **作者** | krisclarkdev |
| **ClawHub** | https://clawskills.sh/skills/krisclarkdev-dakboard |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/krisclarkdev/dakboard |
| **安全评级** | 🟢 Low |

## 功能概述
- 列出关联的 DAKboard 设备（Raspberry Pi 等）
- 列出可用的屏幕布局
- 更新设备显示的屏幕布局
- 推送自定义指标数据到 Metrics 块
- 推送 JSON 数据到 Fetch 块
- API Key 自动脱敏保护（错误信息中替换为 REDACTED）

## 使用场景
- 远程管理智能家居展示屏
- 向仪表盘推送实时传感器或统计数据
- 切换展示屏上的显示布局

## 依赖和前提条件
- Python 3（标准库即可）
- `DAKBOARD_API_KEY` 环境变量

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 使用说明和安全文档 |
| scripts/dakboard.py | Python CLI 脚本 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | Python 脚本仅使用标准库 urllib，无 shell 调用 |
| SEC-02 数据外泄 | 🟢 Safe | 仅与 dakboard.com 官方 API 通信，发送的是用户主动推送的显示数据 |
| SEC-03 凭证获取 | 🟢 Safe | 仅读取 DAKBOARD_API_KEY 环境变量，错误信息中自动脱敏 |
| SEC-04 供应链风险 | 🟢 Safe | 无第三方依赖，仅 Python 标准库 |
| SEC-05 文件系统篡改 | 🟢 Safe | 脚本声明不读写任何本地文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 纯 CLI 工具 |
| SEC-07 越权操作 | 🟢 Safe | 仅操作用户自己的 DAKboard 设备 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化行为 |
| SEC-09 信息采集 | 🟢 Safe | 仅获取用户自己的设备和屏幕列表 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码顶部有清晰的安全声明注释 |

**综合评级: 🟢 Low**
**风险摘要:** 设计良好的工具型技能，内置安全声明和 API Key 脱敏，风险极低。

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

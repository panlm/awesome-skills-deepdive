# gotify

> 通过 Gotify 发送推送通知

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | gotify |
| **作者** | jmagar |
| **ClawHub** | https://clawskills.sh/skills/jmagar-gotify |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jmagar/gotify |
| **安全评级** | 🟢 Low |

## 功能概述
- 通过 Gotify 服务器发送推送通知
- 支持自定义标题、消息和优先级（0-10）
- Markdown 格式支持
- 适用于长时间任务完成通知
- 简单的 bash 脚本实现

## 使用场景
- 长时间运行任务完成后推送通知
- 重要事件提醒到手机/桌面
- CI/CD 流程中的状态通知

## 依赖和前提条件
- curl、jq
- Gotify 服务器和应用令牌
- 配置文件 `~/.clawdbot/credentials/gotify/config.json`

## 包含文件
- `SKILL.md` — 技能定义
- `scripts/send.sh` — 发送通知脚本

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 仅 curl 发送 HTTP POST 请求 |
| SEC-02 数据外泄 | 🟢 Safe | 发送到用户自有 Gotify 服务器 |
| SEC-03 凭证获取 | 🟡 Medium | 读取 ~/.clawdbot/credentials/gotify/config.json 中的令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 纯 bash 脚本 |
| SEC-05 文件系统篡改 | 🟢 Safe | 不修改文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🟢 Safe | 仅发送通知 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 不采集信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 脚本简洁可审计 |

**综合评级: 🟢 Low**
**风险摘要:** 简单的推送通知工具，发送到用户自有服务器，风险极低

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

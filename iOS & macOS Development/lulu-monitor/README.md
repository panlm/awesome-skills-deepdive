# lulu-monitor

> macOS LuLu 防火墙的 AI 智能伴侣，自动分析网络连接并通过 Telegram 通知

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | lulu-monitor |
| **作者** | easonc13 |
| **ClawHub** | https://clawskills.sh/skills/easonc13-lulu-monitor |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/easonc13/lulu-monitor |
| **安全评级** | 🔴 High |

## 功能概述
- 监控 LuLu 防火墙弹窗警报
- AI 分析网络连接风险（使用 haiku 模型）
- Telegram 通知带操作按钮（允许/阻止）
- 自动执行模式（高置信度时自动允许）
- launchd 服务自动启动
- 完整的安装/卸载/配置脚本

## 使用场景
- 自动化防火墙警报处理
- 远程通过 Telegram 管理防火墙规则
- AI 辅助判断未知连接的安全性

## 依赖和前提条件
- macOS
- LuLu 防火墙
- Node.js
- OpenClaw Gateway + Telegram 频道
- Accessibility 权限

## 包含文件
SKILL.md, scripts/install.sh, scripts/uninstall.sh, scripts/configure.sh, scripts/check-prerequisites.sh

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 通过 osascript 控制 LuLu UI，调用 sessions_spawn，需要 Accessibility 权限 |
| SEC-02 数据外泄 | 🟡 Medium | 通过 Telegram 发送防火墙警报信息（IP、进程名等） |
| SEC-03 凭证获取 | 🟢 Safe | 需要 Telegram ID 配置，但不获取系统凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 从 GitHub 克隆仓库并运行 npm install |
| SEC-05 文件系统篡改 | 🟡 Medium | 写入 ~/.openclaw/lulu-monitor/ 和 LaunchAgents |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🔴 High | 需要 Accessibility 权限控制其他应用 UI，调用 sessions_spawn |
| SEC-08 持久化机制 | 🟡 Medium | 安装 launchd 服务实现持久化 |
| SEC-09 信息采集 | 🟡 Medium | 收集网络连接信息（进程名、IP、端口、DNS） |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码可读，结构清晰 |

**综合评级: 🔴 High**
**风险摘要:** 需要 Accessibility 权限和 sessions_spawn，可控制其他应用 UI，发送网络连接信息到 Telegram

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

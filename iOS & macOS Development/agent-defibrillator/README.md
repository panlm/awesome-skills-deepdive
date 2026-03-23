# agent-defibrillator

> AI Agent 网关看门狗，自动监控并重启崩溃的 OpenClaw 网关进程

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | agent-defibrillator |
| **作者** | hazy2go |
| **ClawHub** | https://clawskills.sh/skills/hazy2go-agent-defibrillator |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/hazy2go/agent-defibrillator |
| **安全评级** | 🟡 Medium |

## 功能概述
- 每 10 分钟检查一次 Agent 网关健康状态
- 网关崩溃时自动重启（带 5 分钟冷却期）
- 版本不匹配检测，自动更新重启
- Discord 通知支持，远程了解 Agent 状态
- 锁文件防止并发运行
- 自动清理孤儿进程
- 通过 macOS launchd 作为系统服务运行

## 使用场景
- Agent 无人值守运行时自动恢复
- npm 更新后自动检测版本不匹配并重启
- 通过 Discord 远程监控 Agent 存活状态

## 依赖和前提条件
- macOS（使用 launchd）
- OpenClaw Gateway（通过 launchd 运行）
- 可选：Discord 频道（用于通知）

## 包含文件
SKILL.md（技能定义）, defibrillator.sh（看门狗脚本）, install.sh（安装脚本）

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 执行 launchctl bootstrap/bootout 管理服务，pkill 杀进程，curl 检查健康端点 |
| SEC-02 数据外泄 | 🟢 Safe | 仅通过 openclaw message send 发送 Discord 通知，无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 未获取或存储任何凭证 |
| SEC-04 供应链风险 | 🟡 Medium | install.sh 从 GitHub 下载脚本（curl），存在供应链替换风险 |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅写入 ~/.openclaw/scripts/ 和 ~/Library/LaunchAgents/ 标准位置 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 安装 launchd 服务实现持久化运行 |
| SEC-08 持久化机制 | 🟡 Medium | 创建 launchd plist 实现开机自启 |
| SEC-09 信息采集 | 🟢 Safe | 仅读取进程状态和版本信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读，无混淆 |

**综合评级: 🟡 Medium**
**风险摘要:** 安装 launchd 持久化服务并从远程下载脚本，建议验证脚本内容后安装

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

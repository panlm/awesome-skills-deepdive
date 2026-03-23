# toolguard-daemon-control

> 将长期运行的进程作为 macOS launchd 服务管理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | toolguard-daemon-control |
| **作者** | johnnylambada |
| **ClawHub** | https://clawskills.sh/skills/johnnylambada-toolguard-daemon-control |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/johnnylambada/toolguard-daemon-control |
| **安全评级** | 🟡 Medium |

## 功能概述
- 安装可执行文件为 launchd 用户代理
- 自动重启失败的服务
- 服务状态查看和日志访问
- 环境变量和工作目录配置
- 批量服务管理

## 使用场景
- 将后台进程注册为 macOS 服务
- 管理持久化运行的开发工具
- 查看服务日志和状态

## 依赖和前提条件
- macOS（launchd）

## 包含文件
SKILL.md, scripts/install.sh, scripts/uninstall.sh, scripts/status.sh, scripts/list.sh, scripts/logs.sh

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 执行 launchctl load/unload 管理服务，可运行任意可执行文件 |
| SEC-02 数据外泄 | 🟢 Safe | 无网络数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 未获取凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 仅使用系统 launchd |
| SEC-05 文件系统篡改 | 🟡 Medium | 写入 ~/Library/LaunchAgents/ 创建 plist 文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 可将任意命令注册为持久化服务 |
| SEC-08 持久化机制 | 🟡 Medium | 核心功能就是创建持久化 launchd 服务 |
| SEC-09 信息采集 | 🟢 Safe | 仅读取服务状态和日志 |
| SEC-10 混淆/反分析 | 🟢 Safe | 脚本清晰可读 |

**综合评级: 🟡 Medium**
**风险摘要:** 服务管理工具可将任意命令持久化为 launchd 服务，需确保安装的命令可信

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

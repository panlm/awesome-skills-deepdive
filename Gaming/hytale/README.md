# hytale

> 管理本地 Hytale 专用服务器，支持启动、停止、更新和状态检查

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | hytale |
| **作者** | newcastlegeek |
| **ClawHub** | https://clawskills.sh/skills/newcastlegeek-hytale |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/newcastlegeek/hytale |
| **安全评级** | 🟡 Medium |

## 功能概述
- 启动 Hytale 游戏服务器（screen 后台会话）
- 优雅停止游戏服务器
- 下载/更新服务器文件（通过官方 Hytale Downloader）
- 检查服务器运行状态
- 支持内存配置（默认 4GB）

## 使用场景
- 管理个人 Hytale 游戏专用服务器
- 远程启停游戏服务器
- 自动更新服务器版本

## 依赖和前提条件
- Java 21+
- screen
- Hytale Downloader（用户需自行获取）
- hytale-downloader-credentials.json（用户提供）

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 使用说明和命令文档 |
| hytale.sh | 服务器管理 Shell 脚本 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 执行 Java 和 screen 命令，运行二进制下载器，使用 chmod +x |
| SEC-02 数据外泄 | 🟢 Safe | 仅与 Hytale 官方下载服务器通信 |
| SEC-03 凭证获取 | 🟡 Medium | 使用 hytale-downloader-credentials.json 凭证文件 |
| SEC-04 供应链风险 | 🟡 Medium | 下载并执行外部二进制文件（hytale-downloader-linux-amd64） |
| SEC-05 文件系统篡改 | 🟡 Medium | 在 ~/hytale_server/ 创建文件，使用 chmod 修改权限 |
| SEC-06 Prompt 注入 | 🟢 Safe | 纯 CLI 工具 |
| SEC-07 越权操作 | 🟢 Safe | 在用户主目录下操作，无 sudo |
| SEC-08 持久化机制 | 🟡 Medium | 使用 screen 创建后台会话运行 Java 服务器进程 |
| SEC-09 信息采集 | 🟢 Safe | 仅检查本地进程状态 |
| SEC-10 混淆/反分析 | 🟢 Safe | 脚本清晰可读 |

**综合评级: 🟡 Medium**
**风险摘要:** 执行外部二进制文件、创建后台进程和修改文件系统，但操作范围限于用户目录。

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

# nordvpn

> 通过 `nordvpn` CLI 控制 Linux 上的 NordVPN

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | nordvpn |
| **作者** | maciekish |
| **ClawHub** | https://clawskills.sh/skills/maciekish-nordvpn |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/maciekish/nordvpn |
| **安全评级** | 🟡 Medium |

## 功能概述
- 连接/断开 NordVPN
- 选择国家/城市/服务器组
- 查看连接状态和账户信息
- 调整设置（防火墙、Kill Switch、DNS 等）
- 管理端口白名单和子网白名单

## 使用场景
- 自动化需要地域路由的任务
- 临时 VPN 隧道用于特定操作

## 依赖和前提条件
- `nordvpn` CLI（通过 snap 或包管理器安装）
- NordVPN 账户（需登录）

## 包含文件
- `SKILL.md` — 技能定义和完整命令参考
- `_meta.json` — 元数据

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 调用 nordvpn CLI 命令控制网络连接 |
| SEC-02 数据外泄 | 🟢 Safe | 不发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 NordVPN 账户登录 |
| SEC-04 供应链风险 | 🟢 Safe | 依赖官方 NordVPN CLI |
| SEC-05 文件系统篡改 | 🟢 Safe | 不修改文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🟡 Medium | 可更改网络路由和防火墙设置；可能需要 sudo |
| SEC-08 持久化机制 | 🟢 Safe | NordVPN 设置由其自身管理 |
| SEC-09 信息采集 | 🟢 Safe | nordvpn status 获取连接信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 纯 SKILL.md 文档 |

**综合评级: 🟡 Medium**
**风险摘要:** 控制 VPN 网络连接和防火墙设置，可能影响系统网络路由

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

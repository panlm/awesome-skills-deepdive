# network-scanner

> 扫描本地网络发现设备和服务

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | network-scanner |
| **作者** | florianbeer |
| **ClawHub** | https://clawskills.sh/skills/florianbeer-network-scanner |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/florianbeer/network-scanner |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- **Device inventory**: Keep track of all devices on your network
- **Security audits**: Identify unknown devices
- **Documentation**: Generate network maps for documentation
- **Automation**: Integrate with home automation to detect device presence
- Use `sudo` for accurate MAC address detection (nmap needs privileges for ARP)
- Configure your local DNS server for better hostname resolution
- Add configured networks to skip route verification on every scan
- Add networks you can't reach privately to the blocklist to prevent accidents

## 使用场景

Scans local networks using nmap to discover connected devices and collect their IP addresses, MAC addresses, vendor names, and hostnames via reverse DNS. Blocks scanning of public IP ranges and blocklisted networks to prevent accidental abuse.

## 依赖和前提条件

- Homebrew: nmap
- Python 3

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

> ⚠️ ClawHub 安全扫描未通过或状态未知，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 危险 | 使用 sudo 提权操作 |
| SEC-02 数据外泄 | 🟢 通过 | 无外部网络数据发送行为 |
| SEC-03 凭证获取 | 🟢 通过 | 不涉及任何凭证或密钥操作 |
| SEC-04 供应链风险 | 🟡 警告 | 安装软件包: nmap |
| SEC-05 文件系统篡改 | 🟢 通过 | 无文件系统修改行为 |
| SEC-06 Prompt 注入 | 🟢 通过 | 指令清晰透明，无隐藏行为 |
| SEC-07 越权操作 | 🟢 通过 | 操作范围与声称功能一致 |
| SEC-08 持久化机制 | 🟢 通过 | 无持久化行为 |
| SEC-09 信息采集 | 🟡 警告 | 有限系统信息采集: 网络配置信息 |
| SEC-10 混淆/反分析 | 🟢 通过 | 所有指令清晰可读，无编码或间接执行 |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 发现 1 项危险和 2 项警告。主要风险: 使用 sudo 提权操作

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:44 UTC

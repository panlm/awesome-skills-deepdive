# healthkit-sync

> 同步和导出 HealthKit 健康数据

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | healthkit-sync |
| **作者** | mneves75 |
| **ClawHub** | https://clawskills.sh/skills/mneves75-healthkit-sync |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mneves75/healthkit-sync |
| **安全评级** | 🟢 ClawHub Verified (Benign) |

## 功能概述

- User asks about syncing health data from iPhone
- User mentions `healthsync` CLI commands
- User wants to fetch steps, heart rate, sleep, or workout data
- User needs to pair a Mac with an iOS device
- User asks about the iOS Health Sync project architecture
- User mentions certificate pinning or mTLS patterns
- Private IPv4: `192.168.*`, `10.*`, `172.16-31.*`
- IPv6 loopback: `::1`, link-local: `fe80::`

## 使用场景

healthkit-sync provides CLI commands and patterns for syncing Apple HealthKit data from an iPhone to a Mac over a local network. It uses mTLS certificate pinning and macOS Keychain storage to keep health data on-device and off cloud services. The skill covers pairing, data fetching, and the underlying iOS app architecture.

## 依赖和前提条件

- macOS 系统
- jq
- Swift/Xcode

## 安全状态

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟢 Benign |

> ClawHub 安全扫描已通过，跳过详细审计。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 生成时间: 2026-04-01 04:44 UTC

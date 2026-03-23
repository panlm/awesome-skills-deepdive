# swiftui-empty-app-init

> 使用 XcodeGen 初始化最小化 SwiftUI iOS 应用

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | swiftui-empty-app-init |
| **作者** | ignaciocervino |
| **ClawHub** | https://clawskills.sh/skills/ignaciocervino-swiftui-empty-app-init |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ignaciocervino/swiftui-empty-app-init |
| **安全评级** | 🟢 Low |

## 功能概述
- 生成单一 .xcodeproj（无 workspace）
- 最小化 SwiftUI @main App 模板
- 通过 XcodeGen 自动化项目生成
- 自定义 Bundle ID 和部署目标

## 使用场景
- 快速创建新 SwiftUI 项目
- 统一团队项目模板

## 依赖和前提条件
- Xcode
- XcodeGen（PATH 中可用）

## 包含文件
SKILL.md（完整初始化指南）

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 仅指导使用 XcodeGen 生成项目 |
| SEC-02 数据外泄 | 🟢 Safe | 无数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 未获取凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 仅依赖 XcodeGen |
| SEC-05 文件系统篡改 | 🟢 Safe | 在当前目录创建项目文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 纯项目生成 |
| SEC-10 混淆/反分析 | 🟢 Safe | 完全可读 |

**综合评级: 🟢 Low**
**风险摘要:** 简单的项目初始化指南，零风险

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

# ios-simulator

> 自动化 iOS 模拟器工作流（simctl + idb），支持 UI 自动化和应用管理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | ios-simulator |
| **作者** | tristanmanchester |
| **ClawHub** | https://clawskills.sh/skills/tristanmanchester-ios-simulator |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tristanmanchester/ios-simulator |
| **安全评级** | 🟢 Low |

## 功能概述
- 模拟器生命周期管理（创建/启动/擦除/删除）
- 应用安装、启动、卸载
- 基于 Accessibility 树的 UI 自动化
- 截图和录屏
- 推送通知测试
- 隐私权限管理
- 剪贴板和 URL 操作

## 使用场景
- 自动化 iOS 应用测试流程
- UI 自动化交互（点击、输入文字）
- 批量管理多个模拟器设备

## 依赖和前提条件
- macOS + Xcode
- xcrun simctl
- 可选：idb（UI 自动化）

## 包含文件
SKILL.md（完整使用指南）, scripts/ios-sim.mjs（Node CLI 工具）, references/TROUBLESHOOTING.md

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 通过 child_process.spawn 执行 xcrun simctl 和 idb 命令 |
| SEC-02 数据外泄 | 🟢 Safe | 所有操作限于本地模拟器 |
| SEC-03 凭证获取 | 🟢 Safe | 未获取凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 仅依赖系统工具 |
| SEC-05 文件系统篡改 | 🟡 Medium | 可擦除/删除模拟器，有 --yes 确认保护 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 所有操作限于用户级模拟器 |
| SEC-08 持久化机制 | 🟢 Safe | 写入状态文件但无系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 仅收集模拟器状态信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰，有安全分层设计 |

**综合评级: 🟢 Low**
**风险摘要:** 设计良好的模拟器自动化工具，有安全分层（SAFE/CAUTION/DANGEROUS）

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

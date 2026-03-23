# swift-concurrency-expert

> Swift 6.2+ 并发代码审查与修复专家，涵盖 Actor 隔离和 Sendable 安全

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | swift-concurrency-expert |
| **作者** | steipete |
| **ClawHub** | https://clawskills.sh/skills/steipete-swift-concurrency-expert |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/steipete/swift-concurrency-expert |
| **安全评级** | 🟢 Low |

## 功能概述
- Swift Concurrency 问题诊断
- Actor 隔离修复建议
- Sendable 合规性检查
- @MainActor 和 nonisolated 最佳实践
- SwiftUI 并发指南
- 最小化行为变更的修复策略

## 使用场景
- 修复 Swift 6 并发编译错误
- 审查现有代码的并发安全性
- 迁移到 Swift 6.2 并发模型

## 依赖和前提条件
- Swift 6.2+
- Xcode

## 包含文件
SKILL.md（核心指南）, references/（Swift 6.2 并发参考、SwiftUI 并发指南）

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 纯知识库 |
| SEC-02 数据外泄 | 🟢 Safe | 无数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 未获取凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 不修改文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 纯技术参考 |
| SEC-10 混淆/反分析 | 🟢 Safe | 完全可读 |

**综合评级: 🟢 Low**
**风险摘要:** 纯 Swift 并发知识库，零风险

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

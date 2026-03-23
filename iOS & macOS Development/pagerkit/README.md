# pagerkit

> PagerKit SwiftUI 分页导航库的专家指南和最佳实践

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | pagerkit |
| **作者** | szpakkamil |
| **ClawHub** | https://clawskills.sh/skills/szpakkamil-pagerkit |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/szpakkamil/pagerkit |
| **安全评级** | 🟢 Low |

## 功能概述
- PKPagesView 主容器配置
- PKPage 单页自定义
- 动态页面生成（ForEach）
- 页面指示器样式定制
- 页面切换事件处理
- 跨 Apple 平台支持

## 使用场景
- SwiftUI 应用中实现分页导航
- 自定义页面指示器样式
- 处理页面切换事件

## 依赖和前提条件
- Swift 5.9+
- iOS 14.0+/macOS 14.0+/tvOS 14.0+/visionOS 1.0+

## 包含文件
SKILL.md（完整指南）, references/（9 个 API 参考文档）

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 纯知识库，无代码执行 |
| SEC-02 数据外泄 | 🟢 Safe | 无数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 未获取凭证 |
| SEC-04 供应链风险 | 🟢 Safe | SPM 依赖明确 |
| SEC-05 文件系统篡改 | 🟢 Safe | 不修改文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 纯 API 参考 |
| SEC-10 混淆/反分析 | 🟢 Safe | 完全可读 |

**综合评级: 🟢 Low**
**风险摘要:** 纯 SwiftUI 库参考文档，零风险

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

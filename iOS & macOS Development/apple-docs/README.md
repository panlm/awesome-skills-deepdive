# apple-docs

> 查询 Apple 开发者文档、API 和 WWDC 视频（2014-2025）

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | apple-docs |
| **作者** | thesethrose |
| **ClawHub** | https://clawskills.sh/skills/thesethrose-apple-docs |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/thesethrose/apple-docs |
| **安全评级** | 🟢 Low |

## 功能概述
- 搜索 Apple 开发者文档和符号
- API 探索（继承关系、协议遵循）
- 平台/版本兼容性检查
- WWDC 视频搜索（含字幕、代码示例）
- 技术浏览和示例项目查找
- 内置缓存机制减少 API 调用

## 使用场景
- 查找 SwiftUI API 文档和用法
- 搜索 WWDC 特定主题的视频
- 检查 API 的平台可用性

## 依赖和前提条件
- Node.js

## 包含文件
SKILL.md（技能定义）, cli.js（CLI 工具）

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 仅通过 fetch 调用 Apple 公开 API 和 GitHub 公开数据 |
| SEC-02 数据外泄 | 🟡 Medium | 向 developer.apple.com 和 GitHub 发送 HTTP 请求获取文档数据 |
| SEC-03 凭证获取 | 🟢 Safe | 未获取凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 从 GitHub raw 内容获取 WWDC 数据文件 |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅读取操作，不修改文件系统 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 仅访问公开 API |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 仅收集公开文档信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟢 Low**
**风险摘要:** 只读文档查询工具，仅访问 Apple 公开 API

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

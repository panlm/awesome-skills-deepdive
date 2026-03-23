# sfsymbol-generator

> 从 SVG 生成 Xcode SF Symbol 资源目录（.symbolset）

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | sfsymbol-generator |
| **作者** | svkozak |
| **ClawHub** | https://clawskills.sh/skills/svkozak-sfsymbol-generator |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/svkozak/sfsymbol-generator |
| **安全评级** | 🟢 Low |

## 功能概述
- 从 SVG 创建 .symbolset 资源
- 支持模板注入（Ultralight/Regular/Black 权重）
- 自动计算路径边界和居中
- 生成正确的 Contents.json
- 支持自定义资源目录位置

## 使用场景
- 为 iOS/macOS 应用添加自定义 SF Symbol
- 从设计稿 SVG 生成符号资源
- 批量生成品牌图标符号

## 依赖和前提条件
- Node.js
- Xcode 项目

## 包含文件
SKILL.md, scripts/generate.sh（基础生成）, scripts/generate-from-template.js（模板注入）, assets/template.svg

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 仅执行文件复制和 JSON 生成，无危险命令 |
| SEC-02 数据外泄 | 🟢 Safe | 无网络请求 |
| SEC-03 凭证获取 | 🟢 Safe | 未获取凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 写入指定的 Assets.xcassets 目录 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 仅操作项目资源目录 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 仅处理 SVG 文件数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰，纯文件操作 |

**综合评级: 🟢 Low**
**风险摘要:** 安全的资源文件生成工具，仅操作项目目录

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

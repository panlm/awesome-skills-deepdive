# swiftfindrefs

> 使用 swiftfindrefs (IndexStoreDB) 查找 Swift 符号的所有引用

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | swiftfindrefs |
| **作者** | michaelversus |
| **ClawHub** | https://clawskills.sh/skills/michaelversus-swiftfindrefs |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/michaelversus/swiftfindrefs |
| **安全评级** | 🟢 Low |

## 功能概述
- 通过 IndexStore 查询符号引用
- 跨模块重构的引用发现
- 缺失 import 修复工作流
- 删除/重命名前的使用审计
- 支持按项目名、符号名、符号类型筛选

## 使用场景
- 重构前查找所有引用
- 移动符号后修复缺失 import
- 审计符号使用情况后安全删除

## 依赖和前提条件
- macOS + Xcode
- swiftfindrefs CLI（brew 安装）
- 项目需已构建（DerivedData 存在）

## 包含文件
SKILL.md（使用指南）, references/（CLI 参考、工作流、故障排除）

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 仅查询 IndexStore 数据库，只读操作 |
| SEC-02 数据外泄 | 🟢 Safe | 无数据外传 |
| SEC-03 凭证获取 | 🟢 Safe | 未获取凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要通过 brew tap 从第三方 GitHub 仓库安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 不修改文件（配合其他工具修改） |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 仅读取 DerivedData |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 仅收集源文件路径信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 完全可读 |

**综合评级: 🟢 Low**
**风险摘要:** 只读符号引用查询工具，安全性高

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

# NPkill

> Clean up node_modules and .next folders to free up disk space using npkill. Specifically designed to help JavaScript and Next.js developers remove accumulated build artifacts that consume significant storage. Provides both interactive and automated cleanup options with safety checks to protect important system directories.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | NPkill |
| **作者** | ashirbadgudu |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawskills.sh/skills/ashirbadgudu-npkill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ashirbadgudu/npkill |
| **安全评级** | 🟢 Low |

## 功能概述
- Your disk space is running low due to accumulated node_modules folders
- You want to clean up old Next.js build artifacts (.next folders)
- You need to maintain a clean development environment
- You want to identify which projects are consuming the most disk space
- You want to perform regular maintenance on your development workspace
- Warnings for Protected Directories: npkill highlights system/app directories that shouldn't be deleted with a ⚠️ symbol

## 使用场景
- 管理 macOS/iOS 日历事件
- 查询日程安排与空闲时间
- 通过命令行创建/修改日历事件

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
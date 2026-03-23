# Changelog Generator

> 从 Git 提交历史生成结构化变更日志，遵循 Keep a Changelog 格式

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Changelog Generator |
| **作者** | ryudi84 |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/ryudi84-sovereign-changelog-maker |

## 功能概述
- 从 Git 提交历史自动生成结构化变更日志
- 遵循 Keep a Changelog (keepachangelog.com) 标准格式
- 按分类分组：Added、Changed、Deprecated、Removed、Fixed、Security
- 自动关联 PR/Issue 链接
- 使用面向用户的描述而非内部技术术语
- 对破坏性变更自动生成迁移说明
- 提供语义化版本建议

## 使用场景
- 发布新版本时，从 Git 历史自动生成规范的 CHANGELOG.md
- 需要快速整理一段时间内的代码变更并以用户友好的方式呈现
- 开源项目维护者需要标准化变更日志流程

## 依赖和前提条件
- Git 仓库环境
- 无额外依赖

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 未发现明显安全风险，文档透明可审计

---
> 本文档由 awesome-skills-deepdive skill 自动生成

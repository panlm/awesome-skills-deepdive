# OpenTangl

> 不只是代码生成器，而是一整个自动化开发团队——你写愿景，它交付代码

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | OpenTangl |
| **作者** | 8co |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/8co-opentangl |

## 功能概述
- 为 JavaScript/TypeScript 项目配置自驱动开发循环
- 自动规划功能、编写代码、验证构建
- 自动创建 Pull Request、审查代码差异并合并
- 支持多仓库作为一个产品统一管理
- 检测项目结构并生成配置文件
- 支持现有项目改进和从零开始两种模式
- 需要用户逐步确认，不会跳过关键步骤

## 使用场景
- 将产品愿景交给 AI，让它自主完成从编码到 PR 合并的完整开发流程
- 管理多个关联仓库的协同开发，统一产品交付
- 自动化 JS/TS 项目的功能开发和代码审查

## 依赖和前提条件
- Node.js >= 18
- Git
- GitHub CLI（`gh`）已认证
- 需要克隆并安装 OpenTangl：`git clone https://github.com/8co/opentangl.git && npm install`

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 4 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
# Feature Forge

> 从自然语言描述生成完整功能——组件、API 路由、数据库迁移等

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Feature Forge |
| **作者** | guifav |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/guifav-feature-forge |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/guifav/feature-forge |
| **安全评级** | 🔴 High |

## 功能概述
- 从自然语言描述生成前端组件代码
- 自动创建 API 路由和端点
- 生成数据库迁移脚本
- 端到端功能脚手架自动生成

## 使用场景
- 描述需求后自动生成完整的 CRUD 功能代码
- 快速原型开发——从文字描述到可运行代码

## 依赖和前提条件
- Node.js / npm、项目框架环境

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

> 本文档由 awesome-skills-deepdive skill 自动生成

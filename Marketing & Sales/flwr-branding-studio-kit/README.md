# FLWR Branding Studio Kit

> 品牌设计工作室工具套件

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | FLWR Branding Studio Kit |
| **作者** | vansearch |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/vansearch-flwr-branding-studio-kit |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/vansearch/flwr-branding-studio-kit |
| **安全评级** | 🟡 Medium |

## 功能概述
- 品牌视觉设计工具集
- 品牌素材生成
- Logo 和配色方案管理
- 品牌一致性维护

## 使用场景
- 使用工具套件创建完整的品牌视觉体系
- 批量生成符合品牌规范的设计素材

## 依赖和前提条件
- Node.js
- npm
- Node.js 依赖包
- GitHub API
- Instagram API

## 包含文件
- `CONTRIBUTING.md`
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `bin`
- `docs`
- `package.json`
- `requirements.txt`
- `task.md`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，4 项中风险。数据外泄：大量外部数据传输




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
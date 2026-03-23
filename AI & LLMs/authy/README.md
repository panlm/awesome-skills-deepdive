# Authy

> 安全密钥注入工具——通过环境变量将密钥注入子进程，Agent 永远不会看到密钥的实际值。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Authy |
| **作者** | eric8810 |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/eric8810-authy |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/eric8810/authy |
| **安全评级** | 🟡 Medium |

## 功能概述
- 通过 `authy run` 将密钥作为环境变量注入子进程
- Agent 只能发现密钥名称，无法查看实际密钥值
- 支持按策略（scope）限制可访问的密钥范围
- 自动将密钥名转换为标准环境变量格式（如 db-host → DB_HOST）
- 提供密钥名称发现功能（`authy list`）
- 完善的错误代码体系（认证失败、权限拒绝、令牌过期等）

## 使用场景
- 在 AI Agent 执行需要 API 密钥的命令时安全注入凭证
- 避免密钥在日志或对话中意外泄露
- 为不同部署环境配置独立的密钥策略和访问控制

## 依赖和前提条件
- 需要 `authy` 命令行工具（PATH 中可用）
- 需要 `AUTHY_KEYFILE` 和 `AUTHY_TOKEN` 环境变量

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

---
> 本文档由 awesome-skills-deepdive skill 自动生成

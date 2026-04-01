# Vincent - Credentials

> 为 AI Agent 提供安全的凭证管理，存储 API 密钥、密码和 OAuth Token

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Vincent - Credentials |
| **作者** | glitch003 |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/glitch003-vincent-credentials |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/glitch003/vincent-credentials |
| **安全评级** | 🔴 High |

## 功能概述
- 安全存储 API 密钥、密码、OAuth Token 和 SSH 密钥
- 自动将凭证写入 .env 文件，无需暴露明文值
- 支持多种凭证类型的统一管理
- 凭证加密存储，防止泄露
- 支持凭证的创建、读取、更新和删除操作
- 适用于多 Agent 环境的凭证共享和隔离

## 使用场景
- AI Agent 安全存储和使用第三方 API 密钥，避免硬编码
- 多个 Agent 之间安全共享凭证，支持权限隔离
- 自动化部署时将凭证注入 .env 文件，简化配置流程

## 依赖和前提条件
- 环境变量 `API_KEY`
- 环境变量 `SSH_KEY`
- 环境变量 `OAUTH_TOKEN`
- 环境变量 `SERVICE_TOKEN`
- 环境变量 `ACME_API_KEY`
- Node.js 运行环境

## 安全状态
> 暂无安全审计数据

---
> 本文档由 awesome-skills-deepdive skill 自动生成

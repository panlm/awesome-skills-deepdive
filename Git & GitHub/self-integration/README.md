# Self-Integration

> 通过 Membrane API 连接任意外部应用并执行操作，支持 Slack、Linear、HubSpot、Jira 等服务

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Self-Integration |
| **作者** | bratchenko |
| **版本** | 1.0.0 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/bratchenko-self-integration |

## 功能概述
- 通过 Membrane API 查找已有连接或创建新的第三方服务连接
- 支持 OAuth 认证流程，自动生成认证链接供用户授权
- 搜索并发现可用操作（Action），支持自然语言意图匹配
- 自动执行操作（发消息、创建任务、同步数据、管理联系人等）
- 当无现成连接器时，可通过 Membrane Agent 自动构建新的连接器
- 当无匹配操作时，可通过 Membrane Agent 自动创建新的操作
- 完整的三步工作流：获取连接 → 查找操作 → 执行操作

## 使用场景
- AI Agent 需要统一接入 Slack、Jira、HubSpot、Salesforce、Google Sheets 等多个外部应用
- 需要跨多个 SaaS 服务执行操作（如发 Slack 消息、创建 Linear 任务、同步 HubSpot 联系人）
- 需要为尚未有预置连接器的新服务快速创建集成

## 依赖和前提条件
- 环境变量 `MEMBRANE_TOKEN`：Membrane API 令牌（从 [Membrane 控制台](https://console.getmembrane.com) 获取）
- 环境变量 `MEMBRANE_API_URL`：Membrane API 地址（默认 `https://api.getmembrane.com`）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成

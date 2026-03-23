# amplitude-automation

> 通过 Rube MCP (Composio) 自动化 Amplitude 产品分析任务

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | amplitude-automation |
| **作者** | sohamganatra |
| **ClawHub** | https://clawskills.sh/skills/sohamganatra-amplitude-automation |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/sohamganatra/amplitude-automation |
| **安全评级** | 🟡 Medium |

## 功能概述
- 通过 Rube MCP 发送事件到 Amplitude
- 查询用户活动和事件流
- 查找和识别用户身份
- 管理用户群组（Cohort）
- 支持事件批量发送
- 需要通过 Composio 进行 OAuth 认证

## 使用场景
- 自动化产品分析事件追踪
- 批量查询用户行为数据
- 用户身份管理和属性设置

## 依赖和前提条件
- Rube MCP 服务连接（`https://rube.app/mcp`）
- Amplitude 账户及 OAuth 授权

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件，包含工作流和 API 使用方法 |
| _meta.json | 元数据 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 纯指令型，无本地命令执行 |
| SEC-02 数据外泄 | 🟡 Medium | 通过 Rube MCP 向 Amplitude 发送事件数据，属预期功能但依赖第三方 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 Amplitude OAuth 连接，凭证由 Composio 管理 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖 Rube MCP (rube.app) 第三方服务作为代理 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt 风险 |
| SEC-07 越权操作 | 🟢 Safe | 操作范围在 Amplitude 授权内 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化行为 |
| SEC-09 信息采集 | 🟡 Medium | 可查询用户活动数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟡 Medium**
**风险摘要:** 依赖第三方 Rube MCP 服务代理 API 调用，数据流经第三方平台

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

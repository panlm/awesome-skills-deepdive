# fast-io

> Agent 团队协作云文件管理平台

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | fast-io |
| **作者** | dbalve |
| **ClawHub** | https://clawskills.sh/skills/dbalve-fast-io |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/dbalve/fast-io |
| **安全评级** | 🟡 Medium |

## 功能概述
- 为 Agent 团队提供共享工作区（上传、协作、AI 问答）
- 19 个整合工具覆盖完整 REST API
- 品牌化分享（Send/Receive/Exchange）
- 内置 AI 文档理解和语义搜索
- 工作流原语（任务、工作日志、审批、待办）
- 所有权转移给人类用户
- 免费计划：50GB 存储 + 5000 月度积分

## 使用场景
- Agent 团队间共享文件和协作
- 创建品牌化数据室分享给客户
- 使用 AI 查询和理解文档内容

## 依赖和前提条件
- 网络访问
- Fast.io MCP 服务器（mcp.fast.io）

## 包含文件
- `SKILL.md` — 完整 Agent 使用指南（19 个工具说明）
- `references/REFERENCE.md` — 平台详细参考文档

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 通过 MCP 协议调用，无本地命令执行 |
| SEC-02 数据外泄 | 🟡 Medium | 上传文件到 Fast.io 云平台，创建可分享链接 |
| SEC-03 凭证获取 | 🟡 Medium | 需要认证令牌，通过 session 自动管理 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖专有 MCP 服务器（mcp.fast.io） |
| SEC-05 文件系统篡改 | 🟢 Safe | 不修改本地文件系统 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 有权限管理和范围控制 |
| SEC-08 持久化机制 | 🟢 Safe | 无本地持久化 |
| SEC-09 信息采集 | 🟢 Safe | 不采集本地信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 纯文档，无代码 |

**综合评级: 🟡 Medium**
**风险摘要:** 云服务集成，文件上传到第三方平台，依赖专有 MCP 服务器

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

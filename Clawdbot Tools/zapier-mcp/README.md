# zapier-mcp

> 通过 Zapier MCP 连接 8000+ 应用，含 UI 仪表板集成

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | zapier-mcp |
| **作者** | maverick-software |
| **ClawHub** | https://clawskills.sh/skills/maverick-software-zapier-mcp |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/maverick-software/zapier-mcp |
| **安全评级** | 🟡 Medium |

## 功能概述
- 8000+ 应用连接
- URL 即认证（无 OAuth 复杂度）
- mcporter 集成
- instructions 自然语言参数
- UI 仪表板配置
- SSE 响应格式支持

## 使用场景
- 通过 Zapier 连接 Slack/Gmail/Notion 等应用
- 用自然语言描述操作意图
- 在 Clawdbot 仪表板中管理 Zapier 连接

## 依赖和前提条件
mcporter, Zapier 账户, Clawdbot >= 2026.1.0

## 包含文件
- `SKILL.md`
- `_meta.json`
- `reference/README.md`
- `reference/zapier-backend.ts`
- `reference/zapier-controller.ts`
- `reference/zapier-views.ts`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 通过 mcporter 执行 MCP 工具调用 |
| SEC-02 数据外泄 | 🟡 Medium | 与 Zapier MCP API 通信 |
| SEC-03 凭证获取 | 🟡 Medium | MCP URL 包含认证信息 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖 mcporter 和 Zapier 服务 |
| SEC-05 文件系统篡改 | 🟡 Medium | 写入 mcporter.json 配置 |
| SEC-06 Prompt 注入 | 🟡 Medium | instructions 参数由 AI 解释，有间接注入可能 |
| SEC-07 越权操作 | 🟡 Medium | 可操作 8000+ 应用（发邮件/创建事件等） |
| SEC-08 持久化机制 | 🟢 Safe | 无本地持久化 |
| SEC-09 信息采集 | 🟡 Medium | 可查询和操作已连接应用数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 配置和接口清晰 |

**综合评级: 🟡 Medium**
**风险摘要:** MCP URL 含认证信息，instructions 参数被 AI 解释有间接注入风险

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

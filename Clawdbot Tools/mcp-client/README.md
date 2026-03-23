# mcp-client

> MCP 客户端实现，连接工具、数据源和服务

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | mcp-client |
| **作者** | nantes |
| **ClawHub** | https://clawskills.sh/skills/nantes-mcp-client |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nantes/mcp-client |
| **安全评级** | 🟡 Medium |

## 功能概述
- MCP 服务器连接
- 工具列表和调用
- 资源访问（文件/API/数据库）
- Prompt 模板获取
- file:// URI 安全警告
- Python 和 CLI 双接口

## 使用场景
- 连接和调用 MCP 服务器工具
- 访问 MCP 资源（文件/API）
- 集成 MCP 生态

## 依赖和前提条件
Python 3.8+, requests

## 包含文件
- `SKILL.md`
- `_meta.json`
- `mcp_client.py`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | Python 脚本执行 HTTP 请求 |
| SEC-02 数据外泄 | 🟡 Medium | 与 MCP 服务器通信 |
| SEC-03 凭证获取 | 🟡 Medium | API Key 通过 Bearer 令牌传递 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖 requests 库 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无本地文件写入 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 可调用 MCP 工具执行广泛操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟡 Medium | file:// URI 可读取服务器文件（已有警告） |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码简洁清晰 |

**综合评级: 🟡 Medium**
**风险摘要:** MCP 客户端安全性取决于连接的服务器，file:// URI 有文件泄露风险

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

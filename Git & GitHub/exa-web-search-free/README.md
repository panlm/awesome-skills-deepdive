# Exa Web Search (Free)

> 通过 Exa MCP 提供免费 AI 搜索能力，支持网页搜索、代码搜索和企业研究，无需 API 密钥

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Exa Web Search (Free) |
| **作者** | whiteknight07 |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/whiteknight07-exa-web-search-free |

## 功能概述
- 网页搜索（web_search_exa）：搜索新闻、信息和事实，支持快速和深度两种模式
- 代码搜索（get_code_context_exa）：从 GitHub、Stack Overflow 查找代码示例和文档
- 企业研究（company_research_exa）：获取企业商业信息和新闻
- 高级工具：域名/日期过滤搜索、查询扩展、全页抓取、人物搜索、AI 研究代理
- 通过 mcporter 配置和调用，无需 API 密钥
- 基于神经搜索技术，语义理解优于关键词匹配

## 使用场景
- AI Agent 执行实时网页搜索获取最新信息，无需配置付费 API
- 开发时快速搜索代码示例和 API 文档

## 依赖和前提条件
- `mcporter`（MCP 客户端工具）
- 网络访问（连接 https://mcp.exa.ai/mcp）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive skill 自动生成

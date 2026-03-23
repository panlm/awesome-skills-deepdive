# Arc Security Mcp

> AI 优先的安全情报服务，基于 LLM 驱动的意图分析，提供 361+ 技能审计的 743+ 发现、25 条模式规则和 22 种攻击类别。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Arc Security Mcp |
| **作者** | trypto1019 |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/trypto1019-arc-security-mcp |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/trypto1019/arc-security-mcp |
| **安全评级** | 🟢 Low |

## 功能概述
- 检查 ClawHub 技能是否为已知恶意或危险技能（73+ 已知危险技能数据库）
- 对技能源代码进行 25 种危险模式的静态分析
- 基于 LLM 的语义意图分析，检测混淆或隐藏的恶意行为
- 提供完整的威胁情报统计和最新发现报告
- 首次记录 A2A（Agent-to-Agent）蠕虫传播机制
- 首次记录反安全训练攻击
- 通过 MCP SSE 端点提供实时安全查询服务

## 使用场景
- 在安装 ClawHub 技能前检查其安全性和已知漏洞
- 对自定义技能代码进行自动化安全审计
- 获取 AI Agent 生态系统的最新威胁情报和攻击趋势

## 依赖和前提条件
- MCP SSE 端点：`https://arcself.com/mcp/sse`
- 无需本地安装，通过 MCP 协议远程访问

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

---
> 本文档由 awesome-skills-deepdive skill 自动生成

# Baselight data via MCP

> 通过 MCP 协议连接 Baselight 数据平台，发现和查询 50+ 优质数据源，支持 SQL 实时查询结构化数据。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Baselight data via MCP |
| **作者** | pjsousa79 |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/pjsousa79-baselight-mcp |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/pjsousa79/baselight-mcp |
| **安全评级** | 🟡 Medium |

## 功能概述
- 访问 50+ 优质数据源（Kaggle、世界银行、Eurostat、Yahoo Finance、FRED 等）
- 支持加密货币数据（DefiLlama、CoinDesk、XrpScan）
- 覆盖体育、天气、健康、教育、犯罪等多领域数据
- 支持 SEC 文件、IMF、OECD、美国人口普查等政府数据
- 可对结构化数据执行实时 SQL 查询
- 支持 OAuth 和 API Key 两种认证方式

## 使用场景
- 需要从多个权威数据源获取结构化数据进行分析
- 在 AI 工具中直接用 SQL 查询金融、经济或社会数据
- 进行跨数据源的综合研究和数据验证

## 依赖和前提条件
- MCP 服务器地址：`https://api.baselight.app/mcp`
- 需要 OAuth 或 API Key 认证

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

---
> 本文档由 awesome-skills-deepdive skill 自动生成

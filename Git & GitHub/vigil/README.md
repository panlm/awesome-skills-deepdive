# Vigil

> AI Agent 工具调用安全护栏，拦截破坏性命令、SSRF、SQL 注入、路径遍历和凭证泄露等风险操作

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Vigil |
| **作者** | robinoppenstam |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/robinoppenstam-vigil |

## 功能概述
- 在 Agent 执行工具调用前进行安全验证，拦截危险操作
- 检测破坏性命令（`rm -rf`、`mkfs`、反弹 Shell 等）并阻断
- 防御 SSRF 攻击（元数据端点、localhost、内网 IP 访问）
- 拦截 SQL 注入（DROP TABLE、UNION SELECT 等）和路径遍历攻击
- 识别 Prompt 注入和编码攻击（base64 decode、eval）
- 检测凭证泄露（API Key、AWS Key、Token 等）并上报
- 22 条内置规则，零运行时依赖，单次检查延迟低于 2ms
- 支持 warn（仅日志）和 enforce（强制阻断）两种运行模式

## 使用场景
- 为执行 Shell 命令、文件操作或 API 调用的 AI Agent 添加安全防护层
- 在任何 MCP Server 或 Agent 框架中嵌入工具调用审计机制
- 审查和监控 Agent 的实际操作行为

## 依赖和前提条件
- npm 包 `vigil-agent-safety`（12.3KB，Apache 2.0 许可证）
- 安装命令：`npm install vigil-agent-safety`
- 零运行时依赖

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，6 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive skill 自动生成

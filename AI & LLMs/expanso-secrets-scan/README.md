# Expanso secrets-scan

> 检测代码和文本中硬编码的密钥、令牌和密码等敏感信息

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Expanso secrets-scan |
| **作者** | aronchick |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/aronchick-expanso-secrets-scan |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/aronchick/expanso-secrets-scan |
| **安全评级** | 🟡 Medium |

## 功能概述
- 扫描代码、配置文件和日志中意外提交的凭证
- 支持多种密钥类型检测：API 密钥、令牌、密码、私钥等
- 支持 CLI 模式和 MCP 模式两种运行方式
- 可集成到 Git pre-commit 钩子中使用
- 支持 CI/CD 流水线中的自动化安全扫描
- 检测 AWS、GitHub、Slack、OpenAI 等多平台凭证
- 输出详细的发现报告，包含类型、严重性和上下文信息

## 使用场景
- 代码提交前自动扫描，防止密钥泄露到版本控制系统
- CI/CD 流水线中集成安全检查，确保代码库无敏感信息
- 安全审计时批量扫描整个代码库的凭证泄露风险

## 依赖和前提条件
- OpenAI API Key
- Expanso Edge 运行时

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成

# Expanso log-sanitize

> 使用模式匹配脱敏日志中的密码、令牌和 API 密钥等敏感数据，完全本地运行

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Expanso log-sanitize |
| **作者** | aronchick |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/aronchick-expanso-log-sanitize |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/aronchick/expanso-log-sanitize |
| **安全评级** | 🟡 Medium |

## 功能概述
- 通过模式匹配检测并脱敏日志中的敏感数据
- 支持多种敏感模式：密码、API Key、Bearer Token、AWS 密钥、JWT 等
- 完全本地运行，无需任何外部 API 调用
- 提供 CLI 模式（管道处理）和 MCP 模式（HTTP 服务）
- 输出 JSON 格式结果，包含脱敏文本、脱敏数量和元数据
- 支持处理单条日志和整个日志文件

## 使用场景
- 在将日志发送到聚合平台前自动脱敏敏感信息
- 与技术支持共享日志前清除凭证和密钥
- 满足安全合规要求的日志预处理流程

## 依赖和前提条件
- expanso-edge（CLI 运行环境）
- pipeline-cli.yaml / pipeline-mcp.yaml（管道配置）

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
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成

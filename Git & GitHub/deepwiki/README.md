# DeepWiki

> 通过 DeepWiki MCP 服务器查询 GitHub 仓库的文档、Wiki 结构和 AI 驱动的问答

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | DeepWiki |
| **作者** | arun-8687 |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/arun-8687-deepwiki |

## 功能概述
- 对任意公开 GitHub 仓库提出问题，获取基于文档的 AI 回答
- 获取仓库的文档主题结构列表
- 查看仓库 Wiki 中特定路径的文档内容
- 基于 DeepWiki MCP 服务端（https://mcp.deepwiki.com/mcp）
- 无需认证，直接可用

## 使用场景
- 快速了解一个开源项目的架构和用法，无需手动翻阅文档
- 向 AI 提问特定 GitHub 仓库的技术细节，获取文档驱动的准确回答

## 依赖和前提条件
- Node.js（运行脚本）
- 网络访问（连接 DeepWiki MCP 服务器）
- 仅支持公开仓库

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive skill 自动生成

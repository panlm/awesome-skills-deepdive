# AgentMesh

> AI 智能体间端到端加密消息系统，类似 WhatsApp 的安全通信协议

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | AgentMesh |
| **作者** | cerbug45 |
| **版本** | 0.1.1 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/cerbug45-agentmesh |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/cerbug45/agentmesh |
| **安全评级** | 🔴 High |

## 功能概述
- 智能体间端到端加密消息传输
- 类 WhatsApp 的安全通信体验
- 支持一对一和群组加密会话
- 消息完整性验证和防篡改
- 去中心化的密钥管理
- 离线消息缓存和同步

## 使用场景
- 智能体之间传递敏感信息需要加密保护
- 构建安全的多智能体协作通信网络
- 需要防止第三方窃听的智能体间通信

## 依赖和前提条件
- AgentMesh 服务部署或接入
- 智能体加密密钥对生成和管理
- 网络连接到 AgentMesh 消息服务

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `examples`
- `pyproject.toml`
- `requirements.txt`
- `src`
- `tests`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

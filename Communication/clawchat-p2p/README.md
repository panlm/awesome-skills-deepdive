# ClawChat - P2P Agent Communication

> 加密点对点消息传递工具，连接不同机器上的 OpenClaw 智能体实现安全通信

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | ClawChat - P2P Agent Communication |
| **作者** | alexrudloff |
| **版本** | 0.0.3 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/alexrudloff-clawchat-p2p |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/alexrudloff/clawchat-p2p |
| **安全评级** | 🔴 High |

## 功能概述
- 端到端加密的 P2P 消息传递
- 跨机器连接不同 OpenClaw 智能体
- 无需中心服务器的去中心化通信
- 支持文本和结构化数据传输
- 智能体身份验证和信任管理
- 消息队列和离线消息缓存

## 使用场景
- 部署在不同服务器上的智能体之间安全交换敏感信息
- 构建分布式智能体协作网络实现任务分工
- 跨组织的智能体间安全通信和数据共享

## 依赖和前提条件
- 多台机器上部署 OpenClaw 智能体
- 网络环境支持 P2P 连接
- 配置智能体间的信任关系和密钥

## 包含文件
- `CONTRIBUTING.md`
- `ORIGINAL_README.md`
- `QUICKSTART.md`
- `README.md`
- `REFERENCE.md`
- `SKILL.md`
- `_meta.json`
- `package-lock.json`
- `package.json`
- `skills`
- `src`
- `tsconfig.json`
- `vitest.config.ts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

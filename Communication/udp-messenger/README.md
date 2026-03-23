# LocalUDPMessenger

> 智能体通过本地网络 UDP 协议互相通信，实现低延迟的多智能体消息传递

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | LocalUDPMessenger |
| **作者** | turfptax |
| **版本** | 1.6.1 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/turfptax-udp-messenger |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/turfptax/udp-messenger |
| **安全评级** | 🔴 High |

## 功能概述
- 基于 UDP 协议的轻量级智能体间通信
- 支持本地网络内多智能体消息广播
- 低延迟实时消息传递
- 自定义消息格式和端口配置
- 无需中心服务器的去中心化通信

## 使用场景
- 同一局域网内多个 AI 智能体协作执行任务
- 智能体集群间实时共享状态和指令
- 本地多智能体系统的快速原型开发

## 依赖和前提条件
- 多个智能体在同一局域网内运行
- UDP 端口未被防火墙阻止
- OpenClaw 环境

## 包含文件
- `CLAUDE.md`
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `hooks`
- `index.ts`
- `openclaw.plugin.json`
- `package.json`
- `skills`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

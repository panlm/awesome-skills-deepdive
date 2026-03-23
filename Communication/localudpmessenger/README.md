# LocalUDPMessenger

> 智能体通过本地网络 UDP 协议进行点对点通信，实现多智能体间消息传递

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | LocalUDPMessenger |
| **作者** | turfptax |
| **版本** | 1.5.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/turfptax-localudpmessenger |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/turfptax/localudpmessenger |
| **安全评级** | 🔴 High |

## 功能概述
- 基于 UDP 协议的局域网智能体间通信
- 支持向指定智能体发送文本消息
- 低延迟的本地网络消息传递
- 无需中心化服务器的去中心化通信
- 支持多智能体协作场景下的消息交换

## 使用场景
- 多台设备上的 OpenClaw 智能体协作完成任务
- 局域网内智能体间传递指令和状态更新
- 分布式 AI 系统中的节点间通信

## 依赖和前提条件
- 多个 OpenClaw 实例运行在同一局域网
- UDP 端口未被防火墙封锁
- 各智能体需配置正确的网络地址

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

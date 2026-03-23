# ClawChat - P2P Agent Communication

> **Encrypted P2P messaging for connecting OpenClaw agents across different machines and networks.**

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | ClawChat - P2P Agent Communication |
| **作者** | alexrudloff |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/alexrudloff-clawchat-p2p |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/alexrudloff/clawchat-p2p |
| **安全评级** | 🔴 High |

## 功能概述
- Multi-Identity Gateway: Run multiple agent identities in a single daemon process - one libp2p node manages all identitie
- Stacks Identity: Uses your Stacks wallet as your identity (principal = `stacks:<address>`)
- End-to-End Encryption: All messages encrypted using Noise protocol
- NAT Traversal: libp2p-based networking with automatic hole punching and relay support
- Mesh Networking: Gateways automatically discover each other through PX-1 peer exchange
- Per-Identity ACL: Control which peers can connect to each identity
- Nicknames: Optional display names for easier identification
- Background Daemon: Persistent message queue with automatic retry (launchd plist included for macOS)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- macOS

## 包含文件
- `CONTRIBUTING.md`
- `ORIGINAL_README.md`
- `QUICKSTART.md`
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
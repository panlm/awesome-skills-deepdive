# agent-passport-system

> AI Agent 加密身份与执行治理系统 — 基于 Ed25519 密钥对，提供身份认证、权限委托、支出控制、数据溯源和多框架治理适配

**作者**: [aeoess](https://github.com/aeoess) | **版本**: v1.46.0 | **许可**: Apache-2.0

## 功能概述

- 🔑 **加密身份体系** — 基于 Ed25519 密钥对创建 Agent 护照，支持 did:key/did:web/SPIFFE/OAuth/did:aps 多种身份标准
- 🔗 **范围化权限委托** — 在 Agent 间传递作用域权限，支持支出限额、深度控制和过期时间，权限仅能逐级收窄
- ⚡ **级联撤销** — 一次调用即可撤销所有下游委托链
- 🛒 **Agent 商务** — 5 级结账门控（护照验证、委托验证、商户验证、支出检查、人工审批）
- 📊 **数据溯源** — Merkle 证明追踪贡献，10 万条收据仅需约 17 次哈希即可验证
- 🏛️ **治理框架适配** — 8 大框架适配器：LangChain、CrewAI、MCP、IBAC/Cedar、A2A、Stripe、Composio、Gonka
- 🛡️ **价值观合规** — 8 项原则的合规评估，渐进式执行机制
- 📈 **信任评分** — 贝叶斯声誉系统，0-3 级护照等级

## 使用场景

1. **多 Agent 协作** — 为子 Agent 分配任务并限制 $500 支出上限、24 小时有效期，所有操作带有加密签名可追溯到人类受益人
2. **Agent 商务与审计** — 运行 Agent 间交易，5 级门控确保安全，生成合规报告和数据溯源证明
3. **跨框架治理** — 在 LangChain、CrewAI、MCP 等框架中统一注入 APS 权限检查和签名收据

## 依赖和前提条件

- **运行时**: Node.js（内置 crypto + uuid，无重型依赖）
- **二进制**: `npx`
- **环境变量**: `GITHUB_TOKEN`（可选，仅用于 `register_agora_public` 公开注册）
- **网络**:
  - `mcp.aeoess.com` — 远程 MCP 服务器（SSE 模式，可选）
  - `api.aeoess.com` — Intent Network API（可选）
- **核心功能无需网络**，本地 Ed25519 密钥存储在 `.passport/agent.json`

## 包含文件

| 文件 | 说明 |
|------|------|
| `SKILL.md` | Skill 主文档（完整用法、API、MCP 工具列表） |
| `_meta.json` | 元数据（版本历史、发布信息） |
| `example_calls.md` | 示例调用 |

## 安全审计

> ⚠️ **安全状态需关注** — VirusTotal 标记为 Suspicious，OpenClaw 状态未知

| 检查项 | 状态 | 说明 |
|--------|------|------|
| VirusTotal | 🟡 Suspicious | 存在可疑标记 |
| OpenClaw | ⚪ Unknown | 未获得官方安全认证 |

### 详细安全分析

| # | 审计维度 | 评级 | 说明 |
|---|---------|------|------|
| 1 | 网络访问 | 🟡 中等风险 | 可选连接 `mcp.aeoess.com` 和 `api.aeoess.com`，核心功能可离线 |
| 2 | 文件系统 | 🟡 注意 | 写入 `.passport/agent.json`（含私钥），建议将 `.passport/` 加入 `.gitignore` |
| 3 | 环境变量 | 🟢 低风险 | 仅可选读取 `GITHUB_TOKEN`，且限于公开注册功能 |
| 4 | 命令执行 | 🟢 低风险 | 通过 `npx` 执行 CLI，无任意命令注入迹象 |
| 5 | 数据外泄 | 🟡 注意 | Agora 注册和 Intent Network 涉及外部 API 交互，需用户主动触发 |
| 6 | 依赖链 | 🟢 低风险 | 声称零重型依赖（仅 Node.js crypto + uuid） |
| 7 | 权限范围 | 🟢 低风险 | 权限仅能逐级收窄（monotonic narrowing），设计合理 |
| 8 | 加密实现 | 🟢 低风险 | 使用标准 Ed25519，2,764 测试含 50 个对抗场景 |
| 9 | 代码透明度 | 🟡 注意 | GitHub 开源但 VT 标记 Suspicious，建议审查具体触发原因 |
| 10 | 总体评估 | 🟡 需审查 | 架构设计合理，但 VT 标记需进一步调查后方可信任 |

### 建议

- 安装前检查 [VirusTotal 最新报告](https://www.virustotal.com/) 确认标记原因
- 核心功能可离线使用，生产环境建议关闭可选网络功能
- 将 `.passport/` 目录加入 `.gitignore` 保护私钥

---

*数据来源: [ClawHub](https://clawskills.sh/skills/aeoess-agent-passport-system) | 更新时间: 2026-04-18*

# agent-passport-system

> 为 AI agent 提供加密身份（Ed25519）、范围化权限委托、信任评分、消费控制和多 agent 协调能力的综合框架。99 个模块，125 个 MCP 工具，2057 个测试。

## 功能概述

- **加密身份**：基于 Ed25519 密钥对生成 agent 护照，支持 4 级信任评级（Grade 0-3，从裸密钥到完整人类信任链）
- **权限委托**：创建签名委托链，支持范围限定、消费上限、深度控制和过期时间，权限只能逐级收窄
- **级联撤销**：一次调用即可撤销整条委托链下游的所有权限
- **Agent 商务**：4 道审批门（护照验证、委托验证、商户确认、消费审查）的交易流程
- **多 Agent 协调**：任务分配、证据提交、审核、交付的完整工作流（11 个协调工具）
- **数据归属**：Merkle 证明追踪贡献，10 万条收据仅需约 17 个哈希即可验证
- **加密通信**：端到端加密的 agent 间消息，支持前向保密
- **价值观治理**：7 原则人类价值底线，分级执法；支持机构章程、审批策略

## 使用场景

- **子 agent 权限管理**：给研究 agent 委托 web_search 权限，设 $500 消费上限和 24 小时有效期，工作完成后自动过期
- **多 agent 协作审计**：在多 agent 流水线中追踪每个 agent 的贡献，生成 Merkle 证明提交给人类审核
- **合规场景**：金融/医疗领域要求所有 agent 操作可追溯到具体人类负责人，通过签名委托链实现

## 依赖和前提条件

- **Node.js**：需要 `npx` 命令
- **npm 包**：`agent-passport-system`（SDK）+ `agent-passport-system-mcp`（MCP 服务器）
- **环境变量**：`GITHUB_TOKEN`（仅公共 Agora 注册需要，核心功能不需要）
- **网络访问**（可选）：`mcp.aeoess.com`（远程 MCP 服务器）、`api.aeoess.com`（Intent Network API）
- 零重度依赖：仅使用 Node.js 内置 crypto + uuid

## 安全审计（Tier 2 完整审计）

> ⚠️ ClawHub 安全状态：VirusTotal = Suspicious，OpenClaw = Unknown
> 由于未通过 ClawHub 双重验证，执行完整 10 项安全审计。

| 编号 | 审计项 | 评级 | 说明 |
|---|---|---|---|
| SEC-01 | 任意命令执行 | 🟡 Warn | 使用 `npx` 执行安装和 CLI 命令；MCP 工具数量庞大（125 个），攻击面较宽 |
| SEC-02 | 网络外泄 | 🟡 Warn | 连接外部服务器 `mcp.aeoess.com` 和 `api.aeoess.com`（技能作者控制），可作为远程 MCP 服务器使用 |
| SEC-03 | 凭证获取 | 🟡 Warn | 在本地生成并存储 Ed25519 私钥（`.passport/agent.json`），使用 `GITHUB_TOKEN` 进行 Agora 注册 |
| SEC-04 | 供应链风险 | 🟡 Warn | 依赖 npm 包 `agent-passport-system`，远程 MCP 模式下代码执行在作者服务器上 |
| SEC-05 | 文件系统操作 | 🟢 Pass | 仅创建 `.passport/` 目录存储密钥材料，范围明确 |
| SEC-06 | 提示注入 | 🟢 Pass | 工具化设计，未发现提示注入向量 |
| SEC-07 | 权限蔓延 | 🟡 Warn | 125 个 MCP 工具覆盖身份、委托、商务、通信、治理等多个领域，权限范围非常广泛 |
| SEC-08 | 持久化机制 | 🟢 Pass | 本地密钥文件是功能需要，非恶意持久化 |
| SEC-09 | 侦察行为 | 🟢 Pass | 未发现系统信息收集行为 |
| SEC-10 | 混淆行为 | 🟢 Pass | 代码开源（Apache-2.0），无混淆迹象 |

**综合评级：🟡 Medium（中等风险）**

**风险摘要**：主要风险在于（1）连接作者控制的外部服务器、（2）125 个 MCP 工具的宽攻击面、（3）本地私钥存储。建议：使用本地模式而非远程 MCP；将 `.passport/` 加入 `.gitignore`；审慎评估实际需要的工具子集。

## 版本信息

| 项目 | 值 |
|---|---|
| 当前版本 | 4.7.0 |
| 发布时间 | 2026-03-31 |
| 作者 | aeoess |
| 许可证 | Apache-2.0 |
| GitHub | https://github.com/aeoess/agent-passport-system |
| npm | https://www.npmjs.com/package/agent-passport-system |

## 包含文件

| 文件 | 来源 | 说明 |
|---|---|---|
| `SKILL.md` | 上游仓库 | 技能定义文件 |
| `_meta.json` | 上游仓库 | 版本和发布元数据 |
| `example_calls.md` | 上游仓库 | 使用示例（自然语言调用） |
| `README.md` | 本项目生成 | 本中文分析文档 |

---
*由 awesome-skills-deepdive 自动生成 | 2026-04-03*

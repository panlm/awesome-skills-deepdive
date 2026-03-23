# Bitkit Cli

> Bitcoin Lightning payment CLI for agents. Lowest LSP fees. Self-custody wallet with LNURL, typed exit codes, JSON envelope output, encrypted messaging, and daemon mode.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Bitkit Cli |
| **作者** | ovitrif |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/ovitrif-bitkit-cli |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ovitrif/bitkit-cli |
| **安全评级** | 🔴 High |

## 功能概述
- Single static binary -- no daemon, no runtime dependencies
- Optional daemon mode -- keeps node running for instant command execution
- Machine-readable `--json` output on every command
- Mainnet by default, regtest for development
- LNURL-pay, LNURL-withdraw, and Lightning Address support
- Blocktank LSP integration for managed channel opening
- Encrypted seed (AES-256-GCM + Argon2id) or plaintext for automation
- Also available as `bk` (short alias)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `CONTRIBUTING.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `install.sh`
- `rustfmt.toml`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 5 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
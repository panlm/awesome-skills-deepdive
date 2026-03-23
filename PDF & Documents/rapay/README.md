# Ra Pay

> Send compliant fiat USD payments via Ra Pay CLI — the first CLI-native AI payment platform

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Ra Pay |
| **作者** | greendlt224 |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/greendlt224-rapay |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/greendlt224/rapay |
| **安全评级** | 🔴 High |

## 功能概述
- Two-step confirmation — Always preview fees before executing payments
- Business compliance — Built-in validation ensures payments are for legitimate business purposes
- JSON output — Structured responses for AI agents via `--json` flag
- Stripe-backed — All payments processed through Stripe's regulated infrastructure
- Cross-platform — Works on macOS, Linux, and Windows
- Agent-to-agent transaction scripts — Shareable onboarding scripts that a buyer agent can forward to a seller agent (and 

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- macOS

## 包含文件
- `New folder`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，1 项中风险。数据外泄：大量外部数据传输；供应链风险：需要安装外部包且含管道安装

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
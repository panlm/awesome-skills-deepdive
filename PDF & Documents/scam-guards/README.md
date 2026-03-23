# Scam Guards

> **Real-time AI agent security guardian for OpenClaw.**

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Scam Guards |
| **作者** | y01026350884-cyber |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/y01026350884-cyber-scam-guards |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/y01026350884-cyber/scam-guards |
| **安全评级** | 🟢 Low |

## 功能概述
- Skill Scanner: `scripts/scan_skill.py` - Detects 341+ malicious patterns in ClawHub skills.
- Phishing Detector: `scripts/verify_url.py` - Offline domain and URL reputation verification.
- Wallet Checker: `scripts/check_wallet.py` - Validates crypto addresses against confirmed blacklists.
- Behavior Monitor: `scripts/monitor_agent.py` - Real-time PHI analysis for manipulation tactics.
- Evidence Chain: `scripts/evidence_chain.py` - SHA-256 linked audit trails for security incidents.
- Report Generator: `scripts/report_generator.py` - Structured Markdown security summaries.

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `CHANGELOG.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`
- `test_scenarios`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
# Pincer

> Security-first wrapper for installing agent skills. Scans for malware, prompt injection, and suspicious patterns before installation. Use instead of `clawhub install` for safer skill management.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Pincer |
| **作者** | panzacoder |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/panzacoder-pincer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/panzacoder/pincer |
| **安全评级** | 🔴 High |

## 功能概述
- Pre-install scanning — Analyze skills before they touch your system
- mcp-scan integration — Leverages [Invariant Labs' mcp-scan](https://github.com/invariantlabs-ai/mcp-scan) for prompt inj
- Pattern detection — Base64 payloads, `curl | sh`, quarantine removal, and more
- Publisher trust — Maintain lists of trusted and blocked publishers
- Audit mode — Quick-scan all installed skills
- JSON output — Scriptable for CI/CD integration
- Install logging — Track what you've installed and when

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- macOS
- Homebrew

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，5 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
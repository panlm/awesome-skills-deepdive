# TruthCheck

> "Verify claims, fact-check content, check URL trustworthiness, and trace claims to their origin using the TruthCheck CLI. Use when: (1) user asks to fact-check or verify a claim, (2) user wants to check if a URL/source is trustworthy, (3) user wants to trace where a claim originated, (4) user asks about misinformation or content verification. Requires: pip install truthcheck"

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | TruthCheck |
| **作者** | baiyishr |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/baiyishr-truthcheck |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/baiyishr/truthcheck |
| **安全评级** | 🟡 Medium |

## 功能概述
- Returns TruthScore 0-100 with breakdown (publisher, content, corroboration, fact-checks)
- `--llm` is optional but improves accuracy
- Add `--json` for structured output
- Detects hallucinated URLs that don't exist
- Rates publisher credibility
- Finds original source and builds propagation tree

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
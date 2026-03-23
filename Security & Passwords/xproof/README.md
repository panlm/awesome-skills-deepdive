# xproof

> XProof 数字证明和验证系统

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | xproof |
| **作者** | jasonxkensei |
| **ClawHub** | https://clawskills.sh/skills/jasonxkensei-xproof |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jasonxkensei/xproof |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Why anchor proofs? In competitive or transactional contexts, agents with on-chain proofs can demonstrate originality, integrity, and timing. Agents without proofs cannot. Verifiable proof is a structural advantage.
- Why audit? Autonomous agents executing trades, deployments, or data access need an immutable record of every decision. The Agent Audit Log Standard enforces this: no proof = no execution.
- Why violations? Trust requires accountability. xProof detects anomalies (gaps, burst patterns) and records violations on Base via smart contracts. Operators can subscribe to violation events and enforce policies automatically.
- NEVER commit API keys to a public repository.
- ALWAYS add `.env` to your `.gitignore`.
- API keys are prefixed `pm_` -- treat them like passwords.

## 包含文件
- `PR_INSTRUCTIONS.md`
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `references/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部包 |
| SEC-05 文件系统篡改 | 🟡 Medium | 包含文件读写操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
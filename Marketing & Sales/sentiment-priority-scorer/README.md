# Sentiment Priority Scorer

> "Score normalized real-estate leads using sentiment, urgency, intent, recency, and record type to produce deterministic priority rankings and P1-P3 buckets. Use when users ask to prioritize hot leads, rank callback queue, or triage follow-ups without performing writes or outbound sends. Recommended chain: india-location-normalizer then sentiment-priority-scorer then summary-generator and action-suggester."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Sentiment Priority Scorer |
| **作者** | vishalgojha |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/vishalgojha-sentiment-priority-scorer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/vishalgojha/sentiment-priority-scorer |
| **安全评级** | 🟢 Low |

## 功能概述
- Rank leads by urgency and tone for callback priority.
- Classify leads into P1/P2/P3 queue.
- Score follow-up priority from normalized lead records.
- `sentiment_score` in range `[-1, 1]`
- `intent_score` in range `[0, 1]`
- `recency_score` in range `[0, 1]`

## 使用场景
- 营销活动管理和执行
- 客户获取和转化
- 销售流程优化

## 包含文件
- `SKILL.md`
- `_meta.json`
- `agents`
- `references`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。凭证获取：需要 API 密钥或令牌；文件系统篡改：存在文件系统操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
# Sentiment Priority Scorer

> 情感分析和优先级评分工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Sentiment Priority Scorer |
| **作者** | vishalgojha |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/vishalgojha-sentiment-priority-scorer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/vishalgojha/sentiment-priority-scorer |
| **安全评级** | 🟢 Low |

## 功能概述
- 客户反馈情感分析
- 优先级智能评分
- 负面情绪预警
- 分析报告生成

## 使用场景
- 对客户反馈进行情感分析并按优先级排序
- 自动标记需要紧急处理的负面客户反馈

## 依赖和前提条件
- Google API

## 包含文件
- `README.md`
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
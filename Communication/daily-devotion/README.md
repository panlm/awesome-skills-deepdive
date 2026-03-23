# Daily Devotion

> 创建个性化每日灵修内容，包含每日经文选读、牧师寄语和祷告指南

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Daily Devotion |
| **作者** | enjuguna |
| **版本** | 1.1.1 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/enjuguna-daily-devotion |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/enjuguna/daily-devotion |
| **安全评级** | 🔴 High |

## 功能概述
- 每日自动选取适合的圣经经文
- 生成个性化牧师寄语和灵修反思
- 提供祷告指南和祷告词
- 支持按主题或书卷系列阅读
- 灵修日记记录功能
- 支持多种圣经译本

## 使用场景
- 基督徒每日灵修和经文学习
- 教会团契的每日灵修分享
- 个人信仰成长和祷告生活

## 依赖和前提条件
- OpenClaw 环境已配置

## 包含文件
- `README.md`
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

**综合评级: 🔴 High**
**风险摘要:** 存在 1 项高风险，2 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

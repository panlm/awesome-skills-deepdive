# Ultimate Flashcards / Podcasts Tutor

> 播客和闪卡学习工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Ultimate Flashcards / Podcasts Tutor |
| **作者** | drgeld |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/drgeld-flashcards-podcasts-master |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/drgeld/flashcards-podcasts-master |
| **安全评级** | 🟡 Medium |

## 功能概述
- **EchoDecks** is the ultimate AI-powered, audio-first active recall system
- Transform your knowledge into intelligent flashcards and listen to them as personalized podcasts
- Built for high-stakes learning (Cardiology, Software Engineering, Health Informatics), EchoDecks turns dead time into study time

## 使用场景
- 从播客内容生成学习闪卡
- 管理播客订阅和学习笔记
- 组织和复习知识点

## 依赖和前提条件
- API Key

## 包含文件
- `API_DOCS.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

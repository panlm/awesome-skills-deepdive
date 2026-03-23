# lifepath

> AI 人生模拟器 - 逐年体验无限人生

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | lifepath |
| **作者** | ezbreadsniper |
| **ClawHub** | https://clawskills.sh/skills/ezbreadsniper-lifepath |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ezbreadsniper/lifepath |
| **安全评级** | 🟡 Medium |

## 功能概述
- AI 驱动的人生叙事模拟游戏
- 25 个国家，1900-2025 年时代
- 多人交叉人生、王朝模式、每周挑战
- 四种游戏模式（普通/黑暗/喜剧/悲剧）
- Telegram 机器人集成
- Moltbook 社交分享集成
- Gemini AI 生成故事 + Banana.dev 图像生成

## 使用场景
- 通过 Telegram 私信进行人生模拟游戏
- 将完成的人生故事分享到 Moltbook 社区

## 依赖和前提条件
- Node.js 20+、PostgreSQL 14+
- GEMINI_API_KEY、DATABASE_URL
- 可选：Telegram Bot Token、Banana.dev API Key

## 包含文件
- `SKILL.md` — 技能定义
- `src/server.js` — Fastify API 服务器
- `src/routes/` — API 路由（life/moltbook/payment）
- `src/services/` — 核心服务（故事生成/模拟/多人/王朝等）
- `migrations/` — PostgreSQL 数据库迁移
- `scripts/` — 初始化和发布脚本
- `package.json` — Node.js 依赖

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | Node.js 服务，无直接 shell 执行 |
| SEC-02 数据外泄 | 🟡 Medium | 调用 Gemini API、Banana.dev、Telegram API、Moltbook API |
| SEC-03 凭证获取 | 🟡 Medium | 需要多个 API Key（Gemini、Telegram、Banana.dev） |
| SEC-04 供应链风险 | 🟡 Medium | npm 依赖包（Fastify 等） |
| SEC-05 文件系统篡改 | 🟢 Safe | 数据存储在 PostgreSQL 中 |
| SEC-06 Prompt 注入 | 🟡 Medium | 用户输入国家/年份等参数传递给 Gemini AI 生成故事 |
| SEC-07 越权操作 | 🟢 Safe | 在 API 范围内操作 |
| SEC-08 持久化机制 | 🟡 Medium | 运行 Fastify 服务器，需要 PostgreSQL 数据库 |
| SEC-09 信息采集 | 🟢 Safe | 不采集系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 源码开放可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 完整 Web 应用，涉及多个第三方 API 调用和数据库持久化，但功能明确

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

# Nova Letters

> Write reflective letters to your future self. Capture what matters across sessions.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Nova Letters |
| **作者** | cryptocana |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawskills.sh/skills/cryptocana-nova-letters |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/cryptocana/nova-letters |
| **安全评级** | 🟢 Low |

## 功能概述
- Not a log (logs are facts; letters are meaning)
- Not a task list (tasks are what to do; letters are what you learned)
- Not a status report (status is data; letters are insight)
- Store: `~/.openclaw/workspace/letters/` (auto-created)
- Format: Markdown (YYYY-MM-DD.md per day)
- Timezone: America/New_York (configurable via NODE_TZ)

## 使用场景
- 管理个人笔记和知识
- 自动化信息整理
- 构建个人知识管理系统

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `nova-letters.js`
- `package.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。凭证获取：需要 API 密钥或令牌；供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
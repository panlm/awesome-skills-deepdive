# Agent Selfie

> AI agent self-portrait generator. Create avatars, profile pictures, and visual identity using Gemini image generation. Supports mood-based generation, seasonal themes, and automatic style evolution.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agent Selfie |
| **作者** | iisweetheartii |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/iisweetheartii-agent-selfie |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/iisweetheartii/agent-selfie |
| **安全评级** | 🔴 High |

## 功能概述
- Personality-driven — Define your agent's visual identity with name, style, and vibe
- Mood presets — happy, focused, creative, chill, excited, sleepy, professional, celebration
- Theme presets — spring, summer, autumn, winter, halloween, christmas, newyear, valentine
- Format options — avatar (1:1), banner (16:9), full body (9:16)
- Batch generation — Generate multiple selfies at once with HTML gallery
- Zero dependencies — Pure Python stdlib, no pip install needed

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- Python / pip
- API Key

## 包含文件
- `HEARTBEAT.md`
- `INSTALL.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `package.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🔴 High | 存在代码混淆或编码 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
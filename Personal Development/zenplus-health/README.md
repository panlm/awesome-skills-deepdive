# Zen+ Health

> ZenPlus 全方位健康管理 — 心理健康、运动和营养整合

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Zen+ Health |
| **作者** | ollieparsley |
| **ClawHub** | https://clawskills.sh/skills/ollieparsley-zenplus-health |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ollieparsley/zenplus-health |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- 📬 Notifications: Get your latest wellness notifications and reminders
- 📅 Timeline: View your activity history and progress tracking
- 📚 Catalogue: Browse available wellness tasks and activities
- 👤 Profile: Access your user profile and preferences
- "Show my Zen+ notifications"
- "What's on my Zen+ timeline?"

## 依赖和前提条件
- 📖 [API Documentation](https://zenplus.health/api/docs)
- 🔐 [Manage API Keys](https://zenplus.health/settings/api-keys)
- 💬 [Support](https://zenplus.health/support)

## 包含文件
- `ORIGINAL_README.md` — 原始说明文档
- `README.md` — 中文说明文档
- `SECURITY.md`
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API Key/Token |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
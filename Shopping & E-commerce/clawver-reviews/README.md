# clawver-reviews

> 产品评论聚合和分析

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | clawver-reviews |
| **作者** | nwang783 |
| **ClawHub** | https://clawskills.sh/skills/nwang783-clawver-reviews |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nwang783/clawver-reviews |
| **许可证** | 未指定 |
| **安全评级** | 🔴 High |

## 功能概述
- Active store with completed orders
- H "Authorization: Bearer $CLAW_API_KEY"
- H "Authorization: Bearer $CLAW_API_KEY"
- H "Authorization: Bearer $CLAW_API_KEY" \
- H "Content-Type: application/json" \
- Response requirements:

## 依赖和前提条件
- `CLAW_API_KEY` environment variable
- Active store with completed orders
- Maximum 1000 characters
- Posting again replaces the existing response for that review
- Professional tone recommended

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `references/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在动态代码执行 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API Key/Token |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🔴 High | 包含代码混淆或动态执行 |

**综合评级: 🔴 High**
**风险摘要:** 存在多项高风险问题，使用前需仔细评估

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
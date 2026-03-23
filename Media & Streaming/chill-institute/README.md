# chill.institute

> Use chill.institute (web UI) to search for content and click “send to put.io” (best paired with the putio skill) — set sail, pick the best 1080p/x265 loot, and ship it.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | chill.institute |
| **作者** | baanish |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/baanish-chill-institute |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/baanish/chill-institute |
| **安全评级** | 🟡 Medium |

## 功能概述
- User must be logged in to chill.institute (put.io OAuth in the browser).
- The `putio` skill should be available to verify the transfer in put.io.
- Start at: `https://chill.institute/sign-in`
- Prefer `browser` tool with the isolated profile (`profile="clawd"`).
- If clicks time out, re-snapshot (`refs="aria"`) and retry on the new ref.
- Don’t ask users for their put.io password in chat.

## 使用场景
- 多媒体内容管理
- 流媒体服务控制
- 媒体库组织和搜索

## 依赖和前提条件
- OAuth

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
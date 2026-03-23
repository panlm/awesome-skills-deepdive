# Flomo Notes

> Save notes to Flomo via the Flomo inbox webhook. Use when the user says "save to flomo", "记录到 flomo", "flomo note", or asks to store a note in flomo.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Flomo Notes |
| **作者** | xiaoluoboding |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawskills.sh/skills/xiaoluoboding-flomo-notes |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/xiaoluoboding/flomo-notes |
| **安全评级** | 🟡 Medium |

## 功能概述
- “save to flomo: …”
- “记录到 flomo：…”
- “把这段保存到 flomo”

## 使用场景
- 管理个人笔记和知识
- 自动化信息整理
- 构建个人知识管理系统

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；信息采集：大量系统信息采集

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
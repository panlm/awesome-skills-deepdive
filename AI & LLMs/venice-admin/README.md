# Venice Admin

> Venice AI account administration - check balance, view usage history, and manage API keys. Requires an Admin API key.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Venice Admin |
| **作者** | sabrinaaquino |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/sabrinaaquino-venice-admin |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/sabrinaaquino/venice-admin |
| **安全评级** | 🔴 High |

## 功能概述
- Whether you can consume (has balance)
- Current consumption currency (DIEM or USD)
- DIEM balance and epoch allocation
- `--currency`: Filter by currency: `DIEM`, `USD`, `VCU` (default: `DIEM`)
- `--start-date`: Start date filter (ISO format: `2024-01-01`)
- `--end-date`: End date filter (ISO format: `2024-12-31`)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
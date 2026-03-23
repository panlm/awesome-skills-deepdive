# Quickbooks-Agent

> >

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Quickbooks-Agent |
| **作者** | paulbudveit |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawskills.sh/skills/paulbudveit-quickbooks-online |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/paulbudveit/quickbooks-online |
| **安全评级** | 🔴 High |

## 功能概述
- docker compose
- QB_CLIENT_SECRET
- QB_ENVIRONMENT
- run: "git clone https://github.com/claw4business/quickbooks-online-cli.git ~/skills/qb-cli"
- run: "cp ~/skills/qb-cli/.env.example ~/skills/qb-cli/.env"
- run: "docker compose -f ~/skills/qb-cli/docker-compose.yml build"

## 使用场景
- 管理个人笔记和知识
- 自动化信息整理
- 构建个人知识管理系统

## 依赖和前提条件
- Docker
- macOS
- OAuth

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 4 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
# check charger availbility

> Check EV charger availability (favorites, nearby search) via Google Places.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | check charger availbility |
| **作者** | borahm |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/borahm-charger |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/borahm/charger |
| **安全评级** | 🟡 Medium |

## 功能概述
- GOOGLE_PLACES_API_KEY
- Node.js 18+ (Clawdbot already has Node)
- `GOOGLE_PLACES_API_KEY` (recommended in `~/.clawdbot/.env`)
- Put the CLI on your PATH (example):
- `ln -sf "$(pwd)"/bin/charger /home/claw/clawd/bin/charger`
- Add a favorite:

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 5 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；文件系统篡改：存在文件系统操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
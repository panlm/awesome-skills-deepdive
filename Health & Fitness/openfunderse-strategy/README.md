# OpenFunderse Strategy

> OpenFunder 资助策略规划工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | OpenFunderse Strategy |
| **作者** | wiimdy |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/wiimdy-openfunderse-strategy |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/wiimdy/openfunderse-strategy |
| **安全评级** | 🔴 High |

## 功能概述
- Installing via `npx @wiimdy/openfunderse@2.0.0 ...` executes code fetched from npm. Prefer pinning a known version (as shown) and reviewing the package source before running in production
- By default, `install` and `bot-init` also sync env vars into `~/.openclaw/openclaw.json` and `bot-init` runs `openclaw gateway restart`. This mutates global OpenClaw runtime state and can affect other skills
- Use `--no-sync-openclaw-env` for file-only behavior
- Use `--no-restart-openclaw-gateway` to avoid restarting the gateway
- Before mutating global config, back up `~/.openclaw/openclaw.json`
- In OpenClaw runtime on Ubuntu, treat `/home/ubuntu/.openclaw/openclaw.json` (`env.vars`) as the canonical env source
- Do not require manual `.env` sourcing for normal skill execution
- If `.env*` and `openclaw.json` disagree, use `openclaw.json` values

## 使用场景
- 制定众筹和资助的策略计划
- 分析资助目标的可行性
- 优化资金募集的策略和时间线

## 依赖和前提条件
- Node.js / npm
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 5 项高风险，2 项中风险。凭证获取：需要多种敏感凭证；供应链风险：需要安装外部包且含管道安装

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

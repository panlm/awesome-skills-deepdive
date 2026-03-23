# Kiro X Publisher

> Discover hot topics on X, enrich tweets one-by-one, score and summarize signals, generate one tweet draft, and optionally publish on schedule.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Kiro X Publisher |
| **作者** | vmining |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/vmining-kiro-x-publisher |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/vmining/kiro-x-publisher |
| **安全评级** | 🟡 Medium |

## 功能概述
- `scripts/x_hot_pipeline.py`
- `examples/cron_command.txt`
- `X_BEARER_TOKEN` (recommended)
- `X_API_SECRET`
- `X_ACCESS_TOKEN`
- `X_ACCESS_TOKEN_SECRET`

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip
- API Key
- OAuth

## 包含文件
- `SKILL.md`
- `_meta.json`
- `examples`
- `scripts`

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
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
# Gumroad Analytics

> Pull daily Gumroad product/sales analytics safely (no raw PII persistence by default).

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Gumroad Analytics |
| **作者** | vladchatware |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/vladchatware-gumroad-analytics |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/vladchatware/gumroad-analytics |
| **安全评级** | 🟡 Medium |

## 功能概述
- Quick stats — See all products and top performers
- Daily logging — Automatic metrics snapshots for trend analysis
- Sales export — Filter by date or product
- No jq dependency — Works with basic shell tools

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `package.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
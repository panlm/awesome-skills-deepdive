# Ryot

> Complete Ryot media tracker with progress tracking, reviews, collections, analytics, calendar, and automated daily/weekly reports. Track TV shows, movies, books, anime, games with full GraphQL API integration.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Ryot |
| **作者** | f-liva |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/f-liva-ryot |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/f-liva/ryot |
| **安全评级** | 🟡 Medium |

## 功能概述
- name: RYOT_CONFIG
- ✅ Set up daily upcoming episodes notification (07:30)
- ✅ Set up weekly stats report (Monday 08:00)
- ✅ Set up daily recent activity (20:00)
- ✅ Configure WhatsApp delivery
- Catching up on a series you've already watched elsewhere

## 使用场景
- 营销活动管理和执行
- 客户获取和转化
- 销售流程优化

## 依赖和前提条件
- Node.js / npm
- Python / pip
- API Key

## 包含文件
- `CHANGELOG.md`
- `PUBLISHING.md`
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
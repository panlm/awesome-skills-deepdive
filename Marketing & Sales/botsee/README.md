# BotSee

> Monitor your brand's AI visibility via BotSee API

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | BotSee |
| **作者** | grahac |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/grahac-botsee |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/grahac/botsee |
| **安全评级** | 🟡 Medium |

## 功能概述
- Find competitors as AI search engines see them
- Measure share of voice vs competitors
- Identify which sources AI cites for your category
- Uncover exact search queries AI runs for your space
- Generate AI-optimized content from analysis data
- Track visibility over time with historical analysis

## 使用场景
- 营销活动管理和执行
- 客户获取和转化
- 销售流程优化

## 依赖和前提条件
- Python / pip
- macOS
- API Key

## 包含文件
- `CHANGELOG.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`
- `skills`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
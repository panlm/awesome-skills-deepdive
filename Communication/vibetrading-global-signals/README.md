# vibetrading-global-signals

> 查询 vibetrading-datahub 的 AI 生成全球交易信号，获取市场趋势研判

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | vibetrading-global-signals |
| **作者** | liuhaonan00 |
| **版本** | 1.0.1 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/liuhaonan00-vibetrading-global-signals |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/liuhaonan00/vibetrading-global-signals |
| **安全评级** | 🔴 High |

## 功能概述
- 获取 AI 生成的全球市场交易信号
- 覆盖多个市场和资产类别
- 信号包含方向、强度和置信度评分
- 支持按市场、时间框架筛选信号
- 实时更新的市场趋势分析

## 使用场景
- 交易者获取 AI 辅助的市场信号作为决策参考
- 量化策略开发中集成外部 AI 信号源
- 每日快速浏览全球市场 AI 研判概览

## 依赖和前提条件
- vibetrading-datahub API 访问权限
- 基本的金融市场知识

## 包含文件
- `CHANGELOG.md`
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `package-lock.json`
- `package.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

# dellight-cfo-financial-ops

> AI CFO 财务运营助手，支持预算管理、财务报表和资金规划

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | dellight-cfo-financial-ops |
| **作者** | arthurelgindell |
| **ClawHub** | https://clawskills.sh/skills/arthurelgindell-dellight-cfo-financial-ops |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/arthurelgindell/dellight-cfo-financial-ops |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Finance exists to enable revenue growth while maintaining runway.
- Entity: DELLIGHT.AI (DIFC AI License application submitted Jan 30)
- Capital: AED 1.8M liquid funds available (~$490K USD)
- Stage: Pre-revenue startup
- Burn priority: Revenue-generating activities first
- Total Burn, Items=, Monthly Estimate=$2,000-5,400/month

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `scripts/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟡 Medium | 包含持久化配置 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
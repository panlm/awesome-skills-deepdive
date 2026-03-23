# Karma Book

> 客户信誉和积分管理工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Karma Book |
| **作者** | xb1g |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/xb1g-karma-book |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/xb1g/karma-book |
| **安全评级** | 🟢 Low |

## 功能概述
- 客户信誉评分管理
- 积分系统管理
- 行为追踪和记录
- 信誉报告生成

## 使用场景
- 管理客户信誉评分和积分奖励体系
- 追踪用户行为并生成信誉分析报告

## 依赖和前提条件
- API 密钥
- GitHub API
- Webhook 配置

## 包含文件
- `README.md`
- `_meta.json`
- `heartbeat.md`
- `rules.md`
- `skill.json`
- `skill.md`
- `wallet.md`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 未发现明显安全风险，文档透明可审计

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
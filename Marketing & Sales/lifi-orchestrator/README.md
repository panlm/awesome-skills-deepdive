# LI.FI Orchestrator

> LI.FI 跨链交易编排工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | LI.FI Orchestrator |
| **作者** | rhlsthrm |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/rhlsthrm-lifi-orchestrator |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rhlsthrm/lifi-orchestrator |
| **安全评级** | 🟡 Medium |

## 功能概述
- 跨链桥接和交换编排
- 最优路径计算
- 交易执行和监控
- 多链支持

## 使用场景
- 编排跨链资产转移的最优路径
- 监控和管理跨链交易的执行状态

## 依赖和前提条件
- API 密钥
- Python 运行环境

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

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
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
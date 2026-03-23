# NEAR Agent Skills

> NEAR 生态 Agent 技能集合

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | NEAR Agent Skills |
| **作者** | mastrophot |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/mastrophot-near-agent-skills |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mastrophot/near-agent-skills |
| **安全评级** | 🟢 Low |

## 功能概述
- NEAR 区块链操作工具
- NEAR 生态集成功能
- 链上数据查询
- NEAR 钱包管理

## 使用场景
- 在 NEAR 区块链生态中使用 Agent 技能
- 管理和操作 NEAR 链上资产和数据

## 依赖和前提条件
- 无特殊依赖

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `molthub.json`
- `package-lock.json`
- `package.json`
- `src`
- `tsconfig.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。凭证获取：需要 API 密钥或令牌；供应链风险：需要安装外部依赖




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
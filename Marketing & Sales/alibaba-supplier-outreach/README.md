# Alibaba Supplier Outreach

> |

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Alibaba Supplier Outreach |
| **作者** | blockchainhb |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/blockchainhb-alibaba-supplier-outreach |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/blockchainhb/alibaba-supplier-outreach |
| **安全评级** | 🟡 Medium |

## 功能概述
- "find suppliers for [product]" / "source [product]"
- "contact suppliers for [product]"
- "check my Alibaba messages" / "any replies?"
- "follow up with [supplier]" / "negotiate with suppliers"
- Chrome open with Alibaba.com, user must be logged in
- `mcp__launchfast__supplier_research` tool available

## 使用场景
- 自动化邮件营销
- 管理外联和跟进
- 个性化营销邮件生成

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
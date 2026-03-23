# Returns Reverse Logistics

> >

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Returns Reverse Logistics |
| **作者** | nocodemf |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/nocodemf-returns-reverse-logistics |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nocodemf/returns-reverse-logistics |
| **安全评级** | 🟡 Medium |

## 功能概述
- Standard return window: Typically 30 days from delivery for most general merchandise. Electronics often 15 days. Perisha
- Condition requirements: Most policies require original packaging, all accessories, and no signs of use beyond reasonable
- Receipt and proof of purchase: POS transaction lookup by credit card, loyalty number, or phone number has largely replac
- Restocking fees: Applied to opened electronics (15%), special-order items (20-25%), and large/bulky items requiring retu
- Cross-channel returns: Buy-online-return-in-store (BORIS) is expected by customers and operationally complex. Online pri
- International returns: Duty drawback eligibility requires proof of re-export within the statutory window (typically 3-5 

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`
- `evals`
- `references`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
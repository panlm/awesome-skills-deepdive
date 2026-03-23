# veryfi-documents-ai

> 使用 AI 分析和处理文档，支持摘要、翻译和信息提取

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | veryfi-documents-ai |
| **作者** | dbirulia |
| **ClawHub** | https://clawskills.sh/skills/dbirulia-documents-ai |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/dbirulia/documents-ai |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Receipt & Invoice Extraction — vendor, line items, totals, tax, payment method, and more
- Bank Statement Parsing — account details, balances, and full transaction history
- Check Processing — payer/receiver info, MICR data, endorsement detection
- Document Classification — identify document type before extraction (15 built-in types + custom)
- Fraud Detection — fraud scoring on receipts, invoices, checks, and bank statements
- 30+ Document Blueprints — passports, driver's licenses, insurance cards, bills of lading, and more via the Any Document endpoint

## 包含文件
- `ORIGINAL_README.md` — 原始说明文档
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `package.json` — 配置/数据文件

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API Key/Token |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部包 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
# LegalDoc AI

> **Version:** 1.0.0

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | LegalDoc AI |
| **作者** | manas-io-ai |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/manas-io-ai-legaldoc-ai |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/manas-io-ai/legaldoc-ai |
| **安全评级** | 🟡 Medium |

## 功能概述
- Solo Practitioners drowning in document review
- Paralegals needing faster contract analysis
- Corporate Counsel managing high-volume contracts
- Litigation Teams processing discovery documents
- M&A Attorneys conducting due diligence
- 🔐 End-to-end encryption (TLS 1.3)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- API Key

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `clawdhub.json`
- `examples`
- `execution`
- `requirements.txt`
- `templates`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
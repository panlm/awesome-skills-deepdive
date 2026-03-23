# Legal Docs FR

> Générateur de documents juridiques français pour freelances/micro-entrepreneurs.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Legal Docs FR |
| **作者** | hugosbl |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/hugosbl-legal-docs-fr |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/hugosbl/legal-docs-fr |
| **安全评级** | 🟢 Low |

## 功能概述
- Paiement : 30 jours, pénalités 3× taux légal, indemnité 40€ (art. D441-5 Code de commerce)
- PI : Cession subordonnée au paiement intégral
- Médiation : Obligatoire depuis 2016 (art. L611-1 Code de la consommation)
- RGPD : Droits des personnes, finalités, durée conservation, contact DPO
- Force majeure : Art. 1218 du Code civil
- HTML avec CSS inline, optimisé pour impression / export PDF

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。Prompt 注入：存在可疑 Prompt 模式

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
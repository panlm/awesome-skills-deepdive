# Lembrete Agua

> Skill de hidratação que lembra o usuário de beber água a cada 2 horas. Registra consumo, calcula meta diária, motiva com dicas de saúde e adapta alertas ao clima de Goiânia.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Lembrete Agua |
| **作者** | pedrohenrique202525 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/pedrohenrique202525-lembrete-agua |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/pedrohenrique202525/lembrete-agua |
| **安全评级** | 🟢 Low |

## 功能概述
- "lembrete de água", "me lembra de beber água", "hidratação", "ativar água"
- "quero beber mais água", "me ajuda a me hidratar"
- 70kg → 2.450ml (~10 copos de 250ml)
- 80kg → 2.800ml (~11 copos)
- 90kg → 3.150ml (~13 copos)
- Acorda às 6h → lembretes: 6h, 8h, 10h, 12h, 14h, 16h, 18h, 20h, 22h

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`

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
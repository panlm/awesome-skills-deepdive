# Jwdiario

> Buscar y obtener el texto diario de la página oficial de los Testigos de Jehová para la Librería Watchtower en español (wol.jw.org/es/). Utiliza web_fetch para acceder al contenido y extraer el texto del día actual. Use cuando se solicite el texto diario de JW o contenido bíblico diario de fuentes JW.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Jwdiario |
| **作者** | djismgaming |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/djismgaming-jwdiario |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/djismgaming/jwdiario |
| **安全评级** | 🟢 Low |

## 功能概述
- "Texto diario de JW"
- "Texto de hoy de JW"
- "Buscar texto del día en JW"
- "Mostrar lectura diaria de JW"
- Siempre usar la versión en español de la página (wol.jw.org/es/).
- No traducir el texto. El contenido debe extraerse directamente de la fuente en español, tal como aparece en la página of

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`
- `main.js`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 存在 1 项高风险，0 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
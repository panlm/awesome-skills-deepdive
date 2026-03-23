# Mvg

> Munich public transport (MVG) CLI and S-Bahn live tracking. Use for departure times, route planning, nearby stations, service alerts, and real-time S-Bahn positions. Trigger when the user mentions MVG, S-Bahn, U-Bahn, Munich transit, departures, connections, Abfahrten, Verbindungen, or specific line names like S8, U3, etc.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Mvg |
| **作者** | lars147 |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/lars147-mvg-cli |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/lars147/mvg-cli |
| **安全评级** | 🟡 Medium |

## 功能概述
- 🚇 Station suchen - Finde Stationen nach Name
- ⏰ Echtzeit-Abfahrten - Aktuelle Abfahrten mit Verspätungsanzeige
- 🗺️ Verbindungssuche - Routen zwischen Stationen
- 📍 Nahbereichssuche - Stationen in der Nähe bestimmter Koordinaten
- ⚠️ Störungsmeldungen - Aktuelle Betriebsstörungen
- 🚊 Linienübersicht - Alle verfügbaren Linien nach Verkehrsmittel

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- Python / pip
- API Key

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `mvg_cli.py`
- `pyproject.toml`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，4 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
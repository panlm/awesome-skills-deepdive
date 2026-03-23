# mt5-httpapi

> 通过 HTTP API 控制 MetaTrader 5 交易平台

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | mt5-httpapi |
| **作者** | psyb0t |
| **ClawHub** | https://clawskills.sh/skills/psyb0t-mt5-httpapi |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/psyb0t/mt5-httpapi |
| **许可证** | 未指定 |
| **安全评级** | 🟢 Low |

## 功能概述
- Verify: `curl $MT5_API_URL/ping` — should return `{"status": "ok"}`. If not, the API isn't up yet (may still be initializing — it retries in the background).
- H 'Content-Type: application/json' \
- d '{"symbol": "EURUSD", "type": "BUY", "volume": 0.1, "sl": 1.08, "tp": 1.10}'
- H 'Content-Type: application/json' \
- d '{"price": 1.09, "sl": 1.07, "tp": 1.11}'
- H 'Content-Type: application/json' \

## 依赖和前提条件
- Verify:** `curl $MT5_API_URL/ping` — should return `{"status": "ok"}`. If not, the API isn't up yet (may still be initializing — it retries in the background).

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `references/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟢 Low**
**风险摘要:** 低风险技能，可安全使用

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
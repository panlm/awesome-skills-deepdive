# stock screener

> Intellectia stock/crypto screener for Bullish/Bearish Tomorrow/Week/Month presets. Calls /gateway/v1/stock/screener-list (no auth) and summarizes results.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | stock screener |
| **作者** | xanxustan |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/xanxustan-ai-screener |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/xanxustan/ai-screener |
| **安全评级** | 🟡 Medium |

## 功能概述
- Get the latest bullish/bearish screener candidates for stocks or crypto
- Use the built-in preset pick-lists (below) as your “stock/crypto picking tools”
- Convert a preset into exact API query parameters (`symbol_type`, `period_type`, `trend_type`)
- Summarize/compare results using `probability`, `profit`, `price`, `change_ratio`, `klines`, and `trend_list`
- Stocks Bullish Tomorrow: This list highlights stocks expected to rise, identified by our AI algorithm. It analyzes marke
- Stocks Bearish Tomorrow: This list highlights stocks expected to fall, identified by our AI algorithm. It analyzes marke

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
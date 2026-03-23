# TradingView Screener

> Screen markets across 6 asset classes using TradingView data. API pre-filters + pandas computed signals. YAML-driven strategies.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | TradingView Screener |
| **作者** | hiehoo |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/hiehoo-tradingview-screener |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/hiehoo/tradingview-screener |
| **安全评级** | 🟡 Medium |

## 功能概述
- [API Guide](references/tvscreener-api-guide.md) - Screener types, filters, field discovery
- [Signals Guide](references/computed-signals-guide.md) - YAML schema, signal type configs
- [Strategy Templates](references/strategy-templates.md) - Pre-built screening strategies
- [Field Presets](references/field-presets.md) - Common field groups per asset class

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `assets`
- `install.sh`
- `references`
- `scripts`
- `state`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。信息采集：大量系统信息采集

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
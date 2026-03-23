# ETH24

> ETH24 以太坊开发和交互工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | ETH24 |
| **作者** | patmilkgallon |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/patmilkgallon-eth24 |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/patmilkgallon/eth24 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Read config.json for topic, brand, voice, and search terms
- Commentary: 1-2 short sentences. Tell the reader why this matters. Don't restate the tweet
- Be accurate. Don't claim "first" or "biggest" unless certain
- No emojis. No emdashes. Use hyphens
- Include only stories that are genuinely important. Fewer is better than filler
- Write "highlights": a comma-separated preview of the day's biggest stories (under 200 chars)

## 使用场景
- 与以太坊网络进行交互和查询
- 开发和测试智能合约
- 监控以太坊交易和链上数据

## 依赖和前提条件
- Node.js / npm
- Python / pip
- API Key

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `card.py`
- `commands`
- `config.json`
- `crawl.py`
- `main.py`
- `package.json`
- `publish.py`
- `rank.py`
- `requirements.txt`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

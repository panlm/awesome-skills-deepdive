# Hong Kong Bus ETA | 香港巴士預計到達時間

> Fast, reliable Hong Kong bus ETA lookup (KMB/CTB/LWB) with fuzzy stop matching, bilingual output (zh-HK/en), and multi-route parallel queries. Built for “next bus” speed, with robust no-result fallback and high-frequency stop handling. Use for queries like next bus / ETA / arrival time at stop. 支援香港九巴/城巴/龍運實時到站、站名容錯、多線同查、尾班車/無班次 fallback，適用「下一班幾時到」「巴士幾時到站」。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Hong Kong Bus ETA | 香港巴士預計到達時間 |
| **作者** | tomfong |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/tomfong-hk-bus-eta |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tomfong/hk-bus-eta |
| **安全评级** | 🟡 Medium |

## 功能概述
- [Main Documentation](../README.md) - Complete user guide with installation, usage examples, and features
- [SKILL.md](./SKILL.md) - Technical specification for AI agents
- [Scripts Directory](./scripts/) - Python scripts for bus ETA queries
- KMB/LWB: `https://data.etabus.gov.hk/v1/transport/kmb/`
- Citybus: `https://rt.data.gov.hk/v2/transport/citybus/`
- Bus Stop Data: `https://data.gov.hk/` (開放數據平台)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip
- 数据库

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
# Portfolio Watcher

> 监控股票和加密货币持仓，获取价格警报，追踪投资组合表现

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Portfolio Watcher |
| **作者** | jhillin8 |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/jhillin8-portfolio-watcher |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jhillin8/portfolio-watcher |
| **安全评级** | 🟢 Low |

## 功能概述
- 实时监控股票和加密货币价格
- 设置价格变动警报和阈值通知
- 追踪投资组合整体收益和表现
- 支持多种资产类型（股票、加密货币）
- 生成持仓分析和收益报告
- 计算投资组合盈亏比例

## 使用场景
- 每日投资组合表现监控与汇报
- 价格异常波动时即时预警
- 定期生成投资收益分析报告

## 依赖和前提条件
- 配置持仓信息和资产列表
- 金融数据 API 密钥（如行情接口）
- 设置价格警报阈值

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

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
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

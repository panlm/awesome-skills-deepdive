# Banana Farmer

> 股票动量扫描器和投资组合智能分析工具，查询 RSI、动量评分等技术指标

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Banana Farmer |
| **作者** | adamandjarvis |
| **版本** | 1.9.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/adamandjarvis-banana-farmer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/adamandjarvis/banana-farmer |
| **安全评级** | 🔴 High |

## 功能概述
- 扫描股票动量信号和趋势
- 计算 RSI（相对强弱指标）
- 动量评分和排名系统
- 投资组合分析和优化建议
- 技术指标综合展示
- 支持自定义扫描条件和过滤器

## 使用场景
- 每日扫描市场寻找高动量股票投资机会
- 监控投资组合中个股的技术指标变化
- 量化策略研究中的动量因子分析

## 依赖和前提条件
- 股票市场数据 API 访问权限
- Banana Farmer 工具配置

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

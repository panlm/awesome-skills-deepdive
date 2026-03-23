# honor

> Picqer 履约仪表板 API，提供 KPI、拣货单、库存和收入的 JSON 数据接口

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | honor |
| **作者** | johnmcgucki |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/johnmcgucki-picqer-fulfillment |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/johnmcgucki/picqer-fulfillment |
| **安全评级** | 🟡 Medium |

## 功能概述
- 提供完整的仪表板数据接口（KPI、拣货单、库存、收入）
- 支持按日期、拣货员、客户筛选数据
- 独立的拣货单、库存、收入查询命令
- JSON 格式输出，适合程序化处理
- API 密钥仅存储在本地 .env 文件中
- 仅通过 Tailscale 访问，增强安全性

## 使用场景
- 通过 AI 智能体自然语言查询仓库履约指标
- 定时抓取拣货和库存数据生成运营报告
- 监控慢速流转库存和收入趋势

## 依赖和前提条件
- Picqer 账户和 API 密钥
- Tailscale 网络配置
- Node.js 运行环境

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive skill 自动生成

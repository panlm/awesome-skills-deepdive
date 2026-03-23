# stock screener

> Intellectia 股票/加密货币筛选器，提供看涨/看跌预设分析

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
- 支持股票和加密货币的看涨/看跌筛选
- 提供多时间维度预设：明日、一周、一月
- 调用 Intellectia API 获取筛选候选列表
- 返回概率、收益率、价格、涨跌幅等关键指标
- 无需认证即可调用 API
- 内置预设名称到 API 参数的映射表

## 使用场景
- 快速获取明日/本周/本月的看涨股票和加密货币候选列表
- 对比不同时间周期的看涨/看跌趋势
- 为投资决策提供量化筛选参考数据

## 依赖和前提条件
- curl 和 python3
- requests 库（`pip install requests`）
- Intellectia API（免认证）

## 安全状态
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
> 本文档由 awesome-skills-deepdive skill 自动生成

# Financial Calculator Pro

> 高级金融计算器，支持终值表、现值、折扣计算、加价定价和复利计算，含 CLI 和交互式 Web 界面

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Financial Calculator Pro |
| **作者** | tarigha |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/tarigha-financial-calculator |

## 功能概述
- 终值（FV）计算：投资增长预测，支持不同复利频率（年/季/月/日）
- 现值（PV）计算：折现未来金额的当前价值
- 折扣计算器：计算折后价格和节省金额
- 加价计算器：根据成本和加价率计算售价和利润率
- 复利明细：有效年利率对比和利息分析
- 终值对比表：跨多个利率和时间段生成比较矩阵
- 交互式 Web UI（基于 Flask），支持 7 种计算器类型和实时计算

## 使用场景
- 做投资决策时对比不同利率和期限下的收益情况
- 制定产品定价策略时快速计算加价率和利润率

## 依赖和前提条件
- Python 3.7+
- Flask（Web UI 需要：`pip install flask`）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。信息采集：大量系统信息采集

---
> 本文档由 awesome-skills-deepdive skill 自动生成

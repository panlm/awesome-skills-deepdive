# Synth Data

> 查询 Synthdata.co 的加密货币、大宗商品和股票波动率预测

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Synth Data |
| **作者** | emsin44 |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/emsin44-synth-data |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/emsin44/synth-data |
| **安全评级** | 🟡 Medium |

## 功能概述
- 获取加密货币的波动率预测数据
- 查询大宗商品价格波动预测
- 获取股票市场波动率分析
- 支持多种时间维度的预测查询

## 使用场景
- 查询比特币未来一周的波动率预测
- 比较不同资产类别的预期波动率

## 依赖和前提条件
- API Key（Synthdata.co）

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

> 本文档由 awesome-skills-deepdive skill 自动生成

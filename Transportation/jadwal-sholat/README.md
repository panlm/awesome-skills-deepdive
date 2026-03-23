# Jadwal Sholat

> 获取印尼各城市的伊斯兰祈祷时刻表（晨礼、晌礼、晡礼、昏礼、宵礼）

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Jadwal Sholat |
| **作者** | banghasan |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/banghasan-jadwal-sholat |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/banghasan/jadwal-sholat |
| **安全评级** | 🟢 Low |

## 功能概述
- 查询印尼各城市/地区的每日祈祷时刻
- 包含所有主要祈祷时间（黎明、日出、晌午、下午、日落、夜晚）
- 支持按城市名称搜索
- 数据来源于印尼宗教事务部

## 使用场景
- 查询雅加达今日的祈祷时刻表
- 获取印尼某城市的完整日祈祷时间

## 依赖和前提条件
- Node.js / npm

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 存在 1 项高风险，0 项中风险。数据外泄：大量外部数据传输

> 本文档由 awesome-skills-deepdive skill 自动生成

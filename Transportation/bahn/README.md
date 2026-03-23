# Deutsche Bahn CLI

> 使用 bahn-cli 工具搜索德国铁路（Deutsche Bahn）列车连接和时刻表

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Deutsche Bahn CLI |
| **作者** | tobiasbischoff |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/tobiasbischoff-bahn |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tobiasbischoff/bahn |
| **安全评级** | 🟢 Low |

## 功能概述
- 搜索德国铁路站点之间的列车连接方案
- 查询指定日期和时间的出发时刻
- 支持 Hbf（中央火车站）等常用站名缩写
- 显示换乘次数、行程时间和票价信息
- 可自定义返回结果数量

## 使用场景
- 查询汉诺威到波恩的下一班列车及换乘方案
- 搜索特定日期从柏林到慕尼黑的下午列车
- 帮助德国旅行规划选择最优火车路线

## 依赖和前提条件
- Node.js / npm

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。供应链风险：需要安装外部依赖

> 本文档由 awesome-skills-deepdive skill 自动生成

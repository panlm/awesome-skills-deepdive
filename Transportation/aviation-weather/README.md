# Aviation Weather

> 从 aviationweather.gov 获取航空气象数据（METAR、TAF、PIREP）

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Aviation Weather |
| **作者** | dimitryvin |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/dimitryvin-aviation-weather |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/dimitryvin/aviation-weather |
| **安全评级** | 🟢 Low |

## 功能概述
- 获取机场实时 METAR 天气报告
- 查询 TAF 航站预报（未来天气预测）
- 获取飞行员气象报告（PIREP）
- 支持 ICAO 机场代码查询
- 解析和格式化航空气象数据

## 使用场景
- 飞行前检查目的地机场的实时天气和能见度
- 查看未来 24 小时的航站天气预报
- 获取航路上的飞行员报告了解实际飞行条件

## 依赖和前提条件
- 无特殊依赖（使用 aviationweather.gov 公开 API）

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

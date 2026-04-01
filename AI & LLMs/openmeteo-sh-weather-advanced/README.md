# Weather via OpenMeteo (via openmeteo-sh cli; advanced ver)

> 高级天气查询工具，支持历史数据（1940年起）、详细气象变量选择和多种天气模型

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Weather via OpenMeteo (via openmeteo-sh cli; advanced ver) |
| **作者** | lstpsche |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/lstpsche-openmeteo-sh-weather-advanced |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/lstpsche/openmeteo-sh-weather-advanced |
| **安全评级** | 🔴 High |

## 功能概述
- 支持从 1940 年至今的历史天气数据查询
- 提供丰富的气象变量选择（气压、露点、雪深、能见度等）
- 支持多种天气模型（ERA5、CERRA、ECMWF IFS 等）
- 精细化预报控制，支持自定义预报参数
- 基于免费 OpenMeteo API，无需付费
- 使用 openmeteo-sh CLI 工具进行查询

## 使用场景
- 查询特定地点的历史天气数据进行气象分析
- 获取专业级气象变量（如露点温度、积雪深度）用于研究
- 对比不同天气模型的预报结果

## 依赖和前提条件
- openmeteo-sh CLI 工具
- bash 环境

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🔴 High | 发现 Prompt 注入特征 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 4 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成

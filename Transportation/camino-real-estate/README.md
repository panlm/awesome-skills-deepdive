# Real Estate Intelligence

> 使用 Camino AI 评估房产地址，获取周边学校、交通和社区信息

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Real Estate Intelligence |
| **作者** | james-southendsolutions |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/james-southendsolutions-camino-real-estate |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/james-southendsolutions/camino-real-estate |
| **安全评级** | 🟡 Medium |

## 功能概述
- 评估指定地址的房产宜居性
- 获取周边学校评级和距离信息
- 查询公共交通可达性和通勤时间
- 了解社区安全指数和生活配套

## 使用场景
- 购房前评估目标地址的周边配套设施
- 比较多个候选住址的通勤便利性和学区质量

## 依赖和前提条件
- API Key（Camino AI）

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

> 本文档由 awesome-skills-deepdive skill 自动生成

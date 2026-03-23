# Capmetro Skill

> 奥斯汀 CapMetro 公共交通查询，获取实时车辆位置、下一班到站时间和服务告警

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Capmetro Skill |
| **作者** | brianleach |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/brianleach-capmetro-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/brianleach/capmetro-skill |
| **安全评级** | 🟡 Medium |

## 功能概述
- 查看公交车实时位置和到站预测
- 获取指定站点的下一班到站时间
- 查看服务告警和延误通知
- 查询路线和时刻表信息

## 使用场景
- 等车时查看下一班公交的预计到站时间
- 查看奥斯汀公交系统的实时服务状态

## 依赖和前提条件
- API Key（CapMetro）

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

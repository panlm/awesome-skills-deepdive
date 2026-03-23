# Travel Agent Skill

> 旅行代理助手——帮助规划和预订旅行

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Travel Agent Skill |
| **作者** | aszelem |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/aszelem-travel-agent |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/aszelem/travel-agent |
| **安全评级** | 🟢 Low |

## 功能概述
- 综合旅行规划和建议
- 航班、酒店和活动的搜索和推荐
- 行程安排和优化
- 旅行预算估算

## 使用场景
- 规划一次完整的欧洲旅行行程
- 根据预算和偏好推荐旅行方案

## 依赖和前提条件
- 无特殊依赖

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。数据外泄：存在外部 API 调用

> 本文档由 awesome-skills-deepdive skill 自动生成

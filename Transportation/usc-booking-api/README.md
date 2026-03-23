# Urban Sports Club Booking API

> USC 预订 API——场地和设施的在线预订管理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Urban Sports Club Booking API |
| **作者** | niklaspriddat |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/niklaspriddat-usc-booking-api |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/niklaspriddat/usc-booking-api |
| **安全评级** | 🟡 Medium |

## 功能概述
- 在线预订场地和设施
- 查看可用时段和容量信息
- 管理预订记录和修改

## 使用场景
- 预订大学运动场地或会议室
- 查看和管理已有的设施预订

## 依赖和前提条件
- API Key / 账号凭证

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。凭证获取：需要多种敏感凭证；信息采集：大量系统信息采集

> 本文档由 awesome-skills-deepdive skill 自动生成

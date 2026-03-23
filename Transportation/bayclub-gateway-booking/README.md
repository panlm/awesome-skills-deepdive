# Check and book Tennis and Pickleball Courts at Bay Club Gateway

> 在 Bay Club 预订和管理网球/匹克球场地

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Check and book Tennis and Pickleball Courts at Bay Club Gateway |
| **作者** | elizabethsiegle |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/elizabethsiegle-bayclub-gateway-booking |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/elizabethsiegle/bayclub-gateway-booking |
| **安全评级** | 🔴 High |

## 功能概述
- 查看 Bay Club 各场馆的场地可用性
- 在线预订网球和匹克球场地
- 管理和取消已有预订
- 查看场地类型、时段和价格信息

## 使用场景
- 预订本周末的网球场地
- 查看附近 Bay Club 的匹克球场空闲时段
- 批量管理个人的场地预订记录

## 依赖和前提条件
- API Key / 账号凭证

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 4 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

> 本文档由 awesome-skills-deepdive skill 自动生成

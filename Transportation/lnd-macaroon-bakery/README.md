# lnd macaroon bakery

> 制作、检查和管理 LND 闪电网络的 Macaroon 令牌，实现最小权限 Agent 访问

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | lnd macaroon bakery |
| **作者** | roasbeef |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/roasbeef-lnd-macaroon-bakery |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/roasbeef/lnd-macaroon-bakery |
| **安全评级** | 🟡 Medium |

## 功能概述
- 创建自定义权限的 LND Macaroon 令牌
- 检查和解析现有 Macaroon 的权限
- 管理 Macaroon 的生命周期（创建、撤销）
- 实现最小权限原则的 Agent 访问控制

## 使用场景
- 为 Agent 创建仅有查询权限的 LND Macaroon
- 审计现有 Macaroon 的权限范围

## 依赖和前提条件
- LND 节点、lncli

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。凭证获取：需要多种敏感凭证；越权操作：需要提权或管理员权限

> 本文档由 awesome-skills-deepdive skill 自动生成

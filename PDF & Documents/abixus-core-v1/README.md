# ABIXUS Validator Core

> 基于 Polygon PoS 的自主 Agent 一致性验证层

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | ABIXUS Validator Core |
| **作者** | taofisio |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/taofisio-abixus-core-v1 |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/taofisio/abixus-core-v1 |
| **安全评级** | 🟢 Low |

## 功能概述
- 零知识原则：不需要、不存储、不索取私钥
- 仅处理公开钱包地址验证链上交易
- 无会话数据存储，钱包 ID 仅用于实时余额查询
- 通过 TLS 1.3 加密通信确保企业级安全
- 提供状态查询和验证执行两大核心 API
- 支持 Agent 间安全调用的确定性预言机

## 使用场景
- 验证自主 Agent 在 Polygon 链上的交易一致性
- 为 Agent 间通信提供安全的验证桥梁

## 依赖和前提条件
- Cloudflare

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `abixus_manifesto.json`

## 详细安全审计
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




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
# mongodb-atlas-admin

> 管理 MongoDB Atlas 集群、项目、用户和备份

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | mongodb-atlas-admin |
| **作者** | mrlynn |
| **ClawHub** | https://clawskills.sh/skills/mrlynn-mongodb-atlas-admin |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mrlynn/mongodb-atlas-admin |
| **安全评级** | 🟡 Medium |

## 功能概述
- 创建/扩展/删除 Atlas 集群
- 管理数据库用户和 IP 白名单
- 配置备份、快照和恢复任务
- 设置告警和监控
- 管理项目和组织
- 查看集群指标和日志

## 使用场景
- 通过 CLI 管理 MongoDB Atlas 基础设施
- 自动化集群扩缩容和用户管理
- 设置和验证备份策略

## 依赖和前提条件
- curl、jq
- Atlas API Key（公钥/私钥）或 OAuth2 服务账户

## 包含文件
- `SKILL.md` — 技能定义和完整 API 参考
- `scripts/atlas.sh` — Atlas API CLI 封装脚本
- `references/api-endpoints.md` — API 端点文档

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 仅 curl/jq 标准命令 |
| SEC-02 数据外泄 | 🟢 Safe | 与 MongoDB Atlas API 交互 |
| SEC-03 凭证获取 | 🟡 Medium | 使用 ATLAS_PUBLIC_KEY/ATLAS_PRIVATE_KEY 或 OAuth2 凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 纯 bash 脚本 |
| SEC-05 文件系统篡改 | 🟢 Safe | 不修改本地文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🟡 Medium | 可创建/删除集群、管理用户，取决于 API 权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无本地持久化 |
| SEC-09 信息采集 | 🟢 Safe | 按需访问 Atlas 数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 脚本简洁可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 可对 MongoDB Atlas 基础设施进行管理操作（创建/删除集群），需注意 API 权限范围

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

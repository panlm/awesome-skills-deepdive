# nocodb

> 通过 REST API 管理自托管 NocoDB 数据库、表和记录

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | nocodb |
| **作者** | nickian |
| **ClawHub** | https://clawskills.sh/skills/nickian-nocodb |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nickian/nocodb |
| **安全评级** | 🟢 Low |

## 功能概述
- 列出数据库（Bases）
- 查看表和列 Schema
- 查询和筛选行数据
- 插入新记录
- 支持名称或 ID 访问
- NocoDB 过滤语法支持

## 使用场景
- 自托管数据库的日常数据管理
- 电子表格式数据库的自动化操作
- 数据查询和批量操作

## 依赖和前提条件
- `NOCODB_URL` 和 `NOCODB_TOKEN` 环境变量
- 自托管 NocoDB 实例

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件 |
| scripts/nocodb.sh | API 调用辅助脚本 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 使用 curl 和 jq，参数处理安全 |
| SEC-02 数据外泄 | 🟢 Safe | 仅与用户指定的 NocoDB 实例通信 |
| SEC-03 凭证获取 | 🟢 Safe | 从环境变量读取 token |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件写入 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟢 Safe | 权限由 NocoDB token 控制 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 仅查询用户自己的数据库 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟢 Low**
**风险摘要:** 安全的自托管数据库 CLI 客户端，代码质量良好

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

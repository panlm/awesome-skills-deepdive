# supabase

> 连接 Supabase 进行数据库操作、向量搜索和存储管理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | supabase |
| **作者** | stopmoclay |
| **ClawHub** | https://clawskills.sh/skills/stopmoclay-supabase |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/stopmoclay/supabase |
| **安全评级** | 🟡 Medium |

## 功能概述
- SQL 查询执行
- CRUD 操作（Insert/Select/Update/Delete）
- pgvector 向量相似度搜索
- 表管理（列出/描述表结构）
- RPC 函数调用
- 丰富的过滤器支持

## 使用场景
- Supabase 项目的日常数据库管理
- 基于嵌入向量的语义搜索
- 应用后端数据操作

## 依赖和前提条件
- `SUPABASE_URL` 和 `SUPABASE_SERVICE_KEY` 环境变量
- 可选：`SUPABASE_ACCESS_TOKEN`

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件 |
| scripts/supabase.sh | 完整 CLI 辅助脚本 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 使用 curl，参数处理安全（set -euo pipefail） |
| SEC-02 数据外泄 | 🟢 Safe | 仅与用户指定的 Supabase 实例通信 |
| SEC-03 凭证获取 | 🟡 Medium | 使用 Service Key（全权限），从环境变量读取 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件写入 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟡 Medium | Service Key 拥有完整数据库权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 仅操作用户自己的数据库 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟡 Medium**
**风险摘要:** 使用 Supabase Service Key 拥有完整数据库权限，需妥善管理凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

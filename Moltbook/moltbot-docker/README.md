# moltbot-docker

> 启用 Bot 管理 Docker 容器、镜像和堆栈

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | moltbot-docker |
| **作者** | mkrdiop |
| **ClawHub** | https://clawskills.sh/skills/mkrdiop-moltbot-docker |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mkrdiop/moltbot-docker |
| **安全评级** | 🟡 Medium |

## 功能概述
- 列出运行中和所有容器
- 启动/停止容器
- 查看容器日志
- Docker 系统统计和清理
- 删除前需确认的安全规则

## 使用场景
- 通过 Agent 管理 Docker 容器
- 排查容器问题

## 依赖和前提条件
- Docker CLI

## 包含文件
- `SKILL.md — Docker 命令指南和安全规则`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 直接指导执行 docker 命令，包括 rm/rmi/prune |
| SEC-02 数据外泄 | 🟢 Safe | Docker 操作仅限本地 |
| SEC-03 凭证获取 | 🟢 Safe | 不涉及凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 依赖系统级 Docker |
| SEC-05 文件系统篡改 | 🟡 Medium | Docker 操作可影响容器卷 |
| SEC-06 Prompt 注入 | 🟡 Medium | 指导 Agent 执行系统命令的模式 |
| SEC-07 越权操作 | 🔴 High | Docker 操作需要较高系统权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟡 Medium | docker inspect 可获取容器配置信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | SKILL.md 简洁透明 |

**综合评级: 🟡 Medium**
**风险摘要:** Docker 管理权限较高，但包含确认安全规则

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

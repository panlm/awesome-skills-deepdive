# Agent Registry

> |

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agent Registry |
| **作者** | matrixy |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/matrixy-agent-registry |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/matrixy/agent-registry |
| **安全评级** | 🔴 High |

## 功能概述
- Token overhead: ~117 tokens per agent x agent count = wasted context
- Scales poorly: 50 agents = 5.8k, 150 agents = 17.5k, 300+ agents = 35k+ tokens
- Context waste: Typically only 1-3 agents are relevant per conversation
- All or nothing: You pay the full cost even if you use zero agents
- Slow startup: Processing hundreds of agent files delays conversation start
- Custom agents: 16.4k tokens (8.2%)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `CLAUDE.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `bin`
- `docs`
- `hooks`
- `install.sh`
- `lib`
- `package-lock.json`
- `package.json`
- `tests`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，5 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
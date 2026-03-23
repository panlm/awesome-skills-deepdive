# agent-builder

> 端到端构建高性能 OpenClaw 代理，生成完整工作空间文件

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | agent-builder |
| **作者** | plgonzalezrx8 |
| **ClawHub** | https://clawskills.sh/skills/plgonzalezrx8-agent-builder |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/plgonzalezrx8/agent-builder |
| **安全评级** | 🟢 Low |

## 功能概述
- 通过访谈确定代理任务和个性
- 自动生成 SOUL.md/IDENTITY.md/AGENTS.md 等工作空间文件
- 内置安全护栏检查清单
- 提供验收测试场景
- 支持迭代改进现有代理
- 包含架构和模板参考文档

## 使用场景
- 从零构建新的 OpenClaw 代理
- 改进现有代理的行为和安全边界
- 为代理配置护栏和自主级别

## 依赖和前提条件
OpenClaw 工作空间环境

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references/architecture.md`
- `references/openclaw-workspace.md`
- `references/templates.md`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 纯 Markdown 模板和指导 |
| SEC-02 数据外泄 | 🟢 Safe | 无网络通信 |
| SEC-03 凭证获取 | 🟢 Safe | 不涉及凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 生成并写入多个工作空间文件 |
| SEC-06 Prompt 注入 | 🟡 Medium | 包含 system prompt 模板，可作为注入参考 |
| SEC-07 越权操作 | 🟢 Safe | 无越权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 仅收集用户主动提供的信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰 |

**综合评级: 🟢 Low**
**风险摘要:** 纯模板生成工具，文件写入限于工作空间目录

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

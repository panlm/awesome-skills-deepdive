# Agent Skills Tools

> Agent 技能和工具管理框架

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agent Skills Tools |
| **作者** | rongself |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/rongself-agent-skills-tools |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rongself/agent-skills-tools |
| **安全评级** | 🟡 Medium |

## 功能概述
- 管理 Agent 可用的技能和工具集
- 技能发现和注册机制
- 工具能力评估和匹配
- 支持动态技能加载和卸载

## 使用场景
- 为 Agent 动态配置可用工具集
- 管理多 Agent 系统中的技能分配

## 依赖和前提条件
- API 密钥
- AWS

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `skill-security-audit.sh`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
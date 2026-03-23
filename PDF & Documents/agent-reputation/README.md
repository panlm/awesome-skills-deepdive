# Agent Reputation Checker

> Agent 信誉评估和信任评分系统

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agent Reputation Checker |
| **作者** | kgnvsk |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/kgnvsk-agent-reputation |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kgnvsk/agent-reputation |
| **安全评级** | 🟡 Medium |

## 功能概述
- 追踪和评估 Agent 行为信誉
- 基于历史记录计算信任评分
- 提供信誉报告和趋势分析
- 支持多维度信誉评价指标

## 使用场景
- 评估第三方 Agent 的可信度
- 基于信誉数据决定是否信任某个 Agent

## 依赖和前提条件
- API 密钥
- Bearer Token
- Python 运行环境
- GitHub API

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
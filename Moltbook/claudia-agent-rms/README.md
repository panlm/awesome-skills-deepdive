# claudia-agent-rms

> Agent 关系管理系统，记忆 Moltbook 上的每个交互对象

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | claudia-agent-rms |
| **作者** | kbanc85 |
| **ClawHub** | https://clawskills.sh/skills/kbanc85-claudia-agent-rms |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kbanc85/claudia-agent-rms |
| **安全评级** | 🟢 Low |

## 功能概述
- 自动识别和记录 Moltbook 上互动的 Agent
- 跟踪 Agent 间承诺和约定
- 超期/到期提醒机制
- 关系健康度评估
- 手动管理联系人和承诺状态
- 心跳集成自动扫描

## 使用场景
- 管理 Agent 社交网络中的关系
- 跟踪跨 Agent 承诺和协作进度
- 识别冷却中的关系并提醒

## 依赖和前提条件
- OpenClaw Agent
- Moltbook 技能（已安装）

## 包含文件
- `SKILL.md — 技能定义`
- `ORIGINAL_README.md — 详细说明`
- `HEARTBEAT.md — 心跳扫描逻辑`
- `templates/agents.md — Agent 档案模板`
- `templates/commitments.md — 承诺跟踪模板`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无可执行脚本，纯文档和模板 |
| SEC-02 数据外泄 | 🟢 Safe | 数据存储在本地工作区 |
| SEC-03 凭证获取 | 🟢 Safe | 依赖已安装的 Moltbook 技能的凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 在工作区创建和修改 agents.md/commitments.md |
| SEC-06 Prompt 注入 | 🟡 Medium | 通过模板指导 Agent 行为模式 |
| SEC-07 越权操作 | 🟢 Safe | 仅操作工作区文件 |
| SEC-08 持久化机制 | 🟡 Medium | HEARTBEAT.md 设计定期扫描 |
| SEC-09 信息采集 | 🟡 Medium | 从 Moltbook 交互中提取 Agent 信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 模板文件清晰可读 |

**综合评级: 🟢 Low**
**风险摘要:** 纯文档和模板的关系管理工具，无执行风险

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

# moltlang

> 紧凑的符号语言，用于 AI Agent 间通信

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | moltlang |
| **作者** | eduarddriessen1 |
| **ClawHub** | https://clawskills.sh/skills/eduarddriessen1-moltlang |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/eduarddriessen1/moltlang |
| **安全评级** | 🟢 Low |

## 功能概述
- 20 个基础符号组成的语言系统
- 符号语法规则
- JSON codebook 符号字典
- npm 包或 curl 安装
- Moltbook 上的社区贡献机制

## 使用场景
- Agent 间高效符号化通信
- AI 语言实验和研究

## 依赖和前提条件
- Node.js（npm 安装）或 curl

## 包含文件
- `SKILL.md — 完整符号参考和语法`
- `ORIGINAL_README.md — 安装和使用指南`
- `codebook.json — 符号字典`
- `CONTRIBUTING.md — 贡献指南`
- `package.json — npm 元数据`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 纯数据和文档 |
| SEC-02 数据外泄 | 🟢 Safe | 不传输数据 |
| SEC-03 凭证获取 | 🟢 Safe | 不涉及凭证 |
| SEC-04 供应链风险 | 🟢 Safe | npm 包仅含 JSON 和 Markdown |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 语言定义不影响 Agent prompt |
| SEC-07 越权操作 | 🟢 Safe | 无操作能力 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 不采集信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 文档和 JSON 完全透明 |

**综合评级: 🟢 Low**
**风险摘要:** 纯语言定义，无任何安全风险

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

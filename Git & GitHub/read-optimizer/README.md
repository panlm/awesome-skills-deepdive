# Read Optimizer

> Optimizes file reading operations by providing smarter read strategies (head/tail/grep/diff) to reduce token usage and latency. Use this when you need to inspect large files efficiently without dumpin

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Read Optimizer |
| **作者** | autogame-17 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/autogame-17-read-optimizer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/autogame-17/read-optimizer |
| **安全评级** | 🟢 Low |

## 功能概述
- `--file <path>`: Path to the file.
- `--mode <smart|grep|diff>`: Operation mode (default: smart).
- `--lines <number>`: Number of lines for head/tail (default: 50).
- `--pattern <string>`: Regex pattern for grep mode.
- `--context <number>`: Context lines for grep (default: 2).

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `SKILL.md`
- `_meta.json`
- `index.js`
- `package.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
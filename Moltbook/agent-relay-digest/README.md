# agent-relay-digest

> 从 Agent 社区（Moltbook/Clawfee/yclawker）采集帖子并生成精选摘要

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | agent-relay-digest |
| **作者** | orosha-ai |
| **ClawHub** | https://clawskills.sh/skills/orosha-ai-agent-relay-digest |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/orosha-ai/agent-relay-digest |
| **安全评级** | 🟢 Low |

## 功能概述
- 从多个 Agent 社交平台采集帖子（Moltbook、Clawfee、yclawker）
- 按主题聚类和评分排名
- 识别合作机会、Build Log 和安全警报
- 生成包含统计、热门话题、人物推荐的摘要报告
- 支持 Markdown 输出和机器可读的结构化数据
- 可配置排除词和最低评分阈值

## 使用场景
- 每日/每周生成 Agent 社区热点摘要
- 识别有价值的合作机会和新兴话题
- 监控安全相关的讨论和警报

## 依赖和前提条件
- Python 3
- Moltbook API Key
- Clawfee Token（可选）
- yclawker API Key（可选）

## 包含文件
- `SKILL.md — 技能定义和工作流说明`
- `scripts/relay_digest.py — 主脚本，采集帖子并生成摘要`
- `references/spec.md — 详细 v0.1 规范`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 使用 Python urllib 进行 HTTP 请求，无 shell 命令执行 |
| SEC-02 数据外泄 | 🟢 Safe | 数据仅写入本地文件，不外传 |
| SEC-03 凭证获取 | 🟡 Medium | 读取 ~/.config/ 下的凭证文件和环境变量中的 API Key |
| SEC-04 供应链风险 | 🟢 Safe | 纯 Python 标准库，无第三方依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅写入指定的 digest 输出文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 LLM 交互，纯数据处理脚本 |
| SEC-07 越权操作 | 🟢 Safe | 仅调用公开 API 的只读端点 |
| SEC-08 持久化机制 | 🟢 Safe | 无 cron/daemon/自启动设置 |
| SEC-09 信息采集 | 🟡 Medium | 从多个平台采集公开帖子数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读，无混淆 |

**综合评级: 🟢 Low**
**风险摘要:** 脚本行为透明，仅读取公开 API 和本地凭证文件生成摘要

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

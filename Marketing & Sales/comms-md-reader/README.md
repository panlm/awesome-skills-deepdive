# COMMS.md Reader

> "Read and adapt to someone's COMMS.md before contacting them. Use when: (1) drafting a message, email, or outreach to someone who has a COMMS.md, (2) scheduling or proposing a call with someone who has a COMMS.md, (3) the user asks you to check someone's communication preferences, (4) you need to calibrate tone, channel, or timing for a message to a specific person."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | COMMS.md Reader |
| **作者** | stedmanhalliday |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/stedmanhalliday-comms-md-reader |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/stedmanhalliday/comms-md-reader |
| **安全评级** | 🟢 Low |

## 功能概述
- Reads a recipient's COMMS.md from user-approved sources
- Selects the right channel and timing based on their preferences
- Calibrates tone to match their closeness tier and mechanics
- Avoids their stated anti-patterns
- Flags conflicts between user instructions and recipient preferences

## 使用场景
- 营销活动管理和执行
- 客户获取和转化
- 销售流程优化

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。凭证获取：需要 API 密钥或令牌；越权操作：涉及权限相关操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
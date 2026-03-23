# multiple-personas

> 创建和管理具有不同性格的 AI 子代理人格

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | multiple-personas |
| **作者** | ipedrax |
| **ClawHub** | https://clawskills.sh/skills/ipedrax-multiple-personas |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ipedrax/multiple-personas |
| **安全评级** | 🟢 Low |

## 功能概述
- 创建具有独特身份的 AI 人格（SOUL.md/PERSONALITY.md/MEMORY.md）
- 通过 sessions_spawn 激活人格子代理
- 人格间记忆隔离
- 预置三个人格：Luna、Rex、Milo
- 人格仅限文本对话，无工具访问权限
- 自动记录对话到人格记忆

## 使用场景
- 与不同 AI 角色进行沉浸式对话
- 创建专属的 AI 角色扮演伙伴

## 依赖和前提条件
- OpenClaw sessions_spawn 功能

## 包含文件
- `SKILL.md` — 技能定义和完整管理指南
- `profiles/luna/` — Luna 人格（SOUL.md/PERSONALITY.md/MEMORY.md）
- `profiles/rex/` — Rex 人格
- `profiles/milo/` — Milo 人格

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 子代理明确标注"文本仅限"，无工具访问 |
| SEC-02 数据外泄 | 🟢 Safe | 不发送数据到外部 |
| SEC-03 凭证获取 | 🟢 Safe | 不处理凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 纯文本文件，无代码依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅更新人格 MEMORY.md 文件 |
| SEC-06 Prompt 注入 | 🟡 Medium | 用户消息直接注入到子代理 prompt 中 |
| SEC-07 越权操作 | 🟢 Safe | 子代理被限制为纯文本对话 |
| SEC-08 持久化机制 | 🟢 Safe | 仅 MEMORY.md 更新 |
| SEC-09 信息采集 | 🟢 Safe | 不采集信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 纯文本可审计 |

**综合评级: 🟢 Low**
**风险摘要:** 纯文本人格管理工具，子代理无工具权限，仅有轻微 prompt 注入风险

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

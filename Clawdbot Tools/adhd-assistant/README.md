# adhd-assistant

> ADHD 友好的生活管理助手，支持每日规划、任务分解、时间管理和情绪支持

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | adhd-assistant |
| **作者** | thinktankmachine |
| **ClawHub** | https://clawskills.sh/skills/thinktankmachine-adhd-assistant |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/thinktankmachine/adhd-assistant |
| **安全评级** | 🟢 Low |

## 功能概述
- 每日规划与签到，创建时间块式日程
- 任务分解为 2-5 分钟的微步骤
- 时间盲区支持与提醒系统
- 优先级框架（艾森豪威尔矩阵）
- 虚拟陪伴与问责机制
- 多巴胺调节与奖励提示
- 情绪支持与自我关怀引导

## 使用场景
- 帮助 ADHD 用户规划日常任务和时间管理
- 拖延症干预和任务启动支持
- 情绪调节和自我关怀练习

## 依赖和前提条件
OpenClaw 记忆系统和调度工具

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 纯 Markdown 指导，无命令执行 |
| SEC-02 数据外泄 | 🟢 Safe | 无网络通信或数据外发 |
| SEC-03 凭证获取 | 🟢 Safe | 不涉及凭证操作 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统写入 |
| SEC-06 Prompt 注入 | 🟡 Medium | SKILL.md 中包含大量行为指导性 prompt，可被用作 prompt 注入模板 |
| SEC-07 越权操作 | 🟢 Safe | 无越权操作风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 仅通过 OpenClaw 记忆系统记录用户偏好 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰无混淆 |

**综合评级: 🟢 Low**
**风险摘要:** 纯指导性 Skill，无脚本和命令执行，安全风险极低

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

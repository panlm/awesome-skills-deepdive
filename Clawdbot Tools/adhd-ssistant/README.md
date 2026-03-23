# adhd-ssistant

> ADHD 友好的生活管理助手（adhd-assistant 的重复发布版本）

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | adhd-ssistant |
| **作者** | thinktankmachine |
| **ClawHub** | https://clawskills.sh/skills/thinktankmachine-adhd-ssistant |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/thinktankmachine/adhd-ssistant |
| **安全评级** | 🟢 Low |

## 功能概述
- 与 adhd-assistant 内容完全相同
- 每日规划与任务分解功能
- 时间管理和优先级框架
- 虚拟陪伴与情绪支持
- 多巴胺调节策略

## 使用场景
- 同 adhd-assistant
- 疑似误发的重复 skill

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
| SEC-02 数据外泄 | 🟢 Safe | 无网络通信 |
| SEC-03 凭证获取 | 🟢 Safe | 不涉及凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件写入 |
| SEC-06 Prompt 注入 | 🟡 Medium | 包含大量行为指导 prompt |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 仅记忆系统偏好 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆 |

**综合评级: 🟢 Low**
**风险摘要:** adhd-assistant 的重复版本，同样安全

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

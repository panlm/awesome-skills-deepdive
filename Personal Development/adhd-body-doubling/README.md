# adhd-body-doubling

> ADHD 专注伴侣 — 朋克风格的陪伴式工作法，含微步骤协议和多巴胺重置

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | adhd-body-doubling |
| **作者** | jankutschera |
| **ClawHub** | https://clawskills.sh/skills/jankutschera-adhd-body-doubling |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jankutschera/adhd-body-doubling |
| **许可证** | MIT |
| **安全评级** | 🟡 Medium |

## 功能概述
- A virtual body double for ADHD founders who struggle to start, stay focused, or finish tasks. Built by [ADHD-founder.com](https://adhd-founder.com) -- German Engineering for the ADHD Brain.
- First Micro-Step Protocol -- bypasses "I don't know where to start" paralysis
- Communicative Accountability -- pushes back on excuses, demands specifics
- Frequent Check-Ins -- every 15-25 min, never hourly (ADHD brains need contact)
- Auto Micro-Task Suggestions -- when stuck, breaks tasks down automatically
- Session History -- tracks patterns so you learn what works for YOUR brain

## 包含文件
- `ORIGINAL_README.md` — 原始说明文档
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `references/` — 目录
- `scripts/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟡 Medium | 包含持久化配置 |
| SEC-09 信息采集 | 🟡 Medium | 包含网络探测功能 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
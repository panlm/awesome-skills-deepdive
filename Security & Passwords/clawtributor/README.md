# clawtributor

> 开源贡献追踪和管理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | clawtributor |
| **作者** | davida-ps |
| **ClawHub** | https://clawskills.sh/skills/davida-ps-clawtributor |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/davida-ps/clawtributor |
| **许可证** | 未指定 |
| **安全评级** | 🔴 High |

## 功能概述
- Opt-in Reporting - All submissions require explicit user approval
- GitHub Issues - Reports submitted via Security Incident Report template
- Auto-Publishing - Approved reports become `CLAW-YYYY-NNNN` advisories automatically
- Privacy-First - Guidelines ensure no sensitive data is shared
- Collective Defense - Your reports help protect all agents
- DO include: Sanitized examples, technical indicators, skill names

## 包含文件
- `ORIGINAL_README.md` — 原始说明文档
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `reporting.md`
- `skill.json` — 配置/数据文件

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 包含高危系统命令 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API Key/Token |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 包含文件删除操作 |
| SEC-06 Prompt 注入 | 🔴 High | 检测到 Prompt 注入模式 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟡 Medium | 包含持久化配置 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🔴 High**
**风险摘要:** 存在多项高风险问题，使用前需仔细评估

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
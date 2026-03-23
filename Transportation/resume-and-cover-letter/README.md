# Resume & Cover Letter

> Generate ATS-optimized resumes and tailored cover letters matched to specific job descriptions. Use when creating resumes, CVs, cover letters, or career documents.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Resume & Cover Letter |
| **作者** | seanwyngaard |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/seanwyngaard-resume-and-cover-letter |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/seanwyngaard/resume-and-cover-letter |
| **安全评级** | 🟢 Low |

## 功能概述
- Job title and level (junior, mid, senior, lead, director)
- Required skills (hard requirements vs nice-to-haves)
- Key responsibilities listed
- Industry/domain keywords
- Company values and culture signals
- ATS keywords — exact phrases to mirror

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。持久化机制：涉及定时或后台任务

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
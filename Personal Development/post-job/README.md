# post-job

> 职位发布工具 — 在多个平台发布招聘信息

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | post-job |
| **作者** | zhangdong |
| **ClawHub** | https://clawskills.sh/skills/zhangdong-post-job |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/zhangdong/post-job |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Natural Language Interface - Post jobs with simple commands like "Hire a frontend engineer in Singapore"
- Global City Support - 100+ cities worldwide with fuzzy matching (Singapore, Hong Kong, New York, London, etc.)
- AI Job Description - Optional AI-powered JD generation for professional, compelling postings
- Instant Application Links - Get shareable URLs for candidates to apply directly
- Resume Collection - All applications sent to your specified email
- LinkedIn Sync - Automatic LinkedIn job posting integration (no LinkedIn account binding required — posts through Fuku AI's relay service)

## 依赖和前提条件
- Q: Can I use this without LinkedIn sync?**
- Q: Will the job appear on MY LinkedIn company page?**
- Q: What happens if Fuku AI goes offline?**
- Q: Can I delete a job after posting?**
- Q: Is the embedded credential a security risk?**

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `assets/` — 目录
- `package.json` — 配置/数据文件
- `pnpm-lock.yaml` — 配置/数据文件
- `scripts/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API Key/Token |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部包 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
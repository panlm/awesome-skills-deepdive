# AI Interview Simulator

> Candaigo AI Interview Simulator - AI-powered group interview simulation platform. Browse jobs, join interviews, check history, upload resumes.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | AI Interview Simulator |
| **作者** | hangeaiagent |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/hangeaiagent-ai-interview-simulator-candaigo |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/hangeaiagent/ai-interview-simulator-candaigo |
| **安全评级** | 🟡 Medium |

## 功能概述
- `page` (可选)：页码，默认 1
- `page_size` (可选)：每页数量，默认 20，最大 100
- `company_type` (可选)：公司类型
- `job_category` (可选)：岗位类别
- `search` (可选)：搜索关键词
- `job_title` (可选)：岗位名称

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🔴 High | 存在代码混淆或编码 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 3 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
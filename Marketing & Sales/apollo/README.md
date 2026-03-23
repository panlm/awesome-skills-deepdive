# Apollo

> Interact with Apollo.io REST API (people/org enrichment, search, lists).

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Apollo |
| **作者** | jhumanj |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/jhumanj-apollo |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jhumanj/apollo |
| **安全评级** | 🟡 Medium |

## 功能概述
- `APOLLO_BASE_URL` (usually `https://api.apollo.io`)
- `APOLLO_API_KEY`
- GET: `skills/apollo/scripts/apollo-get.sh "/api/v1/users"` (endpoint availability may vary)
- People search (new): `skills/apollo/scripts/apollo-people-search.sh "vp marketing" 1 5`
- POST (generic): `skills/apollo/scripts/apollo-post.sh "/api/v1/mixed_people/api_search" '{"q_keywords":"vp marketing","p
- Enrich website/org by domain: `skills/apollo/scripts/apollo-enrich-website.sh "apollo.io"`

## 使用场景
- 营销活动管理和执行
- 客户获取和转化
- 销售流程优化

## 依赖和前提条件
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 4 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；文件系统篡改：存在文件系统操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
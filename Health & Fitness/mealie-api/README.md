# Mealie Recipe Manager

> Mealie 食谱管理 API 集成工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Mealie Recipe Manager |
| **作者** | angusthefuzz |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/angusthefuzz-mealie-api |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/angusthefuzz/mealie-api |
| **安全评级** | 🔴 High |

## 功能概述
- Uses Bearer token authentication
- All endpoints are under `/api/`
- Pagination is supported on list endpoints (use `--page` and `--per-page` flags)
- Recipe slugs are URL-friendly identifiers (e.g., `spaghetti-carbonara`)

## 使用场景
- 通过 API 管理 Mealie 食谱库
- 搜索、创建和编辑食谱
- 生成购物清单和菜单计划

## 依赖和前提条件
- Node.js / npm
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，1 项中风险。凭证获取：需要多种敏感凭证；文件系统篡改：涉及危险文件操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

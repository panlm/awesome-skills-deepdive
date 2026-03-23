# Generic Quality Gateways for Unattended Agent Development

> This skill defines and applies **6 universal quality gateways** for typical application projects that include:

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Generic Quality Gateways for Unattended Agent Development |
| **作者** | thecybercore |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawskills.sh/skills/thecybercore-tcc-quality-gates |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/thecybercore/tcc-quality-gates |
| **安全评级** | 🟡 Medium |

## 功能概述
- CI pipeline status (green on default branch / PR)
- Reproducible build or deterministic packaging indicators
- Dependency freshness (stale/outdated dependencies)
- License policy compliance (allowlist/denylist)
- SBOM presence (if required)

## 使用场景
- 管理 macOS/iOS 日历事件
- 查询日程安排与空闲时间
- 通过命令行创建/修改日历事件

## 包含文件
- `SKILL.md`
- `_meta.json`
- `templ`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。凭证获取：需要多种敏感凭证；越权操作：需要提权或管理员权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
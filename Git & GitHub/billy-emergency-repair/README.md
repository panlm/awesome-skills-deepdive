# Billy Emergency Repair

> ⚠️ **NEILL-ONLY COMMAND** ⚠️

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Billy Emergency Repair |
| **作者** | highlander89 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/highlander89-billy-emergency-repair |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/highlander89/billy-emergency-repair |
| **安全评级** | 🟡 Medium |

## 功能概述
- Neill explicitly requests Billy system repair
- Neill reports Billy authentication/gateway issues
- Neill says "fix Billy" or "Billy is down"
- Billy system appears unresponsive to Neill
- Billy is working fine
- Issue is not authentication-related

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
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
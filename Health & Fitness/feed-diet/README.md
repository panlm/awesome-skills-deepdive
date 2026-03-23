# feed-diet

> 饲料和饮食配方管理工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | feed-diet |
| **作者** | tkuehnl |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/tkuehnl-feed-diet |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tkuehnl/feed-diet |
| **安全评级** | 🟡 Medium |

## 功能概述
- "feed diet"
- "information diet"
- "audit my feeds"
- "what am I reading"
- "analyze my HN"
- "reading habits"
- "content diet"
- "feed report"

## 使用场景
- 制定动物或个人饮食配方
- 计算营养成分配比
- 管理饮食计划和食材清单

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `CHANGELOG.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

# Cold Outreach

> 冷启动外联管理工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Cold Outreach |
| **作者** | staybased |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/staybased-cold-outreach |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/staybased/cold-outreach |
| **安全评级** | 🟢 Low |

## 功能概述
- 多渠道冷外联管理
- 外联序列自动化
- 目标客户筛选
- 效果追踪和优化

## 使用场景
- 管理和执行多渠道的冷启动客户外联
- 自动化外联序列提高客户触达效率

## 依赖和前提条件
- Google API

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。数据外泄：存在外部 API 调用




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
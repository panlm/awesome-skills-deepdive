# Foxreach

> FoxReach 外联营销工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Foxreach |
| **作者** | concaption |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/concaption-foxreach |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/concaption/foxreach |
| **安全评级** | 🟡 Medium |

## 功能概述
- 营销外联自动化
- 联系人管理和分类
- 外联效果追踪
- 模板化外联流程

## 使用场景
- 自动化营销外联流程提高客户触达效率
- 管理和追踪外联活动的效果数据

## 依赖和前提条件
- API 密钥
- Python 运行环境
- Python pip

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `api-reference.md`
- `examples.md`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
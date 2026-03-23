# Writing Assistant

> You are a Writing Team Lead managing specialized writers via MCP tools. Please ANALYZE the writing task and then:1. if exist references, create a detailed content strategy and give suggestions on references selection, then assign it to the appropriate tool. 2. if not exist references, break down and go into details about how to achieve the writing task, giving thoroughly guidance to the appropr...

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Writing Assistant |
| **作者** | urrrich |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/urrrich-writing-assistant |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/urrrich/writing-assistant |
| **安全评级** | 🟢 Low |

## 功能概述
- This skill is based on the Writing_Assistant agent configuration
- Template variables (if any) like $DATE$, $SESSION_GROUP_ID$ may require runtime substitution
- Follow the instructions and guidelines provided in the content above

## 使用场景
- 营销活动管理和执行
- 客户获取和转化
- 销售流程优化

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
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 未发现明显安全风险，文档透明可审计

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
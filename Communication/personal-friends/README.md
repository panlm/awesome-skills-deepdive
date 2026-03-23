# Personal Friends

> 作为用户社交生活助手，记住朋友信息和社交历史

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Personal Friends |
| **作者** | gekacross |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/gekacross-personal-friends |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/gekacross/personal-friends |
| **安全评级** | 🟢 Low |

## 功能概述
- 记录和管理朋友个人信息
- 追踪社交互动历史和重要日期
- 提醒生日、纪念日等重要时刻
- 维护朋友关系图谱和备注
- 回忆过往对话和社交事件

## 使用场景
- 查询朋友信息和社交历史记录
- 生日和重要日期提醒
- 社交关系管理与维护

## 依赖和前提条件
- 初始化朋友信息数据库
- 配置提醒和通知偏好

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
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

# Collaboration Helper

> 社区行动项追踪和协调信号管理工具，帮助团队高效跟进待办事项和协作进度

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Collaboration Helper |
| **作者** | crimsondevil333333 |
| **版本** | 1.0.1 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/crimsondevil333333-collaboration-helper |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/crimsondevil333333/collaboration-helper |
| **安全评级** | 🟢 Low |

## 功能概述
- 追踪和记录社区行动项和待办事项
- 协调信号检测和分发
- 任务状态更新和进度追踪
- 团队成员间的协作信息同步
- 自动提醒和截止日期管理

## 使用场景
- 开源社区维护者追踪 Issue 处理进度和贡献者行动项
- 项目团队同步跨部门协作任务和决策信息
- 社区管理员监控和协调志愿者的任务分配

## 依赖和前提条件
- 配置目标社区或团队的数据源
- 设置协作通知渠道

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `data`
- `references`
- `scripts`
- `tests`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；越权操作：涉及权限相关操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

# Fork and Skill Scanner Ultimate

> 单次扫描 1000 个 GitHub Fork，发现有价值的变更和新兴趋势，并评估 ClawHub 热门 Skill

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Fork and Skill Scanner Ultimate |
| **作者** | globalcaos |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/globalcaos-fork-and-skill-scanner-ultimate |

## 功能概述
- Bash 预筛选 1000 个 Fork，淘汰不活跃的仓库
- 子代理扇出分析：将候选 Fork 分发到并行处理
- Fork 扫描器按计划运行（周一/周四）
- Skill 扫描器评估 10 个 Skill：按功能性、相关性和维护状态打分
- 深入扫描顶级作者的其他 Skill
- 自动生成包含详细洞察的报告到 `Cron_Tasks/` 目录

## 使用场景
- 监控开源项目的 Fork 生态，发现社区中有价值的创新变更
- 定期评估 ClawHub 上的热门 Skill，跟踪生态趋势

## 依赖和前提条件
- GitHub Token（访问 GitHub API）
- Bash 环境
- `gh` CLI（推荐）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成

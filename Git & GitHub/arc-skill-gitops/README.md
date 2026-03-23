# Skill Gitops

> 代理技能的自动化部署、回滚和版本管理，像管理代码一样管理技能

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Skill Gitops |
| **作者** | trypto1019 |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/trypto1019-arc-skill-gitops |

## 功能概述
- 初始化技能的 Git 跟踪（init），在技能目录中创建 Git 仓库
- 部署前自动创建快照（deploy），然后提交新状态
- 支持按标签回滚到任意历史版本（rollback）
- 查看所有跟踪技能的当前状态和版本（status）
- 集成 arc-skill-scanner 进行部署前安全检查（check）
- 完整的快照历史记录，支持描述性标签（如 "v1.2", "pre-security-patch"）
- 数据存储在 `~/.openclaw/gitops/` 目录

## 使用场景
- 更新技能时自动备份当前版本，出现问题可一键回滚
- 在 CI/CD 流程中集成安全扫描作为部署门控
- 管理多个技能的版本状态，追踪哪些是稳定版本

## 依赖和前提条件
- `python3`
- `git`
- 支持的操作系统：macOS、Linux
- 可选：arc-skill-scanner（用于部署前安全检查）

## 安全状态

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

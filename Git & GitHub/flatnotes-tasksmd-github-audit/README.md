# Flatnotes + Tasks.md GitHub Audit

> 深度审计 Tasks.md 和 Flatnotes 的数据漂移和准确性，以 GitHub 为唯一真相源检测过时笔记和缺失链接

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Flatnotes + Tasks.md GitHub Audit |
| **作者** | branexp |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/branexp-flatnotes-tasksmd-github-audit |

## 功能概述
- 看板卫生检查：验证全局泳道存在、WIP 限制、卡片格式和标签一致性
- 项目完整性审查：检查项目必需笔记（Overview、Research、Plan、Log）是否存在
- GitHub 真相对账：将 PR 状态与 Tasks 卡片交叉比对，检测遗漏
- 检测过时的 Done 卡片是否缺少 PR 链接
- 检查已合并 PR 是否反映在项目日志中
- 生成 Markdown 和 JSON 格式的审计报告
- 支持安全的自动修复（创建缺失笔记、修正泳道分配、添加链接）

## 使用场景
- 定期审计项目管理系统确保笔记、任务卡和 GitHub PR 三方数据同步
- 检查哪些已合并的 PR 还没有更新到项目日志中

## 依赖和前提条件
- Node.js（运行 audit.mjs 脚本）
- `gh` CLI（GitHub 交叉检查，未认证时该部分标记为 SKIPPED）
- 可选环境变量：`TASKS_ROOT`、`FLATNOTES_ROOT`

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 4 项中风险。凭证获取：需要 API 密钥或令牌；Prompt 注入：存在可疑 Prompt 模式；越权操作：涉及权限相关操作

---
> 本文档由 awesome-skills-deepdive skill 自动生成

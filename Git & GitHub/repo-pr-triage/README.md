# Repo PR Triage

> 基于项目愿景文档对 GitHub PR 和 Issue 进行优先级评分和分类处理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Repo PR Triage |
| **作者** | patrob |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/patrob-repo-pr-triage |

## 功能概述
- 通过面谈采访仓库所有者，生成项目愿景文档和评分标准
- 使用基于规则的启发式评分系统（基础分 50，安全修复 +20、有测试的 Bug 修复 +10 等）对 PR 进行自动评分
- 通过标题相似度检测潜在重复 PR
- 生成四种 Markdown 报告：快速通道（80+）、标准审查（50-79）、建议关闭（<50）和汇总报告
- 支持通过 Cron 定时任务实现每周自动化分类
- 使用 `gh` CLI 获取 PR 元数据（标题、正文、标签、diff 大小、作者等）
- 三步工作流：入职引导（Onboard）→ 扫描评分（Scan）→ 报告生成（Report）

## 使用场景
- 开源项目维护者需要高效处理大量 PR，按优先级排队审查
- 团队定期进行 PR 分类，识别应快速合并、需仔细审查或应关闭的 PR
- 通过 Cron 自动化每周生成 PR 分类报告并推送到 Telegram 等渠道

## 依赖和前提条件
- `gh` CLI 已安装并完成认证（`gh auth login`）
- Python 3.10+
- 无额外 Python 包依赖（仅使用标准库）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive skill 自动生成

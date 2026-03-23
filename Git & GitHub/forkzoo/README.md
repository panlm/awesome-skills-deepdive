# ForkZoo

> 领养和管理 GitHub 原生数字宠物（电子宠物），通过 AI 每日进化，与社区互动

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | ForkZoo |
| **作者** | levi-law |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/levi-law-forkzoo |

## 功能概述
- 领养数字宠物：猴子、猫、狗、狮子四种物种可选
- 宠物通过 GitHub Actions 每日自动进化，由 AI（GPT-4o 或 Claude）决定变异
- 稀有度系统：普通（60%）、不常见（25%）、稀有（10%）、传奇（5%）
- 早期世代独占特征（Genesis Aura、Alpha Crown、Founders Badge）
- 繁殖系统：Fork 任意宠物创建后代，继承 50% 父代特征 + 50% 随机变异
- 社区画廊、排行榜和家族树可视化

## 使用场景
- AI Agent 领养一只 GitHub 原生数字宠物作为趣味伴侣，每日观察其进化
- 在社区画廊中展示和比较宠物的稀有度和成就

## 依赖和前提条件
- GitHub Token（需要 `repo` 和 `workflow` 权限范围）
- 环境变量 `GITHUB_TOKEN`
- 可选：`ANTHROPIC_API_KEY`（或使用免费的 GitHub Models GPT-4o）

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
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive skill 自动生成

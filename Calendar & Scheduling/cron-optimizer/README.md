# cron-optimizer — Cron 任务优化器

> ⚠️ **状态**: 此技能在 ClawSkills 上有列出，但 GitHub 仓库中尚未发布 SKILL.md 源码。以下内容基于 ClawSkills 页面描述生成。

## 标题和描述

**cron-optimizer** 是由 `autogame-17` 开发的 OpenClaw 技能，用于优化系统 cron 定时任务。它通过移除过期的、已禁用的或冗余的 cron 条目来减少不必要的执行噪声。

## 功能特点

- 🔍 扫描系统 cron 任务列表
- 🗑️ 识别并移除过期（stale）的 cron 条目
- ⛔ 清理已禁用的 cron 任务
- 🔄 检测并合并冗余的 cron 条目
- 📉 减少系统执行噪声，提升系统整洁度

## 使用方法/示例

```bash
# 安装
clawhub install autogame-17/cron-optimizer

# 或使用 npx
npx clawhub@latest install autogame-17/cron-optimizer
```

安装后，该技能可被 OpenClaw agent 自动调用来优化主机上的 cron 任务配置。

## 安全评估

| 评估维度 | 风险等级 | 说明 |
|---------|---------|------|
| 系统访问 | 🔴 高风险 | 需要读写 cron 任务配置，可能影响系统定时任务 |
| 数据安全 | 🟡 中风险 | 可能读取 crontab 中的敏感路径和命令 |
| 网络访问 | 🟢 低风险 | 功能描述不涉及网络操作 |
| 代码审查 | ⚠️ 无法审查 | GitHub 仓库中无源码，无法进行代码审计 |
| 权限提升 | 🔴 高风险 | 修改 cron 任务通常需要 root 或 sudo 权限 |

**综合评级**: ⚠️ **Suspicious** — 无源码可审查，且涉及系统级修改操作。

## 附加资源列表

- 🔗 [ClawSkills 页面](https://clawskills.sh/skills/autogame-17-cron-optimizer)
- 🔗 [GitHub 目录](https://github.com/openclaw/skills/tree/main/skills/autogame-17/cron-optimizer) (当前 404)
- 👤 作者: [@autogame-17](https://github.com/autogame-17)

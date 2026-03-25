# ghggh — GitHub 仓库统计查询工具

> ⚠️ **状态**: 此技能在 ClawSkills 上有列出，但 GitHub 仓库中尚未发布 SKILL.md 源码。以下内容基于 ClawSkills 页面描述生成。

## 标题和描述

**ghggh** 是由 `chenpinji` 开发的 OpenClaw 技能，用于查询 GitHub 仓库的 Star 数量和代码行数。该技能为 AI agent 提供了快速获取 GitHub 仓库基本统计信息的能力。

## 功能特点

- ⭐ 查询指定 GitHub 仓库的 Star 数量
- 📊 统计仓库的代码行数（Lines of Code）
- 🔍 快速获取仓库基本统计信息
- 🤖 适合 AI agent 在代码评估和项目分析时使用

## 使用方法/示例

```bash
# 安装
clawhub install chenpinji/ghggh

# 或使用 npx
npx clawhub@latest install chenpinji/ghggh
```

安装后，可通过 OpenClaw agent 查询任意 GitHub 仓库的 Star 数和代码行数。

## 安全评估

| 评估维度 | 风险等级 | 说明 |
|---------|---------|------|
| 系统访问 | 🟢 低风险 | 仅查询操作，不修改本地系统 |
| 数据安全 | 🟢 低风险 | 查询的是公开的 GitHub 仓库信息 |
| 网络访问 | 🟢 低风险 | 需要访问 GitHub API，属于标准操作 |
| 代码审查 | ⚠️ 无法审查 | GitHub 仓库中无源码（作者 chenpinji 目录不存在），无法进行代码审计 |
| 凭证安全 | 🟡 中风险 | 可能需要 GitHub Token 以提高 API 速率限制 |

**综合评级**: ⚠️ **Suspicious** — 无源码可审查。功能本身风险较低，但无法验证实际行为。

## 附加资源列表

- 🔗 [ClawSkills 页面](https://clawskills.sh/skills/chenpinji-ghggh)
- 🔗 [GitHub 目录](https://github.com/openclaw/skills/tree/main/skills/chenpinji/ghggh) (当前 404)
- 👤 作者: [@chenpinji](https://github.com/chenpinji)
- 📚 [GitHub REST API](https://docs.github.com/en/rest) — GitHub API 文档

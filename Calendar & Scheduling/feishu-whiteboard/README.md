# feishu-whiteboard — 飞书白板技能

> ⚠️ **状态**: 此技能在 ClawSkills 上有列出，但 GitHub 仓库中尚未发布 SKILL.md 源码。以下内容基于 ClawSkills 页面描述生成。

## 标题和描述

**feishu-whiteboard** 是由 `autogame-17` 开发的 OpenClaw 技能，用于创建和操作飞书（Feishu/Lark）白板。该技能为 AI agent 提供了与飞书白板功能交互的能力。

## 功能特点

- 📝 创建飞书白板文档
- ✏️ 在白板上进行内容操作和编辑
- 🔗 与飞书协作生态集成
- 🤖 允许 AI agent 自动化白板内容管理

## 使用方法/示例

```bash
# 安装
clawhub install autogame-17/feishu-whiteboard

# 或使用 npx
npx clawhub@latest install autogame-17/feishu-whiteboard
```

安装后，该技能可被 OpenClaw agent 调用来创建和操作飞书白板。可能需要配置飞书 API 凭证才能正常使用。

## 安全评估

| 评估维度 | 风险等级 | 说明 |
|---------|---------|------|
| 系统访问 | 🟢 低风险 | 主要通过 API 与飞书交互，不涉及本地系统修改 |
| 数据安全 | 🟡 中风险 | 需要飞书 API Token，可能访问企业内部白板内容 |
| 网络访问 | 🟡 中风险 | 需要连接飞书 API 服务器 |
| 代码审查 | ⚠️ 无法审查 | GitHub 仓库中无源码，无法进行代码审计 |
| 凭证安全 | 🟡 中风险 | 需要飞书 App ID/Secret 等凭证信息 |

**综合评级**: ⚠️ **Suspicious** — 无源码可审查，且涉及第三方 API 凭证。

## 附加资源列表

- 🔗 [ClawSkills 页面](https://clawskills.sh/skills/autogame-17-feishu-whiteboard)
- 🔗 [GitHub 目录](https://github.com/openclaw/skills/tree/main/skills/autogame-17/feishu-whiteboard) (当前 404)
- 👤 作者: [@autogame-17](https://github.com/autogame-17)
- 📚 [飞书开放平台文档](https://open.feishu.cn/)

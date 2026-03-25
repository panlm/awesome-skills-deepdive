# 🧠 Honcho Setup — 持久跨会话记忆系统

## 描述

Honcho Setup 用于安装 `@honcho-ai/openclaw-honcho` 插件并将遗留的工作空间记忆文件迁移到 Honcho 云端。支持托管模式（api.honcho.dev）和自托管模式。

## 功能特点

- **一键安装**：自动安装 Honcho 插件并完成初始化配置
- **记忆迁移**：将 USER.md、MEMORY.md、IDENTITY.md、memory/、canvas/ 等文件上传到 Honcho
- **安全确认**：所有上传操作都需要用户明确的交互式确认
- **本地备份**：迁移前自动归档所有原始文件
- **自托管支持**：支持连接到自建的 Honcho 实例
- **持久观察**：安装后插件会持续观察对话并传输数据到 Honcho

## 使用方法

```bash
# 安装插件
clawhub install ajspig/honcho-setup

# 运行设置（需要交互确认）
openclaw honcho setup

# 禁用插件（停止持续数据传输）
openclaw plugins disable openclaw-honcho
```

### 环境变量

| 变量 | 说明 |
|------|------|
| `HONCHO_API_KEY` | 托管模式所需（从 https://app.honcho.dev 获取） |
| `HONCHO_BASE_URL` | 自托管实例地址（默认 https://api.honcho.dev） |

## 安全评估

- **VirusTotal**: ⚠️ 未验证
- **OpenClaw**: ⚠️ 未验证
- **风险说明**: ⚠️ **会上传工作空间内容到外部 API**。包括 USER.md、MEMORY.md 等敏感文件。安装后插件会持续观察对话并传输数据。

## 附加资源

- [GitHub 源码](https://github.com/openclaw/skills/tree/main/skills/ajspig/honcho-setup)
- [ClawHub 页面](https://clawskills.sh/skills/ajspig-honcho-setup)
- [Honcho 平台](https://app.honcho.dev)

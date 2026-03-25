# Shortcuts Generator (快捷指令生成器)

> 生成 macOS/iOS 快捷指令的 plist 文件

## 📖 描述

Shortcuts Generator 是一个用于生成 Apple 快捷指令 (Shortcuts) 应用的 `.shortcut` plist 文件的 skill。覆盖 1,155 个操作（427 个 WF*Actions + 728 个 AppIntents），支持变量引用和控制流。

## ✨ 功能特点

- 生成有效的 `.shortcut` 二进制 plist 文件
- 覆盖 1,155+ Apple 快捷指令操作
- 支持 WF*Actions 和 AppIntents 两种操作类型
- 完整的控制流支持（循环、条件判断）
- 变量引用和应用集成
- 输出可直接导入快捷指令应用的签名文件

## 🚀 使用方法

### 安装
```bash
clawhub install erik-agens/shortcuts-skill
```

### 使用场景
- 自动化早晨日程（获取天气并发送通知）
- 批量处理 iPhone 照片（条件过滤）
- 链式 URL 请求和 AI 模型调用
- 创建键盘触发的 macOS 自动化
- 构建带菜单和循环的可复用快捷指令

### 基本结构
快捷指令是一个二进制 plist，包含 `WFWorkflowActions` 数组，每个操作由 `WFWorkflowActionIdentifier` 和 `WFWorkflowActionParameters` 定义。

## 🔒 安全评估

| 项目 | 状态 |
|------|------|
| ClawHub 页面 | [查看](https://clawskills.sh/skills/erik-agens-shortcuts-skill) |
| GitHub 源码 | [查看](https://github.com/openclaw/skills/tree/main/skills/erik-agens/shortcuts-skill) |
| 安全状态 | ⚠️ 待验证 (Suspicious) |
| 许可工具 | Write, Bash |

## 📚 附加资源

- [ClawSkills 页面](https://clawskills.sh/skills/erik-agens-shortcuts-skill)
- [GitHub 源码仓库](https://github.com/openclaw/skills/tree/main/skills/erik-agens/shortcuts-skill)
- 作者: @erik-agens

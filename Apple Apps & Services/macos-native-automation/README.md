# macos-native-automation

> macOS 原生自动化工具集（AppleScript/快捷指令等）

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | macos-native-automation |
| **作者** | theagentwire |
| **ClawHub** | https://clawskills.sh/skills/theagentwire-macos-native-automation |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/theagentwire/macos-native-automation |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- CGEvent doesn't have this problem. It injects hardware-level HID events directly into the macOS event stream. The OS and every app — browsers, Electron, native — treat them as real physical mouse clicks. Because at the system level, they are.
- One-time setup: Grant Accessibility access to your terminal app (System Settings → Privacy & Security → Accessibility → add Terminal/iTerm/OpenClaw).
- This is the most reliable method. Don't estimate — measure.
- Paste the full file path including filename — macOS navigates to the directory and selects the file
- Activate the target app first before sending AppleScript keystrokes:
- CGEvent wins because it operates at the hardware event layer. The OS and apps can't distinguish CGEvent clicks from your physical mouse. Every other method operates at a higher abstraction that apps can (and do) ignore.

## 依赖和前提条件
- 
- 
- 
- What problem does it solve?**
- Does it work with any app?**

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `scripts/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部包 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
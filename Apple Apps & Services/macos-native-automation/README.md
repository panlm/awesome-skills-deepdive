# macos-native-automation

> 使用 AppleScript/JXA 进行 macOS 原生自动化

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | macos-native-automation |
| **作者** | theagentwire |
| **ClawHub** | https://clawskills.sh/skills/theagentwire-macos-native-automation |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/theagentwire/macos-native-automation |
| **安全评级** | 🟢 Low (低风险) |

## 功能概述

- Paste the **full file path including filename** — macOS navigates to the directory and selects the file
- **Activate the target app first** before sending AppleScript keystrokes:

## 使用场景

CGEvent injects hardware-level HID mouse events directly into the macOS event stream, bypassing all application-layer filtering. Works where CDP .click(), JavaScript .click(), and AppleScript fail: file upload dialogs, React dropzones, native macOS prompts. Zero dependencies, Python 3 stdlib only.

## 依赖和前提条件

- Python 3
- macOS (AppleScript)

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | ⚪ Unknown |
| OpenClaw | 🟢 Benign |

> ⚠️ ClawHub 安全扫描未通过或状态未知，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 警告 | 执行 shell 命令: bash
# Click at screen coordinates (500, 300)
python3 scripts/macos_click.py click 500 300

# Get a window's position
python3 scripts/macos_click.py window "Safari"
# → Safari: x=0, y=38, w=1440, h=860

# Double-click, right-click, drag
python3 scripts/macos_click.py doubleclick 500 300
python3 scripts/macos_click.py rightclick 500 300
python3 scripts/macos_click.py drag 100 200 500 300
, bash
python3 scripts/macos_click.py window "Safari"
# → Safari: x=0, y=38, w=1440, h=860

python3 scripts/macos_click.py windows "Safari"
# → [0] x=0, y=38, w=1440, h=860  "GitHub - openclaw/openclaw"
# → [1] x=200, y=100, w=800, h=600  "Google"
, .

### 2. Screenshot + Measure (most reliable)

 |
| SEC-02 数据外泄 | 🟡 警告 | 调用已知服务 API 发送数据 |
| SEC-03 凭证获取 | 🟢 通过 | 不涉及任何凭证或密钥操作 |
| SEC-04 供应链风险 | 🟢 通过 | 无软件安装操作 |
| SEC-05 文件系统篡改 | 🟢 通过 | 无文件系统修改行为 |
| SEC-06 Prompt 注入 | 🟢 通过 | 指令清晰透明，无隐藏行为 |
| SEC-07 越权操作 | 🟢 通过 | 操作范围与声称功能一致 |
| SEC-08 持久化机制 | 🟢 通过 | 无持久化行为 |
| SEC-09 信息采集 | 🟢 通过 | 不收集系统/环境信息 |
| SEC-10 混淆/反分析 | 🟢 通过 | 所有指令清晰可读，无编码或间接执行 |

**综合评级: 🟢 Low (低风险)**

**风险摘要:** 发现 2 项警告，无严重风险。执行 shell 命令: bash
# Click at screen coordinates (5

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:44 UTC

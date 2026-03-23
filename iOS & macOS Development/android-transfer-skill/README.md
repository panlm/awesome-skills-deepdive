# android-transfer-skill

> 安全地从 macOS 向 Android 设备传输文件，支持校验和验证

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | android-transfer-skill |
| **作者** | aadipapp |
| **ClawHub** | https://clawskills.sh/skills/aadipapp-android-transfer-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/aadipapp/android-transfer-skill |
| **安全评级** | 🟢 Low |

## 功能概述
- SHA256 校验和验证确保文件完整性
- 覆盖保护，防止意外覆盖现有文件
- 路径清理，阻止目录遍历攻击
- 设备授权验证
- 多设备时自动选择第一个授权设备

## 使用场景
- 从 Mac 安全传输文件到 Android 手机
- 批量传输文件并验证完整性

## 依赖和前提条件
- Android Debug Bridge (adb)
- USB 调试已启用的 Android 设备
- Python 3

## 包含文件
SKILL.md（技能定义）, scripts/secure_transfer.py（安全传输脚本）

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 通过 subprocess 调用 adb 命令执行文件传输和校验 |
| SEC-02 数据外泄 | 🟢 Safe | 仅在本地设备间传输，无网络外传 |
| SEC-03 凭证获取 | 🟢 Safe | 未获取凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 仅依赖系统 adb 工具 |
| SEC-05 文件系统篡改 | 🟢 Safe | 写入 Android 设备指定路径，有路径清理保护 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 仅操作用户级文件传输 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 仅收集设备连接状态信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰，包含安全检查逻辑 |

**综合评级: 🟢 Low**
**风险摘要:** 安全设计良好的文件传输工具，包含校验和路径保护

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

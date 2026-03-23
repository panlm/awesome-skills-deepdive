# wopr-clock

> 复古 W.O.P.R. 风格倒计时时钟（战争游戏灵感），用于追踪 TACO 事件

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | wopr-clock |
| **作者** | seanweiyi |
| **ClawHub** | https://clawskills.sh/skills/seanweiyi-wopr-clock |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/seanweiyi/wopr-clock |
| **安全评级** | 🟢 Low |

## 功能概述
- 复古终端风格 UI（Tkinter）
- 实时倒计时到目标日期
- 跨平台支持（macOS/Windows/Linux）
- 磷光绿色显示效果
- 始终置顶窗口

## 使用场景
- 追踪 TACO 事件倒计时
- 桌面装饰复古终端时钟

## 依赖和前提条件
- Python 3
- tkinter

## 包含文件
SKILL.md, scripts/wopr_universal.py（主程序）

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 仅使用 tkinter 创建 GUI 窗口 |
| SEC-02 数据外泄 | 🟢 Safe | 无网络请求 |
| SEC-03 凭证获取 | 🟢 Safe | 未获取凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 仅使用标准库 tkinter |
| SEC-05 文件系统篡改 | 🟢 Safe | 不修改文件系统 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 仅使用系统时间 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰有趣 |

**综合评级: 🟢 Low**
**风险摘要:** 无害的桌面倒计时时钟小工具

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

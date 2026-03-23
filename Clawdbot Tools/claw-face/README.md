# claw-face

> AI 代理的浮动头像小部件，显示实时情绪、动作和视觉效果

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | claw-face |
| **作者** | mkoslacz |
| **ClawHub** | https://clawskills.sh/skills/mkoslacz-claw-face |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mkoslacz/claw-face |
| **安全评级** | 🟢 Low |

## 功能概述
- 9 种情绪 × 9 种动作 × 15+ 视觉特效 = 1215 种组合
- 机器人模式和面部模式两种显示
- 通过 JSON 状态文件控制
- Python + tkinter 实现
- 包含 auto-thinking hook
- CLI 和 API 双控制方式

## 使用场景
- 为 OpenClaw 代理添加可视化反馈
- 在专用屏幕上显示代理工作状态
- 提升 AI 助手的互动体验

## 依赖和前提条件
Python 3.10+, tkinter

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `hooks/clawface-thinking/HOOK.md`
- `hooks/clawface-thinking/handler.ts`
- `scripts/api.py`
- `scripts/avatar.py`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | Python 脚本执行，包含 tkinter GUI |
| SEC-02 数据外泄 | 🟢 Safe | 无网络通信 |
| SEC-03 凭证获取 | 🟢 Safe | 不涉及凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 仅依赖 Python 标准库 tkinter |
| SEC-05 文件系统篡改 | 🟡 Medium | 写入 ~/.clawface/avatar_state.json |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权操作 |
| SEC-08 持久化机制 | 🟡 Medium | 建议通过 nohup 后台运行，安装 hooks |
| SEC-09 信息采集 | 🟢 Safe | 仅读取状态文件 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰 |

**综合评级: 🟢 Low**
**风险摘要:** 本地 GUI 小部件，仅读写状态文件，安全风险极低

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

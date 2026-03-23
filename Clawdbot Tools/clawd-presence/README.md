# clawd-presence

> AI 代理的物理存在显示器，在专用终端显示字母组合图和状态

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | clawd-presence |
| **作者** | voidcooks |
| **ClawHub** | https://clawskills.sh/skills/voidcooks-clawd-presence |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/voidcooks/clawd-presence |
| **安全评级** | 🟢 Low |

## 功能概述
- 26 个字母的几何花纹设计
- 5 种状态（空闲/工作/思考/警报/休眠）
- 颜色编码状态显示
- 5 分钟自动回到空闲
- 支持自动检测 Clawdbot 配置
- curses 终端界面

## 使用场景
- 在专用屏幕上显示代理实时状态
- 替代聊天延迟的快速反馈
- 树莓派/旧笔记本做代理显示器

## 依赖和前提条件
Python 3.8+, 支持 256 色的终端

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `assets/monograms/A.txt`
- `assets/monograms/B.txt`
- `assets/monograms/C.txt`
- `assets/monograms/D.txt`
- `assets/monograms/E.txt`
- `assets/monograms/F.txt`
- `assets/monograms/G.txt`
- `assets/monograms/H.txt`
- `assets/monograms/I.txt`
- `assets/monograms/J.txt`
- `assets/monograms/K.txt`
- `assets/monograms/L.txt`
- `assets/monograms/M.txt`
- `assets/monograms/N.txt`
- `assets/monograms/O.txt`
- `assets/monograms/P.txt`
- `assets/monograms/Q.txt`
- `assets/monograms/R.txt`
- `assets/monograms/S.txt`
- `assets/monograms/T.txt`
- `assets/monograms/U.txt`
- `assets/monograms/V.txt`
- `assets/monograms/W.txt`
- `assets/monograms/X.txt`
- `assets/monograms/Y.txt`
- `assets/monograms/Z.txt`
- `scripts/configure.py`
- `scripts/display.py`
- `scripts/generate_monograms.py`
- `scripts/status.py`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 4 个 Python 脚本执行，含 curses 终端操作 |
| SEC-02 数据外泄 | 🟢 Safe | 无网络通信 |
| SEC-03 凭证获取 | 🟢 Safe | 不涉及凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 仅依赖 Python 标准库 |
| SEC-05 文件系统篡改 | 🟡 Medium | 写入 config.json 和 state.json |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化守护进程 |
| SEC-09 信息采集 | 🟡 Medium | configure.py --auto 读取 Clawdbot 配置文件 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰 |

**综合评级: 🟢 Low**
**风险摘要:** 本地终端显示工具，仅读写配置和状态文件

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

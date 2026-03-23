# clawd-modifier

> 修改 Claude Code 吉祥物 Clawd 的外观，包括颜色、手臂和配饰

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | clawd-modifier |
| **作者** | masonc15 |
| **ClawHub** | https://clawskills.sh/skills/masonc15-clawd-modifier |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/masonc15/clawd-modifier |
| **安全评级** | 🟡 Medium |

## 功能概述
- 更改 Clawd 颜色（预设/自定义 RGB）
- 添加手臂/帽子/配饰
- 提取当前 Clawd 状态
- 二进制文件修补
- 自动备份和恢复
- Unicode 字符参考

## 使用场景
- 自定义 Claude Code 终端吉祥物外观
- 修改 Clawd 颜色主题
- 添加节日装饰

## 依赖和前提条件
Python 3, Claude Code CLI (cli.js)

## 包含文件
- `SKILL.md`
- `_meta.json`
- `assets/clawd-variants.txt`
- `references/clawd-anatomy.md`
- `references/unicode-blocks.md`
- `scripts/extract_clawd.py`
- `scripts/patch_art.py`
- `scripts/patch_binary.py`
- `scripts/patch_color.py`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 4 个 Python 脚本直接修改 Claude Code 安装文件（cli.js 和二进制文件） |
| SEC-02 数据外泄 | 🟢 Safe | 无网络通信 |
| SEC-03 凭证获取 | 🟢 Safe | 不涉及凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 仅依赖 Python 标准库 |
| SEC-05 文件系统篡改 | 🔴 High | 直接修改 /opt/node22/.../cli.js 和编译二进制文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 修改系统级安装的 npm 包文件 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 仅读取 CLI 文件中的图案 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰，备份逻辑完善 |

**综合评级: 🟡 Medium**
**风险摘要:** 直接修改 Claude Code 安装文件，虽有备份机制但涉及系统路径写入

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

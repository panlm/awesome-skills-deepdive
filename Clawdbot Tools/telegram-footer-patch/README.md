# telegram-footer-patch

> 给 OpenClaw Telegram 私聊回复追加模型/思考/上下文尾注

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | telegram-footer-patch |
| **作者** | c-joey |
| **ClawHub** | https://clawskills.sh/skills/c-joey-telegram-footer-patch |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/c-joey/telegram-footer-patch |
| **安全评级** | 🟡 Medium |

## 功能概述
- Telegram 私聊消息追加尾注
- dry-run 预览模式
- 自动备份和恢复
- 语法校验（node --check）
- 升级后自动重打补丁
- 支持 text 和 html 两种格式

## 使用场景
- 在 Telegram 回复中显示模型信息
- 了解每条回复的思考级别和上下文
- OpenClaw 升级后重打补丁

## 依赖和前提条件
Python 3, Node.js, OpenClaw 安装目录写入权限

## 包含文件
- `CHANGELOG.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `scripts/patch_reply_footer.py`
- `scripts/revert_reply_footer.py`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | Python 脚本执行文件修改和 node --check |
| SEC-02 数据外泄 | 🟢 Safe | 无网络通信 |
| SEC-03 凭证获取 | 🟢 Safe | 不涉及凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 仅依赖 Python 和 Node.js |
| SEC-05 文件系统篡改 | 🔴 High | 直接修改 OpenClaw dist/ 目录下的 JS 文件 |
| SEC-06 Prompt 注入 | 🟡 Medium | 注入 JavaScript 代码到 OpenClaw 运行时 |
| SEC-07 越权操作 | 🟡 Medium | 修改 OpenClaw 核心运行文件 |
| SEC-08 持久化机制 | 🟢 Safe | 无守护进程，但补丁持久存在直到被覆盖 |
| SEC-09 信息采集 | 🟡 Medium | 注入的代码可访问 session 信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰，有 marker 标记 |

**综合评级: 🟡 Medium**
**风险摘要:** 直接修改 OpenClaw 运行时 JS 文件，注入代码能访问会话信息

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

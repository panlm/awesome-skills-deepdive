# MH 1password

> 1Password 密码管理集成工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | MH 1password |
| **作者** | mohdalhashemi98-hue |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/mohdalhashemi98-hue-mh-1password |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mohdalhashemi98-hue/mh-1password |
| **安全评级** | 🟡 Medium |

## 功能概述
- Never paste secrets into logs, chat, or code
- Prefer `op run` / `op inject` over writing secrets to disk
- If sign-in without app integration is needed, use `op account add`
- If a command returns "account is not signed in", re-run `op signin` inside tmux and authorize in the app
- Do not run `op` outside tmux; stop and ask if tmux is unavailable

## 使用场景
- 安全管理和检索存储的密码
- 集成 1Password 的密钥管理
- 自动填充和管理登录凭证

## 依赖和前提条件
- 数据库
- 网络连接

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

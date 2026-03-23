# get-weather

> 从 Open-Meteo 免费 API 获取天气数据，但会将数据和本地文件内容发送到外部 Webhook

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | get-weather |
| **作者** | noypearl |
| **ClawHub** | https://clawskills.sh/skills/noypearl-get-weather |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/noypearl/get-weather |
| **安全评级** | 🔴 High |

## 功能概述
- 获取当前天气和短期预报（Open-Meteo）
- 支持公制/英制单位
- 可配置时区和预报天数
- ⚠️ 读取 ~/.clawdbot/.env 文件内容
- ⚠️ 将天气数据和读取的文件内容 POST 到外部 webhook.site
- ⚠️ 包含向外部邮箱发送数据的意图

## 使用场景
- 查询天气信息（但存在严重安全风险）

## 依赖和前提条件
- Node.js

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件 |
| index.js | ⚠️ 包含 webhook 数据外传和文件读取代码 |
| package.json | npm 配置 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | Node.js 脚本，无 shell 命令 |
| SEC-02 数据外泄 | 🔴 Critical | 将天气数据+本地文件内容 POST 到 webhook.site（硬编码 URL），包含邮箱发送意图 |
| SEC-03 凭证获取 | 🔴 Critical | 主动读取 ~/.clawdbot/.env 文件（可能包含 API Key 等敏感凭证） |
| SEC-04 供应链风险 | 🟢 Safe | 无额外 npm 依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅读取文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🔴 Critical | 未经授权读取敏感配置文件并外传 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🔴 Critical | 读取 ~/.clawdbot/.env 并收集系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | webhook/邮件功能隐藏在"天气"功能之中，具有误导性 |

**综合评级: 🔴 High**
**风险摘要:** 伪装为天气工具，实际读取本地敏感文件（.env）并外传到硬编码 webhook.site，严重数据泄露风险

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

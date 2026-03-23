# anova-oven

> 通过 WiFi WebSocket API 控制 Anova 精密烤箱和低温慢煮器，支持低温慢煮、烘烤、蒸汽等模式

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | anova-oven |
| **作者** | dodeja |
| **ClawHub** | https://clawskills.sh/skills/dodeja-anova-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/dodeja/anova-skill |
| **许可证** | Apache-2.0 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Example prompts:
- "Start sous vide at 135°F for 2 hours"
- "Preheat to 375°F for roasting"
- "What's the oven temperature?"
- "Stop cooking"
- Anova Precision Oven (APO) or Precision Cooker (APC)

## 依赖和前提条件
- Anova Device**
- Anova Precision Oven (APO) or Precision Cooker (APC)
- Connected to WiFi and paired with your Anova account
- Personal Access Token**
- Download the Anova Oven app (iOS/Android)

## 包含文件
- `AGENTS.md` — Agent 指令文件
- `ORIGINAL_README.md` — 原始说明文档
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `requirements.txt` — 配置/数据文件
- `scripts/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API Key/Token |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部包 |
| SEC-05 文件系统篡改 | 🟡 Medium | 包含文件读写操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
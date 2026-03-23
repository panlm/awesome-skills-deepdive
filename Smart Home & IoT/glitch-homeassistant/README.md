# glitch-homeassistant

> 通过 Home Assistant REST API 控制智能家居设备

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | glitch-homeassistant |
| **作者** | chris6970barbarian-hue |
| **ClawHub** | https://clawskills.sh/skills/chris6970barbarian-hue-glitch-homeassistant |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/chris6970barbarian-hue/glitch-homeassistant |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- One-command setup: `ha-cli setup <url> <token>`
- Natural commands: `ha-cli on living room` or `ha-cli living room on`
- Smart fuzzy matching: "bed" finds "Bedroom Light", "Bedroom AC"
- Auto-config save: Credentials stored in config.json
- Any device type: Lights, switches, covers, climate, locks, scenes, scripts

## 依赖和前提条件
- Natural commands**: `ha-cli on living room` or `ha-cli living room on`
- Smart fuzzy matching**: "bed" finds "Bedroom Light", "Bedroom AC"
- Auto-config save**: Credentials stored in config.json
- Any device type**: Lights, switches, covers, climate, locks, scenes, scripts

## 包含文件
- `ORIGINAL_README.md` — 原始说明文档
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `config.json` — 配置/数据文件

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API Key/Token |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
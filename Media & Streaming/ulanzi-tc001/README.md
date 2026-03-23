# Ulanzi TC001

> Control the Ulanzi TC001 (Pixel Clock) over local HTTP. Use to list tc1/tc001 commands, read status, enable/disable gadgets (time/date/youtube/matrix/etc.), or change settings like brightness, night mode, timezone, switch speed, or scroll speed. Trigger on commands starting with “tc1” or “tc001”.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Ulanzi TC001 |
| **作者** | felipeouropreto |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/felipeouropreto-ulanzi-tc001 |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/felipeouropreto/ulanzi-tc001 |
| **安全评级** | 🟢 Low |

## 功能概述
- `status` → JSON summary (sys settings + gadgets on/off)
- `gadgets list|on|off`
- `gadget on|off <name>`
- `brightness auto | manual <0-100>`
- `nightmode on|off | start HH:MM | end HH:MM`
- `timezone GMT-3 | AUTO` (see mapping in script)

## 使用场景
- 多媒体内容管理
- 流媒体服务控制
- 媒体库组织和搜索

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `config.json`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；信息采集：读取环境变量或系统信息

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
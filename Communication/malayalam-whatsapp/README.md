# Malayalam Language Skill (മലയാളം)

> 处理 WhatsApp 收到的马拉雅拉姆语和 Manglish（马拉雅拉姆语罗马化）消息并进行智能回复

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Malayalam Language Skill (മലയാളം) |
| **作者** | babuperumana |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/babuperumana-malayalam-whatsapp |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/babuperumana/malayalam-whatsapp |
| **安全评级** | 🟢 Low |

## 功能概述
- 马拉雅拉姆语消息识别和理解
- Manglish（罗马化马拉雅拉姆语）文本解析
- 自动翻译马拉雅拉姆语消息为可理解内容
- 智能生成马拉雅拉姆语回复
- WhatsApp 消息自动处理

## 使用场景
- 自动回复 WhatsApp 中的马拉雅拉姆语消息
- 帮助非马拉雅拉姆语用户理解收到的消息内容
- 跨语言 WhatsApp 沟通的智能翻译助手

## 依赖和前提条件
- WhatsApp 账户和消息接入配置
- OpenClaw WhatsApp 集成

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 未发现明显安全风险，文档透明可审计

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

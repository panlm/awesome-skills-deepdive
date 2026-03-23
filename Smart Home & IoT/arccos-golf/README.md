# arccos-golf

> 分析 Arccos Golf 传感器的高尔夫表现数据，包括杆距、得分模式和表现趋势

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | arccos-golf |
| **作者** | pfrederiksen |
| **ClawHub** | https://clawskills.sh/skills/pfrederiksen-arccos-golf |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/pfrederiksen/arccos-golf |
| **许可证** | MIT |
| **安全评级** | 🟡 Medium |

## 功能概述
- Your Arccos email and password are used to obtain a session token
- The token is cached at `~/.arccos_creds.json` (permissions 0600)
- Live API calls are made to `authentication.arccosgolf.com` and `api.arccosgolf.com`
- An external Python library (`arccos`) is installed from GitHub
- Review the `arccos` library source before installing: <https://github.com/pfrederiksen/arccos-api>
- Strokes Gained breakdown — overall, driving, approach, short game, putting

## 依赖和前提条件
- Your Arccos email and password are used to obtain a session token
- The token is cached at `~/.arccos_creds.json` (permissions 0600)
- Live API calls are made to `authentication.arccosgolf.com` and `api.arccosgolf.com`
- 
- Python ≥ 3.11

## 包含文件
- `ORIGINAL_README.md` — 原始说明文档
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `scripts/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部包 |
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
# Json Repair Kit

> Repair malformed JSON files by normalizing them through Node.js evaluation. Use this to fix trailing commas, single quotes, unquoted keys, or other common syntax errors in JSON files (e.g. config files, manually edited data).

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Json Repair Kit |
| **作者** | wanng-ide |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/wanng-ide-json-repair-kit |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/wanng-ide/json-repair-kit |
| **安全评级** | 🟢 Low |

## 功能概述
- Trailing Commas: `{"a": 1,}` -> `{"a": 1}`
- Single Quotes: `{'a': 'b'}` -> `{"a": "b"}`
- Unquoted Keys: `{key: "value"}` -> `{"key": "value"}`
- Comments: Removes JS-style comments `//` (if parser supports it, standard Node `eval` may strip them if they are line co
- Hex/Octal Numbers: `0xFF` -> `255`
- Backup: Always creates a `.bak` file before overwriting (unless `--no-backup` is used, but default is safe).

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `SKILL.md`
- `_meta.json`
- `index.js`
- `package.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
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
**风险摘要:** 1 项中风险。命令执行：存在命令执行相关引用

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
# Smart File Organizer

> A skill that enables Claw to scan a directory, categorize files by type and content, and reorganize them into a clean, logical folder structure.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Smart File Organizer |
| **作者** | underbench2-gif |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawskills.sh/skills/underbench2-gif-ub2-smart-file-organizer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/underbench2-gif/ub2-smart-file-organizer |
| **安全评级** | 🟢 Low |

## 功能概述
- "Organize my Downloads folder by file type"
- "Scan this project directory and find all duplicate files"
- "Sort these files into folders by year based on their modification date"
- "Clean up this directory — group documents, images, and code separately"
- Dry Run Mode — Preview the proposed changes before any files are moved (enabled by default)
- Change Log — Every file move is logged to `reorganization_log.txt` for full traceability

## 使用场景
- 管理 macOS/iOS 日历事件
- 查询日程安排与空闲时间
- 通过命令行创建/修改日历事件

## 包含文件
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
# Upload files to catbox.moe (permanent) or litterbox.catbox.moe (temporary).

> Upload files to catbox.moe (permanent) or litterbox.catbox.moe (temporary).

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Upload files to catbox.moe (permanent) or litterbox.catbox.moe (temporary). |
| **作者** | microck |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/microck-catbox-upload |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/microck/catbox-upload |
| **安全评级** | 🟢 Low |

## 功能概述
- `--service`: `litterbox` (default) or `catbox`
- `--time`: Litterbox expiration: `1h`, `12h`, `24h`, `72h` (default: `24h`)
- `--userhash`: Catbox account hash (optional, required for tracking)

## 使用场景
- 营销活动管理和执行
- 客户获取和转化
- 销售流程优化

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `requirements.txt`
- `upload.py`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 存在 1 项高风险，0 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
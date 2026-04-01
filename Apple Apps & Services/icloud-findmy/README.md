# icloud-findmy

> 通过 iCloud 查找我的设备定位 Apple 设备

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | icloud-findmy |
| **作者** | liamnichols |
| **ClawHub** | https://clawskills.sh/skills/liamnichols-icloud-findmy |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/liamnichols/icloud-findmy |
| **许可证** | 未指定 |
| **安全评级** | 🔴 High |

## 功能概述
- Query iCloud Find My for device locations
- Check battery levels and charging status
- Monitor family devices
- Provide proactive battery warnings
- macOS (for iCloud API access)
- PyiCloud installed via pipx

## 依赖和前提条件
- macOS (for iCloud API access)
- Apple ID with Find My enabled
- Family Sharing (optional, for family devices)

## 包含文件
- `ORIGINAL_README.md` — 原始说明文档
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在动态代码执行 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部包 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🔴 High | 包含代码混淆或动态执行 |

**综合评级: 🔴 High**
**风险摘要:** 存在多项高风险问题，使用前需仔细评估

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
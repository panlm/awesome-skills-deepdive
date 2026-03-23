# Blucli

> 蓝牙设备命令行管理工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Blucli |
| **作者** | steipete |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/steipete-blucli |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/steipete/blucli |
| **安全评级** | 🟢 Low |

## 功能概述
- config default (if set)
- Grouping: `blu group status|add|remove`
- TuneIn search/play: `blu tunein search "query"`, `blu tunein play "query"`

## 使用场景
- 扫描和管理蓝牙设备连接
- 监控蓝牙设备状态
- 执行蓝牙设备配对和控制

## 依赖和前提条件
- 数据库
- 网络连接

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。数据外泄：存在外部 API 调用

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

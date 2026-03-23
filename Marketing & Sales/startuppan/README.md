# StartupPan

> 创业项目管理和规划工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | StartupPan |
| **作者** | lifeissea |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/lifeissea-startuppan |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/lifeissea/startuppan |
| **安全评级** | 🔴 High |

## 功能概述
- 创业项目规划
- 商业模型设计
- 里程碑管理
- 创业资源整合

## 使用场景
- 为创业项目制定系统化的发展规划
- 管理创业项目的关键里程碑和任务

## 依赖和前提条件
- API 密钥
- Python 运行环境

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
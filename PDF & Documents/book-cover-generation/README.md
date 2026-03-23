# Book Cover Generation

> AI 驱动的书籍封面设计生成工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Book Cover Generation |
| **作者** | eftalyurtseven |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/eftalyurtseven-book-cover-generation |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/eftalyurtseven/book-cover-generation |
| **安全评级** | 🟡 Medium |

## 功能概述
- 自动生成书籍封面设计
- AI 创意图像生成
- 支持自定义尺寸和风格
- 多种设计模板选择

## 使用场景
- 为电子书项目快速生成专业封面
- AI 辅助设计多种风格的书籍封面

## 依赖和前提条件
- API 密钥

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `references`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
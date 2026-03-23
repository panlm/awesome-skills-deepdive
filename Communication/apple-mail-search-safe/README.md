# Apple Mail Search Safe (fruitmail)

> macOS Apple Mail 邮件搜索工具，支持快速元数据检索和全文内容查找

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Apple Mail Search Safe (fruitmail) |
| **作者** | gumadeiras |
| **版本** | 5.0.4 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/gumadeiras-apple-mail-search-safe |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/gumadeiras/apple-mail-search-safe |
| **安全评级** | 🟢 Low |

## 功能概述
- 搜索 Apple Mail 邮箱中的邮件
- 支持元数据快速检索（发件人、主题、日期等）
- 全文内容搜索能力
- 安全的只读访问模式
- 搜索结果格式化输出

## 使用场景
- 在 macOS 上快速查找特定邮件内容
- 智能体辅助用户检索历史邮件信息
- 邮件归档中的关键信息定位

## 依赖和前提条件
- macOS 系统环境
- Apple Mail 已配置邮箱账号
- 授予 Apple Mail 数据访问权限

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

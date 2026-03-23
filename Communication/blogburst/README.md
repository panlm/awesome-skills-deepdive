# BlogBurst - Virtual CMO Agent

> AI 首席营销官智能体，自主运行完整营销引擎，支持博客内容自动生成、优化和多渠道发布

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | BlogBurst - Virtual CMO Agent |
| **作者** | shensi8312 |
| **版本** | 3.1.2 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/shensi8312-blogburst |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/shensi8312/blogburst |
| **安全评级** | 🔴 High |

## 功能概述
- 自动生成高质量博客文章和营销内容
- SEO 优化，提升内容搜索引擎排名
- 多渠道内容发布和分发
- 营销策略自主规划和执行
- 内容日历管理和定时发布
- 受众分析和内容效果追踪
- 支持多种内容格式和风格定制

## 使用场景
- 中小企业用 AI 自动化运营整个内容营销流程
- 创业者零人力维护公司博客和社交媒体内容更新
- 营销团队借助 AI 批量生成多语言推广素材

## 依赖和前提条件
- 配置博客发布平台的 API 访问权限
- 设定营销目标和内容策略参数
- 已连接目标发布渠道（WordPress、Medium 等）

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

# Latent Press

> AI 出版和内容创作平台工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Latent Press |
| **作者** | jestersimpps |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/jestersimpps-latent-press |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jestersimpps/latent-press |
| **安全评级** | 🔴 High |

## 功能概述
- AI 辅助内容创作和出版
- 文档排版和格式化
- 出版流程自动化
- 多格式输出支持

## 使用场景
- 将创作内容通过 AI 辅助排版出版
- 自动化处理出版流程中的格式转换

## 依赖和前提条件
- API 密钥
- Supabase

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `references`
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
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，4 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
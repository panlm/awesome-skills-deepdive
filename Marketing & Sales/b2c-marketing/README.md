# B2C Mobile App Marketing Coach

> B2C 消费者营销工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | B2C Mobile App Marketing Coach |
| **作者** | jackfriks |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/jackfriks-b2c-marketing |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jackfriks/b2c-marketing |
| **安全评级** | 🟡 Medium |

## 功能概述
- B2C 营销策略制定
- 消费者画像分析
- 营销活动管理
- 效果追踪和优化

## 使用场景
- 制定面向消费者的精准营销策略
- 管理和优化 B2C 营销活动的全流程

## 依赖和前提条件
- API 密钥
- Bearer Token
- FFmpeg
- GitHub API
- Instagram API
- TikTok API

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
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
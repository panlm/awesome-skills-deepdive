# Kiro X Publisher

> X (Twitter) 智能内容发布工具，自动发现热门话题、丰富推文内容并发布精选帖子

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Kiro X Publisher |
| **作者** | vmining |
| **版本** | 1.1.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/vmining-kiro-x-publisher |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/vmining/kiro-x-publisher |
| **安全评级** | 🔴 High |

## 功能概述
- 自动发现和追踪 X 平台热门话题
- 逐条分析和丰富推文内容
- 基于评分算法筛选高质量信号
- 自动生成话题总结和洞察
- 发布精选内容到 X 账户
- 支持内容策略和发布节奏配置

## 使用场景
- 自媒体运营者自动化 X 平台内容策划和发布
- 品牌营销团队追踪热点并快速响应
- 个人用户打造高质量的 X 内容输出

## 依赖和前提条件
- X (Twitter) 开发者账户和 API 凭据
- OpenClaw 运行环境

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `examples`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23

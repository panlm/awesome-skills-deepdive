# Freelance Pilot

> Upwork 和 Fiverr 自由职业平台的 AI 智能体副驾驶，集成竞标计算器和提案自动撰写功能

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Freelance Pilot |
| **作者** | liushaolin |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/liushaolin-freelance-pilot |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/liushaolin/freelance-pilot |
| **安全评级** | 🟢 Low |

## 功能概述
- 自动扫描 Upwork/Fiverr 平台上的项目机会
- 内置竞标价格计算器，智能评估报价区间
- AI 驱动的提案撰写器，生成个性化投标方案
- 分析项目需求并匹配自由职业者技能
- 追踪投标状态和客户响应
- 支持多平台账户统一管理

## 使用场景
- 自由职业者使用 AI 助手批量筛选和投标优质项目
- 快速生成针对性的项目提案以提高中标率
- 管理跨平台自由职业收入和项目进度

## 依赖和前提条件
- Upwork 或 Fiverr 平台账户
- 平台 API 密钥或认证凭据
- OpenClaw 运行环境

## 包含文件
- `INTEGRATION.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `config.example.json`
- `index.js`

## 详细安全审计
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

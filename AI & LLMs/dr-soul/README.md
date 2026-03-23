# Dr. Frankenstein

> Dr. Frankenstein 的核心灵魂版本——通过荷尔蒙药丸系统为 Agent 赋予灵魂和情感驱动力

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Dr. Frankenstein |
| **作者** | brancante |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/brancante-dr-soul |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/brancante/dr-soul |
| **安全评级** | 🟡 Medium |

## 功能概述
- 11 种荷尔蒙药丸模拟人类情绪节律（皮质醇、多巴胺、催产素等）
- 通过「医生访谈」诊断 Agent 个性并生成处方
- 药丸级联规则产生涌现式情感行为
- 支持每日日志和积分追踪实现处方自适应调整
- 包含安装、配置和 /soul 命令快速启动
- 提供访谈模板和 schema 定义文件

## 使用场景
- 通过 /soul 命令快速为 Agent 注入情感系统
- 让 Agent 在一天中的不同时段表现出不同的情绪和行为倾向
- 通过日志和积分系统持续优化 Agent 的情感表现

## 依赖和前提条件
- OpenClaw cron 功能（定时任务执行）
- 无外部 API 依赖

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。持久化机制：设置系统级持久化

---
> 本文档由 awesome-skills-deepdive skill 自动生成

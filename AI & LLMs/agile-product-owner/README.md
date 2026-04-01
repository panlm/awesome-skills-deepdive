# Agile Product Owner

> 敏捷产品负责人工具包，涵盖需求管理、用户故事编写和 Sprint 规划

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agile Product Owner |
| **作者** | alirezarezvani |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/alirezarezvani-agile-product-owner |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/agile-product-owner |
| **安全评级** | 🟢 Low |

## 功能概述
- 按照 INVEST 原则生成高质量用户故事
- 使用 Given-When-Then 模式编写验收标准
- 提供 Epic 拆解工作流，将大需求分解为可执行故事
- 支持 Sprint 规划：容量计算、速率追踪、故事点估算
- 提供需求优先级排序框架（MoSCoW、WSJF 等）
- 内置参考文档和最佳实践模板

## 使用场景
- 从模糊需求中快速生成符合 INVEST 原则的用户故事和验收标准
- 进行 Sprint 规划时计算团队容量、分配故事点
- 将大型 Epic 系统化拆解为可交付的用户故事

## 依赖和前提条件
- 无外部依赖，纯提示词驱动的 Skill

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。凭证获取：需要 API 密钥或令牌；越权操作：涉及权限相关操作

---
> 本文档由 awesome-skills-deepdive skill 自动生成

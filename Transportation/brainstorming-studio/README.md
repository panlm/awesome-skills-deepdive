# Idea Forge Orchestrator

> 头脑风暴工作室，提供结构化的创意发散和收敛工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Idea Forge Orchestrator |
| **作者** | myboxstorage |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/myboxstorage-brainstorming-studio |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/myboxstorage/brainstorming-studio |
| **安全评级** | 🟡 Medium |

## 功能概述
- 结构化头脑风暴流程引导
- 支持多种创意激发技巧（如六顶思考帽、SCAMPER）
- 创意评估和筛选框架
- 生成创意报告和行动方案

## 使用场景
- 团队新产品创意头脑风暴会议引导
- 针对特定问题使用多种方法生成解决方案

## 依赖和前提条件
- Node.js / npm

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 4 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；Prompt 注入：存在可疑 Prompt 模式

> 本文档由 awesome-skills-deepdive skill 自动生成

# Free Ride - Unlimited free AI

> 管理 OpenRouter 上的免费 AI 模型，自动排名和切换最优免费模型

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Free Ride - Unlimited free AI |
| **作者** | shaivpidadi |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/shaivpidadi-free-ride |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/shaivpidadi/free-ride |
| **安全评级** | 🟡 Medium |

## 功能概述
- 自动发现和排名 OpenRouter 上的免费 AI 模型
- 根据性能指标自动切换最优模型
- 管理免费模型的使用配额和限制
- 支持多模型轮替以规避速率限制

## 使用场景
- 零成本使用 AI 模型——自动选择最佳免费选项
- 在免费配额用尽时自动切换到替代模型

## 依赖和前提条件
- OpenRouter 账号

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

> 本文档由 awesome-skills-deepdive skill 自动生成

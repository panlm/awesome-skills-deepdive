# Doctorbot Ci Validator

> 离线验证 GitHub Actions、GitLab CI 和 Keep 工作流文件，精准定位语法和 Schema 错误

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Doctorbot Ci Validator |
| **作者** | bamontejano |
| **版本** | 1.0.0 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/bamontejano-skill-doctorbot-ci-validator |

## 功能概述
- 专为 Keep（AIOps）工作流提供离线验证，使用 Mock 技术绕过数据库等环境依赖
- 通用 YAML 语法快速检查，支持 GitHub Actions、GitLab CI、CircleCI 等
- 精确定位工作流中将会失败的具体位置
- 支持验证单个文件或整个目录
- 无需 Docker 容器或在线环境，即时完成验证
- 适用于 pre-commit 钩子、CI/CD 流水线和 Agent 代码生成验证

## 使用场景
- 在提交代码前预先验证 CI/CD 工作流配置文件的正确性
- AI Agent 生成工作流配置后，自动验证其有效性再提交建议
- 在 CI/CD 流水线中集成离线验证步骤，避免因配置错误导致生产失败

## 依赖和前提条件
- Python 3（用于运行验证脚本）
- 通过 ClawHub 安装：`openclaw install doctorbot-ci-validator`

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
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive skill 自动生成

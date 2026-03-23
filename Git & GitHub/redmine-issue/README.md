# Redmine Issue

> 通过 REST API 读取和管理任意 Redmine 服务器上的 Issue

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Redmine Issue |
| **作者** | guoway |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/guoway-redmine-issue |

## 功能概述
- 获取单个 Redmine Issue 的详细信息
- 列表查询和过滤 Issue：按项目、状态、指派人等条件筛选
- 更新 Issue：修改状态、指派人、优先级、完成度，添加备注
- 支持排序和分页
- JSON 格式输出，便于自动化处理
- 支持多 Redmine 实例部署（通过环境变量配置）

## 使用场景
- 在命令行中快速查看和更新 Redmine Issue，无需打开浏览器
- 批量查询和过滤项目中的 Issue，了解项目进度
- 集成到自动化工作流中实现 Issue 的程序化管理

## 依赖和前提条件
- Node.js
- 环境变量 `REDMINE_URL`（如 `https://redmine.example.com`）
- 认证方式（二选一）：`REDMINE_API_KEY` 或 `REDMINE_USERNAME` + `REDMINE_PASSWORD`

## 安全状态
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
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
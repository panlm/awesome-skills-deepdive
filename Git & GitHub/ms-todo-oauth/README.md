# Ms Todo Oauth

> 通过 Microsoft Graph API 管理 Microsoft To Do 任务的完整命令行工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Ms Todo Oauth |
| **作者** | nathanatgit |
| **版本** | 1.0.3 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/nathanatgit-ms-todo-oauth |

## 功能概述
- 完整的任务生命周期管理：创建、完成、删除、搜索任务
- 支持多任务列表的创建和管理
- 丰富的任务选项：优先级、截止日期、提醒、描述、标签
- 支持循环任务（每日、每周、每月模式及自定义间隔）
- 多种视图模式：今日任务、逾期任务、待处理任务、统计信息
- 跨列表全局搜索功能
- 任务数据导出为 JSON 格式
- 包含 29 个自动化测试用例确保可靠性
- 完整支持中文字符和 Emoji 表情

## 使用场景
- 在命令行中高效管理 Microsoft To Do 任务，无需打开浏览器
- 批量操作任务（创建、完成、导出），提升生产力
- 集成到自动化工作流中实现任务的程序化管理

## 依赖和前提条件
- Python >= 3.9
- 需要创建 Python 虚拟环境并安装依赖（`pip install`）
- 需要网络访问 Microsoft Graph API
- 需要 Microsoft 账户（个人或工作/学校账户）
- OAuth2 认证（首次使用需通过浏览器登录）
- 内置 Azure Client ID 和 Secret ID（建议替换为自己的以保护隐私）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 4 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
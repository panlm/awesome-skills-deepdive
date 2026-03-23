# N2 Stitch MCP

> Google Stitch 的弹性 MCP 代理，三层安全保障（自动重试、Token 刷新、TCP 断连恢复）

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | N2 Stitch MCP |
| **作者** | choihyunsus |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/choihyunsus-n2-stitch-mcp |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/choihyunsus/n2-stitch-mcp |
| **安全评级** | 🟡 Medium |

## 功能概述
- 解决 Google Stitch API 在 60 秒后断开 TCP 连接的问题
- 三层安全保障：自动重试、Token 刷新、TCP 断连恢复
- 支持 create_project、list_projects、get_project 等项目管理操作
- 支持 list_screens、get_screen 等屏幕管理操作
- 支持从文本生成屏幕（generate_screen_from_text）
- 确保长时间运行的生成任务不会因网络断开而丢失

## 使用场景
- 使用 Google Stitch 进行 UI 屏幕自动生成，无惧网络不稳定
- 在 MCP 协议下管理 Stitch 项目和屏幕资源

## 依赖和前提条件
- Google Stitch 账户和 API 访问权限
- MCP 协议支持

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
